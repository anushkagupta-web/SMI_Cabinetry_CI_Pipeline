# SMI Cabinetry CI Pipeline Demo 

Simple Flask API for demonstrating GCP Cloud Build CI pipeline. (Only for Practice Purpose)

## Project Structure

```
├── app/
│   ├── __init__.py
│   └── main.py              # Flask API
├── tests/
│   ├── __init__.py
│   └── test_main.py         # Unit tests
├── Dockerfile
├── requirements.txt
├── cloudbuild.yaml          # GCP Cloud Build config
└── README.md
```

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | Returns hello message |
| `GET /health` | Health check |
| `GET /api/greet/<name>` | Personalized greeting |

## Local Development

```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run app
python app/main.py

# Run tests
pytest tests/ -v
```

## Docker

```bash
# Build image
docker build -t ci-demo-app .

# Run container
docker run -p 8080:8080 ci-demo-app
```

## CI Pipeline (Cloud Build)

Pipeline triggers on push to `main` branch:

| Step | Description |
|------|-------------|
| Checkout | Automatic by Cloud Build |
| Build | Docker image build |
| Push | Push to Artifact Registry |

## GCP Setup

1. Create Artifact Registry:
```bash
gcloud artifacts repositories create smi-repo \
  --repository-format=docker \
  --location=asia-south1
```

2. Connect GitHub repo to Cloud Build

3. Create trigger for `main` branch pointing to `cloudbuild.yaml`
