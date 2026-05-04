import pandas as pd

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values(["store_id", "item_id", "date"])

    group_cols = ["store_id", "item_id"]

    df["sales_lag_1"] = df.groupby(group_cols)["sales"].shift(1)
    df["sales_lag_7"] = df.groupby(group_cols)["sales"].shift(7)
    df["sales_lag_30"] = df.groupby(group_cols)["sales"].shift(30)

    df["sales_rolling_mean_7"] = (
        df.groupby(group_cols)["sales"].shift(1).rolling(7).mean()
    )

    df["sales_rolling_std_7"] = (
        df.groupby(group_cols)["sales"].shift(1).rolling(7).std()
    )

    df["dayofweek"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month

    return df.dropna()
