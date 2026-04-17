# Solivagant - AI Brand Designer

[ ![AI-Powered Brand Generator](https://img.shields.io/badge/AI-Powered%20Brand-Generator-blue) ](https://github.com/ImranMZ/Solivagant)
[ ![MIT License](https://img.shields.io/badge/License-MIT-green) ](https://opensource.org/licenses/MIT)

An AI-powered brand identity generator that creates complete brand assets including logos, websites, social media posts, and brand kits using 100% Groq AI - no external image APIs required.

## Features

- **AI Logo Generation** - Generate unique SVG logos using Groq LLM
- **AI Website Generation** - Create complete landing page HTML with AI-generated content
- **Social Media Posts** - AI-generated poster designs for Twitter, LinkedIn, and Instagram
- **Brand Kit** - Color palettes, email signatures, business cards, font recommendations
- **Multiple Vibe Styles** - Professional, Playful, Premium, Minimal, Bold

## Quick Start

### Backend
```bash
cd backend
pip install -r requirements.txt
# Add GROQ_API_KEY to backend/.env
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

### Frontend
```bash
cd frontend
python -m http.server 3000
```

Open http://127.0.0.1:3000

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Health check |
| POST | `/api/generate` | Generate full brand identity |
| GET | `/api/vibes` | List available vibe styles |
| POST | `/api/social-posts` | Generate social media posts |

## Tech Stack

- **Backend**: FastAPI + Groq LLM
- **Frontend**: Vanilla HTML/CSS/JS (iOS dark theme)
- **No external image APIs** - 100% AI-generated content

## Project Structure

```
Solivagant/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI app
│   │   ├── models/        # Pydantic models
│   │   ├── routes/       # API endpoints
│   │   └── services/     # AI generation services
│   │       ├── logo_gen.py
│   │       ├── website_gen_ai.py
│   │       ├── social_posts_gen.py
│   │       └── seo_gen.py
│   ├── .env              # API keys (not in git)
│   └── requirements.txt
├── frontend/
│   └── index.html        # Single-page app
└── tests/
    ├── test_routes.py
    └── test_website_gen_ai.py
```

## Brand Generation Flow

1. User enters business name + tagline
2. Selects vibe (Professional/Playful/Premium/Minimal/Bold)
3. Backend calls Groq LLM for each component:
   - Logo (SVG)
   - Website (HTML)
   - Social Posts (HTML poster designs)
   - SEO metadata
4. Frontend displays all brand assets
5. Download as SVG, HTML, or JSON brand kit

## Environment Variables

Create `backend/.env`:
```
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

## License

MIT License