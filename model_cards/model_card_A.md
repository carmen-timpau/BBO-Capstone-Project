**Model Card A**

<br>
<br>

**Model Title:** BBO Initial Phase (Weeks 1-5) Full Bayesian Optimisation ML Pipeline

**Week(s) of Deployment in BBO Capstone Project:** Weeks 1-5

**Model Versions & Locations:** 

- **Version A.1.:** [`experiments/week_01`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments/week_01)
- **Version A.2.:** [`experiments/week_02`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments/week_02)
- **Version A.3.:** [`experiments/week_03`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments/week_03)
- **Version A.4.:** [`experiments/week_04`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments/week_04)
- **Version A.5.:** [`experiments/week_05`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments/week_05)

**Model Description:** Manual, Iterative and Data-Driven Gaussian Process (GP) Kernel and Acquisition Function Hyperparameter Tuning-Informed Bayesian Optimisation

<br>
<br>

<ins> **Intended Use:** </ins>

This Bayesian Optimisation overall ML model design and its individual (weekly-specific) versions A.1-A.5 were developed and are intended for use as part of the Black-Box Optimisation (BBO) Challenge, during Weeks 1-5 of 13, for weekly next-query prediction generation for each of the 8 given black-box functions. 

Use cases to be avoided include the optimisation of unknown, black-box functions which do not form part of this specific capstone project. In those cases, slight modifications are required to ensure that the number of functions investigated is appropriately matched within loops and any required function-specific pre-processing is added to the pipeline to satisfy all of the new function(s)’ specific requirements.

<br>
<br>

<br> 
<br> 

<ins> **Assumptions:** </ins>

The main assumption that underlies this BO ML model is: 

**(1)** that the hyperparameters of the GP kernels and acquisition functions employed for each function within each consecutive version (A.1-A.5) of this manually-tuned BO ML pipeline reflect incremental data-driven improvements for each function that aim to increase the quality of the next query predictions over time (Weeks 1-5 of the capstone project). 

The above is considered an assumption, because it cannot be guaranteed that the week-by-week incremental BO ML model version (function-specific) tuning automatically leads to improvements, but they are intended to, based on previously obtained results, thus being a data-driven, manually tuned pipeline.
In retrospect, considering the limited and expensive budget available for this project, this initial phase (Week 1-5) could have been shortened, to allow for a richer implementation of automated, offline testing and statistically-reliable ML models to be developed later on.
Nonetheless, this model and its component versions (A.1-A.5) represent the initial phase of the capstone project which helped explore, reveal and document the black-box functions’ behaviour in response to different kernel and acqusition function hyperparameter settings. 

<br> 
<br> 


<ins> **Ethical Considerations:** </ins>

This ML model does not make use of or produce any sensitive or personal information.
