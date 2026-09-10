**Model Card E**

<br> 
<br> 

**Model Title:** BBO Week 9 Full Bayesian Optimisation ML Pipeline

**Week(s) of Deployment in BBO Capstone Project:** Week 9

**Model Location:** [`experiments/week_09`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments/week_09)

**Model Description:** Reproducible, Transparent, Interpretable, Robust & Automated Joint Kernel-Acquisition Function Ablation-Informed Bayesian Optimisation

<br> 
<br> 

<ins> **Intended Use:** </ins>

This Bayesian Optimisation ML model was developed and is intended for use as part of the Black-Box Optimisation (BBO) Challenge, during Week 9 of 13, for next-query prediction generation for each of the 8 given black-box functions. 
Use cases to be avoided include the optimisation of unknown, black-box functions which do not form part of this specific capstone project. In those cases, slight modifications are required to ensure that the number of functions investigated is appropriately matched within loops and any function-specific pre-processing is adapted to the new function(s)’ specific requirements (similar to the log10-transform of function 1’s very small outputs).

<br> 
<br> 

<ins> **Model Characteristics:** </ins>

This Bayesian Optimisation ML model makes use of Gaussian Processes (GPs) to perform surrogate modelling for each of the 8 black-box functions investigated in this capstone project, and uses acquisition functions (UCB, EI, PI) or processes (Thompson sampling) to predict the next-query point to be submitted for the expensive execution of the real functions for Week 9.

The GP kernel and acquisition function pair and their hyperparameters to be used for each function in next-query prediction is selected following a transparent and interpretable, grid-search-based **single Full Joint Kernel × Acquisition Rollout Ablation Study** [1] as the core of the pipeline, sweeping a large set of [8 kernel variants](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_09/full_ablation/kernels.py) against [10 acquisition strategies](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_09/full_ablation/acq_strategies.py) balancing exploration with exploitation to various extents, plus a random baseline acquisition function (amounting to 88 kernel x acquisition combinations per function) via a robust **Multi-Step Sequential Offline Bayesian Optimization Rollout**. 

The performance metrics used in this ML model to rank the GP kernel-acqusition function pairs in the joint ablation study are **Mean Final Simple Regret** (directly reflecting the global maximization goal [1]), used as the _primary performance metric_ and **Area Under the Regret Curve (AURC)** as the _secondary tiebreaker capturing convergence speed_. The highest-ranking kernel-acqusition function pair for each function is selected as the complete hyperparameter settings to be used for next-query point prediction via Bayesian Optimisation. A Random Baseline (uniform random candidate selection) is added to every function's ablation, to confirm whether the tested acquisition strategies meaningfully outperform blind search rather than assuming it, as it was done before.

A **Holdout Fraction (30%) Cap on Rollout Iterations** _ is used to prevent every acqusition strategy (including random) from being forced to exhaust the finite candidate pool and collapse to an artificial 0.0 regret. 

**HEBO-style Non-Linear Output Warping** [2] is implemented to handle function heteroscedasticities, which is accompanied by appropriate unwarping. Function 1 requires a specific log10 pre-transform with data-driven clipping floor and reversal to original scales on unwarping.

**Dynamic Sobol Sampling Resolution Scaled to Input Dimensionality** is used for continuous-domain next-query candidate generation, with the _Sobol seed tied to the current dataset size_ (rather than a fixed seed).

<br> 
<br> 

<ins> **Additions to Previous Version:** </ins>

In addition to the ML model deployed in Week 8 of the BBO capstone project, which is represented by the previous version of this model, described in [Model Card D](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/model_cards/model_card_D.md), this model brings with it the following improvements:

Replaced the separate BBO Week 8 Sequential Kernel and Acquisition Function Ablation Studies with a single Full Joint Kernel × Acquisition Rollout Ablation Study [1], sweeping all [8 kernel variants]( https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_09/full_ablation/kernels.py) against an enhanced, larger list of [10 acquisition strategies]( https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_09/full_ablation/acq_strategies.py) (plus an added Random Baseline) — 88 combinations tested jointly, per function — via Robust Multi-Step Sequential Offline Bayesian Optimization Rollout. Since kernel and acquisition choices interact, and a kernel selected purely for regression fit quality is not guaranteed to pair best with the eventual acquisition strategy, leading to less-than-optimal-quality query predictions, especially in highly-dimensional spaces [1], this joint study replaced the suboptimal approach taken in BBO Week 8 of selecting the kernel first (via LOOCV R²) and only ablating acquisition functions afterwards, using the 'winning' kernel.
Introduced a Holdout Fraction (30%) Cap on Rollout Iterations, preventing the rollout from exhausting the finite candidate pool. Without this, every strategy (including random) is eventually forced to visit every remaining point, collapsing all combos to an artificial 0.0 final regret and making the ranking metric uninformative - this was identified and corrected after observing it directly in Function 1 and Function 2's initial results.

The addition of a Random Baseline and the holdout-fraction were both introduced reactively, after inspecting intermediate results (plots, tied final-regret values, pool-exhaustion artefacts) in surfaced cases.

Dropped Surrogate Model Architecture Comparison (GP vs. Deep Ensemble) entirely. Given the small sample sizes across all 8 functions (18-48 points), a 5-member MLP ensemble with (32,16) hidden layers is actually heavily overparameterized relative to available data, and any LOOCV RMSE "win" over GP is more plausibly noise than a genuine surrogate quality advantage. GP is now used unconditionally as the surrogate model for all functions, removing this risk along with the associated compute and complexity.

Introduced a _Near-Duplicate Exclusion Filter_ (currently disabled feature in this model, min_distance_to_existing=0.0) for next-query candidate generation may be used in future/other pipelines/implementations to prevent the BO model from predicting next-query points which are too close to (or the same as) existing datapoints.


