"""
Main Execution Script: Week 07 Full Machine Learning Pipeline
-----------------------------------------------------------
Coordinates the end-to-end execution of:
1. Kernel Ablation Study (Gaussian Process Regression optimization)
2. Surrogate Model Selection (GP or Deep Ensemble)
3. Sequential Acquisition Ablation Study
4. SVM Classification (NuSVC modeling for top-25% acquisition filtering)
5. MLP Classification (MLPClassifier modeling for top-25% acquisition filtering)
6. Classifier Selection Summary (Comparative analysis and optimal model routing)
7. Next Query Prediction (Including HEBO Output Warping, GP/NN Surrogate Modeling, 
   Dynamic Sobol Sampling, SVM/MLP Sobol Candidate Classification and Acquisition Function 
   (optimised) Evaluation and Scoring, Output Unwarping of Best Query)
"""

import sys
import os
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import NuSVC
from sklearn.neural_network import MLPClassifier

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kernel_ablation.kernel_ablation import run_kernel_ablation
from kernel_ablation.kernels import get_kernel_suite, get_kernel_suite_f1
from surrogate_selection.surrogate_selection import run_surrogate_comparison
from acquisition_ablation.acquisition_ablation import run_sequential_acq_ablation
from svm_classification.svm_classification import run_svm_classification
from mlp_classifier.mlp_classification import run_mlp_classification
from breusch_pagan.breusch_pagan import run_bp
from classifier_selection.classifier_selection import generate_comparison_summary
from query_predict.query_predict import run_next_query_prediction

def main():
    print("=" * 100)
    print("                    WEEK 07 BBO PIPELINE: EXECUTION & EVALUATION START")
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

    # Step 2. Executing Kernel Ablation Study (Part 1)
    print("\n" + "=" * 100)
    print(" [STEP 1] Running Unified Kernel Ablation Study (GPR)...")
    print("=" * 100)
    top_kernels = run_kernel_ablation(data)
    print("\n[SUCCESS] Kernel ablation study execution complete!")

    # Step 3. Executing Surrogate Model Selection (GP vs Deep Ensemble)
    print("\n" + "=" * 100)
    print(" [STEP 2] Running Surrogate Model LOOCV Comparison...")
    print("=" * 100)
    surrogate_evaluation_summary = run_surrogate_comparison(
        data=data, 
        top_kernels_summary=top_kernels, 
        get_kernel_suite=get_kernel_suite, 
        get_kernel_suite_f1=get_kernel_suite_f1
    )
    print("\n[SUCCESS] Surrogate model comparison complete!")

    # Step 4. Executing Sequential Acquisition Ablation Study
    print("\n" + "=" * 100)
    print(" [STEP 3] Running Sequential Acquisition Rollout Ablation Study...")
    print("=" * 100)
    sequential_ablation_summary = run_sequential_acq_ablation(
        data=data, 
        top_kernels_summary=top_kernels, 
        n_init=5, 
        n_iterations=15, 
        n_seeds=20
    )
    print("\n[SUCCESS] Acquisition ablation study complete!")

    # Step 5. Executing SVM Classification (Part 3A) - Updated to match clean function signature
    print("\n" + "=" * 100)
    print(" [STEP 4A] Running NuSVC Classification & 3-Fold CV Evaluation...")
    print("=" * 100)
    svm_auc_scores = run_svm_classification(data)
    print("\n[SUCCESS] NuSVC classification evaluation complete!")

    # Step 6. Executing MLP Classification (Part 3B)
    print("\n" + "=" * 100)
    print(" [STEP 4B] Running MLPClassifier & 3-Fold CV Evaluation...")
    print("=" * 100)
    mlp_auc_scores = run_mlp_classification(data)
    print("\n[SUCCESS] MLPClassifier evaluation complete!")

    # Step 7. Executing Final Classifier Selection & Comparison Summary (Part 4)
    print("\n" + "=" * 100)
    print(" [STEP 5] Generating Classifier Comparative Summary & Acquisition Filtering Decisions...")
    print("=" * 100)
    comparison_summary = generate_comparison_summary(data, svm_auc_scores, mlp_auc_scores)
    print("\n[SUCCESS] Classifier comparison summary generated!")

    # Step 8. Building Trained Classifiers Dictionary for Active Filtering in Next Query Prediction
    print("\n" + "=" * 100)
    print(" [STEP 6] Training Final Winning Classifiers for Sobol Candidate Filtering...")
    print("=" * 100)
    
    trained_classifiers_dict = {}
    
    for fn_idx in range(1, 9):
        fn_key = f"function_{fn_idx}"
        if fn_key not in comparison_summary or fn_key not in data:
            continue
            
        winning_clf_name = comparison_summary[fn_key]["Winning_Classifier"]
        
        # Extracting Data
        X = np.array(data[fn_key]["x"])
        Y = np.array(data[fn_key]["y"]).flatten()
        Y_target = np.log10(np.clip(Y, 1e-300, None)) if fn_idx == 1 else Y
        
        # Scaling features and projecting high-D space -> 2D via PCA
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        pca = PCA(n_components=2, random_state=42)
        X_pca = pca.fit_transform(X_scaled)
        
        # Binary target labeling (top 25% threshold)
        y_threshold = np.quantile(Y_target, 0.75)
        Y_binary = (Y_target >= y_threshold).astype(int)
        
        if len(np.unique(Y_binary)) < 2:
            continue
            
        # Fitting the winning model type dynamically based on comparison choice
        if winning_clf_name == "NuSVC" or winning_clf_name == "SVM":
            clf = NuSVC(nu=0.25, kernel="rbf", gamma="scale", probability=True, random_state=42)
        else:
            clf = MLPClassifier(hidden_layer_sizes=(32, 16), activation='relu', solver='adam', max_iter=1000, random_state=42)
            
        clf.fit(X_pca, Y_binary)
        
        # Caching the trained model and PCA transformer tuple
        trained_classifiers_dict[fn_key] = (clf, pca)

    print("[SUCCESS] Winning classifiers fitted and cached successfully!")

    # Step 9. Executing Final Next Query Predictions (Part 5)
    print("\n" + "=" * 100)
    print(" [STEP 7] Executing Final HEBO & Classifier-Filtered Next Query Predictions...")
    print("=" * 100)

    # Dynamically defining kernel suites dictionary required for candidate scoring
    kernel_suites_dict = {}
    for fn_idx in range(1, 9):
        fn_key = f"function_{fn_idx}"
        if fn_key in data:
            n_dims = data[fn_key]["x"].shape[1]
            if fn_idx == 1:
                kernel_suites_dict[fn_key] = get_kernel_suite_f1(n_dims)
            else:
                kernel_suites_dict[fn_key] = get_kernel_suite(n_dims)

    next_queries_results = run_next_query_prediction(
        data=data,
        surrogate_evaluation_summary=surrogate_evaluation_summary,
        sequential_ablation_summary=sequential_ablation_summary,
        comparison_summary=comparison_summary,
        kernel_suites_dict=kernel_suites_dict,
        trained_classifiers_dict=trained_classifiers_dict
    )

    print("\n" + "=" * 100)
    print("                    WEEK 07 BBO PIPELINE: ALL TASKS COMPLETED SUCCESSFULLY")
    print("=" * 100)

if __name__ == "__main__":
    main()
