import streamlit as st
import requests

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="CaloriMate",
    page_icon="🔥",
    layout="centered"
)

st.title("🔥 CaloriMate")
st.write("Predict how many calories you burn during exercise")

# -------------------------------
# Input Form
# -------------------------------
with st.form("calorie_form"):
    sex = st.selectbox("Sex", ["male", "female"])
    age = st.number_input("Age", min_value=10, max_value=100, value=30)
    height = st.number_input("Height (cm)", min_value=120, max_value=220, value=170)
    weight = st.number_input("Weight (kg)", min_value=30, max_value=150, value=70)
    duration = st.number_input("Workout Duration (minutes)", min_value=1, max_value=300, value=30)
    heart_rate = st.number_input("Heart Rate", min_value=50, max_value=200, value=110)
    body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=40.0)

    submitted = st.form_submit_button("Predict Calories")

# -------------------------------
# On Submit
# -------------------------------
if submitted:
    payload = {
        "id": 1,
        "Sex": sex,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "Duration": duration,
        "Heart_Rate": heart_rate,
        "Body_Temp": body_temp
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)

        if response.status_code == 200:
            result = response.json()
            calories = result["Calories Burned"]

            st.success(f"🔥 Estimated Calories Burned: {calories}")

        else:
            st.error("API Error: " + response.text)

    except Exception as e:
        st.error("Could not connect to FastAPI server")

