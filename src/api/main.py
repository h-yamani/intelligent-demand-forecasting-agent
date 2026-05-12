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

    prediction = predict_demand(request.model_dump())
    prediction_rounded = round(prediction, 2)

    if prediction_rounded >= 35:
        recommendation = "Increase inventory"
        confidence_level = "high"
        anomaly_warning = "Possible high-demand period"
    elif prediction_rounded <= 10:
        recommendation = "Reduce inventory"
        confidence_level = "medium"
        anomaly_warning = "Possible low-demand period"
    else:
        recommendation = "Maintain current stock level"
        confidence_level = "high"
        anomaly_warning = "No anomaly detected"

    forecast_summary = (
        f"Expected demand for {request.item_id} at {request.store_id} "
        f"on {request.date} is {prediction_rounded}. "
        f"Recommended action: {recommendation}."
    )

    return PredictionResponse(
        store_id=request.store_id,
        item_id=request.item_id,
        forecast_date=request.date,
        predicted_demand=prediction_rounded,
        recommendation=recommendation,
        confidence_level=confidence_level,
        anomaly_warning=anomaly_warning,
        forecast_summary=forecast_summary,
        model_name="LightGBM Demand Forecasting Model",
        model_version="1.0.0"
    )
