# Predicting the fifth query for black-box Function 8
# Using Automatic Relevance Determination (ARD) on the RBF with conservative baseline (length_scale=[1.0]*8) and wider length_scale_bounds (1e-6, 1e8)
# Starting to use WhiteKernel to estimate noise automatically, by simulating (learning) the noise in the existing data so far; 
# WhiteKernel parameters are set based on computed std. dev. of the up-to-date dataset (1.083139)
# Starting to normalise y values to better assist the optimisation process (GP)
# Expected Improvement (EI) acquisition function with large exploration parameter xi = 0.1
# Z formula was improved to account for post_std = 0, which would cause Z = NaN and lead to numerical instability further down the line, causing meaningless query prediction
# Sobol Sampling

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from scipy.stats.qmc import Sobol

#Loading the data
X = data["function_8"]["x"]      #shape (44, 8)
Y = data["function_8"]["y"]      #shape (44, )

#Defining and fitting the Gaussian Process (GP) model
kernel = RBF(length_scale=[1.0]*8,length_scale_bounds=(1e-6, 1e8)) + WhiteKernel(noise_level=0.3, noise_level_bounds=(1e-12, 10.0))
gp = GaussianProcessRegressor(kernel=kernel, alpha=0.0, normalize_y=True)
gp.fit(X, Y)

#Defining the input bounds
minimum = X.min(axis=0)
maximum = X.max(axis=0)

#Sobol sequence (power of 2)
sobol = Sobol(d=8, scramble=True)
unit_samples = sobol.random_base2(m=13)

#Scaling Sobol samples to actual bounds
x_grid = minimum + unit_samples * (maximum - minimum)

#Computing the Gaussian Process (GP) posterior
post_mean, post_std = gp.predict(x_grid, return_std=True)

#Expected Improvement (EI) Acquisition Function with high exploration parameter xi = 0.1
y_best = Y.max()
xi = 0.1             #large exploration parameter

improvement = post_mean - y_best - xi
Z = np.where(post_std > 0, improvement / post_std, 0.0) 
#Improvement in Z formula from previous code versions employed so far, as if post_std=0, Z will be NaN and may result in meaningless query prediction due to numerical instability

#EI formula with safe handling of zero std
ei_acquisition_function = np.where(
    post_std > 0,
    improvement * norm.cdf(Z) + post_std * norm.pdf(Z),
    0.0
)

#Next query => argmax acquisition
x_next = x_grid[np.argmax(ei_acquisition_function)]

print("Fifth raw query point for Function 8:", x_next)
print("Fifth query point for Function 8 (6 decimals):", np.round(x_next, 6))
