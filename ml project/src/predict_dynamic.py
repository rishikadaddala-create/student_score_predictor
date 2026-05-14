import joblib
import numpy as np

# Load trained model
model = joblib.load("models/trained_model.pkl")

# Take user input
writing = float(input("Enter Writing Score: "))
reading = float(input("Enter Reading Score: "))
math = float(input("Enter Math Score: "))

# Predict
features = np.array([[writing, reading, math]])
prediction = model.predict(features)

print(f"✅ Predicted Overall Score: {prediction[0]:.2f}")
