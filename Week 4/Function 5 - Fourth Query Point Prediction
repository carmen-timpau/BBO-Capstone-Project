#Next Query Prediction for black-box Function 5 Week 4 Submission
#using Automatic Relevance Determination (ARD) on the RBF kernel with aggresive baseline and default length_scale_bounds (worked better than wider length_scale_bounds which were tested in Week 2's strategy)
#Sobol Sampling
#Using EI (with xi = 0.1, large exploration parameter) instead of UCB as acqusition function

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from scipy.stats.qmc import Sobol
from scipy.stats import norm

#Loading the data
X = data["function_5"]["x"]      #shape (23, 4)
Y = data["function_5"]["y"]      #shape (23, )

#Defining and fitting the Gaussian Process (GP) model
kernel = RBF(length_scale=[0.1]*4) #ARD, aggresive baseline
#using Automatic Relevance Determination (ARD) with aggresive baseline and default length_scale_bounds
gp = GaussianProcessRegressor(kernel=kernel, alpha=1e-10)
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

#Expected Improvement (EI) acquisition
y_best = Y.max()    #maximisation
xi = 0.1            #large exploration parameter

improvement = post_mean - y_best - xi
Z = improvement / post_std

# EI formula with safe handling of zero std
ei_acquisition_function = np.where(
    post_std > 0,
    improvement * norm.cdf(Z) + post_std * norm.pdf(Z),
    0.0
)

# Next query => argmax EI
x_next = x_grid[np.argmax(ei_acquisition_function)]

print("Fourth raw query point for Function 5:", x_next)
print("Fourth query point for Function 5 (6 decimals):", np.round(x_next, 6))
