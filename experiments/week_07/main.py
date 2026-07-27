"""
Main Execution Script: Week 07 Full Machine Learning Pipeline
-----------------------------------------------------------
Coordinates the end-to-end execution of:
1. Kernel Ablation Study (Gaussian Process Regression optimization)
2. SVM Classification (NuSVC modeling for top-25% acquisition filtering)
3. MLP Classification (MLPClassifier modeling for top-25% acquisition filtering)
4. Classifier Selection Summary (Comparative analysis and optimal model routing)
"""

import sys
import os
import pickle

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kernel_ablation.kernel_ablation import run_kernel_ablation
from svm_classification.svm_classification import run_svm_classification
from mlp_classifier.mlp_classification import run_mlp_classification
from classifier_selection.classifier_selection import generate_comparison_summary

def main():
    print("=" * 100)
    print("                 WEEK 07 BBO PIPELINE: EXECUTION & EVALUATION START")
    print("=" * 100)

    # Step 1. Loading the unified input dataset snapshot
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'wk7_input_data.pkl'))
    print(f"\n[INFO] Loading dataset from: {data_path}")
    
    if not os.path.exists(data_path):
        print(f"[ERROR] Dataset file not found at '{data_path}'. Please ensure 'wk7_input_data.pkl' is present.")
        return

    with open(data_path, "rb") as file:
        data = pickle.load(file)
    print("[INFO] Dataset successfully loaded into memory.")

    # Step 2. Executing Kernel Ablation Study (Step 1)
    print("\n" + "=" * 100)
    print(" [STEP 1] Running Unified Kernel Ablation Study (GPR)...")
    print("=" * 100)
    top_kernels = run_kernel_ablation(data)
    print("\n[SUCCESS] Kernel ablation study execution complete!")

    # Step 3. Executing SVM Classification (Step 2A)
    print("\n" + "=" * 100)
    print(" [STEP 2A] Running NuSVC Classification & 3-Fold CV Evaluation...")
    print("=" * 100)
    svm_auc_scores = run_svm_classification(data, top_kernels)
    print("\n[SUCCESS] NuSVC classification evaluation complete!")

    # Step 4. Executing MLP Classification (Step 2B)
    print("\n" + "=" * 100)
    print(" [STEP 2B] Running MLPClassifier & 3-Fold CV Evaluation...")
    print("=" * 100)
    mlp_auc_scores = run_mlp_classification(data)
    print("\n[SUCCESS] MLPClassifier evaluation complete!")

    # Step 5. Executing Final Classifier Selection & Comparison Summary (Step 3)
    print("\n" + "=" * 100)
    print(" [STEP 3] Generating Comparative Summary & Acquisition Filtering Decisions...")
    print("=" * 100)
    comparison_summary = generate_comparison_summary(data, svm_auc_scores, mlp_auc_scores)
    
    print("\n" + "=" * 100)
    print("                 WEEK 07 BBO PIPELINE: ALL TASKS COMPLETED SUCCESSFULLY")
    print("=" * 100)

if __name__ == "__main__":
    main()
