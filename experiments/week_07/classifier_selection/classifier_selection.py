"""
NuSVM vs MLP Classifier Selection and Comparison Module
------------------------------------------
Comparing out-of-sample Stratified K-Fold CV ROC-AUC scores between NuSVC and MLPClassifier 
across all valid dataset functions to determine the optimal winning classifier for top-25% 
performance region acquisition filtering strategy selection.
"""

import numpy as np

def generate_comparison_summary(data, svm_auc_scores, mlp_auc_scores):
    """
    Computing and printing a comparison summary dictionary matching 
    valid evaluated functions to their respective SVM and MLP CV ROC-AUC scores.
    """
    comparison_summary = {}
    valid_fn_indices = []

    for fn_idx in range(1, 9):
        fn_key = f"function_{fn_idx}"
        if fn_key in data:
            # Checking if it has sufficient class variance to have been scored
            X = np.array(data[fn_key]["x"])
            Y = np.array(data[fn_key]["y"]).flatten()
            Y_target = np.log10(np.clip(Y, 1e-300, None)) if fn_idx == 1 else Y
            y_threshold = np.quantile(Y_target, 0.75)
            Y_binary = (Y_target >= y_threshold).astype(int)
            
            if len(np.unique(Y_binary)) >= 2:
                valid_fn_indices.append(fn_key)

    # Pairing up the scores sequentially based on the valid evaluated functions
    for i, fn_key in enumerate(valid_fn_indices):
        if i < len(svm_auc_scores) and i < len(mlp_auc_scores):
            svm_auc = svm_auc_scores[i]
            mlp_auc = mlp_auc_scores[i]
            
            winning_classifier = "MLP" if mlp_auc >= svm_auc else "NuSVC"
            winning_auc = max(mlp_auc, svm_auc)
            
            comparison_summary[fn_key] = {
                "SVM AUC": svm_auc,
                "MLP AUC": mlp_auc,
                "Winning_Classifier": winning_classifier,
                "Winning AUC": winning_auc
            }

    # Printing the Final Comparison Summary Table
    print("=" * 90)
    print("             COMPARATIVE SVM vs. MLP 3-FOLD CV ROC-AUC & ACQUISITION FILTERING DECISIONS")
    print("=" * 90)

    for fn_key, info in comparison_summary.items():
        print(f"[{fn_key.upper()}]")
        print(f"  • NuSVC CV ROC-AUC       : {info['SVM AUC']:.4f}")
        print(f"  • MLPClassifier CV AUC   : {info['MLP AUC']:.4f}")
        print(f"  • Recommended Winner     : {info['Winning_Classifier']} (AUC: {info['Winning AUC']:.4f})")
        print("-" * 90)
        
    return comparison_summary

# Executing summary generation if run directly
if __name__ == "__main__":
    if 'data' in globals() and 'svm_auc_scores' in globals() and 'mlp_auc_scores' in globals():
        summary = generate_comparison_summary(data, svm_auc_scores, mlp_auc_scores)
    else:
        print("[INFO] 'data', 'svm_auc_scores', or 'mlp_auc_scores' not found in workspace scope.")
