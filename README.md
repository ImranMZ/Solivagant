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

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/health | Health check |
| POST | /api/generate | Generate full brand identity |
| GET | /api/vibes | List vibe styles |

## Tech Stack

- **Backend**: FastAPI + Groq LLM
- **Frontend**: Vanilla HTML/CSS/JS (iOS dark theme)
- **No external image APIs** - 100% AI-generated

## Project Structure

```
Solivagant/
â”œâ”€â”€ backend/
â”‚   â”œâ”€â”€ app/
â”‚   â”‚   â”œâ”€â”€ main.py
â”‚   â”‚   â”œâ”€â”€ models/
â”‚   â”‚   â”œâ”€â”€ routes/
â”‚   â”‚   â””â”€â”€ services/
â”‚   â”‚       â”œâ”€â”€ logo_gen.py
â”‚   â”‚       â”œâ”€â”€ website_gen_ai.py
â”‚   â”‚       â”œâ”€â”€ social_posts_gen.py
â”‚   â”‚       â””â”€â”€ seo_gen.py
â”‚   â”œâ”€â”€ .env
â”‚   â””â”€â”€ requirements.txt
â”œâ”€â”€ frontend/
â”‚   â””â”€â”€ index.html
â””â”€â”€ tests/
```

## Environment Variables

Create `backend/.env`:
```
GROQ_API_KEY=your_key_here
```

## License

MIT