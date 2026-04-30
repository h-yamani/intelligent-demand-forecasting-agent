import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("archive/retail_sales.csv")

weekday_sales = df.groupby("weekday")["sales"].mean().reset_index()

plt.figure(figsize=(8, 5))
plt.bar(weekday_sales["weekday"], weekday_sales["sales"])
plt.title("Average Sales by Weekday")
plt.xlabel("Weekday")
plt.ylabel("Average Sales")
plt.tight_layout()
plt.savefig("reports/figures/04_seasonality_weekday.png")
print("Saved: reports/figures/04_seasonality_weekday.png")
