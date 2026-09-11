<br>
 <p align="center"> <strong> 13-Week Black-Box Optimisation (BBO) Capstone Project</strong>  (June - August 2026)</p> 
  <p align="center"> <em> Iterative, Data-Driven Bayesian Optimisation Machine Learning Pipeline Development</em> </p> 

<br>
<br>

📝 <ins> **Project Description:** </ins> 

Given an initial dataset of true datapoints describing 8 different, unrelated and unknown Black-Box functions of varying dimensionality (2D-8D), each modelling  real-world processes within various application industries, this project aims to apply and refine Bayesian Optimisation to iteratively maximise each function over a period of 13 weeks of informed ML pipeline design and development.

Each of the 8 Black-Box functions were characterised only by an initial small-sized set of individual datapoints (between 10-40) provided by Imperial College London at the beginning of the challenge and the functions' internal processes are completely unknown. 

Every week, over a period of 13 weeks (strict, limited budget), each function can only be queried once (as the functions are expensive-to-query). Each full set of input queries predicted (1 per function) are processed that same week and the outputs received are used to help inform the coordinates of the next set of queries to be submitted for processing in the upcoming week, therefore leading to an iterative process and this consequently enables a natural refinement of the optimisation strategy for each of the 8 unknown functions in a data-driven and function-personalised approach.

<br>
<br>

📒 <ins>**Black-Box Function Datasets:**</ins>

The [`BBO-Capstone-Project/data/`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/data) directory contains:

•	A [`baseline_data/`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/data/baseline_data) subfolder containing the initial input-output datasets provided in original format by Imperial College London for each of the 8 Black-Box functions, along with a `stats.md` file which details a short initial statistical analysis for these. All initial black-box function data provided has been consolidated into a single dictionary saved as a .pkl file for ease of use within this project, titled `wk1_input_data.pkl` and structured as described in its related datasheet (see _Datasheets for Datasets_ below).

•	A [`weekly_processed/`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/data/weekly_processed) subfolder that stores the complete week‑by‑week evolution of each dataset as .pkl snapshots, from start (initial datasets) to finish (final datasets). Each .pkl file is structured as a top‑level dictionary with keys “function_1” through to “function_8”, where each entry contains a nested dictionary consisting of an “x” array of sampled inputs and a “y” array of corresponding function evaluations.

•	A [`final_data/`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/data/final_data) subfolder containing the final data obtained after the completion of the 13-week capstone project as a .pkl file, a `stats.md` file with a short statistical analysis for each functions’ final dataset and a `functions_maxima_outcomes.md` file reporting the maximum output points identified for each Black-Box function as a result of the full work conducted for the BBO capstone project.


📥 **[Datasets](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/data/weekly_processed)**

📄 **[Datasheets for Datasets](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/data/weekly_processed/datasheets_info.md)**

<br>
<br>

<ins>⚙️**Bayesian Optimisation ML Pipelines**</ins>:

The weekly Bayesian Optimisation (BO) machine learning (ML) frameworks logged in corresponding `week_XX/` directories transition the approach from manual, data-driven and intuitive strategy tuning focused on individual black-box function behavioural exploration to fully reproducible, automated, statistically reliable, robust and optimised BO ML workflows. The project develops end-to-end production-ready Bayesian Optimisation ML pipelines that support the iterative, data-driven optimisation of expensive and opaque (Black-Box) processes across various industries (see **Table 1** below), by leveraging small-datasets, offline testing and state-of-the-art BO practices, like Gaussian Process (GP) methodology [1], acquisition functions (UCB, EI, PI) [3] and HEBO output warping [5,6], while balancing exploration with exploitation strategically under limited budgets.

🔍 **[Literature-Supported Bayesian Optimisation ML Pipeline Design Choices](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/DESIGN_NOTES.md)**

The [`BBO-Capstone-Project/experiments/`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments) folder is itself organised in separate directories for each week `BBO-Capstone-Project/experiments/week_XX/`, documenting the self‑contained implementation and evolution of each week’s Bayesian Optimisation ML pipeline used to generate the next query predictions over 13 weeks.

For optimal navigability, _every week’s Bayesian Optimisation ML pipeline developed_ has been structured in packages (folders containing a blank `__init__.py` file, along with corresponding `.py` modules) and/or independent modules (`.py` files), as well as a master standalone `main.py` file, which calls all relevant modules from their corresponding locations in order to execute the respective full Bayesian Optimisation ML pipeline start-to-finish. This helps ensure an easier understanding of the flow and logic of each developed BO ML pipeline, while providing a clear and organised structure and allowing anyone to directly inspect integral modules/packages for further details on individual key coding blocks and their objectives.

