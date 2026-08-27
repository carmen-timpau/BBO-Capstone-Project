""" Week 11 Next Query Prediction Module
--------------------------------------------------------------------------------------------------------
Predicting the next query point for each function (1–8) using global GP modelling, acquisition‑function 
scoring and a more advanced Sobol candidate sampling strategy, via sampling within both the full input 
domain space and the best K‑means cluster’s local bounding box (Sobol density‑enhanced).

1. Global GP training on the full output‑warped function datasets, using the winning kernel selected for
each function during the full joint kernel x acquisition ablation study performed earlier in the pipeline. 

2. Advanced Sobol candidate pools generation:
- a full‑domain Sobol pool, sized according to input dimensionality;
- a controlled density‑enhanced local‑box Sobol pool, restricted to the best cluster’s bounding box.

3. Sobol candidate scoring using the winning acquisition function selected for each function during the 
full joint kernel x acquisition ablation study performed earlier in the pipeline. 

4. Next‑query point prediction per function = argmax acquisition candidate, unwarped to original scale.

Detailed diagnostics per function are reported, including best full‑domain score, best local‑box score,
volume ratio, candidate counts, and predicted GP values/stds for the best candidate in each pool. 
"""

import numpy as np
from scipy.stats.qmc import Sobol
from scipy.spatial.distance import cdist
from sklearn.preprocessing import StandardScaler
from sklearn.gaussian_process import GaussianProcessRegressor

from output_warping.output_warping import apply_output_warping_to_dataset
from output_unwarping.output_unwarping import unwarp_predictions_and_values
from full_ablation.acq_strategies import acq_strategies
from full_ablation.acquisition import compute_acquisition_scores


def is_noiseless_kernel(kernel):
    """Returns True if the kernel has no WhiteKernel component."""
    return "WhiteKernel" not in str(kernel)


