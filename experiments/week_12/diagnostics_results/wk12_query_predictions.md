**Next-Query PRedictions Submitted for Week 12 (Penultimate Week) of the Black-Box Optimisation Project**

```text
====================================================================================================
 FINAL NEXT-QUERY SUMMARY
====================================================================================================
FUNCTION_1:
    Next Query Coordinates : [0.358419 0.733623]
    Kernel Used            : Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise
    Acquisition Used       : Probability of Improvement (xi=0.01)
    Predicted Value        : 6.5945841980038e-10
    Predicted Std (warped) : 0.0050
    Chosen From Pool       : local-box (full-domain candidates: 4096, local-box candidates: 8192)
    Box Volume Ratio       : 27.9607% of full domain
    Best Score (full-domain / local-box): 0.989902 / 0.990557
    Full-domain best candidate  : coords=[0.575911 0.733666] | predicted value=8.301384199926113e-10 | predicted std=0.0067
    Local-box best candidate    : coords=[0.358419 0.733623] | predicted value=6.5945841980038e-10 | predicted std=0.0050
----------------------------------------------------------------------------------------------------
FUNCTION_2:
    Next Query Coordinates : [0.714214 0.698559]
    Kernel Used            : Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)
    Acquisition Used       : Probability of Improvement (xi=0.1)
    Predicted Value        : 0.6310740093869494
    Predicted Std (warped) : 0.5052
    Chosen From Pool       : local-box (full-domain candidates: 4096, local-box candidates: 4096)
    Box Volume Ratio       : 19.5282% of full domain
    Best Score (full-domain / local-box): 0.206343 / 0.206344
    Full-domain best candidate  : coords=[0.714127 0.225744] | predicted value=0.631113 | predicted std=0.5051
    Local-box best candidate    : coords=[0.714214 0.698559] | predicted value=0.631074 | predicted std=0.5052
----------------------------------------------------------------------------------------------------
FUNCTION_3:
    Next Query Coordinates : [0.963158 0.853901 0.378722]
    Kernel Used            : Baseline: Matern 2.5 + WhiteNoise (ARD)
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : -0.02602021695424206
    Predicted Std (warped) : 0.2032
    Chosen From Pool       : local-box (full-domain candidates: 4096, local-box candidates: 16384)
    Box Volume Ratio       : 61.9305% of full domain
    Best Score (full-domain / local-box): 1.497426 / 1.502765
    Full-domain best candidate  : coords=[0.928797 0.32869  0.37833 ] | predicted value=-0.026154 | predicted std=0.2013
    Local-box best candidate    : coords=[0.963158 0.853901 0.378722] | predicted value=-0.026020 | predicted std=0.2032
----------------------------------------------------------------------------------------------------
FUNCTION_4:
    Next Query Coordinates : [0.357364 0.379669 0.334667 0.417004]
    Kernel Used            : Ablation 3: Rational Quadratic + WhiteNoise
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : -0.061768205812961385
    Predicted Std (warped) : 0.1117
    Chosen From Pool       : local-box (full-domain candidates: 8192, local-box candidates: 16384)
    Box Volume Ratio       : 49.9973% of full domain
    Best Score (full-domain / local-box): 1.822518 / 1.844477
    Full-domain best candidate  : coords=[0.366761 0.402593 0.319079 0.384426] | predicted value=-0.163723 | predicted std=0.1131
    Local-box best candidate    : coords=[0.357364 0.379669 0.334667 0.417004] | predicted value=-0.061768 | predicted std=0.1117
----------------------------------------------------------------------------------------------------
FUNCTION_5:
    Next Query Coordinates : [0.567349 0.86235  0.853409 0.740108]
    Kernel Used            : Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)
    Acquisition Used       : Thompson Sampling
    Predicted Value        : 740.9863089113692
    Predicted Std (warped) : 0.2911
    Chosen From Pool       : full-domain (full-domain candidates: 8192, local-box candidates: 4096)
    Box Volume Ratio       : 10.3912% of full domain
    Best Score (full-domain / local-box): 1.690959 / 1.523104
    Full-domain best candidate  : coords=[0.567349 0.86235  0.853409 0.740108] | predicted value=740.986309 | predicted std=0.2911
    Local-box best candidate    : coords=[0.737871 0.836873 0.875186 0.940624] | predicted value=2119.338560 | predicted std=0.0418
----------------------------------------------------------------------------------------------------
FUNCTION_6:
    Next Query Coordinates : [0.4164   0.362244 0.606464 0.816435 0.207588]
    Kernel Used            : Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : -0.24363300721559922
    Predicted Std (warped) : 0.1368
    Chosen From Pool       : local-box (full-domain candidates: 8192, local-box candidates: 16384)
    Box Volume Ratio       : 30.6506% of full domain
    Best Score (full-domain / local-box): 1.623602 / 1.664141
    Full-domain best candidate  : coords=[0.478461 0.374718 0.572271 0.747668 0.215243] | predicted value=-0.263679 | predicted std=0.1305
    Local-box best candidate    : coords=[0.4164   0.362244 0.606464 0.816435 0.207588] | predicted value=-0.243633 | predicted std=0.1368
----------------------------------------------------------------------------------------------------
FUNCTION_7:
    Next Query Coordinates : [0.203662 0.23191  0.316101 0.200651 0.260254 0.638377]
    Kernel Used            : Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise
    Acquisition Used       : Expected Improvement (xi=0.001)
    Predicted Value        : 2.5934032598696595
    Predicted Std (warped) : 0.2785
    Chosen From Pool       : local-box (full-domain candidates: 16384, local-box candidates: 32768)
    Box Volume Ratio       : 27.8226% of full domain
    Best Score (full-domain / local-box): 0.059245 / 0.074759
    Full-domain best candidate  : coords=[0.34492  0.171805 0.427944 0.151805 0.287644 0.664089] | predicted value=2.235113 | predicted std=0.3237
    Local-box best candidate    : coords=[0.203662 0.23191  0.316101 0.200651 0.260254 0.638377] | predicted value=2.593403 | predicted std=0.2785
----------------------------------------------------------------------------------------------------
FUNCTION_8:
    Next Query Coordinates : [0.030407 0.014844 0.175073 0.283089 0.912311 0.367875 0.243127 0.527953]
    Kernel Used            : Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : 9.950026917647417
    Predicted Std (warped) : 0.0539
    Chosen From Pool       : local-box (full-domain candidates: 16384, local-box candidates: 8192)
    Box Volume Ratio       : 8.1661% of full domain
    Best Score (full-domain / local-box): 1.523816 / 1.532829
    Full-domain best candidate  : coords=[0.124368 0.152845 0.130169 0.086871 0.784312 0.504132 0.188381 0.527319] | predicted value=9.952083 | predicted std=0.0320
    Local-box best candidate    : coords=[0.030407 0.014844 0.175073 0.283089 0.912311 0.367875 0.243127 0.527953] | predicted value=9.950027 | predicted std=0.0539
----------------------------------------------------------------------------------------------------
```
