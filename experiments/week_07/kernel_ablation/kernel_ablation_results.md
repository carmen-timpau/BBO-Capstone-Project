
----------------------------------------------------------------------------------------------------
                     FUNCTION 1 (Dim=2, N=16) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                       Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
       Ablation 2: RBF + WhiteNoise (Smooth Gaussian)    97.50534   0.28292                  -20.406
              Baseline: Matern 2.5 + WhiteNoise (ARD)   101.61130   0.22126                  -20.926
  Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)   103.52629   0.19163                  -21.185
Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)   109.18848   0.10078                  -20.926
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale)   135.84510  -0.39187                  -22.703
          Ablation 3: Rational Quadratic + WhiteNoise   137.60479  -0.42816                  -22.703

Top Performing Kernel Config:
  Name   : Ablation 2: RBF + WhiteNoise (Smooth Gaussian)
  Params : RBF(length_scale=[1e+08, 0.0873]) + WhiteKernel(noise_level=2.58e-09)

----------------------------------------------------------------------------------------------------
                     FUNCTION 2 (Dim=2, N=16) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                       Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
          Ablation 3: Rational Quadratic + WhiteNoise     0.22038   0.30529                  -18.338
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale)     0.22898   0.25000                  -18.728
  Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)     0.26092   0.02616                  -18.459
              Baseline: Matern 2.5 + WhiteNoise (ARD)     0.26424   0.00118                  -18.379
Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)     0.27537  -0.08466                  -18.704
       Ablation 2: RBF + WhiteNoise (Smooth Gaussian)     0.27818  -0.10699                  -18.231

Top Performing Kernel Config:
  Name   : Ablation 3: Rational Quadratic + WhiteNoise
  Params : RationalQuadratic(alpha=1e+05, length_scale=0.257) + WhiteKernel(noise_level=1e-06)

----------------------------------------------------------------------------------------------------
                     FUNCTION 3 (Dim=3, N=21) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                       Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
       Ablation 2: RBF + WhiteNoise (Smooth Gaussian)     0.03813   0.81188                  -16.412
              Baseline: Matern 2.5 + WhiteNoise (ARD)     0.04007   0.79229                  -17.912
  Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)     0.04244   0.76696                  -18.659
Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)     0.04530   0.73456                  -20.105
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale)     0.09644  -0.20314                  -29.376
          Ablation 3: Rational Quadratic + WhiteNoise     0.09830  -0.25012                  -29.331

Top Performing Kernel Config:
  Name   : Ablation 2: RBF + WhiteNoise (Smooth Gaussian)
  Params : RBF(length_scale=[1e+04, 1e+04, 0.264]) + WhiteKernel(noise_level=0.0266)

----------------------------------------------------------------------------------------------------
                     FUNCTION 4 (Dim=4, N=36) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                       Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
          Ablation 3: Rational Quadratic + WhiteNoise     1.99066   0.94089                  -18.502
       Ablation 2: RBF + WhiteNoise (Smooth Gaussian)     2.18059   0.92908                  -18.236
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale)     2.27790   0.92260                  -20.740
              Baseline: Matern 2.5 + WhiteNoise (ARD)     2.37670   0.91574                  -19.534
  Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)     2.52095   0.90521                  -20.924
Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)     3.00174   0.86560                  -22.697

Top Performing Kernel Config:
  Name   : Ablation 3: Rational Quadratic + WhiteNoise
  Params : RationalQuadratic(alpha=1.53, length_scale=2.34) + WhiteKernel(noise_level=0.00517)

----------------------------------------------------------------------------------------------------
                     FUNCTION 5 (Dim=4, N=26) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                       Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
          Ablation 3: Rational Quadratic + WhiteNoise   327.17569   0.61389                  -24.768
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale)   335.45324   0.59410                  -25.671
       Ablation 2: RBF + WhiteNoise (Smooth Gaussian)   373.45795   0.49692                  -23.864
Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)   375.40772   0.49166                  -26.790
  Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)   379.32362   0.48099                  -25.407
              Baseline: Matern 2.5 + WhiteNoise (ARD)   388.32396   0.45607                  -24.708

Top Performing Kernel Config:
  Name   : Ablation 3: Rational Quadratic + WhiteNoise
  Params : RationalQuadratic(alpha=1e+05, length_scale=1.83) + WhiteKernel(noise_level=0.0412)

