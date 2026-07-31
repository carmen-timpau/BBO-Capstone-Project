"""Centralized acquisition function strategy configurations."""

acq_strategies = {
    "Expected Improvement (xi=0.01)": ("EI", 0.01),
    "Expected Improvement (xi=0.1)": ("EI", 0.1),
    "Upper Confidence Bound (beta=1.96)": ("UCB", 1.96),
    "Upper Confidence Bound (beta=2.58)": ("UCB", 2.58),
    "Probability of Improvement (xi=0.1)": ("PI", 0.1),
    "Thompson Sampling": ("TS", 0.0)
}
