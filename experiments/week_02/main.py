"""
Week 2 Black-Box Optimisation (BBO) Capstone Project 
Sequential Bayesian Optimisation using Gaussian Processes (GP) surrogate models

Generating the 2nd query points to be submitted for each of the 8 Black-Box functions
Overall Aim: Global Function Maximisation

Input: wk2_input_data.pkl (containing initial data + 1 submitted query)
Output: Printed 2nd query coordinates (raw and 6-decimal rounded)
"""

import pickle
import numpy as np
from config import get_function_configs
from query_predict import compute_next_query


def run_all_functions(data: dict):
    print("\nFetching model configurations...")
    configs = get_function_configs()
    query_results = {}

    print("\nStarting Bayesian Optimization loop across all 8 functions...")
    for fn_idx in range(1, 9):
        fn_key = f"function_{fn_idx}"
        if fn_key not in data:
            print(f"Skipping {fn_key}: Key not found in input data.")
            continue

        print(f"\nGenerating Next Query Prediction for Function {fn_idx}...")
        X = np.array(data[fn_key]["x"])
        Y = np.array(data[fn_key]["y"]).flatten()
        cfg = configs[fn_idx]

        x_next = compute_next_query(
            X=X,
            Y=Y,
            kernel=cfg["kernel"],
            acq_type=cfg["acq_type"],
            acq_param=cfg["acq_param"],
            sobol_m=cfg["sobol_m"],
            alpha=cfg["alpha"],
            normalize_y=cfg["normalize_y"],
        )

        query_results[fn_key] = x_next

        print(f"Second raw query point for Function {fn_idx}:", x_next)
        print(f"Second query point for Function {fn_idx} (6 decimals):", np.round(x_next, 6))
        print()

    print("All predictions completed successfully!")
    return query_results

if __name__ == "__main__":
    # Loading pickle data file 
    print("Locating Week 2 input dataset...")
    file_path = "wk2_input_data.pkl"
    
    try:
        print(f"Loading binary pickle file '{file_path}'...")
        with open(file_path, "rb") as f:
            data = pickle.load(f)
            
        # Running the Bayesian Optimization loop for Week 2
        next_queries = run_all_functions(data)
        
    except FileNotFoundError:
        print(f"Error: Could not find '{file_path}'. Double check that it is in the same folder.")
