# Predicting the fifth query for black-box Function 5 
# Using Automatic Relevance Determination (ARD) on the RBF kernel with agressive baseline (length_scale=[0.1]*4) and default length_scale_bounds(1e-5, 1e5)
# UCB acquisition function with beta = 0.5, strong exploitation
# Started using WhiteKernel to estimate noise automatically, by simulating (learning) the noise in the existing data so far
# WhiteKernel parameters are set based on computed std. dev. of the up-to-date dataset (271.712127)
# Starting to normalise y values to better assist the optimisation process (GP)
# Sobol Sampling

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from scipy.stats.qmc import Sobol

#Loading the data
X = data["function_5"]["x"]      #shape (24, 4)
Y = data["function_5"]["y"]      #shape (24, )

#Defining and fitting the Gaussian Process (GP) model
kernel = RBF(length_scale=[0.1]*4) + WhiteKernel(noise_level=7.4e4, noise_level_bounds=(1e-3, 1e7))
gp = GaussianProcessRegressor(kernel=kernel, alpha=0.0, normalize_y=True)
gp.fit(X, Y)

#Defining the input bounds
minimum = X.min(axis=0)
maximum = X.max(axis=0)

#Sobol sequence (power of 2)
sobol = Sobol(d=4, scramble=True)
unit_samples = sobol.random_base2(m=13) 

#Scale Sobol samples to actual bounds
x_grid = minimum + unit_samples * (maximum - minimum)

#Computing the Gaussian Process (GP) posterior
post_mean, post_std = gp.predict(x_grid, return_std=True)

#Computing the Upper Confidence Bound (UCB) acquisition function
beta = 0.5 #strong exploitation
ucb_acquisition_function = post_mean + beta * post_std

#Next query => argmax acquisition
x_next = x_grid[np.argmax(ucb_acquisition_function)]

print("Fifth raw query point for Function 5:", x_next)
print("Fifth query point for Function 5 (6 decimals):", np.round(x_next, 6))
