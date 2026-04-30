import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("archive/retail_sales.csv")

month_sales = df.groupby("month")["sales"].mean().reset_index()

plt.figure(figsize=(8, 5))
plt.bar(month_sales["month"], month_sales["sales"])
plt.title("Average Sales by Month")
plt.xlabel("Month")
plt.ylabel("Average Sales")
plt.tight_layout()
plt.savefig("reports/figures/05_seasonality_month.png")
print("Saved: reports/figures/05_seasonality_month.png")
