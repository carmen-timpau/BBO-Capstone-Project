# Week 6 BBO - LOOCV Acquisition Function Ablation Study (Functions 1-8)
# Using best performing kernels found for each function through the Kernel Ablation Study ran beforehand

import numpy as np
import pandas as pd
import warnings
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.exceptions import ConvergenceWarning

warnings.filterwarnings("ignore", category=ConvergenceWarning)
warnings.filterwarnings("ignore", message="Predicted variances smaller than 0", category=UserWarning,)

# Acquisition Functions (Designed for Batch/Vector Inputs)
def compute_acquisition_scores(X_cand, gp, y_best, acq_type, param=0.01):
    """Computes acquisition scores for a given GP and candidate points."""
    mu, sigma = gp.predict(X_cand, return_std=True)
    sigma = np.maximum(sigma, 1e-9)
    
    if acq_type == "EI":
        # param = xi (exploration trade-off)
        improvement = mu - y_best - param
        Z = improvement / sigma
        return improvement * norm.cdf(Z) + sigma * norm.pdf(Z)

    elif acq_type == "UCB":
        # param = beta (confidence multiplier)
        return mu + param * sigma

    elif acq_type == "PI":
        # param = xi
        improvement = mu - y_best - param
        Z = improvement / sigma
        return norm.cdf(Z)

# LOOCV Acquisition Function Ablation Study
acq_ablation_summary = {}

# Defining candidate acquisition strategies to evaluate
acq_strategies = {
    "EI (xi=0.01)": ("EI", 0.01),
    "EI (Exploration, xi=0.1)": ("EI", 0.10),
    "UCB (beta=1.96)": ("UCB", 1.96),
    "UCB (beta=2.58)": ("UCB", 2.58),
    "PI (xi=0.01)": ("PI", 0.01),
}

for fn_idx in range(1, 9):
    fn_key = f"function_{fn_idx}"

    if fn_key not in data:
        continue

    X = np.array(data[fn_key]["x"])
    Y = np.array(data[fn_key]["y"]).flatten()
    n_samples, n_dims = X.shape

    # Targeted preprocessing (Function 1 log10 transformation required only)
    if fn_idx == 1:
        Y_safe = np.clip(Y, 1e-300, None)
        Y_target = np.log10(Y_safe)
    else:
        Y_target = Y

    # Retrieving winning kernel and learned parameters from previous kernel ablation study
    winning_variant_name = top_kernels_summary[fn_key]["Best Variant"]
    learned_kernel_params = top_kernels_summary[fn_key].get("Learned Kernel", "N/A")
    winning_r2 = top_kernels_summary[fn_key].get("LOOCV R²", "N/A")

    kernel_suite = get_kernel_suite_f1(n_dims) if fn_idx == 1 else get_kernel_suite(n_dims)
    best_kernel = kernel_suite[winning_variant_name]

    # Dictionary to collect scores across all LOOCV folds
    strategy_loocv_scores = {strat: [] for strat in acq_strategies}

    # LOOCV Loop across all data points
    for j in range(n_samples):
        X_train = np.delete(X, j, axis=0)
        Y_train = np.delete(Y_target, j, axis=0)
        X_test = X[j].reshape(1, -1)
        Y_test = Y_target[j]

        # Scaling features strictly per fold
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Fitting GP on training fold
        gp = GaussianProcessRegressor(
            kernel=best_kernel,
            alpha=0.0,
            normalize_y=True,
            n_restarts_optimizer=5,
            random_state=42,
        )
        gp.fit(X_train_scaled, Y_train)

        y_best_fold = np.max(Y_train)

        # Calculating acquisition scores for held-out point and training points
        for strat_name, (acq_type, param) in acq_strategies.items():
            test_score = compute_acquisition_scores(
                X_test_scaled, gp, y_best_fold, acq_type, param
            )[0]
            train_scores = compute_acquisition_scores(
                X_train_scaled, gp, y_best_fold, acq_type, param
            )

            # Measuring relative rank: Percentage of training points the held-out point beat
            rank_percentile = (np.sum(train_scores < test_score) / len(train_scores)) * 100
            strategy_loocv_scores[strat_name].append(rank_percentile)

    # Compiling LOOCV results for this function
    acq_results = []
    for strat_name, percentiles in strategy_loocv_scores.items():
        acq_results.append({
            "Acquisition Variant": strat_name,
            "Mean LOOCV Rank Percentile (%)": round(np.mean(percentiles), 2),
            "Median LOOCV Rank Percentile (%)": round(np.median(percentiles), 2),
            "Std Dev (%)": round(np.std(percentiles), 2)
        })

    acq_df = pd.DataFrame(acq_results)
    acq_df = acq_df.sort_values(by="Mean LOOCV Rank Percentile (%)", ascending=False).reset_index(drop=True)

    # Formatting display title for winning variant
    winning_title = (
        winning_variant_name.split(":")[1].strip().upper()
        if ":" in winning_variant_name
        else winning_variant_name.upper()
    )

    print("=" * 105)
    print(f"       FUNCTION {fn_idx} (Dim={n_dims}, N={n_samples}) — LOOCV ACQUISITION ABLATION STUDY")
    print("=" * 105)
    print(acq_df.to_string(index=False))
    print("-" * 105)

    best_acq = acq_df.iloc[0]

    # Printing Best Model from Kernel Ablation & Acquisition Diagnostics
    print("==========================================================================")
    print(f"     FUNCTION {fn_idx} SUMMARY — BEST KERNEL & ACQUISITION CONFIG")
    print("==========================================================================")
    print(f"Best Kernel Variant (Kernel Ablation) : {winning_title}")
    print(f"Kernel Ablation LOOCV R² Score        : {winning_r2}")
    print("--------------------------------------------------------------------------")
    print(f"Learned Kernel Parameters:\n{learned_kernel_params}")
    print("--------------------------------------------------------------------------")
    print(f"Winning Acquisition Strategy          : {best_acq['Acquisition Variant']}")
    print(f"Mean LOOCV Rank Percentile            : {best_acq['Mean LOOCV Rank Percentile (%)']}%")
    print("==========================================================================\n")

    acq_ablation_summary[fn_key] = {
        "Best Kernel Variant": winning_title,
        "Best Acquisition": best_acq["Acquisition Variant"],
        "Mean Rank Percentile": best_acq["Mean LOOCV Rank Percentile (%)"]
    }
