# train.py
import pandas as pd
import numpy as np
import optuna
from catboost import CatBoostRegressor, Pool
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error, r2_score
import joblib
import json
import os

# Загрузка данных
df = pd.read_csv("data/cars.csv")
df = df[df["Levy"] != "-"]
df.replace("-", np.nan, inplace=True)
df.dropna(inplace=True)

# Преобразование колонок
df["Levy"] = df["Levy"].astype(int)
df["Mileage"] = df["Mileage"].str.replace(" km", "").str.replace(",", "").astype(int)
df["Engine volume"] = df["Engine volume"].str.extract(r'([0-9.]+)').astype(float)
df["Cylinders"] = df["Cylinders"].astype(int)
df["Airbags"] = df["Airbags"].astype(int)
df["Leather interior"] = df["Leather interior"].map({"Yes": 1, "No": 0})
df["Doors"] = df["Doors"].str.extract(r"(\d+)").astype(int)


df["Age"] = 2025 - df["Prod. year"]
df["Levy_rate"] = df["Levy"] / df["Price"]

df.drop(columns=["ID", "Levy", "Prod. year"], inplace=True)

# Подготовка признаков
target = "Price"
features = [col for col in df.columns if col != target]
cat_cols = [col for col in features if df[col].dtype == "object"]

X = df[features]
y = df[target]

X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

train_pool = Pool(X_train, y_train, cat_features=cat_cols)
valid_pool = Pool(X_valid, y_valid, cat_features=cat_cols)

# Оптимизация гиперпараметров через Optuna
def objective(trial):
    params = {
        "iterations": 500,
        "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.3),
        "depth": trial.suggest_int("depth", 4, 10),
        "l2_leaf_reg": trial.suggest_float("l2_leaf_reg", 1e-2, 10.0),
        "loss_function": "RMSE",
        "random_seed": 42,
        "verbose": 0
    }

    model = CatBoostRegressor(**params)
    model.fit(train_pool, eval_set=valid_pool, early_stopping_rounds=50, verbose=0)
    preds = model.predict(X_valid)
    rmse = root_mean_squared_error(y_valid, preds)
    return rmse

study = optuna.create_study(direction="minimize")
study.optimize(objective, n_trials=15)

# Лучшая модель
best_params = study.best_trial.params
best_model = CatBoostRegressor(
    iterations=500,
    loss_function="RMSE",
    random_seed=42,
    verbose=100,
    **best_params
)

best_model.fit(train_pool, eval_set=valid_pool)

# Предсказания и метрики
preds = best_model.predict(X_valid)
rmse = root_mean_squared_error(y_valid, preds)
r2 = r2_score(y_valid, preds)

print(f"RMSE: {rmse:.2f}")
print(f"R²: {r2:.4f}")
print("Best parameters:", best_params)

# Сохраняем модель
os.makedirs("app/model", exist_ok=True)
joblib.dump(best_model, "app/model/model.pkl")

# Сохраняем метрики и параметры
results = {
    "rmse": round(rmse, 2),
    "r2": round(r2, 4),
    "params": best_params
}

with open("app/model/results.json", "w") as f:
    json.dump(results, f, indent=4)

print("Модель и метрики успешно сохранены.")