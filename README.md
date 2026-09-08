 **Black-Box Optimisation (BBO) Capstone Project - Bayesian Optimisation**

<br>

📝 <ins> **Project Description:** </ins> 

Given an initial dataset of true datapoints describing 8 different, unrelated and unknown Black-Box functions of varying dimensionality (2D-8D), each modelling  real-world processes within various application industries, this project aims to apply and refine Bayesian Optimisation to identify the global maximum or maxima for each function.

Every week, over a period of 13 weeks, each function can only be queried once. Each full set of inputs (1 per function) are processed that same week and the outputs received help inform the coordinates of the next set of queries to be submitted for processing in the upcoming week, therefore leading to a refinement of the optimisation strategy for each of the 8 functions in a data-driven and personalised approach.

<br>
<br>

📒 <ins>**Black-Box Function Datasets:**</ins>

The [`BBO-Capstone-Project/data/`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/data) directory contains:

•	A [`baseline_data/`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/data/baseline_data) subfolder containing the initial input-output datasets provided in original format by Imperial College London for each of the 8 Black-Box functions, along with a `stats.md` file which details a short initial statistical analysis for these. These have been embedded into a single dictionary for ease of use within this project saved as a .pkl file titled `wk1_input_data.pkl` and saved within the directory detailed below, following the described structure.

•	A [`weekly_processed/`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/data/weekly_processed) subfolder that stores the complete week‑by‑week evolution of each dataset as .pkl snapshots, from start (initial datasets) to finish (final datasets). Each .pkl file is structured as a top‑level dictionary with keys “function_1” through to “function_8”, where each entry contains a nested dictionary consisting of an “x” array of sampled inputs and a “y” array of corresponding function evaluations.

•	A [`final_data/`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/data/final_data) subfolder containing the final data obtained after the completion of the 13-week capstone project as a .pkl file, a `stats.md` file with a short statistical analysis for each functions’ final dataset and a `functions_maxima_outcomes.md` file reporting the maximum output points identified for each Black-Box function as a result of the full work conducted for the BBO capstone project.


📥 **[Datasets](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/data/weekly_processed)**

📄 **[Datasheets for Datasets](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/data/weekly_processed/datasheets_info.md)**

<br>
<br>

<ins>⚙️**Bayesian Optimisation (BO) ML Pipelines**</ins>:

The frameworks transition the approach from manual, data-driven and intuitive strategy tuning to fully automated, robust and optimised machine learning workflows. By leveraging state-of-the-art practices, like HEBO, the project delivers fast, reliable, and high-quality Bayesian Optimisation results to tackle expensive, opaque Black-Box process optimisation across various industries within as few queries as possible.

🔍 **[Literature-Supported Bayesian Optimisation ML Pipeline Design Choices](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/DESIGN_NOTES.md)**

Functional research code is logged in [`experiments/`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments), which is itself organised in separate directories for each week, documenting the evolution of the Bayesian Optimisation ML pipelines over time.

For optimal navigability, _every week’s Bayesian Optimisation ML pipeline developed_ has been structured in packages (folders containing a blank `__init__.py` file, along with corresponding `.py` modules) and/or independent modules (`.py` files), as well as a master standalone `main.py` file, which calls all relevant modules from their corresponding locations in order to execute the respective full Bayesian Optimisation ML pipeline start-to-finish. This helps ensure an easier understanding of the flow and logic of each developed BO ML pipeline, while providing a clear and organised structure and allowing anyone to directly inspect integral modules/packages for further details on individual key coding blocks and their objectives.

🔩 **[Bayesian Optimisation ML Pipelines](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments)**

📄 **[Model Cards for Bayesian Optimisation ML Pipelines](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/model_cards/model_cards_info.md)**

The direct outputs of each weekly Bayesian Optimisation ML pipeline are all logged in the `diagnostics_results` subfolder within each corresponding week's folder. 

A comprehensive technical overview of the weekly BO ML pipeline results, documenting the development and progression of their diagnostic and predictive complexity, robustness and performance can be found linked below. 

📄 **[Technical Report for the 13-Week Black-Box Optimisation Challenge](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/TECHNICAL_REPORT.md)**

<br>
<br>

📁 <ins> **Discussion of Weekly Query Results & Data-Informed Strategy Summary:** </ins> 

All weekly Bayesian Optimisation ML strategies deployed have been informed by previous-week query output results.

A dicussion of previous-week query output results and current week strategy summaries can be found in `strategy_discussion.md` and `strategy_summary.md` files within each week's directory.

<br>
<br>

<ins>📈 **Bayesian Optimisation Outcomes:** </ins>

