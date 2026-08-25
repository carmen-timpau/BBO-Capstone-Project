"""Centralized acquisition function strategy configurations for a highly-exploitative Bayesian Optimisation pipeline (Week 13 BBO, final submission)."""

acq_strategies = {
    "Expected Improvement (xi=0.001)": ("EI", 0.001),
    "Upper Confidence Bound (beta=0.5)": ("UCB", 0.5),
    "Probability of Improvement (xi=0.01)": ("PI", 0.01),
}
