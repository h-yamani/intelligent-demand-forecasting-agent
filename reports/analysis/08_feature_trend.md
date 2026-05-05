# Feature Analysis: Signal vs Noise (Trend Extraction)

## Objective
To distinguish between short-term fluctuations (noise) and the underlying demand signal in the time series.

## Visualization
Rolling mean (7-day) compared with raw sales.

## Key Observations
- Raw sales exhibit high-frequency fluctuations and spikes
- The rolling mean smooths noise and reveals a clear underlying structure
- The trend evolves gradually over time

## Interpretation
The observed volatility is largely driven by short-term noise, while the rolling mean captures the true demand signal. This separation is essential for stable forecasting.

## Feature Justification
- `rolling_mean_7`: captures short-term trend while filtering noise
- `rolling_mean_30`: captures long-term structural changes
- These features allow the model to learn stable patterns instead of reacting to noise

## Conclusion
Demand is composed of signal + noise. Rolling features are essential to extract meaningful structure and improve model robustness.
