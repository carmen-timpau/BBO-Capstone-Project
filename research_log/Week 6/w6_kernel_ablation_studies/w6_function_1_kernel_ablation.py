# Week 6 BBO - Function 1 Kernel Ablation Study

import numpy as np
import pandas as pd
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern, RBF, RationalQuadratic, WhiteKernel
from sklearn.metrics import root_mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Pulling Data for Function 1 and using clipping and log10 to prepare and scale outputs
X = np.array(data["function_1"]["x"])  # shape (15, 2)
Y = np.array(data["function_1"]["y"]).flatten()

Y_safe = np.clip(Y, 1e-300, None)
Y_log = np.log10(Y_safe)
n_samples = len(X)

# Defining Kernel Configurations to Test for Ablation Study
kernels_to_test = {
    "Baseline: Matern 2.5 + WhiteNoise (ARD)": (
        Matern(length_scale=[0.1, 0.1], nu=2.5, length_scale_bounds=(1e-6, 1e8)) +
        WhiteKernel(noise_level=1e-3, noise_level_bounds=(1e-6, 1e2))
    ),
    "Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)": (
        Matern(length_scale=[0.1, 0.1], nu=1.5, length_scale_bounds=(1e-6, 1e8)) +
        WhiteKernel(noise_level=1e-3, noise_level_bounds=(1e-6, 1e2))
    ),
    "Ablation 2: RBF + WhiteNoise (Smooth Gaussian)": (
        RBF(length_scale=[0.1, 0.1], length_scale_bounds=(1e-6, 1e8)) +
        WhiteKernel(noise_level=1e-3, noise_level_bounds=(1e-6, 1e2))
    ),
    "Ablation 3: Rational Quadratic + WhiteNoise": (
        RationalQuadratic(length_scale=0.1, alpha=1.0) +
        WhiteKernel(noise_level=1e-3, noise_level_bounds=(1e-6, 1e2))
    ),
    "Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)": (
        Matern(length_scale=[0.1, 0.1], nu=2.5, length_scale_bounds=(1e-6, 1e8))
    ),
    "Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale)": (
        Matern(length_scale=0.1, nu=2.5, length_scale_bounds=(1e-6, 1e8)) +
        WhiteKernel(noise_level=1e-3, noise_level_bounds=(1e-6, 1e2))
    )
}

ablation_results = []

# Running LOOCV and Full Fit Loop for each Kernel
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
    
    # Performing a Full Fit on All Data to get Log Marginal Likelihood (LML)
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

# Printing Kernel Ablation Results Summary Table
results_df = pd.DataFrame(ablation_results)
results_df = results_df.sort_values(by="LOOCV R²", ascending=False).reset_index(drop=True)

print("----------------------------------------------------------------------------------------------------")
print("                            FUNCTION 1 - KERNEL ABLATION STUDY RESULTS                              ")
print("----------------------------------------------------------------------------------------------------")
print(results_df[["Kernel Variant", "LOOCV RMSE", "LOOCV R²", "Log Marginal Likelihood"]].to_string(index=False))
print("\nTop Performing Kernel Config:")
print(f"Name   : {results_df.iloc[0]['Kernel Variant']}")
print(f"Params : {results_df.iloc[0]['Learned Kernel']}")
