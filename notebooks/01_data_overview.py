import pandas as pd

df = pd.read_csv("archive/retail_sales.csv")
df["date"] = pd.to_datetime(df["date"])

print("Dataset shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isna().sum())

print("\nBasic statistics:")
print(df.describe())

print("\nNumber of stores:", df["store_id"].nunique())
print("Number of items:", df["item_id"].nunique())
print("Number of store-item series:", df[["store_id", "item_id"]].drop_duplicates().shape[0])

print("\nStart date:", df["date"].min())
print("End date:", df["date"].max())
