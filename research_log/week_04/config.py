"""
Week 4 BBO - Configuration Module
=================================
Hyperparameter configurations, kernel selections, and acquisition strategies for black-box 
functions 1 through 8. Used to generate query predicitions in Week 4 of the BBO Capstone Project.
"""


from sklearn.gaussian_process.kernels import RBF, Matern

def get_function_configs():
  
    """Returning configuration dictionary for each of the 8 Black-Box functions (Week 4)."""
  
    return {
        1: {
            "kernel": Matern(length_scale=[0.1, 0.1], nu=1.5, length_scale_bounds=(1e-6, 1e8)),
            "alpha": 1e-4,
            "acq_type": "TS",        # Thompson Sampling
            "acq_param": None,
            "sobol_m": 12,
        },
        2: {
            "kernel": RBF(length_scale=[0.1] * 2, length_scale_bounds=(1e-6, 1e8)),
            "alpha": 1e-10,
            "acq_type": "EI",        # Expected Improvement
            "acq_param": 0.1,
            "sobol_m": 12,
        },
        3: {
            "kernel": RBF(length_scale=[0.5] * 3, length_scale_bounds=(1e-6, 1e8)),
            "alpha": 1e-10,
            "acq_type": "EI",
            "acq_param": 0.1,
            "sobol_m": 12,
        },
        4: {
            "kernel": RBF(length_scale=[0.1] * 4, length_scale_bounds=(1e-6, 1e8)),
            "alpha": 1e-10,
            "acq_type": "TS",
            "acq_param": None,
            "sobol_m": 13,
        },
        5: {
            "kernel": RBF(length_scale=[0.1] * 4), # Default length_scale_bounds
            "alpha": 1e-10,
            "acq_type": "EI",
            "acq_param": 0.1,
            "sobol_m": 13,
        },
        6: {
            "kernel": RBF(length_scale=[1.0] * 5, length_scale_bounds=(1e-6, 1e8)),
            "alpha": 1e-10,
            "acq_type": "EI",
            "acq_param": 0.1,
            "sobol_m": 13,
        },
        7: {
            "kernel": RBF(length_scale=[0.5] * 6), # Default length_scale_bounds
            "alpha": 1e-10,
            "acq_type": "EI",
            "acq_param": 0.1,
            "sobol_m": 13,
        },
        8: {
            "kernel": RBF(length_scale=[1.0] * 8, length_scale_bounds=(1e-6, 1e8)),
            "alpha": 1e-10,
            "acq_type": "TS",
            "acq_param": None,
            "sobol_m": 13,
        },
    }
