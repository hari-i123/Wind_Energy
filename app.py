import streamlit as st
import pickle
import numpy as np

# Load the model
with open('wind_power_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit App
st.set_page_config(page_title="Wind Power Predictor", layout="centered")

st.title("⚡ Wind Turbine Power Predictor")
st.markdown("Predict **LV Active Power (kW)** based on wind conditions.")

# Input fields
wind_speed = st.number_input("🌬️ Wind Speed (m/s)", min_value=0.0, max_value=25.0, step=0.1)
wind_direction = st.number_input("🧭 Wind Direction (°)", min_value=0.0, max_value=360.0, step=1.0)
theoretical_power = st.number_input("🔋 Theoretical Power Curve (KWh)", min_value=0.0, max_value=1500.0, step=1.0)

# Predict button
if st.button("Predict Active Power"):
    input_data = np.array([[wind_speed, wind_direction, theoretical_power]])
    prediction = model.predict(input_data)[0]
    st.success(f"🔌 Predicted LV Active Power: **{prediction:.2f} kW**")
