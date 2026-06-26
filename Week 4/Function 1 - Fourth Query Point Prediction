# Next Query Prediction for black-box Function 1 Week 4 Submission
# Using a Matern kernel (nu=1.5) (because Function 1 is spiky) 
# Kernel with applied Automatic Relevance Determination (ARD) with aggresive baseline and wider bounds
# Using Sobol Sampling and Thompson Sampling

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern
from scipy.stats.qmc import Sobol

#Loading the data
X = data["function_1"]["x"]      # shape (13, 2)
Y = data["function_1"]["y"]      # shape (13, )

#Defining and fitting the Gaussian Process (GP) model
kernel = Matern(length_scale=[0.1, 0.1], nu=1.5, length_scale_bounds=(1e-6, 1e8)) #ARD, aggresive baseline and wider bounds
#using a Matern kernel (nu=1.5) as this is a spiky function, with applied Automatic Relevance Determination (ARD) with aggresive baseline and wider bounds 
gp = GaussianProcessRegressor(kernel=kernel, alpha=1e-4, normalize_y=True)
gp.fit(X, Y)

#Defining the input bounds
minimum = X.min(axis=0)
maximum = X.max(axis=0)

#Sobol sequence (power of 2)
sobol = Sobol(d=2, scramble=True)
unit_samples = sobol.random_base2(m=12)

#Scaling Sobol samples to actual bounds
x_grid = minimum + unit_samples * (maximum - minimum)

#GP posterior mean + covariance (required for TS)
post_mean, post_cov = gp.predict(x_grid, return_cov=True)

#Thompson Sampling
#Draw one sample from the GP posterior over all Sobol points
sampled_function = np.random.multivariate_normal(post_mean, post_cov)

#Next query => argmax acquisition
x_next = x_grid[np.argmax(sampled_function)]

print("Fourth raw query point for Function 1:", x_next)
print("Fourth query point for Function 1 rounded to 6 decimals:", np.round(x_next, 6))
