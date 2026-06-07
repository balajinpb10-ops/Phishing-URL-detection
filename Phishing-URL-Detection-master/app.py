#importing required libraries

from flask import Flask, request, render_template
import numpy as np
import pandas as pd

import warnings
import pickle
warnings.filterwarnings('ignore')
from feature import FeatureExtraction
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler






app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        obj = FeatureExtraction(url)
        y=obj.getFeaturesList()
        
        # Load the saved model
        loaded_model = load_model("bigru.h5")

        # Input data for prediction
        y.append(1)

        # Reshape the input data to match the model's input shape
        input_data_reshaped = np.array(y).reshape((1, len(y), 1))

        # Make predictions on the reshaped input data using the loaded model
        predictions = loaded_model.predict(input_data_reshaped)

        # Thresholding probabilities to obtain class labels
        threshold = 0.5  # Example threshold
        predicted_class = 1 if predictions[0][0] > threshold else 0

        # Print the predicted class
        print("Predicted Class:", predicted_class)
        print(predicted_class)
        return render_template('index.html',xx =predicted_class,url=url )
        
        
    return render_template("index.html", xx =-1)


if __name__ == "__main__":
    app.run(debug=True)