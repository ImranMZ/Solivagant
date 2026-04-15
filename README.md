# AI Brand & Website Generator

A lightweight full-stack project that generates brand identity assets, website preview HTML, and SEO metadata from user inputs.

## What this repo contains

- `backend/` — FastAPI backend powering generation endpoints
- `frontend/` — static HTML/CSS/JS frontend for the UI
- `tests/` — test suite for backend sanity checks
- `PROJECT_ARCHITECTURE.md` — architecture notes and folder structure
- `python-package.yml` — package metadata or CI configuration

## Features

- Generate a brand logo preview based on business name, industry, and style
- Produce a responsive landing page HTML preview with brand palette and template metadata
- Create SEO-friendly metadata for page title, description, keywords, and social sharing
- Provide a logo download endpoint for easier brand asset export

## Run locally

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
Open `frontend/index.html` directly in your browser, or serve it from a local static server:

```bash
cd frontend
python -m http.server 3000
```

Then visit `http://localhost:3000`.

## API Endpoints

- `GET /api/health` — health check
- `POST /api/generate` — generate brand assets and website HTML
- `GET /api/logo` — proxy download for generated logo

## Project structure

```text
.
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── utils/
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── tests/
├── PROJECT_ARCHITECTURE.md
├── README.md
└── python-package.yml
```

## Notes

- Keep `backend/.env` out of source control. The repo `.gitignore` already excludes `.env` files.
- If you want frontend and backend on separate ports, update `API_URL` in `frontend/script.js`.

## Next steps

- Add detailed deploy instructions for production
- Add automated CI workflow for tests and linting
- Provide a simple export ZIP feature for generated brand kits
