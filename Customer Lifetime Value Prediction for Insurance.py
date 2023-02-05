#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pickle

# Load the trained model from a pickle file
loaded_model = pickle.load(open("Cltv_Predictor_model.sav", "rb"))

def predict(inputs):
    prediction = loaded_model.predict(inputs)
    return prediction

st.title("Customer Lifetime Value Prediction App")

# Define the user interface for collecting inputs
id = st.number_input("Enter the customer ID:")
marital_status = st.selectbox("Marital Status:", ["Single", "Married"])
vintage = st.number_input("Vintage (in months):")
claim_amount = st.number_input("Claim Amount:")
gender = st.selectbox("Gender:", ["Male", "Female"])
area = st.selectbox("Area:", ["Urban", "Rural"])
qualification = st.selectbox("Qualification:", ["Bachelor", "High School"])
income = st.number_input("Income:")
policy = st.selectbox("Policy:", ["A", "B", "C"])
type_of_policy = st.selectbox("Type of Policy:", ["Platinum", "Gold", "Silver"])

inputs = [id, marital_status, vintage, claim_amount, gender, area, qualification, income, policy, type_of_policy]

if st.button("Predict"):
    prediction = predict(inputs)
    st.write("The predicted customer lifetime value is:", prediction)

