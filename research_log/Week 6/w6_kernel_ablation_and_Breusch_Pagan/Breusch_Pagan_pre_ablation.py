# Week 6 BBO - Breusch-Pagan test to assess Homo/Heteroscedasticity across Functions 1-8 Pre-Kernel Ablation Studies
# Using datasets collected after obtaining Week 5's query output 
# Performed before performing Kernel Ablation Studies, using GPs of Week 5's strategies for each function 
# Performed for pre-/post-kernel comparative purposes - only post-ablation results are considered

import warnings
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern, RBF, WhiteKernel
from sklearn.metrics import root_mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.diagnostic import het_breuschpagan
from sklearn.exceptions import ConvergenceWarning

# Filtering out ConvergenceWarning
warnings.filterwarnings("ignore", category=ConvergenceWarning)

def run_pre_bp(data):
    # Defining specific Week 5 pre-ablation GP configurations and plotting aesthetics per function
    # All functions are configured to perform feature scaling on X
    function_configs = {
        1: {
            "kernel": Matern(length_scale=[0.1, 0.1], nu=1.5, length_scale_bounds=(1e-6, 1e8)) + WhiteKernel(noise_level=1e-6, noise_level_bounds=(1e-16, 1e-2)),
            "color": "gold"
        },
        2: {
            "kernel": RBF(length_scale=[0.1]*2, length_scale_bounds=(1e-6, 1e8)) + WhiteKernel(noise_level=0.05, noise_level_bounds=(1e-4, 1.0)),
            "color": "darkviolet"
        },
        3: {
            "kernel": RBF(length_scale=[1.0]*3, length_scale_bounds=(1e-6, 1e8)) + WhiteKernel(noise_level=0.5, noise_level_bounds=(1e-4, 1.0)),
            "color": "royalblue"
        },
        4: {
            "kernel": RBF(length_scale=[0.1]*4, length_scale_bounds=(1e-6, 1e8)) + WhiteKernel(noise_level=60.0, noise_level_bounds=(1e-3, 1e4)),
            "color": "crimson"
        },
        5: {
            "kernel": RBF(length_scale=[0.1]*4) + WhiteKernel(noise_level=7.4e4, noise_level_bounds=(1e-3, 1e7)),
            "color": "mediumpurple"
        },
        6: {
            "kernel": RBF(length_scale=[1.0]*5, length_scale_bounds=(1e-6, 1e8)) + WhiteKernel(noise_level=0.2, noise_level_bounds=(1e-8, 5.0)),
            "color": "forestgreen"
        },
        7: {
            "kernel": RBF(length_scale=[0.5]*6) + WhiteKernel(noise_level=0.12, noise_level_bounds=(1e-3, 3.0)),
            "color": "darkorange"
        },
        8: {
            "kernel": RBF(length_scale=[1.0]*8, length_scale_bounds=(1e-6, 1e8)) + WhiteKernel(noise_level=0.3, noise_level_bounds=(1e-12, 10.0)),
            "color": "teal"
        }
    }

    # Running diagnostic tests sequentially for Functions 1 through 8
    for fn_idx in range(1, 9):
        fn_key = f"function_{fn_idx}"
        
        if fn_key not in data:
            print(f"Skipping {fn_key}: Not found in data dictionary.")
            continue

        # Pulling updated function data
        X = np.array(data[fn_key]["x"])
        Y = np.array(data[fn_key]["y"]).flatten()
        n_samples = len(X)

        cfg = function_configs[fn_idx]

        # Special log transformation handling for Function 1
        if fn_idx == 1:
            # Transforming Y to log10 space to avoid numerical underflow issues with extreme values
            Y_safe = np.clip(Y, 1e-300, None)  # Clipping to prevent log10(0) from producing NaN
            Y_target = np.log10(Y_safe)
        else:
            Y_target = Y

        fn_predictions = []
        fn_residuals = []
        fn_fold_lmls = []

        # Running LOOCV Loop across points using Week 5's GP parameters
        for j in range(n_samples):
            X_train = np.delete(X, j, axis=0)
            Y_train = np.delete(Y_target, j, axis=0)
            X_test = X[j].reshape(1, -1)
            Y_test = Y_target[j]

            # Standardizing input features strictly per fold to prevent data leakage
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            gp = GaussianProcessRegressor(
                kernel=cfg["kernel"],
                alpha=0.0,
                normalize_y=True,
                n_restarts_optimizer=5,
                random_state=42
            )

            gp.fit(X_train_scaled, Y_train)
            y_pred = gp.predict(X_test_scaled)[0]

            fn_predictions.append(y_pred)
            fn_residuals.append(Y_test - y_pred)
            fn_fold_lmls.append(gp.log_marginal_likelihood(gp.kernel_.theta))

        fn_predictions = np.array(fn_predictions)
        fn_residuals = np.array(fn_residuals)

        # Calculating RMSE and R-squared score
        fn_rmse = root_mean_squared_error(Y_target, fn_predictions)
        fn_r2 = r2_score(Y_target, fn_predictions)

        # Fitting Full Dataset for Log Marginal Likelihood and Learned Kernel Parameters
        scaler_full = StandardScaler()
        X_full_scaled = scaler_full.fit_transform(X)

        gp_full = GaussianProcessRegressor(
            kernel=cfg["kernel"],
            alpha=0.0,
            normalize_y=True,
            n_restarts_optimizer=5,
            random_state=42
        )
        gp_full.fit(X_full_scaled, Y_target)
        full_lml = gp_full.log_marginal_likelihood(gp_full.kernel_.theta)
        mean_loocv_lml = np.mean(fn_fold_lmls)

        # Performing a Breusch-Pagan test to assess Homo/Heteroscedasticity
        X_test_matrix = sm.add_constant(fn_predictions)
        lm_stat, p_value, f_stat, f_p_value = het_breuschpagan(fn_residuals, X_test_matrix)

        # Setting up dynamic plot labels for log-scaled vs raw output functions
        title_scale = " (Log Scale)" if fn_idx == 1 else ""
        xlabel_str = 'Predicted Log Value ($\hat{y}_{log}$)' if fn_idx == 1 else 'Predicted Value ($\hat{y}$)'
        ylabel_str = 'Log Residual ($y_{log} - \hat{y}_{log}$)' if fn_idx == 1 else 'Residual ($y - \hat{y}$)'
        hline_color = 'black' if fn_idx in [1, 2, 3, 4] else 'crimson'

        # Plotting Residuals vs GP Predictions
        plt.figure(figsize=(8, 5))
        plt.scatter(fn_predictions, fn_residuals, color=cfg["color"], alpha=0.7, edgecolors='k', s=50, zorder=2)
        plt.axhline(y=0, color=hline_color, linestyle='--', linewidth=2, zorder=1)

        plt.title(
            f'Function {fn_idx}, Week 5{title_scale}: LOOCV Residuals vs. Predictions (N={n_samples})\n'
            f'RMSE: {fn_rmse:.4f}  | LOOCV R-squared Score: {fn_r2:.4f} | Breusch-Pagan p-value: {p_value:.5f}',
            fontsize=11, fontweight='bold'
        )
        plt.xlabel(xlabel_str, fontsize=10)
        plt.ylabel(ylabel_str, fontsize=10)
        plt.grid(True, linestyle=':', alpha=0.6)
        plt.tight_layout()
        plt.show()

        # Title label for diagnostic header
        winning_title = "WEEK 5 PRE-ABLATION BASELINE"

        # Printing Diagnostics and Results
        print("==========================================================================")
        print(f"     FUNCTION {fn_idx} DIAGNOSTICS — CONFIG: {winning_title}")
        print("==========================================================================")
        print(f"Full Dataset Log Marginal Likelihood (LML) : {full_lml:.3f}")
        print(f"Mean LOOCV Fold Log Marginal Likelihood    : {mean_loocv_lml:.3f}")
        print(f"LOOCV Root Mean Squared Error (RMSE)       : {fn_rmse:.4f}")
        print(f"LOOCV R-squared Score                      : {fn_r2:.4f}")
        print(f"Breusch-Pagan Test p-value                 : {p_value:.5f}")
        print("--------------------------------------------------------------------------")
        print(f"Learned Kernel Parameters:\n{gp_full.kernel_}")
        print("--------------------------------------------------------------------------")

        if p_value < 0.05:
            print(f"Verdict for Function {fn_idx} ({n_samples} datapoints, Week 5): Statistically HETEROSCEDASTIC")
        else:
            print(f"Verdict for Function {fn_idx} ({n_samples} datapoints, Week 5): Statistically HOMOSCEDASTIC")
        print("==========================================================================\n")        "color": "crimson"
    },
    5: {
        "kernel": RBF(length_scale=[0.1]*4) + WhiteKernel(noise_level=7.4e4, noise_level_bounds=(1e-3, 1e7)),
        "color": "mediumpurple"
    },
    6: {
        "kernel": RBF(length_scale=[1.0]*5, length_scale_bounds=(1e-6, 1e8)) + WhiteKernel(noise_level=0.2, noise_level_bounds=(1e-8, 5.0)),
        "color": "forestgreen"
    },
    7: {
        "kernel": RBF(length_scale=[0.5]*6) + WhiteKernel(noise_level=0.12, noise_level_bounds=(1e-3, 3.0)),
        "color": "darkorange"
    },
    8: {
        "kernel": RBF(length_scale=[1.0]*8, length_scale_bounds=(1e-6, 1e8)) + WhiteKernel(noise_level=0.3, noise_level_bounds=(1e-12, 10.0)),
        "color": "teal"
    }
}

