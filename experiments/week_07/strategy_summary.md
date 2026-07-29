**BBO Week 7 - Bayesian Optimisation Strategy Summary**

1. Perfomed a robust **Kernel Ablation Study** for Gaussian Process surrogate modelling optimisation (performed individually for each Black-Box function), using [**Leave-One-Out Cross-Validation**] LOOCV R² as an out-of-sample (generalization) predictive performance metric to rank the tested kernels.

2. Performed a **Surrogate Model Architecture Comparison Study** to evaluate whether a _Gaussian Process_ or _Deep Ensemble of Neural Networks_ (Multi-Layer Perceptrons, MLPs) better models each of the Black-Box functions (performed individually for each function), using **Root Mean Squared Error (RMSE)** as a surrogate model performance metric, evaluated out-of-sample via **Leave-One-Out Cross-Validation (LOOCV)**.

3. Performed a robust **Acquisition Function Ablation Study** _via_ **Robust Multi-Step Sequential Offline Bayesian Optimization Rollout**, using **Long-Term Cumulative Regret** as the acquisition function's performance metric.

4. Performed a **Binary Classifier Architecture Comparison Study**, benchmarking **NuSVC** against **MLP**, using the **Out-of-Sample Stratified 3-Fold Cross Validation Receiver Operating Characteristic - Area Under the Curve (ROC-AUC)** scores to assess their performance at correctly classifying the top-25% highest-output datapoints within the dataset of each Black-Box function. The best-performing classifier for each function was used for **Classifier-informed Space Reduction and Acquisition Filtering**. 
   
5. Implemented **Dynamic Sobol Sampling Resolution strategy based on dimensionality** to ensure high candidate resolution for high-dimensional spaces.

6. Implemented **HEBO-inspired Non-linear Output Warping** to stabilize target variance and mitigate heteroscedasticity, improving the surrogate model's predictive accuracy during hyperparameter optimization.

