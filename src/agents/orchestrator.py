from src.agents.anomaly_detection_agent import AnomalyDetectionAgent
from src.agents.forecast_agent import ForecastAgent
from src.agents.inventory_agent import InventoryAgent
from src.agents.trend_analysis_agent import TrendAnalysisAgent


class DemandDecisionOrchestrator:
    """Coordinates forecasting, trend analysis, anomaly detection, and inventory decision agents."""

    def __init__(self):
        self.forecast_agent = ForecastAgent()
        self.trend_analysis_agent = TrendAnalysisAgent()
        self.anomaly_detection_agent = AnomalyDetectionAgent()
        self.inventory_agent = InventoryAgent()

    def run(self, request_data: dict) -> dict:
        forecast_result = self.forecast_agent.run(request_data)
        predicted_demand = forecast_result["predicted_demand"]

        trend_result = self.trend_analysis_agent.run(
            request_data=request_data,
            predicted_demand=predicted_demand,
        )

        anomaly_result = self.anomaly_detection_agent.run(
            request_data=request_data,
            predicted_demand=predicted_demand,
            trend_result=trend_result,
        )

        inventory_result = self.inventory_agent.run(predicted_demand)

        return {
            "predicted_demand": predicted_demand,
            "recommendation": inventory_result["recommendation"],
            "confidence_level": inventory_result["confidence_level"],
            "anomaly_warning": anomaly_result["anomaly_warning"],
            "trend": trend_result["trend"],
            "trend_reason": trend_result["trend_reason"],
            "anomaly_severity": anomaly_result["severity"],
            "agents": {
                "forecast_agent": forecast_result,
                "trend_analysis_agent": trend_result,
                "anomaly_detection_agent": anomaly_result,
                "inventory_agent": inventory_result,
            },
        }