<br> 
<br> 

<ins>**Performance Results:** </ins> 

For each function, a summary of the next-query point input coordinates, along with the selected GP kernel and acqusition function used is printed, as well as the predicted output value and standard deviation. The results of the joint kernel ablation are also plotted, as shown in the section below.

Week 9's BBO ML Pipeline managed to maximise half (4 out of 8) of the Black-Box functions, specifically Functions 3,4,6,7, which is a great achievement at this stage, indicating good pipeline performance. 
At the stage of Week 9 in the BBO capstone project, Function 1 remains the only one that has not been maximised so far through any of the BBO pipelines, and remains a challenging one to investigate even at this stage, due to a very low amount of initial and current data, as well as its peculiar nature (very spiky, only non-zero and high values in narrow regions of space).
<br> 
<br> 

<ins>**Representative Model Outputs:** </ins>

Full execution output results produced by this ML model obtained post-deployment on [`wk9_input_data.pkl`]( https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_09/wk9_input_data.pkl) input data in Week 9 of the BBO capstone project can be accessed at: [`experiments/week_09/diagnostics_results/full_joint_ablation_results.md`](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_09/diagnostics_results/full_joint_ablation_results.md) and [`experiments/week_09/diagnostics_results/wk9_query_predictions.md`]( https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_09/diagnostics_results/wk9_query_predictions.md).

Plotted Results of the Single Full Joint GP Kernel-Acqusition Function Ablation Study performed in Week 9 of the BBO Capstone Project via Bayesian Optimisation Model E Deployment can be accessed here: [`experiments/week_09/diagnostics_results/full_joint_ablation_all_functions_legend.png`](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_09/diagnostics_results/full_joint_ablation_all_functions_legend.png).

<br> 
<br> 

<ins> **Assumptions:** </ins>

The main assumptions that underlie this strategy are: 

**(1)** that the sets of 8 kernels and 10 acquisition functions implemented within the single full joint kernel-acqusition function ablation sweep study conducted in this BO ML pipeline are overarching and exhaustive enough to truly identify the best performing GP kernel x acquisition function pair to use for each function to predict the highest-quality next query; and

**(2)** that using the mean simple final regret as the primary ranking metric to identify the best-performing kernel-acquisition function pair for each black-box function directly translates into the kernel-acquisition function pair which would generate the highest-quality predicted next query point via Bayesian Optimisation. 
These assumptions may represent good approximations for the given black-box functions, as implementing them effectively led to improvements in their maxima, driving considerable progress.
Without these two assumptions, the Sobol candidates could not have been ranked and the next-query prediction for each unknown function could not have been selected.

<br> 
<br> 

<ins> **Limitations, Biases & Potential Failure Modes:** </ins>

The main limitations of this BO ML model are:

**(1)** the Sobol candidate generation across the high-dimensional input space was restricted by the per-dimension minimum and maximum values observed in the initial dataset for each black-box function, meaning that the search was only conducted within the bounding box defined by the initial datapoints for each black-box function; and 

**(2)** the top few GP kernel-acqusition function pairs within the joint ablation study remained statistically indistinguishable due to overlapping 95% CI values. The ranking of GP kernel-acqusition function pairs for BO hyperparameter system selection (for next-query prediction) was nonetheless performed based on the average, raw mean simple final regret (primary metric) or (if tied) AURC (secondary metric) values. Increasing the number of seeds to 500/1000 (function-specific) has drastically lowered the number of indistinguishable pairs to a more reasonable, small number, making the results more statistically reliable; and

The first limitation (1) contributes to a real bias in the possible optimisation results obtained, as potential function maximisation results will always be bounded to the high-dimensional space restricted by the given initial dataset for each function. A potential failure mode of this BO ML pipeline resulting directly from limitation (1) is when applied to black-box functions which do not contain any further maxima than the ones given in their initial datasets, in which case the model will perpetually fail to predict a higher-outputting input query point for those functions. 

Because of these limitations, and despite the assumptions made that are stated above, the resulting next-query predictions remain exploratory estimates, not guarantees of beating the current known maximum for each function. 

These limitations, while very real and likely to have prevented the pipeline to perform at its absolute best performance, have not prevented the BO ML model to further maximise the outputs of black-box functions and achieve significant progress.

<br> 
<br> 

<ins> **Ethical Considerations:** </ins>

This BO ML pipeline is fully reproducible across identical hardware configurations, with random_state variables always specified for all pseudo-random number generation instances. Note that parallel execution via n_jobs = -1 may introduce slight variation if migrated across different systems or environments.

By printing a detailed yet clear, concise and well-structured `execution_output.log` summarising the key results of the BO ML model used for decision-making, as well as any relevant predicted next query values, the pipeline is highly transparent and easily interpretable. This advanced transparency also helps validate the reproducibility of the results generated using this ML model.

Due to its reproducibility, transparency, interpretability, robustness and statistical reliability, this ML model or its core strategic principles may be adapted for responsible use in real-world Bayesian Optimisation problems.
This ML model does not make use of or produce any sensitive or personal information.

<br> 
<br> 

<ins> **References:** </ins>

1. F. Zhang and Y. Chen. “Direct Regret Optimization in Bayesian Optimization.” arXiv:2507.06529, 2025.
2. A. I. Cowen‑Rivers, W. Lyu, R. Tutunov, Z. Wang, A. Grosnit, R. R. Griffiths, A. M. Maraval, H. Jianye, J. Wang, J. Peters, and H. Bou Ammar. “HEBO: Pushing the Limits of Sample‑Efficient Hyperparameter Optimisation.” arXiv:2012.03826, 2022.
