#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pickle

# Load the trained model from a pickle file
loaded_model = pickle.load(open("Cltv_Predictor_model.sav", "rb"))

def predict(inputs):
    prediction = loaded_model.predict(inputs)
    return prediction

st.title("Customer Lifetime Value Prediction App")

# Define the user interface for collecting inputs
marital_status = st.number_input("Marital Status:")
vintage = st.number_input("Vintage:")
claim_amount = st.number_input("Claim Amount:")
gender = st.number_input("Gender:")
area = st.number_input("Area:")
qualification = st.number_input("Qualification:")
income = st.number_input("Income:")
policy = st.number_input("Policy:")
type_of_policy = st.number_input("Type of Policy:")

inputs = [marital_status, vintage, claim_amount, gender, area, qualification, income, policy, type_of_policy]

if st.button("Predict"):
    prediction = predict(inputs)
    st.write("The predicted customer lifetime value is:", prediction)


# In[ ]:




