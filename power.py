import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("⚡ Power Consumption Prediction App")

temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=100.0, value=25.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
windspeed = st.number_input("Wind Speed", min_value=0.0, value=5.0)
general_diffuse = st.number_input("General Diffuse Flows", min_value=0.0, value=100.0)
diffuse = st.number_input("Diffuse Flows", min_value=0.0, value=50.0)

hour = st.slider("Hour", 0, 23, 12)
day = st.slider("Day", 1, 31, 15)
month = st.slider("Month", 1, 12, 6)

if st.button("Predict Power Consumption"):
    features = np.array([[temperature, humidity, windspeed,
                          general_diffuse, diffuse,
                          hour, day, month]])

    prediction = model.predict(features)

    st.success(f"⚡ Predicted Power Consumption: {prediction[0]:.2f} kW")
