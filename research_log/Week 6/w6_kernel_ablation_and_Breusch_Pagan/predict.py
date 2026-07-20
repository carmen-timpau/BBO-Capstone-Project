# Week 6 BBO - Unified Next Query Prediction (Functions 1-8)
# Using winning kernel and acquisition configurations determined by ablation studies beforehand
# Implementing Dynamic Sobol sampling resolution based on dimensionality to ensure high candidate resolution for high-dimensional spaces

import warnings
import numpy as np
import pandas as pd
from scipy.stats.qmc import Sobol
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.preprocessing import StandardScaler

from kernels import get_kernel_suite, get_kernel_suite_f1
from acquisition import compute_acquisition_scores

warnings.filterwarnings("ignore", message="Predicted variances smaller than 0", category=UserWarning)

# Store next query predictions for Functions 1 through 8
next_queries_summary = {}

for fn_idx in range(1, 9):
    fn_key = f"function_{fn_idx}"

    if fn_key not in data:
        print(f"Skipping {fn_key}: Not found in data dictionary.")
        continue

    # Loading Data and Targeted Preprocessing
    X = np.array(data[fn_key]["x"])
    Y = np.array(data[fn_key]["y"]).flatten()
    n_samples, n_dims = X.shape

    # Function 1 special log-transform to handle numerical scale
    if fn_idx == 1:
        Y_safe = np.clip(Y, 1e-300, None)
        Y_target = np.log10(Y_safe)
    else:
        Y_target = Y

    # Scaling input features strictly using StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)


    # Re-instantiating Winning Kernel from Kernel Ablation
    winning_variant_name = top_kernels_summary[fn_key]["Best Variant"]
    kernel_suite = get_kernel_suite_f1(n_dims) if fn_idx == 1 else get_kernel_suite(n_dims)
    best_kernel = kernel_suite[winning_variant_name]

    # Fitting GP model on full dataset
    gp = GaussianProcessRegressor(
        kernel=best_kernel,
        alpha=0.0,
        normalize_y=True,
        n_restarts_optimizer=10,
        random_state=42
    )
    gp.fit(X_scaled, Y_target)

    # Generating Candidate Space via Sobol Quasi-Random Sampling
    minimum = X.min(axis=0)
    maximum = X.max(axis=0)

    # Dynamic Sobol sample resolution based on dimensionality
    if n_dims >= 6:
        m_samples = 14  # 2^14 = 16,384 points
    elif n_dims >= 4:
        m_samples = 13  # 2^13 = 8,192 points
    else:
        m_samples = 12  # 2^12 = 4,096 points

    # Sobol sequence (power of 2)
    sobol = Sobol(d=n_dims, scramble=True, seed=42)
    unit_samples = sobol.random_base2(m=m_samples)
    
    x_grid = minimum + unit_samples * (maximum - minimum)
    x_grid_scaled = scaler.transform(x_grid)

    # Computing Acquisition Scores via Winning Strategy
    winning_acq_str = acq_ablation_summary[fn_key]["Best Acquisition"]
    
    # Parsing acquisition function name and parameter value
    acq_type, param_val = acq_strategies[winning_acq_str]
    y_best = np.max(Y_target)

    acq_scores = compute_acquisition_scores(
        X_cand=x_grid_scaled,
        gp=gp,
        y_best=y_best,
        acq_type=acq_type,
        param=param_val
    )

    # Extracting Next Query Point (Argmax Acquisition)
    best_candidate_idx = np.argmax(acq_scores)
    x_next = x_grid[best_candidate_idx]

    next_queries_summary[fn_key] = {
        "Dim": n_dims,
        "Winning Kernel": winning_variant_name,
        "Winning Acquisition": winning_acq_str,
        "Next Query Raw": x_next,
        "Next Query (6 Dec)": np.round(x_next, 6).tolist()
    }

# Printing Results Table for Functions 1-8

print("=" * 110)
print("                       WEEK 6 — ALL FUNCTIONS NEXT QUERY PREDICTIONS")
print("=" * 110)

for fn_key, info in next_queries_summary.items():
    print(f"[{fn_key.upper()}] (Dim={info['Dim']})")
    print(f"  • Kernel      : {info['Winning Kernel']}")
    print(f"  • Acquisition : {info['Winning Acquisition']}")
    print(f"  • Next Query  : {info['Next Query (6 Dec)']}")
    print("-" * 110)
