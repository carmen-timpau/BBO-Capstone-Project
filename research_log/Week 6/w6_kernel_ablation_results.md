Week 6 BBO - Kernel Ablation Study Results (Pre-Query 6th Prediction Generation)
```text
----------------------------------------------------------------------------------------------------
                     FUNCTION 1 (Dim=2, N=15) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                       Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
       Ablation 2: RBF + WhiteNoise (Smooth Gaussian)    99.12465   0.25498                  -19.547
              Baseline: Matern 2.5 + WhiteNoise (ARD)   105.61635   0.15420                  -20.019
  Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)   108.46588   0.10794                  -20.241
Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)   120.35536  -0.09834                  -20.990
          Ablation 3: Rational Quadratic + WhiteNoise   123.04389  -0.14796                  -21.284
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale)   123.25044  -0.15182                  -21.284

Top Performing Kernel Config:
  Name   : Ablation 2: RBF + WhiteNoise (Smooth Gaussian)
  Params : RBF(length_scale=[3.85e+03, 0.0804]) + WhiteKernel(noise_level=7.45e-09)

----------------------------------------------------------------------------------------------------
                     FUNCTION 2 (Dim=2, N=15) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                       Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
          Ablation 3: Rational Quadratic + WhiteNoise     0.20683   0.25867                  -18.882
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale)     0.20819   0.24888                  -18.958
Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)     0.21268   0.21616                  -18.200
  Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)     0.24747  -0.06129                  -18.191
              Baseline: Matern 2.5 + WhiteNoise (ARD)     0.24969  -0.08045                  -18.200
       Ablation 2: RBF + WhiteNoise (Smooth Gaussian)     0.25094  -0.09132                  -18.227

Top Performing Kernel Config:
  Name   : Ablation 3: Rational Quadratic + WhiteNoise
  Params : RationalQuadratic(alpha=1e+05, length_scale=0.193) + WhiteKernel(noise_level=0.0023)

----------------------------------------------------------------------------------------------------
                     FUNCTION 3 (Dim=3, N=20) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                       Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
       Ablation 2: RBF + WhiteNoise (Smooth Gaussian)     0.04033   0.79129                  -16.489
              Baseline: Matern 2.5 + WhiteNoise (ARD)     0.04245   0.76880                  -17.679
  Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)     0.04492   0.74103                  -18.260
Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)     0.04760   0.70926                  -19.514
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale)     0.09733  -0.21562                  -28.091
          Ablation 3: Rational Quadratic + WhiteNoise     0.09889  -0.25484                  -27.985

Top Performing Kernel Config:
  Name   : Ablation 2: RBF + WhiteNoise (Smooth Gaussian)
  Params : RBF(length_scale=[1e+04, 1e+04, 0.247]) + WhiteKernel(noise_level=0.0286)

----------------------------------------------------------------------------------------------------
                     FUNCTION 4 (Dim=4, N=35) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                       Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
          Ablation 3: Rational Quadratic + WhiteNoise     2.05875   0.93250                  -20.586
       Ablation 2: RBF + WhiteNoise (Smooth Gaussian)     2.21921   0.92156                  -19.989
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale)     2.36409   0.91099                  -22.677
              Baseline: Matern 2.5 + WhiteNoise (ARD)     2.44011   0.90517                  -21.307
  Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)     2.62090   0.89060                  -22.626
Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)     3.10959   0.84600                  -24.273

Top Performing Kernel Config:
  Name   : Ablation 3: Rational Quadratic + WhiteNoise
  Params : RationalQuadratic(alpha=1.67, length_scale=2.25) + WhiteKernel(noise_level=0.00589)

----------------------------------------------------------------------------------------------------
                     FUNCTION 5 (Dim=4, N=25) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                       Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)   130.14615   0.86237                  -26.910
              Baseline: Matern 2.5 + WhiteNoise (ARD)   177.47083   0.74409                  -23.057
          Ablation 3: Rational Quadratic + WhiteNoise   179.67073   0.73771                  -25.299
  Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)   183.26797   0.72710                  -23.285
       Ablation 2: RBF + WhiteNoise (Smooth Gaussian)   183.46774   0.72650                  -23.041
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale)   184.48083   0.72347                  -25.825

Top Performing Kernel Config:
  Name   : Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)
  Params : Matern(length_scale=[8.16, 0.893, 1.15, 0.528], nu=2.5)

----------------------------------------------------------------------------------------------------
                     FUNCTION 6 (Dim=5, N=25) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                       Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
          Ablation 3: Rational Quadratic + WhiteNoise     0.28177   0.68873                  -26.575
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale)     0.30074   0.64542                  -27.055
Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)     0.33010   0.57280                  -25.661
  Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)     0.33403   0.56256                  -27.668
              Baseline: Matern 2.5 + WhiteNoise (ARD)     0.34720   0.52739                  -27.213
       Ablation 2: RBF + WhiteNoise (Smooth Gaussian)     0.37002   0.46323                  -26.402

Top Performing Kernel Config:
  Name   : Ablation 3: Rational Quadratic + WhiteNoise
  Params : RationalQuadratic(alpha=1.22, length_scale=1.94) + WhiteKernel(noise_level=0.0188)

----------------------------------------------------------------------------------------------------
                     FUNCTION 7 (Dim=6, N=35) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                       Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)     0.19035   0.78395                  -30.067
  Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)     0.19622   0.77042                  -30.577
              Baseline: Matern 2.5 + WhiteNoise (ARD)     0.19671   0.76929                  -30.729
       Ablation 2: RBF + WhiteNoise (Smooth Gaussian)     0.20540   0.74845                  -29.236
          Ablation 3: Rational Quadratic + WhiteNoise     0.24688   0.63659                  -41.440
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale)     0.26001   0.59690                  -42.093

Top Performing Kernel Config:
  Name   : Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)
  Params : Matern(length_scale=[5.73, 3.42, 1e+04, 2.16, 0.761, 1.82], nu=2.5)

----------------------------------------------------------------------------------------------------
                     FUNCTION 8 (Dim=8, N=45) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                       Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
              Baseline: Matern 2.5 + WhiteNoise (ARD)     0.15394   0.98034                    2.440
Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)     0.15402   0.98032                    2.442
  Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)     0.16025   0.97869                   -0.919
          Ablation 3: Rational Quadratic + WhiteNoise     0.27793   0.93590                  -21.815
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale)     0.28216   0.93394                  -22.353
       Ablation 2: RBF + WhiteNoise (Smooth Gaussian)     0.38921   0.87430                    1.200

Top Performing Kernel Config:
  Name   : Baseline: Matern 2.5 + WhiteNoise (ARD)
  Params : Matern(length_scale=[4.16, 6.15, 3.33, 10.3, 17.2, 7.89e+03, 4.31, 1e+04], nu=2.5) + WhiteKernel(noise_level=1e-06)

####################################################################################################
                           FUNCTIONS 1 THROUGH 8 SUMMARY
####################################################################################################
                                                     Best Variant  LOOCV R²                                                                                                       Learned Kernel
function_1         Ablation 2: RBF + WhiteNoise (Smooth Gaussian)   0.25498                                             RBF(length_scale=[3.85e+03, 0.0804]) + WhiteKernel(noise_level=7.45e-09)
function_2            Ablation 3: Rational Quadratic + WhiteNoise   0.25867                                 RationalQuadratic(alpha=1e+05, length_scale=0.193) + WhiteKernel(noise_level=0.0023)
function_3         Ablation 2: RBF + WhiteNoise (Smooth Gaussian)   0.79129                                            RBF(length_scale=[1e+04, 1e+04, 0.247]) + WhiteKernel(noise_level=0.0286)
function_4            Ablation 3: Rational Quadratic + WhiteNoise   0.93250                                  RationalQuadratic(alpha=1.67, length_scale=2.25) + WhiteKernel(noise_level=0.00589)
function_5  Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)   0.86237                                                              Matern(length_scale=[8.16, 0.893, 1.15, 0.528], nu=2.5)
function_6            Ablation 3: Rational Quadratic + WhiteNoise   0.68873                                   RationalQuadratic(alpha=1.22, length_scale=1.94) + WhiteKernel(noise_level=0.0188)
function_7  Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)   0.78395                                                  Matern(length_scale=[5.73, 3.42, 1e+04, 2.16, 0.761, 1.82], nu=2.5)
function_8                Baseline: Matern 2.5 + WhiteNoise (ARD)   0.98034  Matern(length_scale=[4.16, 6.15, 3.33, 10.3, 17.2, 7.89e+03, 4.31, 1e+04], nu=2.5) + WhiteKernel(noise_level=1e-06)
```
