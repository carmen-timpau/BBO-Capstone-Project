"""
Full Joint Kernel x Acquisition Rollout Ablation (Functions 1-8)
----------------------------------------------------------------------------
This module gives for each function, the (kernel, acquisition) combination that
found the highest output during the rollout study - i.e. ranked directly for the 
global function maximization goal, not just for GP fit quality.
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

from .acq_strategies import acq_strategies
from .acquisition import compute_acquisition_scores
from ..kernel_ablation.kernels import get_kernel_suite, get_kernel_suite_f1  # unchanged, as pasted

warnings.filterwarnings("ignore", category=ConvergenceWarning)
warnings.filterwarnings("ignore", message="Predicted variances smaller than 0", category=UserWarning)


def is_noiseless_kernel(kernel):
    """Returning True if the kernel has no WhiteKernel component."""
    return "WhiteKernel" not in str(kernel)


def compute_effective_n_init(n_dims, n_samples, n_init_base=5, init_per_dim=2):
    """Scaling the initial design size with dimensionality instead of using a fixed constant, capped so at least 1 rollout step remains."""
    target = max(n_init_base, int(np.ceil(init_per_dim * n_dims)))
    return int(min(target, max(n_samples - 1, 1)))


def run_single_seed_rollout(seed, X_full, Y_target, true_global_max, kernel, n_init, n_iterations,
                             strategies_to_run):
    """Simulating a complete sequential rollout for every strategy in strategies_to_run, on a
    single random seed, for one specific kernel."""
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


def plot_master_convergence_grid(all_functions_regrets, output_dir="week_09/diagnostics_results",
                                  filename="full_joint_ablation_all_functions.png"):
    """Plotting 2x4 grid of convergence trajectories per function, using all 
    (kernel, acquisition) combinations swept for each function."""
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    fig, axes = plt.subplots(2, 4, figsize=(22, 11), sharey=False)
    axes = axes.flatten()

    for idx in range(8):
        fn_idx = idx + 1
        fn_key = f"function_{fn_idx}"
        ax = axes[idx]

        if fn_key not in all_functions_regrets:
            ax.set_visible(False)
            continue

        combo_regrets = all_functions_regrets[fn_key]

        for combo_name, trajectories in combo_regrets.items():
            if len(trajectories) == 0:
                continue
            traj_array = np.array(trajectories)
            mean_traj = np.mean(traj_array, axis=0)
            iterations = range(1, len(mean_traj) + 1)
            ax.plot(iterations, mean_traj, linewidth=1.0, alpha=0.6)

        ax.set_title(f"Function {fn_idx}", fontsize=14, fontweight='bold')
        ax.set_xlabel("Iteration", fontsize=11)
        ax.set_ylabel("Simple Regret", fontsize=11)
        ax.grid(True, linestyle="--", alpha=0.5)

    plt.suptitle(
        "Full Joint Kernel x Acquisition Sweep (all combos, incl. Random Baseline): "
        "Simple Regret Trajectories, Functions 1-8",
        fontsize=15, fontweight='bold', y=0.98
    )
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f"Master plot successfully saved to '{filepath}'")
    plt.show()


def run_full_joint_ablation(data, n_init_base=5, init_per_dim=2, n_iterations=15,
                             n_seeds=20, n_jobs=-1, holdout_fraction=0.3, regret_tie_tol=1e-9):
    """
    Performing the full kernel x acquisition sweep for every function, and returns the single best 
    (kernel, acquisition function) pair per function, ranked by lowest mean final simple regret.

    Returns: sequential_ablation_summary, a dict:
        {fn_key: {"Best Kernel", "Best Acquisition", "Mean Best Value Found",
                   "Mean Final Regret", "Mean AURC", "n_init_used", "n_iterations_used",
                   "Pool Exhausted", "Vs Random Baseline"}}
    """
    strategies_with_baseline = dict(acq_strategies)
    strategies_with_baseline["Random Baseline"] = ("random", None)

    sequential_ablation_summary = {}
    all_functions_regrets = {}
    all_functions_full_tables = {}

    for fn_idx in range(1, 9):
        fn_key = f"function_{fn_idx}"
        if fn_key not in data:
            continue

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

        n_init = compute_effective_n_init(n_dims, n_samples, n_init_base=n_init_base, init_per_dim=init_per_dim)
        max_possible_iterations = n_samples - n_init
        # Capping by holdout_fraction so the pool is never fully exhausted.
        # Exhausting the pool would otherwise force every strategy to an undesired trivial 0.0 final regret.
        holdout_capped_iterations = max(1, int(np.floor(holdout_fraction * max_possible_iterations)))
        effective_iterations = min(n_iterations, holdout_capped_iterations)
        pool_exhausted = (n_init + effective_iterations) >= n_samples

        kernel_suite = get_kernel_suite_f1(n_dims) if fn_idx == 1 else get_kernel_suite(n_dims)

        print(f"Running Function {fn_idx}: {n_samples} samples, {n_dims}D -> n_init={n_init}, "
              f"{effective_iterations} iterations (holdout_fraction={holdout_fraction}, "
              f"{n_samples - n_init - effective_iterations} points held out) x {n_seeds} seeds x "
              f"{len(kernel_suite)} kernels x {len(strategies_with_baseline)} strategies "
              f"({len(kernel_suite) * len(strategies_with_baseline) * n_seeds} total rollouts)...")
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
                ) for seed in range(n_seeds)
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
            if len(final_regrets) == 0:
                continue
            kernel_name, strat_name = combo_meta[combo_name]
            mean_final_regret = np.mean(final_regrets)
            rows.append({
                "Kernel": kernel_name,
                "Acquisition Variant": strat_name,
                "Mean Best Value Found": round(true_global_max - mean_final_regret, 4),
                "Mean Final Regret": round(mean_final_regret, 4),
                "Median Final Regret": round(np.median(final_regrets), 4),
                "Std Final Regret": round(np.std(final_regrets), 4),
                "Mean AURC (Convergence Speed)": round(np.mean(combo_aurcs[combo_name]), 4)
            })

        combo_df = pd.DataFrame(rows)
        combo_df = combo_df.sort_values(
            by=["Mean Final Regret", "Mean AURC (Convergence Speed)"], ascending=[True, True]
        ).reset_index(drop=True)
        all_functions_full_tables[fn_key] = combo_df

        print("=" * 135)
        print(f"        FUNCTION {fn_idx} — FULL JOINT KERNEL x ACQUISITION SWEEP (N_seeds={n_seeds}, n_init={n_init})")
        print("=" * 135)
        print(combo_df.head(10).to_string(index=False))
        print(f"(showing top 10 of {len(combo_df)} combos)")

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
                    vs_random = "TIE on both final regret and AURC -- indistinguishable from random here"
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
        sequential_ablation_summary[fn_key] = {
            "Best Kernel": best_combo["Kernel"],
            "Best Acquisition": best_combo["Acquisition Variant"],
            "Mean Best Value Found": best_combo["Mean Best Value Found"],
            "Mean Final Regret": best_combo["Mean Final Regret"],
            "Mean AURC": best_combo["Mean AURC (Convergence Speed)"],
            "n_init_used": n_init,
            "n_iterations_used": effective_iterations,
            "Pool Exhausted": pool_exhausted,
            "Vs Random Baseline": vs_random
        }

    print("\n" + "=" * 100)
    print(" SUMMARY: BEST (KERNEL, ACQUISITION) COMBO PER FUNCTION — RANKED FOR GLOBAL MAXIMIZATION")
    print("=" * 100)
    for fn_k, res in sequential_ablation_summary.items():
        print(f"{fn_k.upper()}: {res['Best Kernel']} + {res['Best Acquisition']}")
        print(f"    Mean Best Value Found : {res['Mean Best Value Found']}")
        print(f"    Mean Final Regret     : {res['Mean Final Regret']}")
        print(f"    Mean AURC             : {res['Mean AURC']}")
        print(f"    n_init / n_iterations : {res['n_init_used']} / {res['n_iterations_used']}"
              f"{' (pool exhausted!)' if res['Pool Exhausted'] else ''}")
        print(f"    Vs random baseline    : {res['Vs Random Baseline']}")
    print("=" * 100)

    plot_master_convergence_grid(all_functions_regrets, output_dir="week_09/diagnostics_results",
                                  filename="full_joint_ablation_all_functions.png")

    return sequential_ablation_summary
