 **Black-Box Optimisation (BBO) Capstone Project - Bayesian Optimisation**

<br>

📝 <ins> **Project Introduction:** </ins> 

Given an initial dataset of true datapoints describing 8 different, unrelated and unknown Black-Box functions of varying dimensionality (2D-8D), each modelling  real-world processes within various application industries, this project aims to apply and refine Bayesian Optimisation to identify the global maximum or maxima for each function.

Every week, over a period of 13 weeks, each function can only be queried once. Each full set of inputs (1 per function) are processed that same week and the outputs received help inform the coordinates of the next set of queries to be submitted for processing in the upcoming week, therefore leading to a refinement of the optimisation strategy for each of the 8 functions in a data-driven and personalised approach.

<br>

📥 **[Datasets](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/data/weekly_processed)**

📄 **[Datasheets for Datasets](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/data/weekly_processed/datasheets_info.md)**

<br>

<ins>⚙️**Bayesian Optimisation (BO) ML Pipelines**</ins>:

The frameworks transition the approach from manual, intuitive strategy tuning to fully automated, robust and optimised machine learning workflows. By leveraging state-of-the-art practices, like HEBO, the project delivers fast, reliable, and high-quality Bayesian Optimisation results to tackle expensive, opaque Black-Box process optimisation across various industries within as few queries as possible.

Functional research code is logged in `experiments/`, which is itself organised in separate directories for each week, documenting the evolution of the Bayesian Optimisation ML pipelines over time.


🔩 **[Bayesian Optimisation ML Pipelines](https://github.com/carmen-timpau/BBO-Capstone-Project/tree/main/experiments)**

📄 **[Model Cards for Bayesian Optimisation ML Pipelines](https://github.com/carmen-timpau/BBO-Capstone-Project/blob/main/model_cards/model_cards_info.md)**



<br>

📑 <ins> **Research Documentation & Dicussion:** </ins> 

Research documentation and the dicussion of strategies used at each stage can be found in `strategy_discussion.md` and `strategy_summary.md` files within each week's directory.

<br>

<ins>📈 **Bayesian Optimisation Outcomes:** </ins>

<br>

| Function | Input | Output | # of Initial <br> Datapoints | # of Final <br> Datapoints | Initial <br> Maximum | Final <br> Maximum | Week <br> Optimised | Process / Industry |
|----------|----------------------|-----------------------|-------------------------|-----------------------|-----------------------|-----------------------|-----------------------| -----------------------| 
| <div align="center">1</div> | <div align="center">2D</div> | <div align="center">1D</div> | <div align="center">10</div> | <div align="center">23</div> | <div align="center">7.711e-16</div> | <div align="center">1.796e-10</div> |  <div align="center">**10**</div> | <div align="center">Radiation Detection</div> |
| <div align="center">2</div> | <div align="center">2D</div> | <div align="center">1D</div> | <div align="center">10</div> | <div align="center">23</div> | <div align="center">0.611</div> | <div align="center">0.756</div> | <div align="center">**6**</div> | <div align="center">Noisy Log-Likelihood <br> Optimisation</div> |
| <div align="center">3</div> | <div align="center">3D</div> | <div align="center">1D</div> | <div align="center">15</div> | <div align="center">28</div> | <div align="center">-0.035</div> | <div align="center">-0.019</div> | <div align="center">**11**</div> | <div align="center">Pharmaceutical <br> Drug Formulation</div> |
| <div align="center">4</div> | <div align="center">4D</div> | <div align="center">1D</div> | <div align="center">30</div> | <div align="center">43</div> | <div align="center">-4.026</div> | <div align="center">0.570</div> | <div align="center">**10**</div> | <div align="center">Warehouse Optimisation</div> |
| <div align="center">5</div> | <div align="center">4D</div> | <div align="center">1D</div> | <div align="center">20</div> | <div align="center">33</div> | <div align="center">1088.860</div> | <div align="center">2333.007</div> | <div align="center">**6**</div> | <div align="center">Chemical Process <br> Engineering</div> |
| <div align="center">6</div> | <div align="center">5D</div> | <div align="center">1D</div> | <div align="center">20</div> | <div align="center">33</div> | <div align="center">-0.714</div> | <div align="center">-0.172</div> | <div align="center">**12**</div> | <div align="center">Product Formulation</div> |
| <div align="center">7</div> | <div align="center">6D</div> | <div align="center">1D</div> | <div align="center">30</div> | <div align="center">43</div> | <div align="center">1.365</div> | <div align="center">3.224</div> | <div align="center">**13**</div> | <div align="center">Machine Learning Model <br> Hyperparameter Tuning</div> |
| <div align="center">8</div> | <div align="center">8D</div> | <div align="center">1D</div> | <div align="center">40</div> | <div align="center">53</div> | <div align="center">9.598</div> | <div align="center">9.956</div> | <div align="center">**2**</div> | <div align="center">Machine Learning Model <br> Hyperparameter Tuning</div> |

<br>

<p align="center">
<img width="6563" height="2956" alt="image" src="https://github.com/user-attachments/assets/dc28b713-a3ba-4eb4-ae7c-585e90bf15cf" />
</p>

<p align="center">
<strong>Figure 1.</strong> <em>Bayesian Optimisation Outcomes Landscape - Progress over 13-Week Optimisation Period for each Black-Box Function</em>
</p>

<br>

<ins> **Foundational References:** </ins> 

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
