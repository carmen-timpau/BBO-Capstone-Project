"""Surrogate Modeling: Evaluation of Gaussian Processes for Bayesian Optimization

Training and evaluating Gaussian Process Regressors using ablation-tuned kernels for Black-Box function surrogate 
modelling in Bayesian Optimisation, to capture aleatoric and epistemic uncertainty and provide robust predictive distributions.

This experiment was conducted on Week 8 input data to assess model accuracy and performance before potential deployment in
Bayesian Optimization loop for next query prediction.

The performance metric for surrogate modeling that will be used to compare Gaussian Processes with Deep Ensembles of Neural Networks as
surrogate models for the Bayesian Optimisation of the 8 Black-Box functions will be Root Mean Squared Error (RMSE).
"""

from sklearn.gaussian_process import GaussianProcessRegressor

def is_noiseless_kernel(kernel):
    """Returns True if the kernel has no WhiteKernel component."""
    return "WhiteKernel" not in str(kernel)

def evaluate_gaussian_process(X_train, y_train, X_test, best_kernel):
    """
    Fitting a Gaussian Process Regressor using the winning kernel and predicting on the test set.
    """

    alpha_value = 1e-8 if is_noiseless_kernel(best_kernel) else 0.0
    
    gp = GaussianProcessRegressor(
        kernel=best_kernel,
        alpha=0.0,
        normalize_y=True,
        n_restarts_optimizer=10,
        random_state=42
    )
    gp.fit(X_train, y_train)
    return gp.predict(X_test)
