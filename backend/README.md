# Backend — AI Brand & Website Generator

This backend provides the API for generating brand assets, website HTML, and SEO metadata.

## Stack
- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn
- python-dotenv

## Key Files
- `app/main.py` — FastAPI application entrypoint
- `app/routes/generate.py` — `/api/generate` endpoint
- `app/routes/health.py` — `/api/health` health check
- `app/routes/logo.py` — `/api/logo` logo proxy/download endpoint
- `app/services/logo_gen.py` — logo prompt builder
- `app/services/website_gen.py` — stable landing page HTML generator
- `app/services/seo_gen.py` — SEO metadata helper
- `app/models/request.py` — request validation model
- `app/utils/prompts.py` — prompt templates and utilities

## Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run
```bash
uvicorn app.main:app --reload
```

## API
- `GET /api/health`
- `POST /api/generate`
- `GET /api/logo`

## Notes
- Configure `.env` in `backend/.env` for API keys and environment variables.
- CORS is enabled for development so the frontend can call the API from `http://localhost:8000`.
