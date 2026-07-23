"""
Scrambled Sobol Sampling used to map the search space with low-discrepancy sequences for high-dimensional 
problems. This is a type of Randomised Quasi-Monte Carlo (RQMC) sampling.
"""

import numpy as np
from scipy.stats.qmc import Sobol

def generate_sobol_grid(
    bounds_min: np.ndarray, bounds_max: np.ndarray, m_samples: int = 12
) -> np.ndarray:
  
    """Generating a scrambled Sobol grid which is scaled to domain bounds (2**m_samples points)."""
  
    dim = len(bounds_min)
    sobol = Sobol(d=dim, scramble=True)
    unit_samples = sobol.random_base2(m=m_samples)
  
    return bounds_min + unit_samples * (bounds_max - bounds_min)
