"""Centralized acquisition function strategy configurations."""

acq_strategies = {
    "Expected Improvement (xi=0.001)": ("EI", 0.001),
    "Expected Improvement (xi=0.01)": ("EI", 0.01),
    "Expected Improvement (xi=0.1)": ("EI", 0.1),
    "Upper Confidence Bound (beta=0.5)": ("UCB", 0.5),
    "Upper Confidence Bound (beta=1.0)": ("UCB", 1.0),
    "Upper Confidence Bound (beta=1.96)": ("UCB", 1.96),
    "Upper Confidence Bound (beta=2.58)": ("UCB", 2.58),
    "Probability of Improvement (xi=0.1)": ("PI", 0.1),
    "Probability of Improvement (xi=0.01)": ("PI", 0.01),
    "Thompson Sampling": ("TS", 0.0)
}
