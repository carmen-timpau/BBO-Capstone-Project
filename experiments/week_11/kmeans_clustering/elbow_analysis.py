""" Elbow Analysis Module (Computation + Plotting)
-------------------------------------------------------------------------
'find_elbow_k' identifies the optimal number of K-Means clusters k for 
each function, using the 'distance-to-chord' elbow detection heuristic.

'plot_elbow_grid visualises the elbow curves (inertia vs. k) per function 
and marks the elbow‑selected number of clusters returned by 'find_elbow_k'.
"""

import os
import numpy as np
import matplotlib.pyplot as plt


def find_elbow_k(k_values, inertias):
    """Standard 'distance-to-chord' elbow detection."""
    k_arr = np.array(k_values, dtype=float)
    inertia_arr = np.array(inertias, dtype=float)

    x = (k_arr - k_arr.min()) / (k_arr.max() - k_arr.min() + 1e-12)
    y = (inertia_arr - inertia_arr.min()) / (inertia_arr.max() - inertia_arr.min() + 1e-12)

    p1 = np.array([x[0], y[0]])
    p2 = np.array([x[-1], y[-1]])
    line_vec = p2 - p1
    line_len = np.linalg.norm(line_vec)
    line_unit = line_vec / (line_len + 1e-12)

    distances = []
    for xi, yi in zip(x, y):
        p = np.array([xi, yi]) - p1
        proj_len = np.dot(p, line_unit)
        proj_point = proj_len * line_unit
        perp = p - proj_point
        distances.append(np.linalg.norm(perp))

    elbow_idx = int(np.argmax(distances))
    return int(k_arr[elbow_idx])
  

def plot_elbow_grid(elbow_data_for_plot, output_dir="week_11/diagnostics_results",
                     filename="kmeans_elbow_grid.png"):
    """Plotting the elbow curve (inertia vs. k) per function, marking the optimal, 
    elbow-selected number of clusters k per function."""
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    fig, axes = plt.subplots(2, 4, figsize=(22, 10))
    axes = axes.flatten()

    for idx in range(8):
        fn_idx = idx + 1
        fn_key = f"function_{fn_idx}"
        ax = axes[idx]

        if fn_key not in elbow_data_for_plot:
            ax.set_visible(False)
            continue

        k_values, inertias, best_k = elbow_data_for_plot[fn_key]
        ax.plot(k_values, inertias, marker="o", linewidth=1.5, color="steelblue")
        ax.axvline(best_k, color="red", linestyle="--", linewidth=1.2, label=f"Elbow k={best_k}")
        ax.set_title(f"Function {fn_idx}", fontsize=13, fontweight='bold')
        ax.set_xlabel("k (clusters)", fontsize=10)
        ax.set_ylabel("Inertia", fontsize=10)
        ax.grid(True, linestyle="--", alpha=0.4)
        ax.legend(loc='upper right', fontsize=8)

    plt.suptitle("K-Means Elbow Curves per Function (k selected via distance-to-chord heuristic)",
                 fontsize=15, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f"\nElbow plot grid saved to '{filepath}'")
    plt.show()
