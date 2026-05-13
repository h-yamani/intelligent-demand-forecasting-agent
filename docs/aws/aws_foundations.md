# AWS Deployment Foundations

## Objective

Prepare the AWS cloud foundation required for deploying the Intelligent Demand Forecasting platform safely and professionally.

---

# Planned AWS Architecture

User
↓
FastAPI Forecast API
↓
Docker Container
↓
EC2 Instance
↓
Model Artifacts from S3

---

# AWS Services Planned

## EC2
Purpose:
Host Dockerized FastAPI forecasting service.

## S3
Purpose:
Store:
- trained models
- reports
- deployment artifacts
- backups

## IAM
Purpose:
Control permissions and security access.

## CloudWatch (future)
Purpose:
Logging and monitoring.

---

# Learning Checklist

- [ ] Understand AWS account structure
- [ ] Configure billing alerts
- [ ] Install AWS CLI
- [ ] Understand IAM users and roles
- [ ] Understand EC2 basics
- [ ] Understand S3 buckets
- [ ] Understand security groups
- [ ] Learn Docker deployment on EC2
- [ ] Plan deployment workflow

---

# Initial Deployment Goal

Deploy FastAPI forecasting API inside Docker container on EC2 instance.

---

# Future Goals

- automated deployment
- Docker registry publishing
- monitoring
- HTTPS
- load balancing
- model retraining automation
