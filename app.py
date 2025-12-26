import streamlit as st
import joblib
import os
import pandas as pd

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📉",
    layout="centered"
)

st.title("Customer Churn Prediction")
st.write("Predict whether a customer is likely to churn using a trained ML model.")

# -----------------------------
# Load model and columns safely
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = None
model_columns = None

try:
    model = joblib.load(os.path.join(BASE_DIR, "churn_model.pkl"))
    model_columns = joblib.load(os.path.join(BASE_DIR, "model_columns.pkl"))
    st.success("Model loaded successfully")
except:
    st.warning("Model files not found. Please train the model first using `churn_model.py`.")

st.divider()

# -----------------------------
# User input section
# -----------------------------
st.subheader("Enter Customer Details")

tenure = st.number_input("Tenure (months)", min_value=0, step=1)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, step=1.0)
total_charges = st.number_input("Total Charges", min_value=0.0, step=1.0)

contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

st.divider()

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Churn"):
    if model is None or model_columns is None:
        st.error("Model not available. Train the model first.")
    else:
        # Create input dictionary
        input_data = {
            "tenure": tenure,
            "MonthlyCharges": monthly_charges,
            "TotalCharges": total_charges,
            "Contract": contract,
            "InternetService": internet_service,
            "PaymentMethod": payment_method
        }

        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])

        # One-hot encode
        input_df = pd.get_dummies(input_df)

        # Align with training columns
        input_df = input_df.reindex(columns=model_columns, fill_value=0)

        # Make prediction
        prediction = model.predict(input_df)[0]

        # Display result
        if prediction == 1:
            st.error("⚠️ Customer is likely to churn")
        else:
            st.success("✅ Customer is not likely to churn")
