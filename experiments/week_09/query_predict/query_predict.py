"""
Next Query Prediction Module
---------------------------------------------------------------------------------------
Executing the HEBO-inspired, Dynamic Sobol-Sampled Bayesian Optimization next-query prediction pipeline:
1. Parametric Output Warping (Box-Cox / Yeo-Johnson, with a log10 pre-transform for Function 1)
2. GP Surrogate Fitting using the kernel chosen jointly with acquisition by the full kernel x
   acquisition ablation sweep (full_joint_ablation.run_full_joint_ablation).
3. Dynamic Sobol Quasi-Random Candidate Generation (continuous input-space exploration)
4. Acquisition Function (jointly-chosen) Evaluation and Scoring of Sobol candidates
5. Output Unwarping back to the original objective scale
"""

import numpy as np
from scipy.stats.qmc import Sobol
from sklearn.preprocessing import StandardScaler
from sklearn.gaussian_process import GaussianProcessRegressor

from output_warping.output_warping import apply_output_warping_to_dataset
from output_unwarping.output_unwarping import unwarp_predictions_and_values
from full_ablation.acq_strategies import acq_strategies
from full_ablation.acquisition import compute_acquisition_scores

def is_noiseless_kernel(kernel):
    """Returning True if the kernel has no WhiteKernel component."""
    return "WhiteKernel" not in str(kernel)

def run_next_query_prediction(
    data,
    sequential_ablation_summary,
    kernel_suites_dict,
    on_random_baseline="sample_random"
):
    """
    Predicting the next query point per function.
    
    Args:
        data: raw {"function_k": {"x": ..., "y": ...}} dataset dict.
        sequential_ablation_summary: output of full_joint_ablation.run_full_joint_ablation -
            must contain, per function, "Best Kernel" and "Best Acquisition".
        kernel_suites_dict: {fn_key: {kernel_name: kernel_object}} - used to look up the
            actual (unfitted) kernel object matching the winning kernel name.
        on_random_baseline: "sample_random" (default) draws a genuine random Sobol candidate
            when the ablation winner was "Random Baseline" (faithful to that finding).
            "fallback_best_nonrandom" instead uses EI(xi=0.01) with an explicit warning.

    Returns: {fn_key: {"Next Query Coordinates", "Winning Kernel", "Winning Acquisition",
                        "Predicted Original Scale Value", "Predicted Std (warped scale)"}}
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
                  f"-- make sure run_full_joint_ablation was run for this function.")

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
                            f"acq_strategies -- falling back to EI(xi=0.01).")
        else:
            acq_type, param = acq_strategies[best_acq_variant]

        if acq_warning:
            print(f"  [WARNING] {acq_warning}")

        # GP fitting using the jointly-chosen kernel on the full dataset
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_full)

        kernel_suite = kernel_suites_dict.get(fn_key, {})
        best_kernel = kernel_suite.get(winning_kernel_name)
        if best_kernel is None:
            print(f"  [WARNING] Kernel '{winning_kernel_name}' not found in kernel_suites_dict for "
                  f"{fn_key} -- falling back to first available kernel.")
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

        # Sobol candidate generation over the continuous input domain
        minimum = X_full.min(axis=0)
        maximum = X_full.max(axis=0)

        if n_dims >= 6:
            m_samples = 14
        elif n_dims >= 4:
            m_samples = 13
        else:
            m_samples = 12

        sobol = Sobol(d=n_dims, scramble=True, seed=42)
        unit_samples = sobol.random_base2(m=m_samples)
        x_grid = minimum + unit_samples * (maximum - minimum)
        x_grid_scaled = scaler.transform(x_grid)

        y_best_current = np.max(Y_target)

        if acq_type == "random":
            rng = np.random.default_rng(42 + fn_idx)
            chosen_global_idx = int(rng.integers(0, len(x_grid)))
        else:
            scores = compute_acquisition_scores(x_grid_scaled, gp, y_best_current, acq_type, param)
            chosen_global_idx = np.argmax(scores)

        next_query_coords = x_grid[chosen_global_idx]
        next_query_scaled_2d = x_grid_scaled[chosen_global_idx].reshape(1, -1)

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
            "Predicted Std (warped scale)": predicted_std
        }

        print(f"Function {fn_idx} | Next Query: {np.round(next_query_coords, 6)} | "
              f"Kernel: {winning_kernel_name} | Acq: {best_acq_variant:<20} | "
              f"Predicted Value: {predicted_original_value:.6f} | Pred Std (warped): {predicted_std:.4f}")

    print("=" * 115)
    return next_queries_results
