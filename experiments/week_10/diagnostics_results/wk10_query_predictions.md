**Week 10 BBO Capstone Project**

**Next Query Predictions For Functions 1-8**

```text
====================================================================================================
 [STEP 2] Executing Final HEBO-Based Next Query Predictions (GP-only)...
====================================================================================================

===================================================================================================================
 COMPILING FINAL HEBO & SOBOL-BASED NEXT QUERY PREDICTIONS ACROSS FUNCTIONS 1-8
===================================================================================================================
Function 1 | Next Query: [0.584965 0.733487] | Kernel: Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise | Acq: Probability of Improvement (xi=0.01) | Predicted Value: 0.000000 | Pred Std (warped): 0.1174
Function 2 | Next Query: [0.689113 0.397611] | Kernel: Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky) | Acq: Upper Confidence Bound (beta=2.58) | Predicted Value: 0.594681 | Pred Std (warped): 0.5902
Function 3 | Next Query: [0.546056 0.816106 0.377222] | Kernel: Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky) | Acq: Upper Confidence Bound (beta=0.5) | Predicted Value: -0.030757 | Pred Std (warped): 0.2227
Function 4 | Next Query: [0.410114 0.432907 0.358436 0.425839] | Kernel: Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise | Acq: Upper Confidence Bound (beta=0.5) | Predicted Value: -0.480863 | Pred Std (warped): 0.1038
Function 5 | Next Query: [0.217004 0.090711 0.117054 0.753255] | Kernel: Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise | Acq: Thompson Sampling    | Predicted Value: 354.259385 | Pred Std (warped): 0.6144
Function 6 | Next Query: [0.488983 0.342134 0.589925 0.773329 0.175729] | Kernel: Ablation 3: Rational Quadratic + WhiteNoise | Acq: Upper Confidence Bound (beta=0.5) | Predicted Value: -0.217290 | Pred Std (warped): 0.0948
Function 7 | Next Query: [0.260923 0.182894 0.51157  0.356937 0.235955 0.892622] | Kernel: Ablation 3: Rational Quadratic + WhiteNoise | Acq: Upper Confidence Bound (beta=1.0) | Predicted Value: 2.666887 | Pred Std (warped): 0.2589
Function 8 | Next Query: [0.059034 0.188108 0.070117 0.206863 0.95846  0.21822  0.371424 0.596697] | Kernel: Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky) | Acq: Upper Confidence Bound (beta=0.5) | Predicted Value: 10.010636 | Pred Std (warped): 0.0596
===================================================================================================================

====================================================================================================
 FINAL NEXT-QUERY SUMMARY
====================================================================================================
FUNCTION_1:
    Next Query Coordinates : [0.584965 0.733487]
    Kernel Used            : Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise
    Acquisition Used       : Probability of Improvement (xi=0.01)
    Predicted Value        : 2.724113098955348e-16
    Predicted Std (warped) : 0.1174
----------------------------------------------------------------------------------------------------
FUNCTION_2:
    Next Query Coordinates : [0.689113 0.397611]
    Kernel Used            : Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)
    Acquisition Used       : Upper Confidence Bound (beta=2.58)
    Predicted Value        : 0.5946811472173572
    Predicted Std (warped) : 0.5902
----------------------------------------------------------------------------------------------------
FUNCTION_3:
    Next Query Coordinates : [0.546056 0.816106 0.377222]
    Kernel Used            : Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : -0.03075686128451527
    Predicted Std (warped) : 0.2227
----------------------------------------------------------------------------------------------------
FUNCTION_4:
    Next Query Coordinates : [0.410114 0.432907 0.358436 0.425839]
    Kernel Used            : Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : -0.48086343578075286
    Predicted Std (warped) : 0.1038
----------------------------------------------------------------------------------------------------
FUNCTION_5:
    Next Query Coordinates : [0.217004 0.090711 0.117054 0.753255]
    Kernel Used            : Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise
    Acquisition Used       : Thompson Sampling
    Predicted Value        : 354.25938497737775
    Predicted Std (warped) : 0.6144
----------------------------------------------------------------------------------------------------
FUNCTION_6:
    Next Query Coordinates : [0.488983 0.342134 0.589925 0.773329 0.175729]
    Kernel Used            : Ablation 3: Rational Quadratic + WhiteNoise
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : -0.21728960253873142
    Predicted Std (warped) : 0.0948
----------------------------------------------------------------------------------------------------
FUNCTION_7:
    Next Query Coordinates : [0.260923 0.182894 0.51157  0.356937 0.235955 0.892622]
    Kernel Used            : Ablation 3: Rational Quadratic + WhiteNoise
    Acquisition Used       : Upper Confidence Bound (beta=1.0)
    Predicted Value        : 2.666886556810939
    Predicted Std (warped) : 0.2589
----------------------------------------------------------------------------------------------------
FUNCTION_8:
    Next Query Coordinates : [0.059034 0.188108 0.070117 0.206863 0.95846  0.21822  0.371424 0.596697]
    Kernel Used            : Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : 10.010635750015311
    Predicted Std (warped) : 0.0596
----------------------------------------------------------------------------------------------------
```
