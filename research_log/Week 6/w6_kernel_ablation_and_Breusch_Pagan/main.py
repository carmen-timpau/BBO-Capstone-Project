import pickle
import runpy

print("Loading data snapshot...")
with open("wk6_input_data.pkl", "rb") as file:
    data = pickle.load(file) # Week 6 input data snapshot = all initial data + 5 submitted queries

print("\n1. Running Pre-Kernel Ablation Breusch-Pagan Test...") 
runpy.run_path("Breusch_Pagan_pre_ablation.py")

print("\n2. Running Kernel Ablation Study...")
runpy.run_path("kernel_ablation.py")

print("\n3. Running Post-Kernel Ablation Breusch-Pagan Test...")
runpy.run_path("Breusch_Pagan_post_ablation.py")

print("\n4. Running Acquisition Ablation Study...")
runpy.run_path("acquisition_ablation.py")

print("\n5. Generating Next Query Predictions...")
runpy.run_path("query_predict.py")

print("\nWeek 6 Bayesian Optimisation Pipeline execution complete!")
