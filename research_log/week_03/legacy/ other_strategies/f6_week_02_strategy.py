#Strategy optimisation 1. for Week 3 for black-box Function 6 with Sobol Sampling
#using Automatic Relevance Determination (ARD) on the RBF kernel with conservative baseline and wider bounds
#UCB acquisition function, with beta = 1.96 (balance between exploration and exploitation)
#Week 2's strategy (that worked better than Week 1's strategy)

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from scipy.stats.qmc import Sobol

#Loading the data
X = data["function_6"]["x"]      #shape (22, 5)
Y = data["function_6"]["y"]      #shape (22, )

#Defining the Gaussian Process model
kernel = RBF(
    length_scale=[1.0]*5, #ARD, Keeping length_scale at [1.0]*3 (conservative baseline) as in Week 2 which worked better than Week 1
    length_scale_bounds=(1e-6, 1e8) #wider bounds
) #using Automatic Relevance Determination (ARD) with conservative baseline and wider bounds
gp = GaussianProcessRegressor(kernel=kernel, alpha=1e-10)
gp.fit(X, Y)

#Defining the input bounds
minimum = X.min(axis=0)
maximum = X.max(axis=0)

#Sobol sequence (power of 2)
sobol = Sobol(d=5, scramble=True)
unit_samples = sobol.random_base2(m=13)

#Scale to actual bounds
x_grid = minimum + unit_samples * (maximum - minimum)

#Computing the Gaussian Process (GP) posterior
post_mean, post_std = gp.predict(x_grid, return_std=True)

#Computing the Upper Confidence Bound (UCB) acquisition function
beta = 1.96 #balance between exploration and exploitation
ucb_acquisition_function = post_mean + beta * post_std

#Next query => argmax acquisition
x_next = x_grid[np.argmax(ucb_acquisition_function)]

print("Third raw query point for Function 6:", x_next)
print("Third query point for Function 6 (6 decimals):", np.round(x_next, 6))
