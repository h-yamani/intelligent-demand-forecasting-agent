import os


class LLMReasoningAgent:
    """LLM-style reasoning agent for senior-level inventory decision explanation."""

    def run(
        self,
        predicted_demand: float,
        recommendation: str,
        confidence_level: str,
        anomaly_warning: str,
        trend: str,
        trend_reason: str,
        anomaly_severity: str,
        optimization_result: dict | None = None,
    ) -> dict:
        optimization_result = optimization_result or {}

        decision = optimization_result.get("decision", recommendation)
        reorder_point = optimization_result.get("reorder_point")
        order_quantity = optimization_result.get("recommended_order_quantity")
        stockout_risk = optimization_result.get("stockout_risk", "unknown")
        overstock_risk = optimization_result.get("overstock_risk", "unknown")

        executive_summary = (
            f"Demand is forecast at {predicted_demand} units and the trend is {trend}. "
            f"The optimized inventory decision is: {decision}."
        )

        reasoning_steps = [
            f"The forecasting model predicted demand of {predicted_demand} units.",
            f"The trend analysis agent classified demand as {trend}.",
            trend_reason,
            f"The anomaly detection agent reported: {anomaly_warning}.",
            f"The inventory optimization agent calculated a reorder point of {reorder_point}.",
            f"The recommended order quantity is {order_quantity}.",
            f"Stockout risk is {stockout_risk} and overstock risk is {overstock_risk}.",
        ]

        if stockout_risk == "high" or anomaly_severity == "high":
            risk_assessment = (
                "High operational risk. Immediate inventory review is recommended."
            )
        elif stockout_risk == "medium" or anomaly_severity == "medium":
            risk_assessment = (
                "Medium operational risk. Inventory should be monitored closely."
            )
        else:
            risk_assessment = (
                "Low operational risk. No urgent intervention is required."
            )

        next_best_actions = [
            decision,
            "Monitor demand changes over the next forecasting cycle.",
            "Re-run the forecast if price, promotion, stock, or lead-time conditions change.",
        ]

        return {
            "agent": "LLMReasoningAgent",
            "mode": "fallback" if not os.getenv("OPENAI_API_KEY") else "llm_ready",
            "executive_summary": executive_summary,
            "reasoning_steps": reasoning_steps,
            "risk_assessment": risk_assessment,
            "next_best_actions": next_best_actions,
        }
