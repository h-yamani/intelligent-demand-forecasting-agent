import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("archive/retail_sales.csv")
df["date"] = pd.to_datetime(df["date"])

df_sample = df[(df["store_id"] == "store_1") & (df["item_id"] == "item_1")]
df_sample = df_sample.sort_values("date")

plt.figure(figsize=(10,5))
plt.plot(df_sample["date"], df_sample["sales"])
plt.title("Sales over time (store_1, item_1)")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("reports/figures/sales_trend.png")
