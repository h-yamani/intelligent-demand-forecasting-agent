# Feature Analysis: Correlation Structure

## Objective
To understand relationships between features and the target variable.

## Visualization
Correlation heatmap.

## Key Observations
- Strong correlation between lag/rolling features and sales
- Moderate correlation for promotion
- Weak correlation for price

## Interpretation
Temporal features dominate predictive power, while price alone is not a strong driver.

## Feature Justification
- Prioritizes lag and rolling features
- Supports inclusion of promo interactions
- Suggests non-linear modeling for price

## Conclusion
Effective forecasting relies primarily on temporal and behavioral features rather than isolated variables.