----------------------------------------------------------------------------------------------------
                     FUNCTION 6 (Dim=5, N=26) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                       Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
          Ablation 3: Rational Quadratic + WhiteNoise     0.25748   0.77273                  -24.681
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale)     0.28164   0.72807                  -25.380
Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)     0.30843   0.67389                  -24.125
  Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)     0.31258   0.66505                  -24.526
              Baseline: Matern 2.5 + WhiteNoise (ARD)     0.32059   0.64767                  -24.125
       Ablation 2: RBF + WhiteNoise (Smooth Gaussian)     0.36013   0.55541                  -25.631

Top Performing Kernel Config:
  Name   : Ablation 3: Rational Quadratic + WhiteNoise
  Params : RationalQuadratic(alpha=0.894, length_scale=2.01) + WhiteKernel(noise_level=1e-06)

----------------------------------------------------------------------------------------------------
                     FUNCTION 7 (Dim=6, N=36) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                       Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)     0.20567   0.74216                  -33.252
          Ablation 3: Rational Quadratic + WhiteNoise     0.22859   0.68151                  -42.687
       Ablation 2: RBF + WhiteNoise (Smooth Gaussian)     0.22897   0.68046                  -31.960
  Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)     0.23459   0.66457                  -34.367
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale)     0.24462   0.63527                  -43.373
              Baseline: Matern 2.5 + WhiteNoise (ARD)     0.25708   0.59716                  -33.252

Top Performing Kernel Config:
  Name   : Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)
  Params : Matern(length_scale=[4.16, 1.41, 1e+04, 2.46, 1.17, 2.23], nu=2.5)

----------------------------------------------------------------------------------------------------
                     FUNCTION 8 (Dim=8, N=46) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                       Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)     0.15385   0.98088                    3.674
  Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)     0.15845   0.97971                    0.432
              Baseline: Matern 2.5 + WhiteNoise (ARD)     0.17727   0.97461                    3.672
       Ablation 2: RBF + WhiteNoise (Smooth Gaussian)     0.18997   0.97084                    2.083
          Ablation 3: Rational Quadratic + WhiteNoise     0.27488   0.93895                  -21.188
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale)     0.28097   0.93621                  -21.814

Top Performing Kernel Config:
  Name   : Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)
  Params : Matern(length_scale=[4.14, 6.41, 3.31, 10.4, 17, 162, 4.33, 1e+04], nu=2.5)

####################################################################################################
                           FUNCTIONS 1 THROUGH 8 SUMMARY
####################################################################################################
                                                     Best Variant  LOOCV R²                                                                       Learned Kernel
function_1         Ablation 2: RBF + WhiteNoise (Smooth Gaussian)   0.28292                RBF(length_scale=[1e+08, 0.0873]) + WhiteKernel(noise_level=2.58e-09)
function_2            Ablation 3: Rational Quadratic + WhiteNoise   0.30529  RationalQuadratic(alpha=1e+05, length_scale=0.257) + WhiteKernel(noise_level=1e-06)
function_3         Ablation 2: RBF + WhiteNoise (Smooth Gaussian)   0.81188            RBF(length_scale=[1e+04, 1e+04, 0.264]) + WhiteKernel(noise_level=0.0266)
function_4            Ablation 3: Rational Quadratic + WhiteNoise   0.94089  RationalQuadratic(alpha=1.53, length_scale=2.34) + WhiteKernel(noise_level=0.00517)
function_5            Ablation 3: Rational Quadratic + WhiteNoise   0.61389  RationalQuadratic(alpha=1e+05, length_scale=1.83) + WhiteKernel(noise_level=0.0412)
function_6            Ablation 3: Rational Quadratic + WhiteNoise   0.77273   RationalQuadratic(alpha=0.894, length_scale=2.01) + WhiteKernel(noise_level=1e-06)
function_7  Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)   0.74216                   Matern(length_scale=[4.16, 1.41, 1e+04, 2.46, 1.17, 2.23], nu=2.5)
function_8  Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)   0.98088          Matern(length_scale=[4.14, 6.41, 3.31, 10.4, 17, 162, 4.33, 1e+04], nu=2.5)
