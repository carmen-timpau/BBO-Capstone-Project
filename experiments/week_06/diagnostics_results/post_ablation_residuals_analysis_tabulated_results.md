```text
==========================================================================
     FUNCTION 1 DIAGNOSTICS — WINNING CONFIG: RBF + WHITENOISE (SMOOTH GAUSSIAN)
==========================================================================
Full Dataset Log Marginal Likelihood (LML)   : -19.547
Mean LOOCV Fold Log Marginal Likelihood      : -18.473
LOOCV Root Mean Squared Error (RMSE)         : 99.1246
LOOCV R-squared Score                        : 0.2550
Breusch-Pagan-like p-value (not stat. valid) : 0.68598
--------------------------------------------------------------------------
Learned Kernel Parameters:
RBF(length_scale=[3.85e+03, 0.0804]) + WhiteKernel(noise_level=7.45e-09)
--------------------------------------------------------------------------
Verdict for Function 1 (15 datapoints, Week 5): HOMOSCEDASTIC
==========================================================================

==========================================================================
     FUNCTION 2 DIAGNOSTICS — WINNING CONFIG: RATIONAL QUADRATIC + WHITENOISE
==========================================================================
Full Dataset Log Marginal Likelihood (LML)   : -18.882
Mean LOOCV Fold Log Marginal Likelihood      : -17.812
LOOCV Root Mean Squared Error (RMSE)         : 0.2068
LOOCV R-squared Score                        : 0.2587
Breusch-Pagan-like p-value (not stat. valid) : 0.07283
--------------------------------------------------------------------------
Learned Kernel Parameters:
RationalQuadratic(alpha=1e+05, length_scale=0.193) + WhiteKernel(noise_level=0.0023)
--------------------------------------------------------------------------
Verdict for Function 2 (15 datapoints, Week 5): HOMOSCEDASTIC
==========================================================================

==========================================================================
     FUNCTION 3 DIAGNOSTICS — WINNING CONFIG: RBF + WHITENOISE (SMOOTH GAUSSIAN)
==========================================================================
Full Dataset Log Marginal Likelihood (LML)   : -16.489
Mean LOOCV Fold Log Marginal Likelihood      : -16.143
LOOCV Root Mean Squared Error (RMSE)         : 0.0403
LOOCV R-squared Score                        : 0.7913
Breusch-Pagan-like p-value (not stat. valid) : 0.01474
--------------------------------------------------------------------------
Learned Kernel Parameters:
RBF(length_scale=[1e+04, 1e+04, 0.247]) + WhiteKernel(noise_level=0.0286)
--------------------------------------------------------------------------
Verdict for Function 3 (20 datapoints, Week 5): HETEROSCEDASTIC
==========================================================================

==========================================================================
     FUNCTION 4 DIAGNOSTICS — WINNING CONFIG: RATIONAL QUADRATIC + WHITENOISE
==========================================================================
Full Dataset Log Marginal Likelihood (LML)   : -20.586
Mean LOOCV Fold Log Marginal Likelihood      : -20.778
LOOCV Root Mean Squared Error (RMSE)         : 2.0588
LOOCV R-squared Score                        : 0.9325
Breusch-Pagan-like p-value (not stat. valid) : 0.00709
--------------------------------------------------------------------------
Learned Kernel Parameters:
RationalQuadratic(alpha=1.67, length_scale=2.25) + WhiteKernel(noise_level=0.00589)
--------------------------------------------------------------------------
Verdict for Function 4 (35 datapoints, Week 5): HETEROSCEDASTIC
==========================================================================

==========================================================================
     FUNCTION 5 DIAGNOSTICS — WINNING CONFIG: MATERN 2.5 WITHOUT WHITENOISE (NOISELESS)
==========================================================================
Full Dataset Log Marginal Likelihood (LML)   : -26.910
Mean LOOCV Fold Log Marginal Likelihood      : -25.869
LOOCV Root Mean Squared Error (RMSE)         : 130.1462
LOOCV R-squared Score                        : 0.8624
Breusch-Pagan-like p-value (not stat. valid) : 0.00003
--------------------------------------------------------------------------
Learned Kernel Parameters:
Matern(length_scale=[8.16, 0.893, 1.15, 0.528], nu=2.5)
--------------------------------------------------------------------------
Verdict for Function 5 (25 datapoints, Week 5): HETEROSCEDASTIC
==========================================================================

==========================================================================
     FUNCTION 6 DIAGNOSTICS — WINNING CONFIG: RATIONAL QUADRATIC + WHITENOISE
==========================================================================
Full Dataset Log Marginal Likelihood (LML)   : -26.575
Mean LOOCV Fold Log Marginal Likelihood      : -25.831
LOOCV Root Mean Squared Error (RMSE)         : 0.2818
LOOCV R-squared Score                        : 0.6887
Breusch-Pagan-like p-value (not stat. valid) : 0.20402
--------------------------------------------------------------------------
Learned Kernel Parameters:
RationalQuadratic(alpha=1.22, length_scale=1.94) + WhiteKernel(noise_level=0.0188)
--------------------------------------------------------------------------
Verdict for Function 6 (25 datapoints, Week 5): HOMOSCEDASTIC
==========================================================================

==========================================================================
     FUNCTION 7 DIAGNOSTICS — WINNING CONFIG: MATERN 2.5 WITHOUT WHITENOISE (NOISELESS)
==========================================================================
Full Dataset Log Marginal Likelihood (LML)   : -30.067
Mean LOOCV Fold Log Marginal Likelihood      : -29.615
LOOCV Root Mean Squared Error (RMSE)         : 0.1904
LOOCV R-squared Score                        : 0.7839
Breusch-Pagan-like p-value (not stat. valid) : 0.41671
--------------------------------------------------------------------------
Learned Kernel Parameters:
Matern(length_scale=[5.73, 3.42, 1e+04, 2.16, 0.761, 1.82], nu=2.5)
--------------------------------------------------------------------------
Verdict for Function 7 (35 datapoints, Week 5): HOMOSCEDASTIC
==========================================================================

==========================================================================
     FUNCTION 8 DIAGNOSTICS — WINNING CONFIG: MATERN 2.5 + WHITENOISE (ARD)
==========================================================================
Full Dataset Log Marginal Likelihood (LML)   : 2.440
Mean LOOCV Fold Log Marginal Likelihood      : 1.356
LOOCV Root Mean Squared Error (RMSE)         : 0.1539
LOOCV R-squared Score                        : 0.9803
Breusch-Pagan-like p-value (not stat. valid) : 0.14158
--------------------------------------------------------------------------
Learned Kernel Parameters:
Matern(length_scale=[4.16, 6.15, 3.33, 10.3, 17.2, 7.89e+03, 4.31, 1e+04], nu=2.5) + WhiteKernel(noise_level=1e-06)
--------------------------------------------------------------------------
Verdict for Function 8 (45 datapoints, Week 5): HOMOSCEDASTIC
==========================================================================
```
