import json
import pandas as pd
import numpy as np
import yaml
from sklearn.metrics import mean_absolute_error, mean_squared_error

from src.features.build_features import create_features


def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / np.maximum(y_true, 1))) * 100


def wape(y_true, y_pred):
    return np.sum(np.abs(y_true - y_pred)) / np.sum(np.abs(y_true)) * 100


with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

df = pd.read_csv(config["data"]["raw_path"])
df["date"] = pd.to_datetime(df["date"])
df = create_features(df)

test = df[df["date"] > config["split"]["valid_end"]].copy()

y_true = test["sales"]
y_pred = test["sales_lag_7"]

metrics = {
    "model": "lag_7_baseline",
    "MAE": mean_absolute_error(y_true, y_pred),
    "RMSE": mean_squared_error(y_true, y_pred, squared=False),
    "MAPE": mape(y_true, y_pred),
    "WAPE": wape(y_true, y_pred),
}

with open("reports/modeling/baseline_metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

print(metrics)
