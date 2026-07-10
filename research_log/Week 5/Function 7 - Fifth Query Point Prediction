# Fifth Query Prediction for black-box Function 7 Week 5 Submission
# Using Automatic Relevance Determination (ARD) on the RBF kernel with less aggresive baseline than Week 1 (length_scale=[0.5]*6) and default length_scale_bounds  
# Sobol Sampling
# Week 4's strategy employed again for Week 5, as it successfully maximised the output so far
# Starting to use WhiteKernel to estimate noise automatically, by simulating (learning) the noise in the existing data so far; 
# WhiteKernel parameters are set based on computed std. dev. of the up-to-date dataset (0.354785)
# Starting to normalise y values to better assist the optimisation process (GP)
# EI acquisition function with xi = 0.1 (large exploration parameter)
# Z formula was improved to account for post_std = 0, which would cause Z = NaN and lead to numerical instability further down the line, causing meaningless query prediction

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from scipy.stats.qmc import Sobol

#Loading the data
X = data["function_7"]["x"]      #shape (34, 6)
Y = data["function_7"]["y"]      #shape (34, )

#Defining and fitting a Gaussian Process (GP) model
kernel = RBF(length_scale=[0.5]*6) + WhiteKernel(noise_level=0.12, noise_level_bounds=(1e-3, 3.0))
gp = GaussianProcessRegressor(kernel=kernel, alpha=0.0, normalize_y=True)
gp.fit(X, Y)

#Defining the input bounds
minimum = X.min(axis=0)
maximum = X.max(axis=0)

#Sobol sequence (power of 2)
sobol = Sobol(d=6, scramble=True)
unit_samples = sobol.random_base2(m=13)

#Scale Sobol samples to actual bounds
x_grid = minimum + unit_samples * (maximum - minimum)

#Computing the Gaussian Process (GP) posterior
post_mean, post_std = gp.predict(x_grid, return_std=True)

#Expected Improvement (EI) acquisition
y_best = Y.max()     #maximisation
xi = 0.1             #large exploration parameter

improvement = post_mean - y_best - xi
Z = np.where(post_std > 0, improvement / post_std, 0.0) 
#Improvement in Z formula from previous code versions employed so far, as if post_std=0, Z will be NaN and may result in meaningless query prediction due to numer

#EI formula with safe handling of zero std
ei_acquisition_function = np.where(
    post_std > 0,
    improvement * norm.cdf(Z) + post_std * norm.pdf(Z),
    0.0
)

#Next query => argmax acquisition
x_next = x_grid[np.argmax(ei_acquisition_function)]

print("Fifth raw query point for Function 7:", x_next)
print("Fifth query point for Function 7 (6 decimals):", np.round(x_next, 6))
