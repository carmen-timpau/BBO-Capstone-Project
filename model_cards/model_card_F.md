**Model Card F**

<br> 
<br> 

**Model Title:** BBO Week 10 Full Bayesian Optimisation ML Pipeline

**Week(s) of Deployment in BBO Capstone Project:** Week 10

**Model Location:** [`experiments/week_10`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments/week_10)

**Model Description:** Statistically Reliable, Reproducible, Transparent, Interpretable, Robust & Automated Joint Kernel-Acquisition Function Ablation-Informed Bayesian Optimisation

<br> 
<br> 

**Intended Use:**

This Bayesian Optimisation ML model was developed and is intended for use as part of the Black-Box Optimisation (BBO) Challenge, during Week 10 of 13, for next-query prediction generation for each of the 8 given black-box functions. 
Use cases to be avoided include the optimisation of unknown, black-box functions which do not form part of this specific capstone project. In those cases, slight modifications are required to ensure that the number of functions investigated is appropriately matched within loops and any function-specific pre-processing is adapted to the new function(s)’ specific requirements (similar to the log10-transform of function 1’s very small outputs).

<br> 
<br> 

<ins> **Model Characteristics:** </ins>

This Bayesian Optimisation ML model makes use of Gaussian Processes (GPs) to perform surrogate modelling for each of the 8 black-box functions investigated in this capstone project, and uses acquisition functions (UCB, EI, PI) or processes (Thompson sampling) to predict the next-query point to be submitted for the expensive execution of the real functions for Week 10.

The GP kernel and acquisition function pair and their hyperparameters to be used for each function in next-query prediction is selected following a transparent and interpretable, grid-search-based **single Full Joint Kernel × Acquisition Rollout Ablation Study** [1] as the core of the pipeline, sweeping a large set of 8 kernel variants against 10 acquisition strategies balancing exploration with exploitation to various extents, plus a random baseline acquisition function (amounting to 88 kernel x acquisition combinations per function) via a robust **Multi-Step Sequential Offline Bayesian Optimization Rollout**. 

The performance metrics used in this ML model to rank the GP kernel-acqusition function pairs in the joint ablation study are **Mean Final Simple Regret**, used as the _primary performance metric_ and ** Area Under the Regret Curve (AURC)** as the _secondary tiebreaker capturing convergence speed_. The kernel-acqusition function pair ranking algorithm computes the 95%CI/SEM uncertainty estimates for both metrics and takes them into account when establishing ties and making ranking decisions. When all metrics are tied, the ranking is based on the raw average value of the primary metric. The highest-ranking kernel-acqusition function pair for each function is then selected as the complete hyperparameter settings to be used for next-query point prediction via Bayesian Optimisation.

A **Holdout Fraction Cap on Rollout Iterations** _ is used to stop every acqusition strategy (including random) from being forced to exhaust the candidate pool and collapse to an artificial 0.0 regret_. A few data-driven, function-specific modifications have been made to the holdout percentage, to address a few observations, as detailed in the section below.

**HEBO-style Non-Linear Output Warping** [2] is implemented to handle function heteroscedasticities, which is accompanied by appropriate unwarping. Function 1 requires a specific log10 pre-transform with data-driven clipping floor and reversal to original scales on unwarping.

**Dynamic Sobol Sampling Resolution Scaled to Input Dimensionality** is used for continuous-domain next-query candidate generation, with the _Sobol seed tied to the current dataset size_ (rather than a fixed seed).

A _Near-Duplicate Exclusion Filter_ (currently disabled feature in this model, min_distance_to_existing=0.0) for next-query candidate generation may be used in future/other pipelines/implementations to prevent the BO model from predicting next-query points which are too close to (or the same as) existing datapoints.

<br> 
<br> 

<ins> **Additions to Previous Version:** </ins>

In addition to the ML model deployed in Week 9 of the BBO capstone project, which is represented by the previous version of this model, described in [Model Card E](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/model_cards/model_card_E.md), this model brings with it the following improvements:

Added **Uncertainty Quantification** to the Kernel x Acquisition pair ranking to improve interpretability, transparency and statical reliability. Specifically, **Standard Errors (SEM)** and **95% Confidence Intervals** (t-distribution, computed across seeds) were added to the **Mean Simple Final Regret** combo scoring system, plus a _"Vs #1 Ranked" flag showing whether a pair’s 95% CI overlaps the #1-ranked combo's_, so near-ties are surfaced explicitly instead of the ranking being read as fully settled. 