# Running diagnostic tests sequentially for Functions 1 through 8
for fn_idx in range(1, 9):
    fn_key = f"function_{fn_idx}"
    
    if fn_key not in data:
        print(f"Skipping {fn_key}: Not found in data dictionary.")
        continue

    # Pulling updated function data
    X = np.array(data[fn_key]["x"])
    Y = np.array(data[fn_key]["y"]).flatten()
    n_samples = len(X)

    cfg = function_configs[fn_idx]

    # Special log transformation handling for Function 1
    if fn_idx == 1:
        # Transforming Y to log10 space to avoid numerical underflow issues with extreme values
        Y_safe = np.clip(Y, 1e-300, None)  # Clipping to prevent log10(0) from producing NaN
        Y_target = np.log10(Y_safe)
    else:
        Y_target = Y

    fn_predictions = []
    fn_residuals = []
    fn_fold_lmls = []

    # Running LOOCV Loop across points using Week 5's GP parameters
    for j in range(n_samples):
        X_train = np.delete(X, j, axis=0)
        Y_train = np.delete(Y_target, j, axis=0)
        X_test = X[j].reshape(1, -1)
        Y_test = Y_target[j]

        # Standardizing input features strictly per fold to prevent data leakage
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        gp = GaussianProcessRegressor(
            kernel=cfg["kernel"],
            alpha=0.0,
            normalize_y=True,
            n_restarts_optimizer=5,
            random_state=42
        )

        gp.fit(X_train_scaled, Y_train)
        y_pred = gp.predict(X_test_scaled)[0]

        fn_predictions.append(y_pred)
        fn_residuals.append(Y_test - y_pred)
        fn_fold_lmls.append(gp.log_marginal_likelihood(gp.kernel_.theta))

    fn_predictions = np.array(fn_predictions)
    fn_residuals = np.array(fn_residuals)

    # Calculating RMSE and R-squared score
    fn_rmse = root_mean_squared_error(Y_target, fn_predictions)
    fn_r2 = r2_score(Y_target, fn_predictions)

    # Fitting Full Dataset for Log Marginal Likelihood and Learned Kernel Parameters
    scaler_full = StandardScaler()
    X_full_scaled = scaler_full.fit_transform(X)

    gp_full = GaussianProcessRegressor(
        kernel=cfg["kernel"],
        alpha=0.0,
        normalize_y=True,
        n_restarts_optimizer=5,
        random_state=42
    )
    gp_full.fit(X_full_scaled, Y_target)
    full_lml = gp_full.log_marginal_likelihood(gp_full.kernel_.theta)
    mean_loocv_lml = np.mean(fn_fold_lmls)

    # Performing a Breusch-Pagan test to assess Homo/Heteroscedasticity
    X_test_matrix = sm.add_constant(fn_predictions)
    lm_stat, p_value, f_stat, f_p_value = het_breuschpagan(fn_residuals, X_test_matrix)

    # Setting up dynamic plot labels for log-scaled vs raw output functions
    title_scale = " (Log Scale)" if fn_idx == 1 else ""
    xlabel_str = 'Predicted Log Value ($\hat{y}_{log}$)' if fn_idx == 1 else 'Predicted Value ($\hat{y}$)'
    ylabel_str = 'Log Residual ($y_{log} - \hat{y}_{log}$)' if fn_idx == 1 else 'Residual ($y - \hat{y}$)'
    hline_color = 'black' if fn_idx in [1, 2, 3, 4] else 'crimson'

    # Plotting Residuals vs GP Predictions
    plt.figure(figsize=(8, 5))
    plt.scatter(fn_predictions, fn_residuals, color=cfg["color"], alpha=0.7, edgecolors='k', s=50, zorder=2)
    plt.axhline(y=0, color=hline_color, linestyle='--', linewidth=2, zorder=1)

    plt.title(
        f'Function {fn_idx}, Week 5{title_scale}: LOOCV Residuals vs. Predictions (N={n_samples})\n'
        f'RMSE: {fn_rmse:.4f}  | LOOCV R-squared Score: {fn_r2:.4f} | Breusch-Pagan p-value: {p_value:.5f}',
        fontsize=11, fontweight='bold'
    )
    plt.xlabel(xlabel_str, fontsize=10)
    plt.ylabel(ylabel_str, fontsize=10)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()
    plt.show()

    # Title label for diagnostic header
    winning_title = "WEEK 5 PRE-ABLATION BASELINE"

    # Printing Diagnostics and Results
    print(
        "=========================================================================="
    )
    print(
        f"     FUNCTION {fn_idx} DIAGNOSTICS — CONFIG: {winning_title}"
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
