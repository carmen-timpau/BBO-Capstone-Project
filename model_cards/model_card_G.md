**Model Card G**

<br> 
<br> 

**Model Title:** BBO Week 11 Full Bayesian Optimisation ML Pipeline

**Week(s) of Deployment in BBO Capstone Project:** Weeks 11 and 12

**Model Locations:** [`experiments/week_11`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments/week_11); [`experiments/week_12`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments/week_12).

**Model Description:** Statistically Reliable, Reproducible, Transparent, Interpretable, Robust & Automated Joint Kernel-Acquisition Function Ablation Hyperparameter Optimisation with Density-Enhanced Best K-Means Cluster-Informed Local-Box Sobol Candidate Search-Driven Bayesian Optimisation

<br> 
<br> 

<ins> **Intended Use:** </ins>

This Bayesian Optimisation ML model was developed and is intended for use as part of the Black-Box Optimisation (BBO) Challenge, during Weeks 11 and 12 of 13, for next-query prediction generation for each of the 8 given black-box functions. 
Use cases to be avoided include the optimisation of unknown, black-box functions which do not form part of this specific capstone project. In those cases, slight modifications are required to ensure that the number of functions investigated is appropriately matched within loops and any function-specific pre-processing is adapted to the new function(s)’ specific requirements (similar to the log10-transform of function 1’s very small outputs).

<br> 
<br> 

<ins> **Model Characteristics:** </ins>

This Bayesian Optimisation ML model makes use of Gaussian Processes (GPs) to perform surrogate modelling for each of the 8 black-box functions investigated in this capstone project, and uses acquisition functions (UCB, EI, PI) or processes (Thompson sampling) to predict the next-query point to be submitted for the expensive execution of the real functions for Weeks 11 and 12.

The GP kernel and acquisition function pair and their hyperparameters to be used for each function in next-query prediction is selected following a transparent and interpretable, grid-search-based **single Full Joint Kernel × Acquisition Rollout Ablation Study** [1] as the core of the pipeline, sweeping a large set of [8 kernel variants](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_11/full_ablation/kernels.py) against [10 acquisition strategies](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_11/full_ablation/acq_strategies.py) balancing exploration with exploitation to various extents, plus a random baseline acquisition function (amounting to 88 kernel x acquisition combinations per function) via a robust **Multi-Step Sequential Offline Bayesian Optimization Rollout**. 

The performance metrics used in this ML model to rank the GP kernel-acqusition function pairs in the joint ablation study are **Mean Final Simple Regret**, used as the _primary performance metric_ and **Area Under the Regret Curve (AURC)** as the _secondary tiebreaker capturing convergence speed_. The kernel-acqusition function pair ranking algorithm computes the 95%CI/SEM uncertainty estimates for both metrics and takes them into account when establishing ties and making ranking decisions. When all metrics are tied, the ranking is based on the raw average value of the primary metric. The highest-ranking kernel-acqusition function pair for each function is then selected as the complete hyperparameter settings to be used for next-query point prediction via Bayesian Optimisation.

A **Holdout Fraction Cap on Rollout Iterations** _ is used to stop every acqusition strategy (including random) from being forced to exhaust the candidate pool and collapse to an artificial 0.0 regret. 

Pre-existing **Manually Tuned Per-function Overrides** from previous model:
- init_per_dim was lowered (2→1) for Functions 4–8 to stop the initial draw from over-consuming higher-dimensional pools and lead to early pool exhaustion, i.e. 0.0 regret (which halts meaningful combo ranking);
- holdout = 0.6 for Functions 1/2 for more usable iterations on their small 19-point pools;
- holdout = 0.15 to Functions 5/8 to fix early pool exhaustion.
- n_seeds = 1000 seeds for Functions 1/2, since small-pool functions need many more seeds than large-pool ones to meaningfully tighten their CIs (since SEM ∝ std/√n_seeds);
- n_seeds = 500 seeds for Functions 3–8, based on diagnostics from prior runs using n_seeds=100 and n_seeds=20 (which led to an extremely high number of other combos to be statistically indistinguishable from the 'winner' due to overlapping 95% CI, and therefore not giving any meaningful insights at that point).
- n_init_base = 4 Functions 1/2 (5→4) to stay under the 25% pool-fraction threshold.

Pre-existing **[Diagnostic] flags** from previous model for:
-	when n_init alone consumes a disproportionate share (>25%) of a function's pool, since that lets the initial random draw "accidentally" capture the max before acquisition ever runs. 
-	when multiple points share the exact global max value within the dataset** (as it was the case for Function 5, for which the maximum was most likely already identified based on repetitive past query predictions saved to the dataset), since that trivially inflates how "discriminating" regret-based ranking appears regardless of actual strategy quality, and therefore some caution is required when interpreting results for such functions.

