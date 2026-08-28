""" PCA Projection Computation Module [Same as in BBO Week 11]
--------------------------------------------------------------------------------------------
Computes PCA-based dimensionality reduction statistics for all functions with n_dims>2 (3–8), 
providing PCA coordinates, variance curves and the optimal number of Principal Components.
These are then used by the Scree Plotting and the K‑Means Cluster Scatter Grid Plotting modules.

This fits PCA once per function, evaluates the Per‑Component Explained Variance and Cumulative 
Variance, and determines the smallest number of Principal Components (2 or 3) that captures at 
least variance_threshold = 0.8 of the total variance. The #-of-PCs is capped at 3 even if the 
variance threshold is not met, as a 4th+ axis isn't plottable anyway.
""""

import numpy as np
from sklearn.decomposition import PCA

def compute_pca_projection(X_scaled, n_dims, variance_threshold=0.80,
                      min_components=2, max_components=3, max_components_for_scree=6):
    """
    Fitting PCA once per function and deciding, per-function, whether a 2D or 3D scatter representation 
    better captures the variance within the k-means cluster structures plotted for functions with n_dims>2.

    Returns: the full per-component/cumulative variance (for the Scree Plot, up to max_components_for_scree=6 
    principal components - to show broad overview of variance captured), the chosen component count for scatter 
    plotting, the cumulative variance captured at that count, and the PCA-transformed coordinates.
    """
                              
    n_scree_components = min(n_dims, max_components_for_scree)
    pca_full = PCA(n_components=n_scree_components, random_state=42)
    X_pca_full = pca_full.fit_transform(X_scaled)
    variance_ratio = pca_full.explained_variance_ratio_
    cumulative_variance = np.cumsum(variance_ratio)

    n_components_chosen = max_components
    upper = min(max_components, n_scree_components)
    for k in range(min_components, upper + 1):
        if cumulative_variance[k - 1] >= variance_threshold:
            n_components_chosen = k
            break
    n_components_chosen = min(n_components_chosen, n_scree_components)

    return {
        "variance_ratio": variance_ratio,
        "cumulative_variance": cumulative_variance,
        "n_components_chosen": n_components_chosen,
        "cumulative_variance_at_chosen": float(cumulative_variance[n_components_chosen - 1]),
        "X_pca": X_pca_full
    }
