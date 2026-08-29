**Discussion of Week 12 Query Outcomes:**

_The aim of this discussion is to inform a data-driven strategy for BBO Week 13 (the final week of the project)._

---------------------------------------------------------------------------------------------------------------------------------

For Function 1, Week 12's BBO ML next query prediction strategy (deploying Week 11's BBO ML pipeline) yielded the following output: 7.800755492248212e-60. This output is extremely far from the highest output obtained so far for this function (1.7960297527814237e-10), which can be explained by the very spiky nature of Function 1 and the small size of the available dataset for this function.

For Function 2, Week 12's BBO ML next query prediction strategy (deploying Week 11's BBO ML pipeline) yielded the following output: 0.596142510999502. This output value is fairly close to the current maximum achieved for this function so far (0.7560218355559285). While this did not set a new maximum output value for this function, the fairly high result obtained shows that Week 11's BBO pipeline deployed for Week 12 next query prediction is performing equitably well for this function.

For Function 3, Week 12's BBO ML next query prediction strategy (deploying Week 11's BBO ML pipeline) yielded the following output: -0.04171061207850359. This output value is fairly close to the current maximum achieved for this function so far (-0.01907237834718998). While this did not set a new maximum output value for this function, the fairly high result obtained shows that Week 11's BBO pipeline deployed for Week 12 next query prediction is performing equitably well for this function.

For Function 4, Week 12's BBO ML next query prediction strategy (deploying Week 11's BBO ML pipeline) yielded the following output: 0.34614651718389355. This output value is fairly close to the current maximum achieved for this function so far (0.5702077009884445). While this did not set a new maximum output value for this function, the fairly high result obtained shows that Week 11's BBO pipeline deployed for Week 12 next query prediction is performing equitably well for this function.

For Function 5, Week 12's BBO ML next query prediction strategy (deploying Week 11's BBO ML pipeline) yielded the following output: 745.9931553847641. This output is far from the highest output obtained so far for this function (2333.006822317816). This is however not surprising or indicative of a poorly-performing Bayesian Optimisation ML pipeline, as Thompson Sampling (TS) was selected in the ablation study for generating the next query prediction, which is an intrinsically stochastic algorithm, based on randomised sample value drawing from each candidate's posterior probability distribution and therefore cannot guarantee a high-value output, but balances exploration with exploitation automatically and well.

For Function 6, Week 12's BBO ML next query prediction strategy (deploying Week 11's BBO ML pipeline) yielded the following output: -0.17200299465050722. This is the highest output value obtained so far for this function, indicating that this pipeline worked very well for this function. 

For Function 7, Week 12's BBO ML next query prediction strategy (deploying Week 11's BBO ML pipeline) yielded the following output: 2.7648512476329046. This output value is very close to the current maximum achieved for this function so far (2.9397772255463352). While this did not set a new maximum output value for this function, the fairly high result obtained shows that Week 11's BBO pipeline deployed for Week 12 next query prediction is performing equitably well for this function.

For Function 8, Week 12's BBO ML next query prediction strategy (deploying Week 11's BBO ML pipeline) yielded the following output: 9.9202362271936. This output value is very close to the current maximum achieved for this function so far (9.9561276549796). While this did not set a new maximum output value for this function, the fairly high result obtained shows that Week 11's BBO pipeline deployed for Week 12 next query prediction is performing equitably well for this function.

------------------------------------------------------------------------

**<ins>Discussion Summary:</ins>**

At this advanced stage in the BBO capstone project, Week 12's BBO ML next query prediction strategy (deploying Week 11's BBO ML pipeline) managed to further maximise 1 out of 8 Black-Box functions, specifically Function 6. Not further maximising the rest of the functions does not reflect on the quality or performance of the pipeline/strategy itself, as some (if not many) of these Black-Box functions may have already been globally maximised by now, in previous weeks. In that case, there would be no better points left to be identified through Bayesian Optimisation for those functions and therefore next query predictions will not be able to override the current already established (global) maxima, regardless of how rigorous and effective the pipeline has become.

As the Week 11 BBO ML pipeline is very robust, this will be only slightly modified for Week 13 (the final week) of the BBO project, to conduct a highly-exploitative search for final query predictions for all Black-Box functions. To do this, the acquisition functions that will be considered for testing during the full joint kernel x acquisition function ablation study within the **Week 13 BBO ML Pipeline** will be only the most exploitative ones within the previous larger list, and Thompson Sampling will be completely eliminated as an option, as this carries significant high risk for a final prediction due to its intrinsic stochasticity.
