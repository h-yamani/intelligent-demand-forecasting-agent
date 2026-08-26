# Intelligent Demand Forecasting & Decision Intelligence Platform

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-009688.svg)](https://fastapi.tiangolo.com/)
[![LightGBM](https://img.shields.io/badge/LightGBM-Forecasting-green.svg)](https://lightgbm.readthedocs.io/)
[![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-0194E2.svg)](https://mlflow.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-Cloud%20Deployment-FF9900.svg)](https://aws.amazon.com/)
[![CI/CD](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF.svg)](https://github.com/features/actions)

An end-to-end **machine learning and decision-intelligence platform** for retail demand forecasting, inventory optimisation, agent-based reasoning, and cloud deployment.

The project demonstrates how a forecasting model can be developed into a broader production-oriented ML system: from feature engineering and experiment tracking to API serving, containerisation, cloud infrastructure, automated testing, and business-facing decision support.

---

## Overview

Most forecasting projects stop after model training and evaluation.

This project goes further by connecting the forecasting model to a complete engineering workflow:

```text
Retail Data
    ↓
Feature Engineering
    ↓
Demand Forecasting
    ↓
Model Evaluation
    ↓
MLflow Experiment Tracking
    ↓
FastAPI Inference
    ↓
Agent-Based Decision Layer
    ↓
Inventory Optimisation
    ↓
Business Reasoning
    ↓
Streamlit Dashboard
    ↓
Docker / AWS Deployment
```

The central objective is not only to answer:

> **How much demand should we expect?**

but also:

> **What should the business do about it?**

Forecasts are therefore passed through specialised agents that analyse trends, detect anomalies, evaluate inventory risk, and produce actionable recommendations.

---

# System Capabilities

| Area | Capabilities |
|---|---|
| **Machine Learning** | Multi-series forecasting, LightGBM, lag features, rolling statistics, calendar features, evaluation and diagnostics |
| **Decision Intelligence** | Forecast interpretation, inventory recommendations, stockout/overstock assessment |
| **Agentic AI** | LangGraph orchestration, specialised analysis agents, LLM-assisted business reasoning |
| **MLOps** | MLflow experiment tracking, reproducible training, model artifacts, automated testing |
| **API Engineering** | FastAPI inference services, validation, health endpoints, structured logging |
| **Cloud Engineering** | Docker, Amazon EC2, Amazon S3, Amazon ECR, Amazon SageMaker-compatible serving |
| **Software Quality** | Pytest, Ruff, Black, GitHub Actions CI/CD |
| **Business Interface** | Interactive Streamlit decision dashboard |

---

# Machine Learning

## Forecasting Problem

The forecasting system predicts future demand for a specific:

- store
- product
- date
- price
- promotion configuration

A single global forecasting model is trained across multiple store-product time series.

---

## Model

The primary production candidate is:

**LightGBM Regressor**

The model is designed to capture nonlinear interactions between historical sales, pricing, promotions, seasonality, store characteristics, and product characteristics.

---

## Feature Engineering

The forecasting pipeline includes more than simple calendar variables.

### Historical Demand

```text
sales_lag_1
sales_lag_7
sales_lag_14
sales_lag_30
```

### Rolling Statistics

```text
rolling_mean_7
rolling_std_7
rolling_mean_14
rolling_std_14
rolling_mean_30
rolling_std_30
expanding_mean
```

### Calendar Features

```text
weekday
month
dayofweek
weekofyear
is_weekend
sin_day
cos_day
sin_month
cos_month
```

### Pricing and Promotion Features

```text
price
price_lag_1
price_change
price_rolling_mean_7

promo
promo_lag_1
promo_rolling_7
```

### Store and Product Context

```text
store_avg_sales
item_avg_sales
```

---

## Model Performance

The LightGBM model substantially improves over the baseline forecasting model.

| Model | MAE | RMSE | WAPE |
|---|---:|---:|---:|
| Baseline | 5.459 | 8.098 | 17.924% |
| **LightGBM** | **2.518** | **3.156** | **8.269%** |

This corresponds to a substantial reduction in forecasting error and supports the selection of LightGBM as the production deployment candidate.

---

# Agent-Based Decision Architecture

Forecasting is only the first stage of the system.

The platform introduces a specialised multi-agent decision layer that converts predictions into operational recommendations.

```text
                    ┌──────────────────┐
                    │  Forecast Agent  │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │  Trend Analysis  │
                    │      Agent       │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Anomaly Detection│
                    │      Agent       │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │    Inventory     │
                    │ Optimisation Agent│
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │  LLM Reasoning   │
                    │      Agent       │
                    └────────┬─────────┘
                             ↓
                    Business Decision
```

LangGraph coordinates the workflow and manages the flow of information between agents.

---

## Forecast Agent

Responsible for:

- generating demand forecasts
- calling the forecasting model
- preparing forecast information for downstream agents

---

## Trend Analysis Agent

Responsible for:

- identifying demand direction
- analysing forecast behaviour
- highlighting meaningful demand shifts

---

## Anomaly Detection Agent

Responsible for:

- detecting unusual predictions
- identifying operational anomalies
- communicating potential forecasting risks

---

## Inventory Optimisation Agent

Transforms forecast outputs into inventory decisions.

Responsibilities include:

- estimating reorder requirements
- calculating recommended order quantities
- assessing stockout risk
- assessing overstock risk
- supporting safety-stock decisions

---

## LLM Reasoning Agent

Provides a business-facing interpretation layer.

Responsibilities include:

- summarising agent outputs
- explaining recommendations
- translating model results into operational language
- generating executive-level decision summaries

The LLM is used as a **reasoning and communication layer**, while numerical forecasts continue to come from the trained forecasting model.

---

# FastAPI Inference Service

The system exposes forecasting and decision functionality through FastAPI.

## Key Features

- structured request validation
- forecasting inference
- multi-agent decision execution
- inventory recommendations
- health monitoring
- structured operational logging
- automatically generated OpenAPI documentation

### Start the Agentic API

```bash
PYTHONPATH=. uvicorn src.api.agentic_main_llm:app \
  --host 0.0.0.0 \
  --port 8002
```

API documentation:

```text
http://127.0.0.1:8002/docs
```

---

# Example Request

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

# Example Response

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

# Executive Dashboard

A Streamlit dashboard provides a business-facing interface over the forecasting and decision system.

The dashboard communicates both predictions and the reasoning surrounding them.

## Dashboard Capabilities

- demand forecast visualisation
- trend analysis
- anomaly indicators
- inventory recommendations
- stockout and overstock risk
- agent execution summaries
- business-oriented explanations
- executive decision support

### Start the Dashboard

```bash
streamlit run src/dashboard/app.py
```

Then open:

```text
http://localhost:8501
```

---

# MLOps

## MLflow Experiment Tracking

MLflow is used during model development to track experiments and support reproducibility.

Tracked information includes:

- model parameters
- evaluation metrics
- experiment runs
- model artifacts
- feature information
- model comparisons

Start MLflow locally:

```bash
mlflow ui
```

Then open:

```text
http://127.0.0.1:5000
```

---

# AWS Deployment Architecture

The project is designed around separation between the application layer and the managed model-serving layer.

```text
User / Streamlit Dashboard
            ↓
          HTTPS
            ↓
       FastAPI on EC2
            ↓
          boto3
            ↓
 Amazon SageMaker Endpoint
            ↓
       LightGBM Model
```

Supporting AWS services include:

```text
Amazon S3
├── model artifacts
├── deployment artifacts
└── monitoring outputs

Amazon ECR
└── SageMaker inference container

Amazon SageMaker
└── managed model serving

Amazon CloudWatch
├── application logs
├── endpoint metrics
└── operational monitoring
```

---

# SageMaker Inference Container

A dedicated SageMaker-compatible inference service is included under:

```text
sagemaker/
```

The container implements the standard SageMaker inference contract:

```text
GET  /ping
POST /invocations
```

The inference image:

- loads the packaged LightGBM model
- loads the model feature schema
- validates incoming feature vectors
- preserves feature ordering
- performs inference
- returns structured JSON predictions
- exposes health checks
- writes inference logs

The container has been validated locally using Docker and is designed for deployment through Amazon SageMaker.

---

# Model Packaging

The deployment bundle contains the model and supporting inference metadata:

```text
model.tar.gz
├── lgbm_model.pkl
└── feature_list.json
```

The package is stored in Amazon S3 for managed SageMaker deployment.

The inference Docker image is stored in Amazon ECR.

---

# Monitoring & Observability

Operational monitoring is designed across several layers.

### Application Monitoring

- API request logging
- prediction logging
- exception logging
- request latency
- health endpoints

### Model Monitoring

- prediction diagnostics
- abnormal prediction warnings
- future prediction-vs-actual comparison
- drift-monitoring architecture

### AWS Monitoring

Planned deployment monitoring includes:

- SageMaker invocation metrics
- model latency
- endpoint errors
- CloudWatch logs
- custom drift metrics

---

# CI/CD & Software Quality

GitHub Actions provides automated validation for code changes.

The CI pipeline performs:

```text
Code Change
    ↓
Install Dependencies
    ↓
Run Pytest
    ↓
Run Ruff
    ↓
Run Black Check
    ↓
Build Docker Image
    ↓
Validate Project Structure
```

Quality tooling:

- **Pytest** — automated testing
- **Ruff** — static analysis and linting
- **Black** — deterministic formatting
- **GitHub Actions** — CI/CD automation
- **Docker** — deployment validation

Run locally:

```bash
PYTHONPATH=. pytest
```

```bash
ruff check src tests
```

```bash
black --check src tests
```

---

# Repository Structure

```text
intelligent-demand-forecasting-agent/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── config/
│   └── config.yaml
│
├── docs/
│   ├── aws/
│   ├── monitoring/
│   └── dashboard.md
│
├── models/
│   ├── lgbm_model.pkl
│   └── feature_list.json
│
├── reports/
│
├── sagemaker/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── inference/
│   │   ├── app.py
│   │   └── serve.py
│   └── model_artifacts/
│
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
│
├── Dockerfile
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

# Technology Stack

| Layer | Technologies |
|---|---|
| **Programming & Data** | Python, Pandas, NumPy |
| **Machine Learning** | LightGBM, Scikit-learn |
| **Agentic AI** | LangGraph, LangChain |
| **API** | FastAPI, Pydantic |
| **Experiment Tracking** | MLflow |
| **Testing & Quality** | Pytest, Ruff, Black |
| **Containerisation** | Docker |
| **CI/CD** | GitHub Actions |
| **Cloud** | AWS EC2, S3, ECR, SageMaker |
| **Dashboard** | Streamlit |

---

# Quick Start

## 1. Clone the Repository

```bash
git clone https://github.com/h-yamani/intelligent-demand-forecasting-agent.git
cd intelligent-demand-forecasting-agent
```

## 2. Create an Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run Tests

```bash
PYTHONPATH=. pytest
```

## 5. Start the API

```bash
PYTHONPATH=. uvicorn src.api.agentic_main_llm:app \
  --host 0.0.0.0 \
  --port 8002
```

## 6. Start the Dashboard

In another terminal:

```bash
streamlit run src/dashboard/app.py
```

---

# Engineering Focus

This project was developed to demonstrate the integration of several areas that are often presented separately:

**Machine Learning Engineering**
- forecasting
- feature engineering
- model evaluation
- production inference

**MLOps**
- experiment tracking
- reproducible artifacts
- automated validation
- containerisation
- CI/CD

**AI Engineering**
- agent orchestration
- LLM-assisted reasoning
- decision workflows
- human-readable explanations

**Cloud Engineering**
- AWS infrastructure
- model artifacts in S3
- container images in ECR
- SageMaker-compatible model serving

**Business Decision Intelligence**
- inventory optimisation
- risk assessment
- executive summaries
- operational recommendations

---

# Project Status

### Implemented

- [x] Retail demand forecasting pipeline
- [x] LightGBM forecasting model
- [x] Feature engineering pipeline
- [x] Model evaluation and diagnostics
- [x] MLflow experiment tracking
- [x] FastAPI inference services
- [x] Agent-based decision architecture
- [x] Inventory optimisation
- [x] Streamlit executive dashboard
- [x] Docker containerisation
- [x] Automated testing
- [x] Ruff and Black validation
- [x] GitHub Actions CI/CD
- [x] SageMaker-compatible inference container
- [x] Versioned model artifact packaging
- [x] Model artifact storage in Amazon S3
- [x] Inference container storage in Amazon ECR

### Cloud Deployment in Progress

- [ ] SageMaker managed model resource
- [ ] SageMaker managed endpoint
- [ ] FastAPI → SageMaker runtime integration
- [ ] CloudWatch endpoint monitoring
- [ ] Prediction and drift monitoring

---

# Documentation

Additional engineering documentation is available under:

```text
docs/
├── aws/
├── monitoring/
└── dashboard.md
```

Technical reports and evaluation outputs are stored under:

```text
reports/
```

---

# Author

## Hoda Yamani

**Machine Learning Engineer | AI Engineer | Reinforcement Learning Researcher**

Research and engineering interests include:

- machine learning systems
- predictive modelling
- reinforcement learning
- agentic AI
- robotics
- MLOps
- applied AI systems

GitHub: [h-yamani](https://github.com/h-yamani)

---

## License

This repository is intended for research, engineering demonstration, and portfolio use.
