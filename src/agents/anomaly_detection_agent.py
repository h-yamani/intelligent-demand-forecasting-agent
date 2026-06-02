class AnomalyDetectionAgent:
    """Detects unusual demand, price, and promotion patterns."""

    def run(
        self, request_data: dict, predicted_demand: float, trend_result: dict
    ) -> dict:
        price = float(request_data.get("price", 0))
        promo = int(request_data.get("promo", 0))
        trend = trend_result.get("trend", "unknown")

        anomaly_detected = False
        anomaly_warning = "No anomaly detected"
        severity = "low"

        if predicted_demand < 0:
            anomaly_detected = True
            anomaly_warning = "Negative demand prediction detected"
            severity = "high"

        elif predicted_demand >= 80:
            anomaly_detected = True
            anomaly_warning = "Unusually high demand detected"
            severity = "high"

        elif predicted_demand <= 3:
            anomaly_detected = True
            anomaly_warning = "Unusually low demand detected"
            severity = "medium"

        elif promo == 1 and predicted_demand >= 50:
            anomaly_detected = True
            anomaly_warning = "Promotion may be causing an unusual demand spike"
            severity = "medium"

        elif price > 30 and trend == "price-sensitive decrease":
            anomaly_detected = True
            anomaly_warning = "High price may be suppressing demand"
            severity = "medium"

        return {
            "agent": "AnomalyDetectionAgent",
            "anomaly_detected": anomaly_detected,
            "anomaly_warning": anomaly_warning,
            "severity": severity,
        }
