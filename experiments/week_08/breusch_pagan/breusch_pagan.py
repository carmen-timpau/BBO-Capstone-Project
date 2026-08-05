# Week 8 BBO - Breusch-Pagan Homoscedasticity Analysis & Diagnostics for Functions 1-8
# Using the winning kernel objects dynamically retrieved from the previously completed Kernel Ablation Study

# BP Test only carried out for informational purposes, but was not implemented in the main pipeline for Week 8
# As the HEBO-inspired output warping was implemented instead and it is applied regardless of BP test results.

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import warnings

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import root_mean_squared_error, r2_score
from statsmodels.stats.diagnostic import het_breuschpagan
from sklearn.exceptions import ConvergenceWarning

from kernel_ablation.kernels import get_kernel_suite, get_kernel_suite_f1

warnings.filterwarnings("ignore", category=ConvergenceWarning)

def is_noiseless_kernel_name(kernel_name):
    """Returns True if the kernel name indicates a noiseless GP (Week 8 rule)."""
    return "Noiseless" in kernel_name

def run_bp(data, top_kernels_summary):

    fig, axes = plt.subplots(2, 4, figsize=(24, 12))
    axes = axes.flatten()

    breusch_pagan_summary = {}

    for fn_idx in range(1, 9):
        fn_key = f"function_{fn_idx}"
        ax = axes[fn_idx - 1]

        if fn_key not in data:
            ax.set_title(f"{fn_key}: Missing Data")
            ax.axis('off')
            continue

        # Extracting data
        X = np.array(data[fn_key]["x"])
        Y_raw = np.array(data[fn_key]["y"]).flatten()
        n_samples, n_dims = X.shape

        # Week 8 Function 1 preprocessing (data-driven floor + log10)
        if fn_idx == 1:
            positive_Y = Y_raw[Y_raw > 0]
            if positive_Y.size == 0:
                raise ValueError("Function 1 contains no positive Y values; cannot apply log10 transform.")
            noise_floor = positive_Y.min()
            Y_target = np.log10(np.clip(Y_raw, noise_floor, None))
        else:
            Y_target = Y_raw

        # Retrieving winning kernel from Week 8 kernel ablation
        winning_variant_name = top_kernels_summary[fn_key]["Best Variant"]

        # Rebuilding kernel suite (Week 8)
        kernel_suite = get_kernel_suite_f1(n_dims) if fn_idx == 1 else get_kernel_suite(n_dims)
        best_kernel = kernel_suite[winning_variant_name]

        alpha_value = 1e-8 if is_noiseless_kernel_name(winning_variant_name) else 0.0

        fn_predictions = []
        fn_residuals = []
        fn_fold_lmls = []

        # LOOCV loop (Week 8: per-fold scaling)
        for j in range(n_samples):
            X_train = np.delete(X, j, axis=0)
            Y_train = np.delete(Y_target, j, axis=0)
            X_test = X[j].reshape(1, -1)
            Y_test = Y_target[j]

            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            gp = GaussianProcessRegressor(
                kernel=best_kernel,
                alpha=alpha_value,
                normalize_y=True,
                n_restarts_optimizer=5,
                random_state=42,
            )

            gp.fit(X_train_scaled, Y_train)
            y_pred = gp.predict(X_test_scaled)[0]

            fn_predictions.append(y_pred)
            fn_residuals.append(Y_test - y_pred)
            fn_fold_lmls.append(gp.log_marginal_likelihood(gp.kernel_.theta))

        fn_predictions = np.array(fn_predictions)
        fn_residuals = np.array(fn_residuals)

        # RMSE & R²
        fn_rmse = root_mean_squared_error(Y_target, fn_predictions)
        fn_r2 = r2_score(Y_target, fn_predictions)

        # Full fit for LML
        scaler_full = StandardScaler()
        X_full_scaled = scaler_full.fit_transform(X)

        gp_full = GaussianProcessRegressor(
            kernel=best_kernel,
            alpha=alpha_value,
            normalize_y=True,
            n_restarts_optimizer=5,
            random_state=42,
        )
        gp_full.fit(X_full_scaled, Y_target)
        full_lml = gp_full.log_marginal_likelihood(gp_full.kernel_.theta)
        mean_loocv_lml = np.mean(fn_fold_lmls)

        # Breusch-Pagan test
        X_test_matrix = sm.add_constant(fn_predictions)
        lm_stat, p_value, f_stat, f_p_value = het_breuschpagan(fn_residuals, X_test_matrix)

        hetero_label = "Heteroscedastic" if p_value < 0.05 else "Homoscedastic"

        breusch_pagan_summary[fn_key] = {
            "Dim": n_dims,
            "N_Samples": n_samples,
            "Winning Kernel": winning_variant_name,
            "RMSE": fn_rmse,
            "R2": fn_r2,
            "BP_Lagrange_Multiplier": lm_stat,
            "BP_P_Value": p_value,
            "Verdict": hetero_label
        }

        # Plot residuals
        ax.scatter(fn_predictions, fn_residuals, color="darkviolet", alpha=0.7, edgecolors="k", s=50)
        ax.axhline(y=0, color="black", linestyle="--", linewidth=2)

        title_target_label = r"\hat{y}" if fn_idx != 1 else r"\hat{\log_{10}(y)}"
        ylabel_target = "Residual" if fn_idx != 1 else "Residual ($\log_{10}$)"

        ax.set_title(
            f"Function {fn_idx} — {hetero_label} (N={n_samples})\nRMSE: {fn_rmse:.3f} | R²: {fn_r2:.3f} | BP p: {p_value:.4f}",
            fontsize=11,
            fontweight="bold",
        )
        ax.set_xlabel(f"Predicted Value (${title_target_label}$)", fontsize=8)
        ax.set_ylabel(ylabel_target, fontsize=8)
        ax.grid(True, linestyle=":", alpha=0.6)

        print("=" * 75)
        print(f"FUNCTION {fn_idx} — Week 8 Breusch-Pagan Diagnostics")
        print("=" * 75)
        print(f"Full LML: {full_lml:.3f}")
        print(f"Mean LOOCV LML: {mean_loocv_lml:.3f}")
        print(f"RMSE: {fn_rmse:.4f}")
        print(f"R²: {fn_r2:.4f}")
        print(f"BP p-value: {p_value:.5f}")
        print(f"Verdict: {hetero_label}")
        print("-" * 75)
        print(f"Learned Kernel:\n{gp_full.kernel_}")
        print("=" * 75, "\n")

    # Saving plot into diagnostics_results folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'diagnostics_results'))
    os.makedirs(output_dir, exist_ok=True)

    plt.tight_layout()
    output_filename = os.path.join(output_dir, 'wk8_breusch_pagan_all_functions.png')
    fig.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"All residual plots successfully saved to '{output_filename}'")
    plt.show()

    return breusch_pagan_summary
