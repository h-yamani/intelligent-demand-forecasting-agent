#!/bin/bash

echo "========== Baseline Model =========="
PYTHONPATH=. python src/models/train_baseline.py

echo "========== LightGBM Model =========="
PYTHONPATH=. python src/models/train_lightgbm.py

echo "========== Error Analysis =========="
PYTHONPATH=. python src/evaluation/error_analysis.py

echo "========== Training pipeline completed successfully =========="
