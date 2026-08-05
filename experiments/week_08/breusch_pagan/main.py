"""Breusch-Pagan Homo/Heteroscedasticity Analysis — Week 8
Not used to inform the main ML pipeline, since HEBO-style output warping is applied
regardless of BP test results. This module is purely diagnostic.
"""

import sys
import os
import pickle

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kernel_ablation.kernel_ablation import run_kernel_ablation
from breusch_pagan.breusch_pagan import run_bp


def main():

    # Step 1 — Loading unified Week 8 dataset snapshot
    data_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'wk8_input_data.pkl')
    )
    print(f"\n[INFO] Loading dataset from: {data_path}")

    if not os.path.exists(data_path):
        print(f"[ERROR] Dataset file not found at '{data_path}'. "
              f"Please ensure 'wk8_input_data.pkl' is present.")
        return

    with open(data_path, "rb") as file:
        data = pickle.load(file)

    print("[INFO] Dataset successfully loaded into memory.")

    # Step 2 — Kernel Ablation Study (Week 8)
    print("\n" + "=" * 100)
    print(" [STEP 1] Running Unified Kernel Ablation Study (GPR)...")
    print("=" * 100)

    top_kernels = run_kernel_ablation(data)

    print("\n[SUCCESS] Kernel ablation study execution complete!")

    # Step 3 — Breusch-Pagan Heteroscedasticity Diagnostics (Week 8)
    print("\n" + "=" * 100)
    print(" [STEP 2] Running Breusch-Pagan Homo/Heteroscedasticity Analysis...")
    print("=" * 100)

    run_bp(data, top_kernels)

    print("\n[SUCCESS] Breusch-Pagan analysis complete!")


if __name__ == "__main__":
    main()
