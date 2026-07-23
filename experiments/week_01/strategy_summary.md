**Overall Initial Strategy for First Set of Query Points Prediction:**

To decide the first query for each of the 8 given black-box functions, a Bayesian Optimisation strategy based on a Gaussian Process (GP) as the surrogate model fitted to the data was used. 


_Acquisition Function:_

The Upper Confidence Bound (UCB) was selected as the acquisition function to guide query selection, with β = 1.96 (95% confidence interval), which is 
balanced between exploitation and exploration. 


_Kernels:_

Similarity between the data points was measured using Automatic Relevance Determination (ARD) applied to the Radial Basis Function (RBF) kernel, 
with a length-scale of 0.1xD (D = no. of dimensions for input variables) and default length-scale bounds (1e-05, 100000.0) for all functions, 
except for function 8. 

For function 8, Automatic Relevance Determination (ARD) with wider length-scale bounds (1e-6, 1e8) was applied to the RBF with a length scale of 1.0xD, 
to assign independent length-scales to each input dimension, because the length-scale of the RBF kernel was pushed to the maximum value (100000) when 
ARD with default bounds was tried initially. 


_Sampling Methods:_

For functions 1 and 2 (2D), grid sampling was used to evaluate the acquisition function.
For all functions with >=3 dimensions (functions 3-8), Sobol sampling was used rather than grid sampling to generate the search space in a uniform, structured, 
space-filling and highly performing way and support a fast and effective Bayesian optimisation process when working with high-dimensional spaces.
