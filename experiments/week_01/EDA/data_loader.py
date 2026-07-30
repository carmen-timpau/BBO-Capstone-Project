"""
Data Loader Module
Handles loading the pickle dataset from the parent week_01 folder.
"""

import pickle
import os

def load_data(filename: str = "wk1_input_data.pkl") -> dict:
    """Loading binary pickle file from the parent directory."""
    # Constructing path to look one directory up
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "..", filename)
    
    print(f"Locating dataset at '{file_path}'...")
    
    try:
        with open(file_path, "rb") as f:
            data = pickle.load(f)
        print("Data loaded successfully!\n")
        return data
    except FileNotFoundError:
        print(f"Error: Could not find '{file_path}'. Double-check that it is in the week_01 folder.")
        raise
