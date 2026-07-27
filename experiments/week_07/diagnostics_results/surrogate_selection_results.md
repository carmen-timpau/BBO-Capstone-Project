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
