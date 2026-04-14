<div align="center">

# 🚀 AI-Powered Brand & Website Generator

[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python)](https://python.org)
[![Next.js](https://img.shields.io/badge/Next.js-14-black.svg?style=for-the-badge&logo=next.js)](https://nextjs.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green.svg?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)

### ✨ Generate Complete Brand Identities & Landing Pages in Seconds Using AI

**$0 Budget Friendly** - Uses free Groq API (Llama 3) and Pollinations.ai

</div>

---

## 🌟 Overview

This project is an **AI-powered brand generator** that creates complete brand identities and landing pages in seconds. Perfect for entrepreneurs, startups, and anyone needing a quick professional online presence.

### Key Features
- 🎨 **AI Logo Generation** - Create unique logos using Pollinations.ai (free, no API key)
- 🌈 **Color Scheme Generation** - Get cohesive color palettes for your brand
- 📝 **Website Content** - Auto-generate compelling copy for your landing page
- 🔍 **SEO Meta Tags** - Optimized meta tags for search engines
- 📱 **Responsive Design** - Mobile-friendly landing pages
- 💾 **One-Click Export** - Download all assets as a ZIP file

---

## 🛠️ Tech Stack

### Frontend
- **Next.js 14** - React framework with SSR
- **Tailwind CSS** - Rapid, responsive styling
- **Framer Motion** - Smooth animations
- **React Hook Form** - Form handling
- **Axios** - HTTP client

### Backend
- **FastAPI** - High-performance Python API
- **Groq API (Llama 3)** - Free AI text/code generation
- **Pollinations.ai** - Free logo/image generation
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- Groq API Key (free from https://console.groq.com)

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/ai-brand-generator.git
cd ai-brand-generator
```

### 2. Setup Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

### 3. Setup Frontend
```bash
cd ../frontend
npm install

# Configure environment variables
cp .env.local.example .env.local
```

### 4. Run the Application

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # If not already active
uvicorn app.main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

Open http://localhost:3000 in your browser!

---

## 📁 Project Structure

```
ai-brand-generator/
├── frontend/                 # Next.js Frontend
│   ├── src/
│   │   ├── components/       # UI components
│   │   ├── pages/            # Page routes
│   │   ├── styles/           # Tailwind CSS
│   │   └── utils/            # Helper functions
│   └── package.json
│
├── backend/                  # FastAPI Backend
│   ├── app/
│   │   ├── routes/           # API endpoints
│   │   ├── services/         # Business logic
│   │   ├── models/           # Data models
│   │   └── utils/            # Utilities
│   └── requirements.txt
│
├── docs/                     # Documentation
├── tests/                    # Test suites
└── README.md
```

---

## 🎯 Usage

1. **Enter Business Details** - Fill in your business name, industry, and style preferences
2. **Generate Brand** - Click "Generate My Brand" to create your complete brand kit
3. **Review Results** - See your logo, colors, website content, and SEO tags
4. **Download Assets** - Export everything as a ZIP file

---

## 📄 License

MIT License - feel free to use this for your projects!

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

<div align="center">

### "Code is poetry, design is the rhythm." 

Made with ❤️ using AI

</div>
