**Function 1 Investigation of Strategy Optimisation for Week 3 Submission:**

Strategies tested:

- Week 2's strategy used for Function 1

- Week 2's strategy used for Function 1, but using EI instead of UCB as the acqusition function; a small exploration parameter is used for EI, 
so that we exploit the promising regions, as function 1 is spiky and almost everywhere close to 0 (exploration as we did in Weeks 1-2 
isn't actually ideal, because the chances are that simple broad exploration is highly unlikely to quickly detect the sparse regions where 
the output values are high

- Week 2's startegy used for Function 1 + Thompson sampling instead of UCB (or EI) acqusiition function, which is expected to work best, because TS doesn't 
require any parameter tuning, which in the cases of UCB/EI takes time and consumes valuable queries with no promised improvement being 
certain (This one was submitted for week 3 submission).

----------------------------------------------------------------------------------------------------------------------------------------------

**Function 2 Investigation of Strategy Optimisation for Week 3 Submission:**

Strategies tested:

- Week 2's strategy used for Function 2

- Week 2's strategy used for Function 2, but using EI instead of UCB as the acqusition function.

- Week 2's startegy used for Function 2 + Thompson sampling instead of UCB (or EI) acqusiition function, which is expected to work best, because TS doesn't 
require any parameter tuning, which in the cases of UCB/EI takes time and consumes valuable queries with no promised improvement being 
certain (This one was submitted for week 3 submission).

----------------------------------------------------------------------------------------------------------------------------------------------

**Function 3 Investigation of Strategy Optimisation for Week 3 Submission:**

Strategies tested:

- Week 2's strategy used for Function 3 with length_scale changed from [1.0]*3 to [0.1]*3, because of ConvergenceWarning

- Week 2's strategy used for Function 3 with length_scale changed from [1.0]*3 to [0.1]*3, because of ConvergenceWarning + using EI instead of UCB as the 
acquisition function

- Week 2's strategy used for Function 3 with length_scale changed from [1.0]*3 to [0.1]*3, because of ConvergenceWarning + Thompson sampling instead of UCB 
(or EI) acqusiition function, which is expected to work best, because TS doesn't require any parameter tuning, which in the cases of 
UCB/EI takes time and consumes valuable queries with no promised improvement being certain (This one was submitted for week 3 submission).

----------------------------------------------------------------------------------------------------------------------------------------------

**Function 4 Prediction Week 3** (using the same strategy as in Week 2 because this led to effective function maximisation so far)

Also trying Thompson sampling instead of UCB acquisition function as strategy optimisation 2. to see how this performs. Depending on the 
results that I will get as output from the week 3's submission, I'll decide if I'll implement Thompson sampling for functon 8 in Week 4.

----------------------------------------------------------------------------------------------------------------------------------------------

**Function 5 Investigation of Strategy Optimisation for Week 3 Submission:**

Strategies tested:

- Week 1's strategy used for Function 5 (which worked better than Week 2's strategy, this is why this one is selected for further improvements)

- Week 1's strategy used for Function 5 + using EI (with xi = 0.01, small exploration parameter) instead of UCB as the acquisition function

- Week 1's strategy used for Function 5 + Thompson sampling instead of UCB (or EI) acqusiition function, which is expected to work best, because TS doesn't 
require any parameter tuning, which in the cases of UCB/EI takes time and consumes valuable queries with no promised improvement being 
certain (This one was submitted for week 3 submission).

----------------------------------------------------------------------------------------------------------------------------------------------

**Function 6 Investigation of Strategy Optimisation for Week 3 Submission:**

Strategies tested:

- Week 2's strategy used for Function 6 (which worked better than Week 1's strategy, this is why this one is selected for further improvements)

- Week 2's strategy used for Function 6 + using EI (with xi = 0.01, small exploration parameter) instead of UCB as the acquisition function

- Week 2's strategy used for Function 6 + Thompson sampling instead of UCB (or EI) acqusiition function, which is expected to work best, because TS doesn't 
require any parameter tuning, which in the cases of UCB/EI takes time and consumes valuable queries with no promised improvement being 
certain (This one was submitted for week 3 submission).

----------------------------------------------------------------------------------------------------------------------------------------------

**Function 7 Investigation of Strategy Optimisation for Week 3 Submission:**

Strategies tested:

- Week 1's strategy used for Function 7 (which worked much much better than Week 2's strategy, this is why this one is selected for further improvements)

- Week 1's strategy used for Function 7 + using EI (with xi = 0.01, small exploration parameter) instead of UCB as the acquisition function

- Week 1's strategy + Thompson sampling instead of UCB (or EI) acqusiition function, which is expected to work best, because TS doesn't 
require any parameter tuning, which in the cases of UCB/EI takes time and consumes valuable queries with no promised improvement being 
certain (This one was submitted for week 3 submission).

----------------------------------------------------------------------------------------------------------------------------------------------

**Function 8 Prediction Week 3 (using same strategy as in Weeks 1 & 2 because this led to effective maximisation so far)**

Also trying Thompson sampling instead of UCB acquisition function as strategy optimisation 2. to see how this performs. Depending on the 
results that I will get as output from the week 3's submission, I'll decide if I'll implement Thompson sampling for functon 8 in Week 4.
