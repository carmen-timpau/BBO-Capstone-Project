"""Breusch-Pagan Homo/heteroscedasticity Analysis & Diagnostics
Not used to inform main ML pipeline for Week 7, as HEBO-style output warping was applied 
to all functions, independent of any test results, to avoid limit cases and model instability. 
"""

import sys
import os
import pickle

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kernel_ablation.kernel_ablation import run_kernel_ablation
from breusch_pagan.breusch_pagan import run_bp

def main():

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

    # Step 3. Executing Breusch-Pagan Homo/heteroscedasticity Analysis (Part 2)
    print("\n" + "=" * 100)
    print(" [STEP 2] Running Breusch-Pagan Homo/Heteroscedasticity Analysis...")
    print("=" * 100)
    run_bp(data, top_kernels)
    print("\n[SUCCESS] Breusch-Pagan analysis complete!")

if __name__ == "__main__":
    main()
