import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("archive/retail_sales.csv")
df["date"] = pd.to_datetime(df["date"])

sample = df[(df["store_id"] == "store_1") & (df["item_id"] == "item_1")]
sample = sample.sort_values("date")

plt.figure(figsize=(12, 5))
plt.plot(sample["date"], sample["sales"])
plt.title("Sales Trend for store_1 / item_1")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("reports/figures/03_single_series_trend.png")
print("Saved: reports/figures/03_single_series_trend.png")
