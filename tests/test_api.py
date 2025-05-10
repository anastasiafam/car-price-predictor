# tests/test_api.py
import requests

def test_api_prediction():
    sample = {
        "Manufacturer": "HONDA",
        "Model": "CIVIC",
        "Category": "Sedan",
        "Leather_interior": 1,
        "Fuel_type": "Petrol",
        "Engine_volume": 1.8,
        "Mileage": 90000,
        "Cylinders": 4,
        "Gear_box_type": "Automatic",
        "Drive_wheels": "Front",
        "Doors": 4,
        "Wheel": "Left",
        "Color": "Black",
        "Airbags": 4,
        "Age": 10,
        "Levy_rate": 0.05
    }
    response = requests.post("http://localhost:8000/predict", json=sample)
    assert response.status_code == 200
    assert "predicted_price" in response.json()

def test_api_missing_field():
    # Пропущено поле "Model"
    sample = {
        "Manufacturer": "HONDA",
        "Category": "Sedan",
        "Leather_interior": 1,
        "Fuel_type": "Petrol",
        "Engine_volume": 1.8,
        "Mileage": 90000,
        "Cylinders": 4,
        "Gear_box_type": "Automatic",
        "Drive_wheels": "Front",
        "Doors": 4,
        "Wheel": "Left",
        "Color": "Black",
        "Airbags": 4,
        "Age": 10,
        "Levy_rate": 0.05
    }
    response = requests.post("http://localhost:8000/predict", json=sample)
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()