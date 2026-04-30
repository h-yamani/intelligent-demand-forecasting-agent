import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("archive/retail_sales.csv")

sample = df.sample(n=50000, random_state=42)

plt.figure(figsize=(8, 5))
plt.scatter(sample["price"], sample["sales"], alpha=0.2)
plt.title("Price vs Sales")
plt.xlabel("Price")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("reports/figures/07_price_effect.png")
print("Saved: reports/figures/07_price_effect.png")
