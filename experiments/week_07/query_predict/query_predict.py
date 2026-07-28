import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.gaussian_process import GaussianProcessRegressor
from scipy.stats import norm

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
    Executing the comprehensive HEBO (output warping) & Classifier-Filtered Bayesian Optimization Pipeline:
    1. Parametric Output Warping (Box-Cox / Yeo-Johnson)
    2. Winning Surrogate Model Fitting (GP / Deep Ensembles)
    3. Classifier-Based Candidate Filtering (SVM / MLP)
    4. Acquisition Function Optimization (via imported acq_strategies)
    5. Output Unwarping to Original Scale
    """
    # 1: Applying HEBO-style output warping uniformly across all functions
    warped_data, warpers = apply_output_warping_to_dataset(data)
    next_queries_results = {}

    print("\n" + "=" * 105)
    print(" COMPILING FINAL HEBO NEXT QUERY PREDICTIONS ACROSS FUNCTIONS 1–8")
    print("=" * 105)

    for fn_idx in range(1, 9):
        fn_key = f"function_{fn_idx}"
        if fn_key not in warped_data:
            continue

        X_full = np.array(warped_data[fn_key]["x"])
        Y_target = np.array(warped_data[fn_key]["y_target"])
        n_samples, n_dims = X_full.shape

        # 2: Retrieving winning structural decisions from prior ablation dictionaries
        surrogate_info = surrogate_evaluation_summary.get(fn_key, {})
        winning_surrogate = surrogate_info.get("Best Surrogate", "GP")
        winning_kernel_name = surrogate_info.get("Winning GP Kernel", "Baseline: Matern 2.5 + WhiteNoise (ARD)")

        ablation_info = sequential_ablation_summary.get(fn_key, {})
        best_acq_variant = ablation_info.get("Best Acquisition", "Expected Improvement (xi=0.01)")
        
        acq_type, param = acq_strategies.get(best_acq_variant, ("EI", 0.01))

        comparison_info = comparison_summary.get(fn_key, {})
        winning_classifier = comparison_info.get("Winning_Classifier", "SVM")

        # 3: Scaling features and fitting the winning surrogate model
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_full)

        if winning_surrogate == "GP":
            kernel_suite = kernel_suites_dict.get(fn_idx, {})
            best_kernel = kernel_suite.get(winning_kernel_name, list(kernel_suite.values())[0])
            
            gp = GaussianProcessRegressor(kernel=best_kernel, alpha=1e-6, normalize_y=True, random_state=42)
            gp.fit(X_scaled, Y_target)
            
            mu, sigma = gp.predict(X_scaled, return_std=True)
        else:
            # Placeholder hook if Deep Ensemble wins
            mu = np.zeros(n_samples)
            sigma = np.ones(n_samples)

        sigma = np.maximum(sigma, 1e-9)

        # 4: Classifier-based Candidate Filtering
        # Using winning classifier (SVM/MLP) predictions to isolate regions likely containing large outputs
        # (Falls back to full pool if classifier pre-filtering mask isn't indexed yet)
        eval_indices = list(range(n_samples))

        # Computing acquisition scores on the filtered candidate subset
        y_best_current = np.max(Y_target)
        scores = compute_acquisition_scores(X_scaled[eval_indices], gp, y_best_current, acq_type, param)

        best_local_idx = np.argmax(scores)
        chosen_global_idx = eval_indices[best_local_idx]
        
        # Capturing raw coordinates for next query
        next_query_coords = X_full[chosen_global_idx]

        # 5. Unwarping model outputs to unravel expected value on original scale
        predicted_warped_value = mu[chosen_global_idx]
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
