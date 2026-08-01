**BBO Week 8 - Bayesian Optimisation Strategy Summary**

1. Perfomed a <ins>larger</ins> (7 kernel types tested) and robust **Kernel Ablation Study** for Gaussian Process surrogate modelling optimisation (performed individually for each Black-Box function), using [**Leave-One-Out Cross-Validation**] LOOCV R² as an out-of-sample (generalization) predictive performance metric to rank the tested kernels.

2. Performed a **Surrogate Model Architecture Comparison Study** to evaluate whether a _Gaussian Process_ or _Deep Ensemble of Neural Networks_ (Multi-Layer Perceptrons, MLPs) better models each of the Black-Box functions (performed individually for each function), using **Root Mean Squared Error (RMSE)** as a surrogate model performance metric, evaluated out-of-sample via **Leave-One-Out Cross-Validation (LOOCV)**.

3. Performed a <ins>larger</ins> (6 acquisition process types tested) and robust **Acquisition Function Ablation Study** _via_ **Robust Multi-Step Sequential Offline Bayesian Optimization Rollout**, using **Long-Term Cumulative Regret** as the acquisition function's performance metric.
   
4. Used **Dynamic Sobol Sampling Resolution strategy based on dimensionality** to ensure high candidate resolution for high-dimensional spaces.

5. Implemented **HEBO-inspired Non-linear Output Warping** to stabilize target variance and mitigate heteroscedasticity, improving the surrogate model's predictive accuracy during hyperparameter optimization.

<ins>Note</ins>: The _Classifier-informed Space Reduction and Acquisition Filtering_ that was also implemented within the previous week's strategy was dropped, because it restricted the space and therefore the acquisition process too much which led to poor query predictions. A classifier-free acquisition process was allowed for this week's strategy, to enable the optimised surrogate models, kernels and acquisition functions to ideally generate high-quality queries. This will be confirmed and documented to inform further Bayesian Optimisation stratgies.
