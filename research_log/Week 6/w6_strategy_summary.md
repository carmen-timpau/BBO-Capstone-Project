**BBO Capstone Project** <br />
_**Overall Strategy Summary - Week 6**_

**Kernel Ablation Studies** were performed for all functions in an attempt to identify suitable GP surrogate models for the 8 Black-Box functions. The code for this can be found in the `w6_kernel_ablation_studies` folder within this repo.

Before moving further, the **homo/heteroscedasticity** of each of the 8 functions modelled by Gaussian Processes was assessed, by plotting the residuals against the predictions of the GP surrogate model and conducting corresponding **Breusch-Pagan tests** (the latest GP hyperparameters from Week 5's strategies will be used for this). The code for this can be found in the `w6_Breusch_Pagan_tests` folder within this repo. 

To plot the residuals vs predictions plots, the GP hyperparameters used in Week 5 to predict the fifth query for each function were used to train the GP surrogate model and generate the predictions using **Leave-One-Out Cross-Validation (LOOCV)**.

In the case of functions that showed a linear relationship between the plotted residuals (indicating a highly biased GP), the GP hyperparameters were manually tuned until the scatter plot no longer profiled the linear relationship, but instead resembled just a cloud of points with no discernible patterns, which ensures that any pre-existent bias was successfully removed. The newfound GP hyperparamteres will be used to generate the next query for those respective functions.

For the functions found to be _heteroscedatic_, a **non-linear output warping startegy**<sup>1</sup> will be implemented, as deployed by Noah's Ark Lab at Huawei, in their _Heteroscedastic Evolutionary Bayesian Optimization (HEBO)_ algorithm, to deal with non-constant noise variance (heteroscedasticity). This method was developed by the team as part of the _34<sup>th</sup> Conference on Neural Information Processing Systems (NeurIPS 2020)_ that took place in Vancouver, Canada in 2020.<sup>1,2</sup>

<ins>References<ins>:

[1]. Cowen-Rivers, A. I., Lyu, W., Wang, Z., Tutunov, R., Jianye, H., Wang, J., & Ammar, H. B. (n.d.). HEBO: Heteroscedastic Evolutionary Bayesian Optimisation.

[2]. Mower, Christopher E., et al. HEBO: Bayesian Optimisation and Reinforcement Learning Library library developed by Huawei Noah's Ark Lab. v0.3.4, GitHub, 2020, https://github.com/huawei-noah/HEBO. 
