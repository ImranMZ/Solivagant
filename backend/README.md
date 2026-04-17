# Solivagant - AI Brand Designer

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

- `GET /api/health` - Health check
- `POST /api/generate` - Generate full brand identity
- `GET /api/vibes` - List vibe styles

## Tech Stack

- Backend: FastAPI + Groq LLM
- Frontend: Vanilla HTML/CSS/JS (iOS dark theme)

## License

MIT