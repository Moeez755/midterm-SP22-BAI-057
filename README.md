# Midterm — SP22-BAI-057

CSC418 DevOps for Cloud Computing — Lab Midterm.

Automated ML retraining pipeline: GitHub push triggers Jenkins to regenerate the dataset, retrain the model, run tests, rebuild the Docker image, and redeploy the FastAPI service on AWS EC2, then emails the result.

## Endpoints (port 8000)

- GET /health — service readiness
- GET /metrics — model metrics (student_id, accuracy, training_rows, model_version, git_sha)
- POST /predict — batch prediction

## Stack

FastAPI + uvicorn · scikit-learn logistic regression · Jenkins pipeline · Docker · AWS EC2
# webhook test
# webhook test
# webhook test
# webhook test
# webhook test
