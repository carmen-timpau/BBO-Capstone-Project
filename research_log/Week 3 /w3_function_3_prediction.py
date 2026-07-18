#Strategy Investigation 3. for Week 3 submission of black-box Function 3 with Sobol Sampling (more suitable than grid sampling for higher dimensionality functions)
#using Automatic Relevance Determination (ARD) on the RBF kernel with aggresive baseline and wider bounds
#Week 2's strategy with length_scale changed from [1.0]*3 to [0.1]*3, because of ConvergenceWarning + Thompson sampling instead of UCB (or EI) acqusition function
#Submitted for Week 3 

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from scipy.stats.qmc import Sobol
from scipy.stats import norm

# Loading the data
X = data["function_3"]["x"]      #shape (17, 3)
Y = data["function_3"]["y"]      #shape (17, )

# Defining the Gaussian Process model
kernel = RBF(
    length_scale=[0.1]*3, # ARD, aggresive baseline; Changing length_scale from [1.0]*3 (conservative baseline) to [0.1]*3 (aggresive baseline), because otherwise I got a ConvergenceWarning
    length_scale_bounds=(1e-6, 1e8)) # Using Automatic Relevance Determination (ARD) with aggresive baseline and wider bounds
gp = GaussianProcessRegressor(kernel=kernel, alpha=1e-10)
gp.fit(X, Y)

# Defining the input bounds
minimum = X.min(axis=0)
maximum = X.max(axis=0)

# Sobol sequence (power of 2)
sobol = Sobol(d=3, scramble=True)
unit_samples = sobol.random_base2(m=12)

# Scaling Sobol samples to actual bounds
x_grid = minimum + unit_samples * (maximum - minimum)

# Computing the Gaussian Process (GP) posterior
post_mean, post_cov = gp.predict(x_grid, return_cov=True)

# Thompson Sampling
# Drawing one sample from the GP posterior over all Sobol points
sampled_function = np.random.multivariate_normal(post_mean, post_cov)

# Select the point where the sampled function is maximal
x_next = x_grid[np.argmax(sampled_function)]

print("Third raw query point for Function 3:", x_next)
print("Third query point for Function 3 (6 decimals):", np.round(x_next, 6))
