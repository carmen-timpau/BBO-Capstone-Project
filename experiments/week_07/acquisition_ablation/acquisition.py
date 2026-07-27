# Computing Scores for Acquisition Functions (Designed for Batch/Vector Inputs)
# Contains the Acquisition Functions Tested in Acquisition Ablation Study conducted in Week 6 BBO

import numpy as np
from scipy.stats import norm

def compute_acquisition_scores(X_candidates, gp, y_best, acq_type, param):
    """Computes rigorous acquisition values using GP posterior mean and std."""
    mu, sigma = gp.predict(X_candidates, return_std=True)
    sigma = np.maximum(sigma, 1e-9)
    
    if acq_type.upper() == "EI":
        improvement = mu - y_best - param
        z = improvement / sigma
        ei = improvement * norm.cdf(z) + sigma * norm.pdf(z)
        ei[sigma == 0.0] = 0.0
        return ei
    elif acq_type.upper() == "UCB":
        return mu + param * sigma
    elif acq_type.upper() == "PI":
        z = (mu - y_best - param) / sigma
        return norm.cdf(z)
    else:
        raise ValueError(f"Unknown acquisition type: {acq_type}")
