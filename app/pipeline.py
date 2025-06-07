import json
import os

import joblib
import numpy as np
import optuna
import pandas as pd
import yaml
from catboost import CatBoostRegressor, Pool
from logger import logger
from sklearn.metrics import r2_score, root_mean_squared_error
from sklearn.model_selection import train_test_split

try:
    logger.info("Loading configuration...")
    with open("app/config.yaml", "r") as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    logger.info("Configuration loaded successfully.")
except Exception as e:
    logger.error(f"Error loading configuration: {e}")
    raise

try:
    logger.info("Loading dataset...")
    df = pd.read_csv("app/data/cars.csv")
    df = df[df["Levy"] != "-"]
    df.replace("-", np.nan, inplace=True)
    df.dropna(inplace=True)
except Exception as e:
    logger.error(f"Error loading dataset: {e}")
    raise

try:
    df["Levy"] = df["Levy"].astype(int)
    df["Mileage"] = (
        df["Mileage"].str.replace(" km", "").str.replace(",", "").astype(int)
    )
    df["Engine volume"] = (
        df["Engine volume"].str.extract(r"([0-9.]+)").astype(float)
    )
    df["Cylinders"] = df["Cylinders"].astype(int)
    df["Airbags"] = df["Airbags"].astype(int)
    df["Leather interior"] = df["Leather interior"].map({"Yes": 1, "No": 0})
    df["Doors"] = df["Doors"].str.extract(r"(\d+)").astype(int)

    df["Age"] = 2025 - df["Prod. year"]
    df["Levy_rate"] = df["Levy"] / df["Price"]
    df.drop(columns=["ID", "Levy", "Prod. year"], inplace=True)
    logger.info("Columns processed successfully.")
except Exception as e:
    logger.error(f"Error processing columns: {e}")
    raise

target = "Price"
features = [col for col in df.columns if col != target]
cat_cols = [col for col in features if df[col].dtype == "object"]

X = df[features]
y = df[target]

try:
    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    train_pool = Pool(X_train, y_train, cat_features=cat_cols)
    valid_pool = Pool(X_valid, y_valid, cat_features=cat_cols)
    logger.info("Data split successfully.")
except Exception as e:
    logger.error(f"Error splitting data: {e}")
    raise

catboost_model = CatBoostRegressor(
    loss_function="RMSE", random_seed=42, verbose=100
)


def objective(trial):
    try:
        params = {
            "iterations": trial.suggest_int("iterations", 100, 1000),
            "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.3),
            "depth": trial.suggest_int("depth", 4, 10),
            "l2_leaf_reg": trial.suggest_float("l2_leaf_reg", 1e-2, 10.0),
            "loss_function": "RMSE",
            "random_seed": 42,
            "verbose": 0,
        }

        model = CatBoostRegressor(**params)
        model.fit(
            train_pool,
            eval_set=valid_pool,
            early_stopping_rounds=50,
            verbose=0,
        )

        preds = model.predict(X_valid)
        rmse = root_mean_squared_error(y_valid, preds)
        logger.info(f"RMSE: {rmse:.2f} for trial with params: {params}")
        return rmse
    except Exception as e:
        logger.error(f"Error during hyperparameter optimization: {e}")
        raise


try:
    logger.info("Starting hyperparameter optimization...")
    study = optuna.create_study(direction="minimize")
    study.optimize(objective, n_trials=config["n_trials"])
    logger.info(f"Best parameters found: {study.best_trial.params}")
except Exception as e:
    logger.error(f"Error during Optuna optimization: {e}")
    raise


try:
    best_params = study.best_trial.params
    best_model = CatBoostRegressor(
        iterations=best_params["iterations"],
        learning_rate=best_params["learning_rate"],
        depth=best_params["depth"],
        l2_leaf_reg=best_params["l2_leaf_reg"],
        loss_function="RMSE",
        random_seed=42,
        verbose=100,
    )

    best_model.fit(train_pool, eval_set=valid_pool)
    logger.info("Model trained successfully.")
except Exception as e:
    logger.error(f"Error training the model: {e}")
    raise


try:
    preds = best_model.predict(X_valid)
    rmse = root_mean_squared_error(y_valid, preds)
    r2 = r2_score(y_valid, preds)

    logger.info(f"RMSE: {rmse:.2f}")
    logger.info(f"R²: {r2:.4f}")
    logger.info(f"Best parameters: {best_params}")
except Exception as e:
    logger.error(f"Error during predictions or metrics calculation: {e}")
    raise

try:
    os.makedirs("app/model", exist_ok=True)
    joblib.dump(best_model, "app/model/model.pkl")

    results = {
        "rmse": round(rmse, 2),
        "r2": round(r2, 4),
        "params": best_params,
    }

    with open("app/model/results.json", "w") as f:
        json.dump(results, f, indent=4)

    logger.info("Model and results saved successfully.")
except Exception as e:
    logger.error(f"Error saving model or results: {e}")
    raise

logger.info("Training process completed.")
