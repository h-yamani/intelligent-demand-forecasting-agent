from pydantic import BaseModel


class PredictionRequest(BaseModel):
    store_id: str
    item_id: str
    price: float
    promo: int
    date: str


class PredictionResponse(BaseModel):
    store_id: str
    item_id: str
    forecast_date: str
    predicted_demand: float
    recommendation: str
    model_name: str
    model_version: str
