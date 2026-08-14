"""
Main Execution Script: BBO Capstone Project Week 9 - Full Machine Learning Pipeline
--------------------------------------------------------------------------------------
Coordinates the end-to-end execution of:
1. Full Joint Kernel x Acquisition Rollout Ablation Study: picks kernel and acquisition
   together per function (full_joint_ablation.run_full_joint_ablation).
2. Next Query Prediction (HEBO output warping, GP surrogate using the jointly-chosen kernel,
   Dynamic Sobol Sampling, jointly-chosen acquisition scoring, output unwarping).
"""

import sys
import os
import pickle
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from full_ablation.kernels import get_kernel_suite, get_kernel_suite_f1
from full_ablation.full_joint_ablation import run_full_joint_ablation
from query_predict.query_predict import run_next_query_prediction

def main():
    print("=" * 100)
    print("                    WEEK 09 BBO PIPELINE: EXECUTION & EVALUATION START")
    print("=" * 100)

    # Step 1. Loading the unified input dataset snapshot
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'wk9_input_data.pkl'))
    print(f"\n[INFO] Loading dataset from: {data_path}")
    if not os.path.exists(data_path):
        print(f"[ERROR] Dataset file not found at '{data_path}'. Please ensure 'wk9_input_data.pkl' is present.")
        return
    with open(data_path, "rb") as file:
        data = pickle.load(file)
    print("[INFO] Dataset successfully loaded into memory.")

    # Step 2. Executing Full Joint Kernel x Acquisition Rollout Ablation Study.
    # Picking the best kernel and acquisition pair per function.
    print("\n" + "=" * 100)
    print(" [STEP 1] Running Full Joint Kernel x Acquisition Rollout Ablation Study...")
    print("=" * 100)
    sequential_ablation_summary = run_full_joint_ablation(
        data=data,
        n_init_base=5,
        init_per_dim=2,
        n_iterations=15,
        n_seeds=20,
        holdout_fraction=0.3
    )
    print("\n[SUCCESS] Joint kernel x acquisition ablation study complete!")

    # Step 3. Executing the Final Next Query Predictions.
    print("\n" + "=" * 100)
    print(" [STEP 2] Executing Final HEBO-Based Next Query Predictions...")
    print("=" * 100)

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
        sequential_ablation_summary=sequential_ablation_summary,
        kernel_suites_dict=kernel_suites_dict,
        on_random_baseline="sample_random"
    )

    print("\n" + "=" * 100)
    print(" FINAL NEXT-QUERY SUMMARY")
    print("=" * 100)
    for fn_key, res in next_queries_results.items():
        print(f"{fn_key.upper()}:")
        print(f"    Next Query Coordinates : {np.round(res['Next Query Coordinates'], 6)}")
        print(f"    Kernel Used            : {res['Winning Kernel']}")
        print(f"    Acquisition Used       : {res['Winning Acquisition']}")
        print(f"    Predicted Value        : {res['Predicted Original Scale Value']:.6f}")
        print(f"    Predicted Std (warped) : {res['Predicted Std (warped scale)']:.4f}")
        print("-" * 100)

    print("\n" + "=" * 100)
    print("                    WEEK 09 BBO PIPELINE: ALL TASKS COMPLETED SUCCESSFULLY")
    print("=" * 100)

if __name__ == "__main__":
    main()
