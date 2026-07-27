"""Centralized acquisition function strategy configurations."""

acq_strategies = {
    "EI (xi=0.01)": ("EI", 0.01),
    "EI (Exploration, xi=0.1)": ("EI", 0.10),
    "UCB (beta=1.96)": ("UCB", 1.96),
    "UCB (beta=2.58)": ("UCB", 2.58),
    "PI (xi=0.01)": ("PI", 0.01),
}
