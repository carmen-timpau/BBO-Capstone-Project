**Model Card C**

<br> 
<br> 

**Model Title:** BBO Week 7 Full Bayesian Optimisation ML Pipeline

**Week(s) of Deployment in BBO Capstone Project:** Week 7

**Model Location:** [`experiments/week_07`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments/week_07)

**Model Description:** Reproducible, Transparent, Interpretable & Automated Surrogate Model Selection (GP/Deep Ensemble of MLPs) and Sequential Standalone Kernel and Acquisition Function-Informed Bayesian Optimisation with Classifier-Informed (SVC/MLP) Acquisition Filtering

<br> 
<br> 

<ins> **Intended Use:** </ins>

This Bayesian Optimisation ML model was developed and is intended for use as part of the Black-Box Optimisation (BBO) Challenge, during Week 7 of 13, for next-query prediction generation for each of the 7 given black-box functions. 

Use cases to be avoided include the optimisation of unknown, black-box functions which do not form part of this specific capstone project. In those cases, slight modifications are required to ensure that the number of functions investigated is appropriately matched within loops and any function-specific pre-processing is adapted to the new function(s)’ specific requirements (similar to the log10-transform of function 1’s very small outputs).

<br> 
<br> 

<br> 
<br> 

<ins> **Ethical Considerations:** </ins>

This BO ML pipeline is fully reproducible across identical hardware configurations, with random_state variables always specified for all pseudo-random number generation instances. 

By compiling the results in [`diagnostics_results`]( https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments/week_07/diagnostics_results) in a detailed yet clear, concise and well-structured way, the key results of the BO ML model used for decision-making, as well as any relevant predicted next query values, the pipeline is highly transparent and easily interpretable. Transparency helps to also validate the reproducibility of the results generated using this ML model.

Due to its reproducibility, transparency, interpretability, robustness and statistical reliability, this ML model or its core strategic principles may be adapted for responsible use in real-world Bayesian Optimisation problems. However, because this ML model did not perform as desired (due to limitation (2) mentioned above, most likely), there are several other BO ML models developed within this capstone project (Model Cards E, F, G, H), which may be much more helpful, suitable and effective for such an application.

This ML model does not make use of or produce any sensitive or personal information.

<br> 
<br> 

<ins> **References:** </ins>

1. F. Zhang and Y. Chen. “Direct Regret Optimization in Bayesian Optimization.” arXiv:2507.06529, 2025.
2. A. I. Cowen‑Rivers, W. Lyu, R. Tutunov, Z. Wang, A. Grosnit, R. R. Griffiths, A. M. Maraval, H. Jianye, J. Wang, J. Peters, and H. Bou Ammar. “HEBO: Pushing the Limits of Sample‑Efficient Hyperparameter Optimisation.” arXiv:2012.03826, 2022.
3. T. S. Breusch and A. R. Pagan. “A Simple Test for Heteroscedasticity and Random Coefficient Variation.” Econometrica, 47(5):1287–1294, 1979. https://doi.org/10.2307/1911963.

