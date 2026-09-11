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

This Bayesian Optimisation ML model was developed and is intended for use as part of the Black-Box Optimisation (BBO) Challenge, during Week 7 of 13, for next-query prediction generation for each of the 8 given black-box functions. 

Use cases to be avoided include the optimisation of unknown, black-box functions which do not form part of this specific capstone project. In those cases, slight modifications are required to ensure that the number of functions investigated is appropriately matched within loops and any function-specific pre-processing is adapted to the new function(s)’ specific requirements (similar to the log10-transform of function 1’s very small outputs).

<br> 
<br> 

<br> 
<br> 

<ins> **Limitations, Biases & Potential Failure Modes:** </ins>

The main limitations of this BO ML model are:

**(1)** the Sobol candidate generation across the high-dimensional input space was restricted by the per-dimension minimum and maximum values observed in the initial dataset for each black-box function, meaning that the search was only conducted within the bounding box defined by the initial datapoints for each black-box function; and 

**(2)** the 'best' kernel and acquisition function pair to be used for next-query prediction for each black-box function is computed separately in this model, _via_ two sequential, standalone ablation studies, which completely disregard the direct and intrinsic interaction between the kernel and the acquisition function [1] in Bayesian Optimisation, and consequently their performance as a whole. By firstly selecting the kernel _via_ ablation and fixing it in place for each black-box function, to only then go on and perform an acquisition function ablation study in search for the 'best' acquisition function for each objective using only that fixed-in-place kernel chosen prior to this, the model may very likely deliver suboptimal results (hyperparameter settings), by being prevented to even test the performance of several kernel-acquisition function combinations as a whole; and

**(3)** the post-kernel ablation Breusch-Pagan-style analysis study performed does not output statistically valid p-values, as the residuals plotted are not OLS residuals, but computed using surrogate model predictions. This adapted study was not performed to achieve full statistical certainty over black-box function behaviour, but only to visually reveal and monitor homo-/heteroscedasticity in the black-box functions’ behaviour, based on the scattered residuals’ shape in the plots.  

The first limitation (1) contributes to a real bias in the possible optimisation results obtained, as potential function maximisation results will always be bounded to the high-dimensional space restricted by the given initial dataset for each function. A potential failure mode of this BO ML pipeline resulting directly from limitation (1) is when applied to black-box functions which do not contain any further maxima within the area restricted by their input datasets' coordinates, other than the ones given in their initial datasets, in which case the model will perpetually fail to predict a higher-outputting input query point for those functions. 

Because of these limitations, and despite the assumptions made that are stated above, the resulting next-query predictions remain exploratory estimates, not guarantees of beating the current known maximum for each function. 

These limitations are real. Limitation (2) specifically may have likely severely prevented the pipeline to perform at its absolute best performance, by delivering suboptimal results.

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

