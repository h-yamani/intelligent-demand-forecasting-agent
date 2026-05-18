# Phase 11: AWS Cloud Deployment Report

## Project
Intelligent Demand Forecasting & Agent-Based Decision Platform

---

# Objective

The objective of this phase was to transition the forecasting platform from a local development environment into a cloud-capable deployment system using AWS infrastructure and Docker-based deployment workflows.

This phase focused on:

- cloud infrastructure setup
- secure AWS access configuration
- cloud artifact storage
- Linux server management
- Docker containerization
- FastAPI deployment
- public API hosting foundations

---

# Cloud Deployment Architecture

```text
User
↓
FastAPI Forecast API
↓
Docker Container
↓
EC2 Instance
↓
S3 Artifact Storage
```

---

# AWS Services Used

- IAM  
  Purpose: Secure identity and permission management

- AWS CLI  
  Purpose: Programmatic interaction with AWS

- S3  
  Purpose: Cloud artifact and file storage

- EC2  
  Purpose: Linux cloud server hosting

- Security Groups  
  Purpose: Firewall and network access control

- Docker  
  Purpose: Containerized deployment

- FastAPI  
  Purpose: API serving layer

---

# IAM and Security Configuration

## IAM Setup

A dedicated IAM workflow was configured instead of using the AWS root account directly.

Completed:

- IAM access configuration
- MFA-enabled authentication
- AWS CLI authentication setup
- budget and billing monitoring configuration

Purpose:

- improve cloud security
- follow AWS best practices
- reduce operational risk
- support secure deployment workflows

---

# AWS CLI Configuration

AWS CLI was installed and configured locally to allow terminal-based interaction with AWS services.

## Commands Used

```bash
sudo snap install aws-cli --classic
aws configure
aws sts get-caller-identity
```

## Configured Parameters

- AWS Access Key
- AWS Secret Access Key
- Default Region
- Output Format

## Outcome

The local machine successfully authenticated with AWS infrastructure through the AWS CLI.

---

# S3 Cloud Storage Setup

An S3 bucket was created to support cloud-based artifact storage.

## Intended Usage

The bucket is designed to store:

- trained ML models
- deployment assets
- reports
- backups
- future experiment artifacts

## S3 Upload Validation

A test upload workflow was performed successfully.

### Commands Used

```bash
echo "AWS S3 connection successful" > test_s3.txt
aws s3 cp test_s3.txt s3://BUCKET-NAME/
```

## Security Configuration

Configured:

- Block all public access enabled
- ACLs disabled
- Bucket-owner enforced mode enabled

## Outcome

The system successfully uploaded and managed files in cloud storage using terminal-based workflows.

---

# EC2 Cloud Server Deployment

A Linux-based AWS EC2 instance was launched to host the forecasting API.

## EC2 Configuration

- Operating System: Ubuntu Server 26.04 LTS
- Instance Type: t3.micro
- Public IP: Enabled
- Authentication: SSH Key Pair

## Purpose

The EC2 server serves as the deployment environment for:

- Docker containers
- FastAPI inference service
- future deployment automation

---

# SSH Remote Access

A secure SSH-based workflow was configured for remote cloud server management.

## Commands Used

```bash
chmod 400 forecasting-key.pem
ssh -i forecasting-key.pem ubuntu@PUBLIC-IP
```

## Outcome

Successfully established:

- secure remote Linux access
- key-based authentication
- remote infrastructure management workflow

---

# Docker Installation and Configuration

Docker Engine was installed and configured on the EC2 server.

## Commands Used

```bash
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo systemctl status docker
```

## Verification

Docker service status:

```text
active (running)
```

## Outcome

The EC2 server became capable of:

- container execution
- reproducible deployments
- API container hosting

---

# GitHub Repository Deployment

The forecasting project repository was cloned directly onto the EC2 server.

## Command Used

```bash
git clone https://github.com/h-yamani/intelligent-demand-forecasting-agent.git
```

## Outcome

The cloud server successfully retrieved and hosted the project source code.

---

# Docker Image Build

A Docker image was built for the forecasting API.

## Command Used

```bash
sudo docker build -t intelligent-demand-api .
```

## Docker Build Responsibilities

The Docker workflow:

- installed dependencies
- packaged the FastAPI application
- created a deployable image
- prepared the API for cloud deployment

## Result

Docker image successfully created:

```text
intelligent-demand-api:latest
```

---

# FastAPI Cloud Deployment

The forecasting API container was deployed on the EC2 server.

## Command Used

```bash
sudo docker run -d -p 8000:8000 --name forecasting-api intelligent-demand-api
```

## Verification

Container verification:

```bash
sudo docker ps
```

## Outcome

The FastAPI application successfully:

- launched inside Docker
- exposed port 8000 publicly
- became accessible through the EC2 public IP

---

# Deployment Workflow Achieved

The deployment workflow now supports:

```text
GitHub Repository
↓
EC2 Cloud Server
↓
Docker Image Build
↓
Container Deployment
↓
FastAPI API Hosting
```

---

# Cost and Resource Management

Cost-awareness practices were incorporated during deployment.

## EC2 Management

The instance was stopped when not in use to reduce operational costs.

## Important Understanding

- Stopping EC2 preserves files and configuration
- Terminating EC2 deletes infrastructure permanently

This workflow supports practical and cost-efficient cloud experimentation.

---

# Skills Demonstrated

This phase demonstrated practical experience with:

- AWS infrastructure
- IAM security workflows
- Linux server administration
- SSH remote access
- Docker containerization
- FastAPI deployment
- cloud storage workflows
- MLOps foundations
- infrastructure engineering
- deployment engineering

---

# Final Outcome

The project successfully transitioned from a local ML system into a cloud-deployable machine learning platform.

The platform now supports:

- cloud-hosted infrastructure
- Dockerized deployment
- remote server operations
- public API hosting
- scalable deployment foundations

---

# Future Improvements

Planned future improvements include:

- HTTPS support
- CI/CD deployment automation
- monitoring and logging
- CloudWatch integration
- Docker registry publishing
- model retraining automation
- scalable inference pipelines
- load balancing

---

# Conclusion

Phase 11 successfully established the cloud deployment foundation for the Intelligent Demand Forecasting platform.

The forecasting system can now operate as a Dockerized FastAPI application deployed on AWS cloud infrastructure using EC2 and S3 services.

This phase established the core infrastructure required for future production-ready MLOps workflows and scalable ML deployment systems.
