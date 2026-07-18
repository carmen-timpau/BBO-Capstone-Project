**BBO Capstone Project** <br />
_**Overall Strategy Summary - Week 6**_

**Kernel Ablation Studies** were performed for all functions in an attempt to identify the optimal acqusiition function for each of the 8 Black-Box functions. The code for this can be found in the `w6_kernel_ablation_studies` folder.

Before moving further, the homo/heteroscedasticity of each of the 8 functions modelled by Gaussian Processes was assessed, by plotting the residuals against the predictions of the GP surrogate model and conducting corresponding **Breusch-Pagan tests** (the latest GP hyperparameters from Week 5's strategies will be used for this). The code for this can be found in the `w6_Breusch_Pagan_tests` folder. 

For the functions found to be _heteroscedatic_, an **non-linear output warping startegy**<sup>1</sup> will be implemented, as deployed by Noah's Ark Lab at Huawei, in their Heteroscedastic Evolutionary Bayesian Optimization (HEBO) algorithm, to deal with non-constant noise variance (heteroscedasticity). This method was developed by the team as part of the 34th Conference on Neural Information Processing Systems (NeurIPS 2020) conference that took place in Vancouver, Canada in 2020.<sup>1,2</sup>

<ins>References<ins>:

[1]. Cowen-Rivers, A. I., Lyu, W., Wang, Z., Tutunov, R., Jianye, H., Wang, J., & Ammar, H. B. (n.d.). HEBO: Heteroscedastic Evolutionary Bayesian Optimisation.

[2]. Mower, Christopher E., et al. HEBO: Bayesian Optimisation and Reinforcement Learning Library library developed by Huawei Noah's Ark Lab. v0.3.4, GitHub, 2020, https://github.com/huawei-noah/HEBO. 
