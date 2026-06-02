class InventoryAgent:
    """Agent responsible for inventory recommendations."""

    def run(self, predicted_demand: float) -> dict:
        if predicted_demand >= 35:
            recommendation = "Increase inventory"
            confidence_level = "high"
            anomaly_warning = "Possible high-demand period"

        elif predicted_demand <= 10:
            recommendation = "Reduce inventory"
            confidence_level = "medium"
            anomaly_warning = "Possible low-demand period"

        else:
            recommendation = "Maintain current stock level"
            confidence_level = "high"
            anomaly_warning = "No anomaly detected"

        return {
            "recommendation": recommendation,
            "confidence_level": confidence_level,
            "anomaly_warning": anomaly_warning,
            "agent_name": "InventoryAgent",
            "agent_status": "success",
        }
