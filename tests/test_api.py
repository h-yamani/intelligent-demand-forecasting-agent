from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Demand Forecasting API is running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_predict():

    payload = {
        "store_id": "store_1",
        "item_id": "item_1",
        "price": 20.5,
        "promo": 1,
        "date": "2023-04-15",
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "predicted_demand" in data
    assert "recommendation" in data
    assert "model_name" in data
