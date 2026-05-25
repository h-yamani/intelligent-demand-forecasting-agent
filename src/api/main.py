import logging
import time
from pathlib import Path

from fastapi import FastAPI, Request

from src.api.predict import predict_demand
from src.api.schemas import PredictionRequest, PredictionResponse

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "api.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

app = FastAPI(title="Intelligent Demand Forecasting API", version="1.0.0")


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = round(time.time() - start_time, 4)

    logging.info(
        "method=%s path=%s status_code=%s latency_seconds=%s",
        request.method,
        request.url.path,
        response.status_code,
        process_time,
    )

    return response


@app.get("/")
def home():
    return {"message": "Demand Forecasting API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    request_data = request.model_dump()

    logging.info(
        "prediction_request store_id=%s item_id=%s date=%s price=%s promo=%s",
        request.store_id,
        request.item_id,
        request.date,
        request.price,
        request.promo,
    )

    prediction = predict_demand(request_data)
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

    logging.info(
        "prediction_response store_id=%s item_id=%s predicted_demand=%s "
        "recommendation=%s confidence_level=%s anomaly_warning=%s",
        request.store_id,
        request.item_id,
        prediction_rounded,
        recommendation,
        confidence_level,
        anomaly_warning,
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
        model_version="1.0.0",
    )
