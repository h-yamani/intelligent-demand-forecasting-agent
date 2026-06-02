import boto3

bucket_name = "your-bucket-name"
model_path = "models/model.joblib"
s3_key = "models/model.joblib"

s3 = boto3.client("s3")

s3.upload_file(model_path, bucket_name, s3_key)

print("Model uploaded successfully.")
