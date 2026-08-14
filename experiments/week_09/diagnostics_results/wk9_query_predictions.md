_**Week 9 BBO Capstone Project**_

**Next Query Predictions For Functions 1-8**

```text
====================================================================================================
 [STEP 2] Executing Final HEBO-Based Next Query Predictions...
====================================================================================================

===================================================================================================================
 COMPILING FINAL HEBO & SOBOL-BASED NEXT QUERY PREDICTIONS ACROSS FUNCTIONS 1-8
===================================================================================================================
Function 1 | Next Query: [0.191877 0.449326] | Kernel: Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless) | Acq: Upper Confidence Bound (beta=2.58) | Predicted Value: 0.000000 | Pred Std (warped): 0.8398
Function 2 | Next Query: [0.728949 0.100912] | Kernel: Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise | Acq: Thompson Sampling    | Predicted Value: 0.521212 | Pred Std (warped): 0.6412
Function 3 | Next Query: [0.853375 0.364122 0.378225] | Kernel: Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise | Acq: Upper Confidence Bound (beta=0.5) | Predicted Value: -0.034769 | Pred Std (warped): 0.2229
Function 4 | Next Query: [0.431247 0.414915 0.382929 0.467884] | Kernel: Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise | Acq: Upper Confidence Bound (beta=0.5) | Predicted Value: -1.019527 | Pred Std (warped): 0.1204
Function 5 | Next Query: [0.826892 0.82409  0.873481 0.937759] | Kernel: Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky) | Acq: Upper Confidence Bound (beta=1.0) | Predicted Value: 2332.997418 | Pred Std (warped): 0.0012
Function 6 | Next Query: [0.427127 0.263496 0.675556 0.813551 0.076409] | Kernel: Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise | Acq: Upper Confidence Bound (beta=0.5) | Predicted Value: -0.287887 | Pred Std (warped): 0.1356
Function 7 | Next Query: [0.130562 0.2437   0.527783 0.406015 0.267176 0.798679] | Kernel: Ablation 3: Rational Quadratic + WhiteNoise | Acq: Upper Confidence Bound (beta=0.5) | Predicted Value: 2.313814 | Pred Std (warped): 0.3856
Function 8 | Next Query: [0.048728 0.19876  0.027573 0.165691 0.481095 0.46375  0.247159 0.709556] | Kernel: Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise | Acq: Probability of Improvement (xi=0.01) | Predicted Value: 10.098430 | Pred Std (warped): 0.1494
===================================================================================================================

====================================================================================================
 FINAL NEXT-QUERY SUMMARY
====================================================================================================
FUNCTION_1:
    Next Query Coordinates : [0.191877 0.449326]
    Kernel Used            : Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)
    Acquisition Used       : Upper Confidence Bound (beta=2.58)
    Predicted Value        : 0.000000
    Predicted Std (warped) : 0.8398
----------------------------------------------------------------------------------------------------
FUNCTION_2:
    Next Query Coordinates : [0.728949 0.100912]
    Kernel Used            : Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise
    Acquisition Used       : Thompson Sampling
    Predicted Value        : 0.521212
    Predicted Std (warped) : 0.6412
----------------------------------------------------------------------------------------------------
FUNCTION_3:
    Next Query Coordinates : [0.853375 0.364122 0.378225]
    Kernel Used            : Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : -0.034769
    Predicted Std (warped) : 0.2229
----------------------------------------------------------------------------------------------------
FUNCTION_4:
    Next Query Coordinates : [0.431247 0.414915 0.382929 0.467884]
    Kernel Used            : Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : -1.019527
    Predicted Std (warped) : 0.1204
----------------------------------------------------------------------------------------------------
FUNCTION_5:
    Next Query Coordinates : [0.826892 0.82409  0.873481 0.937759]
    Kernel Used            : Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)
    Acquisition Used       : Upper Confidence Bound (beta=1.0)
    Predicted Value        : 2332.997418
    Predicted Std (warped) : 0.0012
----------------------------------------------------------------------------------------------------
FUNCTION_6:
    Next Query Coordinates : [0.427127 0.263496 0.675556 0.813551 0.076409]
    Kernel Used            : Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : -0.287887
    Predicted Std (warped) : 0.1356
----------------------------------------------------------------------------------------------------
FUNCTION_7:
    Next Query Coordinates : [0.130562 0.2437   0.527783 0.406015 0.267176 0.798679]
    Kernel Used            : Ablation 3: Rational Quadratic + WhiteNoise
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : 2.313814
    Predicted Std (warped) : 0.3856
----------------------------------------------------------------------------------------------------
FUNCTION_8:
    Next Query Coordinates : [0.048728 0.19876  0.027573 0.165691 0.481095 0.46375  0.247159 0.709556]
    Kernel Used            : Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise
    Acquisition Used       : Probability of Improvement (xi=0.01)
    Predicted Value        : 10.098430
    Predicted Std (warped) : 0.1494
----------------------------------------------------------------------------------------------------

====================================================================================================
                    WEEK 09 BBO PIPELINE: ALL TASKS COMPLETED SUCCESSFULLY
====================================================================================================
```
