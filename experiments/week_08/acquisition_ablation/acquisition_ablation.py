"""Robust Multi-Step Sequential Offline Bayesian Optimization Rollout Ablation Study (Functions 1–8)

This robust acquisition ablation study runs entirely on pre-existing datasets (X_full and Y_target) without querying 
a live, physical black-box function in real-time, functioning as an offline sequential optimization process.

Main strategies used:

- Offline Rollout Simulation: Iteratively selects points from pre-computed pools (X_full, Y_target) 
  using diverse acquisition strategies (e.g., EI, UCB, PI, Thompson Sampling) to track simple regret trajectories.
  
- GP Surrogate Modeling: Fits Gaussian Process Regressors with optimized kernels (from prior kernel ablation study) 
  using gradient-based L-BFGS-B optimization (`optimizer="fmin_l_bfgs_b"`, `n_restarts_optimizer=10`) 
  to maximize Log Marginal Likelihood and ensure reliable uncertainty estimates.
  
- Multi-Seed Parallelization: Runs rollouts across multiple random seeds in parallel via Joblib 
  to eliminate stochastic initialization bias.
  
- Comprehensive Performance Metrics Evaluation: Computes final simple regret and Area Under the Regret Curve (AURC) 
  to rigorously rank acquisition strategies based on both ultimate accuracy (final regret) and convergence speed.
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
from ..kernel_ablation.kernels import get_kernel_suite, get_kernel_suite_f1

warnings.filterwarnings("ignore", category=ConvergenceWarning)
warnings.filterwarnings("ignore", message="Predicted variances smaller than 0", category=UserWarning)

def run_single_seed_rollout(seed, X_full, Y_target, true_global_max, best_kernel, n_init, n_iterations):
    """Simulates a complete sequential rollout for all strategies on a single random seed."""
    rng = np.random.default_rng(seed)
    n_samples = len(X_full)
    init_indices = rng.choice(n_samples, size=min(n_init, n_samples), replace=False)
    
    seed_trajectories = {}

    for strat_name, (acq_type, param) in acq_strategies.items():
        X_train = X_full[init_indices].copy()
        Y_train = Y_target[init_indices].copy()
        remaining_indices = list(set(range(n_samples)) - set(init_indices))
        
        regret_trajectory = []

        for iteration_idx in range(n_iterations):
            if len(remaining_indices) == 0:
                break

            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)

            # Explicitly passing an integer seed to random_state (using deterministic offset based on seed prevents core collisions)
            gp_random_state = int(seed) + 42
            gp = GaussianProcessRegressor(
                kernel=best_kernel, 
                alpha=1e-6, 
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
            
            # Pass a unique deterministic seed for Thompson Sampling generation per iteration if applicable
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

def plot_master_convergence_grid(all_functions_regrets, output_dir="week_08/diagnostics_results", filename="wk8_acquisition_ablation_results_all_functions.png"):
    """Plotting a consolidated 2x4 grid of convergence trajectories for Functions 1 to 8, saving it to the target directory, and displaying it."""
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    fig, axes = plt.subplots(2, 4, figsize=(20, 10), sharey=False)
    axes = axes.flatten()

    for idx in range(8):
        fn_idx = idx + 1
        fn_key = f"function_{fn_idx}"
        ax = axes[idx]
        
        if fn_key not in all_functions_regrets:
            ax.set_visible(False)
            continue

        strategy_regrets = all_functions_regrets[fn_key]

        for strat_name, trajectories in strategy_regrets.items():
            if len(trajectories) == 0:
                continue
            traj_array = np.array(trajectories)
            mean_traj = np.mean(traj_array, axis=0)
            std_err = np.std(traj_array, axis=0) / np.sqrt(len(trajectories))
            
            iterations = range(1, len(mean_traj) + 1)
            ax.plot(iterations, mean_traj, linewidth=1.5, label=strat_name)
            ax.fill_between(iterations, mean_traj - std_err, mean_traj + std_err, alpha=0.12)
            
        ax.set_title(f"Function {fn_idx}", fontsize=14, fontweight='bold')
        ax.set_xlabel("Iteration", fontsize=12)
        ax.set_ylabel("Simple Regret", fontsize=12)
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.legend(loc='upper right', fontsize=9, framealpha=0.7)

    plt.suptitle("Multi-Step Rollout and Acquisition Ablation via Offline Bayesian Optimization: Simple Regret Trajectories Across Datasets of Black-Box Functions 1–8", fontsize=15, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f"Master plot successfully saved to '{filepath}'")
    
    plt.show()

def run_sequential_acq_ablation(data, top_kernels_summary, n_init=5, n_iterations=15, n_seeds=20, n_jobs=-1):
    """
    Upgraded BBO Acquisition Ablation Study:
    - Parallelized seed execution across all functions.
    - Full trajectory tracking & AURC computation.
    - Dynamically capping rollout iterations per function based on available pool size.
    - Automatically storing and printing the best acquisition function per function based on lowest Mean AURC.
    """
    sequential_ablation_summary = {}
    all_functions_regrets = {}

    for fn_idx in range(1, 9):
        fn_key = f"function_{fn_idx}"
        if fn_key not in data:
            continue

        X_full = np.array(data[fn_key]["x"])
        Y_raw = np.array(data[fn_key]["y"]).flatten()
        n_samples, n_dims = X_full.shape

        if fn_idx == 1:
            Y_target = np.log10(np.maximum(Y_raw, 1e-300))
        else:
            Y_target = Y_raw

        true_global_max = np.max(Y_target)

        kernel_info = top_kernels_summary.get(fn_key, {})
        winning_variant_name = kernel_info.get("Best Variant", "Baseline: Matern 2.5 + WhiteNoise (ARD)")
        
        kernel_suite = get_kernel_suite_f1(n_dims) if fn_idx == 1 else get_kernel_suite(n_dims)
        best_kernel = kernel_suite.get(winning_variant_name, list(kernel_suite.values())[0])

        max_possible_iterations = n_samples - n_init
        effective_iterations = min(n_iterations, max_possible_iterations)

        print(f"Running Function {fn_idx}: {n_samples} samples -> Capping rollout at {effective_iterations} iterations across {n_seeds} seeds...")
        
        seed_results = Parallel(n_jobs=n_jobs)(
            delayed(run_single_seed_rollout)(
                seed, X_full, Y_target, true_global_max, best_kernel, n_init, effective_iterations
            ) for seed in range(n_seeds)
        )

        strategy_regrets = {strat: [] for strat in acq_strategies}
        strategy_aurcs = {strat: [] for strat in acq_strategies}

        for seed_res in seed_results:
            for strat_name, trajectory in seed_res.items():
                if len(trajectory) > 0:
                    strategy_regrets[strat_name].append(trajectory)
                    aurc = np.trapezoid(trajectory)
                    strategy_aurcs[strat_name].append(aurc)

        all_functions_regrets[fn_key] = strategy_regrets

        acq_results = []
        for strat_name in acq_strategies:
            final_regrets = [traj[-1] for traj in strategy_regrets[strat_name] if len(traj) > 0]
            aurc_values = strategy_aurcs[strat_name]

            acq_results.append({
                "Acquisition Variant": strat_name,
                "Mean Final Regret": round(np.mean(final_regrets), 4),
                "Median Final Regret": round(np.median(final_regrets), 4),
                "Std Final Regret": round(np.std(final_regrets), 4),
                "Mean AURC (Convergence Speed)": round(np.mean(aurc_values), 4)
            })

        acq_df = pd.DataFrame(acq_results)
        acq_df = acq_df.sort_values(by=["Mean Final Regret", "Mean AURC (Convergence Speed)"], ascending=[True, True]).reset_index(drop=True)

        print("=" * 115)
        print(f"        FUNCTION {fn_idx} — WEEK 7 ROBUST SEQUENTIAL ROLLOUT ABLATION (N_seeds={n_seeds})")
        print("=" * 115)
        print(acq_df.to_string(index=False))
        print("-" * 115)

        best_acq = acq_df.iloc[0]
        sequential_ablation_summary[fn_key] = {
            "Best Acquisition": best_acq["Acquisition Variant"],
            "Mean Final Regret": best_acq["Mean Final Regret"],
            "Mean AURC": best_acq["Mean AURC (Convergence Speed)"]
        }

    print("\n" + "=" * 80)
    print(" SUMMARY: BEST ACQUISITION FUNCTION PER FUNCTION (BASED ON RANKING)")
    print("=" * 80)
    for fn_k, res in sequential_ablation_summary.items():
        print(f"{fn_k.upper()}: {res['Best Acquisition']} (Final Regret: {res['Mean Final Regret']}, AURC: {res['Mean AURC']})")
    print("=" * 80)

    plot_master_convergence_grid(all_functions_regrets, output_dir="week_08/diagnostics_results", filename="wk8_acquisition_ablation_results_all_functions.png")

    return sequential_ablation_summary
