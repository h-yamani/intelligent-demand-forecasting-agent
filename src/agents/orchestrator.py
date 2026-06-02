from src.agents.forecast_agent import ForecastAgent
from src.agents.inventory_agent import InventoryAgent


class DemandDecisionOrchestrator:
    """Coordinates forecasting and inventory decision agents."""

    def __init__(self):
        self.forecast_agent = ForecastAgent()
        self.inventory_agent = InventoryAgent()

    def run(self, request_data: dict) -> dict:
        forecast_result = self.forecast_agent.run(request_data)

        predicted_demand = forecast_result["predicted_demand"]

        inventory_result = self.inventory_agent.run(predicted_demand)

        return {
            "predicted_demand": predicted_demand,
            "recommendation": inventory_result["recommendation"],
            "confidence_level": inventory_result["confidence_level"],
            "anomaly_warning": inventory_result["anomaly_warning"],
            "agents": {
                "forecast_agent": forecast_result,
                "inventory_agent": inventory_result,
            },
        }

