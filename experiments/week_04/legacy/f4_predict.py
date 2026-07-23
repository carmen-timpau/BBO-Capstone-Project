#Next Query Prediction for black-box Function 4 Week 4 Submission
#using Automatic Relevance Determination (ARD) on the RBF kernel with aggresive baseline and wider bounds
#Sobol sampling
#Maintaining the same strategy as in Week 2, but using Thompson sampling instead of UCB acquisition function

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from scipy.stats.qmc import Sobol

#Loading the data
X = data["function_4"]["x"]      #shape (33, 4)
Y = data["function_4"]["y"]      #shape (33, )

#Defining and fitting the Gaussian Process model
kernel = RBF(
    length_scale=[0.1]*4, #Keeping length_scale at [0.1]*4 (aggresive baseline) as used in Week 2
    length_scale_bounds=(1e-6, 1e8) #wider bounds
) #using Automatic Relevance Determination (ARD) with aggresive baseline and wider bounds
gp = GaussianProcessRegressor(kernel=kernel, alpha=1e-10)
gp.fit(X, Y)

#Defining the input bounds
minimum = X.min(axis=0)
maximum = X.max(axis=0)

#Sobol sequence (power of 2)
sobol = Sobol(d=4, scramble=True)
unit_samples = sobol.random_base2(m=13)

#Scaling Sobol samples to actual bounds
x_grid = minimum + unit_samples * (maximum - minimum)

#Computing the Gaussian Process (GP) posterior
post_mean, post_cov = gp.predict(x_grid, return_cov=True)

#Thompson Sampling
#Draw one sample from the GP posterior over all Sobol points
sampled_function = np.random.multivariate_normal(post_mean, post_cov)

#Select the point where the sampled function is maximal
x_next = x_grid[np.argmax(sampled_function)]

#Next query => argmax acquisition
x_next = x_grid[np.argmax(ucb_acquisition_function)]

print("Fourth raw query point for Function 4:", x_next)
print("Fourth query point for Function 4 (6 decimals):", np.round(x_next, 6))
