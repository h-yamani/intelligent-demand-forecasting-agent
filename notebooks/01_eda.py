import pandas as pd

df = pd.read_csv("archive/retail_sales.csv")
df["date"] = pd.to_datetime(df["date"]) 

print("Shape:", df.shape)
print("\nColumns:", df.columns)
print("\nInfo:")
print(df.info())

print("\nMissing values:")
print(df.isna().sum())

print("\nBasic stats:")
print(df.describe())

print("\nNumber of stores:", df["store_id"].nunique())
print("Number of items:", df["item_id"].nunique())

print("\nStart date:", df["date"].min())
print("End date:", df["date"].max())

df_sample = df[(df["store_id"] == "store_1") & (df["item_id"] == "item_1")]
df_sample = df_sample.sort_values("date")

print("\nSample rows:")
print(df_sample.head())



import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
plt.plot(df_sample["date"], df_sample["sales"])
plt.title("Sales over time (store_1, item_1)")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("reports/sales_plot.png")


