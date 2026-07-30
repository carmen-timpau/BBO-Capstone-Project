"""
Week 2 BBO - Configurations Module

Hyperparameter configurations, kernel selections, and acquisition strategies for black-box 
functions 1 through 8. Used to generate query predictions in Week 2 of the BBO Capstone Project.
"""

from sklearn.gaussian_process.kernels import RBF, Matern

def get_function_configs():
    """Returning configurations dictionary for each of the 8 Black-Box functions (Week 2)."""
    
    return {
        1: {
            "kernel": Matern(length_scale=[0.1, 0.1], nu=1.5, length_scale_bounds=(1e-6, 1e8)),
            "alpha": 1e-4,
            "acq_type": "UCB",       # Upper Confidence Bound
            "acq_param": 4.0,        # Higher beta for increased exploration
            "sobol_m": 12,
            "normalize_y": True,
        },
        2: {
            "kernel": RBF(length_scale=[0.1, 0.1], length_scale_bounds=(1e-6, 1e8)),
            "alpha": 1e-10,
            "acq_type": "UCB",       # Upper Confidence Bound
            "acq_param": 1.96,
            "sobol_m": 12,
            "normalize_y": False,
        },
        3: {
            "kernel": RBF(length_scale=[1.0, 1.0, 1.0], length_scale_bounds=(1e-6, 1e8)),
            "alpha": 1e-10,
            "acq_type": "UCB",       # Upper Confidence Bound
            "acq_param": 1.96,
            "sobol_m": 12,
            "normalize_y": False,
        },
        4: {
            "kernel": RBF(length_scale=[0.1] * 4, length_scale_bounds=(1e-6, 1e8)),
            "alpha": 1e-10,
            "acq_type": "UCB",       # Upper Confidence Bound
            "acq_param": 1.96,
            "sobol_m": 13,
            "normalize_y": False,
        },
        5: {
            "kernel": RBF(length_scale=[0.1] * 4, length_scale_bounds=(1e-6, 1e8)),
            "alpha": 1e-10,
            "acq_type": "UCB",       # Upper Confidence Bound
            "acq_param": 1.96,
            "sobol_m": 13,
            "normalize_y": False,
        },
        6: {
            "kernel": RBF(length_scale=[1.0] * 5, length_scale_bounds=(1e-6, 1e8)),
            "alpha": 1e-10,
            "acq_type": "UCB",       # Upper Confidence Bound
            "acq_param": 1.96,
            "sobol_m": 13,
            "normalize_y": False,
        },
        7: {
            "kernel": RBF(length_scale=[1.0] * 6, length_scale_bounds=(1e-6, 1e8)),
            "alpha": 1e-10,
            "acq_type": "UCB",       # Upper Confidence Bound
            "acq_param": 1.96,
            "sobol_m": 13,
            "normalize_y": False,
        },
        8: {
            "kernel": RBF(length_scale=[1.0] * 8, length_scale_bounds=(1e-6, 1e8)),
            "alpha": 1e-10,
            "acq_type": "UCB",       # Upper Confidence Bound
            "acq_param": 1.96,
            "sobol_m": 13,
            "normalize_y": False,
        },
    }
