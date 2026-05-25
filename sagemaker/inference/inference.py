import json
import joblib
import pandas as pd
from io import StringIO

MODEL_PATH = "/opt/ml/model/model.joblib"

model = joblib.load(MODEL_PATH)


def input_fn(request_body, request_content_type):
    if request_content_type == "application/json":
        data = json.loads(request_body)
        return pd.DataFrame([data])

    raise ValueError(f"Unsupported content type: {request_content_type}")


def predict_fn(input_data, model):
    prediction = model.predict(input_data)

    return {
        "predicted_demand": float(prediction[0])
    }


def output_fn(prediction, accept):
    if accept == "application/json":
        return json.dumps(prediction), accept

    raise ValueError(f"Unsupported accept type: {accept}")

