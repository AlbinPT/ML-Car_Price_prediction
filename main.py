from fastapi import FastAPI
import pickle
from pydantic import BaseModel

app = FastAPI()

with open("model (1).pkl", "rb") as file:
    model = pickle.load(file)

class CarData(BaseModel):
    # Car_Name: str
    Year: int
    Present_Price: float
    Kms_Driven: int
    Fuel_Type: str
    Seller_Type: str
    Transmission: str
    Owner: int

@app.post("/predict")
def predict_car_price(data: CarData):
    features = [[
        # data.Car_Name,
        data.Year,
        data.Present_Price,
        data.Kms_Driven,
        1 if data.Fuel_Type == "Diesel" else 0,
        1 if data.Fuel_Type == "Petrol" else 0,
        1 if data.Seller_Type == "Individual" else 0,
        1 if data.Transmission == "Manual" else 0,
        data.Owner
    ]]
    prediction = model.predict(features)
    return {
        "prediction": float(prediction[0])
    }

    