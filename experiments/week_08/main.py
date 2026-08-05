"""
Main Execution Script: Week 08 Full Machine Learning Pipeline
-----------------------------------------------------------
Coordinates the end-to-end execution of:
1. Kernel Ablation Study (Gaussian Process Regression optimization)
2. Surrogate Model Selection (GP or Deep Ensemble)
3. Sequential Acquisition Ablation Study
4. Next Query Prediction (Including HEBO Output Warping, GP/NN Surrogate Modeling, 
   Dynamic Sobol Sampling, and Acquisition Function (optimised) Evaluation and Scoring,
   Output Unwarping of Best Query)
"""

import sys
import os
import pickle
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kernel_ablation.kernel_ablation import run_kernel_ablation
from kernel_ablation.kernels import get_kernel_suite, get_kernel_suite_f1
from surrogate_selection.surrogate_selection import run_surrogate_comparison
from acquisition_ablation.acquisition_ablation import run_sequential_acq_ablation
from query_predict.query_predict import run_next_query_prediction


def main():
    print("=" * 100)
    print("                    WEEK 08 BBO PIPELINE: EXECUTION & EVALUATION START")
    print("=" * 100)

    # Step 1. Loading the unified input dataset snapshot
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'wk8_input_data.pkl'))
    print(f"\n[INFO] Loading dataset from: {data_path}")

    if not os.path.exists(data_path):
        print(f"[ERROR] Dataset file not found at '{data_path}'. Please ensure 'wk8_input_data.pkl' is present.")
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

    # Step 5. Executing Final Next Query Predictions
    print("\n" + "=" * 100)
    print(" [STEP 4] Executing Final HEBO-Based Next Query Predictions...")
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
        kernel_suites_dict=kernel_suites_dict
    )

    print("\n" + "=" * 100)
    print("                    WEEK 08 BBO PIPELINE: ALL TASKS COMPLETED SUCCESSFULLY")
    print("=" * 100)


if __name__ == "__main__":
    main()
