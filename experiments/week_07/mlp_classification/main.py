import sys
import os
import pickle

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mlp_classification.mlp_classification import run_mlp_classification

def main():
    print("Loading Week 7 full input data snapshot...") # All data collected so far till Week 7 (initial data + 6 submitted queries)
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'wk7_input_data.pkl'))
    with open(data_path, "rb") as file:
        data = pickle.load(file)

    print("\n[STEP 1] Performing Target Classification on Each Function (Top 25% MLP)...")
    run_mlp_classification(data)

    print("\nWeek 7 MLP Classification Pipeline execution complete!")

if __name__ == "__main__":
    main()
