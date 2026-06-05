# Intelligent Demand Forecasting & Agent-Based Decision Platform

## Production-Grade Machine Learning, MLOps, Agentic AI, and Cloud Deployment System

---

## Overview

The Intelligent Demand Forecasting & Agent-Based Decision Platform is an end-to-end Machine Learning Engineering and AI Engineering project designed to demonstrate production-oriented forecasting, MLOps, cloud deployment, agentic AI workflows, and business decision support.

Unlike traditional forecasting projects that focus solely on model training, this platform covers the complete machine learning lifecycle:

* Data Engineering
* Feature Engineering
* Forecasting
* Model Evaluation
* Experiment Tracking
* MLOps Automation
* API Development
* Docker Containerization
* AWS Deployment
* Agent-Based Decision Systems
* LLM-Powered Business Reasoning
* Interactive Business Dashboards

The system forecasts retail demand and transforms predictions into actionable inventory decisions through a multi-agent decision architecture.

---

## Key Highlights

### Machine Learning

* Multi-series retail demand forecasting
* LightGBM forecasting model
* Time-series feature engineering
* Forecast evaluation and diagnostics
* Feature importance analysis
* Error analysis workflows

### Agentic AI

* Forecast Agent
* Trend Analysis Agent
* Anomaly Detection Agent
* Inventory Optimization Agent
* LLM Reasoning Agent
* LangGraph orchestration workflow

### MLOps

* Automated training pipeline
* MLflow experiment tracking
* Model artifact management
* CI/CD workflows
* Automated testing and validation
* Monitoring and observability

### Cloud & Deployment

* FastAPI inference service
* Docker containerization
* AWS deployment workflows
* SageMaker-compatible inference
* Cloud-ready architecture

### Business Intelligence

* Interactive Streamlit dashboard
* Executive summaries
* Inventory recommendations
* Risk assessment
* Agent reasoning visualization

---

## End-to-End System Architecture

```text
Retail Sales Data
        ↓
Feature Engineering
        ↓
LightGBM Forecasting Model
        ↓
Model Evaluation
        ↓
MLflow Experiment Tracking
        ↓
Automated Training Pipeline
        ↓
FastAPI Inference Service
        ↓
Docker Containerization
        ↓
AWS / SageMaker Deployment
        ↓
LangGraph Agent System
        ↓
Inventory Optimization
        ↓
LLM Business Reasoning
        ↓
Streamlit Executive Dashboard
```

---

## Agent-Based Decision Architecture

The platform extends traditional forecasting systems with a multi-agent decision layer.

### Forecast Agent

Responsibilities:

* Generate demand forecasts
* Produce model predictions
* Supply forecasting outputs to downstream agents

### Trend Analysis Agent

Responsibilities:

* Identify demand trends
* Explain forecast behavior
* Detect demand shifts

### Anomaly Detection Agent

Responsibilities:

* Detect unusual forecast patterns
* Identify operational anomalies
* Assess anomaly severity

### Inventory Optimization Agent

Responsibilities:

* Calculate reorder points
* Calculate safety stock
* Estimate stockout risk
* Estimate overstock risk
* Recommend order quantities

### LLM Reasoning Agent

Responsibilities:

* Generate executive summaries
* Explain agent decisions
* Produce business-oriented recommendations
* Translate model outputs into actionable insights

### Agent Workflow

```text
Forecast Agent
        ↓
Trend Analysis Agent
        ↓
Anomaly Detection Agent
        ↓
Inventory Optimization Agent
        ↓
LLM Reasoning Agent
```

---

## Executive Dashboard

The project includes a business-facing Streamlit dashboard.

### Dashboard Features

* Demand forecasting visualization
* Trend analysis visualization
* Anomaly monitoring
* Inventory optimization recommendations
* Risk assessment indicators
* Agent workflow visualization
* Executive summaries
* Decision explanations

### Launch Dashboard

```bash
streamlit run src/dashboard/app.py
```

Dashboard URL:

```text
http://localhost:8501
```

---

## FastAPI Inference Service

The project provides a production-oriented inference API.

### API Features

