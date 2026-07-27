# Personalised NuSVM vs MLP Classifier Selection for Acquisition Filtering Strategy Selection for Each Function
Comparative evaluation of **NuSVC** (Support Vector Classifier) and **MLPClassifier** (Multilayer Perceptron Neural Network) 
across all 8 Black-Box functions. 

## Evaluation Methodology
* **Task:** Binary classification to identify the top 25% highest-performing target regions ($75^{\text{th}}$ percentile threshold) for each black-box function dataset. The winning classifier for each function will be used for acquistion filtering in the Bayesian Optimisation query prediction pipeline for Week 7.
* **Validation Strategy:** Stratified 3-Fold Cross-Validation.
* **Performance Metric:** Out-of-sample Receiver Operating Characteristic Area Under the Curve (ROC-AUC) evaluated across unseen test folds to prevent data leakage and measure generalization capability.

## Results

```text
==========================================================================================
        COMPARATIVE SVM vs. MLP 3-FOLD CV ROC-AUC & ACQUISITION FILTERING DECISIONS
==========================================================================================
[FUNCTION_1]
  • NuSVC CV ROC-AUC       : 0.4167
  • MLPClassifier CV AUC   : 0.4792
  • Recommended Winner     : MLP (AUC: 0.4792)
------------------------------------------------------------------------------------------
[FUNCTION_2]
  • NuSVC CV ROC-AUC       : 0.4167
  • MLPClassifier CV AUC   : 0.8750
  • Recommended Winner     : MLP (AUC: 0.8750)
------------------------------------------------------------------------------------------
[FUNCTION_3]
  • NuSVC CV ROC-AUC       : 0.5222
  • MLPClassifier CV AUC   : 0.5000
  • Recommended Winner     : NuSVC (AUC: 0.5222)
------------------------------------------------------------------------------------------
[FUNCTION_4]
  • NuSVC CV ROC-AUC       : 0.6790
  • MLPClassifier CV AUC   : 0.7778
  • Recommended Winner     : MLP (AUC: 0.7778)
------------------------------------------------------------------------------------------
[FUNCTION_5]
  • NuSVC CV ROC-AUC       : 0.9850
  • MLPClassifier CV AUC   : 0.9699
  • Recommended Winner     : NuSVC (AUC: 0.9850)
------------------------------------------------------------------------------------------
[FUNCTION_6]
  • NuSVC CV ROC-AUC       : 0.6767
  • MLPClassifier CV AUC   : 0.8346
  • Recommended Winner     : MLP (AUC: 0.8346)
------------------------------------------------------------------------------------------
[FUNCTION_7]
  • NuSVC CV ROC-AUC       : 0.6214
  • MLPClassifier CV AUC   : 0.6543
  • Recommended Winner     : MLP (AUC: 0.6543)
------------------------------------------------------------------------------------------
[FUNCTION_8]
  • NuSVC CV ROC-AUC       : 0.9216
  • MLPClassifier CV AUC   : 0.9142
  • Recommended Winner     : NuSVC (AUC: 0.9216)
------------------------------------------------------------------------------------------
```
