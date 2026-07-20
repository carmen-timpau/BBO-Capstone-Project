# Week 6 BBO - Breusch-Pagan Homoscedasticity Analysis & Diagnostics for Functions 1-8
# Using the winning kernel objects dynamically retrieved from the previously completed Kernel Ablation Study

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import warnings

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern, RBF, RationalQuadratic, WhiteKernel
from sklearn.metrics import root_mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.diagnostic import het_breuschpagan
from sklearn.exceptions import ConvergenceWarning

warnings.filterwarnings("ignore", category=ConvergenceWarning)

# Using `get_kernel_suite_f1` function defined in `get_kernel_suite_f1.py`
# Using `get_kernel_suite` function defined in `get_kernel_suite.py`

# Running Diagnostics and Breusch-Pagan Test across Functions 1 to 8
for fn_idx in range(1, 9):
    fn_key = f"function_{fn_idx}"

    if fn_key not in data:
        continue

    # Extracting Data
    X = np.array(data[fn_key]["x"])
    Y = np.array(data[fn_key]["y"]).flatten()
    n_samples, n_dims = X.shape

    # Preprocessing target for Function 1 (safe clipping + log10 scale)
    if fn_idx == 1:
        Y_safe = np.clip(Y, 1e-300, None)
        Y_target = np.log10(Y_safe)
    else:
        Y_target = Y

    # Retrieving the winning kernel variant name stored in top_kernels_summary
    winning_variant_name = top_kernels_summary[fn_key]["Best Variant"]

    # Re-instantiating a fresh instance of the winning kernel configuration from the suite
    kernel_suite = get_kernel_suite_f1(n_dims) if fn_idx == 1 else get_kernel_suite(n_dims)
    best_kernel = kernel_suite[winning_variant_name]

    fn_predictions = []
    fn_residuals = []
    fn_fold_lmls = []

    # Running LOOCV Loop across all points using the winning GP configuration
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
            alpha=0.0,
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

    # Calculating RMSE & R²
    fn_rmse = root_mean_squared_error(Y_target, fn_predictions)
    fn_r2 = r2_score(Y_target, fn_predictions)

    # Fitting Full Dataset for Log Marginal Likelihood and Learned Kernel Parameters
    scaler_full = StandardScaler()
    X_full_scaled = scaler_full.fit_transform(X)

    gp_full = GaussianProcessRegressor(
        kernel=best_kernel,
        alpha=0.0,
        normalize_y=True,
        n_restarts_optimizer=5,
        random_state=42,
    )
    gp_full.fit(X_full_scaled, Y_target)
    full_lml = gp_full.log_marginal_likelihood(gp_full.kernel_.theta)
    mean_loocv_lml = np.mean(fn_fold_lmls)

    # Performing Breusch-Pagan test
    X_test_matrix = sm.add_constant(fn_predictions)
    lm_stat, p_value, f_stat, f_p_value = het_breuschpagan(
        fn_residuals, X_test_matrix
    )

    # Plotting Residuals vs GP Predictions
    plt.figure(figsize=(8, 5))
    plt.scatter(
        fn_predictions,
        fn_residuals,
        color="darkviolet",
        alpha=0.7,
        edgecolors="k",
        s=50,
        zorder=2,
    )
    plt.axhline(y=0, color="black", linestyle="--", linewidth=2, zorder=1)

    title_target_label = "\hat{y}" if fn_idx != 1 else "\hat{\log_{10}(y)}"
    ylabel_target = "Residual ($y - \hat{y}$)" if fn_idx != 1 else "Residual ($\log_{10}(y) - \hat{\log_{10}(y)}$)"

    plt.title(
        f"Function {fn_idx}, Week 5: LOOCV Residuals vs. Predictions (N={n_samples})\n"
        f"RMSE: {fn_rmse:.4f} | LOOCV R-squared Score: {fn_r2:.4f} | Breusch-Pagan p-value: {p_value:.5f}",
        fontsize=11,
        fontweight="bold",
    )
    plt.xlabel(f"Predicted Value (${title_target_label}$)", fontsize=10)
    plt.ylabel(ylabel_target, fontsize=10)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    plt.show()

    # Formatting display title for winning variant
    winning_title = (
        winning_variant_name.split(":")[1].strip().upper()
        if ":" in winning_variant_name
        else winning_variant_name.upper()
    )

    # Printing Diagnostics and Results
    print(
        "=========================================================================="
    )
    print(
        f"     FUNCTION {fn_idx} DIAGNOSTICS — WINNING CONFIG: {winning_title}"
    )
    print(
        "=========================================================================="
    )
    print(f"Full Dataset Log Marginal Likelihood (LML) : {full_lml:.3f}")
    print(f"Mean LOOCV Fold Log Marginal Likelihood    : {mean_loocv_lml:.3f}")
    print(f"LOOCV Root Mean Squared Error (RMSE)       : {fn_rmse:.4f}")
    print(f"LOOCV R-squared Score                      : {fn_r2:.4f}")
    print(f"Breusch-Pagan Test p-value                 : {p_value:.5f}")
    print(
        "--------------------------------------------------------------------------"
    )
    print(f"Learned Kernel Parameters:\n{gp_full.kernel_}")
    print(
        "--------------------------------------------------------------------------"
    )

    if p_value < 0.05:
        print(
            f"Verdict for Function {fn_idx} ({n_samples} datapoints, Week 5): Statistically HETEROSCEDASTIC"
        )
    else:
        print(
            f"Verdict for Function {fn_idx} ({n_samples} datapoints, Week 5): Statistically HOMOSCEDASTIC"
        )
    print(
        "==========================================================================\n"
    )
