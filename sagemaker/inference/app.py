import os
import json
import logging
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, Response


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

MODEL_DIR = Path("/opt/ml/model")
MODEL_PATH = MODEL_DIR / "lgbm_model.pkl"
FEATURE_LIST_PATH = MODEL_DIR / "feature_list.json"

app = FastAPI(title="SageMaker Demand Forecasting Inference")


# Load model once when the container starts
try:
    model = joblib.load(MODEL_PATH)

    with open(FEATURE_LIST_PATH, "r", encoding="utf-8") as f:
        feature_list = json.load(f)

    logging.info("Model loaded successfully with %s features", len(feature_list))

except Exception:
    logging.exception("Failed to load model")
    model = None
    feature_list = None


@app.get("/ping")
def ping():
    """SageMaker health check."""
    if model is None or feature_list is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    return Response(status_code=200)


@app.post("/invocations")
async def invocations(request: Request):
    """SageMaker prediction endpoint."""

    if model is None or feature_list is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    if request.headers.get("content-type", "").split(";")[0] != "application/json":
        raise HTTPException(
            status_code=415,
            detail="Content-Type must be application/json",
        )

    try:
        payload = await request.json()

        if isinstance(payload, dict):
            rows = pd.DataFrame([payload])
        elif isinstance(payload, list):
            rows = pd.DataFrame(payload)
        else:
            raise ValueError("Input must be a JSON object or list of objects")

        missing = [
            feature
            for feature in feature_list
            if feature not in rows.columns
        ]

        if missing:
            raise ValueError(f"Missing required features: {missing}")

        rows = rows[feature_list]

        for col in ["store_id", "item_id"]:
            if col in rows.columns:
                rows[col] = rows[col].astype("category")

        predictions = model.predict(rows)

        result = {
            "predicted_demand": [
                float(value) for value in predictions
            ]
        }

        logging.info(
            "prediction_success rows=%s predictions=%s",
            len(rows),
            len(predictions),
        )

        return JSONResponse(content=result)

    except Exception as exc:
        logging.exception("prediction_failed")

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )
