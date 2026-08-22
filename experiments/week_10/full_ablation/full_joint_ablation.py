"""
Upgraded Full Joint Kernel x Acquisition Rollout Ablation (Functions 1-8)
----------------------------------------------------------------------------
This module gives for each function, the (kernel, acquisition) combination that
found the highest output during the rollout study - i.e. ranked directly for the 
global function maximization goal, not just for GP fit quality.

Each combo's Mean Simple Final Regret is now accompanied by a Standard Error (SEM) and a 95% Confidence Interval 
(via the t-distribution, computed per-seed across the n_seeds rollouts). A "Vs #1 Ranked" column flags whether a 
combo's CI overlaps the #1-ranked combo's CI, so the ranking reflects statistical confidence rather than a bare 
point-estimate comparison — surfacing when the reported "winner" is genuinely distinguishable from the runner-ups 
versus merely ahead by an amount within noise.
  
"""

import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.exceptions import ConvergenceWarning
from joblib import Parallel, delayed
from scipy.stats import t as t_dist

from .acq_strategies import acq_strategies
from .acquisition import compute_acquisition_scores
from ..kernel_ablation.kernels import get_kernel_suite, get_kernel_suite_f1 

warnings.filterwarnings("ignore", category=ConvergenceWarning)
warnings.filterwarnings("ignore", message="Predicted variances smaller than 0", category=UserWarning)


def is_noiseless_kernel(kernel):
    """Returning True if the kernel has no WhiteKernel component."""
    return "WhiteKernel" not in str(kernel)


def compute_effective_n_init(n_dims, n_samples, n_init_base=5, init_per_dim=2):
    """Scaling the initial design size with dimensionality."""
    target = max(n_init_base, int(np.ceil(init_per_dim * n_dims)))
    return int(min(target, max(n_samples - 1, 1)))


def run_single_seed_rollout(seed, X_full, Y_target, true_global_max, kernel, n_init, n_iterations,
                             strategies_to_run):
    """Simulating a complete sequential rollout for every strategy in strategies_to_run, on a single seed, one kernel."""
    rng = np.random.default_rng(seed)
    n_samples = len(X_full)
    init_indices = rng.choice(n_samples, size=min(n_init, n_samples), replace=False)

    seed_trajectories = {}

    for strat_name, (acq_type, param) in strategies_to_run.items():
        X_train = X_full[init_indices].copy()
        Y_train = Y_target[init_indices].copy()
        remaining_indices = list(set(range(n_samples)) - set(init_indices))

        regret_trajectory = []

        for iteration_idx in range(n_iterations):
            if len(remaining_indices) == 0:
                break

            if acq_type == "random":
                best_candidate_local_idx = int(rng.integers(0, len(remaining_indices)))
            else:
                scaler = StandardScaler()
                X_train_scaled = scaler.fit_transform(X_train)

                gp_random_state = int(seed) + 42
                alpha_value = 1e-8 if is_noiseless_kernel(kernel) else 0.0
                gp = GaussianProcessRegressor(
                    kernel=kernel,
                    alpha=alpha_value,
                    normalize_y=True,
                    n_restarts_optimizer=10,
                    optimizer="fmin_l_bfgs_b",
                    random_state=gp_random_state
                )

                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", category=ConvergenceWarning)
                    gp.fit(X_train_scaled, Y_train)

                X_rem_scaled = scaler.transform(X_full[remaining_indices])
                y_best_current = np.max(Y_train)

                ts_random_state = int(seed) + iteration_idx * 1000
                scores = compute_acquisition_scores(
                    X_rem_scaled, gp, y_best_current, acq_type, param, random_state=ts_random_state
                )
                best_candidate_local_idx = np.argmax(scores)

            chosen_global_idx = remaining_indices[best_candidate_local_idx]

            X_train = np.vstack([X_train, X_full[chosen_global_idx]])
            Y_train = np.append(Y_train, Y_target[chosen_global_idx])
            remaining_indices.pop(best_candidate_local_idx)

            simple_regret = true_global_max - np.max(Y_train)
            regret_trajectory.append(simple_regret)

        seed_trajectories[strat_name] = regret_trajectory

    return seed_trajectories


