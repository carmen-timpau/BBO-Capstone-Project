# Predicting the second query for black-box Function 7 with Sobol Sampling
# Using Automatic Relevance Determination (ARD) on the RBF kernel with conservative baseline and wider bounds

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from scipy.stats.qmc import Sobol

# Loading the data
X = data["function_7"]["x"]      #shape (31, 6)
Y = data["function_7"]["y"]      #shape (31, )

# Defining the Gaussian Process model
kernel = RBF(length_scale=[1.0]*6, #ARD, conservative baseline # Changing length_scale from [0.1]*3 (aggresive baseline) to [1.0]*3 (conservative baseline)
    length_scale_bounds=(1e-6, 1e8)) # Using Automatic Relevance Determination (ARD) with conservative baseline and wider bounds
gp = GaussianProcessRegressor(kernel=kernel, alpha=1e-10)
gp.fit(X, Y)

# Defining the input bounds
minimum = X.min(axis=0)
maximum = X.max(axis=0)

# Sobol sequence (power of 2)
sobol = Sobol(d=6, scramble=True)
unit_samples = sobol.random_base2(m=13)

# Scale Sobol samples to actual bounds
x_grid = minimum + unit_samples * (maximum - minimum)

# Computing the Gaussian Process (GP) posterior
post_mean, post_std = gp.predict(x_grid, return_std=True)

# Computing the Upper Confidence Bound (UCB) acquisition function
beta = 1.96 #balance between exploration and exploitation
ucb_acquisition_function = post_mean + beta * post_std

# Next query => argmax acquisition
x_next = x_grid[np.argmax(ucb_acquisition_function)]

print("Second raw query point for Function 7:", x_next)
print("Second query point for Function 7 (6 decimals):", np.round(x_next, 6))
