import pandas as pd

from src.features.build_features import create_features


def test_create_features_outputs_expected_columns():
    df = pd.DataFrame(
        {
            "date": pd.date_range(start="2023-01-01", periods=40),
            "store_id": ["store_1"] * 40,
            "item_id": ["item_1"] * 40,
            "sales": list(range(40)),
            "price": [10.0] * 40,
            "promo": [0] * 40,
        }
    )

    result = create_features(df)

    expected_columns = [
        "sales_lag_1",
        "sales_lag_7",
        "sales_lag_30",
        "rolling_mean_7",
        "rolling_std_7",
        "dayofweek",
        "month",
    ]

    for column in expected_columns:
        assert column in result.columns

    assert not result.empty
