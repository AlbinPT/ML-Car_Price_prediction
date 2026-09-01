import streamlit as st
import requests

st.title("Car Price Prediction System")
st.write("Welcome to my app!")

# Car_Name = st.text_input("Car Name", value="Car")  
year = st.number_input("Year of Manufacture", min_value=1900, max_value=2024, value=2020)
present_price = st.number_input("Present Price (in lakhs)", min_value=0.0, max_value=100.0, value=5.0)
kms_driven = st.number_input("Kms Driven", min_value=0, max_value=1000000, value=50000)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"]) 

transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.number_input("Number of Previous Owners", min_value=0, max_value=10, value=0)

if st.button("Predict"):

    st.write("Sending request to FastAPI...")

    data = {
        # "Car_Name": str("Car"), 
        "Year": int(year),
        "Present_Price": float(present_price),
        "Kms_Driven": int(kms_driven),
        "Fuel_Type": fuel_type,
        "Seller_Type": seller_type,
        "Transmission": transmission,
        "Owner": int(owner)
    }


    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data,
            timeout=10
        )

        st.write("Response received!")

        # response.raise_for_status()

        result = response.json()

        # st.write(result)

        prediction = result["prediction"]

        st.success(
            f"The predicted selling price of the car is: ₹{prediction:.1f} lakhs"
        )

    except requests.exceptions.Timeout:
        st.error("The prediction took more than 10 seconds.")

    except requests.exceptions.ConnectionError:
        st.error(" Cannot connect to FastAPI.")

    except Exception as e:
        st.error(f" Error: {e}")