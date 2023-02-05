#!/usr/bin/env python
# coding: utf-8

# In[11]:


import streamlit as st
import pickle

# Load the trained model from a pickle file
loaded_model = pickle.load(open("Cltv_Predictor_model.sav", "rb"))

def predict(inputs):
    prediction = loaded_model.predict(inputs)
    return prediction

st.title("Customer Lifetime Value Prediction App")

# Define the user interface for collecting inputs
marital_status = st.selectbox("Marital Status:", ["Single", "Married"])
vintage = st.number_input("Vintage:")
claim_amount = st.number_input("Claim Amount:")
gender = st.selectbox("Gender:", ["Male", "Female"])
area = st.selectbox("Area:", ["Urban", "Rural"])
qualification = st.selectbox("Qualification:", ["Bachelor", "High School"])
income = st.selectbox("Income:", ["<=2L", "2L-5L", "5L-10L","More than 10L"])
policy = st.selectbox("Policy:", ["A", "B", "C"])
type_of_policy = st.selectbox("Type of Policy:", ["Platinum", "Gold", "Silver"])

inputs = [marital_status, vintage, claim_amount, gender, area, qualification, income, policy, type_of_policy]

if st.button("Predict"):
    prediction = predict(inputs)
    st.write("The predicted customer lifetime value is:", prediction)

