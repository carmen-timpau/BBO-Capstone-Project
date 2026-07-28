import numpy as np
from sklearn.preprocessing import PowerTransformer

class HEBOStyleWarper:
    """
    Implementing true HEBO-style output warping using Box-Cox or Yeo-Johnson 
    transformations with automatically optimized parameters.
    """
    def __init__(self):
        self.transformer = None

    def fit_transform(self, y):
        # Flatten and reshape to 2D array format required by scikit-learn
        y_reshaped = np.array(y).flatten().reshape(-1, 1)
        
        # Check if all values are strictly positive to determine the method
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
    Applying HEBO-style parametric output warping uniformly to all functions 
    without relying on an external Breusch-Pagan test (to avoid limit cases).
    """
    warped_data = {}
    warpers = {}

    for fn_key, content in data.items():
        Y = np.array(content["y"]).flatten()
        
        # Always instantiating and applying a parametric warper
        warper = HEBOStyleWarper()
        Y_target = warper.fit_transform(Y)
        
        warpers[fn_key] = warper
        warped_data[fn_key] = {
            "x": content["x"],
            "y_target": Y_target
        }

    return warped_data, warpers
