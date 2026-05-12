import json
import joblib
import pandas as pd

MODEL_PATH = "models/lgbm_model.pkl"
FEATURE_LIST_PATH = "models/feature_list.json"


model = joblib.load(MODEL_PATH)

with open(FEATURE_LIST_PATH, "r") as f:
    feature_list = json.load(f)


def predict_demand(input_data: dict) -> float:
    row = pd.DataFrame([input_data])

    row["date"] = pd.to_datetime(row["date"])
    row["weekday"] = row["date"].dt.dayofweek
    row["month"] = row["date"].dt.month

    row = row.drop(columns=["date"])

    for feature in feature_list:
        if feature not in row.columns:
            row[feature] = 0

    row = row[feature_list]

    for col in ["store_id", "item_id"]:
        row[col] = row[col].astype("category")

    prediction = model.predict(row)[0]
    return float(prediction)
