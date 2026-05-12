import pandas as pd
import joblib
import matplotlib.pyplot as plt

from lightgbm import LGBMRegressor
from sklearn.metrics import mean_squared_error
from src.features.build_features import create_features

df = pd.read_csv("archive/retail_sales.csv")
df["date"] = pd.to_datetime(df["date"])

df = create_features(df)

split = int(len(df) * 0.8)
train = df.iloc[:split]
test = df.iloc[split:]

X_train = train.drop(columns=["sales", "date"])
y_train = train["sales"]

X_test = test.drop(columns=["sales", "date"])
y_test = test["sales"]

# Encode categorical IDs
for col in ["store_id", "item_id"]:
    X_train[col] = X_train[col].astype("category")
    X_test[col] = X_test[col].astype("category")

model = LGBMRegressor(n_estimators=200)
model.fit(X_train, y_train)

preds = model.predict(X_test)
rmse = mean_squared_error(y_test, preds, squared=False)
print("RMSE:", rmse)

joblib.dump(model, "models/lgbm_model.pkl")

importances = model.feature_importances_

plt.figure(figsize=(10, 5))
plt.barh(X_train.columns, importances)
plt.title("Feature Importance")
plt.tight_layout()
plt.savefig("reports/figures/feature_importance.png")
