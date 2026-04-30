import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("archive/retail_sales.csv")
df["date"] = pd.to_datetime(df["date"])

daily_sales = df.groupby("date")["sales"].sum().reset_index()

plt.figure(figsize=(12, 5))
plt.plot(daily_sales["date"], daily_sales["sales"])
plt.title("Global Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("reports/figures/02_global_trend.png")
print("Saved: reports/figures/02_global_trend.png")
