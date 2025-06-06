# app/api/main.py
import os

import joblib
import pandas as pd
from catboost import Pool
from fastapi import FastAPI
from pydantic import BaseModel, Field

# Загружаем модель
model_path = "app/model/model.pkl"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at: {model_path}")

model = joblib.load(model_path)

# Инициализация FastAPI
app = FastAPI()

# Категориальные признаки для модели
cat_features = [
    "Manufacturer",
    "Model",
    "Category",
    "Fuel type",
    "Gear box type",
    "Drive wheels",
    "Wheel",
    "Color",
]


class CarInput(BaseModel):
    Manufacturer: str = Field(..., example="HONDA")
    Model: str = Field(..., example="CIVIC")
    Category: str = Field(..., example="Sedan")
    Leather_interior: int = Field(..., example=1)
    Fuel_type: str = Field(..., example="Petrol")
    Engine_volume: float = Field(..., example=1.8)
    Mileage: int = Field(..., example=90000)
    Cylinders: int = Field(..., example=4)
    Gear_box_type: str = Field(..., example="Automatic")
    Drive_wheels: str = Field(..., example="Front")
    Doors: int = Field(..., example=4)
    Wheel: str = Field(..., example="Left")
    Color: str = Field(..., example="Black")
    Airbags: int = Field(..., example=4)
    Age: int = Field(..., example=10)
    Levy_rate: float = Field(..., example=0.05)


@app.post("/predict")
def predict_price(car: CarInput):
    raw_input = car.dict()
    rename_map = {
        "Leather_interior": "Leather interior",
        "Fuel_type": "Fuel type",
        "Gear_box_type": "Gear box type",
        "Drive_wheels": "Drive wheels",
        "Engine_volume": "Engine volume",
    }
    for old_key, new_key in rename_map.items():
        raw_input[new_key] = raw_input.pop(old_key)

    feature_order = [
        "Manufacturer",
        "Model",
        "Category",
        "Leather interior",
        "Fuel type",
        "Engine volume",
        "Mileage",
        "Cylinders",
        "Gear box type",
        "Drive wheels",
        "Doors",
        "Wheel",
        "Color",
        "Airbags",
        "Age",
        "Levy_rate",
    ]

    input_df = pd.DataFrame(
        [[raw_input[col] for col in feature_order]], columns=feature_order
    )
    input_pool = Pool(input_df, cat_features=cat_features)
    prediction = model.predict(input_pool)[0]
    return {"predicted_price": round(prediction, 2)}