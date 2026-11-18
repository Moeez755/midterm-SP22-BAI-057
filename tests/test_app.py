import os
import json

def test_config_exists():
    assert os.path.exists("config.json")
    with open("config.json") as f:
        cfg = json.load(f)
    assert cfg["student_id"] == "SP22-BAI-057"

def test_dataset_generated():
    assert os.path.exists("dataset/train.csv"), "dataset/train.csv missing — generate_dataset.py must run first"

def test_artifacts_generated():
    assert os.path.exists("artifacts/model.joblib"), "model.joblib missing — train.py must run first"
    assert os.path.exists("artifacts/metrics.json"), "metrics.json missing — train.py must run first"

def test_metrics_shape():
    with open("artifacts/metrics.json") as f:
        m = json.load(f)
    assert "accuracy" in m
    assert isinstance(m["accuracy"], (int, float))
    assert m["accuracy"] > 0.5, f"Accuracy {m['accuracy']} should beat random"