* Request validation
* Forecast generation
* Inventory recommendations
* Agent-based reasoning
* Health monitoring
* Interactive Swagger documentation

### Launch API

```bash
PYTHONPATH=. uvicorn src.api.agentic_main_llm:app --host 0.0.0.0 --port 8002
```

### API Documentation

```text
http://127.0.0.1:8002/docs
```

---

## Example Prediction Request

```json
{
  "store_id": "STORE_001",
  "item_id": "ITEM_001",
  "price": 9.99,
  "promo": 1,
  "date": "2026-06-02"
}
```

---

## Example Prediction Response

```json
{
  "forecast": {
    "store_id": "STORE_001",
    "item_id": "ITEM_001",
    "forecast_date": "2026-06-02",
    "predicted_demand": 15.45
  },
  "decision": {
    "recommendation": "Maintain current stock level",
    "confidence_level": "high"
  },
  "analysis": {
    "trend": "stable",
    "anomaly_warning": "No anomaly detected"
  },
  "inventory_optimization": {
    "recommended_order_quantity": 31,
    "stockout_risk": "medium",
    "overstock_risk": "low"
  }
}
```

---

## Machine Learning Pipeline

### Feature Engineering

Time-based Features

* weekday
* month
* year

Lag Features

* lag_1
* lag_7
* lag_30

Rolling Statistics

* rolling_mean_7
* rolling_std_7

Business Features

* promotions
* pricing information
* demand aggregates

### Forecasting Model

Primary model:

* LightGBM

Evaluation metrics:

* MAE
* RMSE
* MAPE
* WAPE

---

## MLOps & Experiment Tracking

### MLflow Integration

Tracked components:

* parameters
* metrics
* model artifacts
* feature importance
* experiment runs

Launch MLflow:

```bash
mlflow ui
```

Open:

```text
http://127.0.0.1:5000
```

---

## AWS & SageMaker Deployment

### Cloud Components

* Amazon EC2
* Amazon S3
* Amazon SageMaker
* Docker Containers

### Deployment Capabilities

* containerized inference
* cloud-ready deployment
* scalable serving
* reproducible model packaging

---

## Monitoring & Observability

Implemented monitoring capabilities include:

* API request logging
* prediction logging
* health monitoring
* operational diagnostics
* monitoring documentation

---

## Software Quality & Testing

### Quality Controls

* Pytest
* Ruff
* Black
* GitHub Actions
* CI/CD validation

Run tests:

```bash
PYTHONPATH=. pytest
```

Run static analysis:

```bash
ruff check src tests
```

Run formatting:

```bash
black src tests
```

---

## Repository Structure

```text
intelligent-demand-agent/
│
├── config/
├── docs/
│   ├── aws/
│   ├── monitoring/
│   └── dashboard.md
│
├── models/
├── reports/
├── sagemaker/
├── src/
│   ├── agents/
│   ├── api/
│   ├── dashboard/
│   ├── evaluation/
│   ├── features/
│   ├── models/
│   └── pipeline/
│
├── tests/
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Technology Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-Learn
* LightGBM

### Agentic AI

* LangGraph
* LangChain

### APIs

* FastAPI
* Pydantic

### MLOps

* MLflow
* GitHub Actions
* Docker
* Pytest
* Ruff
* Black

### Cloud

* AWS
* SageMaker
* EC2
* S3

### Dashboard

* Streamlit

---

## Documentation

| Document                    | Description                  |
| --------------------------- | ---------------------------- |
| docs/dashboard.md           | Dashboard documentation      |
| docs/aws/                   | AWS deployment documentation |
| docs/monitoring/            | Monitoring documentation     |
| reports/technical_report.md | Technical report             |

---

## Project Status

Current Version: v1.0

Completed:

* Demand forecasting
* Agent-based decision system
* Inventory optimization
* Dashboard visualization
* FastAPI deployment
* Docker containerization
* AWS deployment workflows
* SageMaker integration
* Monitoring
* CI/CD automation

---

## Author

### Hoda Yamani

AI & Machine Learning Engineer | Reinforcement Learning Researcher



