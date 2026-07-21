import pickle
from Breusch_Pagan_pre_ablation import run_pre_bp
from kernel_ablation import run_kernel_ablation
from Breusch_Pagan_post_ablation import run_post_bp
from acquisition_ablation import run_acq_ablation
from query_predict import run_predictions

def main():
    print("Loading Week 6 full input data snapshot...") # All data collected so far till Week 6 (initial data + 5 submitted queries)
    with open("wk6_input_data.pkl", "rb") as file:
        data = pickle.load(file) 

    print("\n[STEP 1] Running Pre-Kernel Ablation Breusch-Pagan Test...")
    run_pre_bp(data)

    print("\n[STEP 2] Running Kernel Ablation Study...")
    top_kernels = run_kernel_ablation(data)

    print("\n[STEP 3] Running Post-Kernel Ablation Breusch-Pagan Test...")
    run_post_bp(data, top_kernels)

    print("\n[STEP 4] Running Acquisition Ablation Study...")
    best_acquisitions = run_acq_ablation(data, top_kernels)

    print("\n[STEP 5] Generating Next Query Predictions...")
    next_queries = run_predictions(data, top_kernels, best_acquisitions)

    print("\nWeek 6 Bayesian Optimisation Pipeline execution complete!")

if __name__ == "__main__":
    main()
