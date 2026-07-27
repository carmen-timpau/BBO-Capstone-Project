"""Surrogate Modeling: Evaluation of Deep Ensembles of Neural Networks for Bayesian Optimization

Training and evaluating Deep Ensembles of  MLP Regressors for Black-Box function surrogate modelling in Bayesian Optimisation 
to capture epistemic uncertainty and improve surrogate robustness. 

This experiment was conducted on Week 7 input data to assess model accuracy and performance before potential deployment in 
Bayesian Optimization loop for next query prediction.

The performance metric for surrogate modeling that will be used to compare Deep Ensembles of Neural Networks with GPs as 
surrogate models for the Bayesian Optimisation of the 8 Black-Box functions will be Root Mean Squared Error (RMSE).
"""

import numpy as np
from sklearn.neural_network import MLPRegressor

def evaluate_deep_ensemble(X_train, y_train, X_test, n_ensemble_members=5):
    """
    Training multiple MLP Regressors with varied random seeds and averaging their predictions over the test set.
    """
    ensemble_preds = np.zeros((n_ensemble_members, len(X_test)))
    
    for member_idx in range(n_ensemble_members):
        mlp = MLPRegressor(
            hidden_layer_sizes=(32, 16),
            activation='relu',
            solver='adam',
            max_iter=1000,
            random_state=42 + member_idx
        )
        mlp.fit(X_train, y_train)
        ensemble_preds[member_idx] = mlp.predict(X_test)
        
    return np.mean(ensemble_preds, axis=0)
