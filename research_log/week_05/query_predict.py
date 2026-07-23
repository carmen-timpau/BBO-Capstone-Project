# Computing the next query for each function for Week 5 BBO

import numpy as np
from acquisition import expected_improvement, upper_confidence_bound
from sampling import generate_sobol_grid
from sklearn.gaussian_process import GaussianProcessRegressor

def compute_next_query(
    X: np.ndarray,
    Y: np.ndarray,
    kernel,
    acq_type: str = "EI",
    acq_param: float = 0.1,
    sobol_m: int = 12,
    alpha: float = 0.0,
    normalize_y: bool = True,
) -> np.ndarray:
    """Fitting GP surrogate and calculating the next optimal query point."""
    
    # Fitting Gaussian Process (GP)
    gp = GaussianProcessRegressor(
        kernel=kernel, alpha=alpha, normalize_y=normalize_y
    )
    gp.fit(X, Y)

    # Sampling candidate points using Sobol grid
    b_min, b_max = X.min(axis=0), X.max(axis=0)
    x_grid = generate_sobol_grid(b_min, b_max, m_samples=sobol_m)

    # Computing the GP Posterior predictions
    post_mean, post_std = gp.predict(x_grid, return_std=True)

    # Computing the acquisition scores
    if acq_type.upper() == "EI":
        scores = expected_improvement(
            post_mean, post_std, y_max=Y.max(), xi=acq_param
        )
    elif acq_type.upper() == "UCB":
        scores = upper_confidence_bound(post_mean, post_std, beta=acq_param)
    else:
        raise ValueError(f"Unknown acquisition function type: {acq_type}")

    # Returning next query (argmax candidate)
    return x_grid[np.argmax(scores)]
