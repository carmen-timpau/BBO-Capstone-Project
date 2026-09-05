**BBO Week 9 - Bayesian Optimisation Strategy Summary**

1. Replaced the separate Week 8 Kernel Ablation Study and Acquisition Function Ablation Study with a **single Full Joint Kernel × Acquisition Rollout Ablation Study** [1], sweeping all 8 kernel variants against all 10<sup>*</sup> acquisition strategies (plus an added **Random Baseline**) — 88 combinations tested jointly, per function — via **Robust Multi-Step Sequential Offline Bayesian Optimization Rollout**. This replaced the Week 8 approach of selecting the kernel first (via LOOCV R²) and only ablating acquisition functions afterwards, using the 'winning' kernel, since _kernel and acquisition choices interact, and a kernel selected purely for regression fit quality is not guaranteed to pair best with the eventual acquisition strategy_, leading to less-than-optimal-quality query predictions.[1]

2. Used **Mean Final Simple Regret** as the _primary ranking metric_ (directly reflecting the global maximization goal, reported alongside "Mean Best Value Found" for interpretability), with **Area Under the Regret Curve (AURC)** as a _secondary tiebreaker capturing convergence speed_. A **Random Baseline** (uniform random candidate selection) was added to every function's ablation, to confirm whether the tested acquisition strategies meaningfully outperform blind search rather than assuming it, as it was done before.

3. Introduced a **Holdout Fraction (30%) Cap on Rollout Iterations**, preventing the rollout from exhausting the finite candidate pool. Without this, every strategy (including random) is eventually forced to visit every remaining point, collapsing all combos to an artificial 0.0 final regret and making the ranking metric uninformative — this was identified and corrected after observing it directly in Function 1 and Function 2's initial results.

4. **Dropped** _Surrogate Model Architecture Comparison (GP vs. Deep Ensemble)_ **entirely**. Given the _small sample sizes across all 8 functions_ (18-48 points), a 5-member MLP ensemble with (32,16) hidden layers is actually heavily _overparameterized_ relative to available data, and any LOOCV RMSE "win" over GP is more plausibly noise than a genuine surrogate quality advantage. **GP is now used unconditionally as the surrogate model for all functions**, removing this risk along with the associated compute and complexity.

5. Retained **Dynamic Sobol Sampling Resolution Scaled to Input Dimensionality** for continuous-domain next-query candidate generation, but **tied the Sobol seed to the current dataset size (rather than a fixed seed)** so the candidate grid shifts automatically as new observations are added, rather than regenerating an identical grid every run, which would predict previous, already processed, queries for some functions (not desired, as querying the functions twice on the same input would waste expensive resources).

6. [!This feature is part of the Week 9 BO pipeline, but not used this week, as not required this time i.e. min_distance_to_existing = 0.0 was used to disable this. However, this feature was left and may be used if needed in future runs of this algorithm] Introduced a **Near-Duplicate Exclusion Filter** on next-query candidates, removing any Sobol candidate within a minimum distance (in standardised input space) of an already-evaluated point before acquisition scoring. This was added after observing that the pipeline could repeatedly re-suggest an already-measured point — the GP interpolates near-exactly through its own training data, so a high-value existing point could dominate the acquisition score indefinitely and provide zero new information if re-queried.

7. Retained **HEBO-inspired Non-linear Output Warping** unchanged from Week 8, including the Function 1-specific log10 pre-transform with data-driven clipping floor, and the corresponding reversal during output unwarping.

<ins>**Note**</ins>: The addition of a Random Baseline and the holdout-fraction were both introduced reactively, after inspecting intermediate results (plots, tied final-regret values, pool-exhaustion artefacts) in surfaced cases. 

This joint ranking ML pipeline is intended to be more defensible for informing next-query predictions, although the final query predictions still remain (as is always the case for Bayesian Optimisation) estimates at deliberately exploratory points, _not guarantees of exceeding the current known maximum_ — the progress will continue to be monitored and documented as queries are evaluated in subsequent weeks and as new data-informed pipeline changes are being made.

<sup>*</sup>In Week 9, an enriched list of acquisition functions (10) was used for ablation robustness, compared to Week 8 when only 6 were used.

References:

1. F. Zhang and Y. Chen. “Direct Regret Optimization in Bayesian Optimization.” arXiv:2507.06529, 2025.
