```test
----------------------------------------------------------------------------------------------------
                     FUNCTION 1 (Dim=2, N=17) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                                    Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
             Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)    51.58451  -0.18153                  -23.223
   Ablation 6: RBF Isotropic (Shared Lengthscale 0.5) + WhiteNoise    54.42039  -0.31501                  -24.122
                           Baseline: Matern 2.5 + WhiteNoise (ARD)    55.64102  -0.37466                  -23.223
                       Ablation 3: Rational Quadratic + WhiteNoise    55.68965  -0.37706                  -23.997
               Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)    56.08143  -0.39651                  -23.250
                    Ablation 2: RBF + WhiteNoise (Smooth Gaussian)    57.40695  -0.46330                  -23.181
         Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise    59.03399  -0.54742                  -24.097
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise    60.23244  -0.61089                  -24.077

Top Performing Kernel Config:
  Name   : Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)
  Params : Matern(length_scale=[1.12, 0.0801], nu=2.5)

----------------------------------------------------------------------------------------------------
                     FUNCTION 2 (Dim=2, N=17) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                                    Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
         Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise     0.17189   0.58522                  -18.612
                    Ablation 2: RBF + WhiteNoise (Smooth Gaussian)     0.17204   0.58453                  -18.612
               Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)     0.18233   0.53332                  -18.823
                           Baseline: Matern 2.5 + WhiteNoise (ARD)     0.18353   0.52715                  -18.749
   Ablation 6: RBF Isotropic (Shared Lengthscale 0.5) + WhiteNoise     0.23164   0.24679                  -19.815
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise     0.23216   0.24337                  -20.084
                       Ablation 3: Rational Quadratic + WhiteNoise     0.23221   0.24308                  -19.815
             Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)     0.27693  -0.07653                  -20.067

Top Performing Kernel Config:
  Name   : Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise
  Params : RBF(length_scale=[0.273, 5.06e+03]) + WhiteKernel(noise_level=0.218)

----------------------------------------------------------------------------------------------------
                     FUNCTION 3 (Dim=3, N=22) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                                    Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
                    Ablation 2: RBF + WhiteNoise (Smooth Gaussian)     0.03644   0.82075                  -16.531
         Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise     0.03644   0.82075                  -16.531
                           Baseline: Matern 2.5 + WhiteNoise (ARD)     0.03849   0.79997                  -18.177
               Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)     0.04165   0.76582                  -19.004
             Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)     0.04355   0.74387                  -21.177
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise     0.09451  -0.20602                  -30.934
                       Ablation 3: Rational Quadratic + WhiteNoise     0.09714  -0.27402                  -30.847
   Ablation 6: RBF Isotropic (Shared Lengthscale 0.5) + WhiteNoise     0.09714  -0.27413                  -30.847

Top Performing Kernel Config:
  Name   : Ablation 2: RBF + WhiteNoise (Smooth Gaussian)
  Params : RBF(length_scale=[1e+04, 1e+04, 0.268]) + WhiteKernel(noise_level=0.0255)

----------------------------------------------------------------------------------------------------
                     FUNCTION 4 (Dim=4, N=37) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                                    Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
                       Ablation 3: Rational Quadratic + WhiteNoise     1.91308   0.94449                  -18.647
   Ablation 6: RBF Isotropic (Shared Lengthscale 0.5) + WhiteNoise     2.00353   0.93912                  -19.324
                    Ablation 2: RBF + WhiteNoise (Smooth Gaussian)     2.11008   0.93247                  -18.818
         Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise     2.11008   0.93247                  -18.818
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise     2.19787   0.92674                  -21.022
                           Baseline: Matern 2.5 + WhiteNoise (ARD)     2.32593   0.91795                  -20.182
               Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)     2.49147   0.90586                  -21.589
             Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)     2.96315   0.86684                  -23.685

Top Performing Kernel Config:
  Name   : Ablation 3: Rational Quadratic + WhiteNoise
  Params : RationalQuadratic(alpha=1.53, length_scale=2.38) + WhiteKernel(noise_level=0.00515)

----------------------------------------------------------------------------------------------------
                     FUNCTION 5 (Dim=4, N=27) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                                    Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise   139.60201   0.95231                  -16.223
                       Ablation 3: Rational Quadratic + WhiteNoise   147.73575   0.94659                  -16.799
   Ablation 6: RBF Isotropic (Shared Lengthscale 0.5) + WhiteNoise   158.93279   0.93819                  -17.323
                    Ablation 2: RBF + WhiteNoise (Smooth Gaussian)   181.16960   0.91968                  -16.361
         Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise   191.56006   0.91020                  -16.361
                           Baseline: Matern 2.5 + WhiteNoise (ARD)   271.91680   0.81906                  -15.069
               Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)   284.16836   0.80239                  -14.527
             Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)   350.87672   0.69872                  -16.500

Top Performing Kernel Config:
  Name   : Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise
  Params : Matern(length_scale=2.04, nu=2.5) + WhiteKernel(noise_level=1e-06)

----------------------------------------------------------------------------------------------------
                     FUNCTION 6 (Dim=5, N=27) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                                    Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
                       Ablation 3: Rational Quadratic + WhiteNoise     0.25549   0.78644                  -24.247
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise     0.27937   0.74464                  -25.082
             Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)     0.30596   0.69372                  -23.866
                           Baseline: Matern 2.5 + WhiteNoise (ARD)     0.30970   0.68619                  -23.866
               Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)     0.31334   0.67877                  -24.307
   Ablation 6: RBF Isotropic (Shared Lengthscale 0.5) + WhiteNoise     0.31590   0.67350                  -25.766
         Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise     0.35708   0.58284                  -24.000
                    Ablation 2: RBF + WhiteNoise (Smooth Gaussian)     0.37686   0.53532                  -24.000

Top Performing Kernel Config:
  Name   : Ablation 3: Rational Quadratic + WhiteNoise
  Params : RationalQuadratic(alpha=0.828, length_scale=2.1) + WhiteKernel(noise_level=1e-06)

----------------------------------------------------------------------------------------------------
                     FUNCTION 7 (Dim=6, N=37) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                                    Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
               Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)     0.19488   0.80311                  -33.336
             Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)     0.19831   0.79613                  -32.663
                           Baseline: Matern 2.5 + WhiteNoise (ARD)     0.20701   0.77784                  -32.663
                       Ablation 3: Rational Quadratic + WhiteNoise     0.21245   0.76602                  -41.207
   Ablation 6: RBF Isotropic (Shared Lengthscale 0.5) + WhiteNoise     0.21245   0.76602                  -41.207
         Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise     0.21341   0.76389                  -32.578
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise     0.22437   0.73903                  -41.797
                    Ablation 2: RBF + WhiteNoise (Smooth Gaussian)     0.25564   0.66121                  -32.578

Top Performing Kernel Config:
  Name   : Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)
  Params : Matern(length_scale=[4.5, 1.8, 1e+04, 3, 1.41, 2.61], nu=1.5) + WhiteKernel(noise_level=1e-06)

----------------------------------------------------------------------------------------------------
                     FUNCTION 8 (Dim=8, N=47) - KERNEL ABLATION STUDY
----------------------------------------------------------------------------------------------------
                                                    Kernel Variant  LOOCV RMSE  LOOCV R²  Log Marginal Likelihood
             Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)     0.14738   0.98279                    5.032
               Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)     0.15489   0.98099                    1.730
         Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise     0.16803   0.97763                    3.258
                           Baseline: Matern 2.5 + WhiteNoise (ARD)     0.17154   0.97668                    5.031
                    Ablation 2: RBF + WhiteNoise (Smooth Gaussian)     0.17370   0.97609                    3.258
                       Ablation 3: Rational Quadratic + WhiteNoise     0.26614   0.94388                  -20.590
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise     0.27654   0.93940                  -21.461
   Ablation 6: RBF Isotropic (Shared Lengthscale 0.5) + WhiteNoise     0.31479   0.92148                  -23.553

Top Performing Kernel Config:
  Name   : Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)
  Params : Matern(length_scale=[4.13, 6.67, 3.39, 9.81, 17.4, 1e+04, 4.23, 1e+04], nu=2.5)

####################################################################################################
                           FUNCTIONS 1 THROUGH 8 SUMMARY
####################################################################################################
                                                                  Best Variant  LOOCV R²                                                                                  Learned Kernel
function_1               Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)  -0.18153                                                     Matern(length_scale=[1.12, 0.0801], nu=2.5)
function_2           Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise   0.58522                            RBF(length_scale=[0.273, 5.06e+03]) + WhiteKernel(noise_level=0.218)
function_3                      Ablation 2: RBF + WhiteNoise (Smooth Gaussian)   0.82075                       RBF(length_scale=[1e+04, 1e+04, 0.268]) + WhiteKernel(noise_level=0.0255)
function_4                         Ablation 3: Rational Quadratic + WhiteNoise   0.94449             RationalQuadratic(alpha=1.53, length_scale=2.38) + WhiteKernel(noise_level=0.00515)
function_5  Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise   0.95231                              Matern(length_scale=2.04, nu=2.5) + WhiteKernel(noise_level=1e-06)
function_6                         Ablation 3: Rational Quadratic + WhiteNoise   0.78644               RationalQuadratic(alpha=0.828, length_scale=2.1) + WhiteKernel(noise_level=1e-06)
function_7                 Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)   0.80311  Matern(length_scale=[4.5, 1.8, 1e+04, 3, 1.41, 2.61], nu=1.5) + WhiteKernel(noise_level=1e-06)
function_8               Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)   0.98279                 Matern(length_scale=[4.13, 6.67, 3.39, 9.81, 17.4, 1e+04, 4.23, 1e+04], nu=2.5)
```
