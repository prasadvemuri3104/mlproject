# app.py

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load('gold_price_model.pkl')

# Streamlit app configuration
st.title("Gold Price Prediction App")
st.write("""
This app predicts the price of gold based on various factors.
""")

# Input fields for user to enter the data
spx = st.number_input("S&P 500 Index (SPX)", min_value=0.0, value=1654.32)
uso = st.number_input("United States Oil Fund (USO)", min_value=0.0, value=31.84)
slv = st.number_input("Silver Price (SLV)", min_value=0.0, value=20.08)
eur_usd = st.number_input("EUR/USD Exchange Rate", min_value=0.0, value=1.28)

# Predict button
if st.button("Predict Gold Price"):
    # Create a DataFrame for the input values
    input_data = pd.DataFrame({
        'SPX': [spx],
        'USO': [uso],
        'SLV': [slv],
        'EUR/USD': [eur_usd]
    })

    # Make prediction
    prediction = model.predict(input_data)
    
    # Display the prediction
    st.write(f"The predicted price of gold is: ${prediction[0]:.2f}")
