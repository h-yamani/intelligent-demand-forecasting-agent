from pydantic import BaseModel


class PredictionRequest(BaseModel):
    store_id: str
    item_id: str
    price: float
    promo: int
    date: str


class ForecastOutput(BaseModel):
    store_id: str
    item_id: str
    forecast_date: str
    predicted_demand: float


class DecisionOutput(BaseModel):
    recommendation: str
    confidence_level: str


class AnalysisOutput(BaseModel):
    trend: str
    trend_reason: str
    anomaly_warning: str
    anomaly_severity: str


class InventoryOptimizationOutput(BaseModel):
    current_stock: int
    lead_time_days: int
    safety_stock: int
    reorder_point: float
    recommended_order_quantity: int
    stockout_risk: str
    overstock_risk: str
    decision: str


class ExplanationOutput(BaseModel):
    mode: str
    executive_summary: str
    reasoning_steps: list[str]
    risk_assessment: str
    next_best_actions: list[str]


class SystemOutput(BaseModel):
    model_name: str
    model_version: str
    workflow: str


class PredictionResponse(BaseModel):
    forecast: ForecastOutput
    decision: DecisionOutput
    analysis: AnalysisOutput
    inventory_optimization: InventoryOptimizationOutput
    explanation: ExplanationOutput
    system: SystemOutput
