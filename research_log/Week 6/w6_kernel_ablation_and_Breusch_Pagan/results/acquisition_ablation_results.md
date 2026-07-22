**Week 6 BBO - Acquisition Ablation Study Results (Pre-Query 6th Prediction Generation)**
```text
=========================================================================================================
       FUNCTION 1 (Dim=2, N=15) — LOOCV ACQUISITION ABLATION STUDY
=========================================================================================================
     Acquisition Variant  Mean LOOCV Rank Percentile (%)  Median LOOCV Rank Percentile (%)  Std Dev (%)
            EI (xi=0.01)                          100.00                            100.00         0.00
EI (Exploration, xi=0.1)                          100.00                            100.00         0.00
         UCB (beta=2.58)                          100.00                            100.00         0.00
         UCB (beta=1.96)                           98.10                            100.00         4.86
            PI (xi=0.01)                           92.86                             92.86         0.00
---------------------------------------------------------------------------------------------------------
==========================================================================
     FUNCTION 1 SUMMARY — BEST KERNEL & ACQUISITION CONFIG
==========================================================================
Best Kernel Variant (Kernel Ablation) : RBF + WHITENOISE (SMOOTH GAUSSIAN)
Kernel Ablation LOOCV R² Score        : 0.25498
--------------------------------------------------------------------------
Learned Kernel Parameters:
RBF(length_scale=[3.85e+03, 0.0804]) + WhiteKernel(noise_level=7.45e-09)
--------------------------------------------------------------------------
Winning Acquisition Strategy          : EI (xi=0.01)
Mean LOOCV Rank Percentile            : 100.0%
==========================================================================

=========================================================================================================
       FUNCTION 2 (Dim=2, N=15) — LOOCV ACQUISITION ABLATION STUDY
=========================================================================================================
     Acquisition Variant  Mean LOOCV Rank Percentile (%)  Median LOOCV Rank Percentile (%)  Std Dev (%)
EI (Exploration, xi=0.1)                          100.00                            100.00         0.00
         UCB (beta=2.58)                          100.00                            100.00         0.00
         UCB (beta=1.96)                           99.05                            100.00         2.43
            EI (xi=0.01)                           98.57                            100.00         2.86
            PI (xi=0.01)                           95.24                             92.86         4.26
---------------------------------------------------------------------------------------------------------
==========================================================================
     FUNCTION 2 SUMMARY — BEST KERNEL & ACQUISITION CONFIG
==========================================================================
Best Kernel Variant (Kernel Ablation) : RATIONAL QUADRATIC + WHITENOISE
Kernel Ablation LOOCV R² Score        : 0.25867
--------------------------------------------------------------------------
Learned Kernel Parameters:
RationalQuadratic(alpha=1e+05, length_scale=0.193) + WhiteKernel(noise_level=0.0023)
--------------------------------------------------------------------------
Winning Acquisition Strategy          : EI (Exploration, xi=0.1)
Mean LOOCV Rank Percentile            : 100.0%
==========================================================================

=========================================================================================================
       FUNCTION 3 (Dim=3, N=20) — LOOCV ACQUISITION ABLATION STUDY
=========================================================================================================
     Acquisition Variant  Mean LOOCV Rank Percentile (%)  Median LOOCV Rank Percentile (%)  Std Dev (%)
EI (Exploration, xi=0.1)                           65.79                             73.68        34.05
            EI (xi=0.01)                           63.68                             65.79        31.97
            PI (xi=0.01)                           60.53                             63.16        29.80
         UCB (beta=1.96)                           58.42                             60.53        33.57
         UCB (beta=2.58)                           58.42                             60.53        33.57
---------------------------------------------------------------------------------------------------------
==========================================================================
     FUNCTION 3 SUMMARY — BEST KERNEL & ACQUISITION CONFIG
==========================================================================
Best Kernel Variant (Kernel Ablation) : RBF + WHITENOISE (SMOOTH GAUSSIAN)
Kernel Ablation LOOCV R² Score        : 0.79129
--------------------------------------------------------------------------
Learned Kernel Parameters:
RBF(length_scale=[1e+04, 1e+04, 0.247]) + WhiteKernel(noise_level=0.0286)
--------------------------------------------------------------------------
Winning Acquisition Strategy          : EI (Exploration, xi=0.1)
Mean LOOCV Rank Percentile            : 65.79%
==========================================================================

=========================================================================================================
       FUNCTION 4 (Dim=4, N=35) — LOOCV ACQUISITION ABLATION STUDY
=========================================================================================================
     Acquisition Variant  Mean LOOCV Rank Percentile (%)  Median LOOCV Rank Percentile (%)  Std Dev (%)
            EI (xi=0.01)                           83.87                             88.24        14.00
EI (Exploration, xi=0.1)                           83.87                             88.24        14.00
            PI (xi=0.01)                           83.53                             88.24        13.89
         UCB (beta=2.58)                           63.70                             73.53        25.73
         UCB (beta=1.96)                           60.84                             73.53        26.23
---------------------------------------------------------------------------------------------------------
==========================================================================
     FUNCTION 4 SUMMARY — BEST KERNEL & ACQUISITION CONFIG
==========================================================================
Best Kernel Variant (Kernel Ablation) : RATIONAL QUADRATIC + WHITENOISE
Kernel Ablation LOOCV R² Score        : 0.9325
--------------------------------------------------------------------------
Learned Kernel Parameters:
RationalQuadratic(alpha=1.67, length_scale=2.25) + WhiteKernel(noise_level=0.00589)
--------------------------------------------------------------------------
Winning Acquisition Strategy          : EI (xi=0.01)
Mean LOOCV Rank Percentile            : 83.87%
==========================================================================

=========================================================================================================
       FUNCTION 5 (Dim=4, N=25) — LOOCV ACQUISITION ABLATION STUDY
=========================================================================================================
     Acquisition Variant  Mean LOOCV Rank Percentile (%)  Median LOOCV Rank Percentile (%)  Std Dev (%)
            EI (xi=0.01)                          100.00                            100.00         0.00
EI (Exploration, xi=0.1)                          100.00                            100.00         0.00
            PI (xi=0.01)                          100.00                            100.00         0.00
         UCB (beta=2.58)                           91.50                             91.67         2.76
         UCB (beta=1.96)                           89.67                             91.67         4.73
---------------------------------------------------------------------------------------------------------
==========================================================================
     FUNCTION 5 SUMMARY — BEST KERNEL & ACQUISITION CONFIG
==========================================================================
Best Kernel Variant (Kernel Ablation) : MATERN 2.5 WITHOUT WHITENOISE (NOISELESS)
Kernel Ablation LOOCV R² Score        : 0.86237
--------------------------------------------------------------------------
Learned Kernel Parameters:
Matern(length_scale=[8.16, 0.893, 1.15, 0.528], nu=2.5)
--------------------------------------------------------------------------
Winning Acquisition Strategy          : EI (xi=0.01)
Mean LOOCV Rank Percentile            : 100.0%
==========================================================================

=========================================================================================================
       FUNCTION 6 (Dim=5, N=25) — LOOCV ACQUISITION ABLATION STUDY
=========================================================================================================
     Acquisition Variant  Mean LOOCV Rank Percentile (%)  Median LOOCV Rank Percentile (%)  Std Dev (%)
EI (Exploration, xi=0.1)                           93.67                             95.83         5.67
            EI (xi=0.01)                           92.17                             95.83         6.80
            PI (xi=0.01)                           91.67                             91.67         6.67
         UCB (beta=2.58)                           80.67                             87.50        18.29
         UCB (beta=1.96)                           74.83                             83.33        20.97
---------------------------------------------------------------------------------------------------------
==========================================================================
     FUNCTION 6 SUMMARY — BEST KERNEL & ACQUISITION CONFIG
==========================================================================
Best Kernel Variant (Kernel Ablation) : RATIONAL QUADRATIC + WHITENOISE
Kernel Ablation LOOCV R² Score        : 0.68873
--------------------------------------------------------------------------
Learned Kernel Parameters:
RationalQuadratic(alpha=1.22, length_scale=1.94) + WhiteKernel(noise_level=0.0188)
--------------------------------------------------------------------------
Winning Acquisition Strategy          : EI (Exploration, xi=0.1)
Mean LOOCV Rank Percentile            : 93.67%
==========================================================================

=========================================================================================================
       FUNCTION 7 (Dim=6, N=35) — LOOCV ACQUISITION ABLATION STUDY
=========================================================================================================
     Acquisition Variant  Mean LOOCV Rank Percentile (%)  Median LOOCV Rank Percentile (%)  Std Dev (%)
            EI (xi=0.01)                          100.00                            100.00         0.00
EI (Exploration, xi=0.1)                          100.00                            100.00         0.00
            PI (xi=0.01)                          100.00                            100.00         0.00
         UCB (beta=2.58)                           85.46                             91.18        10.07
         UCB (beta=1.96)                           81.93                             85.29        11.19
---------------------------------------------------------------------------------------------------------
==========================================================================
     FUNCTION 7 SUMMARY — BEST KERNEL & ACQUISITION CONFIG
==========================================================================
Best Kernel Variant (Kernel Ablation) : MATERN 2.5 WITHOUT WHITENOISE (NOISELESS)
Kernel Ablation LOOCV R² Score        : 0.78395
--------------------------------------------------------------------------
Learned Kernel Parameters:
Matern(length_scale=[5.73, 3.42, 1e+04, 2.16, 0.761, 1.82], nu=2.5)
--------------------------------------------------------------------------
Winning Acquisition Strategy          : EI (xi=0.01)
Mean LOOCV Rank Percentile            : 100.0%
==========================================================================

=========================================================================================================
       FUNCTION 8 (Dim=8, N=45) — LOOCV ACQUISITION ABLATION STUDY
=========================================================================================================
     Acquisition Variant  Mean LOOCV Rank Percentile (%)  Median LOOCV Rank Percentile (%)  Std Dev (%)
EI (Exploration, xi=0.1)                           94.39                            100.00        21.77
            EI (xi=0.01)                           92.73                             97.73        21.36
            PI (xi=0.01)                           92.68                             97.73        21.34
         UCB (beta=2.58)                           58.89                             54.55        27.59
         UCB (beta=1.96)                           56.72                             54.55        28.53
---------------------------------------------------------------------------------------------------------
==========================================================================
     FUNCTION 8 SUMMARY — BEST KERNEL & ACQUISITION CONFIG
==========================================================================
Best Kernel Variant (Kernel Ablation) : MATERN 2.5 + WHITENOISE (ARD)
Kernel Ablation LOOCV R² Score        : 0.98034
--------------------------------------------------------------------------
Learned Kernel Parameters:
Matern(length_scale=[4.16, 6.15, 3.33, 10.3, 17.2, 7.89e+03, 4.31, 1e+04], nu=2.5) + WhiteKernel(noise_level=1e-06)
--------------------------------------------------------------------------
Winning Acquisition Strategy          : EI (Exploration, xi=0.1)
Mean LOOCV Rank Percentile            : 94.39%
==========================================================================
```
