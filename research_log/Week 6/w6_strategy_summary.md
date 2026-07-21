**BBO Capstone Project** <br />
_**Overall Strategy Summary - Week 6**_

This week, compared to the previous 5 weeks, which consisted of a lot of human intervention to individually tune the Bayesian Optimisation (BO) ML models, an automated, more comprehensive and robust approach will be taken to try and optimise each GP and acquisition function and test this strategy to see if a significant improvement in predictive model performance (in terms of generating queries that consist of significant output maximisation) will be observed.

In this sense, **Kernel Ablation Studies** were performed for all functions to identify best-performing GP surrogate models for the 8 Black-Box functions. This was done using **Leave-One-Out Cross-Validation (LOOCV)**. The out-of-sample (generalization) predictive performance metric used to rank the tested ML models was the LOOCV R². **Log Marginal Likelihood (LML)** was used as a secondary diagnostic to check for/prevent overfitting. 

**Acquisition Ablation Studies** were performed for all functions to identify best-performing acqusition function and respective hyperparameters using LOOCV. 

A **Dynamic Sobol Sampling Resolution strategy based on dimensionality** was also implemented this week to ensure high candidate resolution for high-dimensional spaces.

The **homo/heteroscedasticity** of each of the 8 functions modelled by Gaussian Processes was also assessed, by plotting the residuals against the predictions of the GP surrogate model and conducting corresponding **Breusch-Pagan tests**. These were performed both pre- (using the latest GP hyperparameters from Week 5's strategies) and post-kernel ablation (using the optimsied kernels) for comparative purposes. Only post-ablation results are taken into consideration.

However, heteroscedasticity was not adressed this week, to allow the performance of fully ablated models to be assessed independent of any measures taken to account for (or despite) function heteroscedaticity, which will reveal important insights. Heteroscedasticity will be dealt with immediately after, in Week 7.

In this sense, for the functions found to be _heteroscedatic_, a **non-linear output warping strategy**<sup>1</sup> will be implemented in Week 7, as deployed by Noah's Ark Lab at Huawei, in their _Heteroscedastic Evolutionary Bayesian Optimization (HEBO)_ algorithm, to deal with non-constant noise variance (heteroscedasticity). This method was developed by the team as part of the _34<sup>th</sup> Conference on Neural Information Processing Systems (NeurIPS 2020)_ that took place in Vancouver, Canada in 2020.<sup>1,2</sup>

<ins>References<ins>:

[1]. Cowen-Rivers, A. I., Lyu, W., Wang, Z., Tutunov, R., Jianye, H., Wang, J., & Ammar, H. B. (n.d.). HEBO: Heteroscedastic Evolutionary Bayesian Optimisation.

[2]. Mower, Christopher E., et al. HEBO: Bayesian Optimisation and Reinforcement Learning Library library developed by Huawei Noah's Ark Lab. v0.3.4, GitHub, 2020, https://github.com/huawei-noah/HEBO. 
