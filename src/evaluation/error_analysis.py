import json
import yaml
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from src.features.build_features import create_features

with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

df = pd.read_csv(config["data"]["raw_path"])
df["date"] = pd.to_datetime(df["date"])
df = create_features(df)

test = df[df["date"] > config["split"]["valid_end"]].copy()

X_test = test.drop(columns=["sales", "date"])
y_test = test["sales"]

for col in ["store_id", "item_id"]:
    X_test[col] = X_test[col].astype("category")

model = joblib.load(config["output"]["model_path"])
test["prediction"] = model.predict(X_test)
test["absolute_error"] = np.abs(test["sales"] - test["prediction"])

worst_pairs = (
    test.groupby(["store_id", "item_id"])["absolute_error"]
    .mean()
    .reset_index()
    .sort_values("absolute_error", ascending=False)
    .head(20)
)

worst_pairs.to_csv("reports/modeling/worst_store_item_pairs.csv", index=False)

plt.figure(figsize=(10, 5))
plt.hist(test["absolute_error"], bins=50)
plt.title("Prediction Error Distribution")
plt.xlabel("Absolute Error")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("reports/figures/error_distribution.png")

summary = {
    "mean_absolute_error": float(test["absolute_error"].mean()),
    "median_absolute_error": float(test["absolute_error"].median()),
    "max_absolute_error": float(test["absolute_error"].max()),
}

with open("reports/modeling/error_summary.json", "w") as f:
    json.dump(summary, f, indent=4)

print(summary)
print("Error analysis completed.")
