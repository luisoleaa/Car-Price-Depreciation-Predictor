import streamlit as st 

st.title("Car Resale Value Predictor")

st.write("Enter your car details to predict the resale value")

make=st.text_input("Enter Car Make").lower()

model=st.text_input("Enter Car Model").lower()

transmission = st.selectbox(
    "Select Transmission",
    ["Automatic", "Manual"]
)
trim=st.text_input("Enter Car Trim").lower()

body=st.text_input("Enter Car Body").lower()

ocolor=st.text_input("Enter Car Outside Color").lower()

icolor=st.text_input("Enter Car Interior Color").lower()

st.button("Predict Resale Price")





