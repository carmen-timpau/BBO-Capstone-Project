import pickle
from kernel_ablation import run_kernel_ablation
from svm_classification import run_svm_classification

def main():
    print("Loading Week 7 full input data snapshot...") # All data collected so far till Week 7 (initial data + 6 submitted queries)
    with open("wk7_input_data.pkl", "rb") as file:
        data = pickle.load(file) 

    print("\n[STEP 1] Running Kernel Ablation Study...")
    top_kernels = run_kernel_ablation(data)

    print("\n[STEP 2] Performing Target Classification on Each Function (Top 25% NuSVM)...")
    run_svm_classification(data, top_kernels)

if __name__ == "__main__":
    main()
