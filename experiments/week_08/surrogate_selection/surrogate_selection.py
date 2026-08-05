"""
Surrogate Model Selection and Comparative Analysis Module (using LOOCV)

Executing Leave-One-Out Cross-Validation (LOOCV) across all functions to compare 
ablation-tuned Gaussian Processes against Deep Ensembles using RMSE, and determine 
the optimal surrogate model for each function.
"""

import warnings
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import mean_squared_error

from gaussian_process.gaussian_process import evaluate_gaussian_process
from deep_ensemble.deep_ensemble import evaluate_deep_ensemble

warnings.filterwarnings("ignore")

def run_surrogate_comparison(data, top_kernels_summary, get_kernel_suite, get_kernel_suite_f1):
    """
    Coordinating the evaluation pipeline for Functions 1 through 8 using LOOCV, computing 
    out-of-fold RMSE for both models, selecting the best surrogate, and generating a summary.
    """
    surrogate_evaluation_summary = {}
    n_ensemble_members = 5
    loo = LeaveOneOut()

    # Counting to track overall model wins
    gp_wins = 0
    ensemble_wins = 0

    for fn_idx in range(1, 9):
        fn_key = f"function_{fn_idx}"

        if fn_key not in data:
            print(f"Skipping {fn_key}: Not found in data dictionary.")
            continue

        # Loading Data and Targeted Preprocessing
        X = np.array(data[fn_key]["x"])
        Y = np.array(data[fn_key]["y"]).flatten()
        n_samples, n_dims = X.shape

        # Function 1 special log-transform to handle numerical scale
        if fn_idx == 1:
            # Preprocessing target for Function 1 (data-driven floor + log10 scale)
            # Using the smallest genuine positive reading in this function's data as the
            # clipping floor, instead of an arbitrary 1e-300, so that negative/near-zero
            # noise points collapse to a value consistent with the data's own weakest
            # real signal rather than an extreme, unphysical outlier which confuses the
            # surrogate model fitting.
            positive_Y = Y[Y > 0]
            noise_floor = positive_Y.min()
            Y_safe = np.clip(Y, noise_floor, None)
            Y_target = np.log10(Y_safe)

            # Dynamically generating kernels matching Function 1's dimension
            kernel_suite = get_kernel_suite_f1(n_dims)

        else:
            Y_target = Y
            kernel_suite = get_kernel_suite(n_dims)

        # Scaling input features strictly using StandardScaler
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Retrieving Winning Kernel configuration
        kernel_info = top_kernels_summary.get(fn_key, {})
        winning_variant_name = kernel_info.get("Best Variant", "Standard RBF")
        
        best_kernel = kernel_suite.get(winning_variant_name, None)

        # Containers for Out-of-Fold predictions
        gp_oof_preds = np.zeros(n_samples)
        nn_ensemble_oof_preds = np.zeros(n_samples)

        # Leave-One-Out Cross-Validation Evaluation loop
        for train_idx, test_idx in loo.split(X_scaled):
            X_train, X_test = X_scaled[train_idx], X_scaled[test_idx]
            y_train, y_test = Y_target[train_idx], Y_target[test_idx]

            # Gaussian Process Evaluation
            gp_oof_preds[test_idx] = evaluate_gaussian_process(
                X_train, y_train, X_test, best_kernel
            )

            # Deep Ensemble Evaluation
            nn_ensemble_oof_preds[test_idx] = evaluate_deep_ensemble(
                X_train, y_train, X_test, n_ensemble_members
            )

        # Computing Root Mean Squared Error (RMSE) and selecting the best model
        gp_rmse = np.sqrt(mean_squared_error(Y_target, gp_oof_preds))
        nn_rmse = np.sqrt(mean_squared_error(Y_target, nn_ensemble_oof_preds))

        if nn_rmse < gp_rmse:
            best_model = "Deep Ensemble"
            ensemble_wins += 1
        else:
            best_model = "Gaussian Process"
            gp_wins += 1

        surrogate_evaluation_summary[fn_key] = {
            "Dim": n_dims,
            "Winning GP Kernel": winning_variant_name,
            "GP RMSE": gp_rmse,
            "Deep Ensemble RMSE": nn_rmse,
            "Best Surrogate": best_model
        }

    # Printing Comparison Table
    print("=" * 110)
    print("        SURROGATE MODELING PERFORMANCE COMPARISON (LOOCV: GP vs. Deep Ensemble RMSE)")
    print("=" * 110)

    for fn_key, info in surrogate_evaluation_summary.items():
        print(f"[{fn_key.upper()}] (Dim={info['Dim']})")
        print(f"  • Winning GP Kernel   : {info['Winning GP Kernel']}")
        print(f"  • GP RMSE             : {info['GP RMSE']:.4f}")
        print(f"  • Deep Ensemble RMSE  : {info['Deep Ensemble RMSE']:.4f}")
        print(f"  • Best Surrogate      : {info['Best Surrogate']}")
        print("-" * 110)

    # Printing Final Tally Summary
    print(f"\n[FINAL SUMMARY] Gaussian Process Wins: {gp_wins} | Deep Ensemble Wins: {ensemble_wins}")
    print("=" * 110)

    return surrogate_evaluation_summary
