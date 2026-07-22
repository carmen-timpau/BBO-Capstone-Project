# Computing Scores for Acquisition Functions (Designed for Batch/Vector Inputs)
# Contains the Acquisition Functions Tested in Acquisition Ablation Study conducted in Week 6 BBO

def compute_acquisition_scores(X_cand, gp, y_best, acq_type, param=0.01):
    """Computes acquisition scores for a given GP and candidate points."""
    mu, sigma = gp.predict(X_cand, return_std=True)
    sigma = np.maximum(sigma, 1e-9)
    
    if acq_type == "EI":
        # param = xi (exploration trade-off)
        improvement = mu - y_best - param
        Z = improvement / sigma
        return improvement * norm.cdf(Z) + sigma * norm.pdf(Z)

    elif acq_type == "UCB":
        # param = beta (confidence multiplier)
        return mu + param * sigma

    elif acq_type == "PI":
        # param = xi
        improvement = mu - y_best - param
        Z = improvement / sigma
        return norm.cdf(Z)
