 **Black-Box Optimisation (BBO) Capstone Project - Bayesian Optimisation**

<br>

📝 <ins> **Project Introduction:** </ins> 

Given an initial dataset of true datapoints describing 8 different, unrelated and unknown Black-Box functions of varying dimensionality (2D-8D), each modelling  real-world processes within various application industries, this project aims to apply and refine Bayesian Optimisation to identify the global maximum or maxima for each function.

Every week, over a period of 13 weeks, each function can only be queried once. Each full set of inputs (1 per function) are processed that same week and the outputs received help inform the coordinates of the next set of queries to be submitted for processing in the upcoming week, therefore leading to a refinement of the optimisation strategy for each of the 8 functions in a data-driven and personalised approach.

<br>

<ins>⚙️**Bayesian Optimisation (BO) ML Pipelines**</ins>:

The frameworks transition the approach from manual, intuitive strategy tuning to fully automated, robust and optimised machine learning workflows. By leveraging state-of-the-art practices, like HEBO, the project delivers fast, reliable, and high-quality Bayesian Optimisation results to tackle expensive, opaque Black-Box process optimisation across various industries within as few queries as possible.

Functional research code is logged in `experiments/`, which is itself organised in separate directories for each week, documenting the evolution of the Bayesian Optimisation ML pipelines over time.

<br>

📥 <ins> **Initial Datasets:** </ins> 

Initial datasets for all 8 Black-Box functions to be maximised can be found in the `initial_data/` folder attached to this repository as `.npy` files. Additionally, the full initial dataset formatted as a dictionary is accessible via `wk1_input_data.pkl` inside the same directory.

<br>

📈 <ins> **Individual Function Descriptions:** </ins>


<br>

📑 <ins> **Research Documentation & Dicussion:** </ins> 

Research documentation and the dicussion of strategies used at each stage can be found in `strategy_discussion.md` and `strategy_summary.md` files within each week's directory.

<br>

<ins> **Foundational References:** </ins> 

1. C. E. Rasmussen and C. K. I. Williams. “Gaussian Processes for Machine Learning.” MIT Press,  doi:10.7551/MITPRESS/3206.001.0001, 2005.

2. T. S. Breusch and A. R. Pagan. “A Simple Test for Heteroscedasticity and Random Coefficient Variation.” Econometrica, 47(5):1287–1294, https://doi.org/10.2307/1911963, 1979.

3. A. I. Cowen‑Rivers, W. Lyu, R. Tutunov, Z. Wang, A. Grosnit, R. R. Griffiths, A. M. Maraval, H. Jianye, J. Wang, J. Peters, and H. Bou Ammar. “HEBO: Pushing the Limits of Sample‑Efficient Hyperparameter Optimisation.” arXiv:2012.03826, 2022. 

4. F. Zhang and Y. Chen. “Direct Regret Optimization in Bayesian Optimization.” arXiv:2507.06529, 2025. 

---------------------------------------------------------------------------------------------------------------------

<br>

🛠️ <ins> **Project Development Details:** </ins> 

The project was developed as part of the 6-month _Professional Certificate in Machine Learning & Artificial Intelligence_ joint programme at Imperial College London.

<br>

✉️ <ins> **Project Developer Contact:** </ins> 

Carmen-Mihaela Timpau, carmen.timpau21@alumni.imperial.ac.uk, Imperial College London, United Kingdom.

_Please feel free to reach out with any questions, feedback, or ideas for discussion._
