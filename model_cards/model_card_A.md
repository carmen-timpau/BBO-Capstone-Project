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


<ins> **Model Characteristics:** </ins>

This Bayesian Optimisation ML model makes use of Gaussian Processes (GPs) to perform surrogate modelling of each of the 8 black-box functions investigated in this capstone project, and uses acquisition functions (UCB, EI, PI) to predict the next-query point to be submitted for the expensive execution of the real functions between Weeks 1-5. **Sobol Sampling** is used for continuous-domain next-query candidate generation.

The GP kernel, acquisition function and their corresponding hyperparameters to be used for predicting the next query point for each black-box function are selected manually following an iterative (over the initial 5-week phase of the capstone project), data-driven strategy, meant to freely explore each functions’ behaviour under various Bayesian Optimisation hyperparameter settings. These are shown in **Table 1** below:

<p align="center"> <strong>Table 1.</strong> BO ML Model A Versions' Locations and Specific Hyperparameter Settings Used </p>

<div align="center">
  
|<p align="center"> BO ML Model Version </p>   | <p align="center"> Week Deployed  </p>  |  <p align="center"> Location </p> |  <p align="center"> Per-Function Hyperparameter Configurations </p> | 
|----------------------------------------|-----------------------------------------|-----------------------------------------------------|-----------------------------------|
| <p align="center"> **A.1.** </p>       |  <p align="center">   Week 1 </p>       |  <p align="center">   [`week_01/main.py`](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_01/main.py)    </p>            |  <p align="center"> [`week_01/config.py`](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_01/config.py)  </p>        |
| <p align="center"> **A.2.** </p>       |  <p align="center">   Week 2 </p>       |  <p align="center">   [`week_02/main.py`](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_02/main.py)    </p>            |  <p align="center"> [`week_02/config.py`](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_02/config.py)  </p>        |
| <p align="center"> **A.3.** </p>       |  <p align="center">   Week 3 </p>       |  <p align="center">   [`week_03/main.py`](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_03/main.py)    </p>            |  <p align="center"> [`week_03/config.py`](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_03/config.py)  </p>        |
| <p align="center"> **A.4.** </p>       |  <p align="center">   Week 4 </p>       |  <p align="center">   [`week_04/main.py`](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_04/main.py)    </p>            |  <p align="center"> [`week_04/config.py`](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_04/config.py)  </p>        |
| <p align="center"> **A.5.** </p>       |  <p align="center">   Week 5 </p>       |  <p align="center">   [`week_05/main.py`](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_05/main.py)    </p>            |  <p align="center"> [`week_05/config.py`](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/week_05/config.py)  </p>        |

</div>

<br> 
<br> 


<ins>**Performance Results:** </ins> 

This ML model only outputs, for each function, the predicted next-query point input coordinates. Considering that the BO hyperparameters are already defined within each version A.1-A.5 for each black-box function (and therefore they are clearly known), this ML model is, through its simplicity, highly transparent. It lacks reproducibility, however, which is a limitation discussed further in the corresponding section below.

This BO ML model deployed in Weeks 1-5 of the BBO capstone project, by employing versions A.1 through to A.5, managed to further maximise different black-box functions, based on the version used at each point in time, as detailed below in **Table 2**. 

<p align="center"> <strong>Table 2.</strong> Performance of ML Model A Versions A.1. - A.5., Based on the Number of Functions Maximised Each Week </p>

<div align="center">
  
|<p align="center"> BO ML Model Version </p>   | <p align="center"> Week Deployed  </p>  | <p align="center"> Functions Further Maximised </p> |  <p align="center"> # of Functions Further Maximised </p>|
|----------------------------------------|-----------------------------------------|-----------------------------------------------------|-----------------------------------|
| <p align="center"> **A.1.** </p>           |  <p align="center">   Week 1 </p>       |  <p align="center">   Function 8    </p>            |  <p align="center"> 1 </p>        |
| <p align="center"> **A.2.** </p>           |  <p align="center">   Week 2 </p>       |  <p align="center">  Functions 4, 8 </p>            |  <p align="center"> 2 </p>        |
| <p align="center"> **A.3.** </p>           |  <p align="center">   Week 3 </p>       |  <p align="center">   - </p>                        |  <p align="center"> 0 </p>        |
| <p align="center"> **A.4.** </p>           |  <p align="center">   Week 4 </p>       |  <p align="center">   Functions 6, 7 </p>           |  <p align="center"> 2 </p>        |
| <p align="center"> **A.5**. </p>           |  <p align="center">   Week 5 </p>       |  <p align="center">   Functions 2, 4, 5, 6, 7 </p>  |  <p align="center"> 5 </p>        |

</div>

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

<ins> **Limitations, Biases & Potential Failure Modes:** </ins>

The main limitations of this BO ML model (and its component versions, A.1-A.5) are:

**(1)** the Sobol candidate generation across the high-dimensional input space was restricted by the per-dimension minimum and maximum values observed in the initial dataset for each black-box function, meaning that the search was only conducted within the bounding box defined by the initial datapoints for each black-box function; and 

**(2)** the lack of reproducibility, due to uncontrolled stochastic behaviour. Running this BO ML model’s pipeline will output different next-query predictions on every execution.

The first limitation (1) contributes to a real bias in the possible optimisation results obtained, as potential function maximisation results will always be bounded to the high-dimensional space restricted by the given initial dataset for each function. A potential failure mode of this BO ML pipeline resulting directly from limitation (1) is when applied to black-box functions which do not contain any further maxima within the area restricted by their input datasets' coordinates, other than the ones given in their initial datasets, in which case the model will perpetually fail to predict a higher-outputting input query point for those functions. 

The second limitation (2) makes the verification of the pipeline’s outputs impossible, since identical runs do not produce identical results. The predictions generated by previous users cannot be reproduced and validated, directly and significantly reducing the model’s trustworthiness, as well as the validity of the results themselves.

Because of these limitations, and despite the assumption made (stated above), the resulting next-query predictions remain exploratory estimates, not guarantees of beating the current known maximum for each function. 

These limitations, while very real and likely to have prevented the pipeline to perform at its absolute best performance, have not prevented the BO ML model to further maximise the outputs of black-box functions over the course of the first 5 weeks of the capstone project and achieve significant exploratory progress.

<br> 
<br> 


<ins> **Ethical Considerations:** </ins>

This BO ML pipeline lacks reproducibility in its generated next-query predictions, as no random_state variables were specified for any pseudo-random number generation instances, in any of the deployed versions (A.1-A.5), leaving all stochastic components uncontrolled. As noted in the section addressing the limitations of this model above, this aspect significantly impacts the model’s trustworthiness and reproducibility, key ethical considerations that have been fully addressed in subsequent BO ML models developed as part of this project (Model Cards B-H).

Due to its uncontrolled stochastic behaviour - which reduces the trustworthiness and reproducibility of this ML model - and the absence of built-in statistically reliable hyperparameter optimisation methods - which can lead to suboptimal performance and an inefficient use of the limited evaluation budget typical of BO settings), this BO ML model is not recommended for real-world Bayesian Optimisation problems. However, more advanced BO ML models developed later in this capstone project (Model Cards E, F, G, H), completely address these issues and are fully reproducible, statistically reliable and much more helpful, suitable and effective for such applications.

This ML model does not make use of or produce any sensitive or personal information.

