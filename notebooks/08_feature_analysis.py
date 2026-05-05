import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from src.features.build_features import create_features

# ======================
# Load & prepare
# ======================
df = pd.read_csv("archive/retail_sales.csv")
df["date"] = pd.to_datetime(df["date"])

# Focus on ONE series (important)
df = df[(df["store_id"] == "store_1") & (df["item_id"] == "item_1")].copy()

df = create_features(df)
df = df.sort_values("date")

# ======================
# 1. Full yearly trend
# ======================
year_df = df.iloc[:365]

plt.figure(figsize=(12,5))
plt.plot(year_df["date"], year_df["sales"], label="Sales", alpha=0.5)
plt.plot(year_df["date"], year_df["rolling_mean_7"], label="Rolling Mean 7", linewidth=2)
plt.title("Yearly Trend (Signal vs Noise)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/figures/14_year_trend.png")

# ======================
# 2. Weekly seasonality
# ======================
plt.figure()
df.groupby("dayofweek")["sales"].mean().plot(kind="bar")
plt.title("Weekly Seasonality")
plt.savefig("reports/figures/15_week_pattern.png")

# ======================
# 3. Monthly seasonality
# ======================
plt.figure()
df.groupby("month")["sales"].mean().plot(kind="bar")
plt.title("Monthly Seasonality")
plt.savefig("reports/figures/16_month_pattern.png")

# ======================
# 4. Lag relationships (multiple)
# ======================
sample = df.sample(min(5000, len(df)))

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.scatter(sample["sales_lag_1"], sample["sales"], alpha=0.3)
plt.title("Lag-1")

plt.subplot(1,2,2)
plt.scatter(sample["sales_lag_7"], sample["sales"], alpha=0.3)
plt.title("Lag-7")

plt.tight_layout()
plt.savefig("reports/figures/17_lag_comparison.png")

# ======================
# 5. Rolling vs actual (variance view)
# ======================
plt.figure(figsize=(12,5))
plt.plot(year_df["date"], year_df["sales"], alpha=0.4)
plt.plot(year_df["date"], year_df["rolling_mean_30"], linewidth=2)
plt.title("Long-term Trend (30-day smoothing)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/figures/18_long_trend.png")

# ======================
# 6. Autocorrelation (VERY important)
# ======================
from pandas.plotting import autocorrelation_plot

plt.figure()
autocorrelation_plot(df["sales"])
plt.title("Autocorrelation (Temporal Dependency)")
plt.savefig("reports/figures/19_autocorrelation.png")

# ======================
# 7. Feature correlation matrix
# ======================
feature_cols = [
    "sales_lag_1","sales_lag_7","sales_lag_30",
    "rolling_mean_7","rolling_mean_30",
    "price","promo"
]

corr = df[feature_cols + ["sales"]].corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Feature Correlation Matrix")
plt.savefig("reports/figures/20_correlation.png")

# ======================
# 8. Distribution shift
# ======================
plt.figure()
sns.histplot(df["sales"], bins=50, kde=True)
plt.title("Sales Distribution")
plt.savefig("reports/figures/21_distribution.png")

print("Advanced feature analysis completed.")
