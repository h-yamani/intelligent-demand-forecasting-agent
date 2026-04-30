import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("archive/retail_sales.csv")

promo_sales = df.groupby("promo")["sales"].mean().reset_index()
promo_sales["promo_label"] = promo_sales["promo"].map({0: "No Promo", 1: "Promo"})

plt.figure(figsize=(7, 5))
plt.bar(promo_sales["promo_label"], promo_sales["sales"])
plt.title("Average Sales: Promo vs No Promo")
plt.xlabel("Promotion Status")
plt.ylabel("Average Sales")
plt.tight_layout()
plt.savefig("reports/figures/06_promo_effect.png")
print("Saved: reports/figures/06_promo_effect.png")

print(promo_sales)
