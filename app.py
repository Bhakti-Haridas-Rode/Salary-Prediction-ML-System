import streamlit as st
import pandas as pd
import joblib

model = joblib.load("salary_prediction_model.pkl")

st.title("Salary Prediction App")
st.write("Predict salary based on years of experience")

years = st.number_input("Enter Years of Experience", min_value=0.0, max_value=50.0, value=5.0)


if st.button("Predict Salary"):
    input_data = pd.DataFrame([[years]], columns=["Years_of_Experience"])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Salary: ₹ {prediction:,.2f}")