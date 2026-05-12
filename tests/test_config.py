import yaml


def test_config_loads_required_sections():
    with open("config/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    assert "data" in config
    assert "split" in config
    assert "model" in config
    assert "output" in config

    assert "raw_path" in config["data"]
    assert "train_end" in config["split"]
    assert "valid_end" in config["split"]
    assert config["model"]["type"] == "lightgbm"
    assert "model_path" in config["output"]
