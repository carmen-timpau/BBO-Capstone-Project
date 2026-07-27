**Personalised Ablation-Tuned GP vs. Deep Ensemble Surrogate Selection**

Comparative evaluation of ablation-tuned Gaussian Processes (GPs) and Deep Ensembles of Multi-Layer Perceptrons across all 8 Black-Box functions for robust surrogate modelling and uncertainty quantification in the Bayesian Optimisation pipeline.

_Evaluation Methodology:_

- **Task**: Regression to model and predict black-box objective values for each function dataset. The winning surrogate model for each function will be used for objective function approximation and next query prediction in the Bayesian Optimisation loop for Week 7.
  
- **Validation Strategy**: Leave-One-Out Cross-Validation (LOOCV).
  
- **Performance Metric**: Out-of-sample Root Mean Squared Error (RMSE) evaluated across unseen test folds to measure generalisation capability and prediction accuracy.

```text
==============================================================================================================
        SURROGATE MODELING PERFORMANCE COMPARISON (LOOCV: GP vs. Deep Ensemble RMSE)
==============================================================================================================
[FUNCTION_1] (Dim=2)
  • Winning GP Kernel   : Ablation 2: RBF + WhiteNoise (Smooth Gaussian)
  • GP RMSE             : 97.5039
  • Deep Ensemble RMSE  : 139.7156
  • Best Surrogate      : Gaussian Process
--------------------------------------------------------------------------------------------------------------
[FUNCTION_2] (Dim=2)
  • Winning GP Kernel   : Ablation 3: Rational Quadratic + WhiteNoise
  • GP RMSE             : 0.2199
  • Deep Ensemble RMSE  : 0.3022
  • Best Surrogate      : Gaussian Process
--------------------------------------------------------------------------------------------------------------
[FUNCTION_3] (Dim=3)
  • Winning GP Kernel   : Ablation 2: RBF + WhiteNoise (Smooth Gaussian)
  • GP RMSE             : 0.0376
  • Deep Ensemble RMSE  : 0.1180
  • Best Surrogate      : Gaussian Process
--------------------------------------------------------------------------------------------------------------
[FUNCTION_4] (Dim=4)
  • Winning GP Kernel   : Ablation 3: Rational Quadratic + WhiteNoise
  • GP RMSE             : 2.0078
  • Deep Ensemble RMSE  : 2.4495
  • Best Surrogate      : Gaussian Process
--------------------------------------------------------------------------------------------------------------
[FUNCTION_5] (Dim=4)
  • Winning GP Kernel   : Ablation 3: Rational Quadratic + WhiteNoise
  • GP RMSE             : 323.2346
  • Deep Ensemble RMSE  : 341.9699
  • Best Surrogate      : Gaussian Process
--------------------------------------------------------------------------------------------------------------
[FUNCTION_6] (Dim=5)
  • Winning GP Kernel   : Ablation 3: Rational Quadratic + WhiteNoise
  • GP RMSE             : 0.2598
  • Deep Ensemble RMSE  : 0.2341
  • Best Surrogate      : Deep Ensemble
--------------------------------------------------------------------------------------------------------------
[FUNCTION_7] (Dim=6)
  • Winning GP Kernel   : Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)
  • GP RMSE             : 0.2057
  • Deep Ensemble RMSE  : 0.3273
  • Best Surrogate      : Gaussian Process
--------------------------------------------------------------------------------------------------------------
[FUNCTION_8] (Dim=8)
  • Winning GP Kernel   : Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)
  • GP RMSE             : 0.1538
  • Deep Ensemble RMSE  : 1.5643
  • Best Surrogate      : Gaussian Process
--------------------------------------------------------------------------------------------------------------

[FINAL SUMMARY] Gaussian Process Wins: 7 | Deep Ensemble Wins: 1
==============================================================================================================
```
