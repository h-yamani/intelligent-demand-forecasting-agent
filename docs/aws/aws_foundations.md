---

# AWS CLI Setup

## Purpose

AWS CLI allows the project to interact with AWS from the terminal for deployment and automation.

## Installation

```bash
sudo snap install aws-cli --classic
```

## Verify Installation

```bash
aws --version
```

Current verified version:

```text
aws-cli/2.34.45
```

## Planned CLI Usage

- Upload model artifacts to S3
- Manage EC2 deployment
- Automate cloud setup
- Support future GitHub Actions deployment workflows

## IAM Best Practice

Use an IAM user for daily development and deployment work instead of the AWS root account.

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
