"""
Week 1 BBO - Configurations Module

Hyperparameter configurations, kernel selections, and acquisition strategies for black-box 
functions 1 through 8. Used to generate query predictions in Week 1 of the BBO Capstone Project.
"""

from sklearn.gaussian_process.kernels import RBF

def get_function_configs():
    """Returning configurations dictionary for each of the 8 Black-Box functions (Week 1)."""
    
    return {
        1: {
            "kernel": RBF(length_scale=[0.1, 0.1]),  # Default length_scale_bounds
            "alpha": 1e-10,
            "acq_type": "UCB",       # Upper Confidence Bound
            "acq_param": 1.96,
            "sobol_m": 12,           # Note: Functions 1 & 2 used grid sampling, but grid can be represented via Sobol or specialized grid logic if preferred. Using 12 here for consistency.
            "normalize_y": False,
        },
        2: {
            "kernel": RBF(length_scale=[0.1, 0.1]),  # Default length_scale_bounds
            "alpha": 1e-10,
            "acq_type": "UCB",       # Upper Confidence Bound
            "acq_param": 1.96,
            "sobol_m": 12,
            "normalize_y": False,
        },
        3: {
            "kernel": RBF(length_scale=[0.1, 0.1, 0.1]),  # Default length_scale_bounds
            "alpha": 1e-10,
            "acq_type": "UCB",       # Upper Confidence Bound
            "acq_param": 1.96,
            "sobol_m": 12,
            "normalize_y": False,
        },
        4: {
            "kernel": RBF(length_scale=[0.1, 0.1, 0.1, 0.1]),  # Default length_scale_bounds
            "alpha": 1e-10,
            "acq_type": "UCB",       # Upper Confidence Bound
            "acq_param": 1.96,
            "sobol_m": 13,
            "normalize_y": False,
        },
        5: {
            "kernel": RBF(length_scale=[0.1, 0.1, 0.1, 0.1]),  # Default length_scale_bounds
            "alpha": 1e-10,
            "acq_type": "UCB",       # Upper Confidence Bound
            "acq_param": 1.96,
            "sobol_m": 13,
            "normalize_y": False,
        },
        6: {
            "kernel": RBF(length_scale=[0.1, 0.1, 0.1, 0.1, 0.1]),  # Default length_scale_bounds
            "alpha": 1e-10,
            "acq_type": "UCB",       # Upper Confidence Bound
            "acq_param": 1.96,
            "sobol_m": 13,
            "normalize_y": False,
        },
        7: {
            "kernel": RBF(length_scale=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1]),  # Default length_scale_bounds
            "alpha": 1e-10,
            "acq_type": "UCB",       # Upper Confidence Bound
            "acq_param": 1.96,
            "sobol_m": 13,
            "normalize_y": False,
        },
        8: {
            "kernel": RBF(length_scale=[1.0] * 8, length_scale_bounds=(1e-6, 1e8)),  # Conservative baseline with wider bounds
            "alpha": 1e-10,
            "acq_type": "UCB",       # Upper Confidence Bound
            "acq_param": 1.96,
            "sobol_m": 13,
            "normalize_y": False,
        },
    }
