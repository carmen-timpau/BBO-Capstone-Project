**Overall Startegy Summary for Week 2 Query Points Predictions in Response to Processed Week 1 Queries**

Because the outputs obtained in week 1 I obtained output optimisation only for function 8 (which is the only one for which I applied ARD with a slightly 
larger length_scale [1.0*D instead of 0.1*D] and wider length-scale_bounds [1e-6, 1e8; instead of the default 1e-5, 1e5] on the RBF kernel), I will 
implement this for all functions to generate the next set of queries for week 2. 

Sobol sampling will also be implemented for the first 2 functions as well, instead of grid sampling.
