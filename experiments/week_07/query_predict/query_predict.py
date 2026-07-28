import numpy as np
import pandas as pd
from scipy.stats.qmc import Sobol
from sklearn.preprocessing import StandardScaler
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.neural_network import MLPRegressor

from output_warping.output_warping import apply_output_warping_to_dataset
from output_unwarping.output_unwarping import unwarp_predictions_and_values
from acquisition_ablation.acq_strategies import acq_strategies
from acquisition_ablation.acquisition import compute_acquisition_scores

def run_next_query_prediction(
    data, 
    surrogate_evaluation_summary, 
    sequential_ablation_summary, 
    comparison_summary, 
    kernel_suites_dict,
    trained_classifiers_dict=None,
    n_ensemble_members=5
):
    """
    Executing the comprehensive HEBO, Dynamic Sobol-Sampled, & Classifier-Filtered Bayesian Optimization Pipeline:
    1. Parametric Output Warping (Box-Cox / Yeo-Johnson)
    2. Winning Surrogate Model Fitting (GP / Deep Ensembles, optimised previously)
    3. Dynamic Sobol Quasi-Random Candidate Generation (Continuous Space Exploration)
    4. Classifier-Based Sobol Candidate Filtering (Active SVM / MLP Filtering, optimised previously)
    5. Acquisition Function (optimised previously) Evaluation and Scoring of SVM/MLP Filtered Sobol Samples
    6. Output Unwarping to Original Scale
    """
    # Applying HEBO-style output warping uniformly across all functions
    warped_data, warpers = apply_output_warping_to_dataset(data)
    next_queries_results = {}

    print("\n" + "=" * 115)
    print(" COMPILING FINAL HEBO, SOBOL, & CLASSIFIER-FILTERED NEXT QUERY PREDICTIONS ACROSS FUNCTIONS 1–8")
    print("=" * 115)

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

            class GPDuckTypeWrapper:
                def __init__(self, gp_model):
                    self.gp_model = gp_model
                def predict(self, X, return_std=False):
                    return self.gp_model.predict(X, return_std=return_std)

            active_surrogate = GPDuckTypeWrapper(gp)

            def predict_single(X_cand_2d):
                return gp.predict(X_cand_2d)[0]
        else:
            # Training an ensemble of MLP regressors to capture epistemic uncertainty if Deep Ensemble wins
            ensemble_models = []
            for member_idx in range(n_ensemble_members):
                mlp = MLPRegressor(
                    hidden_layer_sizes=(32, 16),
                    activation='relu',
                    solver='adam',
                    max_iter=1000,
                    random_state=42 + member_idx
                )
                mlp.fit(X_scaled, Y_target)
                ensemble_models.append(mlp)

            class DeepEnsembleDuckTypeWrapper:
                def __init__(self, models):
                    self.models = models
                def predict(self, X, return_std=False):
                    preds = np.array([m.predict(X) for m in self.models])
                    mu = np.mean(preds, axis=0)
                    if return_std:
                        sigma = np.std(preds, axis=0)
                        return mu, sigma
                    return mu

            active_surrogate = DeepEnsembleDuckTypeWrapper(ensemble_models)
            mu_full = active_surrogate.predict(X_scaled)

            def predict_single(X_cand_2d):
                preds = np.array([m.predict(X_cand_2d) for m in ensemble_models])
                return np.mean(preds, axis=0)[0]

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

        # Performing active classifier-based candidate filtering
        eval_indices = []
        if trained_classifiers_dict is not None and fn_key in trained_classifiers_dict:
            classifier_model, pca_transformer = trained_classifiers_dict[fn_key]
            
            # Projecting Sobol points into the same PCA space used during classification training
            x_grid_pca = pca_transformer.transform(x_grid_scaled)
            
            # Predicting classes for all Sobol candidates (Class 1 = top 25% promising region)
            class_predictions = classifier_model.predict(x_grid_pca)
            eval_indices = np.where(class_predictions == 1)[0]

        # Falling back to full Sobol pool if no classifier is passed or filter returns an empty set
        if len(eval_indices) == 0:
            eval_indices = list(range(len(x_grid_scaled)))

        # Computing acquisition scores on the filtered dynamic candidate subspace
        y_best_current = np.max(Y_target)
        scores = compute_acquisition_scores(x_grid_scaled[eval_indices], active_surrogate, y_best_current, acq_type, param)

        best_local_idx = np.argmax(scores)
        chosen_global_idx = eval_indices[best_local_idx]
        
        # Capturing brand-new, unvisited global coordinates
        next_query_coords = x_grid[chosen_global_idx]

        # Predicting warped value at the chosen new coordinate and unwarping to original scale
        next_query_scaled_2d = x_grid_scaled[chosen_global_idx].reshape(1, -1)
        predicted_warped_value = predict_single(next_query_scaled_2d)
        predicted_original_value = unwarp_predictions_and_values(predicted_warped_value, fn_key, warpers)

        next_queries_results[fn_key] = {
            "Next Query Coordinates": next_query_coords,
            "Winning Surrogate": winning_surrogate,
            "Winning Acquisition": best_acq_variant,
            "Winning Classifier": winning_classifier,
            "Predicted Original Scale Value": predicted_original_value
        }

        print(f"Function {fn_idx} | Surrogate: {winning_surrogate:<12} | Classifier: {winning_classifier:<5} | Acq: {best_acq_variant:<35} | Next Query: {np.round(next_query_coords, 6)}")

    print("=" * 115)
    return next_queries_results
