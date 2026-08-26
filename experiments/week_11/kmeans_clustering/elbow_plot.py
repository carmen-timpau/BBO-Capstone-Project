def plot_elbow_grid(elbow_data_for_plot, output_dir="week_11/diagnostics_results",
                     filename="kmeans_elbow_grid.png"):
    """Plotting the elbow curve (inertia vs. k) per function, marking the optimal, elbow-selected number of clusters k per function."""
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
