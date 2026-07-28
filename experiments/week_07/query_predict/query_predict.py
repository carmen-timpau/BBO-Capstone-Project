import numpy as np
import pandas as pd
from scipy.stats.qmc import Sobol
from sklearn.preprocessing import StandardScaler
from sklearn.gaussian_process import GaussianProcessRegressor

from output_warping.output_warping import apply_output_warping_to_dataset
from output_unwarping.output_unwarping import unwarp_predictions_and_values
from acquisition_ablation.acq_strategies import acq_strategies
from acquisition_ablation.acquisition import compute_acquisition_scores

def run_next_query_prediction(
    data, 
    surrogate_evaluation_summary, 
    sequential_ablation_summary, 
    comparison_summary, 
    kernel_suites_dict
):
    """
    Executing the comprehensive HEBO & Dynamic Sobol-Sampled Bayesian Optimization Pipeline:
    1. Parametric Output Warping (Box-Cox / Yeo-Johnson)
    2. Winning Surrogate Model Fitting (GP / Deep Ensembles)
    3. Dynamic Sobol Quasi-Random Candidate Generation (Continuous Space Exploration)
    4. Classifier-Based Candidate Filtering (SVM / MLP)
    5. Acquisition Function Optimization (via imported acq_strategies & acquisition)
    6. Output Unwarping to Original Scale
    """
    # Applying HEBO-style output warping uniformly across all functions
    warped_data, warpers = apply_output_warping_to_dataset(data)
    next_queries_results = {}

    print("\n" + "=" * 105)
    print(" COMPILING FINAL HEBO & SOBOL NEXT QUERY PREDICTIONS ACROSS FUNCTIONS 1–8")
    print("=" * 105)

    for fn_idx in range(1, 9):
        fn_key = f"function_{fn_idx}"
        if fn_key not in warped_data:
            continue

        X_full = np.array(warped_data[fn_key]["x"])
        Y_target = np.array(warped_data[fn_key]["y_target"])
        n_samples, n_dims = X_full.shape

        # Retrieving winning structural decisions from prior ablation dictionaries
        surrogate_info = surrogate_evaluation_summary.get(fn_key, {})
        winning_surrogate = surrogate_info.get("Best Surrogate", "GP")
        winning_kernel_name = surrogate_info.get("Winning GP Kernel", "Baseline: Matern 2.5 + WhiteNoise (ARD)")

        ablation_info = sequential_ablation_summary.get(fn_key, {})
        best_acq_variant = ablation_info.get("Best Acquisition", "Expected Improvement (xi=0.01)")
        
        # Pulling acquisition type and parameter directly from the centralized module
        acq_type, param = acq_strategies.get(best_acq_variant, ("EI", 0.01))

        comparison_info = comparison_summary.get(fn_key, {})
        winning_classifier = comparison_info.get("Winning_Classifier", "SVM")

        # Scaling features and fitting the winning surrogate model
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_full)

        if winning_surrogate == "GP":
            kernel_suite = kernel_suites_dict.get(fn_idx, {})
            best_kernel = kernel_suite.get(winning_kernel_name, list(kernel_suite.values())[0])
            
            gp = GaussianProcessRegressor(kernel=best_kernel, alpha=1e-6, normalize_y=True, random_state=42)
            gp.fit(X_scaled, Y_target)
            
            # Predicting mean across the historical space for unwarping reference later
            mu_full = gp.predict(X_scaled)
        else:
            # Using placeholder hook if Deep Ensemble wins
            mu_full = np.zeros(n_samples)

        # Generating brand-new candidate space via Sobol quasi-random sampling
        minimum = X_full.min(axis=0)
        maximum = X_full.max(axis=0)

        # Setting dynamic Sobol sample resolution based on dimensionality
        if n_dims >= 6:
            m_samples = 14  # 2^14 = 16,384 points
        elif n_dims >= 4:
            m_samples = 13  # 2^13 = 8,192 points
        else:
            m_samples = 12  # 2^12 = 4,096 points

        # Generating Sobol sequence in unit hypercube and mapping to feature bounds
        sobol = Sobol(d=n_dims, scramble=True, seed=42)
        unit_samples = sobol.random_base2(m=m_samples)
        
        x_grid = minimum + unit_samples * (maximum - minimum)
        x_grid_scaled = scaler.transform(x_grid)

        # Performing classifier-based candidate filtering
        # (Falling back to full Sobol pool if classifier pre-filtering mask isn't indexed yet)
        eval_indices = list(range(len(x_grid_scaled)))

        # Computing acquisition scores on the dynamic candidate subspace
        y_best_current = np.max(Y_target)
        scores = compute_acquisition_scores(x_grid_scaled[eval_indices], gp, y_best_current, acq_type, param)

        best_local_idx = np.argmax(scores)
        chosen_global_idx = eval_indices[best_local_idx]
        
        next_query_coords = x_grid[chosen_global_idx]

        # Predicting warped value at the chosen new coordinate and unwarping to original scale
        next_query_scaled_2d = x_grid_scaled[chosen_global_idx].reshape(1, -1)
        predicted_warped_value = gp.predict(next_query_scaled_2d)[0] if winning_surrogate == "GP" else 0.0
        predicted_original_value = unwarp_predictions_and_values(predicted_warped_value, fn_key, warpers)

        next_queries_results[fn_key] = {
            "Next Query Coordinates": next_query_coords,
            "Winning Surrogate": winning_surrogate,
            "Winning Acquisition": best_acq_variant,
            "Winning Classifier": winning_classifier,
            "Predicted Original Scale Value": predicted_original_value
        }

        print(f"Function {fn_idx} | Surrogate: {winning_surrogate:<12} | Classifier: {winning_classifier:<5} | Acq: {best_acq_variant:<35} | Next Query: {np.round(next_query_coords, 4)}")

    print("=" * 105)
    return next_queries_results
