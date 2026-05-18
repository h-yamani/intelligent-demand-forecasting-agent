# AWS Phase 11 Cloud Deployment Notes

## Project
Intelligent Demand Forecasting & Agent-Based Decision Platform

---

# Objective

Prepare and deploy the forecasting platform to AWS cloud infrastructure.

This phase introduces:

- AWS cloud foundations
- IAM security
- AWS CLI
- S3 artifact storage
- EC2 cloud servers
- SSH remote access
- deployment preparation

---

# AWS Services Used

| Service | Purpose |
|---|---|
| IAM | Identity and access management |
| S3 | Cloud artifact storage |
| EC2 | Virtual cloud server |
| AWS CLI | Terminal interaction with AWS |
| Security Groups | Cloud firewall rules |

---

# AWS Account Setup

## Important Security Steps

Completed:

- Enabled MFA using Authy
- Created IAM user
- Avoided using root account for daily work
- Created AWS budget alerts
- Configured AWS CLI authentication

---

# IAM Setup

## IAM User

Created user:

```text
hoda-mlops
```

Purpose:

- secure AWS access
- avoid using root account
- support CLI and deployment workflows

---

# AWS CLI Installation

## Install AWS CLI

```bash
sudo snap install aws-cli --classic
```

## Verify Installation

```bash
aws --version
```

Example output:

```text
aws-cli/2.x.x
```

---

# Configure AWS CLI

## Configure Credentials

```bash
aws configure
```

Configuration used:

```text
Default region name: us-east-1
Default output format: json
```

---

# Verify AWS Authentication

## Test AWS Connection

```bash
aws sts get-caller-identity
```

Purpose:

- verify authentication
- confirm IAM permissions
- validate AWS CLI setup

---

# S3 Cloud Storage

## Purpose of S3

Used to store:

- ML models
- reports
- deployment artifacts
- backups
- future MLflow artifacts

---

# Create S3 Test File

```bash
echo "AWS S3 connection successful" > test_s3.txt
```

---

# Upload File to S3

```bash
aws s3 cp test_s3.txt s3://YOUR-BUCKET-NAME/
```

---

# Upload Real Project Files

## Upload README

```bash
aws s3 cp README.md s3://YOUR-BUCKET-NAME/reports/
```

## Upload Models Folder

```bash
aws s3 cp models/ s3://YOUR-BUCKET-NAME/models/ --recursive
```

---

# View S3 Bucket Contents

## From Terminal

```bash
aws s3 ls s3://YOUR-BUCKET-NAME/
```

## From AWS Console

- Open AWS Console
- Open Amazon S3
- Open project bucket

---

# S3 Security Configuration

Configured:

- Block all public access = enabled
- ACLs disabled
- Bucket owner enforced
- IAM user used instead of root account

---

# EC2 Cloud Server

## Purpose

Host:

- Docker containers
- FastAPI forecasting API
- deployment services

---

# EC2 Instance Configuration

## Instance Name

```text
forecasting-api-server
```

## Operating System

```text
Ubuntu Server 26.04 LTS
```

## Instance Type

```text
t3.micro
```

Reason:

- low cost
- suitable for learning and API deployment

---

# SSH Key Pair

## Created Key Pair

```text
forecasting-key.pem
```

Purpose:

- secure SSH login
- remote server authentication

IMPORTANT:

Never share the .pem file publicly.

---

# SSH Key Permission Setup

## Secure Private Key

```bash
chmod 400 forecasting-key.pem
```

Purpose:

Restrict private key access for SSH security.

---

# Connect to EC2 via SSH

## SSH Command

```bash
ssh -i forecasting-key.pem ubuntu@YOUR-PUBLIC-IP
```

Example:

```bash
ssh -i forecasting-key.pem ubuntu@54.xxx.xxx.xxx
```

---

# First SSH Login

First-time SSH warning:

```text
Are you sure you want to continue connecting (yes/no)?
```

Answer:

```text
yes
```

Purpose:

- add EC2 server fingerprint to known hosts
- establish trusted connection

---

# Successful EC2 Connection

Example prompt:

```bash
ubuntu@ip-172-31-xx-xxx:~$
```

Meaning:

- connected to AWS cloud server
- remote Linux shell active

---

# First EC2 Server Maintenance Command

## Update Ubuntu Packages

```bash
sudo apt update
```

Purpose:

- refresh package lists
- prepare server for installations

---

# Current Cloud Architecture

```text
User
↓
FastAPI Forecast API
↓
Docker Container
↓
EC2 Instance
↓
S3 Model Artifacts
```

---

# Important AWS Cost Safety Notes

## Always Stop EC2 When Not Using

From AWS Console:

```text
Instance state → Stop instance
```

Reason:

Running EC2 instances generate charges.

---

# Professional Skills Demonstrated

This phase demonstrates:

- cloud engineering
- Linux server management
- IAM security
- AWS CLI usage
- artifact storage workflows
- SSH remote access
- infrastructure setup
- deployment preparation
- MLOps foundations

---

# Next Planned Steps

## Deployment Preparation

Upcoming tasks:

- install Docker on EC2
- deploy FastAPI API
- expose API publicly
- pull artifacts from S3
- container deployment
- CI/CD cloud automation

---

# Long-Term Goals

Future cloud architecture goals:

- Docker registry publishing
- HTTPS setup
- load balancing
- automated deployment
- monitoring
- model retraining automation
- MLflow cloud integration
- production inference pipeline

---

# Key Learning Summary

By completing this phase:

- AWS account configured professionally
- cloud storage integrated
- cloud server launched
- secure authentication implemented
- remote infrastructure management achieved
- project transitioned from local ML system to cloud-capable ML platform

