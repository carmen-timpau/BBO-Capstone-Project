**Week 11 BBO Capstone Project**

**Next Query Predictions For Functions 1-8**

```text
====================================================================================================
 FINAL NEXT-QUERY SUMMARY
====================================================================================================
FUNCTION_1:
    Next Query Coordinates : [0.520357 0.734594]
    Kernel Used            : Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise
    Acquisition Used       : Probability of Improvement (xi=0.01)
    Predicted Value        : 2.0073350587367645e-08
    Predicted Std (warped) : 0.2354
    Chosen From Pool       : local-box (full-domain candidates: 4096, local-box candidates: 16384)
    Box Volume Ratio       : 69.8074% of full domain
    Best Score (full-domain / local-box): 0.593669 / 0.594729
    Full-domain best candidate  : coords=[0.592846 0.7345  ] | predicted value=1.5290368326355708e-08 | predicted std=0.2215
    Local-box best candidate    : coords=[0.520357 0.734594] | predicted value=2.0073350587367645e-08 | predicted std=0.2354
----------------------------------------------------------------------------------------------------
FUNCTION_2:
    Next Query Coordinates : [0.726875 0.671348]
    Kernel Used            : Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)
    Acquisition Used       : Upper Confidence Bound (beta=2.58)
    Predicted Value        : 0.5479280152001755
    Predicted Std (warped) : 0.6176
    Chosen From Pool       : local-box (full-domain candidates: 4096, local-box candidates: 4096)
    Box Volume Ratio       : 17.2769% of full domain
    Best Score (full-domain / local-box): 2.650532 / 2.650533
    Full-domain best candidate  : coords=[0.726917 0.873062] | predicted value=0.547678 | predicted std=0.6179
    Local-box best candidate    : coords=[0.726875 0.671348] | predicted value=0.547928 | predicted std=0.6176
----------------------------------------------------------------------------------------------------
FUNCTION_3:
    Next Query Coordinates : [0.904318 0.73297  0.377777]
    Kernel Used            : Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : -0.031074734156167905
    Predicted Std (warped) : 0.1922
    Chosen From Pool       : full-domain (full-domain candidates: 4096, local-box candidates: 4096)
    Box Volume Ratio       : 19.0264% of full domain
    Best Score (full-domain / local-box): 1.457346 / 1.457346
    Full-domain best candidate  : coords=[0.904318 0.73297  0.377777] | predicted value=-0.031075 | predicted std=0.1922
    Local-box best candidate    : coords=[0.226023 0.791099 0.377807] | predicted value=-0.031075 | predicted std=0.1922
----------------------------------------------------------------------------------------------------
FUNCTION_4:
    Next Query Coordinates : [0.37963  0.389934 0.333318 0.413373]
    Kernel Used            : Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : -0.1600281957376941
    Predicted Std (warped) : 0.1225
    Chosen From Pool       : local-box (full-domain candidates: 8192, local-box candidates: 32768)
    Box Volume Ratio       : 57.0845% of full domain
    Best Score (full-domain / local-box): 1.850273 / 1.909989
    Full-domain best candidate  : coords=[0.405376 0.374028 0.400893 0.479229] | predicted value=-0.476494 | predicted std=0.1347
    Local-box best candidate    : coords=[0.37963  0.389934 0.333318 0.413373] | predicted value=-0.160028 | predicted std=0.1225
----------------------------------------------------------------------------------------------------
FUNCTION_5:
    Next Query Coordinates : [0.833443 0.828832 0.868668 0.918875]
    Kernel Used            : Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise
    Acquisition Used       : Thompson Sampling
    Predicted Value        : 2213.842770522163
    Predicted Std (warped) : 0.0282
    Chosen From Pool       : full-domain (full-domain candidates: 8192, local-box candidates: 4096)
    Box Volume Ratio       : 10.3912% of full domain
    Best Score (full-domain / local-box): 1.600270 / 1.559090
    Full-domain best candidate  : coords=[0.833443 0.828832 0.868668 0.918875] | predicted value=2213.842771 | predicted std=0.0282
    Local-box best candidate    : coords=[0.786466 0.74081  0.855875 0.765086] | predicted value=692.128327 | predicted std=0.2523
----------------------------------------------------------------------------------------------------
FUNCTION_6:
    Next Query Coordinates : [0.453242 0.267177 0.633438 0.710049 0.184406]
    Kernel Used            : Ablation 3: Rational Quadratic + WhiteNoise
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : -0.21050568541096215
    Predicted Std (warped) : 0.0809
    Chosen From Pool       : local-box (full-domain candidates: 8192, local-box candidates: 16384)
    Box Volume Ratio       : 30.6506% of full domain
    Best Score (full-domain / local-box): 1.692526 / 1.752689
    Full-domain best candidate  : coords=[0.41841  0.373988 0.677477 0.765832 0.065707] | predicted value=-0.254949 | predicted std=0.1218
    Local-box best candidate    : coords=[0.453242 0.267177 0.633438 0.710049 0.184406] | predicted value=-0.210506 | predicted std=0.0809
----------------------------------------------------------------------------------------------------
FUNCTION_7:
    Next Query Coordinates : [0.119465 0.167786 0.410458 0.23276  0.363744 0.765572]
    Kernel Used            : Ablation 6: RBF Isotropic (Shared Lengthscale 0.5) + WhiteNoise
    Acquisition Used       : Probability of Improvement (xi=0.01)
    Predicted Value        : 3.1159116548742354
    Predicted Std (warped) : 0.1515
    Chosen From Pool       : local-box (full-domain candidates: 16384, local-box candidates: 16384)
    Box Volume Ratio       : 14.9594% of full domain
    Best Score (full-domain / local-box): 0.511243 / 0.577153
    Full-domain best candidate  : coords=[0.233183 0.193618 0.47923  0.258554 0.42337  0.721583] | predicted value=3.006166 | predicted std=0.1821
    Local-box best candidate    : coords=[0.119465 0.167786 0.410458 0.23276  0.363744 0.765572] | predicted value=3.115912 | predicted std=0.1515
----------------------------------------------------------------------------------------------------
FUNCTION_8:
    Next Query Coordinates : [0.169129 0.094089 0.179808 0.020334 0.94492  0.5084   0.183455 0.630586]
    Kernel Used            : Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)
    Acquisition Used       : Upper Confidence Bound (beta=0.5)
    Predicted Value        : 9.990785757668684
    Predicted Std (warped) : 0.0553
    Chosen From Pool       : local-box (full-domain candidates: 16384, local-box candidates: 8192)
    Box Volume Ratio       : 8.1661% of full domain
    Best Score (full-domain / local-box): 1.597805 / 1.618031
    Full-domain best candidate  : coords=[0.038263 0.039366 0.051224 0.14222  0.929795 0.619814 0.193716 0.135933] | predicted value=9.958879 | predicted std=0.0752
    Local-box best candidate    : coords=[0.169129 0.094089 0.179808 0.020334 0.94492  0.5084   0.183455 0.630586] | predicted value=9.990786 | predicted std=0.0553
----------------------------------------------------------------------------------------------------
```
