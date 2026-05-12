#!/bin/bash

echo "========== Baseline Model =========="
PYTHONPATH=. python src/models/train_baseline.py

echo "========== LightGBM + MLflow =========="
PYTHONPATH=. python src/models/train_lightgbm.py

echo "========== Error Analysis =========="
PYTHONPATH=. python src/evaluation/error_analysis.py

echo "========== Pipeline Finished =========="
echo "Launch MLflow UI with:"
echo "mlflow ui"