def run_next_query_prediction(
    data,
    sequential_ablation_summary,
    kernel_suites_dict,
    on_random_baseline="sample_random",
    min_distance_to_existing=0.0,
    sobol_seed_base=42,
    kmeans_results=None,
    secondary_pool_extra_bits=2,
    m_box_min=6, # m_box_min = floor on the box pool's Sobol bit-count (default 6 i.e. >=64 candidates),
                 # so that even a very small/high-dim box still gets enough candidates to be useful.
    m_box_max_offset=4 # m_box_max_offset = cap on how many more bits than the full-domain pool the box pool can
                       # use (default 4 -> box pool capped at 16x the full-domain pool's candidate count), so a
                       # weakly-restricted box (large volume_ratio) doesn't blow up compute unnecessarily.
):
    """
    Predicting the next query point per function from acquisition function scores computed within both full-domain 
    and density-enhanced <best KMeans cluster> local-box space, post global GP training on full function datasets.

    The local-box Sobol pool's candidate count is initially density-matched to the full-domain pool before applying 
    secondary_pool_extra_bits as a resolution boost for density-enhancement, instead of always getting a flat 
    +secondary_pool_extra_bits over the full-domain pool's bit count regardless of the box's actual volume.
    
    This was done because a small box could end up 50-100x denser than the full-domain pool purely from geometry, 
    which would bias the argmax toward the box for nearly every function (an undesired artifact of scoring more/denser 
    candidates, which would not be direct evidence that the box region's acquisition surface is genuinely better, 
    but only that the full-space region is greatly underresolved in comparison to it).

    [Diagnostics] printed and returned per function:
        "Best Full-Domain Score", "Best Local-Box Score" (None if no box pool was generated),
        "Volume Ratio" (box volume / full-domain volume, None if no box), "Box Candidate Count".

    Returns: {fn_key: {"Next Query Coordinates", "Winning Kernel", "Winning Acquisition",
                        "Predicted Original Scale Value", "Predicted Std (warped scale)",
                        "Chosen From Pool", "N Candidates Full Domain", "N Candidates Local Box",
                        "Volume Ratio", "Best Full-Domain Score", "Best Local-Box Score"}}
    """
    warped_data, warpers = apply_output_warping_to_dataset(data)
    next_queries_results = {}

    print("\n" + "=" * 115)
    print(" COMPILING FINAL HEBO & SOBOL-BASED NEXT QUERY PREDICTIONS ACROSS FUNCTIONS 1-8")
    print("=" * 115)

    for fn_idx in range(1, 9):
        fn_key = f"function_{fn_idx}"
        if fn_key not in warped_data:
            continue

        X_full = np.array(warped_data[fn_key]["x"])
        Y_target = np.array(warped_data[fn_key]["y_target"])
        n_samples, n_dims = X_full.shape

        ablation_info = sequential_ablation_summary.get(fn_key, {})
        winning_kernel_name = ablation_info.get("Best Kernel")
        best_acq_variant = ablation_info.get("Best Acquisition", "Expected Improvement (xi=0.01)")

        if winning_kernel_name is None:
            print(f"  [WARNING] No 'Best Kernel' found in sequential_ablation_summary for {fn_key} "
                  f"- make sure run_full_joint_ablation was run for this function.")

        is_random_baseline = (best_acq_variant == "Random Baseline")
        acq_warning = None

        if is_random_baseline:
            if on_random_baseline == "sample_random":
                acq_type, param = "random", None
            elif on_random_baseline == "fallback_best_nonrandom":
                acq_type, param = "EI", 0.01
                acq_warning = (f"Ablation winner for {fn_key} was 'Random Baseline'; "
                                f"on_random_baseline='fallback_best_nonrandom' -> using EI(xi=0.01) instead.")
            else:
                raise ValueError(f"Unknown on_random_baseline option: {on_random_baseline}")
        elif best_acq_variant not in acq_strategies:
            acq_type, param = "EI", 0.01
            acq_warning = (f"Acquisition variant '{best_acq_variant}' for {fn_key} not found in "
                            f"acq_strategies - falling back to EI(xi=0.01).")
        else:
            acq_type, param = acq_strategies[best_acq_variant]

        if acq_warning:
            print(f"  [WARNING] {acq_warning}")

        # GP trained globally on the full dataset
      
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_full)

        kernel_suite = kernel_suites_dict.get(fn_key, {})
        best_kernel = kernel_suite.get(winning_kernel_name)
        if best_kernel is None:
            print(f"  [WARNING] Kernel '{winning_kernel_name}' not found in kernel_suites_dict for "
                  f"{fn_key} - falling back to first available kernel.")
            best_kernel = list(kernel_suite.values())[0]
            winning_kernel_name = list(kernel_suite.keys())[0]

        alpha_value = 1e-8 if is_noiseless_kernel(best_kernel) else 0.0
        gp = GaussianProcessRegressor(
            kernel=best_kernel,
            alpha=alpha_value,
            normalize_y=True,
            n_restarts_optimizer=10,
            random_state=42
        )
        gp.fit(X_scaled, Y_target)

        # Primary pool: generating full-domain Sobol candidates
      
        minimum = X_full.min(axis=0)
        maximum = X_full.max(axis=0)

        if n_dims >= 6:
            m_samples = 14
        elif n_dims >= 4:
            m_samples = 13
        else:
            m_samples = 12

        sobol_seed = sobol_seed_base + n_samples
        sobol_full = Sobol(d=n_dims, scramble=True, seed=sobol_seed)
        unit_samples_full = sobol_full.random_base2(m=m_samples)
        x_grid_full = minimum + unit_samples_full * (maximum - minimum)
        full_domain_count = len(x_grid_full)

        # Secondary pool: Generating density-matched Sobol candidates restricted to the best K-means
        # cluster's bounding box, applied only if kmeans_results shows real cluster structure (best_k>1)
      
        n_candidates_box = 0
        volume_ratio = None
        pool_source_labels = ["full-domain"] * len(x_grid_full)

        if kmeans_results is not None and fn_key in kmeans_results:
            fn_kmeans_info = kmeans_results[fn_key]
            if fn_kmeans_info.get("best_k", 1) > 1:
                box_min, box_max = fn_kmeans_info["bounding_box"]

                # Computing volume ratio in log-space for numerical stability at higher dimensionality
              
                log_full_vol = np.sum(np.log(np.maximum(maximum - minimum, 1e-300)))
                log_box_vol = np.sum(np.log(np.maximum(box_max - box_min, 1e-300)))
                volume_ratio = float(np.exp(np.clip(log_box_vol - log_full_vol, -700, 0)))

                # Local-box density-matching with full-space
                density_matched_count = full_domain_count * volume_ratio
              
                # Controlled local-box density-enhancement
                target_box_count = density_matched_count * (2 ** secondary_pool_extra_bits)
              
                m_box = int(np.clip(
                    np.ceil(np.log2(max(target_box_count, 1))),
                    m_box_min, m_samples + m_box_max_offset
                ))

                sobol_box = Sobol(d=n_dims, scramble=True, seed=sobol_seed + 777)
                unit_samples_box = sobol_box.random_base2(m=m_box)
                x_grid_box = box_min + unit_samples_box * (box_max - box_min)
                n_candidates_box = len(x_grid_box)

                x_grid = np.vstack([x_grid_full, x_grid_box])
                pool_source_labels = pool_source_labels + ["local-box"] * n_candidates_box

                implied_density_x = (n_candidates_box / max(density_matched_count, 1e-12))
                print(f"  [LOCAL POOL] {fn_key}: box occupies {volume_ratio:.4%} of the full-domain "
                      f"volume -> density-matched baseline would be "
                      f"{density_matched_count:.1f} candidates; using {n_candidates_box} box "
                      f"candidates (~{implied_density_x:.1f}x that baseline, i.e. genuinely "
                      f"~{implied_density_x:.1f}x denser than the full-domain pool, not the "
                      f"uncontrolled ~{(2**secondary_pool_extra_bits)/max(volume_ratio,1e-12):.0f}x "
                      f"it would have been without density-matching), combined with "
                      f"{full_domain_count} full-domain candidates.")
            else:
                x_grid = x_grid_full
        else:
            x_grid = x_grid_full

        pool_source_labels = np.array(pool_source_labels)
        x_grid_scaled = scaler.transform(x_grid)

        if min_distance_to_existing > 0:
            dist_to_existing = cdist(x_grid_scaled, X_scaled)
            min_dist_per_candidate = dist_to_existing.min(axis=1)
            keep_mask = min_dist_per_candidate >= min_distance_to_existing

            if keep_mask.sum() == 0:
                print(f"  [WARNING] All Sobol candidates for {fn_key} were within "
                      f"min_distance_to_existing={min_distance_to_existing} of an existing point "
                      f"- domain may be densely sampled relative to this threshold. "
                      f"Falling back to the unfiltered pool for this function.")
            else:
                n_excluded = len(x_grid) - keep_mask.sum()
                if n_excluded > 0:
                    print(f"  [INFO] {fn_key}: excluded {n_excluded} of {len(x_grid)} Sobol "
                          f"candidates as too close to already-evaluated points.")
                x_grid = x_grid[keep_mask]
                x_grid_scaled = x_grid_scaled[keep_mask]
                pool_source_labels = pool_source_labels[keep_mask]

        y_best_current = np.max(Y_target)

        best_full_score = None
        best_box_score = None
        full_best_coords, full_best_value, full_best_std = None, None, None
        box_best_coords, box_best_value, box_best_std = None, None, None

        if acq_type == "random":
            rng = np.random.default_rng(sobol_seed_base + n_samples + fn_idx)
            chosen_global_idx = int(rng.integers(0, len(x_grid)))
        else:
            scores = compute_acquisition_scores(x_grid_scaled, gp, y_best_current, acq_type, param,
                                                 random_state=sobol_seed_base + n_samples)
            chosen_global_idx = int(np.argmax(scores))
            chosen_from_pool_preview = pool_source_labels[chosen_global_idx] if len(pool_source_labels) > 0 else "full-domain"

            # Per-pool best-score print diagnostic: to compare the best achievable acquisition score in each pool.
            # A small gap means the pools are roughly comparable (the bounding box isn't adding a lot of value);
            # A large gap is a more confident signal that there is a significant difference between candidates' quality.
          
            full_mask = pool_source_labels == "full-domain"
            box_mask = pool_source_labels == "local-box"

            full_best_idx_local = None
            box_best_idx_local = None
            if full_mask.any():
                full_idxs = np.where(full_mask)[0]
                full_best_idx_local = full_idxs[int(np.argmax(scores[full_mask]))]
                best_full_score = float(scores[full_best_idx_local])
              
            if box_mask.any():
                box_idxs = np.where(box_mask)[0]
                box_best_idx_local = box_idxs[int(np.argmax(scores[box_mask]))]
                best_box_score = float(scores[box_best_idx_local])

            if best_full_score is not None and best_box_score is not None:
                gap = best_box_score - best_full_score
                print(f"  [POOL COMPARISON] {fn_key}: best full-domain score={best_full_score:.6f} | "
                      f"best local-box score={best_box_score:.6f} | gap={gap:+.6f} "
                      f"({'box' if gap > 0 else 'full-domain'} pool wins)")

                # The GP's predicted output value and std (not just the acquisition score) of the best 
                # candidate from the runner-up pool (which did not supply the chosen next-query candidate)
                # is also computed and printed, to enable fair comparison and full transparency.
              
                for pool_label, best_idx_local in [("full-domain", full_best_idx_local),
                                                    ("local-box", box_best_idx_local)]:
                    cand_scaled_2d = x_grid_scaled[best_idx_local].reshape(1, -1)
                    cand_warped_val, cand_std = gp.predict(cand_scaled_2d, return_std=True)
                    cand_std = float(cand_std[0])
                    cand_orig_val = unwarp_predictions_and_values(cand_warped_val[0], fn_key, warpers)
                    cand_orig_val = float(np.ravel(cand_orig_val)[0])
                    cand_coords = x_grid[best_idx_local]
                    marker = " <-- WINNER" if pool_label == chosen_from_pool_preview else ""

                    # !Minor issue fix: as function_1's true-scale predicted values are much smaller than
                    # 1e-6, rounding them prints a meaningless "0.000000", so the raw unrounded floats
                    # are printed for function_1 instead; ".6f" rounding is kept for functions 2-8.
                                                      
                    val_str = f"{cand_orig_val}" if fn_idx == 1 else f"{cand_orig_val:.6f}"
                    print(f"      [{pool_label.upper()} BEST CANDIDATE]{marker} coords="
                          f"{np.round(cand_coords, 6)} | predicted value={val_str} | "
                          f"predicted std (warped)={cand_std:.4f}")
                                                      
                    if pool_label == "full-domain":
                        full_best_coords, full_best_value, full_best_std = cand_coords, cand_orig_val, cand_std
                    else:
                        box_best_coords, box_best_value, box_best_std = cand_coords, cand_orig_val, cand_std

        next_query_coords = x_grid[chosen_global_idx]
        next_query_scaled_2d = x_grid_scaled[chosen_global_idx].reshape(1, -1)
        chosen_from_pool = pool_source_labels[chosen_global_idx] if len(pool_source_labels) > 0 else "full-domain"

        predicted_warped_value, predicted_std = gp.predict(next_query_scaled_2d, return_std=True)
        predicted_warped_value = predicted_warped_value[0]
        predicted_std = float(predicted_std[0])

        predicted_original_value = unwarp_predictions_and_values(predicted_warped_value, fn_key, warpers)
        predicted_original_value = float(np.ravel(predicted_original_value)[0])

        next_queries_results[fn_key] = {
            "Next Query Coordinates": next_query_coords,
            "Winning Kernel": winning_kernel_name,
            "Winning Acquisition": best_acq_variant,
            "Predicted Original Scale Value": predicted_original_value,
            "Predicted Std (warped scale)": predicted_std,
            "Chosen From Pool": chosen_from_pool,
            "N Candidates Full Domain": full_domain_count,
            "N Candidates Local Box": n_candidates_box,
            "Volume Ratio": volume_ratio,
            "Best Full-Domain Score": best_full_score,
            "Best Local-Box Score": best_box_score,
          
            # Runner-up-pool visibility: storing the predicted value/std for the best candidate from each
            # pool individually, not just the pool that won, to enable fair comparison and full transparency.
          
            "Full-Domain Best Candidate Coords": full_best_coords,
            "Full-Domain Best Candidate Predicted Value": full_best_value,
            "Full-Domain Best Candidate Predicted Std": full_best_std,
            "Local-Box Best Candidate Coords": box_best_coords,
            "Local-Box Best Candidate Predicted Value": box_best_value,
            "Local-Box Best Candidate Predicted Std": box_best_std,
        }

        print(f"Function {fn_idx} | Next Query: {np.round(next_query_coords, 6)} | "
              f"Kernel: {winning_kernel_name} | Acq: {best_acq_variant:<20} | "
              f"Predicted Value: {predicted_original_value:.6f} | Pred Std (warped): {predicted_std:.4f} | "
              f"Chosen from: {chosen_from_pool} pool")

    print("=" * 115)
    return next_queries_results
