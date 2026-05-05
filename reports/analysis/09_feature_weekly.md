# Feature Analysis: Weekly Seasonality

## Objective
To identify repeating demand patterns within a weekly cycle.

## Visualization
Average sales aggregated by day of week.

## Key Observations
- Clear peak in mid-week
- Noticeable decline during weekends
- Pattern is stable and consistent

## Interpretation
Customer behavior follows a weekly rhythm, with predictable variations in demand across different days.

## Feature Justification
- `dayofweek`: captures discrete weekly behavior
- `sin_day`, `cos_day`: encode cyclical structure and preserve continuity
- These features allow the model to learn periodic patterns effectively

## Conclusion
Weekly seasonality is a strong and reliable signal in the data and must be explicitly modeled.
