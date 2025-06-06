import streamlit as st
import requests

st.set_page_config(page_title="Car Price Predictor", layout="centered")
st.title("🚗 Предсказание цены автомобиля")

st.markdown("Введите параметры автомобиля, чтобы получить примерную рыночную цену.")

manufacturer = st.text_input("Производитель", "HONDA")
model = st.text_input("Модель", "CIVIC")
category = st.selectbox("Категория", ["Sedan", "Hatchback", "Jeep", "Coupe", "Convertible"])
leather = st.selectbox("Кожаный салон", ["Да", "Нет"])
fuel_type = st.selectbox("Тип топлива", ["Petrol", "Diesel", "Hybrid", "CNG"])
engine_volume = st.number_input("Объём двигателя (л)", min_value=0.6, max_value=7.0, value=1.8, step=0.1)
mileage = st.number_input("Пробег (км)", min_value=0, value=90000, step=1000)
cylinders = st.number_input("Цилиндры", min_value=1, max_value=12, value=4)
gear_box = st.selectbox("Коробка передач", ["Automatic", "Manual", "Tiptronic", "Variator"])
drive_wheels = st.selectbox("Привод", ["Front", "Rear", "4x4"])
doors = st.number_input("Количество дверей", min_value=2, max_value=5, value=4)
wheel = st.selectbox("Руль", ["Left", "Right"])
color = st.text_input("Цвет", "Black")
airbags = st.number_input("Подушки безопасности", min_value=0, max_value=20, value=4)
age = st.number_input("Возраст авто", min_value=0, max_value=40, value=10)
levy_rate = st.number_input("Налог как доля от цены (например, 0.05)", min_value=0.0, max_value=1.0, value=0.05)


leather_val = 1 if leather == "Да" else 0

sample = {
    "Manufacturer": manufacturer,
    "Model": model,
    "Category": category,
    "Leather_interior": leather_val,
    "Fuel_type": fuel_type,
    "Engine_volume": engine_volume,
    "Mileage": int(mileage),
    "Cylinders": int(cylinders),
    "Gear_box_type": gear_box,
    "Drive_wheels": drive_wheels,
    "Doors": int(doors),
    "Wheel": wheel,
    "Color": color,
    "Airbags": int(airbags),
    "Age": int(age),
    "Levy_rate": levy_rate
}

if st.button("Предсказать цену"):
    try:
        response = requests.post("http://localhost:8000/predict", json=sample)
        if response.status_code == 200:
            price = response.json()["predicted_price"]
            st.success(f"Оценочная цена: {price:,.2f}")
        else:
            st.error("Ошибка при обращении к API")
    except Exception as e:
        st.error(f"Ошибка: {e}")
