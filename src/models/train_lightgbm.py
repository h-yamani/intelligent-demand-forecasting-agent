import json
import yaml
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from lightgbm import LGBMRegressor
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

train = df[df["date"] <= config["split"]["train_end"]]
valid = df[
    (df["date"] > config["split"]["train_end"]) &
    (df["date"] <= config["split"]["valid_end"])
]
test = df[df["date"] > config["split"]["valid_end"]]

drop_cols = ["sales", "date"]

X_train = train.drop(columns=drop_cols)
y_train = train["sales"]

X_valid = valid.drop(columns=drop_cols)
y_valid = valid["sales"]

X_test = test.drop(columns=drop_cols)
y_test = test["sales"]

for col in ["store_id", "item_id"]:
    X_train[col] = X_train[col].astype("category")
    X_valid[col] = X_valid[col].astype("category")
    X_test[col] = X_test[col].astype("category")

model = LGBMRegressor(
    n_estimators=config["model"]["n_estimators"],
    learning_rate=config["model"]["learning_rate"],
    num_leaves=config["model"]["num_leaves"],
    random_state=config["model"]["random_state"]
)

model.fit(X_train, y_train, eval_set=[(X_valid, y_valid)])

preds = model.predict(X_test)

metrics = {
    "model": "lightgbm",
    "MAE": mean_absolute_error(y_test, preds),
    "RMSE": mean_squared_error(y_test, preds, squared=False),
    "MAPE": mape(y_test, preds),
    "WAPE": wape(y_test, preds),
}

print(metrics)

with open(config["output"]["metrics_path"], "w") as f:
    json.dump(metrics, f, indent=4)

joblib.dump(model, config["output"]["model_path"])

with open(config["output"]["feature_list_path"], "w") as f:
    json.dump(list(X_train.columns), f, indent=4)

importance = pd.DataFrame({
    "feature": X_train.columns,
    "importance": model.feature_importances_
}).sort_values("importance", ascending=False)

plt.figure(figsize=(12, 8))
plt.barh(importance["feature"][:20][::-1], importance["importance"][:20][::-1])
plt.title("Top 20 Feature Importances")
plt.tight_layout()
plt.savefig(config["output"]["feature_importance_path"])

print("LightGBM training completed.")
