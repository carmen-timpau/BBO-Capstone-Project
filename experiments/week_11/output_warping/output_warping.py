import numpy as np
from sklearn.preprocessing import PowerTransformer


def get_function1_log_target(Y):
    """Data-driven floor + log10 transform for Function 1."""
    Y = np.asarray(Y).flatten()
    positive_Y = Y[Y > 0]
    noise_floor = positive_Y.min()
    return np.log10(np.clip(Y, noise_floor, None))


class HEBOStyleWarper:
    """
    Implementing true HEBO-style output warping using Box-Cox or Yeo-Johnson
    transformations with automatically optimized parameters.
    """
    def __init__(self):
        self.transformer = None

    def fit_transform(self, y):
        y_reshaped = np.array(y).flatten().reshape(-1, 1)
        if np.all(y_reshaped > 0):
            self.transformer = PowerTransformer(method='box-cox')
        else:
            self.transformer = PowerTransformer(method='yeo-johnson')
        return self.transformer.fit_transform(y_reshaped).flatten()

    def inverse_transform(self, y_warped):
        y_reshaped = np.array(y_warped).flatten().reshape(-1, 1)
        return self.transformer.inverse_transform(y_reshaped).flatten()


def apply_output_warping_to_dataset(data):
    """
    Applying HEBO-style parametric output warping to all functions.
    Function 1 is log10-transformed (data-driven floor) BEFORE warping,
    since its raw scale (125+ orders of magnitude, sign-flipping noise near
    zero) breaks the assumptions Box-Cox/Yeo-Johnson are built on.
    """
    warped_data = {}
    warpers = {}
    for fn_key, content in data.items():
        Y = np.array(content["y"]).flatten()

        if fn_key == "function_1":
            Y = get_function1_log_target(Y)

        warper = HEBOStyleWarper()
        Y_target = warper.fit_transform(Y)

        warpers[fn_key] = warper
        warped_data[fn_key] = {
            "x": content["x"],
            "y_target": Y_target
        }
    return warped_data, warpers
