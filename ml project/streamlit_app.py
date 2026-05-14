import streamlit as st
import pandas as pd
import joblib

st.title("Student Overall Score Predictor")

# Load trained model
model = joblib.load("models/trained_model.pkl")

# Input fields
math = st.number_input("Math Score", min_value=0, max_value=100, value=0)
reading = st.number_input("Reading Score", min_value=0, max_value=100, value=0)
writing = st.number_input("Writing Score", min_value=0, max_value=100, value=0)

if st.button("Predict Overall"):
    # Create DataFrame
    data = pd.DataFrame([[math, reading, writing]])
    
    # Fix column names to match the trained model exactly
    data.columns = model.feature_names_in_  # This ensures exact match
    
    # Predict
    pred = model.predict(data)
    
    st.success(f"Predicted Overall Score: {pred[0]:.2f}")
