**Model Card D**

<br> 
<br> 

**Model Title:** BBO Week 8 Full Bayesian Optimisation ML Pipeline

**Week(s) of Deployment in BBO Capstone Project:** Week 8

**Model Location:** [`experiments/week_08`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments/week_08)

**Model Description:** Reproducible, Transparent, Interpretable & Automated Surrogate Model Selection (GP/Deep Ensemble of MLPs) and Sequential Standalone Kernel and Acquisition Function-Informed Bayesian Optimisation 

<br> 
<br> 

<ins> **Intended Use:** </ins>

This Bayesian Optimisation ML model was developed and is intended for use as part of the Black-Box Optimisation (BBO) Challenge, during Week 8 of 13, for next-query prediction generation for each of the 8 given black-box functions. 
Use cases to be avoided include the optimisation of unknown, black-box functions which do not form part of this specific capstone project. In those cases, slight modifications are required to ensure that the number of functions investigated is appropriately matched within loops and any function-specific pre-processing is adapted to the new function(s)’ specific requirements (similar to the log10-transform of function 1’s very small outputs).

<br> 
<br> 

<ins> **Model Characteristics:** </ins>

This Bayesian Optimisation ML model makes use of Gaussian Processes (GPs) to perform surrogate modelling for each of the 8 black-box functions investigated in this capstone project, and uses acquisition functions (UCB, EI, PI) or processes (Thompson sampling) to predict the next-query point to be submitted for the expensive execution of the real functions for Week 8.

The GP kernels and related hyperparameters to be used for predicting the next query point for each black-box function in next-query prediction is selected via a **standalone grid-search style GP kernel ablation study** for surrogate model hyperparameter optimisation. This is performed individually for each black-box function, using **Leave-One-Out Cross-Validation (LOOCV) R²** as an out-of-sample (generalization) predictive performance metric to rank the fitting performance of the [8 tested kernels]( https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_08/kernel_ablation/kernels.py) on the unknown functions.

A **Surrogate Model Architecture Comparison Study** was then performed as part of this pipeline to evaluate whether a _Gaussian Process_ or _Deep Ensemble of Neural Networks_ (Multi-Layer Perceptrons, MLPs) better models each of the Black-Box functions (performed individually for each function), using **Root Mean Squared Error (RMSE)** as a surrogate model performance metric, evaluated out-of-sample _via_ **Leave-One-Out Cross-Validation (LOOCV)**.

A grid-search style **Standalone Acquisition Function Ablation Study** using a list of [6 acquisition strategies](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_08/acquisition_ablation/acq_strategies.py), is performed _via_ a **Robust Multi-Step Sequential Offline Bayesian Optimization Rollout** to select the acquisition function to use in next-query prediction. The **Mean Final Simple Regret** is used as the primary acquisition function's performance metric for ranking, and the **Area Under the Regret Curve (AURC)** is implemented as a secondary tiebreaker capturing convergence speed. The best-performing surrogate model for each function identified from the studies conducted prior (see above) is selected to model the black-box functions during this ablation study for each unknown function. 

**HEBO-style Non-Linear Output Warping** [2] is implemented to handle function heteroscedasticities, which is accompanied by appropriate unwarping. Function 1 requires a specific log10 pre-transform with **data-driven clipping** floor and reversal to original scales on unwarping.

**Dynamic Sobol Sampling Resolution Scaled to Input Dimensionality** is used for continuous-domain next-query candidate generation, with a fixed Sobol seed.

<br> 
<br> 

<ins> **Additions to Previous Version:** </ins>

In addition to the ML model deployed in Week 7 of the BBO capstone project, which is represented by the previous version of this model, described in [Model Card C](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/model_cards/model_card_C.md), this model brings with it the following improvements:

Enhanced the list of kernels (6 → 8) and acquisition functions (5 → 6) tested in the standalone ablation studies.

The Classifier-informed Space Reduction and Acquisition Filtering that was implemented within the previous week's strategy was dropped, because it restricted the space and therefore the acquisition process too much which led to poor query predictions. 

Week 7 Strategy used an arbitrary 1e-300 as the clipping floor for function 1, which is not ideal. To ensure that negative/near-zero noise points collapse to a value consistent with Function 1 data's own weakest real signal rather than an extreme, unphysical outlier which confuses the surrogate model fitting, the smallest genuine positive reading in this function's data will be used as the clipping floor this week (data-driven clipping), instead of the arbitrary 1e-300 that was used in Week 7.

<br> 
<br> 

<ins>**Performance Results:** </ins> 

For each function, a summary of the next-query point input coordinates, along with the selected GP kernel and acqusition function used is printed, as well as the predicted output value and standard deviation. The results of the joint kernel ablation are also plotted, as shown in the section below.

Week 8's BBO ML Pipeline did not manage to maximise any of the Black-Box functions.

<br> 
<br> 

<ins>**Representative Model Outputs:** </ins>

The execution output results produced by this ML model obtained post-deployment on [`wk8_input_data.pkl`]( https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_08/wk8_input_data.pkl) input data in Week 8 of the BBO capstone project can be accessed at: [`experiments/week_08/diagnostics_results`]( https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments/week_08/diagnostics_results).
The plots generated by this model after executing it on the [`wk8_input_data.pkl`]( https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_08/wk8_input_data.pkl) input data in Week 8 of the BBO capstone project are presented below.

<br>

 <img width="5972" height="2956" alt="wk8_acquisition_ablation_results_all_functions" src="https://github.com/user-attachments/assets/ba094f58-c5fe-4e5b-9afb-ce497f0dee05" />

