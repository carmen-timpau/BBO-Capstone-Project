""" Scree Plotting Module
-------------------------------------------------------------------------
Generates Scree Plots to visualise the Per-Component Explained Variance bars + Cumulative Variance line
for each function with n_dims>2 (3-8), to rationalise the optimal number of Principal Components (2 or 3), 
chosen and used to represent the computed k-means clusters for each function in reduced dimensionality (2D/3D). 
"""

import os
import numpy as np
import matplotlib.pyplot as plt

def plot_pca_scree_grid(cluster_data_for_plot, variance_threshold=0.80,
                         output_dir="week_11/diagnostics_results",
                         filename="pca_scree_grid.png"):
    """
    Scree plotting (per-component explained variance bars + cumulative variance line) for n_dims>2 functions, 
    to visualise and rationalise the 2-vs-3 principal component choices used in the k-means cluster scatter grids. 
    2D-input functions have no PCA to show (the input space is the plot) and are marked not applicable (N/A).
    """
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    fig, axes = plt.subplots(2, 4, figsize=(22, 10))
    axes = axes.flatten()

    for idx in range(8):
        fn_idx = idx + 1
        fn_key = f"function_{fn_idx}"
        ax = axes[idx]

        if fn_key not in cluster_data_for_plot:
            ax.set_visible(False)
            continue

        info = cluster_data_for_plot[fn_key]
        pca_info = info.get("pca_info")
        n_dims = info["n_dims"]

        if pca_info is None:
            ax.text(0.5, 0.5, f"Function {fn_idx}\n({n_dims}D input)\nN/A, already <= 2D,\nno PCA needed",
                    ha="center", va="center", fontsize=10, transform=ax.transAxes)
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_title(f"Function {fn_idx}", fontsize=12, fontweight='bold')
            continue

        variance_ratio = pca_info["variance_ratio"]
        cumulative_variance = pca_info["cumulative_variance"]
        n_components_chosen = pca_info["n_components_chosen"]
        components = np.arange(1, len(variance_ratio) + 1)

        ax.bar(components, variance_ratio, color="steelblue", alpha=0.75, label="Per-component")
        ax.set_ylim(0, 1.05)
        ax2 = ax.twinx()
        ax2.plot(components, cumulative_variance, color="darkorange", marker="o",
                 linewidth=1.8, label="Cumulative")
        ax2.axhline(variance_threshold, color="gray", linestyle="-", linewidth=1.0,
                    label=f"{variance_threshold:.0%} threshold")
        ax2.axvline(n_components_chosen, color="red", linestyle=":", linewidth=1.5,
                    label=f"Chosen: {n_components_chosen} PC(s)")
        ax2.set_ylim(0, 1.05)

        ax.set_title(f"Function {fn_idx} ({n_dims}D input)", fontsize=12, fontweight='bold')
        ax.set_xlabel("Principal Component", fontsize=9)
        ax.set_ylabel("Explained Var. Ratio", fontsize=8.5)
        ax2.set_ylabel("Cumulative Var.", fontsize=8.5)
        ax.set_xticks(components)

        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='center right', fontsize=6, framealpha=0.85)

    plt.suptitle(
        f"PCA Scree Plots per Function (n_dims >= 3 only): Per-component and Cumulative Explained Variance \n"
        f"(smallest of 2-3 PCs reaching {variance_threshold:.0%} cumulative variance, capped at 3).",
        fontsize=13, fontweight='bold', y=0.98
    )
    plt.tight_layout(rect=[0, 0, 1, 0.94])
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f"PCA scree plot grid saved to '{filepath}'")
    plt.show()
