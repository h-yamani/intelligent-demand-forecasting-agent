# Feature Analysis: Temporal Dependency (Lag Features)

## Objective
To evaluate how past sales influence current demand.

## Visualization
Scatter plots of lagged sales vs current sales.

## Key Observations
- Strong positive correlation between lagged values and current sales
- Lag-7 shows stronger structure than lag-1
- Indicates repeating weekly behavior

## Interpretation
Demand is highly dependent on past observations, particularly at weekly intervals.

## Feature Justification
- `sales_lag_1`: captures immediate short-term memory
- `sales_lag_7`: captures weekly repetition
- `sales_lag_30`: captures longer-term periodicity
- These features form the core predictive signals

## Conclusion
Lag features are the most powerful predictors in time series forecasting due to strong temporal dependency.
