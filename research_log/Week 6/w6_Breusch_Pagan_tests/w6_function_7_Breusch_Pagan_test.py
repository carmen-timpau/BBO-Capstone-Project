# Week 6 BBO - Breusch-Pagan test to assess Homo/Heteroscedasticity for Function 7
# Using Function 7 dataset of 35 points collected after obtaining Week 5's query output 
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

# Pulling updated Function 7 data (35 points, Week 5)
X = np.array(data["function_7"]["x"])  # shape (35, 6)
Y = np.array(data["function_7"]["y"]).flatten()  # shape (35,)

n_samples = len(X)
f7_predictions = []
f7_residuals = []

# Running LOOCV Loop across all 35 points using Week 5's GP for Function 7
for j in range(n_samples):
    X_train = np.delete(X, j, axis=0)
    Y_train = np.delete(Y, j, axis=0)
    X_test = X[j].reshape(1, -1)
    Y_test = Y[j]
    
    kernel = RBF(length_scale=[0.5]*6) + WhiteKernel(noise_level=0.12, noise_level_bounds=(1e-3, 3.0))
    
    gp = GaussianProcessRegressor(
        kernel=kernel, 
        alpha=0.0, 
        normalize_y=True, 
        n_restarts_optimizer=5, 
        random_state=42
    )
    
    gp.fit(X_train, Y_train)
    y_pred = gp.predict(X_test)[0]
    
    f7_predictions.append(y_pred)
    f7_residuals.append(Y_test - y_pred)

f7_predictions = np.array(f7_predictions)
f7_residuals = np.array(f7_residuals)

# Calculating RMSE
f7_rmse = root_mean_squared_error(Y, f7_predictions)

# Calculating R-squared score using true Y values and LOOCV predictions
f7_r2 = r2_score(Y, f7_predictions)

# Performing a Breusch-Pagan test to assess Homo/Heteroscedasticity - Checking if the residuals can be predicted by the model's predictions
# Adding a constant (intercept) term for the linear regression check
X_test_matrix = sm.add_constant(f7_predictions)
lm_stat, p_value, f_stat, f_p_value = het_breuschpagan(f7_residuals, X_test_matrix)

# Plotting the Residuals vs GP Predictions (generated using LOOCV) for Function 7
plt.figure(figsize=(8, 5))
plt.scatter(f7_predictions, f7_residuals, color='darkorange', alpha=0.7, edgecolors='k', s=50, zorder=2)
plt.axhline(y=0, color='crimson', linestyle='--', linewidth=2, zorder=1)

plt.title(f'Function 7: LOOCV Residuals vs. Predictions (N={n_samples})\n'
          f'RMSE: {f7_rmse:.4f}  | LOOCV R-squared Score: {f7_r2:.4f}  |  Breusch-Pagan p-value: {p_value:.5f}', 
          fontsize=11, fontweight='bold')
plt.xlabel('Predicted Value ($\hat{y}$)', fontsize=10)
plt.ylabel('Residual ($y - \hat{y}$)', fontsize=10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()

# Printing Breusch-Pagan Test Outcome
print(f"Breusch-Pagan Test p-value: {p_value:.5f}")

if p_value < 0.05:
    print("Verdict for Function 7 (35 datapoints, Week 5): Statistically HETEROSCEDASTIC (Variance changes significantly)")
else:
    print("Verdict for Function 7 (35 datapoints, Week 5): Statistically HOMOSCEDASTIC (Variance is stable across predictions)")
