# Week 6 BBO - Breusch-Pagan test to assess Homo/Heteroscedasticity for Function 8
# Using Function 8 dataset of 45 points collected after obtaining Week 5's query output 
# Performed before submitting Week 6 query to inform future strategic changes

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import warnings
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics import r2_score
from statsmodels.stats.diagnostic import het_breuschpagan
from sklearn.exceptions import ConvergenceWarning

# Filtering out ConvergenceWarning 
warnings.filterwarnings("ignore", category=ConvergenceWarning)

# Pulling updated Function 8 data (45 points, Week 5)
X = np.array(data["function_8"]["x"])  # shape (45, 8)
Y = np.array(data["function_8"]["y"]).flatten()  # shape (45,)

n_samples = len(X)
f8_predictions = []
f8_residuals = []

# Running LOOCV Loop across all 45 points using Week 5's GP for Function 8
for j in range(n_samples):
    X_train = np.delete(X, j, axis=0)
    Y_train = np.delete(Y, j, axis=0)
    X_test = X[j].reshape(1, -1)
    Y_test = Y[j]
    
    kernel = RBF(length_scale=[1.0]*8, length_scale_bounds=(1e-6, 1e8)) + \
             WhiteKernel(noise_level=0.3, noise_level_bounds=(1e-12, 10.0))
    
    gp = GaussianProcessRegressor(
        kernel=kernel, 
        alpha=0.0, 
        normalize_y=True, 
        n_restarts_optimizer=5, 
        random_state=42
    )
    
    gp.fit(X_train, Y_train)
    y_pred = gp.predict(X_test)[0]
    
    f8_predictions.append(y_pred)
    f8_residuals.append(Y_test - y_pred)

f8_predictions = np.array(f8_predictions)
f8_residuals = np.array(f8_residuals)

# Calculating RMSE
f8_rmse = root_mean_squared_error(Y, f8_predictions)

# Calculating R-squared score using true Y values and LOOCV predictions
f8_r2 = r2_score(Y, f8_predictions)

# Performing a Breusch-Pagan test to assess Homo/Heteroscedasticity - Checking if the residuals can be predicted by the model's predictions
# Adding a constant (intercept) term for the linear regression check
X_test_matrix = sm.add_constant(f8_predictions)
lm_stat, p_value, f_stat, f_p_value = het_breuschpagan(f8_residuals, X_test_matrix)

# Plotting the Residuals vs GP Predictions (generated using LOOCV) for Function 8
plt.figure(figsize=(8, 5))
plt.scatter(f8_predictions, f8_residuals, color='teal', alpha=0.7, edgecolors='k', s=50, zorder=2)
plt.axhline(y=0, color='crimson', linestyle='--', linewidth=2, zorder=1)

plt.title(f'Function 8, Week 5: LOOCV Residuals vs. Predictions (N={n_samples})\n'
          f'RMSE: {f8_rmse:.4f}   | LOOCV R-squared Score: {f8_r2:.4f}  |  Breusch-Pagan p-value: {p_value:.5f}', 
          fontsize=11, fontweight='bold')
plt.xlabel('Predicted Value ($\hat{y}$)', fontsize=10)
plt.ylabel('Residual ($y - \hat{y}$)', fontsize=10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()

# Printing Breusch-Pagan Test Outcome
print(f"Breusch-Pagan Test p-value: {p_value:.5f}")

if p_value < 0.05:
    print("Verdict for Function 8 (45 datapoints, Week 5): Statistically HETEROSCEDASTIC (Variance changes significantly)")
else:
    print("Verdict for Function 8 (45 datapoints, Week 5): Statistically HOMOSCEDASTIC (Variance is stable across predictions)")
