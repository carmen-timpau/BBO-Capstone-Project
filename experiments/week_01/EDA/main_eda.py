"""
Main EDA Execution Script
Runs the data loading, statistical summaries, and visualization suite.
"""

from data_loader import load_data
from statistics import print_raw_data_and_stats
from visualizer import (
    plot_function_1,
    plot_function_2,
    plot_function_3,
    plot_function_4,
    plot_function_5,
    plot_function_6,
    plot_function_7,
    plot_function_8
)

def run_eda():
    # Load data from parent week_01 folder
    data = load_data("wk1_input_data.pkl")

    # Print raw values and statistics
    print_raw_data_and_stats(data)

    # Render exploratory plots
    print("\nGenerating EDA 3D-8D Visualizations...")
    plot_function_1(data)
    plot_function_2(data)
    plot_function_3(data)
    plot_function_4(data)
    plot_function_5(data)
    plot_function_6(data)
    plot_function_7(data)
    plot_function_8(data)

if __name__ == "__main__":
    run_eda()
