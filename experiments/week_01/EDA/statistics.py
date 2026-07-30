"""
Statistics Module
Computes and prints basic statistical analysis for all 8 functions.
"""

import numpy as np

def print_raw_data_and_stats(data: dict):
    """Printing initial data points and summary statistics for all functions."""
    
    print("=" * 50)
    print("Printing all initial data provided for all functions (to 6 decimal places):")
    print("=" * 50)

    for i in range(1, 9):
        fn_key = f"function_{i}"
        if fn_key not in data:
            print(f"\nFunction {fn_key} not found in input data.")
            continue

        x = data[fn_key]["x"]
        y = data[fn_key]["y"]

        print(f"\nFunction {i} initial datapoints are:\n")
        for j, (x_val, y_val) in enumerate(zip(x, y), start=1):
            formatted_x = [f"{coord:.6f}" for coord in x_val] if isinstance(x_val, (list, np.ndarray)) else f"{x_val:.6f}"
            print(f"{j}. ({formatted_x}, {y_val:.6f})")

    print("\n" + "=" * 50)
    print("Computing statistical analysis of all functions' initial outputs:")
    print("=" * 50)

    for i in range(1, 9):
        y_vals = data[f"function_{i}"]["y"]
        min_value = np.min(y_vals)
        max_value = np.max(y_vals)
        mean_value = np.mean(y_vals)
        std_value = np.std(y_vals)
        
        print(f"\nStatistical analysis of Function {i}:")
        print("-" * 35)
        print(f"Minimum value = {min_value:.6f}")
        print(f"Maximum value = {max_value:.6f}")
        print(f"Standard deviation = {std_value:.6f}")
        print(f"Mean = {mean_value:.6f}")
