import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('fraud_model.pkl', 'rb'))

st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details to check if it's Fraud or Not")

# Input fields (simplified)
amount = st.number_input("Transaction Amount")

# Create input array (dummy simplified input)
# NOTE: dataset has many features, so we simulate input
input_data = np.zeros((1, 30))
input_data[0][0] = amount

if st.button("Predict"):
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("⚠️ Fraud Transaction Detected!")
    else:
        st.success("✅ Normal Transaction")