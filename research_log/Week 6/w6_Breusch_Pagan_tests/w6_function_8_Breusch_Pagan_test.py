# Week 6 BBO - Breusch-Pagan test to assess Homo/Heteroscedasticity for Function 8
# Using Function 8 dataset of 45 points collected after obtaining Week 5's query output 
# Performed before submitting Week 6 query to inform future strategic changes

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel
from sklearn.metrics import root_mean_squared_error
from statsmodels.stats.diagnostic import het_breuschpagan

# Pulling updated Function 8 data (45 points, Week 5)
X = np.array(data["function_8"]["x"])  # shape (45, 8)
Y = np.array(data["function_8"]["y"]).flatten()  # shape (45,)

n_samples = len(X)
f8_predictions = []
f8_residuals = []

# Running Leave-One-Out Cross-Validation (LOOCV) Loop across all 45 points

for j in range(n_samples):
    X_train = np.delete(X, j, axis=0)
    Y_train = np.delete(Y, j, axis=0)
    X_test = X[j].reshape(1, -1)
    Y_test = Y[j]
    
    # Using Week 5's Startegy GP settings for Function 8
    kernel = RBF(length_scale=[1.0]*8, length_scale_bounds=(1e-6, 1e8)) + WhiteKernel(noise_level=0.3, noise_level_bounds=(1e-12, 10.0))
    
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

# Calculating global validation score

f8_rmse = root_mean_squared_error(Y, f8_predictions)
print(f"Function 8 LOOCV Root Mean Squared Error: {f8_rmse:.4f}")

# Plotting the Residuals vs GP Predictions (generated using LOOCV) for Function 8 

plt.figure(figsize=(8, 5))
plt.scatter(f8_predictions, f8_residuals, color='teal', alpha=0.7, edgecolors='k', s=50, zorder=2)
plt.axhline(y=0, color='crimson', linestyle='--', linewidth=2, zorder=1)

plt.title(f'Function 8 (Week 5): Residuals vs. Predictions (N={n_samples})\nLOOCV RMSE: {f8_rmse:.4f}', fontsize=12, fontweight='bold')
plt.xlabel('Predicted Value ($\hat{y}$)', fontsize=10)
plt.ylabel('Residual ($y - \hat{y}$)', fontsize=10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()

# Performing a Breusch-Pagan test to assess Homo/Heteroscedasticity - Checking if the residuals can be predicted by the model's predictions
X_test_matrix = sm.add_constant(f8_predictions)
lm_stat, p_value, f_stat, f_p_value = het_breuschpagan(f8_residuals, X_test_matrix)

print(f"Breusch-Pagan Test p-value: {p_value:.5f}")

# Printing direct outcome based on the computed p valued(Homo/Heteroscedastic)
if p_value < 0.05:
    print("Verdict for Function 8 (45 datapoints, Week 5): Statistically HETEROSCEDASTIC (Variance changes significantly)")
else:
    print("Verdict for Function 8 (45 datapoints, Week 5): Statistically HOMOSCEDASTIC (Variance is sufficiently constant)")
