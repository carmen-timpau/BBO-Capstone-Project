# Week 6 BBO - Function 1 Kernel Ablation Study

import numpy as np
import pandas as pd
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern, RBF, RationalQuadratic, WhiteKernel
from sklearn.metrics import root_mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Using `get_kernel_suite` function defined in `get_kernel_suite.py`

# Pulling Data for Function 1
X = np.array(data["function_1"]["x"])
Y = np.array(data["function_1"]["y"]).flatten()

# Preprocessing target for Function 1 (safe clipping + log10 scale)
Y_safe = np.clip(Y, 1e-300, None)
Y_log = np.log10(Y_safe)

n_samples, n_dims = X.shape

# Dynamically generating kernels matching Function 1's dimension
kernels_to_test = get_kernel_suite(n_dims)
ablation_results = []

# Running LOOCV loop for each candidate kernel
for name, kernel_candidate in kernels_to_test.items():
    f1_predictions = []
    
    # LOOCV Loop
    for j in range(n_samples):
        X_train = np.delete(X, j, axis=0)
        Y_train = np.delete(Y_log, j, axis=0)
        X_test = X[j].reshape(1, -1)
        
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        gp = GaussianProcessRegressor(
            kernel=kernel_candidate,
            alpha=0.0,
            normalize_y=True,
            n_restarts_optimizer=5,
            random_state=42
        )
        
        gp.fit(X_train_scaled, Y_train)
        y_pred = gp.predict(X_test_scaled)[0]
        f1_predictions.append(y_pred)
        
    f1_predictions = np.array(f1_predictions)
    
    # Calculating LOOCV metrics
    rmse = root_mean_squared_error(Y_log, f1_predictions)
    r2 = r2_score(Y_log, f1_predictions)
    
    # Performing Full Fit on All Data to compute Log Marginal Likelihood
    scaler_full = StandardScaler()
    X_full_scaled = scaler_full.fit_transform(X)
    
    gp_full = GaussianProcessRegressor(
        kernel=kernel_candidate,
        alpha=0.0,
        normalize_y=True,
        n_restarts_optimizer=5,
        random_state=42
    )
    gp_full.fit(X_full_scaled, Y_log)
    lml = gp_full.log_marginal_likelihood(gp_full.kernel_.theta)
    
    ablation_results.append({
        "Kernel Variant": name,
        "LOOCV RMSE": round(rmse, 5),
        "LOOCV R²": round(r2, 5),
        "Log Marginal Likelihood": round(lml, 3),
        "Learned Kernel": str(gp_full.kernel_)
    })

# Output results for Function 1
results_df = pd.DataFrame(ablation_results)
results_df = results_df.sort_values(by="LOOCV R²", ascending=False).reset_index(drop=True)

print("-" * 100)
print(f"                         FUNCTION 1 (Dim={n_dims}, N={n_samples}) - KERNEL ABLATION STUDY")
print("-" * 100)
print(results_df[["Kernel Variant", "LOOCV RMSE", "LOOCV R²", "Log Marginal Likelihood"]].to_string(index=False))

best_config = results_df.iloc[0]
print("\nTop Performing Kernel Config:")
print(f"  Name   : {best_config['Kernel Variant']}")
print(f"  Params : {best_config['Learned Kernel']}\n")