🔩 **[Bayesian Optimisation ML Pipelines](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments)**

📄 **[Model Cards for Bayesian Optimisation ML Pipelines](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/model_cards/model_cards_info.md)**

The direct outputs of each weekly Bayesian Optimisation ML pipeline are all logged in the `diagnostics_results` subfolder within each corresponding week's folder for Weeks 6-13. For Weeks 1-5, the sole output of the pipeline was the next query prediction generated for each black-box function, which have been saved in the `queries/input_queries.md` file within each week's folder, as also described right below.

The `queries/` subfolder within in each week’s folder keeps track of the input query points generated and submitted for every unknown function each week - stored in `input_queries.md` - along with the corresponding obtained outputs - stored in `query_outputs.md`. `stats.md` details the statistical analysis of the full incumbent dataset for each function _after_ the addition of the new query point of that respective week. 

<br>
<br>

📁 <ins> **Discussion of Weekly Query Results & Data-Informed Strategy Summary:** </ins> 

All weekly Bayesian Optimisation ML strategies deployed have been informed by previous-week query output results.

A dicussion of previous-week query output results and current week strategy summaries can be found in `strategy_discussion.md` and `strategy_summary.md` files within each week's directory.

<br>
<br>

<ins>📈 **Bayesian Optimisation Outcomes:** </ins>

During the 13-week Black-Box Optimisation Challenge, all 8 unknown objective functions have been maximised beyond their initial maxima within the initial given datasets. 

A comparative summary of the initial functions' maxima and [obtained post-BBO results](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/experiments/bayesopt_outcomes/bayesopt_functions_maxima.md) is shown in **Table 1.** below, which also highlights the exact Bayesian Optimisation ML pipeline which yielded the optimised maximum for each function (_'Week Optimised'_ column).

<br>

<p align="center">
<strong>Table 1. Summary of the Results</strong> Achieved for all 8 Black-Box Functions after the 13-week Bayesian Optimisation Challenge
</p>

| Function | Input | Output | Goal | # of Initial <br> Datapoints | # of Final <br> Datapoints | Initial <br> Maximum | Final <br> Maximum | Week <br> Optimised | Process / Industry |
|----------|----------------------|-----------------------|-------------------------|-----------------------|-----------------------|-----------------------|-----------------------| -----------------------| -----------------------| 
| <div align="center">**1**</div> | <div align="center">2D</div> | <div align="center">1D</div> | Maximise | <div align="center">10</div> | <div align="center">23</div> | <div align="center">`7.711` <br> `e-16`</div> | <div align="center">**`1.796` <br> `e-10`**</div> |  <div align="center">**10**</div> | <div align="center">Contamination Detection</div> |
| <div align="center">**2**</div> | <div align="center">2D</div> | <div align="center">1D</div> |  Maximise | <div align="center">10</div> | <div align="center">23</div> | <div align="center">`0.611`</div> | <div align="center">**`0.756`**</div> | <div align="center">**6**</div> | <div align="center">Noisy Log-Likelihood <br> Optimisation</div> |
| <div align="center">**3**</div> | <div align="center">3D</div> | <div align="center">1D</div> |  Maximise | <div align="center">15</div> | <div align="center">28</div> | <div align="center">`-0.035`</div> | <div align="center">-**`0.019`**</div> | <div align="center">**11**</div> | <div align="center">Pharmaceutical <br> Drug Formulation</div> |
| <div align="center">**4**</div> | <div align="center">4D</div> | <div align="center">1D</div> |  Maximise | <div align="center">30</div> | <div align="center">43</div> | <div align="center">`-4.026`</div> | <div align="center">**`0.570`**</div> | <div align="center">**10**</div> | <div align="center">Warehouse Optimisation</div> |
| <div align="center">**5**</div> | <div align="center">4D</div> | <div align="center">1D</div> |  Maximise | <div align="center">20</div> | <div align="center">33</div> | <div align="center">`1088.860`</div> | <div align="center">**`2333.007`**</div> | <div align="center">**6**</div> | <div align="center">Chemical Process <br> Engineering</div> |
| <div align="center">**6**</div> | <div align="center">5D</div> | <div align="center">1D</div> |  Maximise | <div align="center">20</div> | <div align="center">33</div> | <div align="center">`-0.714`</div> | <div align="center">-**`0.172`**</div> | <div align="center">**12**</div> | <div align="center">Product Formulation</div> |
| <div align="center">**7**</div> | <div align="center">6D</div> | <div align="center">1D</div> |  Maximise | <div align="center">30</div> | <div align="center">43</div> | <div align="center">`1.365`</div> | <div align="center">**`3.224`**</div> | <div align="center">**13**</div> | <div align="center">Machine Learning Model <br> Hyperparameter Tuning</div> |
| <div align="center">**8**</div> | <div align="center">8D</div> | <div align="center">1D</div> |  Maximise | <div align="center">40</div> | <div align="center">53</div> | <div align="center">`9.598`</div> | <div align="center">**`9.956`**</div> | <div align="center">**2**</div> | <div align="center">Machine Learning Model <br> Hyperparameter Tuning</div> |

