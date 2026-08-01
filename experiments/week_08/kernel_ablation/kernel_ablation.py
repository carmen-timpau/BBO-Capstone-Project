# Week 8 BBO - Unified Kernel Ablation Study for Functions 1-8

import numpy as np
import pandas as pd
import warnings
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern, RBF, RationalQuadratic, WhiteKernel
from sklearn.metrics import root_mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

from kernels import get_kernel_suite, get_kernel_suite_f1

from sklearn.exceptions import ConvergenceWarning
warnings.filterwarnings("ignore", category=ConvergenceWarning)

NOISELESS_ALPHA = 1e-8  # small fixed jitter, not a learned hyperparameter


def run_kernel_ablation(data):
    # Storing winning configs for Functions 1-8 in a dictionary
    top_kernels_summary = {}

    # Iterating through Functions 1 to 8
    for fn_idx in range(1, 9):
        fn_key = f"function_{fn_idx}"

        # Checking if function exists in data dictionary
        if fn_key not in data:
            print(f"Skipping {fn_key}: Not found in data dictionary.")
            continue

        # Extracting X and Y
        X = np.array(data[fn_key]["x"])
        Y = np.array(data[fn_key]["y"]).flatten()

        n_samples, n_dims = X.shape

        # Applying special target preprocessing and kernel suite for Function 1
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
            kernels_to_test = get_kernel_suite_f1(n_dims)
        else:
            Y_target = Y

            # Dynamically generating kernels matching input dimension `n_dims`
            kernels_to_test = get_kernel_suite(n_dims)

        ablation_results = []

        # LOOCV loop for each candidate kernel
        for name, kernel_candidate in kernels_to_test.items():

            # Using a tiny numerical jitter only for kernels explicitly marked "Noiseless"
            # (i.e. no WhiteKernel component); everything else keeps alpha=0.0 and relies
            # on its own WhiteKernel term for numerical stability.
            alpha_value = NOISELESS_ALPHA if "Noiseless" in name else 0.0

            fn_predictions = []

            for j in range(n_samples):
                X_train = np.delete(X, j, axis=0)
                Y_train = np.delete(Y_target, j, axis=0)
                X_test = X[j].reshape(1, -1)

                # Scale features strictly per fold
                scaler = StandardScaler()
                X_train_scaled = scaler.fit_transform(X_train)
                X_test_scaled = scaler.transform(X_test)

                gp = GaussianProcessRegressor(
                    kernel=kernel_candidate,
                    alpha=alpha_value,
                    normalize_y=True,
                    n_restarts_optimizer=5,
                    random_state=42
                )

                gp.fit(X_train_scaled, Y_train)
                y_pred = gp.predict(X_test_scaled)[0]
                fn_predictions.append(y_pred)

            fn_predictions = np.array(fn_predictions)

            # Calculating LOOCV metrics
            rmse = root_mean_squared_error(Y_target, fn_predictions)
            r2 = r2_score(Y_target, fn_predictions)

            # Performing Full Fit on All Data to compute Log Marginal Likelihood
            scaler_full = StandardScaler()
            X_full_scaled = scaler_full.fit_transform(X)

            gp_full = GaussianProcessRegressor(
                kernel=kernel_candidate,
                alpha=alpha_value,
                normalize_y=True,
                n_restarts_optimizer=5,
                random_state=42
            )
            gp_full.fit(X_full_scaled, Y_target)
            lml = gp_full.log_marginal_likelihood(gp_full.kernel_.theta)

            ablation_results.append({
                "Kernel Variant": name,
                "LOOCV RMSE": round(rmse, 5),
                "LOOCV R²": round(r2, 5),
                "Log Marginal Likelihood": round(lml, 3),
                "Learned Kernel": str(gp_full.kernel_)
            })

        # Outputting results table for current function, sorted by LOOCV R² (descending)
        results_df = pd.DataFrame(ablation_results)
        results_df = results_df.sort_values(by="LOOCV R²", ascending=False).reset_index(drop=True)

        print("-" * 100)
        print(f"                    FUNCTION {fn_idx} (Dim={n_dims}, N={n_samples}) - KERNEL ABLATION STUDY")
        print("-" * 100)
        print(results_df[["Kernel Variant", "LOOCV RMSE", "LOOCV R²", "Log Marginal Likelihood"]].to_string(index=False))

        best_config = results_df.iloc[0]
        print("\nTop Performing Kernel Config:")
        print(f"  Name   : {best_config['Kernel Variant']}")
        print(f"  R²     : {best_config['LOOCV R²']}")
        print(f"  Params : {best_config['Learned Kernel']}\n")

        top_kernels_summary[fn_key] = {
            "Best Variant": best_config['Kernel Variant'],
            "LOOCV R²": best_config['LOOCV R²'],
            "Learned Kernel": best_config['Learned Kernel']
        }

    # Printing Overview Summary Across Functions 1-8
    print("#" * 100)
    print("                        FUNCTIONS 1 THROUGH 8 SUMMARY")
    print("#" * 100)
    summary_df = pd.DataFrame.from_dict(top_kernels_summary, orient='index')
    print(summary_df.to_string())

    return top_kernels_summary
