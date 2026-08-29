""" Main Execution Script: BBO Week 13 Full Highly-Exploitative Bayesian Optimisation ML Pipeline
------------------------------------------------------------------------------------------------------------
1. Full Joint Kernel x Acquisition Rollout Ablation Study, with 95% CI uncertainty reporting on the Mean 
   Simple Final Regret ranking, and adjusted per-function n_seeds, so that small-pool functions get enough 
   seeds to meaningfully tighten their CIs for a more confident kernel x acquisition combo ranking for 
   each 'Black-Box' function.
   
2. Next Query Prediction (HEBO output warping, GP surrogate, Dynamic and more Advanced Sobol Sampling 
   (full-space + density-enhanced best KMeans cluster local-box sampling), jointly-chosen acquisition 
   scoring, output unwarping).

!Note: The BBO Week 13 Full ML Bayesian Optimisation Pipeline is computationally heavy.
       Runtime to completion is expected to be around ~2.5h if 16 CPU cores are available, 
       but it may take slightly/significantly longer if not.
"""


import sys
import os
import pickle
import numpy as np

from full_ablation.full_joint_ablation import run_full_joint_ablation
from query_predict.query_predict import run_next_query_prediction
from full_ablation.kernels import get_kernel_suite, get_kernel_suite_f1
from kmeans_clustering.kmeans_clustering import run_kmeans_clustering_diagnostics

# Importing configurations: global defaults and function-specific overrides
from full_ablation.config_overrides import (
    n_init_base,
    init_per_dim,
    n_iterations,
    n_seeds,
    holdout_fraction,
    n_init_base_overrides,
    init_per_dim_overrides,
    holdout_fraction_overrides,
    n_seeds_overrides,
)


def main():
    print("=" * 100)
    print("                    WEEK 13 BBO FINAL HIGHLY-EXPLOITATIVE PIPELINE (density-matched local pool): EXECUTION START")
    print("=" * 100) # Note that 'density-matched' refers to the *initial* density matching of the local pool with full-space
                     # implemented for a controlled following density enhancement of the local-box Sobol candidate pool

    # Loading the unified input dataset snapshot
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'wk13_input_data.pkl'))
    print(f"\n[INFO] Loading dataset from: {data_path}")
    if not os.path.exists(data_path):
        print(f"[ERROR] Dataset file not found at '{data_path}'. Please ensure 'wk13_input_data.pkl' is present.")
        return
    with open(data_path, "rb") as file:
        data = pickle.load(file)
    print("[INFO] Dataset successfully loaded into memory.")
   
    print("\n" + "=" * 100)
    print(" [STEP 1] Running FULL JOINT Kernel x Acquisition Rollout Ablation Study...")
    print("=" * 100)
    sequential_ablation_summary = run_full_joint_ablation(
    data=data,
    n_init_base=n_init_base,
    init_per_dim=init_per_dim,
    n_iterations=n_iterations,
    n_seeds=n_seeds,
    holdout_fraction=holdout_fraction,
    n_init_base_overrides=n_init_base_overrides,
    init_per_dim_overrides=init_per_dim_overrides,
    holdout_fraction_overrides=holdout_fraction_overrides,
    n_seeds_overrides=n_seeds_overrides
    )

    # Ablation Summary Saving Checkpoint
    with open("week_full_ablation_summary.pkl", "wb") as f:
        pickle.dump(sequential_ablation_summary, f)
    
    print("\n[SUCCESS] Joint kernel x acquisition ablation study complete!")

    print("\n" + "=" * 100)
    print(" [STEP 2] Running K-Means Clustering Diagnostics (elbow method + best-cluster bounding box)...")
    print("=" * 100)
    kmeans_results = run_kmeans_clustering_diagnostics(
        data=data,
        box_margin_fraction=0.1,
        make_plots=True
    )
    print("\n[SUCCESS] K-means clustering diagnostics complete!")

    print("\n" + "=" * 100)
    print(" [STEP 3] Executing Final HEBO-Based Next Query Predictions "
          "(global GP + density-matched combined Sobol pools)...")
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
        on_random_baseline="sample_random",
        min_distance_to_existing=0.0,
        sobol_seed_base=42,
        kmeans_results=kmeans_results,
        secondary_pool_extra_bits=2
    )

    # Next Query Results Saving Checkpoint
    with open("week13_next_query_results.pkl", "wb") as f:
        pickle.dump(next_queries_results, f)
    
    print("\n" + "=" * 100)
    print(" FINAL NEXT-QUERY SUMMARY")
    print("=" * 100)
    for fn_key, res in next_queries_results.items():
        print(f"{fn_key.upper()}:")
        print(f"    Next Query Coordinates : {np.round(res['Next Query Coordinates'], 6)}")
        print(f"    Kernel Used            : {res['Winning Kernel']}")
        print(f"    Acquisition Used       : {res['Winning Acquisition']}")
        print(f"    Predicted Value        : {res['Predicted Original Scale Value']}")
        print(f"    Predicted Std (warped) : {res['Predicted Std (warped scale)']:.4f}")
        print(f"    Chosen From Pool       : {res['Chosen From Pool']} "
              f"(full-domain candidates: {res['N Candidates Full Domain']}, "
              f"local-box candidates: {res['N Candidates Local Box']})")
        if res["Volume Ratio"] is not None:
            print(f"    Box Volume Ratio       : {res['Volume Ratio']:.4%} of full domain")
        if res["Best Full-Domain Score"] is not None and res["Best Local-Box Score"] is not None:
            print(f"    Best Score (full-domain / local-box): "
                  f"{res['Best Full-Domain Score']:.6f} / {res['Best Local-Box Score']:.6f}")
        # Printing unrounded predicted value for function_1, as its outputs are too small and round to '0.000000'.
        if res["Full-Domain Best Candidate Predicted Value"] is not None:
            fd_val = res['Full-Domain Best Candidate Predicted Value']
            fd_val_str = f"{fd_val}" if fn_key == "function_1" else f"{fd_val:.6f}"
            print(f"    Full-domain best candidate  : coords={np.round(res['Full-Domain Best Candidate Coords'], 6)} "
                  f"| predicted value={fd_val_str} "
                  f"| predicted std={res['Full-Domain Best Candidate Predicted Std']:.4f}")
        if res["Local-Box Best Candidate Predicted Value"] is not None:
            lb_val = res['Local-Box Best Candidate Predicted Value']
            lb_val_str = f"{lb_val}" if fn_key == "function_1" else f"{lb_val:.6f}"
            print(f"    Local-box best candidate    : coords={np.round(res['Local-Box Best Candidate Coords'], 6)} "
                  f"| predicted value={lb_val_str} "
                  f"| predicted std={res['Local-Box Best Candidate Predicted Std']:.4f}")
        print("-" * 100)
    print("\n" + "=" * 100)
    print("                    WEEK 13 BBO PIPELINE: ALL TASKS COMPLETED SUCCESSFULLY")
    print("=" * 100)

    return sequential_ablation_summary, kmeans_results, next_queries_results

# Redirecting prints to disk so the browser doesn't memory-crash.
log_file = "execution_output.log"
print(f"Starting execution... streaming all logs to '{log_file}' to protect browser memory.")

original_stdout = sys.stdout
with open(log_file, "w") as f:
    sys.stdout = f
    try:
        main() 
    finally:
        sys.stdout = original_stdout

print(f"Completed! Check '{log_file}' for full results.")
