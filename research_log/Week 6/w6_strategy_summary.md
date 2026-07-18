**BBO Capstone Project** <br />
_**Overall Strategy Summary - Week 6**_

**Kernel Ablation Studies** were performed for all functions in an attempt to identify the optimal acqusiition function for each of the 8 Black-Box functions. The code for this can be found in the `_w6_kernel_ablation_studies_` folder.

Before moving further, the homo/heteroscedasticity of each of the 8 functions modelled by Gaussian Processes was assessed, by plotting the residuals against the predictions of the GP surrogate model and conducting corresponding **Breusch-Pagan tests** (the latest GP hyperparameters from Week 5's strategies will be used for this). The code for this can be found in the `_w6_Breusch_Pagan_tests_` folder.
