# Week 6 BBO - Breusch-Pagan test to assess Homo/Heteroscedasticity for Function 1
# Using Function 1 dataset of 15 points collected after obtaining Week 5's query output 
# Performed before submitting Week 6 query to inform future strategic changes
# Using log10 to scale Function 1 outputs within LOOCV as they are extremely low values
# Using winning kernel config from ablation study: RBF + WhiteNoise

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel
from sklearn.metrics import root_mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.diagnostic import het_breuschpagan

import warnings
from sklearn.exceptions import ConvergenceWarning

warnings.filterwarnings("ignore", category=ConvergenceWarning)

# Pulling updated Function 1 data (15 points, 2D)
X = np.array(data["function_1"]["x"])  # shape (15, 2)
Y = np.array(data["function_1"]["y"]).flatten()  # shape (15,)

# Transforming Y to log10 space to avoid numerical underflow issues
Y_safe = np.clip(Y, 1e-300, None)
Y_log = np.log10(Y_safe)

n_samples, n_dims = X.shape
f1_predictions = []
f1_residuals = []
f1_fold_lmls = []

# Defining Winning Kernel Config (Ablation 2: RBF + WhiteNoise)
kernel_f1 = RBF(
    length_scale=[100.0, 0.1], 
    length_scale_bounds=(1e-3, 1e8)
) + WhiteKernel(
    noise_level=1e-6, 
    noise_level_bounds=(1e-10, 1e2)
)

# Running LOOCV Loop across all 15 points
for j in range(n_samples):
    X_train = np.delete(X, j, axis=0)
    Y_train = np.delete(Y_log, j, axis=0)
    X_test = X[j].reshape(1, -1)
    Y_test = Y_log[j]
    
    # Feature scaling on X to prevent data leakage across LOOCV folds
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    gp = GaussianProcessRegressor(
        kernel=kernel_f1, 
        alpha=0.0, 
        normalize_y=True, 
        n_restarts_optimizer=5, 
        random_state=42
    )
    
    gp.fit(X_train_scaled, Y_train)
    y_pred = gp.predict(X_test_scaled)[0]
    
    f1_predictions.append(y_pred)
    f1_residuals.append(Y_test - y_pred)
    f1_fold_lmls.append(gp.log_marginal_likelihood(gp.kernel_.theta))

f1_predictions = np.array(f1_predictions)
f1_residuals = np.array(f1_residuals)

# Calculating LOOCV Performance Metrics in log space
f1_rmse = root_mean_squared_error(Y_log, f1_predictions)
f1_r2 = r2_score(Y_log, f1_predictions)

# Fitting Full Dataset to extract optimal parameters & Full Log Marginal Likelihood
scaler_full = StandardScaler()
X_full_scaled = scaler_full.fit_transform(X)

gp_full = GaussianProcessRegressor(
    kernel=kernel_f1,
    alpha=0.0,
    normalize_y=True,
    n_restarts_optimizer=5,
    random_state=42
)
gp_full.fit(X_full_scaled, Y_log)
full_lml = gp_full.log_marginal_likelihood(gp_full.kernel_.theta)
mean_loocv_lml = np.mean(f1_fold_lmls)

# Performing Breusch-Pagan test
X_test_matrix = sm.add_constant(f1_predictions)
lm_stat, p_value, f_stat, f_p_value = het_breuschpagan(f1_residuals, X_test_matrix)

# Plotting Residuals vs GP Predictions
plt.figure(figsize=(8, 5))
plt.scatter(f1_predictions, f1_residuals, color='gold', alpha=0.8, edgecolors='k', s=50, zorder=2)
plt.axhline(y=0, color='black', linestyle='--', linewidth=2, zorder=1)

plt.title(f'Function 1, Week 5 (Log Scale): LOOCV Residuals vs. Predictions (N={n_samples})\n'
          f'RMSE: {f1_rmse:.4f}  | LOOCV R²: {f1_r2:.4f}  |  LML: {full_lml:.3f} | BP p-value: {p_value:.5f}', 
          fontsize=10, fontweight='bold')
plt.xlabel('Predicted Log Value ($\hat{y}_{log}$)', fontsize=10)
plt.ylabel('Log Residual ($y_{log} - \hat{y}_{log}$)', fontsize=10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()

# Printing Diagnostics & Results
print("==========================================================================")
print("     FUNCTION 1 DIAGNOSTICS — WINNING CONFIG: RBF + WHITE NOISE           ")
print("==========================================================================")
print(f"Full Dataset Log Marginal Likelihood (LML) : {full_lml:.3f}")
print(f"Mean LOOCV Fold Log Marginal Likelihood    : {mean_loocv_lml:.3f}")
print(f"LOOCV Root Mean Squared Error (RMSE)       : {f1_rmse:.4f}")
print(f"LOOCV R-squared Score                      : {f1_r2:.4f}")
print(f"Breusch-Pagan Test p-value                 : {p_value:.5f}")
print("--------------------------------------------------------------------------")
print(f"Learned Kernel Parameters:\n{gp_full.kernel_}")
print("--------------------------------------------------------------------------")

if p_value < 0.05:
    print("Verdict for Function 1 (15 datapoints, Week 5): Statistically HETEROSCEDASTIC")
else:
    print("Verdict for Function 1 (15 datapoints, Week 5): Statistically HOMOSCEDASTIC")
print("==========================================================================")
