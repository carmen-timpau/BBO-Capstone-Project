**<p align="center">DESIGN NOTES for Data-Informed Iterative Bayesian Optimisation Machine Learning Pipeline Development</p>**

<br>

_Choice of Main Machine Learning Library_

The choice to focus on preponderantly leveraging scikit-learn’s tools instead of leveraging deep learning frameworks like PyTorch and TensorFlow for neural networks as part of this Black-Box Optimisation capstone project was made based on the small sizes (10-40 initial datapoints) of the functions’ datasets, which do not allow the leveraging neural networks for modelling the unknown functions or for productive classification purposes. This is because neural networks require massive datasets for effective training and to avoid overfitting and generalise well, while scikit-learn is best suited for small-sized datasets, like the ones available for this project.

_Main Trade-off_: As no dedicated BO libraries like BoTorch or GPyTorch were used and instead all components of a BO pipeline were built from scratch, full visibility was achieved, as well as complete architectural and tuning control over every step within the developed ML pipelines, and no dependency on a framework’s internal assumptions, but at the expense of a larger codebase to build, develop and maintain.

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
