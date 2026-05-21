import streamlit as st
import pickle
model = pickle.load(open("notebook/model.pkl", "rb"))

st.title("House Price Prediction")

st.write("This app will predict house prices using a machine learning model.")

st.header("Enter House Details")

area = st.number_input("Enter area of the house")
bedrooms = st.number_input("Enter number of bedrooms")
bathrooms = st.number_input("Enter number of bathrooms")
floors = st.number_input("Enter number of floors")
condition = st.selectbox(
    "Select the condition of the house",
    ["Excellent", "Good", "Fair", "Poor"]
)
garage = st.selectbox(
    "Does the house have a garage?",
    ["Yes", "No"]
)
condition_mapping = {"Excellent": 3, "Good": 2, "Fair": 1, "Poor": 0}
garage_mapping = {"Yes": 1, "No": 0}
condition = condition_mapping[condition]        
garage = garage_mapping[garage]
if st.button("Predict Price"):
   input_data = [[area, bedrooms, bathrooms, floors, condition, garage]]
   prediction = model.predict(input_data)
   st.success(f"Predicted House Price: ₹{prediction[0]:,.2f}")