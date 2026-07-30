# Functions computing the acquisition function score

import numpy as np
from scipy.stats import norm

def upper_confidence_bound(
    mean: np.ndarray, std: np.ndarray, beta: float = 1.96
) -> np.ndarray:
    """Calculating Upper Confidence Bound (UCB) balancing exploitation and exploration"""
    return mean + beta * std

def thompson_sampling(
    mean: np.ndarray, cov: np.ndarray
) -> np.ndarray:
    """Calculating Thompson Sampling (TS) draw from GP posterior sample"""
    return np.random.multivariate_normal(mean, cov)
