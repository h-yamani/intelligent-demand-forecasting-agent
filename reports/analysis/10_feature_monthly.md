# Feature Analysis: Monthly Seasonality

## Objective
To capture long-term seasonal patterns across the year.

## Visualization
Average sales aggregated by month.

## Key Observations
- Demand peaks during specific months
- Declines observed in later months
- Clear cyclical yearly pattern

## Interpretation
Demand is influenced by annual cycles, likely driven by external factors such as consumer behavior or seasonal demand shifts.

## Feature Justification
- `month`: captures discrete seasonal phases
- `sin_month`, `cos_month`: encode smooth cyclical transitions
- Enables model to learn continuous seasonal effects

## Conclusion
Monthly seasonality is a key driver of demand and essential for long-horizon forecasting.