**Figure 1.** _Multi-Step Rollout Acquisition Ablation Study _via_ Offline Bayesian Optimization: Simple Regret Trajectories Across Datasets of Black-Box Functions 1-8_


<br>
<br>

<img width="7169" height="3557" alt="wk8_breusch_pagan_all_functions" src="https://github.com/user-attachments/assets/b4c79167-bfc1-4106-8f3c-834daaa1751a" />

<br>
<br>

**Figure 2.** _Post-Kernel Ablation Residuals Plot to Inform Homo-/Heteroscedastic Behaviour of the 8 Unknown, Black-Box Functions._ GP/Deep Ensemble of MLPs predictions were used; therefore, this is only an informational Breusch-Pagan-style analysis study, that may point towards function homo/heteroscedasticity, but where the p-value is strictly not statistically valid. For the latter to be the case, the residuals must be ordinary least squares (OLS) residuals [3], not calculated using surrogate models. This adapted study was not performed to achieve full statistical certainty over black-box function behaviour, but only to visually reveal and monitor homo-/heteroscedasticity in the black-box functions’ behaviour, based on the scattered residuals’ shape in the plots.  

<br> 
<br> 

<ins> **Assumptions:** </ins>

The main assumptions that underlie this strategy are: 

**(1)** that the sets of 8 kernels and 6 acquisition functions implemented within the sequential, standalone kernel and function ablation studies conducted in this BO ML pipeline are overarching and exhaustive enough to truly identify the best performing GP kernel and acquisition function pair to use for each function to predict the highest-quality next query; and

**(2)** that using the mean simple final regret as the primary ranking metric to identify the best-performing kernel-acquisition function pair for each black-box function directly translates into the kernel-acquisition function pair which would generate the highest-quality predicted next query point _via_ Bayesian Optimisation. 

These assumptions may represent good approximations for the given black-box functions, as implementing them effectively led to improvements in their maxima, driving considerable progress.
Without these two assumptions, the Sobol candidates could not have been ranked and the next-query prediction for each unknown function could not have been selected.

<br> 
<br> 

<ins> **Limitations, Biases & Potential Failure Modes:** </ins>

The main limitations of this BO ML model are:

**(1)** the Sobol candidate generation across the high-dimensional input space was restricted by the per-dimension minimum and maximum values observed in the initial dataset for each black-box function, meaning that the search was only conducted within the bounding box defined by the initial datapoints for each black-box function; and 

**(2)** the top few GP kernel-acqusition function pairs within the joint ablation study remained statistically indistinguishable due to overlapping 95% CI values. The ranking of GP kernel-acqusition function pairs for BO hyperparameter system selection (for next-query prediction) was nonetheless performed based on the average, raw mean simple final regret (primary metric) or (if tied) AURC (secondary metric) values. Increasing the number of seeds to 500/1000 (function-specific) has drastically lowered the number of indistinguishable pairs to a more reasonable, small number, making the results more statistically reliable; and

**(3)** the post-kernel ablation Breusch-Pagan-style analysis study performed does not output statistically valid p-values, as the residuals plotted are not OLS residuals, but computed using surrogate model predictions. This adapted study was not performed to achieve full statistical certainty over black-box function behaviour, but only to visually reveal and monitor homo-/heteroscedasticity in the black-box functions’ behaviour, based on the scattered residuals’ shape in the plots.  

The first limitation (1) contributes to a real bias in the possible optimisation results obtained, as potential function maximisation results will always be bounded to the high-dimensional space restricted by the given initial dataset for each function. A potential failure mode of this BO ML pipeline resulting directly from limitation (1) is when applied to black-box functions which do not contain any further maxima within the area restricted by their input datasets' coordinates, other than the ones given in their initial datasets, in which case the model will perpetually fail to predict a higher-outputting input query point for those functions. 

Because of these limitations, and despite the assumptions made that are stated above, the resulting next-query predictions remain exploratory estimates, not guarantees of beating the current known maximum for each function. 

These limitations, while very real and likely to have prevented the pipeline to perform at its absolute best performance, have not prevented the BO ML model to further maximise the outputs of black-box functions and achieve significant progress.

<br> 
<br> 

<ins> **Ethical Considerations:** </ins>

This BO ML pipeline is fully reproducible across identical hardware configurations, with random_state variables always specified for all pseudo-random number generation instances. 

By compiling the results in [`diagnostics_results`]( https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments/week_08/diagnostics_results) in a detailed yet clear, concise and well-structured way, the key results of the BO ML model used for decision-making, as well as any relevant predicted next query values, the pipeline is highly transparent and easily interpretable. Transparency helps to also validate the reproducibility of the results generated using this ML model.

Due to its reproducibility, transparency, interpretability, robustness and statistical reliability, this ML model or its core strategic principles may be adapted for responsible use in real-world Bayesian Optimisation problems.
This ML model does not make use of or produce any sensitive or personal information.

<br> 
<br> 

<ins> **References:** </ins>

1. F. Zhang and Y. Chen. “Direct Regret Optimization in Bayesian Optimization.” arXiv:2507.06529, 2025.
2. A. I. Cowen‑Rivers, W. Lyu, R. Tutunov, Z. Wang, A. Grosnit, R. R. Griffiths, A. M. Maraval, H. Jianye, J. Wang, J. Peters, and H. Bou Ammar. “HEBO: Pushing the Limits of Sample‑Efficient Hyperparameter Optimisation.” arXiv:2012.03826, 2022.
3. T. S. Breusch and A. R. Pagan. “A Simple Test for Heteroscedasticity and Random Coefficient Variation.” Econometrica, 47(5):1287–1294, 1979. https://doi.org/10.2307/1911963.