During the 13-week Black-Box Optimisation Challenge, all 8 unknown objective functions have been maximised beyond their initial maxima within the initial given datasets. A comparative summary of the initial functions' maxima and obtained post-BBO results is shown in **Table 1.** below, which also highlights the exact Bayesian Optimisation ML pipeline which yielded the optimised maximum for each function (in the _'Week Optimised'_ column).

<br>

<p align="center">
<strong>Table 1. Summary of the Results</strong> Achieved for all 8 Black-Box Functions after the 13-week Bayesian Optimisation Challenge
</p>

| Function | Input | Output | # of Initial <br> Datapoints | # of Final <br> Datapoints | Initial <br> Maximum | Final <br> Maximum | Week <br> Optimised | Process / Industry |
|----------|----------------------|-----------------------|-------------------------|-----------------------|-----------------------|-----------------------|-----------------------| -----------------------| 
| <div align="center">**1**</div> | <div align="center">2D</div> | <div align="center">1D</div> | <div align="center">10</div> | <div align="center">23</div> | <div align="center">7.711e-16</div> | <div align="center">**1.796e-10**</div> |  <div align="center">**10**</div> | <div align="center">Radiation Detection</div> |
| <div align="center">**2**</div> | <div align="center">2D</div> | <div align="center">1D</div> | <div align="center">10</div> | <div align="center">23</div> | <div align="center">0.611</div> | <div align="center">**0.756**</div> | <div align="center">**6**</div> | <div align="center">Noisy Log-Likelihood <br> Optimisation</div> |
| <div align="center">**3**</div> | <div align="center">3D</div> | <div align="center">1D</div> | <div align="center">15</div> | <div align="center">28</div> | <div align="center">-0.035</div> | <div align="center">-**0.019**</div> | <div align="center">**11**</div> | <div align="center">Pharmaceutical <br> Drug Formulation</div> |
| <div align="center">**4**</div> | <div align="center">4D</div> | <div align="center">1D</div> | <div align="center">30</div> | <div align="center">43</div> | <div align="center">-4.026</div> | <div align="center">**0.570**</div> | <div align="center">**10**</div> | <div align="center">Warehouse Optimisation</div> |
| <div align="center">**5**</div> | <div align="center">4D</div> | <div align="center">1D</div> | <div align="center">20</div> | <div align="center">33</div> | <div align="center">1088.860</div> | <div align="center">**2333.007**</div> | <div align="center">**6**</div> | <div align="center">Chemical Process <br> Engineering</div> |
| <div align="center">**6**</div> | <div align="center">5D</div> | <div align="center">1D</div> | <div align="center">20</div> | <div align="center">33</div> | <div align="center">-0.714</div> | <div align="center">-**0.172**</div> | <div align="center">**12**</div> | <div align="center">Product Formulation</div> |
| <div align="center">**7**</div> | <div align="center">6D</div> | <div align="center">1D</div> | <div align="center">30</div> | <div align="center">43</div> | <div align="center">1.365</div> | <div align="center">**3.224**</div> | <div align="center">**13**</div> | <div align="center">Machine Learning Model <br> Hyperparameter Tuning</div> |
| <div align="center">**8**</div> | <div align="center">8D</div> | <div align="center">1D</div> | <div align="center">40</div> | <div align="center">53</div> | <div align="center">9.598</div> | <div align="center">**9.956**</div> | <div align="center">**2**</div> | <div align="center">Machine Learning Model <br> Hyperparameter Tuning</div> |


<br>
<br>

<p align="center">
<img width="6563" height="2956" alt="image" src="https://github.com/user-attachments/assets/dc28b713-a3ba-4eb4-ae7c-585e90bf15cf" />
</p>

<p align="center">
<strong>Figure 1. Bayesian Optimisation Outcomes Landscape</strong> - Progress over 13-Week Optimisation Period for each Black-Box Function
</p>

<br>
<br>

💻 <ins> **Coding Libraries & Packages:** </ins>

1. <ins> **`scikit-learn`**</ins> - central to all ML frameworks developed in the BBO project:

•	`sklearn.gaussian_process.GaussianProcessRegressor` - the core surrogate model

•	`sklearn.gaussian_process.kernels` - `Matern`, `RBF``, RationalQuadratic`, `WhiteKernel` (used for kernel ablation)

•	`sklearn.preprocessing` - StandardScaler (feature scaling) and PowerTransformer (Box-Cox/Yeo-Johnson output warping in HEBOStyleWarper)

•	`sklearn.cluster.KMeans` - K-means clustering for targeted, local-box sampling

•	`sklearn.decomposition.PCA` - dimensionality reduction for cluster visualization

