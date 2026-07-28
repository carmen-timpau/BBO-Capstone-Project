**BBO Week 7 - Bayesian Optimisation Strategy Summary**

1. Perfomed a robust **Kernel Ablation Study** for Gaussian Process surrogate modelling optimisation (performed individually for each Black-Box function), using [**Leave-One-Out Cross-Validation**] LOOCV R² as an out-of-sample (generalization) predictive performance metric to rank the tested kernels.

2. Performed a **Surrogate Model Architecture Comparison Study** to evaluate whether a _Gaussian Process_ or _Deep Ensemble of Neural Networks_ (Multi-Layer Perceptrons, MLPs) better models each of the Black-Box functions (performed individually for each function), using **Root Mean Squared Error (RMSE)** as a surrogate model performance metric, evaluated out-of-sample via **Leave-One-Out Cross-Validation (LOOCV)**.

3. Performed a robust **Acquisition Function Ablation Study** via **Robust Multi-Step Sequential Offline Bayesian Optimization Rollout**, using **Long-Term Cumulative Regret** as the acquisition function's performance metric.

4. Performed a **Binary Classifier Architecture Comparison Study**, benchmarking **NuSVC** against **MLP** for each Black-Box function, using the **Out-of-Sample Stratified 3-Fold Cross Validation Receiver Operating Characteristic - Area Under the Curve (ROC-AUC)** scores to assess their performance at correctly classifying the top-25% best-performing datapoints.
   
5. **HEBO-inspired Non-linear Output Warping** 
   
6. Dynamic Sobol Sampling, SVM/MLP Sobol Candidate Classification
   
7. **Classifier-informed Space Reduction and Acquisition Filtering** 
