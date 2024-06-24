import pandas as pd
import joblib
import numpy as np

import os



# supress warning
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")


def predict_viscosity(Total_fat, Fineness, Emulsifier, PGPR, model_path):

    # Load the model
    rf = joblib.load(model_path)

    # Make a prediction using the model
    prediction = rf.predict(np.array([[Total_fat, Fineness, Emulsifier, PGPR]]))
    # return (f"Predicted Viscosity (Lin): {prediction[0]:.2f}")
    return int(prediction[0])