from fastapi import FastAPI

from src.api.schemas import (
    PredictionRequest,
    PredictionResponse,
)

from src.api.predict import predict_demand


app = FastAPI(
    title="Intelligent Demand Forecasting API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Demand Forecasting API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):

    prediction = predict_demand(request.dict())

    if prediction >= 35:
        recommendation = "Increase inventory"

    elif prediction <= 10:
        recommendation = "Reduce inventory"

    else:
        recommendation = "Maintain current stock level"

    return PredictionResponse(
        store_id=request.store_id,
        item_id=request.item_id,
        forecast_date=request.date,
        predicted_demand=round(prediction, 2),
        recommendation=recommendation,
        model_name="LightGBM Demand Forecasting Model",
        model_version="1.0.0"
    )
