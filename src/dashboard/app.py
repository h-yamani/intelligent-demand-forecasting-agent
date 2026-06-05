import requests
import streamlit as st

API_URL = "http://127.0.0.1:8002/predict"

st.set_page_config(
    page_title="Agentic Demand Forecasting Dashboard",
    layout="wide",
)

st.title("Agentic Demand Forecasting Dashboard")
st.caption(
    "Business-facing dashboard for forecast, anomaly detection, "
    "inventory optimization, and agent reasoning."
)

st.sidebar.header("Forecast Input")

store_id = st.sidebar.text_input("Store ID", "STORE_001")
item_id = st.sidebar.text_input("Item ID", "ITEM_001")
price = st.sidebar.number_input("Price", value=9.99)
promo = st.sidebar.selectbox("Promotion Active", [0, 1], index=1)
date = st.sidebar.date_input("Forecast Date")

payload = {
    "store_id": store_id,
    "item_id": item_id,
    "price": price,
    "promo": promo,
    "date": str(date),
}

if st.sidebar.button("Generate Forecast"):
    try:
        response = requests.post(API_URL, json=payload, timeout=10)
        response.raise_for_status()
        result = response.json()

        forecast = result["forecast"]
        decision = result["decision"]
        analysis = result["analysis"]
        optimization = result["inventory_optimization"]
        explanation = result["explanation"]
        system = result["system"]

        st.subheader("Executive Summary")
        st.info(explanation["executive_summary"])

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Predicted Demand", forecast["predicted_demand"])
        col2.metric("Recommendation", decision["recommendation"])
        col3.metric("Stockout Risk", optimization["stockout_risk"])
        col4.metric("Order Quantity", optimization["recommended_order_quantity"])
        chart_data = {
            "Metric": ["Predicted Demand", "Current Stock", "Reorder Point"],
            "Value": [
                forecast["predicted_demand"],
                optimization["current_stock"],
                optimization["reorder_point"],
            ],
        }

        st.subheader("Forecast vs Inventory Position")
        st.bar_chart(chart_data, x="Metric", y="Value")

        st.divider()

        left, right = st.columns(2)

        with left:
            st.subheader("Forecast & Analysis")
            st.write(f"**Store:** {forecast['store_id']}")
            st.write(f"**Item:** {forecast['item_id']}")
            st.write(f"**Date:** {forecast['forecast_date']}")
            st.write(f"**Trend:** {analysis['trend']}")
            st.write(f"**Trend reason:** {analysis['trend_reason']}")
            st.write(f"**Anomaly:** {analysis['anomaly_warning']}")
            st.write(f"**Anomaly severity:** {analysis['anomaly_severity']}")

        with right:
            st.subheader("Inventory Optimization")
            st.write(f"**Current stock:** {optimization['current_stock']}")
            st.write(f"**Lead time days:** {optimization['lead_time_days']}")
            st.write(f"**Safety stock:** {optimization['safety_stock']}")
            st.write(f"**Reorder point:** {optimization['reorder_point']}")
            st.write(
                f"**Recommended order quantity:** {optimization['recommended_order_quantity']}"
            )
            st.write(f"**Overstock risk:** {optimization['overstock_risk']}")
            st.write(f"**Decision:** {optimization['decision']}")

        st.divider()

        st.subheader("Agent Reasoning")
        st.subheader("Agent Workflow")

        st.markdown("""
            Forecast Agent
                  ➜ Trend Analysis Agent
                  ➜ Anomaly Detection Agent
                  ➜ Inventory Optimization Agent
                  ➜ LLM Reasoning Agent
            """)
        for step in explanation["reasoning_steps"]:
            st.write(f"- {step}")

        st.subheader("Risk Assessment")

        risk_col1, risk_col2 = st.columns(2)

        with risk_col1:
            if optimization["stockout_risk"] == "high":
                st.error("Stockout risk: high")
            elif optimization["stockout_risk"] == "medium":
                st.warning("Stockout risk: medium")
            else:
                st.success("Stockout risk: low")

        with risk_col2:
            if optimization["overstock_risk"] == "high":
                st.error("Overstock risk: high")
            elif optimization["overstock_risk"] == "medium":
                st.warning("Overstock risk: medium")
            else:
                st.success("Overstock risk: low")

        st.info(explanation["risk_assessment"])

        st.subheader("Next Best Actions")
        for action in explanation["next_best_actions"]:
            st.write(f"- {action}")

        with st.expander("System Details"):
            st.json(system)

        with st.expander("Raw API Response"):
            st.json(result)

    except requests.exceptions.RequestException as exc:
        st.error(
            "Could not connect to the agentic API. "
            "Make sure it is running on http://127.0.0.1:8002."
        )
        st.exception(exc)
