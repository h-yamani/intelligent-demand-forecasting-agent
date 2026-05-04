import pandas as pd
import numpy as np

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values(["store_id", "item_id", "date"])

    group_cols = ["store_id", "item_id"]

    # ======================
    # Lag features
    # ======================
    for lag in [1, 7, 14, 30]:
        df[f"sales_lag_{lag}"] = df.groupby(group_cols)["sales"].shift(lag)

    # ======================
    # Rolling statistics
    # ======================
    for window in [7, 14, 30]:
        df[f"rolling_mean_{window}"] = (
            df.groupby(group_cols)["sales"]
            .shift(1)
            .rolling(window)
            .mean()
        )

        df[f"rolling_std_{window}"] = (
            df.groupby(group_cols)["sales"]
            .shift(1)
            .rolling(window)
            .std()
        )

    # ======================
    # Expanding (long-term memory)
    # ======================
    df["expanding_mean"] = (
        df.groupby(group_cols)["sales"]
        .shift(1)
        .expanding()
        .mean()
        .reset_index(level=[0,1], drop=True)
    )

    # ======================
    # Calendar features
    # ======================
    df["dayofweek"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month
    df["weekofyear"] = df["date"].dt.isocalendar().week.astype(int)

    df["is_weekend"] = df["dayofweek"].isin([5, 6]).astype(int)

    # ======================
    # Cyclical encoding
    # ======================
    df["sin_day"] = np.sin(2 * np.pi * df["dayofweek"] / 7)
    df["cos_day"] = np.cos(2 * np.pi * df["dayofweek"] / 7)

    df["sin_month"] = np.sin(2 * np.pi * df["month"] / 12)
    df["cos_month"] = np.cos(2 * np.pi * df["month"] / 12)

    # ======================
    # Price features
    # ======================
    df["price_lag_1"] = df.groupby(group_cols)["price"].shift(1)
    df["price_change"] = df.groupby(group_cols)["price"].pct_change()

    df["price_rolling_mean_7"] = (
        df.groupby(group_cols)["price"]
        .shift(1)
        .rolling(7)
        .mean()
    )

    # ======================
    # Promotion features
    # ======================
    df["promo_lag_1"] = df.groupby(group_cols)["promo"].shift(1)

    df["promo_rolling_7"] = (
        df.groupby(group_cols)["promo"]
        .shift(1)
        .rolling(7)
        .sum()
    )

    # ======================
    # Global aggregates
    # ======================
    df["store_avg_sales"] = df.groupby("store_id")["sales"].transform("mean")
    df["item_avg_sales"] = df.groupby("item_id")["sales"].transform("mean")

    # ======================
    # Clean
    # ======================
    df = df.dropna()

    return df
