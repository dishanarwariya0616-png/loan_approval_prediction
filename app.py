import streamlit as st
import numpy as np
import joblib

model = joblib.load("loan_model.pkl")
st.title("Loan Approval Prediction")
age = st.number_input("Age")
income = st.number_input("income")
loan = st.number_input("loan")
credit = st.number_input("Credit Score")

if st.button("Predict"):
    prediction = model.predict([[age,income,loan,credit]])

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")

        #if st.button("Predict"):
    #input_data = [[age, income, loan, credit_score]]

    #prediction = model.predict(input_data)

   # if prediction[0] == 1:
        #st.success("✅ Loan Approved")
   # else:
       # st.error("❌ Loan Rejected")