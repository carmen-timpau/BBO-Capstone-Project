# Week 6 BBO - Breusch-Pagan test to assess Homo/Heteroscedasticity for Function 2
# Using Function 2 dataset of 15 points collected after obtaining Week 5's query output 
# Performed before submitting Week 6 query to inform future strategic changes
# Using newfound GP post-kernel ablation study for Function 2 to remove bias from Week 5's GP for Function 2
# These GP hyperparameters will be used to generate Week 6 query prediction for Function 2, as these give unbiased test results

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RationalQuadratic, WhiteKernel
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.diagnostic import het_breuschpagan

# Pulling updated Function 2 data (15 points, Week 5)
X = np.array(data["function_2"]["x"])  # shape (15, 2)
Y = np.array(data["function_2"]["y"]).flatten()  # shape (15,)

n_samples = len(X)
f2_predictions = []
f2_residuals = []
f2_fold_lmls = []

# Running LOOCV Loop across all 15 points using post-ablation GP for Function 2 that removes bias from Week 5's GP for Function 2
for j in range(n_samples):
    X_train = np.delete(X, j, axis=0)
    Y_train = np.delete(Y, j, axis=0)
    X_test = X[j].reshape(1, -1)
    Y_test = Y[j]
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    kernel = RationalQuadratic(length_scale=0.1, alpha=1.0) + \
             WhiteKernel(noise_level=1e-3, noise_level_bounds=(1e-6, 1e2))
    
    gp = GaussianProcessRegressor(
        kernel=kernel, 
        alpha=0.0, 
        normalize_y=True, 
        n_restarts_optimizer=5, 
        random_state=42
    )
    
    gp.fit(X_train_scaled, Y_train)
    y_pred = gp.predict(X_test_scaled)[0]
    
    f2_predictions.append(y_pred)
    f2_residuals.append(Y_test - y_pred)
    f2_fold_lmls.append(gp.log_marginal_likelihood(gp.kernel_.theta))

f2_predictions = np.array(f2_predictions)
f2_residuals = np.array(f2_residuals)

# Calculating RMSE
f2_rmse = root_mean_squared_error(Y, f2_predictions)

# Calculating R-squared score using true Y values and LOOCV predictions
f2_r2 = r2_score(Y, f2_predictions)

# Fit Full Dataset for Log Marginal Likelihood and Learned Kernel Parameters
scaler_full = StandardScaler()
X_full_scaled = scaler_full.fit_transform(X)

kernel_full = RationalQuadratic(length_scale=0.1, alpha=1.0) + \
              WhiteKernel(noise_level=1e-3, noise_level_bounds=(1e-6, 1e2))

gp_full = GaussianProcessRegressor(
    kernel=kernel_full,
    alpha=0.0,
    normalize_y=True,
    n_restarts_optimizer=5,
    random_state=42
)
gp_full.fit(X_full_scaled, Y)
full_lml = gp_full.log_marginal_likelihood(gp_full.kernel_.theta)
mean_loocv_lml = np.mean(f2_fold_lmls)

# Performing a Breusch-Pagan test to assess Homo/Heteroscedasticity - Checking if the residuals can be predicted by the model's predictions
# Adding a constant (intercept) term for the linear regression check
X_test_matrix = sm.add_constant(f2_predictions)
lm_stat, p_value, f_stat, f_p_value = het_breuschpagan(f2_residuals, X_test_matrix)

# Plotting the Residuals vs GP Predictions (generated using LOOCV) for Function 2
plt.figure(figsize=(8, 5))
plt.scatter(f2_predictions, f2_residuals, color='darkviolet', alpha=0.7, edgecolors='k', s=50, zorder=2)
plt.axhline(y=0, color='black', linestyle='--', linewidth=2, zorder=1)

plt.title(f'Function 2, Week 5: LOOCV Residuals vs. Predictions (N={n_samples})\n'
          f'RMSE: {f2_rmse:.4f} | LOOCV R-squared Score: {f2_r2:.4f} |  Breusch-Pagan p-value: {p_value:.5f}', 
          fontsize=11, fontweight='bold')
plt.xlabel('Predicted Value ($\hat{y}$)', fontsize=10)
plt.ylabel('Residual ($y - \hat{y}$)', fontsize=10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()

# Printing Diagnostics and Results
print("==========================================================================")
print("     FUNCTION 2 DIAGNOSTICS — WINNING CONFIG: RATIONAL QUADRATIC + NOISE ")
print("==========================================================================")
print(f"Full Dataset Log Marginal Likelihood (LML) : {full_lml:.3f}")
print(f"Mean LOOCV Fold Log Marginal Likelihood    : {mean_loocv_lml:.3f}")
print(f"LOOCV Root Mean Squared Error (RMSE)       : {f2_rmse:.4f}")
print(f"LOOCV R-squared Score                      : {f2_r2:.4f}")
print(f"Breusch-Pagan Test p-value                 : {p_value:.5f}")
print("--------------------------------------------------------------------------")
print(f"Learned Kernel Parameters:\n{gp_full.kernel_}")
print("--------------------------------------------------------------------------")

if p_value < 0.05:
    print("Verdict for Function 2 (15 datapoints, Week 5): Statistically HETEROSCEDASTIC")
else:
    print("Verdict for Function 2 (15 datapoints, Week 5): Statistically HOMOSCEDASTIC")
print("==========================================================================")
