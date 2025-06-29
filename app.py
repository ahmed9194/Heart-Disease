import streamlit as st
import pandas as pd
import joblib
import os

# Loading the trained model
model_path = r"C:\Users\user\Desktop\Intelligent Programming\Project 1\ml_model\heart_disease_model.pkl"
if not os.path.exists(model_path):
    st.error("❌ Model file not found! Please check the path.")
    st.stop()

model = joblib.load(model_path)

# Loading the column names used during training
data_path = r"C:\Users\user\Desktop\Project (1)intelligent prog\cleaned_data.csv"
if not os.path.exists(data_path):
    st.error("❌ Data file not found! Please check the path.")
    st.stop()

df = pd.read_csv(data_path)
expected_columns = df.drop(columns=['target']).columns  # Removing the target column

# Creating the user interface
st.title("💙 Heart Disease Prediction System")

# Entering the data
age = st.slider("📅 Age", 20, 80, 50)
cholesterol = st.slider("🩸 Cholesterol Level", 100, 300, 200)
blood_pressure = st.slider("💉 Blood Pressure", 80, 200, 120)
exercise = st.selectbox("🏃‍♂️ Do you exercise regularly?", ["Yes", "No"])
smoking = st.selectbox("🚬 Do you smoke?", ["Yes", "No"])

# Creating a DataFrame for the inputs
user_input = pd.DataFrame([[age, cholesterol, blood_pressure, smoking == "Yes", exercise == "Yes"]],
                          columns=['age', 'cholesterol', 'blood_pressure', 'smoking', 'exercise'])

# Adding missing columns to ensure compatibility with the model
for col in expected_columns:
    if col not in user_input.columns:
        user_input[col] = 0  

# Reordering the columns to match the training order
user_input = user_input[expected_columns]

# Prediction
if st.button("🔍 Predict"):
    prediction = model.predict(user_input)[0]
    
    if prediction == 1:
        st.error("⚠️ High risk of heart disease! Please consult a doctor.")
    else:
        st.success("✅ Low risk of heart disease! Keep up the healthy habits. ")
