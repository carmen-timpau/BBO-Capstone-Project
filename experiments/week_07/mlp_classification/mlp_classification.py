"""Data Quality Control: MLP Classification for Bayesian Optimization

Training MLPClassifier models on Week 7 input data (top 25% highest output datapoints within each functions' dataset) 
to establish a boundary between high-quality and low-quality data points. This evaluation was conducted to potentially 
better inform query selection via Bayesian Optimization.

Using Stratified 3-Fold Cross-Validation ROC-AUC (Receiver Operating Characteristic - Area Under Curve) as a classification performance metric
for comparison of MLP classification performance with that of NuSVC models. 
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score

def run_mlp_classification(data):
    """
    Training an MLPClassifier on the top 25% target region for each of the 8 black-box functions, 
    annotating boundary-adjacent points, and plotting their 2D PCA decision probability landscapes.
    """
    # Setting up Stratified 3-Fold Cross-Validation for robust classification performance evaluation
    cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

    # List to keep track of ROC-AUC scores for each function to calculate the mean later
    auc_scores = []

    # Setting up subplots for Functions 1 to 8 (2 rows, 4 columns)
    fig, axes = plt.subplots(2, 4, figsize=(24, 12))
    axes = axes.flatten()

    for fn_idx in range(1, 9):
        fn_key = f"function_{fn_idx}"
        ax = axes[fn_idx - 1]
        
        if fn_key not in data:
            ax.set_title(f"{fn_key}: Missing Data")
            ax.axis('off')
            continue

        # Extracting Data
        X = np.array(data[fn_key]["x"])
        Y = np.array(data[fn_key]["y"]).flatten()
        n_samples, n_dims = X.shape

        # Applying Function 1 specific log transformation 
        if fn_idx == 1:
            Y_target = np.log10(np.clip(Y, 1e-300, None))
        else:
            Y_target = Y

        # Scaling features and project high-D space -> 2D via PCA
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        pca = PCA(n_components=2, random_state=42)
        X_pca = pca.fit_transform(X_scaled)

        # Labelling top 25% target region (75th percentile threshold)
        y_threshold = np.quantile(Y_target, 0.75)
        Y_binary = (Y_target >= y_threshold).astype(int)

        if len(np.unique(Y_binary)) < 2:
            ax.text(0.5, 0.5, f"Function {fn_idx}\n(Insufficient class variance)", 
                    horizontalalignment='center', verticalalignment='center')
            ax.set_title(f"Func {fn_idx}")
            continue

        # Out-of-Sample CV Evaluation for Robust ROC-AUC using MLP
        oof_preds = np.zeros(n_samples)
        for train_idx, test_idx in cv.split(X_pca, Y_binary):
            X_train, X_test = X_pca[train_idx], X_pca[test_idx]
            y_train, y_test = Y_binary[train_idx], Y_binary[test_idx]
            
            fold_mlp = MLPClassifier(
                hidden_layer_sizes=(32, 16), 
                activation='relu', 
                solver='adam', 
                max_iter=1000, 
                random_state=42
            )
            fold_mlp.fit(X_train, y_train)
            oof_preds[test_idx] = fold_mlp.predict_proba(X_test)[:, 1]

        cv_auc_score = roc_auc_score(Y_binary, oof_preds)
        
        # Storing the score for the final mean calculation
        auc_scores.append(cv_auc_score)

        # Fitting final MLP model on ALL data for visual boundary plotting
        mlp = MLPClassifier(
            hidden_layer_sizes=(32, 16), 
            activation='relu', 
            solver='adam', 
            max_iter=1000, 
            random_state=42
        )
        mlp.fit(X_pca, Y_binary)

        # Creating grid for plotting decision probability landscape
        padding = 0.8  
        x_min, x_max = X_pca[:, 0].min() - padding, X_pca[:, 0].max() + padding
        y_min, y_max = X_pca[:, 1].min() - padding, X_pca[:, 1].max() + padding

        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)

        xx, yy = np.meshgrid(np.linspace(x_min, x_max, 150), np.linspace(y_min, y_max, 150))
        grid_2d = np.c_[xx.ravel(), yy.ravel()]
        
        # Class 1 probabilities across the grid landscape
        probs = mlp.predict_proba(grid_2d)[:, 1].reshape(xx.shape)

        # Plotting individual function panels
        contour = ax.contourf(xx, yy, probs, levels=20, cmap='plasma', alpha=0.7)
        
        # Decision boundary where probability equals 0.5
        ax.contour(xx, yy, probs, levels=[0.5], colors='cyan', linewidths=2.0, linestyles='--')

        # Scatter plot of actual data points colored by observed target values
        scatter = ax.scatter(
            X_pca[:, 0], X_pca[:, 1],
            c=Y_target, cmap='viridis', edgecolors='black', s=60, zorder=5
        )

        # Highlighting and annotating points closest to the 0.5 decision boundary (analogous to support vector behavior)
        decision_probs = mlp.predict_proba(X_pca)[:, 1]
        boundary_mask = np.abs(decision_probs - 0.5) <= 0.05
        boundary_indices = np.where(boundary_mask)[0]

        if len(boundary_indices) > 0:
            ax.scatter(
                X_pca[boundary_indices, 0], X_pca[boundary_indices, 1],
                s=140, facecolors='none', edgecolors='white', linewidths=1.5, zorder=6
            )
            
            for idx in boundary_indices:
                ax.annotate(
                    f"Y={Y_target[idx]:.2f}",
                    (X_pca[idx, 0], X_pca[idx, 1]),
                    xytext=(3, 3), textcoords='offset points',
                    fontsize=6, fontweight='normal', color='yellow',
                    bbox=dict(boxstyle="round,pad=0.1", fc="black", alpha=0.6)
                )

        # Annotating top 2 performing points
        top_indices = np.argsort(Y_target)[-2:]
        for idx in top_indices:
            ax.annotate(
                f"Top: Y={Y_target[idx]:.2f}",
                (X_pca[idx, 0], X_pca[idx, 1]),
                xytext=(5, 5), textcoords='offset points',
                fontsize=8, fontweight='bold', color='white',
                bbox=dict(boxstyle="round,pad=0.1", fc="black", alpha=0.8)
            )

        var_exp = pca.explained_variance_ratio_ * 100
        ax.set_xlabel(f'PC1 ({var_exp[0]:.2f}%)', fontsize=9)
        ax.set_ylabel(f'PC2 ({var_exp[1]:.2f}%)', fontsize=9)
        ax.set_title(f'Function {fn_idx} (MLP Top 25%), PCA Projection Space\nStratified 3-Fold Cross-Validation ROC-AUC: {cv_auc_score:.3f}', fontsize=11, fontweight='bold')
        ax.grid(True, linestyle=':', alpha=0.4)

    plt.tight_layout()

    # Calculating and printing the mean ROC-AUC across all successfully evaluated functions
    if auc_scores:
        mean_auc = np.mean(auc_scores)
        print(f"\nMean Stratified 3-Fold CV ROC-AUC across evaluated functions: {mean_auc:.3f}")

    # Saving the multi-panel figure as a high-resolution PNG file
    output_filename = 'wk7_inputdata_mlp_boundaries_all_functions.png'
    fig.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"MLP classification boundary plots successfully saved to '{output_filename}'")
    
    plt.show()
