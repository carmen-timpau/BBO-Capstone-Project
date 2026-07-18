**BBO Capstone Project** <br />
**_Overall Strategy Summary - Week 4_**


Function 1 Query Prediction Strategy for Week 4:

Matern kernel with nu=1.5 - because Function 1 is spiky - with applied Automatic Relevance Determination (ARD) with aggresive baseline 
and wider bounds, Sobol sampling and Thompson Sampling (Week 3's Strategy repeated).

------------------------------------------------------------------------------------------------------------------------------------------

Function 2 Query Prediction for Week 4:

Automatic Relevance Determination (ARD) on the RBF kernel with aggressive baseline - length_scale=[0.1]*2 - and wider bounds
length_scale_bounds=(1e-6, 1e8), Sobol sampling and Expected Improvement (EI) acqusiiton function, with xi = 0.1 (large), to encourage 
exploration.

------------------------------------------------------------------------------------------------------------------------------------------

Function 3 Query Prediction for Week 4:

Automatic Relevance Determination (ARD) on the RBF kernel with more aggressive baseline length_scale=[0.5]*3 (had to use this instead of 
conservative length_scale=[1.0]*3 used in Week 2, because of ConvergenceWarning) and wider length_scale_bounds=(1e-6, 1e8), Sobol sampling 
and Expected Improvement (EI) acquisiton function, with xi = 0.1 (large), to encourage exploration.

------------------------------------------------------------------------------------------------------------------------------------------

Function 4 Query Prediction for Week 4:

Automatic Relevance Determination (ARD) with aggressive baseline - length_scale=[0.1]*3 - on the RBF kernel and wider bounds 
length_scale_bounds=(1e-6, 1e8), Sobol sampling and Thompson sampling.

------------------------------------------------------------------------------------------------------------------------------------------

Function 5 Query Prediction for Week 4:

Automatic Relevance Determination (ARD) on the RBF kernel with aggressive baseline - length_scale=[0.1]*4 - and default bounds 
length_scale_bounds=(1e-5, 1e5), Sobol sampling and Expected Improvement (EI) acquisiton function, with xi = 0.1 (large), to encourage 
exploration.

------------------------------------------------------------------------------------------------------------------------------------------

Function 6 Query Prediction for Week 4:

Automatic Relevance Determination (ARD) on the RBF kernel with conservative baseline - length_scale=[1.0]*5 - and wider bounds=(1e-6, 1e8), 
Sobol sampling and Expected Improvement (EI) acquisiton function, with xi = 0.1 (large), to encourage exploration.

------------------------------------------------------------------------------------------------------------------------------------------

Function 7 Query Prediction for Week 4:

Automatic Relevance Determination (ARD) on the RBF kernel with less aggresive baseline than in Week 1 - length_scale=[0.5]*4, had to use 
a less aggresive baseline than in Week 1 (length_scale=[0.1)*6) due to ConvergenceWarning - and default length_scale_bounds=(1e-5, 1e5), 
Sobol sampling and Expected Improvement (EI) acquisiton function, with xi = 0.1 (large), to encourage exploration.

------------------------------------------------------------------------------------------------------------------------------------------

Function 8 Query Prediction for Week 4:

Automatic Relevance Determination (ARD) applied to the RBF kernel with conservative baseline (length_scale=[1.0]*8) and wider bounds 
(length_scale_bounds=(1e-6, 1e8)), Sobol sampling and Thompson sampling.
