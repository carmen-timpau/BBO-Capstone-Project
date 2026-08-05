```text
==============================================================================================================
        SURROGATE MODELING PERFORMANCE COMPARISON (LOOCV: GP vs. Deep Ensemble RMSE)
==============================================================================================================
[FUNCTION_1] (Dim=2)
  • Winning GP Kernel   : Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)
  • GP RMSE             : 51.5845
  • Deep Ensemble RMSE  : 48.8050
  • Best Surrogate      : Deep Ensemble
--------------------------------------------------------------------------------------------------------------
[FUNCTION_2] (Dim=2)
  • Winning GP Kernel   : Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise
  • GP RMSE             : 0.1971
  • Deep Ensemble RMSE  : 0.2949
  • Best Surrogate      : Gaussian Process
--------------------------------------------------------------------------------------------------------------
[FUNCTION_3] (Dim=3)
  • Winning GP Kernel   : Ablation 2: RBF + WhiteNoise (Smooth Gaussian)
  • GP RMSE             : 0.0360
  • Deep Ensemble RMSE  : 0.1094
  • Best Surrogate      : Gaussian Process
--------------------------------------------------------------------------------------------------------------
[FUNCTION_4] (Dim=4)
  • Winning GP Kernel   : Ablation 3: Rational Quadratic + WhiteNoise
  • GP RMSE             : 1.9289
  • Deep Ensemble RMSE  : 2.3940
  • Best Surrogate      : Gaussian Process
--------------------------------------------------------------------------------------------------------------
[FUNCTION_5] (Dim=4)
  • Winning GP Kernel   : Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise
  • GP RMSE             : 139.8252
  • Deep Ensemble RMSE  : 262.3063
  • Best Surrogate      : Gaussian Process
--------------------------------------------------------------------------------------------------------------
[FUNCTION_6] (Dim=5)
  • Winning GP Kernel   : Ablation 3: Rational Quadratic + WhiteNoise
  • GP RMSE             : 0.2572
  • Deep Ensemble RMSE  : 0.2323
  • Best Surrogate      : Deep Ensemble
--------------------------------------------------------------------------------------------------------------
[FUNCTION_7] (Dim=6)
  • Winning GP Kernel   : Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)
  • GP RMSE             : 0.1949
  • Deep Ensemble RMSE  : 0.3201
  • Best Surrogate      : Gaussian Process
--------------------------------------------------------------------------------------------------------------
[FUNCTION_8] (Dim=8)
  • Winning GP Kernel   : Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)
  • GP RMSE             : 0.1474
  • Deep Ensemble RMSE  : 1.6166
  • Best Surrogate      : Gaussian Process
--------------------------------------------------------------------------------------------------------------

[FINAL SUMMARY] Gaussian Process Wins: 6 | Deep Ensemble Wins: 2
==============================================================================================================
{'function_1': {'Dim': 2,
  'Winning GP Kernel': 'Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)',
  'GP RMSE': np.float64(51.584489312062836),
  'Deep Ensemble RMSE': np.float64(48.80495392233741),
  'Best Surrogate': 'Deep Ensemble'},
 'function_2': {'Dim': 2,
  'Winning GP Kernel': 'Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise',
  'GP RMSE': np.float64(0.19711804688522244),
  'Deep Ensemble RMSE': np.float64(0.29485102767432503),
  'Best Surrogate': 'Gaussian Process'},
 'function_3': {'Dim': 3,
  'Winning GP Kernel': 'Ablation 2: RBF + WhiteNoise (Smooth Gaussian)',
  'GP RMSE': np.float64(0.03602992278917273),
  'Deep Ensemble RMSE': np.float64(0.10939682607343433),
  'Best Surrogate': 'Gaussian Process'},
 'function_4': {'Dim': 4,
  'Winning GP Kernel': 'Ablation 3: Rational Quadratic + WhiteNoise',
  'GP RMSE': np.float64(1.9288501803354454),
  'Deep Ensemble RMSE': np.float64(2.393953108327435),
  'Best Surrogate': 'Gaussian Process'},
 'function_5': {'Dim': 4,
  'Winning GP Kernel': 'Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise',
  'GP RMSE': np.float64(139.82522047317283),
  'Deep Ensemble RMSE': np.float64(262.3063122715996),
  'Best Surrogate': 'Gaussian Process'},
 'function_6': {'Dim': 5,
  'Winning GP Kernel': 'Ablation 3: Rational Quadratic + WhiteNoise',
  'GP RMSE': np.float64(0.25721218883571806),
  'Deep Ensemble RMSE': np.float64(0.2323490036903266),
  'Best Surrogate': 'Deep Ensemble'},
 'function_7': {'Dim': 6,
  'Winning GP Kernel': 'Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)',
  'GP RMSE': np.float64(0.19488434380087266),
  'Deep Ensemble RMSE': np.float64(0.3201375572041027),
  'Best Surrogate': 'Gaussian Process'},
 'function_8': {'Dim': 8,
  'Winning GP Kernel': 'Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)',
  'GP RMSE': np.float64(0.1473770959764673),
  'Deep Ensemble RMSE': np.float64(1.6166217501732076),
  'Best Surrogate': 'Gaussian Process'}}
```
