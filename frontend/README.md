# Frontend — AI Brand & Website Generator

A lightweight static frontend for generating and previewing brand assets.

## Files
- `index.html` — main page and form UI
- `styles.css` — visual styling for the app
- `script.js` — API integration and UI state management

## Usage
Open `frontend/index.html` in a browser, or serve it with a local static server.

### Recommended local workflow
```bash
cd frontend
# If you have a simple server installed
python -m http.server 3000
```
Then open `http://localhost:3000`.

## Integration
The frontend calls the backend API at `http://localhost:8000/api`.
If your backend runs elsewhere, update `API_URL` in `frontend/script.js`.
