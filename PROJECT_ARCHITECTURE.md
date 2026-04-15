# Project Architecture

This repository contains a working AI-powered brand and website generator project.

## Current Folder Structure

```text
.
+-- backend/
¦   +-- app/
¦   ¦   +-- main.py
¦   ¦   +-- models/
¦   ¦   ¦   +-- request.py
¦   ¦   +-- routes/
¦   ¦   ¦   +-- generate.py
¦   ¦   ¦   +-- health.py
¦   ¦   ¦   +-- logo.py
¦   ¦   +-- services/
¦   ¦   ¦   +-- logo_gen.py
¦   ¦   ¦   +-- seo_gen.py
¦   ¦   ¦   +-- website_gen.py
¦   ¦   +-- utils/
¦   ¦       +-- prompts.py
¦   +-- requirements.txt
¦   +-- .env
+-- frontend/
¦   +-- index.html
¦   +-- script.js
¦   +-- styles.css
+-- tests/
¦   +-- test_main.py
+-- PROJECT_ARCHITECTURE.md
+-- README.md
+-- PROFILE_README.md
+-- python-package.yml
+-- .gitignore
```

## Backend Overview

- `backend/app/main.py` — FastAPI entrypoint and router configuration
- `backend/app/routes/generate.py` — brand generation endpoint
- `backend/app/routes/health.py` — health check endpoint
- `backend/app/routes/logo.py` — logo proxy/download route
- `backend/app/services/logo_gen.py` — logo URL builder
- `backend/app/services/website_gen.py` — HTML landing page generator
- `backend/app/services/seo_gen.py` — SEO metadata generator
- `backend/app/models/request.py` — request validation model
- `backend/app/utils/prompts.py` — prompt helper utilities

## Frontend Overview

- `frontend/index.html` — main application UI
- `frontend/script.js` — frontend logic and API integration
- `frontend/styles.css` — branding and layout styles

## How to Run

### Start Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Start Frontend
Open `frontend/index.html` in a browser or serve it locally:
```bash
cd frontend
python -m http.server 3000
```

## Notes

- Keep `backend/.env` private and do not commit secret credentials.
- The frontend uses `http://localhost:8000/api` by default. Update `API_URL` in `frontend/script.js` if needed.
- This architecture documentation now matches the actual current repository layout.
