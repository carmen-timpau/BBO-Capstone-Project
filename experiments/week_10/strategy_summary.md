**BBO Week 10 - Bayesian Optimisation Strategy Summary**

1. Continued using the **single Full Joint Kernel × Acquisition Rollout Ablation Study** as the core of the pipeline — sweeping all 8 kernel variants against all 10 acquisition strategies plus a Random Baseline (88 kernel x acquisition combinations per function) _via_ **Robust Multi-Step Sequential Offline Bayesian Optimization Rollout**, rather than selecting kernel and acquisition separately [preserved from Week 9].

2. Kept **Gaussian Processes (GPs)** as the **surrogate models for all functions**, having previously already dropped the Deep Ensemble comparison, as it was leading to overparameterized models for such small sample sizes which would generalise poorly [preserved from Week 9].

3. Kept **Mean Final Simple Regret** as the _primary ranking metric_ and **AURC** as the _secondary tiebreaker capturing convergence speed_ [preserved from Week 9]. Added **Uncertainty Quantification to the Kernel x Acquisition Combo Ranking** - **Standard Errors (SEM)** and **95% Confidence Intervals** (t-distribution, computed across seeds) were added to the **Mean Simple Final Regret** combo scoring system, plus a _"Vs #1 Ranked" flag showing whether a combo's CI overlaps the #1-ranked combo's_, so near-ties are surfaced explicitly instead of the ranking being read as fully settled. **Extended this same CI/SEM treatment to AURC** as well, with **degenerate-regret detection**: when final regret collapses to near-identical values across the top 10 combos (e.g. from ties at the exact max, or a large initial draw already capturing it, making final regret uninformative as a discriminator for meaningful ranking), the "Vs #1 Ranked" flag automatically switches to checking AURC's own CI overlap instead, since _AURC is still capturing genuine differences in convergence speed even when final regret no longer can_ and still leads to a meaningful ranking in that case.

4. Kept the **Holdout Fraction Cap on Rollout Iterations** _to stop every strategy (including random) from being forced to exhaust the candidate pool and collapsing to an artificial 0.0 regret_ [preserved from Week 9]. Added a **[Diagnostic] Flag for when n_init alone consumes a disproportionate share (>25%) of a function's pool**, since that lets the initial random draw "accidentally" capture the max before acquisition ever runs. **Tuned the per-function override values** (n_init_base/init_per_dim/holdout_fraction overrides) accordingly, based on pre-production diagnostics:
- n_init_base lowered for Functions 1/2 (5→4) to stay under the 25% pool-fraction threshold;
- init_per_dim was lowered (2→1) for Functions 4–8 to stop the initial draw from over-consuming higher-dimensional pools.
- raised holdout to 0.6 for Functions 1/2 for more usable iterations on their small 19-point pools;
- lowered holdout to 0.15 to Functions 5/8 to fix early pool exhaustion;

5. Kept **Per-function Overrides** (n_init_base, init_per_dim, holdout_fraction) as the mechanism for _handling how much functions differ in dimensionality and pool size_ by the pipeline [preserved from Week 9]. **Extended the same override pattern to n_seeds** (n_seeds_overrides), since  small-pool functions need many more seeds than large-pool ones to meaningfully tighten their CIs (since SEM ∝ std/√n_seeds): 
- For Functions 1/2, n_seeds was raised to 1000 seeds;
- For Functions 3–8, n_seeds was raised to 500 seeds, based on diagnostics from a prior run using n_seeds=100.

6. **Fixed a previously missed reproducibility bug** where Thompson Sampling's (TS) random_state was defaulting to 'None' during next-query scoring (caught on Function 5). TS now uses a deterministic seed for next-query scoring and the prediction is fully reproducible, matching EI/UCB/PI.

7. Added a **[Diagnostic] Flag for when multiple points share the exact global max value within the dataset** (as it was the case for Function 5, for which the maximum was most likely already identified based on repetitive past query predictions saved to the dataset), since that trivially inflates how "discriminating" regret-based ranking appears regardless of actual strategy quality, and therefore some caution is required when interpreting results for such functions.

8. Kept **Dynamic Sobol Sampling Resolution Scaled to Input Dimensionality** for continuous-domain next-query candidate generation, with the _Sobol seed tied to the current dataset size_ (rather than a fixed seed).
   
9. Kept **HEBO-style Output Warping** unchanged, including the Function 1-specific log10 pre-transform with data-driven clipping floor and its reversal on unwarping [preserved from Week 9].

10. Kept the (currently disabled, min_distance_to_existing=0.0) _Near-Duplicate Exclusion Filter_ for next-query candidate generation [preserved unused from Week 9]. This is maintained as it may be useful in other pipelines.

**<ins>Note 1:</ins>** As with Week 9's BBO Pipeline (and in general, as it is always the case with Bayesian Optimisation), the resulting next-query predictions remain exploratory estimates, not guarantees of beating the current known maximum for each function. The CI/SEM reporting added this week is meant to make explicit how much uncertainty still surrounds the "winning" kernel x acquisition combo per function, rather than presenting a single point-estimate ranking as more settled than it is.

**<ins>Note 2:</ins>** The BBO Week 10 Full ML Bayesian Optimisation Pipeline is **computationally heavy**. _Runtime to completion_ is expected to be around _~2h if 14-16 CPUs are available_ (as used here), but it may take slightly/significantly longer if not.

**Technical Modification for Running Script:** Switched execution logging to stream all prints to a log file (execution_output.log) instead of the browser console, after prior runs crashed the browser tab and 2+ hours of progress were lost in pre-production before this change was implemented.
