# S3 Artifact Storage

## Objective

Use Amazon S3 to store project artifacts for the Intelligent Demand Forecasting platform.

---

# S3 Bucket Purpose

The S3 bucket stores:

- trained model artifacts
- evaluation reports
- deployment files
- backup project outputs

---

# AWS CLI Installation

Install AWS CLI:

```bash
sudo snap install aws-cli --classic
```

Verify installation:

```bash
aws --version
```

---

# Configure AWS CLI

Configure AWS credentials:

```bash
aws configure
```

Configuration values used:

```text
Default region name: us-east-1
Default output format: json
```

Verify AWS connection:

```bash
aws sts get-caller-identity
```

---

# Create Test File

Create a local test file:

```bash
echo "AWS S3 connection successful" > test_s3.txt
```

---

# Upload Files to S3

Upload single file:

```bash
aws s3 cp test_s3.txt s3://YOUR-BUCKET-NAME/
```

Upload README example:

```bash
aws s3 cp README.md s3://YOUR-BUCKET-NAME/reports/
```

Upload folder recursively:

```bash
aws s3 cp models/ s3://YOUR-BUCKET-NAME/models/ --recursive
```

---

# View Bucket Contents

List bucket contents from terminal:

```bash
aws s3 ls s3://YOUR-BUCKET-NAME/
```

View bucket in AWS Console:
- AWS Console
- Amazon S3
- Open project bucket

---

# Security Notes

- Public access is blocked.
- IAM user is used instead of root account.
- Bucket is used only for private ML artifacts.

---

# Planned Future Usage

- store trained forecasting models
- store MLflow artifacts
- store deployment assets
- support automated deployment pipelines
- support future CI/CD cloud workflows
