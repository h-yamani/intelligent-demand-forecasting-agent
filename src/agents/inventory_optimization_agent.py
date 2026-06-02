class InventoryOptimizationAgent:
    """Optimizes inventory decisions using demand, stock, lead time, and risk logic."""

    def run(
        self,
        predicted_demand: float,
        current_stock: int = 20,
        lead_time_days: int = 3,
        safety_stock: int = 5,
    ) -> dict:
        expected_demand_during_lead_time = predicted_demand * lead_time_days
        reorder_point = expected_demand_during_lead_time + safety_stock

        stock_gap = reorder_point - current_stock

        if stock_gap > 0:
            recommended_order_quantity = round(stock_gap)
            decision = f"Reorder {recommended_order_quantity} units"
        else:
            recommended_order_quantity = 0
            decision = "No reorder required"

        if current_stock < predicted_demand:
            stockout_risk = "high"
        elif current_stock < reorder_point:
            stockout_risk = "medium"
        else:
            stockout_risk = "low"

        if current_stock > predicted_demand * 5:
            overstock_risk = "high"
        elif current_stock > predicted_demand * 3:
            overstock_risk = "medium"
        else:
            overstock_risk = "low"

        return {
            "agent": "InventoryOptimizationAgent",
            "current_stock": current_stock,
            "lead_time_days": lead_time_days,
            "safety_stock": safety_stock,
            "reorder_point": round(reorder_point, 2),
            "recommended_order_quantity": recommended_order_quantity,
            "stockout_risk": stockout_risk,
            "overstock_risk": overstock_risk,
            "decision": decision,
        }