The **95% CI/SEM uncertainty estimation was implemented for Area Under the Regret Curve (AURC) secondary metric** as well, with **Degenerate Regret Detection**: when final regret collapses to near-identical values across the top 10 combos (e.g. from ties at the exact max, or a large initial draw already capturing it, making final regret uninformative as a discriminator for meaningful ranking), the "Vs #1 Ranked" flag automatically switches to checking AURC's own CI overlap instead, since _AURC is still capturing genuine differences in convergence speed even when final regret no longer can_ and still leads to a meaningful ranking in that case (although the 95%CIs and SEM for AURC are not printed in the report to keep it less cluttered).

**Manually Tuned Per-function Overrides** were implemented, regarding: _n_init_base/init_per_dim/holdout_fraction/n_seeds_ accordingly, based on pre-production diagnostics, as a mechanism for _handling how much functions differ in dimensionality and pool size_ by the pipeline. As a result, the following overrides emerged:

- init_per_dim was lowered (2→1) for Functions 4–8 to stop the initial draw from over-consuming higher-dimensional pools and lead to early pool exhaustion, i.e. 0.0 regret (which halts meaningful combo ranking);
- raised holdout to 0.6 for Functions 1/2 for more usable iterations on their small 19-point pools;
- lowered holdout to 0.15 to Functions 5/8 to fix early pool exhaustion.
- n_seeds was raised to 1000 seeds (from 20, then 100) for Functions 1/2, since small-pool functions need many more seeds than large-pool ones to meaningfully tighten their CIs (since SEM ∝ std/√n_seeds);
- n_seeds was raised to 500 seeds for Functions 3–8, based on diagnostics from prior runs using n_seeds=100 and n_seeds=20 (which led to an extremely high number of other combos to be statistically indistinguishable from the 'winner' due to overlapping 95% CI, and therefore not giving any meaningful insights at that point).

A **[Diagnostic] Flag was added for when n_init alone consumes a disproportionate share (>25%) of a function's pool**, since that lets the initial random draw "accidentally" capture the max before acquisition ever runs. As a result, the following override emerged:
- n_init_base lowered for Functions 1/2 (5→4) to stay under the 25% pool-fraction threshold.

A **[Diagnostic] Flag was added for when multiple points share the exact global max value within the dataset** (as it was the case for Function 5, for which the maximum was most likely already identified based on repetitive past query predictions saved to the dataset), since that trivially inflates how "discriminating" regret-based ranking appears regardless of actual strategy quality, and therefore some caution is required when interpreting results for such functions.

**Fixed a previously missed reproducibility bug** where Thompson Sampling's (TS) random_state was defaulting to 'None' during next-query scoring (caught on Function 5). TS now uses a deterministic seed for next-query scoring and the prediction is fully reproducible, matching EI/UCB/PI.

<br> 
<br> 

<ins>**Performance Results:** </ins> 

For each function, a summary of the next-query point input coordinates, along with the selected GP kernel and acqusition function used is printed, as well as the predicted output value and standard deviation. The results of the joint kernel ablation are also plotted, as shown in the section below.

This BO ML pipeline, deployed in Week 10 of the BBO capstone project, managed to further maximise 3 out of 8 black-box functions, specifically functions 1, 4 and 6. While Functions 4 and 6 have been maximised before, Function 1 has been maximised for the first time since the start of this project, which proves that this ML pipeline performed extremely well and represents a great improvement from previous versions.
While this pipeline has not managed to further maximise other functions (functions 2, 3, 5, 7, 8), this does not reflect on the quality or performance of the pipeline itself, as some of these functions may have already been maximised by now (over the limited investigated area bounded by input datasets, see limitation (1) below), in previous weeks.

<br> 
<br> 

<ins>**Representative Model Outputs:** </ins>

