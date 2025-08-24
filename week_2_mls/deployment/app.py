import streamlit as st
import pandas as pd
from huggingface_hub import hf_hub_download
import joblib

# Download and load the model
model_path = hf_hub_download(repo_id="ddhnauka/learning", filename="best_machine_learning_v1.joblib")
model = joblib.load(model_path)

# Streamlit UI for Machine Failure Prediction
st.title("Machine Learning Prediction App")
st.write("""
This application predicts the likelihood of a machine failing based on its operational parameters.
Please enter the sensor and configuration data below to get a prediction.
""")

# User input
ProdTaken = st.selectbox("Product Taken", ["0", "1"])
Age = st.number_input("Age", min_value=0, max_value=100.0, value=1, step=0.1)
CityTier = st.number_input("City Tier", ["1", "2", "3"])
NumberOfPersonVisiting = st.number_input("Number of Person Visiting", min_value=0, max_value=100, value=1400)
NumberOfFollowups = st.number_input("Number of Followup", min_value=0.0, max_value=100.0, value=40.0, step=0.1)
Passport = st.number_input("Passport", ["0", "1"])
OwnCar = st.number_input("Own Car", ["0", "1"])
NumberOfChildrenVisiting = st.number_input("Number of Children Visiting", min_value=0, max_value=100, value=1400)
MonthlyIncome = st.number_input("Monthly Income", min_value=0, max_value=100000, value=1400)
DurationOfPitch = st.number_input("Duration of Pitch", min_value=0, max_value=100, value=1400)
PitchSatisfactionScore = st.number_input("Pitch Satisfaction Score", min_value=0, max_value=100, value=1400)
NumberOfTrips = st.number_input("Number of Trips", min_value=0, max_value=100, value=1400)


# Assemble input into DataFrame
input_data = pd.DataFrame([{
    'Product Taken': ProdTaken,
    'Age': Age,
    'City Tier': CityTier,
    'Number of Person Visiting': NumberOfPersonVisiting,
    'Number of Followups': NumberOfFollowups,
    'Passport': Passport,
    'Own Car': OwnCar,
    'Number of Children Visiting': NumberOfChildrenVisiting,
    'Monthly Income': MonthlyIncome,
    'Duration of Pitch': DurationOfPitch,
    'Pitch Satisfaction Score': PitchSatisfactionScore,
    'Number of Trips': NumberOfTrips,
    'Type': 'Package',
    'Designation': 'Executive',
    'Marital Status': 'Married',
    'Product Pitch': 'Pitch Perfect',
    'Gender': 'Male'
}])


if st.button("Predict Failure"):
    prediction = model.predict(input_data)[0]
    result = "Machine Failure" if prediction == 1 else "No Failure"
    st.subheader("Prediction Result:")
    st.success(f"The model predicts: **{result}**")
