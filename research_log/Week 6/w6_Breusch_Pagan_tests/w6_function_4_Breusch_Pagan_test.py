# Week 6 BBO - Breusch-Pagan test to assess Homo/Heteroscedasticity for Function 4
# Using Function 4 dataset of 35 points collected after obtaining Week 5's query output 
# Performed before submitting Week 6 query to inform future strategic changes

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics import r2_score
from statsmodels.stats.diagnostic import het_breuschpagan

# Pulling updated Function 4 data (35 points, Week 5)
X = np.array(data["function_4"]["x"])  # shape (35, 4)
Y = np.array(data["function_4"]["y"]).flatten()  # shape (35,)

n_samples = len(X)
f4_predictions = []
f4_residuals = []

# Running LOOCV Loop across all 35 points using Week 5's GP for Function 4
for j in range(n_samples):
    X_train = np.delete(X, j, axis=0)
    Y_train = np.delete(Y, j, axis=0)
    X_test = X[j].reshape(1, -1)
    Y_test = Y[j]
    
    kernel = RBF(length_scale=[0.1]*4, length_scale_bounds=(1e-6, 1e8)) + \
             WhiteKernel(noise_level=60.0, noise_level_bounds=(1e-3, 1e4))
    
    gp = GaussianProcessRegressor(
        kernel=kernel, 
        alpha=0.0, 
        normalize_y=True, 
        n_restarts_optimizer=5, 
        random_state=42
    )
    
    gp.fit(X_train, Y_train)
    y_pred = gp.predict(X_test)[0]
    
    f4_predictions.append(y_pred)
    f4_residuals.append(Y_test - y_pred)

f4_predictions = np.array(f4_predictions)
f4_residuals = np.array(f4_residuals)

# Calculating RMSE
f4_rmse = root_mean_squared_error(Y, f4_predictions)

# Calculating R-squared score using true Y values and LOOCV predictions
f4_r2 = r2_score(Y, f4_predictions)

# Performing a Breusch-Pagan test to assess Homo/Heteroscedasticity - Checking if the residuals can be predicted by the model's predictions
# Adding a constant (intercept) term for the linear regression check
X_test_matrix = sm.add_constant(f4_predictions)
lm_stat, p_value, f_stat, f_p_value = het_breuschpagan(f4_residuals, X_test_matrix)

# Plotting the Residuals vs GP Predictions (generated using LOOCV) for Function 4
plt.figure(figsize=(8, 5))
plt.scatter(f4_predictions, f4_residuals, color='crimson', alpha=0.7, edgecolors='k', s=50, zorder=2)
plt.axhline(y=0, color='black', linestyle='--', linewidth=2, zorder=1)

plt.title(f'Function 4, Week 5: LOOCV Residuals vs. Predictions (N={n_samples})\n'
          f'RMSE: {f4_rmse:.4f}  | LOOCV R-squared Score: {f4_r2:.4f} |  Breusch-Pagan p-value: {p_value:.5f}', 
          fontsize=11, fontweight='bold')
plt.xlabel('Predicted Value ($\hat{y}$)', fontsize=10)
plt.ylabel('Residual ($y - \hat{y}$)', fontsize=10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()

# Printing Breusch-Pagan Test Outcome
print(f"Breusch-Pagan Test p-value: {p_value:.5f}")

if p_value < 0.05:
    print("Verdict for Function 4 (35 datapoints, Week 5): Statistically HETEROSCEDASTIC (Variance changes significantly)")
else:
    print("Verdict for Function 4 (35 datapoints, Week 5): Statistically HOMOSCEDASTIC (Variance is stable across predictions)")
