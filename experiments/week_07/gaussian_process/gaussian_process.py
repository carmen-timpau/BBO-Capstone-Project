from sklearn.gaussian_process import GaussianProcessRegressor

def evaluate_gaussian_process(X_train, y_train, X_test, best_kernel):
    """
    Fitting a Gaussian Process Regressor using the winning kernel and predicting on the test set.
    """
    gp = GaussianProcessRegressor(
        kernel=best_kernel,
        alpha=0.0,
        normalize_y=True,
        n_restarts_optimizer=10,  # Increased restarts for better hyperparameter optimization
        random_state=42
    )
    gp.fit(X_train, y_train)
    return gp.predict(X_test)
