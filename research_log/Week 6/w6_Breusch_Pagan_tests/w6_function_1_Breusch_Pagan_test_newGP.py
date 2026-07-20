# Week 6 BBO - Breusch-Pagan test to assess Homo/Heteroscedasticity for Function 1
# Using Function 1 dataset of 15 points collected after obtaining Week 5's query output 
# Performed before submitting Week 6 query to inform future strategic changes
# Using log10 to scale Function 1 outputs within LOOCV as they are extremely low values
# Using newfound GP hyperparameters that improve R-squared value compared to the GP that was used in Week 5 for Function 1

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern, WhiteKernel
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.diagnostic import het_breuschpagan

# Pulling updated Function 1 data (15 points, Week 5)
X = np.array(data["function_1"]["x"])  # shape (15, 2)
Y = np.array(data["function_1"]["y"]).flatten()  # shape (15,)

# Transforming Y to log10 space to avoid numerical underflow issues with extreme values
Y_safe = np.clip(Y, 1e-300, None)  # Clipping to prevent log10(0) from producing NaN
Y_log = np.log10(Y_safe)

n_samples = len(X)
f1_predictions = []
f1_residuals = []

# Running LOOCV Loop across all 15 points using Week 5's GP for Function 1
for j in range(n_samples):
    X_train = np.delete(X, j, axis=0)
    Y_train = np.delete(Y_log, j, axis=0)
    X_test = X[j].reshape(1, -1)
    Y_test = Y_log[j]
    
    # Feature scaling on X to prevent data leakage across LOOCV folds
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Kernel noise bounds adjusted for log-scale values
    kernel = Matern(length_scale=[0.1, 0.1], nu=2.5, length_scale_bounds=(1e-6, 1e8)) + \
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
    
    f1_predictions.append(y_pred)
    f1_residuals.append(Y_test - y_pred)

f1_predictions = np.array(f1_predictions)
f1_residuals = np.array(f1_residuals)

# Calculating RMSE in log space
f1_rmse = root_mean_squared_error(Y_log, f1_predictions)

# Calculating R-squared score using true log Y values and LOOCV predictions
f1_r2 = r2_score(Y_log, f1_predictions)

# Performing a Breusch-Pagan test to assess Homo/Heteroscedasticity - Checking if the residuals can be predicted by the model's predictions
# Adding a constant (intercept) term for the linear regression check
X_test_matrix = sm.add_constant(f1_predictions)
lm_stat, p_value, f_stat, f_p_value = het_breuschpagan(f1_residuals, X_test_matrix)

# Plotting the Residuals vs GP Predictions (generated using LOOCV) for Function 1 in log space
plt.figure(figsize=(8, 5))
plt.scatter(f1_predictions, f1_residuals, color='gold', alpha=0.7, edgecolors='k', s=50, zorder=2)
plt.axhline(y=0, color='black', linestyle='--', linewidth=2, zorder=1)

plt.title(f'Function 1, Week 5 (Log Scale): LOOCV Residuals vs. Predictions (N={n_samples})\n'
          f'RMSE: {f1_rmse:.4f}  | LOOCV R-squared Score: {f1_r2:.4f} |  Breusch-Pagan p-value: {p_value:.5f}', 
          fontsize=11, fontweight='bold')
plt.xlabel('Predicted Log Value ($\hat{y}_{log}$)', fontsize=10)
plt.ylabel('Log Residual ($y_{log} - \hat{y}_{log}$)', fontsize=10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()

# Printing Breusch-Pagan Test Outcome
print(f"Breusch-Pagan Test p-value: {p_value:.5f}")

if p_value < 0.05:
    print("Verdict for Function 1 (15 datapoints, Week 5): Statistically HETEROSCEDASTIC (Variance changes significantly)")
else:
    print("Verdict for Function 1 (15 datapoints, Week 5): Statistically HOMOSCEDASTIC (Variance is stable across predictions)")
