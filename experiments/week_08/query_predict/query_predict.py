import numpy as np
from scipy.stats.qmc import Sobol
from sklearn.preprocessing import StandardScaler
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.neural_network import MLPRegressor

from output_warping.output_warping import apply_output_warping_to_dataset
from output_unwarping.output_unwarping import unwarp_predictions_and_values
from acquisition_ablation.acq_strategies import acq_strategies
from acquisition_ablation.acquisition import compute_acquisition_scores

def is_noiseless_kernel(kernel):
    """Returns True if the kernel has no WhiteKernel component."""
    return "WhiteKernel" not in str(kernel)

def run_next_query_prediction(
    data,
    surrogate_evaluation_summary,
    sequential_ablation_summary,
    kernel_suites_dict,
    n_ensemble_members=5
):
    """
    Executing the HEBO-inspired, Dynamic Sobol-Sampled Bayesian Optimization Pipeline:
    1. Parametric Output Warping (Box-Cox / Yeo-Johnson)
    2. Winning Surrogate Model Fitting (GP / Deep Ensemble, chosen previously)
    3. Dynamic Sobol Quasi-Random Candidate Generation (Continuous Space Exploration)
    4. Acquisition Function (chosen previously) Evaluation and Scoring of Sobol Samples
    5. Output Unwarping to Original Scale
    """
    warped_data, warpers = apply_output_warping_to_dataset(data)
    next_queries_results = {}

    print("\n" + "=" * 115)
    print(" COMPILING FINAL HEBO & SOBOL-BASED NEXT QUERY PREDICTIONS ACROSS FUNCTIONS 1–8")
    print("=" * 115)

    for fn_idx in range(1, 9):
        fn_key = f"function_{fn_idx}"
        if fn_key not in warped_data:
            continue

        X_full = np.array(warped_data[fn_key]["x"])
        Y_target = np.array(warped_data[fn_key]["y_target"])
        n_samples, n_dims = X_full.shape

        surrogate_info = surrogate_evaluation_summary.get(fn_key, {})
        winning_surrogate = surrogate_info.get("Best Surrogate", "GP")
        winning_kernel_name = surrogate_info.get("Winning GP Kernel", "Baseline: Matern 2.5 + WhiteNoise (ARD)")

        ablation_info = sequential_ablation_summary.get(fn_key, {})
        best_acq_variant = ablation_info.get("Best Acquisition", "Expected Improvement (xi=0.01)")

        acq_type, param = acq_strategies.get(best_acq_variant, ("EI", 0.01))

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_full)

        if winning_surrogate == "GP":
            kernel_suite = kernel_suites_dict.get(fn_key, {})
            best_kernel = kernel_suite.get(winning_kernel_name, list(kernel_suite.values())[0])

            alpha_value = 1e-8 if is_noiseless_kernel(best_kernel) else 0.0
            gp = GaussianProcessRegressor(kernel=best_kernel, alpha=alpha_value, normalize_y=True, n_restarts_optimizer=10, random_state=42)
            gp.fit(X_scaled, Y_target)

            class GPDuckTypeWrapper:
                def __init__(self, gp_model):
                    self.gp_model = gp_model
                def predict(self, X, return_std=False):
                    return self.gp_model.predict(X, return_std=return_std)

            active_surrogate = GPDuckTypeWrapper(gp)

            def predict_single(X_cand_2d):
                return gp.predict(X_cand_2d)[0]
        else:
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

            def predict_single(X_cand_2d):
                preds = np.array([m.predict(X_cand_2d) for m in ensemble_models])
                return np.mean(preds, axis=0)[0]

        minimum = X_full.min(axis=0)
        maximum = X_full.max(axis=0)

        if n_dims >= 6:
            m_samples = 14
        elif n_dims >= 4:
            m_samples = 13
        else:
            m_samples = 12

        sobol = Sobol(d=n_dims, scramble=True, seed=42)
        unit_samples = sobol.random_base2(m=m_samples)

        x_grid = minimum + unit_samples * (maximum - minimum)
        x_grid_scaled = scaler.transform(x_grid)

        # No classifier-based filtering in Week 8 — score the full Sobol candidate pool directly
        y_best_current = np.max(Y_target)
        scores = compute_acquisition_scores(x_grid_scaled, active_surrogate, y_best_current, acq_type, param)

        chosen_global_idx = np.argmax(scores)
        next_query_coords = x_grid[chosen_global_idx]

        next_query_scaled_2d = x_grid_scaled[chosen_global_idx].reshape(1, -1)
        predicted_warped_value = predict_single(next_query_scaled_2d)
        predicted_original_value = unwarp_predictions_and_values(predicted_warped_value, fn_key, warpers)

        next_queries_results[fn_key] = {
            "Next Query Coordinates": next_query_coords,
            "Winning Surrogate": winning_surrogate,
            "Winning Acquisition": best_acq_variant,
            "Predicted Original Scale Value": predicted_original_value
        }

        print(f"Function {fn_idx} | Next Query: {np.round(next_query_coords, 6)} | Surrogate: {winning_surrogate:<12} | Acq: {best_acq_variant:<35}")

    print("=" * 115)
    return next_queries_results
