FROM python:3.10-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY sagemaker/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY sagemaker/inference/ /app/inference/

ENV PYTHONPATH="/app"

EXPOSE 8080

ENTRYPOINT ["python", "/app/inference/serve.py"]
