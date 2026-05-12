import subprocess


def run_step(name, command):
    print(f"\n========== {name} ==========")
    subprocess.run(command, shell=True, check=True)


if __name__ == "__main__":

    run_step(
        "Baseline Forecast Model", "PYTHONPATH=. python src/models/train_baseline.py"
    )

    run_step(
        "LightGBM Forecast Model", "PYTHONPATH=. python src/models/train_lightgbm.py"
    )

    run_step(
        "Forecast Error Analysis",
        "PYTHONPATH=. python src/evaluation/error_analysis.py",
    )

    print("\nTraining pipeline completed successfully.")
