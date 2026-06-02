class TrendAnalysisAgent:
    """Analyzes demand trend based on forecast, promotion, and price signals."""

    def run(self, request_data: dict, predicted_demand: float) -> dict:
        price = float(request_data.get("price", 0))
        promo = int(request_data.get("promo", 0))

        if predicted_demand >= 30:
            trend = "increasing"
            trend_reason = "Forecasted demand is high."
        elif predicted_demand <= 8:
            trend = "decreasing"
            trend_reason = "Forecasted demand is low."
        else:
            trend = "stable"
            trend_reason = "Forecasted demand is within a normal range."

        if promo == 1 and predicted_demand >= 20:
            trend = "promotion-driven increase"
            trend_reason = "Promotion is active and demand is elevated."

        if price > 20 and predicted_demand <= 10:
            trend = "price-sensitive decrease"
            trend_reason = "High price may be reducing demand."

        return {
            "agent": "TrendAnalysisAgent",
            "trend": trend,
            "trend_reason": trend_reason,
        }