**K-Means Clustering-Informed Local Box Definition** is implemented between the joint ablation study and next-query prediction, for the _identification of the most promising region to sample from for the overarching goal of global function maximisation, via unsupervised learning_. For each function, K-means was swept across a range of k values, with the **best number of clusters (k)** selected _via_ a **distance-to-chord elbow heuristic**. The cluster containing the current highest-output (best-observed) point for each function was identified as defining the "most promising" sampling region, and a **bounding box** was computed around it (in original input units, expanded by a margin so that a small cluster doesn't produce a near-zero-volume box). If the elbow selects k=1 (no real cluster structure), the box defaults to the full domain, essentially disabling this step for that function.

**Principal Component Analysis (PCA)-based Cluster Visualisation** is used for each Black-Box function that has an input-space dimensionality higher than 2D (Functions 3-8). Either 2 or 3 (rigid cap) principal components were selected, based on the smallest component count which reached a target cumulative explained variance threshold (80% by default). Scree plots were generated to make this 2-vs-3 decision visually interpretable, showing per-component and cumulative explained variance for every function with 3+ input dimensions.

An advanced **Density-Enhanced K-Means Clustering-Informed Local-Box Sobol Sampling** strategy is introduced, to enrich the existing **Full-Space Sobol Sampling with Dynamically Scaled Resolution to Input Dimensionality** strategy utilised so far, by leveraging the additional knowledge regarding the best K-Means cluster region to sample from for each function for the goal of global function maximisation. Two separate Sobol candidate sampling pools were generated for acquisition scoring and next-query prediction: the already used _full-domain Sobol candidate pool_, and a _density-enhanced K-Means clustering-informed local-box Sobol candidate pool_.

-	The local-box Sobol candidate density enhancement is performed in a controlled manner to avoid introducing bias, by initially density-matching the local-box pool with the full-space pool for each function (accounting for the box's actual volume, computed in log-space for numerical stability at higher dimensions), then applying a preset resolution boost on top of that density-matched baseline. A floor and a cap were also used to keep small/large boxes within good performance limits.
        
-	 The **GP** is still **trained on the full dataset** for each function, but **the final candidate is chosen by argmax over the combined Sobol pools**, so that _the most promising region (defined via the computed best K-Means cluster) gets denser candidate resolution without removing the rest of the domain from consideration_. In this way, the BO pipeline remains fully flexible and non-myopic to the full space, while leveraging the most promising regions that seem to be surrounding a maximum. This maximises the chances of predicting a very high-quality next query point per function and achieving the goal of efficient global function maximisation.

**Per-Pool Best Candidate [Diagnostics]** report the **best acquisition score** achievable, as well as the **GP's predicted value and std** for each pool's (full-space and local-box) own best identified candidate. This ensures a **true and fair comparison** between selected candidates, and their unchosen runner-ups can be made, enabling **full algorithmic transparency and interpretability**.

**HEBO-style Non-Linear Output Warping** [2] is implemented to handle function heteroscedasticities, which is accompanied by appropriate unwarping. Function 1 requires a specific log10 pre-transform with data-driven clipping floor and reversal to original scales on unwarping.

**Dynamic Sobol Sampling Resolution Scaled to Input Dimensionality** is used for continuous-domain next-query candidate generation, with the _Sobol seed tied to the current dataset size_ (rather than a fixed seed).

A _Near-Duplicate Exclusion Filter_ (currently disabled feature in this model, min_distance_to_existing=0.0) for next-query candidate generation may be used in future/other pipelines/implementations to prevent the BO model from predicting next-query points which are too close to (or the same as) existing datapoints.


<br> 
<br> 

<ins> **Additions to Previous Version:** </ins>

In addition to the ML model deployed in Week 10 of the BBO capstone project, which is represented by the previous version of this model, described in [Model Card F](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/model_cards/model_card_F.md), this model brings with it the following improvements:

Introduced **K-Means Clustering-Informed Local Box Definition** as a new BBO pipeline step between the joint ablation study and next-query prediction, for the _identification of the most promising region to sample from for the overarching goal of global function maximisation, via unsupervised learning_, as described in section above.

Introduced an advanced **Density-Enhanced K-Means Clustering-Informed Local-Box Sobol Sampling** strategy, to enrich the existing **Full-Space Sobol Sampling with Dynamically Scaled Resolution to Input Dimensionality** strategy utilised so far, by leveraging the additional knowledge regarding the best K-Means cluster region to sample from for each function for the goal of global function maximisation, as described in section above.

Introduced **Per-Pool Best Candidate [Diagnostics]** to report the **best acquisition score** achievable, and the **GP's predicted value and std** for each pool's (full-space and local-box) own best identified candidate, to ensure a **true and fair comparison** between selected candidates and their unchosen runner-ups can be made, enabling **full algorithmic transparency and interpretability**.

This model also fixes _ 2 minor Function 1-specific reporting bugs from Week 10's pipeline_ stemming from Function 1's log10 pre-transform (Important: these 2 bugs did not impact next-query predictions or any downstream computation or decisions. They are only related to the scale and the non-ideal rounding of exactly 2 printed Function 1-related values within the generated report, which were included in the report for completeness and were not used to make any decisions):
    - "Mean Best Value Found" in the ablation summary was reporting log10(value) directly instead of converting back to the original near-zero scale via 10**x. This is fixed in this pipeline, by back-transforming for Function 1. This was reported as unrounded, as the output values of Function 1 are specifically small and rounding even to 6 decimals prints '0.000000'.
    - The next-query predicted output value reported for Function 1 was left unrounded, since the output values of Function 1 are specifically small and rounding even to 6 decimals prints '0.000000'. Function 1 now prints unrounded values in these diagnostics (for both candidate pools); Functions 2-8 kept the original formatting from before.

<br> 
<br> 

<ins>**Performance Results:** </ins> 

The model outputs an in-depth well-structured and clear written report detailing the key aspects of the joint kernel-acqusition function ablation study (including the mean final regret metric with printed uncertainty estimates 95%CI/SEM + AURC secondary tie-breaking metric), elbow-heuristic computation, K-Means clustering computation, best cluster selection, scree-plot computation and cluster plotting in PC reduced dimensionality space, followed by in-depth metrics about the highest scoring Sobol candidates from each candidate pool (full-space, local-box) for interpretability and transparency purposes.

Right at the end of the execution log file, for each function, a concise summary of the next-query point input coordinates, along with the selected GP kernel and acqusition function used is printed, as well as the predicted output value and standard deviation. The summary table also mentions for each function, from which Sobol  pool the final candidate was chosen (full-space or best K-Means cluster-informed local-box), and specifies exactly what the acqusition scores were for the best candidates from each pool (full-space vs local-box), as well as their input coordinates to increase trustworthiness in the model, transparency, interpretability by enabling candidate comparison and decision rationalisation.

The model also outputs a series of plots with the results of the joint kernel ablation study (**Figure 1**), the Elbow plot (**Figure 2**), the PCA scree plot (**Figure 3**) and the final K-Means cluster plot for each function (**Figure 4**), as shown in the section below. These plots help with model transparency and interpretability.

This BO ML model, when deployed in Week 11 of the BBO capstone, it managed to further maximise 1 out of 8 Black-Box functions, specifically Function 3. 
As the current Week 11 BBO pipeline is very robust, it was also deployed to predict the next queries for all Black-Box functions during Week 12 (penultimate week) of the BBO project, when it managed to further maximise another 1 out of 8 Black-Box functions, specifically Function 6.

Not further maximising the rest of the functions does not reflect on the quality or performance of the pipeline itself, as some (if not many) of these Black-Box functions may have already been maximised by now (within the initial dataset-restricted input space investigated, see limitation (1) below), in previous weeks. In that case, there would be no better points left to be identified through Bayesian Optimisation for those functions and therefore future next query predictions would not be able to override the current already established (global) maxima, regardless of how rigorous and effective the pipeline has become.

<br> 
<br> 

<ins>**Representative Model Outputs:** </ins>

Full execution output results produced by this ML model obtained post-deployment on [`wk11_input_data.pkl`]( https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_11/wk11_input_data.pkl) input data in Week 11 of the BBO capstone project can be accessed at: [`experiments/week_11/diagnostics_results/execution_output.log`]( https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_11/diagnostics_results/execution_output.log). Plots are shown below, but also available at [`experiments/week_11/diagnostics_results`]( https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments/week_11/diagnostics_results).

<br>
 
<img width="6569" height="3247" alt="full_joint_ablation_all_functions_legend" src="https://github.com/user-attachments/assets/87f24bd2-7011-43bc-9c7d-208ab0941475" />


**Figure 1.** _Plotted Results of the Single Full Joint GP Kernel-Acqusition Function Ablation Study performed in Week 11 of the BBO Capstone Project via Bayesian Optimisation Model G Deployment._ Highlighted trajectories represent the rollout next-query selection performance of top 5 kernel-acqusition function pairs which ranked highest based on the performance metrics used in the study (see below).

<br>

<img width="6567" height="2951" alt="kmeans_elbow_grid" src="https://github.com/user-attachments/assets/aa8a3c5e-7095-4737-ab48-cbec056933bc" />

**Figure 2**. _K-Means Elbow Curves per Function Plot (k selected via distance-to-chord heuristic)_ computed in Week 11 of the BBO Capstone Project to visualise the selection of the ideal number of K-Means clusters per unknown function.

<br>
 
<img width="6559" height="2950" alt="pca_scree_grid" src="https://github.com/user-attachments/assets/f9d06e05-cc46-4cf1-b7f1-56b4e9ff0fe9" />

**Figure 3.** _PCA Scree Plots per Function (for n_dims>=3 only): Per-component and Cumulative Explained Variance (smallest of 2-3 PCs reaching 80% cumulative variance, capped at 3)._ Computed in Week 11 of the BBO Capstone Project to select ideal number of PCs.

<br>

 <img width="7166" height="3543" alt="kmeans_cluster_grid" src="https://github.com/user-attachments/assets/f9ca3211-55db-410e-b75a-52b319237428" />

**Figure 4.** _K-Means Cluster Assignments per Function (best cluster outlined in black). _Computed in Week 11 of the BBO Capstone Project. A higher resolution Sobol search was performed in the local-box defined by the best K-Means cluster identified for each function to better inform next-query point prediction, while maintaining normal-resolution full-space Sobol search for best outcomes.

<br>

Similarly, full execution output results produced by this ML model obtained post-deployment on [`wk12_input_data.pkl`]( https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_12/wk12_input_data.pkl) input data in Week 12 of the BBO capstone project can be accessed at: [`experiments/week_12/diagnostics_results/execution_output.log`]( https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_12/diagnostics_results/execution_output.log). Plots are also available in [`experiments/week_12/diagnostics_results`]( https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments/week_12/diagnostics_results).

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

**(3)** the 95% CI and SEM are not printed in the report for the secondary performance metric AURC, to avoid cluttering the report  with too much additional information (that is not always used), which may slightly lower the transparency and interpretability of the model, but nonetheless these values are computed internally and used to thoroughly rank the GP kernel-acqusition function pairs when there is a tie between pairs in the primary metric (mean final regret) in the same way that they are used for ranking the pairs based on the primary metric (when there is no tie), for which 95% CIs and SEM are always printed in the report tables.

The first limitation (1) contributes to a real bias in the possible optimisation results obtained, as potential function maximisation results will always be bounded to the high-dimensional space restricted by the given initial dataset for each function. A potential failure mode of this BO ML pipeline resulting directly from limitation (1) is when applied to black-box functions which do not contain any further maxima than the ones given in their initial datasets, in which case the model will perpetually fail to predict a higher-outputting input query point for those functions. 

Because of these limitations, and despite the assumptions made that are stated above, the resulting next-query predictions remain exploratory estimates, not guarantees of beating the current known maximum for each function. The 95% CI/SEM uncertainty reporting is meant to make explicit how much uncertainty still surrounds the "winning" GP kernel-acquisition function pair per function, rather than presenting a single point-estimate ranking as more settled than it is, therefore enhancing the transparency and interpretability of the model.

These limitations, while very real and likely to have prevented the pipeline to perform at its absolute best performance, have not prevented the BO ML model to further maximise the outputs of black-box functions and achieve significant progress.

<br> 
<br> 

<ins> **Ethical Considerations:** </ins>

This BO ML pipeline is fully reproducible across identical hardware configurations, with random_state variables always specified for all pseudo-random number generation instances. Note that parallel execution via n_jobs = -1 may introduce slight variation if migrated across different systems or environments.

By printing a detailed yet clear, concise and well-structured `execution_output.log` summarising the key results of the BO ML model used for a rather complex decision-making process, as well as any relevant acqusition scores, input coordinates and predicted next query values for both the K-Means cluster-defined local-box and full-space, the pipeline is highly transparent and easily interpretable. This advanced transparency also helps validate the reproducibility of the results generated using this ML model, while increasing the overall users’ trust in its outputs and decision-making process.

Due to its reproducibility, transparency, interpretability, robustness and statistical reliability, this ML model or its core strategic principles may be adapted for responsible use in real-world Bayesian Optimisation problems.
This ML model does not make use of or produce any sensitive or personal information.

<br> 
<br> 

**<ins>Note:</ins>** The BBO Week 11 Full ML Bayesian Optimisation Pipeline is **computationally heavy**. _Runtime to completion_ is expected to be around **~2.5h if 16 CPU cores are available** (as used here), but it may take slightly/significantly longer if not.

<br> 
<br> 

<ins> **References:** </ins>

1. F. Zhang and Y. Chen. “Direct Regret Optimization in Bayesian Optimization.” arXiv:2507.06529, 2025.
2. A. I. Cowen‑Rivers, W. Lyu, R. Tutunov, Z. Wang, A. Grosnit, R. R. Griffiths, A. M. Maraval, H. Jianye, J. Wang, J. Peters, and H. Bou Ammar. “HEBO: Pushing the Limits of Sample‑Efficient Hyperparameter Optimisation.” arXiv:2012.03826, 2022.
