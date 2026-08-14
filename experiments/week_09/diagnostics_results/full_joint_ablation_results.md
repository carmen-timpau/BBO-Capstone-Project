**Week 9 BBO Capstone Project**

**Full Joint Gaussian Process Surrogate Model Kernel x Acquisition Function Ablation Study Results**

```text
====================================================================================================
                    WEEK 09 BBO PIPELINE: EXECUTION & EVALUATION START
====================================================================================================

====================================================================================================
 [STEP 1] Running FULL JOINT Kernel x Acquisition Rollout Ablation Study...
====================================================================================================
Running Function 1: 18 samples, 2D -> n_init=5, 3 iterations (holdout_fraction=0.3, 10 points held out) x 20 seeds x 8 kernels x 11 strategies (1760 total rollouts)...
=======================================================================================================================================
        FUNCTION 1 — FULL JOINT KERNEL x ACQUISITION SWEEP (N_seeds=20, n_init=5)
=======================================================================================================================================
                                                   Kernel                  Acquisition Variant  Mean Best Value Found  Mean Final Regret  Median Final Regret  Std Final Regret  Mean AURC (Convergence Speed)
    Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)   Upper Confidence Bound (beta=2.58)               -19.0975             3.9846               0.0000            8.5096                        21.5220
           Ablation 2: RBF + WhiteNoise (Smooth Gaussian)   Upper Confidence Bound (beta=2.58)               -19.1347             4.0218               2.6447            6.7305                        15.3245
              Ablation 3: Rational Quadratic + WhiteNoise    Upper Confidence Bound (beta=0.5)               -19.2031             4.0902               0.0000            8.2397                        19.6092
              Ablation 3: Rational Quadratic + WhiteNoise  Probability of Improvement (xi=0.1)               -19.2031             4.0902               0.0000            8.2397                        19.6092
              Ablation 3: Rational Quadratic + WhiteNoise Probability of Improvement (xi=0.01)               -19.2031             4.0902               0.0000            8.2397                        19.6092
              Ablation 3: Rational Quadratic + WhiteNoise      Expected Improvement (xi=0.001)               -19.2031             4.0902               0.0000            8.2397                        19.7071
              Ablation 3: Rational Quadratic + WhiteNoise       Expected Improvement (xi=0.01)               -19.2031             4.0902               0.0000            8.2397                        19.7071
              Ablation 3: Rational Quadratic + WhiteNoise        Expected Improvement (xi=0.1)               -19.2031             4.0902               0.0000            8.2397                        19.7071
              Ablation 3: Rational Quadratic + WhiteNoise    Upper Confidence Bound (beta=1.0)               -19.2031             4.0902               0.0000            8.2397                        19.7071
Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise   Upper Confidence Bound (beta=2.58)               -19.2326             4.1197               2.6447            6.7624                        13.8163
(showing top 10 of 88 combos)
Best random-baseline: Mean Final Regret=6.4701, Mean AURC=20.9486
Best overall combo:   Mean Final Regret=3.9846, Mean AURC=21.522
Best combo vs random baseline: WINS on final regret
---------------------------------------------------------------------------------------------------------------------------------------
Running Function 2: 18 samples, 2D -> n_init=5, 3 iterations (holdout_fraction=0.3, 10 points held out) x 20 seeds x 8 kernels x 11 strategies (1760 total rollouts)...
=======================================================================================================================================
        FUNCTION 2 — FULL JOINT KERNEL x ACQUISITION SWEEP (N_seeds=20, n_init=5)
=======================================================================================================================================
                                                            Kernel                 Acquisition Variant  Mean Best Value Found  Mean Final Regret  Median Final Regret  Std Final Regret  Mean AURC (Convergence Speed)
         Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise                   Thompson Sampling                 0.7223             0.0337                  0.0            0.0634                         0.1242
                    Ablation 2: RBF + WhiteNoise (Smooth Gaussian)                   Thompson Sampling                 0.7181             0.0380                  0.0            0.0638                         0.1305
               Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)                   Thompson Sampling                 0.7150             0.0410                  0.0            0.0673                         0.1358
             Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)  Upper Confidence Bound (beta=1.96)                 0.7150             0.0410                  0.0            0.0818                         0.1379
                           Baseline: Matern 2.5 + WhiteNoise (ARD)                   Thompson Sampling                 0.7108             0.0452                  0.0            0.0672                         0.1351
               Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky) Probability of Improvement (xi=0.1)                 0.7108             0.0452                  0.0            0.0817                         0.1458
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise                   Thompson Sampling                 0.7071             0.0489                  0.0            0.0702                         0.1565
             Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)                   Thompson Sampling                 0.7052             0.0508                  0.0            0.0692                         0.1400
                           Baseline: Matern 2.5 + WhiteNoise (ARD)  Upper Confidence Bound (beta=1.96)                 0.7040             0.0521                  0.0            0.0998                         0.1594
             Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)  Upper Confidence Bound (beta=2.58)                 0.7024             0.0536                  0.0            0.0810                         0.1536
(showing top 10 of 88 combos)
Best random-baseline: Mean Final Regret=0.0792, Mean AURC=0.1774
Best overall combo:   Mean Final Regret=0.0337, Mean AURC=0.1242
Best combo vs random baseline: WINS on final regret
---------------------------------------------------------------------------------------------------------------------------------------
Running Function 3: 23 samples, 3D -> n_init=6, 5 iterations (holdout_fraction=0.3, 12 points held out) x 20 seeds x 8 kernels x 11 strategies (1760 total rollouts)...
=======================================================================================================================================
        FUNCTION 3 — FULL JOINT KERNEL x ACQUISITION SWEEP (N_seeds=20, n_init=6)
=======================================================================================================================================
                                                   Kernel               Acquisition Variant  Mean Best Value Found  Mean Final Regret  Median Final Regret  Std Final Regret  Mean AURC (Convergence Speed)
Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise Upper Confidence Bound (beta=0.5)                -0.0355             0.0006               0.0000            0.0008                         0.0041
                  Baseline: Matern 2.5 + WhiteNoise (ARD) Upper Confidence Bound (beta=0.5)                -0.0355             0.0006               0.0000            0.0008                         0.0045
      Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky) Upper Confidence Bound (beta=0.5)                -0.0355             0.0006               0.0000            0.0008                         0.0045
Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise                 Thompson Sampling                -0.0355             0.0006               0.0000            0.0008                         0.0066
           Ablation 2: RBF + WhiteNoise (Smooth Gaussian) Upper Confidence Bound (beta=0.5)                -0.0355             0.0007               0.0000            0.0008                         0.0045
Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise Upper Confidence Bound (beta=1.0)                -0.0355             0.0007               0.0000            0.0008                         0.0052
           Ablation 2: RBF + WhiteNoise (Smooth Gaussian) Upper Confidence Bound (beta=1.0)                -0.0355             0.0007               0.0000            0.0008                         0.0055
           Ablation 2: RBF + WhiteNoise (Smooth Gaussian)                 Thompson Sampling                -0.0355             0.0007               0.0000            0.0008                         0.0069
                  Baseline: Matern 2.5 + WhiteNoise (ARD) Upper Confidence Bound (beta=1.0)                -0.0356             0.0008               0.0008            0.0008                         0.0058
    Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless) Upper Confidence Bound (beta=0.5)                -0.0356             0.0008               0.0008            0.0008                         0.0060
(showing top 10 of 88 combos)
Best random-baseline: Mean Final Regret=0.0018, Mean AURC=0.0092
Best overall combo:   Mean Final Regret=0.0006, Mean AURC=0.0041
Best combo vs random baseline: WINS on final regret
---------------------------------------------------------------------------------------------------------------------------------------
Running Function 4: 38 samples, 4D -> n_init=8, 9 iterations (holdout_fraction=0.3, 21 points held out) x 20 seeds x 8 kernels x 11 strategies (1760 total rollouts)...
=======================================================================================================================================
        FUNCTION 4 — FULL JOINT KERNEL x ACQUISITION SWEEP (N_seeds=20, n_init=8)
=======================================================================================================================================
                                                            Kernel                  Acquisition Variant  Mean Best Value Found  Mean Final Regret  Median Final Regret  Std Final Regret  Mean AURC (Convergence Speed)
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise    Upper Confidence Bound (beta=0.5)                -0.5824                0.0                  0.0               0.0                         3.8084
                           Baseline: Matern 2.5 + WhiteNoise (ARD)    Upper Confidence Bound (beta=0.5)                -0.5824                0.0                  0.0               0.0                         3.9372
         Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise    Upper Confidence Bound (beta=0.5)                -0.5824                0.0                  0.0               0.0                         4.1656
         Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise    Upper Confidence Bound (beta=1.0)                -0.5824                0.0                  0.0               0.0                         4.4751
               Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)    Upper Confidence Bound (beta=0.5)                -0.5824                0.0                  0.0               0.0                         5.3367
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise                    Thompson Sampling                -0.5824                0.0                  0.0               0.0                         6.4692
               Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)  Probability of Improvement (xi=0.1)                -0.5824                0.0                  0.0               0.0                         6.5022
               Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)    Upper Confidence Bound (beta=1.0)                -0.5824                0.0                  0.0               0.0                         6.6987
               Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky) Probability of Improvement (xi=0.01)                -0.5824                0.0                  0.0               0.0                         7.0870
               Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)      Expected Improvement (xi=0.001)                -0.5824                0.0                  0.0               0.0                         7.2222
(showing top 10 of 88 combos)
Best random-baseline: Mean Final Regret=1.0267, Mean AURC=16.6862
Best overall combo:   Mean Final Regret=0.0, Mean AURC=3.8084
Best combo vs random baseline: WINS on final regret
---------------------------------------------------------------------------------------------------------------------------------------
Running Function 5: 28 samples, 4D -> n_init=8, 6 iterations (holdout_fraction=0.3, 14 points held out) x 20 seeds x 8 kernels x 11 strategies (1760 total rollouts)...
=======================================================================================================================================
        FUNCTION 5 — FULL JOINT KERNEL x ACQUISITION SWEEP (N_seeds=20, n_init=8)
=======================================================================================================================================
                                                   Kernel                Acquisition Variant  Mean Best Value Found  Mean Final Regret  Median Final Regret  Std Final Regret  Mean AURC (Convergence Speed)
      Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky)  Upper Confidence Bound (beta=1.0)              2333.0068                0.0                  0.0               0.0                       408.4684
      Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky) Upper Confidence Bound (beta=1.96)              2333.0068                0.0                  0.0               0.0                       430.2649
    Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)  Upper Confidence Bound (beta=0.5)              2333.0068                0.0                  0.0               0.0                       452.6376
    Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)  Upper Confidence Bound (beta=1.0)              2333.0068                0.0                  0.0               0.0                       467.1685
    Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless)                  Thompson Sampling              2333.0068                0.0                  0.0               0.0                       477.9042
Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise                  Thompson Sampling              2333.0068                0.0                  0.0               0.0                       505.8629
              Ablation 3: Rational Quadratic + WhiteNoise Upper Confidence Bound (beta=2.58)              2333.0068                0.0                  0.0               0.0                       507.0612
Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise  Upper Confidence Bound (beta=1.0)              2333.0068                0.0                  0.0               0.0                       509.3701
                  Baseline: Matern 2.5 + WhiteNoise (ARD)    Expected Improvement (xi=0.001)              2333.0068                0.0                  0.0               0.0                       522.1104
                  Baseline: Matern 2.5 + WhiteNoise (ARD)     Expected Improvement (xi=0.01)              2333.0068                0.0                  0.0               0.0                       522.1104
(showing top 10 of 88 combos)
Best random-baseline: Mean Final Regret=109.8838, Mean AURC=2060.0048
Best overall combo:   Mean Final Regret=0.0, Mean AURC=408.4684
Best combo vs random baseline: WINS on final regret
---------------------------------------------------------------------------------------------------------------------------------------
Running Function 6: 28 samples, 5D -> n_init=10, 5 iterations (holdout_fraction=0.3, 13 points held out) x 20 seeds x 8 kernels x 11 strategies (1760 total rollouts)...
=======================================================================================================================================
        FUNCTION 6 — FULL JOINT KERNEL x ACQUISITION SWEEP (N_seeds=20, n_init=10)
=======================================================================================================================================
                                                            Kernel                  Acquisition Variant  Mean Best Value Found  Mean Final Regret  Median Final Regret  Std Final Regret  Mean AURC (Convergence Speed)
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise    Upper Confidence Bound (beta=0.5)                -0.2599                0.0                  0.0               0.0                         0.0133
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise Probability of Improvement (xi=0.01)                -0.2599                0.0                  0.0               0.0                         0.0133
                       Ablation 3: Rational Quadratic + WhiteNoise    Upper Confidence Bound (beta=0.5)                -0.2599                0.0                  0.0               0.0                         0.0152
   Ablation 6: RBF Isotropic (Shared Lengthscale 0.5) + WhiteNoise    Upper Confidence Bound (beta=0.5)                -0.2599                0.0                  0.0               0.0                         0.0152
                       Ablation 3: Rational Quadratic + WhiteNoise Probability of Improvement (xi=0.01)                -0.2599                0.0                  0.0               0.0                         0.0190
   Ablation 6: RBF Isotropic (Shared Lengthscale 0.5) + WhiteNoise Probability of Improvement (xi=0.01)                -0.2599                0.0                  0.0               0.0                         0.0190
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise    Upper Confidence Bound (beta=1.0)                -0.2599                0.0                  0.0               0.0                         0.0293
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise  Probability of Improvement (xi=0.1)                -0.2599                0.0                  0.0               0.0                         0.0473
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise      Expected Improvement (xi=0.001)                -0.2599                0.0                  0.0               0.0                         0.0492
                       Ablation 3: Rational Quadratic + WhiteNoise    Upper Confidence Bound (beta=1.0)                -0.2599                0.0                  0.0               0.0                         0.0511
(showing top 10 of 88 combos)
Best random-baseline: Mean Final Regret=0.074, Mean AURC=0.3548
Best overall combo:   Mean Final Regret=0.0, Mean AURC=0.0133
Best combo vs random baseline: WINS on final regret
---------------------------------------------------------------------------------------------------------------------------------------
Running Function 7: 38 samples, 6D -> n_init=12, 7 iterations (holdout_fraction=0.3, 19 points held out) x 20 seeds x 8 kernels x 11 strategies (1760 total rollouts)...
=======================================================================================================================================
        FUNCTION 7 — FULL JOINT KERNEL x ACQUISITION SWEEP (N_seeds=20, n_init=12)
=======================================================================================================================================
                                                            Kernel                  Acquisition Variant  Mean Best Value Found  Mean Final Regret  Median Final Regret  Std Final Regret  Mean AURC (Convergence Speed)
                       Ablation 3: Rational Quadratic + WhiteNoise    Upper Confidence Bound (beta=0.5)                 1.5366                0.0                  0.0               0.0                         0.1436
   Ablation 6: RBF Isotropic (Shared Lengthscale 0.5) + WhiteNoise    Upper Confidence Bound (beta=0.5)                 1.5366                0.0                  0.0               0.0                         0.1436
                       Ablation 3: Rational Quadratic + WhiteNoise    Upper Confidence Bound (beta=1.0)                 1.5366                0.0                  0.0               0.0                         0.1463
   Ablation 6: RBF Isotropic (Shared Lengthscale 0.5) + WhiteNoise    Upper Confidence Bound (beta=1.0)                 1.5366                0.0                  0.0               0.0                         0.1463
                       Ablation 3: Rational Quadratic + WhiteNoise   Upper Confidence Bound (beta=1.96)                 1.5366                0.0                  0.0               0.0                         0.1771
   Ablation 6: RBF Isotropic (Shared Lengthscale 0.5) + WhiteNoise   Upper Confidence Bound (beta=1.96)                 1.5366                0.0                  0.0               0.0                         0.1771
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise    Upper Confidence Bound (beta=0.5)                 1.5366                0.0                  0.0               0.0                         0.1866
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise    Upper Confidence Bound (beta=1.0)                 1.5366                0.0                  0.0               0.0                         0.1866
                       Ablation 3: Rational Quadratic + WhiteNoise Probability of Improvement (xi=0.01)                 1.5366                0.0                  0.0               0.0                         0.1907
   Ablation 6: RBF Isotropic (Shared Lengthscale 0.5) + WhiteNoise Probability of Improvement (xi=0.01)                 1.5366                0.0                  0.0               0.0                         0.1907
(showing top 10 of 88 combos)
Best random-baseline: Mean Final Regret=0.0933, Mean AURC=0.678
Best overall combo:   Mean Final Regret=0.0, Mean AURC=0.1436
Best combo vs random baseline: WINS on final regret
---------------------------------------------------------------------------------------------------------------------------------------
Running Function 8: 48 samples, 8D -> n_init=16, 9 iterations (holdout_fraction=0.3, 23 points held out) x 20 seeds x 8 kernels x 11 strategies (1760 total rollouts)...
=======================================================================================================================================
        FUNCTION 8 — FULL JOINT KERNEL x ACQUISITION SWEEP (N_seeds=20, n_init=16)
=======================================================================================================================================
                                                            Kernel                  Acquisition Variant  Mean Best Value Found  Mean Final Regret  Median Final Regret  Std Final Regret  Mean AURC (Convergence Speed)
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise Probability of Improvement (xi=0.01)                 9.9561                0.0                  0.0               0.0                         0.0503
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise  Probability of Improvement (xi=0.1)                 9.9561                0.0                  0.0               0.0                         0.0515
Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise    Upper Confidence Bound (beta=0.5)                 9.9561                0.0                  0.0               0.0                         0.0546
                       Ablation 3: Rational Quadratic + WhiteNoise Probability of Improvement (xi=0.01)                 9.9561                0.0                  0.0               0.0                         0.0577
   Ablation 6: RBF Isotropic (Shared Lengthscale 0.5) + WhiteNoise Probability of Improvement (xi=0.01)                 9.9561                0.0                  0.0               0.0                         0.0577
         Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise    Upper Confidence Bound (beta=0.5)                 9.9561                0.0                  0.0               0.0                         0.0689
                    Ablation 2: RBF + WhiteNoise (Smooth Gaussian)    Upper Confidence Bound (beta=0.5)                 9.9561                0.0                  0.0               0.0                         0.0766
         Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise Probability of Improvement (xi=0.01)                 9.9561                0.0                  0.0               0.0                         0.0786
                       Ablation 3: Rational Quadratic + WhiteNoise    Upper Confidence Bound (beta=0.5)                 9.9561                0.0                  0.0               0.0                         0.0806
   Ablation 6: RBF Isotropic (Shared Lengthscale 0.5) + WhiteNoise    Upper Confidence Bound (beta=0.5)                 9.9561                0.0                  0.0               0.0                         0.0806
(showing top 10 of 88 combos)
Best random-baseline: Mean Final Regret=0.0465, Mean AURC=0.3922
Best overall combo:   Mean Final Regret=0.0, Mean AURC=0.0503
Best combo vs random baseline: WINS on final regret
---------------------------------------------------------------------------------------------------------------------------------------

====================================================================================================
 SUMMARY: BEST (KERNEL, ACQUISITION) COMBO PER FUNCTION — RANKED FOR GLOBAL MAXIMIZATION
====================================================================================================
FUNCTION_1: Ablation 4: Matern 2.5 WITHOUT WhiteNoise (Noiseless) + Upper Confidence Bound (beta=2.58)
    Mean Best Value Found : -19.0975
    Mean Final Regret     : 3.9846
    Mean AURC             : 21.522
    n_init / n_iterations : 5 / 3
    Vs random baseline    : WINS on final regret
FUNCTION_2: Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise + Thompson Sampling
    Mean Best Value Found : 0.7223
    Mean Final Regret     : 0.0337
    Mean AURC             : 0.1242
    n_init / n_iterations : 5 / 3
    Vs random baseline    : WINS on final regret
FUNCTION_3: Ablation 7: RBF with Unit Lengthscales (ARD) + WhiteNoise + Upper Confidence Bound (beta=0.5)
    Mean Best Value Found : -0.0355
    Mean Final Regret     : 0.0006
    Mean AURC             : 0.0041
    n_init / n_iterations : 6 / 5
    Vs random baseline    : WINS on final regret
FUNCTION_4: Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise + Upper Confidence Bound (beta=0.5)
    Mean Best Value Found : -0.5824
    Mean Final Regret     : 0.0
    Mean AURC             : 3.8084
    n_init / n_iterations : 8 / 9
    Vs random baseline    : WINS on final regret
FUNCTION_5: Ablation 1: Matern 1.5 + WhiteNoise (Rougher/Spiky) + Upper Confidence Bound (beta=1.0)
    Mean Best Value Found : 2333.0068
    Mean Final Regret     : 0.0
    Mean AURC             : 408.4684
    n_init / n_iterations : 8 / 6
    Vs random baseline    : WINS on final regret
FUNCTION_6: Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise + Upper Confidence Bound (beta=0.5)
    Mean Best Value Found : -0.2599
    Mean Final Regret     : 0.0
    Mean AURC             : 0.0133
    n_init / n_iterations : 10 / 5
    Vs random baseline    : WINS on final regret
FUNCTION_7: Ablation 3: Rational Quadratic + WhiteNoise + Upper Confidence Bound (beta=0.5)
    Mean Best Value Found : 1.5366
    Mean Final Regret     : 0.0
    Mean AURC             : 0.1436
    n_init / n_iterations : 12 / 7
    Vs random baseline    : WINS on final regret
FUNCTION_8: Ablation 5: Matern 2.5 Isotropic (Shared Lengthscale) + WhiteNoise + Probability of Improvement (xi=0.01)
    Mean Best Value Found : 9.9561
    Mean Final Regret     : 0.0
    Mean AURC             : 0.0503
    n_init / n_iterations : 16 / 9
    Vs random baseline    : WINS on final regret
====================================================================================================
Master plot successfully saved to 'week_09/diagnostics_results/full_joint_ablation_all_functions.png'
```
