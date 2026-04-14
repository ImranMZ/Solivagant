# AI-Powered Brand & Website Generator
> **Final Year Project** | Generate complete brand identities and landing pages in seconds using AI.

---

## Project Architecture

### Folder Structure
```
ai-brand-generator/
├── frontend/                 # React/Next.js Frontend
│   ├── public/               # Static assets
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   │   ├── LogoPreview.jsx
│   │   │   ├── WebsitePreview.jsx
│   │   │   ├── SEOCard.jsx
│   │   │   └── LoadingSpinner.jsx
│   │   ├── pages/            # Page routes
│   │   │   ├── index.jsx     # Home/Input page
│   │   │   ├── result.jsx    # Generated results page
│   │   │   └── _app.jsx      # App wrapper
│   │   ├── styles/           # Tailwind CSS
│   │   │   └── globals.css
│   │   ├── utils/            # Helper functions
│   │   │   └── api.js        # API calls
│   │   └── App.jsx
│   ├── package.json
│   └── tailwind.config.js
│
├── backend/                  # Flask/FastAPI Backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py           # Entry point
│   │   ├── routes/           # API endpoints
│   │   │   ├── generate.py   # Main generation logic
│   │   │   └── health.py     # Health check
│   │   ├── services/         # Business logic
│   │   │   ├── logo_gen.py   # Logo generation service
│   │   │   ├── website_gen.py# HTML/CSS generator
│   │   │   └── seo_gen.py    # SEO meta tags generator
│   │   ├── models/           # Data models
│   │   │   └── request.py    # Pydantic schemas
│   │   └── utils/            # Utilities
│   │       └── prompts.py    # AI prompt templates
│   ├── requirements.txt
│   └── .env                  # Environment variables
│
├── docs/                     # Documentation
│   ├── architecture.md
│   ├── api-docs.md
│   └── user-guide.md
│
├── tests/                    # Test suites
│   ├── frontend/
│   └── backend/
│
├── .gitignore
├── README.md
└── docker-compose.yml        # Optional: Containerization
```

---

## Technology Stack

### Frontend
| Technology | Purpose |
|------------|---------|
| **Next.js 14** | React framework with SSR for fast loading |
| **Tailwind CSS** | Rapid, responsive styling |
| **Framer Motion** | Smooth animations for interactive elements |
| **Axios** | HTTP client for API requests |
| **React Hook Form** | Form handling for user inputs |

### Backend
| Technology | Purpose |
|------------|---------|
| **FastAPI** | High-performance Python API framework |
| **Pydantic** | Data validation and settings management |
| **Python 3.10+** | Core backend language |
| **Uvicorn** | ASGI server for FastAPI |
| **python-dotenv** | Environment variable management |

### AI APIs & Services
| Service | Purpose | Alternative Options |
|---------|---------|---------------------|
| **Groq API (Llama 3)** | Generate website copy, SEO tags, color schemes | Anthropic Claude, Google Gemini |
| **Pollinations.ai** | Logo/image generation (free, no API key) | DALL-E 3, Stable Diffusion API |
| **Replicate API** | Run open-source image models cost-effectively | Hugging Face Inference API |
| **Vercel AI SDK** | Stream AI responses smoothly | - |

### Additional Tools
- **Git & GitHub** - Version control
- **Docker** - Containerization for deployment
- **Vercel** - Frontend hosting
- **Railway/Render** - Backend hosting
- **PostgreSQL/SQLite** - Optional: Save generated projects

---

## MVP Core Features

### 1. **User Input Interface** 
- Simple form to collect:
  - Business name
  - Industry/niche
  - Brand personality (modern, playful, professional, etc.)
  - Preferred color scheme (or auto-generate)
  - Tagline (optional)

### 2. **AI Logo Generation** 
- Generate 3-4 logo variations based on input
- Display preview with download option (PNG/SVG)
- Use Pollinations.ai (free, no API key required)
- *Prompt Engineering*: "Minimalist logo for [business] in [industry], [style] style, vector art"
- URL structure: `https://image.pollinations.ai/prompt/{prompt}`

### 3. **Landing Page Generator** 
- Auto-generate complete HTML/CSS single-page website including:
  - Hero section with headline & CTA
  - About section
  - Features/Services section
  - Contact form placeholder
  - Responsive design
  - Brand colors applied throughout
- Live preview in browser
- Download as `.zip` file

### 4. **SEO Meta Tags Generator** 
- Generate optimized meta tags:
  - Title tag (60 chars)
  - Meta description (160 chars)
  - Open Graph tags for social sharing
  - Keywords based on industry
  - Structured data (JSON-LD) for local business

### 5. **Results Dashboard** 
- Unified view of all generated assets:
  - Logo gallery
  - Website preview (iframe)
  - SEO tags (copy-to-clipboard)
- One-click download all assets
- Option to regenerate individual components

### 6. **Export & Share** 
- Download complete brand kit as ZIP:
  - Logo files (PNG, SVG)
  - `index.html` + `styles.css`
  - `seo-tags.txt`
  - `brand-guide.md` (colors, fonts used)
- Shareable link to preview (optional stretch goal)

---

##  Success Metrics for MVP
-  Generate complete brand kit in < 30 seconds
-  Produce visually coherent designs (color consistency)
-  Mobile-responsive landing pages
-  Pass basic SEO score (>80 on Lighthouse)
-  Deploy and demonstrate end-to-end workflow

---

## Future Enhancements (Post-MVP)
- User accounts & project history
- Multiple page generation (About, Contact, Blog)
- Custom domain integration
- E-commerce template support
- A/B testing for generated content
- AI-powered content refinement chatbot

---

## Getting Started

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/ai-brand-generator.git

# Setup Backend
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Setup Frontend
cd ../frontend
npm install

# Run locally
# Terminal 1: Backend
cd backend && uvicorn app.main:app --reload

# Terminal 2: Frontend
cd frontend && npm run dev
