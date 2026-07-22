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

def upper_confidence_bound(
    mean: np.ndarray, std: np.ndarray, beta: float = 1.96
) -> np.ndarray:
    """Calculating Upper Confidence Bound (UCB)"""
    return mean + beta * std
