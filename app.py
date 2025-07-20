import streamlit as st
import pandas as pd
import sqlite3
import joblib

st.title("🐟 Early Warning System for Fish Farm Failure")

# Load model
model = joblib.load("models/farm_failure_model.pkl")

# Connect DB
conn = sqlite3.connect("fishfarm.db")
df = pd.read_sql_query("SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 100", conn)

# Show Data
st.subheader("Latest Sensor Readings")
st.dataframe(df)

# Predict on latest row
latest = df.iloc[0][["temp_c", "ph", "ammonia_mg_l", "do_mg_l"]].values.reshape(1, -1)
prediction = model.predict(latest)[0]

st.subheader("⚠️ Failure Risk Prediction")
if prediction == 1:
    st.error("❗ Warning: HIGH RISK of Fish Farm Failure!")
else:
    st.success("✅ Status: Normal – No immediate risk.")