def abbreviate_acq_name(acq_name):
    """Shortening acquisition variant names for compact legend labels."""
    replacements = {
        "Upper Confidence Bound": "UCB",
        "Expected Improvement": "EI",
        "Probability of Improvement": "PI",
        "Thompson Sampling": "TS",
    }
    for full, short in replacements.items():
        if acq_name.startswith(full):
            return acq_name.replace(full, short)
    return acq_name


def plot_master_convergence_grid(all_functions_regrets, all_functions_full_tables=None,
                                  top_n_labeled=5, output_dir="week_10/diagnostics_results",
                                  filename="full_joint_ablation_all_functions_legend.png"):
    """Plotting 2x4 grid of convergence trajectories per function, using all (kernel, acquisition) 
    combinations swept for each function. The top-N combos are highlighted."""
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    fig, axes = plt.subplots(2, 4, figsize=(22, 11), sharey=False)
    axes = axes.flatten()

    highlight_colors = plt.cm.tab10.colors

    for idx in range(8):
        fn_idx = idx + 1
        fn_key = f"function_{fn_idx}"
        ax = axes[idx]

        if fn_key not in all_functions_regrets:
            ax.set_visible(False)
            continue

        combo_regrets = all_functions_regrets[fn_key]

        top_combo_labels = {}
        if all_functions_full_tables is not None and fn_key in all_functions_full_tables:
            ranked_df = all_functions_full_tables[fn_key]
            for _, row in ranked_df.head(top_n_labeled).iterrows():
                combo_name = f"{row['Kernel']} + {row['Acquisition Variant']}"
                kernel_short = row['Kernel'].split(":")[-1].strip() if ":" in row['Kernel'] else row['Kernel']
                acq_short = abbreviate_acq_name(row['Acquisition Variant'])
                top_combo_labels[combo_name] = f"{kernel_short} + {acq_short}"

        for combo_name, trajectories in combo_regrets.items():
            if len(trajectories) == 0 or combo_name in top_combo_labels:
                continue
            traj_array = np.array(trajectories)
            mean_traj = np.mean(traj_array, axis=0)
            iterations = range(1, len(mean_traj) + 1)
            ax.plot(iterations, mean_traj, linewidth=0.8, alpha=0.15, color="gray")

        for rank, (combo_name, short_label) in enumerate(top_combo_labels.items()):
            trajectories = combo_regrets.get(combo_name, [])
            if len(trajectories) == 0:
                continue
            traj_array = np.array(trajectories)
            mean_traj = np.mean(traj_array, axis=0)
            iterations = range(1, len(mean_traj) + 1)
            ax.plot(iterations, mean_traj, linewidth=2.0, alpha=0.95,
                     color=highlight_colors[rank % len(highlight_colors)], label=short_label)

        ax.set_title(f"Function {fn_idx}", fontsize=14, fontweight='bold')
        ax.set_xlabel("Iteration", fontsize=11)
        ax.set_ylabel("Simple Regret", fontsize=11)
        ax.grid(True, linestyle="--", alpha=0.5)
        if top_combo_labels:
            ax.legend(loc='upper right', fontsize=6.5, framealpha=0.8, title=f"Top {top_n_labeled}",
                       title_fontsize=7)

    plt.suptitle(
        f"Full Joint Kernel x Acquisition Sweep (top {top_n_labeled} highlighted, incl. Random Baseline): "
        "Simple Regret Trajectories, Functions 1-8",
        fontsize=15, fontweight='bold', y=0.98
    )
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f"Master plot successfully saved to '{filepath}'")
    plt.show()