•	`sklearn.exceptions.ConvergenceWarning` – warning suppression during GP fitting

2. <ins>	**`NumPy`**</ins> – linear algebra, array operations, log/exponential transforms (for Function 1's log10 pre-transform), random number generation (`np.random.default_rng`), statistical aggregation (mean, std, median across seeds).

3.	<ins> **`SciPy`**:</ins>

•	`scipy.stats.norm` - Gaussian CDF/PDF for EI/PI acquisition function calculations

•	`scipy.stats.t` -  t-distribution for computing 95% confidence intervals (via `t.ppf`) for mean final regret, mean AURC

•	`scipy.stats.qmc.Sobol` - low-discrepancy Sobol sequence generation for quasi-random candidate pools (both the full-domain pool and the density-enhanced local-box pool)

•	`scipy.spatial.distance.cdist` - pairwise distance computation (used in the `min_distance_to_existing` duplicate exclusion filter - disabled feature) 

4.	 <ins>**`pandas`**</ins> - building/sorting ablation results tables (`combo_df`, `all_functions_full_tables`);

5.	<ins> **`pickle`** </ins> - checkpointing results at various key pipeline stages (ablation summaries, k-means results, next-query predictions, importing input datasets for each new week’s pipeline);

6.	 <ins>**`Matplotlib`** </ins> (`matplotlib.pyplot`, `matplotlib.patches`), used for all plots: elbow curves, PCA scree plots, cluster scatter grids (including 3D plots via `projection='3d'` subplot mode), and convergence trajectories;

7.	 <ins>**`joblib`** </ins> (`Parallel`, `delayed`) – seed parallelization across multiple (all available, `n_jobs=-1`) CPU cores in `run_full_joint_ablation` sweep

8.	 <ins>**`os`**</ins> - directory creation for output paths

9.	<ins> **`sys`**</ins> - stdout redirection to log files

10. <ins> **`warnings`**</ins> - suppressing convergence/variance warnings during fitting (after ensuring healthy behaviour)

<br>
<br>

⚖️ **LICENSE:** **[MIT License](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/LICENSE)**

<br>
<br>

📖 <ins> **Foundational References:** </ins> 

1. C. E. Rasmussen and C. K. I. Williams. “Gaussian Processes for Machine Learning.” _MIT Press_, 2005. https://doi.org/10.7551/mitpress/3206.001.0001

2. I. Roman, R. Santana, A. Mendiburu, and J. A. Lozano. “An Experimental Study in Adaptive Kernel Selection for Bayesian Optimization.” _IEEE Access_, 7:184294–184302, 2019. https://doi.org/10.1109/ACCESS.2019.2960498
   
3. M. Hoffman, E. Brochu, and N. de Freitas. “Portfolio Allocation for Bayesian Optimization.” Proceedings of the 27th Conference on Uncertainty in Artificial Intelligence (UAI), pp. 327–336, arXiv:1009.5419, 2011.

4. T. S. Breusch and A. R. Pagan. “A Simple Test for Heteroscedasticity and Random Coefficient Variation.” _Econometrica_, 47(5):1287–1294, 1979. https://doi.org/10.2307/1911963

5. A. I. Cowen‑Rivers, W. Lyu, R. Tutunov, Z. Wang, A. Grosnit, R. R. Griffiths, A. M. Maraval, H. Jianye, J. Wang, J. Peters, and H. Bou Ammar. “HEBO: Pushing the Limits of Sample‑Efficient Hyperparameter Optimisation.” arXiv:2012.03826, 2022. 

6. J.-H. Park, M. Cheon, and D.-Y. Koh. “BOOST: Bayesian Optimization with Optimal Kernel and Acquisition Function Selection Technique.” arXiv:2508.02332, 2025.
   
7. J.-H. Park, M. Cheon, J. Wi, and D.-Y. Koh. “BOOST: A Data-Driven Framework for the Automated Joint Selection of Kernel and Acquisition Functions in Bayesian Optimization.” arXiv:2508.02332, 2026.

8. F. Zhang and Y. Chen. “Direct Regret Optimization in Bayesian Optimization.” arXiv:2507.06529, 2025. 

---------------------------------------------------------------------------------------------------------------------

<br>

🛠️ <ins> **Project Development Details:** </ins> 

The project was developed as part of the 6-month _Professional Certificate in Machine Learning & Artificial Intelligence_ joint programme at Imperial College London.

<br>

✉️ <ins> **Project Developer Contact:** </ins> 

Carmen-Mihaela Timpau, carmen.timpau21@alumni.imperial.ac.uk, Imperial College London, United Kingdom.

_Please feel free to reach out with any questions, feedback, or ideas for discussion._
