from fastapi.testclient import TestClient

from app.api.main import app

client = TestClient(app)

valid_sample = {
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
    "Levy_rate": 0.05,
}


# Тест на успешное предсказание
def test_api_prediction():
    response = client.post("/predict", json=valid_sample)
    assert response.status_code == 200
    json_data = response.json()
    assert "predicted_price" in json_data
    assert isinstance(json_data["predicted_price"], (float, int))


# Тест на обязательные поля
def test_api_missing_field():
    sample = valid_sample.copy()
    del sample["Model"]
    response = client.post("/predict", json=sample)
    assert response.status_code == 422
    assert "detail" in response.json()


# Тест на типы данных
def test_api_invalid_field_type():
    sample = valid_sample.copy()
    sample["Mileage"] = "много"
    response = client.post("/predict", json=sample)
    assert response.status_code == 422
    assert "detail" in response.json()


# Тест на пустой запрос
def test_api_empty_request():
    response = client.post("/predict", json={})
    assert response.status_code == 422
    assert "detail" in response.json()


# Тест на граничные значения
def test_api_edge_case_zero_mileage():
    sample = valid_sample.copy()
    sample["Mileage"] = 0  # 0 пробега
    response = client.post("/predict", json=sample)
    assert response.status_code == 200
    json_data = response.json()
    assert "predicted_price" in json_data


# Тест на корректность структуры
def test_response_structure():
    response = client.post("/predict", json=valid_sample)
    json_data = response.json()
    assert isinstance(json_data, dict)
    assert "predicted_price" in json_data
    assert isinstance(json_data["predicted_price"], (float, int))
