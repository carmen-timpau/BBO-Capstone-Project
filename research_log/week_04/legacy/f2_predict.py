#Next Query Prediction for black-box Function 2 Week 4 Submission
#Using Automatic Relevance Determination (ARD) on the RBF kernel with aggresive baseline and wider bounds
#Sobol sampling
#Week 2's strategy, but using EI with xi = 0.1 (large exploration parameter) instead of UCB as the acqusition function

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from scipy.stats.qmc import Sobol
from scipy.stats import norm

#Loading the data
X = data["function_2"]["x"]      #shape (13, 2)
Y = data["function_2"]["y"]      #shape (13, )

#Defining and fitting the Gaussian Process (GP) model
kernel = RBF(
    length_scale=[0.1]*2, #ARD, aggresive baseline
    length_scale_bounds=(1e-6, 1e8) #wider bounds
) #using Automatic Relevance Determination (ARD) with aggresive baseline and wider bounds
gp = GaussianProcessRegressor(kernel=kernel, alpha=1e-10)

gp.fit(X, Y)

#Defining the input bounds
minimum = X.min(axis=0)
maximum = X.max(axis=0)

#Sobol sequence (power of 2)
sobol = Sobol(d=2, scramble=True)
unit_samples = sobol.random_base2(m=12)

#Scaling Sobol samples to actual bounds
x_grid = minimum + unit_samples * (maximum - minimum)

#Computing the Gaussian Process (GP) posterior
post_mean, post_std = gp.predict(x_grid, return_std=True)

#Expected Improvement (EI) acquisition
y_best = Y.max()     #maximisation
xi = 0.1             #large exploration parameter

improvement = post_mean - y_best - xi
Z = improvement / post_std

# EI formula with safe handling of zero std
ei_acquisition_function = np.where(
    post_std > 0,
    improvement * norm.cdf(Z) + post_std * norm.pdf(Z),
    0.0
)

#Next query => argmax acquisition
x_next = x_grid[np.argmax(ei_acquisition_function)]

print("Fourth raw query point for Function 2:", x_next)
print("Fourth query point for Function 2 rounded to 6 decimal places:", np.round(x_next, 6))
