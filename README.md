# Intelligent Demand Forecasting and Agent-Based Decision System

## Production-Oriented Machine Learning and MLOps Platform

---

# Project Vision

This project is designed as a production-oriented Machine Learning and MLOps system rather than a simple research notebook. The objective is to demonstrate the ability to design, build, evaluate, automate, deploy, and monitor a real-world machine learning application using modern ML engineering practices.

The platform focuses on:

* multi-series retail demand forecasting
* intelligent business decision support
* automated ML workflows
* experiment tracking and reproducibility
* deployment-ready APIs
* cloud-ready infrastructure
* agent-based AI systems

The project is intentionally structured to simulate the architecture and workflow of modern industrial ML systems.

---

# Project Objectives

Retail businesses require accurate forecasting systems to:

* reduce overstock and understock situations
* improve supply chain planning
* optimize pricing and promotions
* support inventory management
* improve operational efficiency
* enable data-driven business decisions

This project predicts future product demand across multiple stores and items using historical sales data, time-series feature engineering, machine learning forecasting models, and production-oriented engineering workflows.

---

# Key Features

## Machine Learning

* Multi-series retail demand forecasting
* Baseline forecasting model
* Advanced LightGBM forecasting model
* Time-series feature engineering
* Time-based train/validation/test splitting
* Forecast evaluation using multiple metrics
* Feature importance analysis
* Error analysis and diagnostics

## MLOps

* Automated ML pipeline
* MLflow experiment tracking
* Model artifact management
* Reproducible training workflows
* Config-driven training system
* Structured project architecture

## Deployment & Engineering

* FastAPI deployment-ready architecture
* Docker-ready structure
* AWS deployment planning
* CI/CD-ready workflow
* Modular and scalable codebase

## Intelligent Systems

* Agent-based decision system design
* Trend analysis workflows
* Forecast explanation workflows
* Business recommendation architecture

---

# System Architecture

```text
Raw Retail Data
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Baseline Forecasting
        ↓
LightGBM Forecasting
        ↓
Evaluation Metrics
        ↓
Error Analysis
        ↓
MLflow Experiment Tracking
        ↓
Automated Training Pipeline
        ↓
FastAPI Deployment
        ↓
Docker + AWS Deployment
        ↓
Agent-Based Decision System
```

---

# Dataset

## Dataset Structure

The dataset contains:

| Column   | Description      |
| -------- | ---------------- |
| date     | transaction date |
| store_id | store identifier |
| item_id  | item identifier  |
| sales    | target variable  |
| price    | product price    |
| promo    | promotion flag   |

## Forecasting Signals Modeled

The forecasting system captures:

* temporal trends
* weekly seasonality
* monthly seasonality
* lag dependencies
* rolling demand trends
* promotion effects
* price-demand relationships
* store-item demand behavior

---

# Exploratory Data Analysis (EDA)

The project includes extensive data exploration and visualization.

## Implemented Analysis

* global sales trends
* weekday seasonality
* monthly seasonality
* promotional impact
* price effects
* lag relationships
* rolling averages
* autocorrelation analysis
* demand distributions
* feature correlations

## Example Outputs

Generated visualizations include:

* sales trend plots
* seasonal decomposition plots
* promotion impact analysis
* rolling mean analysis
* lag comparison analysis
* correlation heatmaps
* feature importance plots
* error distribution analysis

---

# Feature Engineering

## Implemented Features

### Time Features

* weekday
* month
* year

### Lag Features

* lag_1
* lag_7
* lag_30

### Rolling Statistics

* rolling_mean_7
* rolling_std_7

### Business Features

* promotion indicators
* price information

## Why Feature Engineering Matters

Feature engineering transforms raw retail data into predictive signals that help forecasting models capture:

* recurring patterns
* seasonal demand
* short-term dependencies
* long-term trends
* business-driven fluctuations

---

# Forecasting Models

# 1. Baseline Forecasting Model

A lag-based baseline model was implemented to establish a minimum performance benchmark.

## Baseline Strategy

```text
Tomorrow's sales ≈ sales from 7 days ago
```

## Baseline Metrics

| Metric | Value  |
| ------ | ------ |
| MAE    | 5.46   |
| RMSE   | 8.10   |
| MAPE   | 21.24% |
| WAPE   | 17.92% |

---

# 2. Advanced LightGBM Forecasting Model

The primary forecasting model uses LightGBM.

## Why LightGBM?

LightGBM is widely used in industry because it:

* performs strongly on tabular data
* trains efficiently on large datasets
* supports scalable workflows
* provides feature importance analysis
* handles complex non-linear relationships

## Model Configuration

```yaml
model:
  type: lightgbm
  n_estimators: 500
  learning_rate: 0.05
  num_leaves: 64
  random_state: 42
```

## Time-Based Validation Strategy

The project uses chronological train/validation/test splits to simulate real-world deployment scenarios.

This prevents future information leakage and improves forecasting reliability.

---

# Model Evaluation

## Implemented Metrics

| Metric | Description                        |
| ------ | ---------------------------------- |
| MAE    | Mean Absolute Error                |
| RMSE   | Root Mean Squared Error            |
| MAPE   | Mean Absolute Percentage Error     |
| WAPE   | Weighted Absolute Percentage Error |

## Current LightGBM Results

| Metric | Value  |
| ------ | ------ |
| MAE    | 2.52   |
| RMSE   | 3.16   |
| MAPE   | 11.35% |
| WAPE   | 8.27%  |

## Key Observation

The LightGBM model significantly outperformed the baseline forecasting model across all evaluation metrics.

---

# Feature Importance Analysis

The system automatically generates feature importance analysis.

## Purpose

