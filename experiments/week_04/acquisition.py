# Functions computing the acqusition function score

import numpy as np
from scipy.stats import norm

def expected_improvement(
    mean: np.ndarray, std: np.ndarray, y_max: float, xi: float = 0.1
) -> np.ndarray:
    """Calculating Expected Improvement (EI) with safely handling of zero posterior std"""
    improvement = mean - y_max - xi
    z = np.where(std > 0, improvement / std, 0.0)

    ei = np.where(
        std > 0, improvement * norm.cdf(z) + std * norm.pdf(z), 0.0
    )
    return ei

def thompson_sampling(
    mean: np.ndarray, cov: np.ndarray
) -> np.ndarray:
    """Calculating Thompson Sampling (TS) draw from GP posterior sample"""
    return np.random.multivariate_normal(mean, cov)
