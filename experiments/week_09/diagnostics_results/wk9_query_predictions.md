_**Week 9 BBO Capstone Project**_

**Next Query Predictions For Functions 1-8**

```text
====================================================================================================
 [STEP 2] Executing Final HEBO-Based Next Query Predictions (GP-only)...
====================================================================================================

===================================================================================================================
 COMPILING FINAL HEBO & SOBOL-BASED NEXT QUERY PREDICTIONS ACROSS FUNCTIONS 1-8
===================================================================================================================
Function 1 | Next Query: [0.177698 0.446721] | Kernel: Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless) | Acq: Upper Confidence Bound (beta=2.58) | Predicted Value: 0.000000 | Pred Std (warped): 0.8465
Function 2 | Next Query: [0.231846 0.465131] | Kernel: Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise | Acq: Thompson Sampling    | Predicted Value: 0.136107 | Pred Std (warped): 1.0963
Function 3 | Next Query: [0.176732 0.765677 0.378288] | Kernel: Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise | Acq: Upper Confidence Bound (beta=0.5) | Predicted Value: -0.034770 | Pred Std (warped): 0.2230
Function 4 | Next Query: [0.392974 0.405785 0.33596  0.406421] | Kernel: Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise | Acq: Upper Confidence Bound (beta=0.5) | Predicted Value: -1.054739 | Pred Std (warped): 0.1304
Function 5 | Next Query: [0.831048 0.737492 0.858515 0.955716] | Kernel: Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky) | Acq: Upper Confidence Bound (beta=1.0) | Predicted Value: 1703.469591 | Pred Std (warped): 0.2280
Function 6 | Next Query: [0.44012  0.335949 0.603401 0.789098 0.148306] | Kernel: Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise | Acq: Upper Confidence Bound (beta=0.5) | Predicted Value: -0.285626 | Pred Std (warped): 0.1539
Function 7 | Next Query: [0.277495 0.142918 0.398352 0.358725 0.314242 0.725117] | Kernel: Ablation 3: Rational Quadratic + WhiteNoise | Acq: Upper Confidence Bound (beta=0.5) | Predicted Value: 2.140851 | Pred Std (warped): 0.4300
Function 8 | Next Query: [0.013515 0.138607 0.077065 0.257731 0.618343 0.550669 0.411462 0.574856] | Kernel: Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise | Acq: Probability of Improvement (xi=0.01) | Predicted Value: 10.085526 | Pred Std (warped): 0.1460
===================================================================================================================

====================================================================================================
 FINAL NEXT-QUERY SUMMARY
====================================================================================================
FUNCTION_1:
    Next Query Coordinates : [0.177698 0.446721]
    Kernel Used            : Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)
    Acquisition Used       : Upper Confidence Bound (beta=2.58)
    Predicted Value        : 8.007451033284186e-45
    Predicted Std (warped) : 0.8465
----------------------------------------------------------------------------------------------------
FUNCTION_2:
    Next Query Coordinates : [0.231846 0.465131]
    Kernel Used            : Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise
    Acquisition Used       : Thompson Sampling
    Predicted Value        : 0.13610723000067804
    Predicted Std (warped) : 1.0963
----------------------------------------------------------------------------------------------------
FUNCTION_3:
    Next Query Coordinates : [0.176732 0.765677 0.378288]
    Kernel Used            : Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : -0.03476998478022386
    Predicted Std (warped) : 0.2230
----------------------------------------------------------------------------------------------------
FUNCTION_4:
    Next Query Coordinates : [0.392974 0.405785 0.33596  0.406421]
    Kernel Used            : Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : -1.0547390714815728
    Predicted Std (warped) : 0.1304
----------------------------------------------------------------------------------------------------
FUNCTION_5:
    Next Query Coordinates : [0.831048 0.737492 0.858515 0.955716]
    Kernel Used            : Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)
    Acquisition Used       : Upper Confidence Bound (beta=1.0)
    Predicted Value        : 1703.4695912021969
    Predicted Std (warped) : 0.2280
----------------------------------------------------------------------------------------------------
FUNCTION_6:
    Next Query Coordinates : [0.44012  0.335949 0.603401 0.789098 0.148306]
    Kernel Used            : Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : -0.2856255201565412
    Predicted Std (warped) : 0.1539
----------------------------------------------------------------------------------------------------
FUNCTION_7:
    Next Query Coordinates : [0.277495 0.142918 0.398352 0.358725 0.314242 0.725117]
    Kernel Used            : Ablation 3: Rational Quadratic + WhiteNoise
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : 2.140851049586575
    Predicted Std (warped) : 0.4300
----------------------------------------------------------------------------------------------------
FUNCTION_8:
    Next Query Coordinates : [0.013515 0.138607 0.077065 0.257731 0.618343 0.550669 0.411462 0.574856]
    Kernel Used            : Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise
    Acquisition Used       : Probability of Improvement (xi=0.01)
    Predicted Value        : 10.085525562828632
    Predicted Std (warped) : 0.1460
----------------------------------------------------------------------------------------------------

====================================================================================================
                    WEEK 09 BBO PIPELINE: ALL TASKS COMPLETED SUCCESSFULLY
====================================================================================================
```
