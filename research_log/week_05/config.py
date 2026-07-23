"""
Week 5 BBO - Configurations Module
=================================
Hyperparameter configurations, kernel selections, and acquisition strategies for black-box 
functions 1 through 8. Used to generate query predicitions in Week 5 of the BBO Capstone Project.
"""

from sklearn.gaussian_process.kernels import RBF, Matern, WhiteKernel

def get_function_configs():

    """Returning configurations dictionary for each of the 8 Black-Box functions (Week 5)."""
    
    return {
        1: {
            "kernel": Matern(
                length_scale=[0.1, 0.1],
                nu=1.5,
                length_scale_bounds=(1e-6, 1e8),
            )
            + WhiteKernel(
                noise_level=1e-6, noise_level_bounds=(1e-16, 1e-2)
            ),
            "acq_type": "EI",
            "acq_param": 0.1,
            "sobol_m": 12,
        },
        2: {
            "kernel": RBF(
                length_scale=[0.1] * 2, length_scale_bounds=(1e-6, 1e8)
            )
            + WhiteKernel(
                noise_level=0.05, noise_level_bounds=(1e-4, 1.0)
            ),
            "acq_type": "UCB",
            "acq_param": 1.96,
            "sobol_m": 12,
        },
        3: {
            "kernel": RBF(
                length_scale=[1.0] * 3, length_scale_bounds=(1e-6, 1e8)
            )
            + WhiteKernel(
                noise_level=0.5, noise_level_bounds=(1e-4, 1.0)
            ),
            "acq_type": "UCB",
            "acq_param": 1.96,
            "sobol_m": 12,
        },
        4: {
            "kernel": RBF(
                length_scale=[0.1] * 4, length_scale_bounds=(1e-6, 1e8)
            )
            + WhiteKernel(
                noise_level=60.0, noise_level_bounds=(1e-3, 1e4)
            ),
            "acq_type": "EI",
            "acq_param": 0.1,
            "sobol_m": 13,
        },
        5: {
            "kernel": RBF(length_scale=[0.1] * 4)
            + WhiteKernel(
                noise_level=7.4e4, noise_level_bounds=(1e-3, 1e7)
            ),
            "acq_type": "UCB",
            "acq_param": 0.5,
            "sobol_m": 13,
        },
        6: {
            "kernel": RBF(
                length_scale=[1.0] * 5, length_scale_bounds=(1e-6, 1e8)
            )
            + WhiteKernel(
                noise_level=0.2, noise_level_bounds=(1e-8, 5.0)
            ),
            "acq_type": "EI",
            "acq_param": 0.1,
            "sobol_m": 13,
        },
        7: {
            "kernel": RBF(length_scale=[0.5] * 6)
            + WhiteKernel(
                noise_level=0.12, noise_level_bounds=(1e-3, 3.0)
            ),
            "acq_type": "EI",
            "acq_param": 0.1,
            "sobol_m": 13,
        },
        8: {
            "kernel": RBF(
                length_scale=[1.0] * 8, length_scale_bounds=(1e-6, 1e8)
            )
            + WhiteKernel(
                noise_level=0.3, noise_level_bounds=(1e-12, 10.0)
            ),
            "acq_type": "EI",
            "acq_param": 0.1,
            "sobol_m": 13,
        },
    }
