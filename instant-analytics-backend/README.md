# Instant Analytics API (Backend)

FastAPI + pandas para análisis y agregaciones de datasets.

## Local
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

## Endpoints
- `POST /api/upload` → { upload_id }
- `POST /api/analyze` → { suggestions: Suggestion[] }
- `POST /api/chart-data` → { data: any[] }

## Docker (local)
```bash
docker build -t instant-analytics-api .
docker run -p 8000:8000 instant-analytics-api
```

## Deploy
- **Render**: usa `render.yaml`.
- **Fly.io**: usa `Dockerfile` + `fly.toml`.
