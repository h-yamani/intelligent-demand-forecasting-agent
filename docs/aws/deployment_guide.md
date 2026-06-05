# Deployment Guide

## Overview

This document describes the deployment options available for the Intelligent Demand Forecasting & Agent-Based Decision Platform.

Supported deployment targets:

* Local Development
* Docker Deployment
* AWS EC2 Deployment
* AWS SageMaker Deployment

---

# Local Development Deployment

## Clone Repository

```bash
git clone https://github.com/h-yamani/intelligent-demand-forecasting-agent.git

cd intelligent-demand-forecasting-agent
```

## Create Environment

```bash
python -m venv venv

source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Train Forecasting Model

```bash
PYTHONPATH=. python src/pipeline/run_training_pipeline.py
```

Generated artifacts:

```text
models/lgbm_model.pkl
models/feature_list.json
```

---

# Run FastAPI Service

Standard API:

```bash
PYTHONPATH=. uvicorn src.api.main:app --host 0.0.0.0 --port 8000
```

Agentic API:

```bash
PYTHONPATH=. uvicorn src.api.agentic_main_llm:app --host 0.0.0.0 --port 8002
```

API Documentation:

```text
http://127.0.0.1:8000/docs
http://127.0.0.1:8002/docs
```

---

# Run Streamlit Dashboard

```bash
streamlit run src/dashboard/app.py
```

Dashboard:

```text
http://localhost:8501
```

---

# Docker Deployment

## Build Image

```bash
docker build -t intelligent-demand-api .
```

## Run Container

```bash
docker run -p 8000:8000 intelligent-demand-api
```

Verify:

```text
http://localhost:8000/docs
```

---

# AWS EC2 Deployment

## Launch EC2 Instance

Recommended:

* Ubuntu 22.04
* t3.micro (development)
* t3.small or larger (testing)

Security Group:

* SSH (22)
* HTTP (80)
* HTTPS (443)
* API Port (8000)

---

## Connect to Instance

```bash
ssh -i key.pem ubuntu@<public-ip>
```

---

## Install Docker

```bash
sudo apt update

sudo apt install docker.io -y
```

Enable Docker:

```bash
sudo systemctl enable docker

sudo systemctl start docker
```

---

## Deploy Application

Copy project:

```bash
git clone https://github.com/h-yamani/intelligent-demand-forecasting-agent.git
```

Build:

```bash
docker build -t intelligent-demand-api .
```

Run:

```bash
docker run -d -p 8000:8000 intelligent-demand-api
```

Access:

```text
http://<public-ip>:8000/docs
```

---

# AWS SageMaker Deployment

## Overview

The repository includes a SageMaker-compatible inference implementation.

Relevant files:

```text
sagemaker/
├── Dockerfile
├── inference/
└── requirements.txt
```

---

## Package Model

Model artifacts:

```text
models/lgbm_model.pkl
models/feature_list.json
```

Create archive:

```bash
tar -czf model.tar.gz models/
```

Upload to S3:

```bash
aws s3 cp model.tar.gz s3://<bucket-name>/
```

---

## Build SageMaker Container

```bash
docker build -t demand-forecast-sagemaker \
    -f sagemaker/Dockerfile .
```

---

## Push Container to ECR

```bash
aws ecr create-repository \
    --repository-name demand-forecast-sagemaker
```

Tag image:

```bash
docker tag demand-forecast-sagemaker \
    <account-id>.dkr.ecr.<region>.amazonaws.com/demand-forecast-sagemaker
```

Push:

```bash
docker push \
    <account-id>.dkr.ecr.<region>.amazonaws.com/demand-forecast-sagemaker
```

---

## Create SageMaker Endpoint

Use:

* Model artifact from S3
* Container image from ECR

Deploy endpoint through:

* AWS Console
* SageMaker SDK
* Infrastructure-as-Code

---

# Monitoring

Monitoring features include:

* API request logging
* Prediction logging
* Health checks
* Operational diagnostics

Health endpoint:

```text
GET /health
```

---

# CI/CD

The project includes GitHub Actions workflows for:

* Automated testing
* Static analysis
* Docker validation
* Pipeline validation

Checks run automatically on pull requests and merges.

---

# Production Considerations

For production deployments, consider:

* HTTPS termination
* Load balancing
* Secrets management
* Model versioning
* Auto-scaling
* Centralized logging
* CloudWatch monitoring
* Container orchestration (ECS/EKS)

---

# Deployment Summary

The platform supports deployment across the complete ML lifecycle:

```text
Local Development
        ↓
Docker Deployment
        ↓
AWS EC2
        ↓
AWS SageMaker
        ↓
Production Monitoring
```

