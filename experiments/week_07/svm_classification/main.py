import sys
import os
import pickle

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kernel_ablation.kernel_ablation import run_kernel_ablation
from svm_classification import run_svm_classification

def main():
    print("Loading Week 7 full input data snapshot...") # All data collected so far till Week 7 (initial data + 6 submitted queries)
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'wk7_input_data.pkl'))
    with open(data_path, "rb") as file:
        data = pickle.load(file)

    print("\n[STEP 1] Running Kernel Ablation Study...")
    top_kernels = run_kernel_ablation(data)

    print("\n[STEP 2] Performing Target Classification on Each Function (Top 25% NuSVM)...")
    run_svm_classification(data, top_kernels)

if __name__ == "__main__":
    main()
