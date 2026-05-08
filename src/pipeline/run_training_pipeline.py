import subprocess

def run_step(name, command):
    print(f"\n========== {name} ==========")
    subprocess.run(command, shell=True, check=True)

if __name__ == "__main__":
    run_step(
        "Baseline Model",
        "PYTHONPATH=. python src/models/train_baseline.py"
    )

    run_step(
        "LightGBM Model",
        "PYTHONPATH=. python src/models/train_lightgbm.py"
    )

    print("\nTraining pipeline completed successfully.")
