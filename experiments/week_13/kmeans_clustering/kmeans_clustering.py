""" K‑Means Clustering Diagnostics and Plotting Module [Same as in BBO Week 11 ML Pipeline]
---------------------------------------------------------------------------------------------------
'run_kmeans_clustering_diagnostics': Computes K‑means clustering for each Black-Box function (1–8);
selects the optimal number of clusters using the elbow heuristic; identifies the best cluster 
(which contains the current best‑observed point in the dataset), and constructs an expanded 
bounding box around that best cluster in the original input space for each function.

'plot_kmeans_cluster_grid': Plots K-means cluster assignments per function as a grid plot in 2D/3D.
The dimensionality of higher-dimensional functions is reduced using PCA via 'compute_pca_projection'. 
"""

import os
import numpy as np
import pickle
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from kmeans_clustering.elbow_analysis import find_elbow_k
from kmeans_clustering.elbow_analysis import plot_elbow_grid
from pca.pca_projection import compute_pca_projection
from pca.scree_plot import plot_pca_scree_grid


def run_kmeans_clustering_diagnostics(data, k_range=None, box_margin_fraction=0.1,
                                       k_range_overrides=None, make_plots=True,
                                       pca_variance_threshold=0.80,
                                       plot_output_dir="week_13/diagnostics_results"):
    """Running K-means clustering per function; Identifies the best cluster per function
    (which contains the highest outputs in the current dataset) and its bounding box in input space."""

    k_range_overrides = k_range_overrides or {}
    kmeans_results = {}

    elbow_data_for_plot = {}
    cluster_data_for_plot = {}

    print("=" * 110)
    print(" K-MEANS CLUSTERING DIAGNOSTICS: INPUT SPACE STRUCTURE + BEST-CLUSTER BOUNDING BOX")
    print("=" * 110)

    for fn_idx in range(1, 9):
        fn_key = f"function_{fn_idx}"
        if fn_key not in data:
            continue

        X_full = np.array(data[fn_key]["x"])
        Y_raw = np.array(data[fn_key]["y"]).flatten()
        n_samples, n_dims = X_full.shape

        if fn_idx == 1:
            positive_Y = Y_raw[Y_raw > 0]
            noise_floor = positive_Y.min()
            Y_safe = np.clip(Y_raw, noise_floor, None)
            Y_target = np.log10(Y_safe)
        else:
            Y_target = Y_raw

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_full)

        fn_k_range = k_range_overrides.get(fn_key, k_range)
        if fn_k_range is None:
            max_k = max(2, min(6, n_samples // 4 + 1))
            fn_k_range = list(range(1, max_k + 1))

        inertias = []
        labels_per_k = {}
        for k in fn_k_range:
            km = KMeans(n_clusters=k, n_init=10, random_state=42)
            km.fit(X_scaled)
            inertias.append(km.inertia_)
            labels_per_k[k] = km.labels_

        best_k = find_elbow_k(fn_k_range, inertias)
        labels = labels_per_k[best_k]

        idx_of_max = int(np.argmax(Y_target))
        best_cluster_id = int(labels[idx_of_max])

        cluster_mask = labels == best_cluster_id
        box_min = X_full[cluster_mask].min(axis=0)
        box_max = X_full[cluster_mask].max(axis=0)
        full_range = X_full.max(axis=0) - X_full.min(axis=0)
        margin = box_margin_fraction * full_range
        box_min_expanded = np.maximum(box_min - margin, X_full.min(axis=0))
        box_max_expanded = np.minimum(box_max + margin, X_full.max(axis=0))

        n_points_in_best_cluster = int(cluster_mask.sum())

        print(f"\n{fn_key.upper()} ({n_samples} samples, {n_dims}D): "
              f"k values tried={list(fn_k_range)}, elbow-selected k={best_k}")
        if best_k == 1:
            print(f"  [NOTE] Elbow selected k=1 - no meaningful cluster structure found. "
                  f"Bounding box defaults to the full domain.")
        else:
            print(f"  Best cluster (containing the current best-observed point): cluster "
                  f"{best_cluster_id} ({n_points_in_best_cluster} of {n_samples} points)")
            print(f"  Bounding box (original units, with {box_margin_fraction:.0%} margin): "
                  f"min={np.round(box_min_expanded, 4)}, max={np.round(box_max_expanded, 4)}")

        # PCA projection choice for the cluster-scatter plot is only relevant for functions with n_dims>2
        # 2D-input functions are plotted directly, no projection needed.
      
        if n_dims >= 3:
            pca_info = compute_pca_projection(X_scaled, n_dims, variance_threshold=pca_variance_threshold)
            print(f"  PCA (for cluster-plot projection): using {pca_info['n_components_chosen']} "
                  f"component(s) (captures {pca_info['cumulative_variance_at_chosen']:.1%} of "
                  f"variance; threshold={pca_variance_threshold:.0%}) - see scree plot for full curve.")
        else:
            pca_info = None

        kmeans_results[fn_key] = {
            "best_k": best_k,
            "labels": labels,
            "best_cluster_id": best_cluster_id,
            "bounding_box": (box_min_expanded, box_max_expanded),
            "n_points_in_best_cluster": n_points_in_best_cluster,
            "k_values_tried": list(fn_k_range),
            "inertias": inertias
        }

        elbow_data_for_plot[fn_key] = (list(fn_k_range), inertias, best_k)
        cluster_data_for_plot[fn_key] = {
            "X_scaled": X_scaled, "X_full": X_full, "labels": labels,
            "best_cluster_id": best_cluster_id, "n_dims": n_dims,
            "box": (box_min_expanded, box_max_expanded),
            "pca_info": pca_info
        }

    print("\n" + "=" * 110)
    print(" SUMMARY: K-MEANS RESULTS PER FUNCTION")
    print("=" * 110)
    for fn_key, res in kmeans_results.items():
        print(f"{fn_key.upper()}: k={res['best_k']}, best cluster has "
              f"{res['n_points_in_best_cluster']} point(s)")
    print("=" * 110)

    if make_plots:
        plot_elbow_grid(elbow_data_for_plot, output_dir=plot_output_dir)
        plot_pca_scree_grid(cluster_data_for_plot, variance_threshold=pca_variance_threshold,
                             output_dir=plot_output_dir)
        plot_kmeans_cluster_grid(cluster_data_for_plot, output_dir=plot_output_dir)

    checkpoint = {
        "kmeans_results": kmeans_results,
        "elbow_data_for_plot": elbow_data_for_plot,
        "cluster_data_for_plot": cluster_data_for_plot
        }

    with open("week13_kmeans_checkpoint.pkl", "wb") as f:
        pickle.dump(checkpoint, f)
    
    return kmeans_results


def plot_kmeans_cluster_grid(cluster_data_for_plot, output_dir="week_13/diagnostics_results",
                              filename="kmeans_cluster_grid.png"):
    """
    Plotting K-means cluster assignments per function as a grid plot in 2D/3D. n_dims>2 functions are projected 
    onto either 2 or 3 principal components chosen per-function in 'compute_pca_projection', based on explained 
    variance. n_dims=2 functions are plotted directly in scaled input space (no projection needed)."""
                                
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    fig = plt.figure(figsize=(24, 12))
    cluster_colors = plt.cm.tab10.colors

    for idx in range(8):
        fn_idx = idx + 1
        fn_key = f"function_{fn_idx}"

        if fn_key not in cluster_data_for_plot:
            continue

        info = cluster_data_for_plot[fn_key]
        X_scaled = info["X_scaled"]
        X_full = info["X_full"]
        labels = info["labels"]
        best_cluster_id = info["best_cluster_id"]
        n_dims = info["n_dims"]
        box_min, box_max = info["box"]
        pca_info = info.get("pca_info")

        use_3d = (pca_info is not None) and (pca_info["n_components_chosen"] == 3)
        ax = fig.add_subplot(2, 4, idx + 1, projection='3d' if use_3d else None)

        exact_box_plottable = (n_dims == 2)

        if pca_info is not None:
            n_components_chosen = pca_info["n_components_chosen"]
            X_plot = pca_info["X_pca"][:, :n_components_chosen]
            axis_note = (f" (PCA, {n_components_chosen}D, "
                         f"{pca_info['cumulative_variance_at_chosen']:.0%} var)")
        elif n_dims == 2:
            X_plot = X_scaled
            axis_note = ""
        else:
            X_plot = np.column_stack([X_scaled[:, 0], np.zeros(len(X_scaled))])
            axis_note = " (1D input)"

        for label in sorted(set(labels)):
            mask = labels == label
            color = cluster_colors[label % len(cluster_colors)]
            is_best = (label == best_cluster_id)
            marker_kwargs = dict(
                c=[color], marker="o",
                s=90 if is_best else 50,
                edgecolors="black" if is_best else "none",
                linewidths=1.8 if is_best else 0,
                alpha=0.9, label=f"Cluster {label}" + (" (best)" if is_best else "")
            )
            if use_3d:
                ax.scatter(X_plot[mask, 0], X_plot[mask, 1], X_plot[mask, 2], **marker_kwargs)
            else:
                ax.scatter(X_plot[mask, 0], X_plot[mask, 1], **marker_kwargs)

        if exact_box_plottable:
            from sklearn.preprocessing import StandardScaler as _SS
            _scaler = _SS().fit(X_full)
            box_min_scaled = _scaler.transform(box_min.reshape(1, -1))[0]
            box_max_scaled = _scaler.transform(box_max.reshape(1, -1))[0]
            rect = mpatches.Rectangle(
                (box_min_scaled[0], box_min_scaled[1]),
                box_max_scaled[0] - box_min_scaled[0],
                box_max_scaled[1] - box_min_scaled[1],
                linewidth=1.5, edgecolor="black", facecolor="none", linestyle="--"
            )
            ax.add_patch(rect)

        ax.set_title(f"Function {fn_idx}: k={len(set(labels))}", fontsize=12, fontweight='bold')
        ax.set_xlabel(f"Dim 1{axis_note}", fontsize=8)
        ax.set_ylabel("Dim 2", fontsize=8)
        if use_3d:
            ax.set_zlabel("Dim 3", fontsize=8)
        else:
            ax.grid(True, linestyle="--", alpha=0.4)
        ax.legend(loc='best', fontsize=6, framealpha=0.8)

    plt.suptitle(
        "K-Means Cluster Assignments per Function (best cluster outlined in black)",
        fontsize=12, fontweight='bold', y=0.98
    )
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f"Cluster assignment plot grid saved to '{filepath}'")
    plt.show()