Feature importance helps:

* interpret model behavior
* identify dominant forecasting signals
* improve feature engineering
* support explainability
* understand demand drivers

## Example Outputs

* top feature rankings
* lag importance analysis
* seasonality feature contributions
* business feature contributions

---

# Error Analysis

The project includes automated prediction error analysis.

## Implemented Analysis

* prediction error distribution
* worst-performing store-item pairs
* summary error statistics
* large-error diagnostics

## Why Error Analysis Matters

Error analysis helps identify:

* unstable demand patterns
* weak forecasting regions
* problematic store-item combinations
* opportunities for future improvements

---

# Automated ML Pipeline

The project includes an automated shell-based ML pipeline.

## Automated Workflow

```text
1. Baseline training
2. LightGBM training
3. Evaluation
4. Error analysis
5. Artifact generation
6. MLflow tracking
```

## Example Pipeline Execution

```bash
./pipelines/run_pipeline.sh
```

## Why This Matters

Automation demonstrates:

* reproducibility
* scalable engineering workflows
* modular system design
* production-oriented ML engineering

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

# Project Structure

```text
intelligent-demand-agent/
│
├── api/
├── archive/
├── config/
│   └── config.yaml
├── data/
├── models/
├── notebooks/
├── pipelines/
│   └── run_pipeline.sh
├── reports/
│   ├── figures/
│   └── modeling/
├── src/
│   ├── evaluation/
│   ├── features/
│   └── models/
├── tests/
├── requirements.txt
└── README.md
```

---

# Technologies Used

## Programming & ML

* Python
* Pandas
* NumPy
* scikit-learn
* LightGBM
* Matplotlib

## MLOps & Automation

* MLflow
* Shell scripting
* Git
* GitHub

## Deployment & APIs

* FastAPI
* Uvicorn
* Docker (planned)

## Cloud & Infrastructure (planned)

* AWS S3
* AWS EC2
* AWS Lambda
* IAM
* CloudWatch

---

# Deployment Roadmap

## Current Status

### Completed

* EDA
* feature engineering
* baseline forecasting
* LightGBM forecasting
* evaluation metrics
* error analysis
* feature importance analysis
* MLflow experiment tracking
* automated ML pipeline

### In Progress

* FastAPI deployment

### Planned

* Docker containerization
* AWS deployment
* CI/CD integration
* monitoring system
* dashboard visualization
* multi-agent decision workflows

---

# Future Intelligent Agent System

The long-term goal is to extend forecasting into intelligent business decision support.

## Planned Agents

### Forecast Agent

Generates future demand predictions.

### Trend Agent

Analyzes demand increases and decreases.

### Anomaly Agent

Detects unusual demand behavior.

### Decision Agent

Provides business recommendations such as:

* increase inventory
* reduce inventory
* investigate anomalies
* maintain current strategy

---

# Future Cloud Architecture

## Planned AWS Workflow

```text
Client Request
      ↓
API Gateway
      ↓
FastAPI Service (EC2/Lambda)
      ↓
Load Trained Model
      ↓
Generate Prediction
      ↓
Return Forecast
```

## Planned AWS Components

| Service    | Purpose                    |
| ---------- | -------------------------- |
| S3         | model and artifact storage |
| EC2        | API hosting                |
| Lambda     | serverless inference       |
| IAM        | permission management      |
| CloudWatch | monitoring and logging     |

---

# CI/CD Roadmap

Planned GitHub Actions workflows:

* automated testing
* linting
* pipeline execution
* deployment validation
* artifact generation

---

# Why This Project Matters

This project demonstrates practical skills in:

## Machine Learning

* forecasting
* feature engineering
* model evaluation
* error analysis
* gradient boosting

## MLOps

* experiment tracking
* reproducibility
* artifact management
* automated pipelines
* scalable workflows

## Software Engineering

* modular architecture
* deployment-ready design
* automation pipelines
* configuration-driven systems

## Cloud & Deployment

* API deployment
* Docker readiness
* AWS architecture planning
* CI/CD planning

## Intelligent Systems

* agent-based workflows
* intelligent decision support
* explainable AI systems

---

# Interview Talking Points

Key topics this project demonstrates:

* end-to-end ML system development
* production-oriented forecasting workflows
* reproducible experimentation
* scalable ML engineering
* automation and deployment readiness
* practical MLOps understanding
* cloud-oriented architecture planning

Important concepts to explain during interviews:

* why time-based splits matter
* why baseline models are important
* differences between MAE/RMSE/MAPE/WAPE
* why LightGBM works well for tabular forecasting
* why MLflow matters in MLOps
* why automation pipelines improve reproducibility
* how APIs deploy ML systems into production
* why monitoring and CI/CD matter for ML systems

---

# Example Commands

## Run Automated Pipeline

```bash
./pipelines/run_pipeline.sh
```

## Launch MLflow Dashboard

```bash
mlflow ui
```

## Run Training Script

```bash
PYTHONPATH=. python src/models/train_lightgbm.py
```

---

# Future Improvements

Potential future enhancements:

* Transformer-based forecasting models
* Temporal Fusion Transformer (TFT)
* XGBoost benchmarking
* demand clustering
* advanced drift detection
* real-time streaming inference
* LLM-powered forecast explanations
* LangChain/LangGraph agent orchestration
* cloud-native deployment workflows

---

# Author

## Hoda Yamani

Machine Learning Engineer | Reinforcement Learning & Applied AI | Forecasting & Intelligent Systems

* Reinforcement Learning
* Forecasting Systems
* MLOps
* Robotics & Intelligent Systems
* Data-Efficient AI

---

# License

This project is intended for educational, research, and portfolio purposes.

