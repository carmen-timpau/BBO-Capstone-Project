def unwarp_predictions_and_values(predictions, fn_key, warpers):
    """
    Transforms the warped predictions back to the original objective scale 
    using the stored HEBO warper instance if applicable.
    """
    warper = warpers.get(fn_key, None)
    if warper is not None:
        return warper.inverse_transform(predictions)
    return predictions
