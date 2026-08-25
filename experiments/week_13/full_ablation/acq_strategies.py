"""Centralized acquisition function configurations for a highly-exploitative kernel x acqusition joint ablation, part of the 
Week 13 BBO Bayesian Optimisation ML pipeline (for predicting the final set of next queries in this project, 1 per function)."""

acq_strategies = {
    "Expected Improvement (xi=0.001)": ("EI", 0.001),
    "Upper Confidence Bound (beta=0.5)": ("UCB", 0.5),
    "Probability of Improvement (xi=0.01)": ("PI", 0.01),
}
