# Feature Analysis: Long-Term Trend

## Objective
To understand gradual changes in demand over time.

## Visualization
30-day rolling average overlaid on raw sales.

## Key Observations
- Smooth upward and downward shifts in demand
- Long-term structure clearly visible

## Interpretation
Demand evolves slowly over time, indicating non-stationary behavior.

## Feature Justification
- `rolling_mean_30`: captures long-term movement
- `expanding_mean`: captures historical baseline behavior
- Helps model adapt to evolving demand patterns

## Conclusion
Capturing long-term trends is essential for stable and realistic forecasting.
