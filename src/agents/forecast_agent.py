from src.api.predict import predict_demand


class ForecastAgent:
    """Agent responsible for generating demand forecasts."""

    def run(self, request_data: dict) -> dict:
        prediction = predict_demand(request_data)
        prediction_rounded = round(float(prediction), 2)

        return {
            "predicted_demand": prediction_rounded,
            "agent_name": "ForecastAgent",
            "agent_status": "success",
        }
