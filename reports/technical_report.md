# Intelligent Demand Forecasting System
## Technical Report

---

## 1. Introduction

This project develops a production-oriented demand forecasting system with a focus on understanding temporal structure, feature engineering, and predictive modeling.

The objective is not only to build accurate models, but to analyze and justify the data generation process through structured feature design.

---

## 2. Problem Formulation

The dataset represents a multi-series time series forecasting problem:

- Multiple store-item combinations
- Daily observations
- Target: sales

The key challenge is to capture:
- temporal dependencies
- seasonality
- external effects (promotion, price)

---

## 3. Time Series Characteristics

### 3.1 Trend and Noise
Sales data exhibits high short-term volatility but a clear underlying trend.

- Noise dominates raw observations
- Rolling statistics reveal stable patterns

### 3.2 Seasonality
Two strong seasonal structures are present:

- Weekly seasonality (day-of-week effects)
- Monthly/yearly seasonality (long-term cycles)

### 3.3 Temporal Dependency
Autocorrelation analysis shows:

- strong dependency across time
- repeating periodic structure
- non-random behavior

---

## 4. Feature Engineering Strategy

Feature engineering transforms raw data into structured signals.

### 4.1 Lag Features (Memory)
- sales_lag_1, 7, 14, 30

These capture temporal dependency and repeating patterns.

### 4.2 Rolling Features (Trend)
- rolling_mean_7, 30
- rolling_std

These extract signal from noise and stabilize learning.

### 4.3 Expanding Features (Long-Term Behavior)
- expanding_mean

Captures historical baseline demand.

### 4.4 Calendar Features (Seasonality)
- dayofweek, month
- cyclical encoding (sin/cos)

Captures periodic structure.

### 4.5 Price Features
- price_change
- price_lag

Weak standalone signal, but useful in interactions.

### 4.6 Promotion Features
- promo_lag
- promo_rolling

Strong driver of demand spikes.

### 4.7 Aggregate Features
- store_avg_sales
- item_avg_sales

Provide global context.

---

## 5. Feature Validation

### 5.1 Lag Analysis
Lag features show strong correlation with current sales, confirming temporal dependency.

### 5.2 Rolling Analysis
Rolling averages effectively reveal underlying trends.

### 5.3 Seasonality Analysis
Clear weekly and monthly patterns validate calendar features.

### 5.4 Autocorrelation
Confirms structured memory and periodic behavior.

### 5.5 Correlation Analysis
- Temporal features: strong predictors
- Promotion: moderate impact
- Price: weak direct effect

### 5.6 Distribution Analysis
Sales distribution is right-skewed, indicating:
- non-linear structure
- presence of extreme events

---

## 6. Modeling Implications

Based on analysis:

- Time dependency must be modeled explicitly
- Tree-based models (LightGBM/XGBoost) are appropriate
- Feature interactions are critical
- Linear models are insufficient

---

## 7. Key Insights

- Demand is driven primarily by temporal structure
- Weekly repetition is a dominant signal
- Promotions significantly increase demand
- Price alone is not a strong predictor
- Noise must be filtered to extract signal

---

## 8. Conclusion

This project demonstrates that effective demand forecasting requires:

- deep understanding of time series behavior
- structured feature engineering
- validation of assumptions through analysis

The resulting system moves beyond basic modeling toward a production-ready, interpretable forecasting pipeline.

---

## 9. Future Work

- Model training with feature importance analysis
- MLflow integration
- API deployment
- Agent-based decision system

