from typing import Any, Dict, TypedDict

from langgraph.graph import END, StateGraph

from src.agents.anomaly_detection_agent import AnomalyDetectionAgent
from src.agents.forecast_agent import ForecastAgent
from src.agents.inventory_agent import InventoryAgent
from src.agents.trend_analysis_agent import TrendAnalysisAgent


class DemandDecisionState(TypedDict, total=False):
    request_data: Dict[str, Any]
    forecast_result: Dict[str, Any]
    trend_result: Dict[str, Any]
    anomaly_result: Dict[str, Any]
    inventory_result: Dict[str, Any]
    predicted_demand: float


class LangGraphDemandDecisionOrchestrator:
    """LangGraph workflow for coordinating demand forecasting agents."""

    def __init__(self):
        self.forecast_agent = ForecastAgent()
        self.trend_analysis_agent = TrendAnalysisAgent()
        self.anomaly_detection_agent = AnomalyDetectionAgent()
        self.inventory_agent = InventoryAgent()
        self.graph = self._build_graph()

    def _forecast_node(self, state: DemandDecisionState) -> DemandDecisionState:
        forecast_result = self.forecast_agent.run(state["request_data"])
        return {
            **state,
            "forecast_result": forecast_result,
            "predicted_demand": forecast_result["predicted_demand"],
        }

    def _trend_node(self, state: DemandDecisionState) -> DemandDecisionState:
        trend_result = self.trend_analysis_agent.run(
            request_data=state["request_data"],
            predicted_demand=state["predicted_demand"],
        )
        return {**state, "trend_result": trend_result}

    def _anomaly_node(self, state: DemandDecisionState) -> DemandDecisionState:
        anomaly_result = self.anomaly_detection_agent.run(
            request_data=state["request_data"],
            predicted_demand=state["predicted_demand"],
            trend_result=state["trend_result"],
        )
        return {**state, "anomaly_result": anomaly_result}

    def _inventory_node(self, state: DemandDecisionState) -> DemandDecisionState:
        inventory_result = self.inventory_agent.run(state["predicted_demand"])
        return {**state, "inventory_result": inventory_result}

    def _build_graph(self):
        workflow = StateGraph(DemandDecisionState)

        workflow.add_node("forecast_agent", self._forecast_node)
        workflow.add_node("trend_analysis_agent", self._trend_node)
        workflow.add_node("anomaly_detection_agent", self._anomaly_node)
        workflow.add_node("inventory_decision_agent", self._inventory_node)

        workflow.set_entry_point("forecast_agent")
        workflow.add_edge("forecast_agent", "trend_analysis_agent")
        workflow.add_edge("trend_analysis_agent", "anomaly_detection_agent")
        workflow.add_edge("anomaly_detection_agent", "inventory_decision_agent")
        workflow.add_edge("inventory_decision_agent", END)

        return workflow.compile()

    def run(self, request_data: dict) -> dict:
        state = self.graph.invoke({"request_data": request_data})

        forecast_result = state["forecast_result"]
        trend_result = state["trend_result"]
        anomaly_result = state["anomaly_result"]
        inventory_result = state["inventory_result"]
        predicted_demand = state["predicted_demand"]

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
                "inventory_decision_agent": inventory_result,
            },
            "workflow": "LangGraph",
        }
