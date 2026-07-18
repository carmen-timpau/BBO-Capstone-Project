#Next Query Prediction for black-box Function 3 Week 4 Submission
#using Automatic Relevance Determination (ARD) on the RBF kernel with more aggressive baseline than Week 2 (due to ConvergenceWarning) and wider bounds
#Sobol Sampling
#Week 2's strategy + using EI with xi = 0.1 (large exploration parameter) instead of UCB as the acquisition function

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from scipy.stats.qmc import Sobol
from scipy.stats import norm

#Loading the data
X = data["function_3"]["x"]      #shape (18, 3)
Y = data["function_3"]["y"]      #shape (18, )

#Defining the Gaussian Process model
kernel = RBF(
    length_scale=[0.5]*3, #ARD, more aggressive baseline 
    #Changed length_scale from conservative [1.0]*3 (used in Week 2's strategy) to the more aggresive [0.5]*3 due to ConvergenceWarning
    length_scale_bounds=(1e-6, 1e8)
) #using Automatic Relevance Determination (ARD) with more aggressive baseline and wider bounds
gp = GaussianProcessRegressor(kernel=kernel, alpha=1e-10)
gp.fit(X, Y)

#Defining the input bounds
minimum = X.min(axis=0)
maximum = X.max(axis=0)

#Sobol sequence (power of 2)
sobol = Sobol(d=3, scramble=True)
unit_samples = sobol.random_base2(m=12)

#Scaling Sobol samples to actual bounds
x_grid = minimum + unit_samples * (maximum - minimum)

#Computing the Gaussian Process (GP) posterior
post_mean, post_std = gp.predict(x_grid, return_std=True)

#Computing the Expected Improvement (EI) acquisition function
y_best = Y.max()         #maximisation
xi = 0.1                 #large exploration parameter

improvement = post_mean - y_best - xi
with np.errstate(divide='ignore'):
    Z = improvement / post_std
    ei_acquisition_function = np.where(
        post_std > 0,
        improvement * norm.cdf(Z) + post_std * norm.pdf(Z),
        0.0
    )

#Next query => argmax acquisition function
x_next = x_grid[np.argmax(ei_acquisition_function)]

print("Fourth raw query point for Function 3:", x_next)
print("Fourth query point for Function 3 (6 decimals):", np.round(x_next, 6))
