#Predicting the second query point for black-box Function 1
#using a Matern kernel (nu=1.5) as this is a spiky function and RBF is actually not suitable for it (RBF is suitable for smooth functions),
#kernel with applied Automatic Relevance Determination (ARD) with aggresive baseline and wider bounds
#Sobol sampling
#UCB acquisition function, with beta = 4.0 (more exploration encouraged)

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern
from scipy.stats.qmc import Sobol

#Loading the data
X = data["function_1"]["x"]      #shape (11, 2)
Y = data["function_1"]["y"]      #shape (11, )

#Defining and fitting the Gaussian Process (GP) model
kernel = Matern(length_scale=[0.1, 0.1], nu=1.5, length_scale_bounds = (1e-6, 1e8)) #ARD, aggresive baseline and wider bounds
#using a Matern kernel (nu=1.5) as this is a spiky function with applied Automatic Relevance Determination (ARD) with aggresive baseline and wider bounds
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

#Computing the Gaussian Process (GP) posterior
post_mean, post_std = gp.predict(x_grid, return_std=True)

#Computing the Upper Confidence Bound (UCB) acquisition function
beta = 4.0  # instead of 1.96 => More exploration required here, as the function is mostly close to 0 except in some regions to be identified
ucb_acquisition_function =post_mean + beta * post_std

#Next query => argmax acquisition
x_next = x_grid[np.argmax(ucb_acquisition_function)]

print("Second raw query point for Function 1:", x_next)
print("Second query point for Function 1 rounded to 6 decimal places:", np.round(x_next, 6))