<br>

The landscape overview of the weekly progress achieved for each black-box function during the 13-week project, following an iterative and data-driven Bayesian Optimisation ML pipeline development process is shown below (**Figure 1**). The corresponding code used to compute this final analysis is logged in [`experiments/bayesopt_outcomes`](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments/bayesopt_outcomes).

<br>

<p align="center">
<img width="6563" height="2956" alt="image" src="https://github.com/user-attachments/assets/dc28b713-a3ba-4eb4-ae7c-585e90bf15cf" />
</p>

<p align="center">
<strong>Figure 1. Bayesian Optimisation Outcomes Landscape</strong> <br>
Progress over 13-Week Optimisation Period for each Black-Box Function
</p>

<br>
<br>

💻 <ins> **Coding Libraries & Packages:** </ins>

1. <ins> **`scikit-learn`**</ins> - central to all ML frameworks developed in the BBO project:

      • `sklearn.gaussian_process.GaussianProcessRegressor` - the core surrogate model used in the project

      • `sklearn.gaussian_process.kernels` - `Matern`, `RBF`, RationalQuadratic`, `WhiteKernel` (used for kernel ablation)

      • `sklearn.preprocessing` - StandardScaler (feature scaling) and PowerTransformer (Box-Cox/Yeo-Johnson output warping in HEBOStyleWarper)

      • `sklearn.cluster.KMeans` - K-means clustering for targeted, local-box sampling

      • `sklearn.decomposition.PCA` - dimensionality reduction for cluster visualization
      
      • `sklearn.exceptions.ConvergenceWarning` – warning suppression during GP fitting

2. <ins>	**`NumPy`**</ins> – linear algebra, array operations, log/exponential transforms (for Function 1's log10 pre-transform), random number generation (`np.random.default_rng`), statistical aggregation (mean, std, median across seeds).

3.	<ins> **`SciPy`**:</ins>

      • `scipy.stats.norm` - Gaussian CDF/PDF for EI/PI acquisition function calculations

      • `scipy.stats.t` -  t-distribution for computing 95% confidence intervals (via `t.ppf`) for mean final regret, mean AURC

      • `scipy.stats.qmc.Sobol` - low-discrepancy Sobol sequence generation for quasi-random candidate pools (both the full-domain pool and the density-enhanced local-box pool)

      • `scipy.spatial.distance.cdist` - pairwise distance computation (used in the `min_distance_to_existing` duplicate exclusion filter - disabled feature) 

4.	 <ins>**`pandas`**</ins> - building/sorting ablation results tables (`combo_df`, `all_functions_full_tables`);

5.	<ins> **`pickle`** </ins> - checkpointing results at various key pipeline stages (ablation summaries, k-means results, next-query predictions, importing input datasets for each new week’s pipeline);

6.	 <ins>**`Matplotlib`** </ins> (`matplotlib.pyplot`, `matplotlib.patches`), used for all plots: elbow curves, PCA scree plots, cluster scatter grids (including 3D plots via `projection='3d'` subplot mode), and convergence trajectories;

7.	 <ins>**`joblib`** </ins> (`Parallel`, `delayed`) – seed parallelization across multiple (all available, `n_jobs=-1`) CPU cores in `run_full_joint_ablation` sweep

8.	 <ins>**`os`**</ins> - directory creation for output paths

9.	<ins> **`sys`**</ins> - stdout redirection to log files

10. <ins> **`warnings`**</ins> - suppressing convergence/variance warnings during fitting (after ensuring healthy behaviour)

<br>
<br>

🚀 <ins> **Installation & Running the Project:** </ins>

Prerequisites: 
- Python 3.13
- `git`

1. Clone the repository

```bash
git clone https://github.com/<carmen-timpau>/<BBO-Capstone-Project>.git
cd <BBO-Capstone-Project>
```

2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Choose a pipeline version to run
   
Each `week_XX/` directory within the `experiments/` directory is self-contained with its own `main.py`.
Navigate into the desired week (`week_01`, ..., `week_13`).

```bash
cd experiments/week_13
```

5. Input data
   
Each `week_XX/` directory already includes its corresponding dataset (e.g. `wk1_input_data.pkl`, ..., `wk13_input_data.pkl`, `final_data.pkl`) committed alongside `main.py` — no setup needed. Data is structured as:

```python
data = {
    "function_1": {"x": np.ndarray of shape (n_samples, n_dims), "y": np.ndarray of shape (n_samples,)},
    ...
    "function_8": {"x": ..., "y": ...},
}
```

6. Run the pipeline
   
```bash
python main.py
```

<ins>Note:</ins> Runtime is computationally heavy for later versions - expect roughly 2-2.5 hours to completion with 16 CPU cores available (longer with fewer cores). Outputs are streamed to `execution_output.log` rather than the console for later versions.

<br>
<br>

⚖️ **LICENSE:** **[MIT License](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/LICENSE)**

<br>
<br>

<ins> **Assumptions, Limitations & Biases:** </ins> 

These are dependent on the specific BO ML model employed. The assumptions, limitations, and biases of the different models developed as part of this capstone project have been included in their respective [Model Cards](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/model_cards/model_cards_info.md).

<br>
<br>

<ins> **Ethical Considerations:** </ins>

No part of this project contains sensitive or personal information. 

The initial datasets describing the 8 black-box functions, as well as the black-box functions themselves and all obtained weekly query outputs have been generated and provided by Imperial College London for use within the development of this capstone project for educational purposes only, as part of the 6-month Professional Certificate in Machine Learning and Artificial Intelligence course by Imperial College Executive Education. The intended use of the datasets within this repository is stated within their corresponding datasheets. 

<br>
<br>

📖 <ins> **Foundational References:** </ins> 

1. C. E. Rasmussen and C. K. I. Williams. “Gaussian Processes for Machine Learning.” _MIT Press_, 2005. https://doi.org/10.7551/mitpress/3206.001.0001

2. I. Roman, R. Santana, A. Mendiburu, and J. A. Lozano. “An Experimental Study in Adaptive Kernel Selection for Bayesian Optimization.” _IEEE Access_, 7:184294–184302, 2019. https://doi.org/10.1109/ACCESS.2019.2960498
   
3. M. Hoffman, E. Brochu, and N. de Freitas. “Portfolio Allocation for Bayesian Optimization.” Proceedings of the 27th Conference on Uncertainty in Artificial Intelligence (UAI), pp. 327–336, arXiv:1009.5419, 2011.

4. T. S. Breusch and A. R. Pagan. “A Simple Test for Heteroscedasticity and Random Coefficient Variation.” _Econometrica_, 47(5):1287–1294, 1979. https://doi.org/10.2307/1911963

5. A. I. Cowen‑Rivers, W. Lyu, Z. Wang, R. Tutunov, H. Jianye, J. Wang, and H. B. Ammar. “HEBO: Heteroscedastic Evolutionary Bayesian Optimisation.” Proceedings of the _34th Conference on Neural Information Processing Systems (NeurIPS)_, 2020.

6. A. I. Cowen‑Rivers, W. Lyu, R. Tutunov, Z. Wang, A. Grosnit, R. R. Griffiths, A. M. Maraval, H. Jianye, J. Wang, J. Peters, and H. Bou Ammar. “HEBO: Pushing the Limits of Sample‑Efficient Hyperparameter Optimisation.” arXiv:2012.03826, 2022. 

7. J.-H. Park, M. Cheon, and D.-Y. Koh. “BOOST: Bayesian Optimization with Optimal Kernel and Acquisition Function Selection Technique.” arXiv:2508.02332, 2025.
   
8. J.-H. Park, M. Cheon, J. Wi, and D.-Y. Koh. “BOOST: A Data-Driven Framework for the Automated Joint Selection of Kernel and Acquisition Functions in Bayesian Optimization.” arXiv:2508.02332, 2026.

9. F. Zhang and Y. Chen. “Direct Regret Optimization in Bayesian Optimization.” arXiv:2507.06529, 2025. 

<br>
<br>

<ins> **Acknowledgements:** </ins> 

I would like to express my sincere gratitude to the entire teaching faculty within the Executive Education programme at Imperial College London for their exceptional expertise and guidance. I would also like to recognize and particularly thank Vikesh Koul and Pulkit Saraf for their significant weekly insights and specialized industry expertise, which were instrumental to my progress.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<br>

🛠️ <ins> **Project Development Details:** </ins> 

The 3-month project was developed as part of the 6-month _Professional Certificate in Machine Learning & Artificial Intelligence_ joint programme at Imperial College London, during its second half - between June and August 2026.

<br>

✉️ <ins> **Project Developer Contact:** </ins> 

Carmen-Mihaela Timpau, carmen.timpau21@alumni.imperial.ac.uk, Imperial College London, United Kingdom.

_Please feel free to reach out with any questions, feedback, or ideas for discussion._
