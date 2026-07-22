# Strategy optimisation 1. for Week 3 for black-box Function 6 with Sobol Sampling
# Using Automatic Relevance Determination (ARD) on the RBF kernel with conservative baseline and wider bounds
# Week 2's strategy (that worked better than Week 1's strategy), but using Thompson sampling instead of UCB/EI
# Submitted for Week 3

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from scipy.stats.qmc import Sobol

# Loading the data
X = data["function_6"]["x"]      #shape (22, 5)
Y = data["function_6"]["y"]      #shape (22, )

# Defining the Gaussian Process model
kernel = RBF(length_scale=[1.0]*5, # Keeping initial length_scale at [1.0]*3 (conservative baseline) as in Week 2 which worked better than Week 1
    length_scale_bounds=(1e-6, 1e8)) # Using Automatic Relevance Determination (ARD) with conservative baseline and wider bounds
gp = GaussianProcessRegressor(kernel=kernel, alpha=1e-10)
gp.fit(X, Y)

# Defining the input bounds
minimum = X.min(axis=0)
maximum = X.max(axis=0)

# Sobol sequence (power of 2)
sobol = Sobol(d=5, scramble=True)
unit_samples = sobol.random_base2(m=13)

# Scale to actual bounds
x_grid = minimum + unit_samples * (maximum - minimum)

# Computing GP posterior mean + covariance (required for TS)
post_mean, post_cov = gp.predict(x_grid, return_cov=True)

# Thompson Sampling
# Drawing one sample from the GP posterior over all Sobol points
sampled_function = np.random.multivariate_normal(post_mean, post_cov)

# Selecting the point where the sampled function is maximal
x_next = x_grid[np.argmax(sampled_function)]

print("Third raw query point for Function 6:", x_next)
print("Third query point for Function 6 (6 decimals):", np.round(x_next, 6))
