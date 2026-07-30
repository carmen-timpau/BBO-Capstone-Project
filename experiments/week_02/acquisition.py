# Function computing the acquisition function score

import numpy as np

def upper_confidence_bound(
    mean: np.ndarray, std: np.ndarray, beta: float = 1.96
) -> np.ndarray:
    """Calculating Upper Confidence Bound (UCB) balancing exploitation and exploration"""
    return mean + beta * std
