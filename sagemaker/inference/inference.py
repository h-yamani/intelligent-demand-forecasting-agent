import json
import pickle
from pathlib import Path

import pandas as pd

MODEL_DIR = Path("/opt/ml/model")
MODEL_PATH = MODEL_DIR / "lgbm_model.pkl"
FEATURE_LIST_PATH = MODEL_DIR / "feature_list.json"


def model_fn(model_dir):
    model_path = Path(model_dir) / "lgbm_model.pkl"
    feature_list_path = Path(model_dir) / "feature_list.json"

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    with open(feature_list_path, "r", encoding="utf-8") as f:
        feature_list = json.load(f)

    return {
        "model": model,
        "feature_list": feature_list,
    }


def input_fn(request_body, request_content_type):
    if request_content_type != "application/json":
        raise ValueError(f"Unsupported content type: {request_content_type}")

    data = json.loads(request_body)

    if isinstance(data, dict):
        return pd.DataFrame([data])

    if isinstance(data, list):
        return pd.DataFrame(data)

    raise ValueError("Input must be a JSON object or a list of JSON objects.")


def predict_fn(input_data, model_artifacts):
    model = model_artifacts["model"]
    feature_list = model_artifacts["feature_list"]

    missing_features = [feature for feature in feature_list if feature not in input_data.columns]
    if missing_features:
        raise ValueError(f"Missing required features: {missing_features}")

    input_data = input_data[feature_list]
    predictions = model.predict(input_data)

    return {
        "predicted_demand": [float(value) for value in predictions]
    }


def output_fn(prediction, accept):
    if accept != "application/json":
        raise ValueError(f"Unsupported accept type: {accept}")

    return json.dumps(prediction), accept
