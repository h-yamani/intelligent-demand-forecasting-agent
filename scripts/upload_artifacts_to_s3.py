import os
from pathlib import Path

import boto3

BUCKET_NAME = "forecasting-mlops-artifacts-321157465881-us-east-1-an"

ARTIFACTS = [
    "models/lgbm_model.pkl",
    "models/feature_list.json",
    "reports/modeling/metrics.json",
    "reports/modeling/baseline_metrics.json",
    "reports/modeling/error_summary.json",
    "reports/modeling/worst_store_item_pairs.csv",
]


def upload_file_to_s3(local_path: str, bucket: str, s3_key: str) -> None:
    s3 = boto3.client("s3")
    s3.upload_file(local_path, bucket, s3_key)
    print(f"Uploaded {local_path} to s3://{bucket}/{s3_key}")


def main() -> None:
    for artifact in ARTIFACTS:
        path = Path(artifact)

        if not path.exists():
            print(f"Skipping missing file: {artifact}")
            continue

        s3_key = f"forecasting-system/{artifact}"
        upload_file_to_s3(str(path), BUCKET_NAME, s3_key)


if __name__ == "__main__":
    main()
