import numpy as np

def unwarp_predictions_and_values(predictions, fn_key, warpers):
    """
    Transforming warped predictions back to the original objective scale.
    Function 1 needs a second inversion step (10**x) to undo its log10
    transform, on top of undoing the HEBO output warp.
    """
    warper = warpers.get(fn_key, None)
    if warper is not None:
        unwarped = warper.inverse_transform(predictions)
    else:
        unwarped = predictions

    if fn_key == "function_1":
        return 10 ** unwarped

    return unwarped