Full execution output results produced by this ML model obtained post-deployment on [`wk10_input_data.pkl`]( https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_10/wk10_input_data.pkl) input data in Week 10 of the BBO capstone project can be accessed at: [`experiments/week_10/diagnostics_results/execution_output.log`]( https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_10/diagnostics_results/execution_output.log).
Figure 1 below illustrates an overview of the Single Full Joint GP Kernel-Acqusition Function Ablation Study performed in Week 10 of the BBO Capstone Project to select the ‘winning’ kernel-acqusition function pairs to be used in next-query prediction for each function via deployment of Bayesian Optimisation ML Model F.

 <img width="6569" height="3247" alt="full_joint_ablation_all_functions_legend" src="https://github.com/user-attachments/assets/3462aaa6-18d5-4555-8f80-98d8400c1a0d" />

**Figure 1.** Plotted Results of the Single Full Joint GP Kernel-Acqusition Function Ablation Study performed in Week 10 of the BBO Capstone Project via Bayesian Optimisation Model F Deployment. Highlighted trajectories represent the rollout next-query selection performance of top 5 kernel-acqusition function pairs which ranked highest based on the performance metrics used in the study (see below).


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

**(3)** the 95% CI and SEM are not printed in the report for the secondary performance metric AURC, to not clutter the report  with too much additional information (that is not always used), which may however slightly lower the transparency and interpretability of the model, but nonetheless these values are computed internally and used to thoroughly rank the GP kernel-acqusition function pairs when there is a tie between pairs in the primary metric (mean final regret) in the same way that they are used for ranking the pairs based on the primary metric (when there is no tie), for which 95% CIs and SEM are always printed in the report tables.

The first limitation (1) contributes to a real bias in the possible optimisation results obtained, as potential function maximisation results will always be bounded to the high-dimensional space restricted by the given initial dataset for each function. A potential failure mode of this BO ML pipeline resulting directly from limitation (1) is when applied to black-box functions which do not contain any further maxima than the ones given in their initial datasets, in which case the model will perpetually fail to predict a higher-outputting input query point for those functions. 

Because of these limitations, and despite the assumptions made that are stated above, the resulting next-query predictions remain exploratory estimates, not guarantees of beating the current known maximum for each function. The 95% CI/SEM reporting added this week to the pipeline is meant to make explicit how much uncertainty still surrounds the "winning" GP kernel-acquisition function pair per function, rather than presenting a single point-estimate ranking as more settled than it is, therefore enhancing the transparency and interpretability of the model.

These limitations, while very real and likely to have prevented the pipeline to perform at its absolute best performance, have not prevented the BO ML model to further maximise the outputs of black-box functions and achieve significant progress, as well as an important milestone (maximising the very-challenging-to-model-and-optimise black-box Function 1 for the first time in the project).

<br> 
<br> 

<ins> **Ethical Considerations:** </ins>

This BO ML pipeline is fully reproducible across identical hardware configurations, with random_state variables always specified for all pseudo-random number generation instances. Note that parallel execution via n_jobs = -1 may introduce slight variation if migrated across different systems or environments.

By printing a detailed yet clear, concise and well-structured `execution_output.log` summarising the key results of the BO ML model used for decision-making, as well as any relevant predicted next query values, the pipeline is highly transparent and easily interpretable. This advanced transparency also helps validate the reproducibility of the results generated using this ML model.

Due to its reproducibility, transparency, interpretability, robustness and statistical reliability, this ML model or its core strategic principles may be adapted for responsible use in real-world Bayesian Optimisation problems.
This ML model does not make use of or produce any sensitive or personal information.

<br> 
<br> 

**<ins>Note:</ins>** The BBO Week 10 Full ML Bayesian Optimisation Pipeline is **computationally heavy**. _Runtime to completion_ is expected to be around **~2h if 16 CPU cores are available** (as used here), but it may take slightly/significantly longer if not.

<br> 
<br> 

<ins> **References:** </ins>

1. F. Zhang and Y. Chen. “Direct Regret Optimization in Bayesian Optimization.” arXiv:2507.06529, 2025.
2. A. I. Cowen‑Rivers, W. Lyu, R. Tutunov, Z. Wang, A. Grosnit, R. R. Griffiths, A. M. Maraval, H. Jianye, J. Wang, J. Peters, and H. Bou Ammar. “HEBO: Pushing the Limits of Sample‑Efficient Hyperparameter Optimisation.” arXiv:2012.03826, 2022.
