# Solivagant — AI Brand Designer

An AI-powered web application that automates the creation of complete brand identities. Built as a BS Software Engineering final semester project.

## Features

- **5-Step Brand Wizard** — Guided input for brand identity, audience, visual style, colors, and review
- **AI Logo Generation** — SVG logos generated via Groq LLM
- **Landing Page Generator** — Complete HTML pages with AI-written copy
- **Social Media Posts** — Platform-specific copy for Twitter/X, LinkedIn, Instagram
- **SEO Metadata** — Optimized titles, descriptions, and keywords
- **Interactive Tools** — Editable color palette, logo playground, dark mode, Twist It regeneration
- **Brand Kit Export** — Download all assets as a ZIP (logo.svg, website.html, brand-guide.md, social posts, SEO metadata)
- **Brand Score** — AI-evaluated completeness rating with animated donut chart

## Tech Stack

| Layer | Tech |
|---|---|
| Frontend | Next.js 14, React 18, Tailwind CSS, Framer Motion |
| Backend | FastAPI, Pydantic |
| AI | Groq API (Llama 3), Pollinations.ai |

## Quick Start

### Backend

```bash
cd backend
python -m venv venv
.\venv\Scripts\activate    # Windows
cp .env.example .env       # Add your GROQ_API_KEY
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
cp .env.local.example .env.local
npm install
npm run dev
```

Open http://localhost:3000

## API

| Method | Path | Description |
|---|---|---|
| POST | `/api/generate/brand` | Generate full brand identity |
| POST | `/api/generate/twist` | Regenerate with random color mood |
| POST | `/api/generate/export` | Download brand kit as ZIP |
| GET | `/api/health` | Health check |