def run_full_joint_ablation(data, n_init_base=5, init_per_dim=2, n_iterations=15,
                             n_seeds=20, n_jobs=-1, holdout_fraction=0.3, regret_tie_tol=1e-9,
                             n_init_base_s=None, init_per_dim_s=None,
                             holdout_fraction_s=None, n_seeds_overrides=None):
    """
    Running the FULL kernel x acquisition sweep for every function, ranked by lowest mean final
    regret (ties broken by AURC). AN reports SEM + 95% CI (t-distribution) per combo, and
    flags which combos are statistically indistinguishable from the #1-ranked combo.

    Returns: sequential_ablation_summary, a dict:
        {fn_key: {"Best Kernel", "Best Acquisition", "Mean Best Value Found",
                   "Mean Final Regret", "95% CI", "Mean AURC", "n_init_used",
                   "n_iterations_used", "n_seeds_used", "Pool Exhausted", "Vs Random Baseline",
                   "N Combos Statistically Tied With #1"}}
    """
    n_init_base_overrides = n_init_base_overrides or {}
    init_per_dim_overrides = init_per_dim_overrides or {}
    holdout_fraction_overrides = holdout_fraction_overrides or {}
    n_seeds_overrides = n_seeds_overrides or {}

    strategies_with_baseline = dict(acq_strategies)
    strategies_with_baseline["Random Baseline"] = ("random", None)

    sequential_ablation_summary = {}
    all_functions_regrets = {}
    all_functions_full_tables = {}

    for fn_idx in range(1, 9):
        fn_key = f"function_{fn_idx}"
        if fn_key not in data:
            continue

        # Resolving per-function parameter values: override if provided, else the global default.
        fn_n_init_base = n_init_base_overrides.get(fn_key, n_init_base)
        fn_init_per_dim = init_per_dim_overrides.get(fn_key, init_per_dim)
        fn_holdout_fraction = holdout_fraction_overrides.get(fn_key, holdout_fraction)
        fn_n_seeds = n_seeds_overrides.get(fn_key, n_seeds)

        X_full = np.array(data[fn_key]["x"])
        Y_raw = np.array(data[fn_key]["y"]).flatten()
        n_samples, n_dims = X_full.shape

        if fn_idx == 1:
            positive_Y = Y_raw[Y_raw > 0]
            noise_floor = positive_Y.min()
            Y_safe = np.clip(Y_raw, noise_floor, None)
            Y_target = np.log10(Y_safe)
        else:
            Y_target = Y_raw

        true_global_max = np.max(Y_target)

        # [DIAGNOSTIC] message: if multiple points share the exact max value in the dataset (Function 5), 
        # any strategy (including random) has a much higher chance of "finding" it trivially - 
        # this can produce degenerate zero regret across nearly every combo regardless of acquisition quality.
        n_ties_at_max = int(np.sum(np.isclose(Y_target, true_global_max)))
        if n_ties_at_max > 1:
            print(f"  [DIAGNOSTIC] {fn_key}: {n_ties_at_max} of {n_samples} points share the exact "
                  f"global max value - regret-based ranking will be much less discriminating here, "
                  f"since many strategies can 'find' the max just by chance.")

        n_init = compute_effective_n_init(n_dims, n_samples, n_init_base=fn_n_init_base, init_per_dim=fn_init_per_dim)
        max_possible_iterations = n_samples - n_init
        holdout_capped_iterations = max(1, int(np.floor(fn_holdout_fraction * max_possible_iterations)))
        effective_iterations = min(n_iterations, holdout_capped_iterations)
        pool_exhausted = (n_init + effective_iterations) >= n_samples

        # [DIAGNOSTIC] message: how much of the pool n_init alone consumes. If this fraction is large,
        # the initial random draw (before any acquisition strategy runs) has a meaningful chance
        # of already containing the max, making the eventual acquisition comparison less
        # informative - regret can hit 0 for nearly every combo simply because they all
        # inherited a lucky init, not because of what the acquisition strategy actually did.
        init_fraction_of_pool = n_init / n_samples
        if init_fraction_of_pool > 0.25:
            print(f"  [DIAGNOSTIC] {fn_key}: n_init={n_init} is {init_fraction_of_pool:.0%} of the "
                  f"{n_samples}-point pool - a meaningful chance the max is already captured by "
                  f"the initial random design before acquisition runs, which flattens differences "
                  f"between acquisition strategies. Consider lowering init_per_dim/n_init_base for "
                  f"this function if you want the acquisition process itself to carry more weight.")

        kernel_suite = get_kernel_suite_f1(n_dims) if fn_idx == 1 else get_kernel_suite(n_dims)

        print(f"Running Function {fn_idx}: {n_samples} samples, {n_dims}D -> n_init={n_init}, "
              f"{effective_iterations} iterations (holdout_fraction={fn_holdout_fraction}, "
              f"{n_samples - n_init - effective_iterations} points held out) x {fn_n_seeds} seeds x "
              f"{len(kernel_suite)} kernels x {len(strategies_with_baseline)} strategies "
              f"({len(kernel_suite) * len(strategies_with_baseline) * fn_n_seeds} total rollouts)...")
        if pool_exhausted:
            print(f"  [WARNING] Pool for {fn_key} is small enough that even the holdout-capped "
                  f"rollout reaches all {n_samples} points - final regret may still saturate at 0.0.")

        combo_regrets = {}
        combo_aurcs = {}
        combo_meta = {}

        for kernel_name, kernel_obj in kernel_suite.items():
            seed_results = Parallel(n_jobs=n_jobs)(
                delayed(run_single_seed_rollout)(
                    seed, X_full, Y_target, true_global_max, kernel_obj, n_init,
                    effective_iterations, strategies_with_baseline
                ) for seed in range(fn_n_seeds)
            )

            for strat_name in strategies_with_baseline:
                combo_name = f"{kernel_name} + {strat_name}"
                combo_regrets[combo_name] = []
                combo_aurcs[combo_name] = []
                combo_meta[combo_name] = (kernel_name, strat_name)

            for seed_res in seed_results:
                for strat_name, trajectory in seed_res.items():
                    combo_name = f"{kernel_name} + {strat_name}"
                    if len(trajectory) > 0:
                        combo_regrets[combo_name].append(trajectory)
                        combo_aurcs[combo_name].append(np.trapezoid(trajectory))

        all_functions_regrets[fn_key] = combo_regrets

        rows = []
        for combo_name, trajectories in combo_regrets.items():
            final_regrets = [traj[-1] for traj in trajectories if len(traj) > 0]
            n_valid = len(final_regrets)
            if n_valid == 0:
                continue
            kernel_name, strat_name = combo_meta[combo_name]
            mean_final_regret = np.mean(final_regrets)

            if n_valid > 1:
                sample_std = np.std(final_regrets, ddof=1)
                sem = sample_std / np.sqrt(n_valid)
                t_crit = t_dist.ppf(0.975, df=n_valid - 1)
                ci_half_width = t_crit * sem
                ci_lower = mean_final_regret - ci_half_width
                ci_upper = mean_final_regret + ci_half_width
            else:
                sem = np.nan
                ci_lower, ci_upper = np.nan, np.nan

            rows.append({
                "Kernel": kernel_name,
                "Acquisition Variant": strat_name,
                "Mean Best Value Found": round(true_global_max - mean_final_regret, 4),
                "Mean Final Regret": round(mean_final_regret, 4),
                "Median Final Regret": round(np.median(final_regrets), 4),
                "Std Final Regret": round(np.std(final_regrets), 4),
                "SEM (Final Regret)": round(sem, 6) if not np.isnan(sem) else np.nan,
                "95% CI Lower": round(ci_lower, 6) if not np.isnan(ci_lower) else np.nan,
                "95% CI Upper": round(ci_upper, 6) if not np.isnan(ci_upper) else np.nan,
                "Mean AURC (Convergence Speed)": round(np.mean(combo_aurcs[combo_name]), 4),
                "N Valid Seeds": n_valid
            })

        combo_df = pd.DataFrame(rows)
        combo_df = combo_df.sort_values(
            by=["Mean Final Regret", "Mean AURC (Convergence Speed)"], ascending=[True, True]
        ).reset_index(drop=True)

        # Degenerate regret detection: 
        # If final regret has collapsed to (near) the same value for most of the top combos - typically because 
        # a large n_init already captured the max for most seeds, or because ties exist at the max value - then final-regret 
        # CIs carry no real discriminating signal, though AURC still does (it captures the whole trajectory, not just the last point). 
        # In that regime, the tie flag below switches to comparing AURC's own CI instead of regret's CI, since AURC is
        # the metric still doing genuine discriminating work.
        top10_regrets = combo_df.head(10)["Mean Final Regret"]
        regret_is_degenerate = bool((top10_regrets.max() - top10_regrets.min()) < 1e-6)

        # AURC gets the same SEM/95% CI treatment as final regret, so it can be used as a
        # statistically grounded fallback discriminator rather than a bare point-value comparison.
        aurc_stats = {}
        for combo_name, aurc_values in combo_aurcs.items():
            n_valid_aurc = len(aurc_values)
            if n_valid_aurc > 1:
                aurc_mean = np.mean(aurc_values)
                aurc_sample_std = np.std(aurc_values, ddof=1)
                aurc_sem = aurc_sample_std / np.sqrt(n_valid_aurc)
                aurc_t_crit = t_dist.ppf(0.975, df=n_valid_aurc - 1)
                aurc_ci_lower = aurc_mean - aurc_t_crit * aurc_sem
                aurc_ci_upper = aurc_mean + aurc_t_crit * aurc_sem
            else:
                aurc_ci_lower, aurc_ci_upper = np.nan, np.nan
            aurc_stats[combo_name] = (aurc_ci_lower, aurc_ci_upper)

        if regret_is_degenerate:
            print(f"  [NOTE] Final regret is degenerate (near-zero spread) among the top 10 combos "
                  f"for {fn_key} - the tie-flag below uses AURC's own 95% CI instead of final "
                  f"regret's CI, since AURC is still genuinely discriminating in this regime.")

        best_ci_lower = combo_df.loc[0, "95% CI Lower"]
        best_ci_upper = combo_df.loc[0, "95% CI Upper"]

        best_combo_name_rank0 = f"{combo_df.loc[0, 'Kernel']} + {combo_df.loc[0, 'Acquisition Variant']}"
        best_aurc_ci_lower, best_aurc_ci_upper = aurc_stats.get(best_combo_name_rank0, (np.nan, np.nan))

        def _overlap_flag(row):
            if row.name == 0:
                return "- (top ranked)"
            if regret_is_degenerate:
                combo_name = f"{row['Kernel']} + {row['Acquisition Variant']}"
                row_aurc_ci_lower, row_aurc_ci_upper = aurc_stats.get(combo_name, (np.nan, np.nan))
                if pd.isna(row_aurc_ci_lower) or pd.isna(best_aurc_ci_lower):
                    return "N/A (insufficient seeds, AURC)"
                overlaps = (row_aurc_ci_upper >= best_aurc_ci_lower) and (row_aurc_ci_lower <= best_aurc_ci_upper)
                return "Tied with #1 (AURC CI overlap)" if overlaps else "Distinguishable from #1 (AURC)"
            if pd.isna(row["95% CI Lower"]) or pd.isna(best_ci_lower):
                return "N/A (insufficient seeds)"
            overlaps = (row["95% CI Upper"] >= best_ci_lower) and (row["95% CI Lower"] <= best_ci_upper)
            return "Tied with #1 (CI overlap)" if overlaps else "Distinguishable from #1"

        combo_df["Vs #1 Ranked"] = combo_df.apply(_overlap_flag, axis=1)
        all_functions_full_tables[fn_key] = combo_df

        n_tied_in_top10 = combo_df.head(10)["Vs #1 Ranked"].isin(
            ["Tied with #1 (CI overlap)", "Tied with #1 (AURC CI overlap)"]
        ).sum()

        print("=" * 135)
        print(f"        FUNCTION {fn_idx} — FULL JOINT KERNEL x ACQUISITION SWEEP (N_seeds={fn_n_seeds}, n_init={n_init})")
        print("=" * 135)
        display_cols = ["Kernel", "Acquisition Variant", "Mean Final Regret", "SEM (Final Regret)",
                         "95% CI Lower", "95% CI Upper", "Mean AURC (Convergence Speed)", "Vs #1 Ranked"]
        print(combo_df.head(10)[display_cols].to_string(index=False))
        print(f"(showing top 10 of {len(combo_df)} combos)")
        if n_tied_in_top10 > 0:
            metric_used = "AURC" if regret_is_degenerate else "final regret"
            print(f"  [NOTE] {n_tied_in_top10} of the top 10 combos have a 95% CI ({metric_used}) overlapping "
                  f"the #1-ranked combo's CI - they are statistically indistinguishable from the "
                  f"reported 'winner' given {fn_n_seeds} seeds, not genuinely worse.")

        random_rows = combo_df[combo_df["Acquisition Variant"] == "Random Baseline"]
        non_random_rows = combo_df[combo_df["Acquisition Variant"] != "Random Baseline"]
        vs_random = None
        if not random_rows.empty and not non_random_rows.empty:
            best_random_regret = random_rows["Mean Final Regret"].min()
            best_random_aurc = random_rows.loc[random_rows["Mean Final Regret"].idxmin(), "Mean AURC (Convergence Speed)"]
            best_non_random_row = non_random_rows.iloc[0]
            best_non_random_regret = best_non_random_row["Mean Final Regret"]
            best_non_random_aurc = best_non_random_row["Mean AURC (Convergence Speed)"]

            regret_diff = best_non_random_regret - best_random_regret
            if abs(regret_diff) <= regret_tie_tol:
                if best_non_random_aurc < best_random_aurc - regret_tie_tol:
                    vs_random = "TIE on final regret, WINS on AURC (converges faster)"
                elif best_non_random_aurc > best_random_aurc + regret_tie_tol:
                    vs_random = "TIE on final regret, LOSES on AURC (converges slower)"
                else:
                    vs_random = "TIE on both final regret and AURC - indistinguishable from random here"
            elif regret_diff < 0:
                vs_random = "WINS on final regret"
            else:
                vs_random = "LOSES on final regret"

            print(f"Best random-baseline: Mean Final Regret={round(best_random_regret, 4)}, "
                  f"Mean AURC={round(best_random_aurc, 4)}")
            print(f"Best overall combo:   Mean Final Regret={round(best_non_random_regret, 4)}, "
                  f"Mean AURC={round(best_non_random_aurc, 4)}")
            print(f"Best combo vs random baseline: {vs_random}")
        print("-" * 135)

        best_combo = combo_df.iloc[0]
        n_tied_total = int(combo_df["Vs #1 Ranked"].isin(
            ["Tied with #1 (CI overlap)", "Tied with #1 (AURC CI overlap)"]
        ).sum())
        sequential_ablation_summary[fn_key] = {
            "Best Kernel": best_combo["Kernel"],
            "Best Acquisition": best_combo["Acquisition Variant"],
            "Mean Best Value Found": best_combo["Mean Best Value Found"],
            "Mean Final Regret": best_combo["Mean Final Regret"],
            "95% CI": (best_combo["95% CI Lower"], best_combo["95% CI Upper"]),
            "Mean AURC": best_combo["Mean AURC (Convergence Speed)"],
            "n_init_used": n_init,
            "n_iterations_used": effective_iterations,
            "n_seeds_used": fn_n_seeds,
            "Pool Exhausted": pool_exhausted,
            "Vs Random Baseline": vs_random,
            "N Combos Statistically Tied With #1": n_tied_total
        }

    print("\n" + "=" * 100)
    print(" SUMMARY: BEST (KERNEL, ACQUISITION) COMBO PER FUNCTION — RANKED FOR GLOBAL MAXIMIZATION")
    print("=" * 100)
    for fn_k, res in sequential_ablation_summary.items():
        print(f"{fn_k.upper()}: {res['Best Kernel']} + {res['Best Acquisition']}")
        print(f"    Mean Best Value Found : {res['Mean Best Value Found']}")
        ci_lower, ci_upper = res['95% CI']
        ci_str = f"[{ci_lower:.6f}, {ci_upper:.6f}]" if not (pd.isna(ci_lower) or pd.isna(ci_upper)) else "N/A"
        print(f"    Mean Final Regret     : {res['Mean Final Regret']}  (95% CI: {ci_str})")
        print(f"    Mean AURC             : {res['Mean AURC']}")
        print(f"    n_init / n_iterations : {res['n_init_used']} / {res['n_iterations_used']}"
              f"{' (pool exhausted!)' if res['Pool Exhausted'] else ''}")
        print(f"    n_seeds used          : {res['n_seeds_used']}")
        print(f"    Vs random baseline    : {res['Vs Random Baseline']}")
        if res['N Combos Statistically Tied With #1'] > 0:
            print(f"    [NOTE] {res['N Combos Statistically Tied With #1']} other combo(s) are statistically "
                  f"indistinguishable from this 'winner' (overlapping 95% CI) - treat the ranking among "
                  f"them as uncertain, not a confirmed order.")
    print("=" * 100)

    plot_master_convergence_grid(all_functions_regrets, all_functions_full_tables=all_functions_full_tables,
                                  top_n_labeled=5, output_dir="week_10/diagnostics_results",
                                  filename="full_joint_ablation_all_functions_legend.png")

    return sequential_ablation_summary
