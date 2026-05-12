# Intelligent Demand Forecasting and Agent-Based Decision System

## Production-Oriented Machine Learning and MLOps Platform

---

# Project Vision

This project is designed as a production-oriented Machine Learning and MLOps platform rather than a simple research notebook. The objective is to demonstrate the ability to design, build, evaluate, automate, deploy, monitor, and scale a real-world machine learning system using modern ML engineering practices.

The platform focuses on:

* multi-series retail demand forecasting
* intelligent business decision support
* automated ML workflows
* experiment tracking and reproducibility
* deployment-ready APIs
* containerized infrastructure
* cloud-ready architecture
* agent-based AI systems

---

# Key Features

## Machine Learning

* Multi-series retail demand forecasting
* Baseline forecasting model
* Advanced LightGBM forecasting model
* Time-series feature engineering
* Forecast evaluation using multiple metrics
* Feature importance analysis
* Prediction error analysis

## MLOps

* Automated ML pipeline
* MLflow experiment tracking
* Model artifact management
* Reproducible workflows
* Automated testing and quality checks

## Deployment & Engineering

* FastAPI production inference API
* Docker containerization
* CI/CD-ready architecture
* Modular scalable codebase

## Intelligent Systems

* Agent-based decision system architecture
* Forecast explanation workflows
* Inventory recommendation system

---

# System Architecture

```text
Raw Retail Data
        ↓
Feature Engineering
        ↓
LightGBM Forecasting
        ↓
Evaluation Metrics
        ↓
MLflow Experiment Tracking
        ↓
Automated Training Pipeline
        ↓
FastAPI Inference API
        ↓
Docker Containerization
        ↓
Cloud Deployment
        ↓
Agent-Based Decision System
```

---

# Dataset

## Dataset Structure

| Column | Description |
|--------|-------------|
| date | transaction date |
| store_id | store identifier |
| item_id | item identifier |
| sales | target variable |
| price | product price |
| promo | promotion flag |

---

# Forecasting Signals Modeled

The forecasting system captures:

* temporal trends
* weekly seasonality
* monthly seasonality
* lag dependencies
* rolling demand behavior
* promotion effects
* price-demand relationships
* store-item demand patterns

---

# Feature Engineering

## Time Features

* weekday
* month
* year

## Lag Features

* lag_1
* lag_7
* lag_30

## Rolling Statistics

* rolling_mean_7
* rolling_std_7

## Business Features

* promotion indicators
* pricing information
* aggregate demand statistics

---

# Forecasting Models

## Baseline Forecasting Model

A lag-based baseline forecasting model was implemented to establish a minimum performance benchmark.

### Baseline Strategy

```text
Tomorrow's sales ≈ sales from 7 days ago
```

---

## Advanced LightGBM Forecasting Model

The primary forecasting model uses LightGBM.

### Why LightGBM?

LightGBM is widely used in industry because it:

* performs strongly on tabular forecasting data
* trains efficiently on large datasets
* supports scalable workflows
* provides feature importance analysis
* handles non-linear relationships effectively

### Model Configuration

```yaml
model:
  type: lightgbm
  n_estimators: 500
  learning_rate: 0.05
  num_leaves: 64
  random_state: 42
```

---

# Model Evaluation

## Implemented Metrics

| Metric | Description |
|--------|-------------|
| MAE | Mean Absolute Error |
| RMSE | Root Mean Squared Error |
| MAPE | Mean Absolute Percentage Error |
| WAPE | Weighted Absolute Percentage Error |

---

# Error Analysis

The project includes automated prediction error analysis.

## Implemented Analysis

* prediction error distribution
* worst-performing store-item pairs
* summary error statistics
* large-error diagnostics

---

# Automated ML Pipeline

The project includes an automated ML pipeline.

## Automated Workflow

```text
1. Data loading
2. Feature engineering
3. Baseline training
4. LightGBM training
5. Evaluation
6. Error analysis
7. Artifact generation
8. MLflow tracking
```

## Run Training Pipeline

```bash
PYTHONPATH=. python src/pipeline/run_training_pipeline.py
```

---

# FastAPI Inference Service

The project includes a production-oriented FastAPI inference API.

## API Features

* structured request validation
* forecasting inference
* business recommendations
* model metadata
* health monitoring endpoint
* interactive Swagger documentation

---

# Running the API with Docker

## 1. Build Docker Image

```bash
docker build -t intelligent-demand-api .
```

---

## 2. Run Docker Container

```bash
docker run -p 8000:8000 intelligent-demand-api
```

Expected output:

```text
INFO:     Started server process
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

---

## 3. Open API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

# Available API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|----------|
| `/` | GET | API status |
| `/health` | GET | Health monitoring |
| `/predict` | POST | Demand forecasting |

---

# Example Prediction Request

```json
{
  "store_id": "store_1",
  "item_id": "item_1",
  "price": 20.5,
  "promo": 1,
  "date": "2023-04-15"
}
```

---

# Example Prediction Response

```json
{
  "store_id": "store_1",
  "item_id": "item_1",
  "forecast_date": "2023-04-15",
  "predicted_demand": 13.24,
  "recommendation": "Maintain current stock level",
  "confidence_level": "high",
  "anomaly_warning": "No anomaly detected",
  "forecast_summary": "Expected demand for item_1 at store_1 on 2023-04-15 is 13.24. Recommended action: Maintain current stock level.",
  "model_name": "LightGBM Demand Forecasting Model",
  "model_version": "1.0.0"
}
```

---

# MLflow Experiment Tracking

The system integrates MLflow for experiment management.

## Tracked Components

* model parameters
* training runs
* evaluation metrics
* feature importance artifacts
* trained model artifacts

## MLflow Features Used

* experiment tracking
* metrics logging
* artifact logging
* reproducibility workflows
* model lifecycle management

## Launch MLflow UI

```bash
mlflow ui
```

Open:

```text
http://127.0.0.1:5000
```

---

# Testing & Software Quality

The project includes professional software quality workflows.

## Implemented Quality Controls

* API endpoint testing
* feature engineering testing
* configuration testing
* automated pytest workflows
* Black code formatting
* Ruff static analysis

## Run Tests

```bash
PYTHONPATH=. pytest
```

## Run Formatting

```bash
black src tests
```

## Run Static Analysis

```bash
ruff check src tests
```

---

# Dockerization

The project is fully containerized using Docker.

## Dockerized Components

* FastAPI service
* LightGBM inference model
* Python environment
* dependencies and runtime libraries

---

# Project Structure

```text
intelligent-demand-agent/
│
├── config/
├── models/
├── reports/
├── src/
│   ├── api/
│   ├── evaluation/
│   ├── features/
│   ├── models/
│   └── pipeline/
├── tests/
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# Technologies Used

## Machine Learning

* Python
* Pandas
* NumPy
* scikit-learn
* LightGBM
* XGBoost

## MLOps & Engineering

* MLflow
* FastAPI
* Docker
* Pytest
* Ruff
* Black
* GitHub

## Cloud & Infrastructure

* AWS deployment planning
* Containerized ML systems
* Cloud-ready architecture

---

# Future Improvements

* Transformer forecasting models
* advanced anomaly detection
* monitoring dashboards
* LangChain/LangGraph orchestration
* LLM-powered forecast explanations
* Kubernetes deployment

---

# Author

## Hoda Yamani

ML Engineer | Reinforcement Learning & Applied AI | Forecasting & Intelligent Systems

---

# License

This project is intended for educational, research, and portfolio purposes.
