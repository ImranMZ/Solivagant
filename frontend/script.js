// Configuration
const API_URL = 'http://localhost:8000/api';

// Global state
let currentResults = null;

const form = document.getElementById('brandForm');
const resultsSection = document.getElementById('resultsSection');
const designDetails = document.getElementById('designDetails');
const loadingIndicator = document.getElementById('loadingIndicator');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const formData = {
    business_name: document.getElementById('businessName').value,
    tagline: document.getElementById('tagline').value,
    industry: document.getElementById('industry').value,
    color_scheme: document.getElementById('colorScheme').value,
    // Defaults for hidden UI choices
    logo_style: 'minimalist',
    website_template: 'modern'
  };

  showLoading(true);

  try {
    const response = await fetch(`${API_URL}/generate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    });

    if (!response.ok) {
      const errorPayload = await response.json().catch(() => null);
      const message = errorPayload?.detail || `HTTP error ${response.status}`;
      throw new Error(message);
    }

    const json = await response.json();
    console.log('Backend response:', json);
    
    if (!json.success) {
        throw new Error(json.detail || 'Generation failed on backend');
    }

    currentResults = json.data;
    showLoading(false);
    displayResults(currentResults);
  } catch (error) {
    console.error('Frontend Error:', error);
    showLoading(false);
    showError(error.message);
  }
});

function showLoading(loading) {
  if (loading) {
    form.style.display = 'none';
    loadingIndicator.style.display = 'flex';
    resultsSection.style.display = 'none';
    designDetails.style.display = 'none';
  } else {
    loadingIndicator.style.display = 'none';
  }
}

function showError(message) {
  // Simple but clean alert
  alert(`Generation issue: ${message}`);
  form.style.display = 'flex';
}

function displayResults(data) {
  // Populate Logo
  if (data.logo_url) {
    const logoImg = document.getElementById('logoImage');
    logoImg.src = data.logo_url;
    document.getElementById('logoDownload').href = data.logo_download_url || data.logo_url;
  }

  // General Labels
  document.getElementById('themeName').textContent = data.theme_name || 'Design Ethos';
  document.getElementById('fontFamily').textContent = data.font_family || 'Inter';

  // Palette Logic
  const paletteRow = document.getElementById('paletteRow');
  paletteRow.innerHTML = '';
  if (data.design_palette) {
    const p = data.design_palette;
    const chips = [
      { label: 'Primary', color: p.primary },
      { label: 'Sec', color: p.secondary },
      { label: 'Acc', color: p.accent },
      { label: 'Surf', color: p.surface },
    ];
    chips.forEach(c => {
      const div = document.createElement('div');
      div.className = 'palette-chip';
      div.style.background = c.color;
      div.textContent = c.label;
      paletteRow.appendChild(div);
    });
  }

  // Palette Suggestions
  const suggestions = document.getElementById('paletteSuggestions');
  suggestions.innerHTML = '';
  if (Array.isArray(data.palette_suggestions)) {
    data.palette_suggestions.slice(0, 2).forEach(s => {
        const div = document.createElement('div');
        div.className = 'palette-suggestion';
        div.innerHTML = `<div class="palette-swatch-small" style="background:${s.palette.primary}"></div> <span>${s.palette.name}</span>`;
        suggestions.appendChild(div);
    });
  }

  // SEO Metadata
  const seo = document.getElementById('seoMetadata');
  seo.innerHTML = '';
  if (data.seo_tags) {
      const tags = [
          { k: 'Title', v: data.seo_tags.title },
          { k: 'Desk', v: data.seo_tags.description }
      ];
      tags.forEach(t => {
          if (t.v) {
              const p = document.createElement('p');
              p.innerHTML = `<strong>${t.k}:</strong> ${t.v}`;
              seo.appendChild(p);
          }
      });
  }

  // System Specs
  const featList = document.getElementById('featureList');
  featList.innerHTML = '';
  if (Array.isArray(data.features)) {
      data.features.slice(0, 4).forEach(f => {
          const li = document.createElement('li');
          li.textContent = f.title;
          featList.appendChild(li);
      });
  }

  const tone = document.getElementById('brandTone');
  tone.textContent = data.template_description || 'Sophisticated, modern, and high-performance design.';

  // Show Sections
  resultsSection.style.display = 'grid';
  designDetails.style.display = 'block';

  // Final Polish: Scroll to results
  resultsSection.scrollIntoView({ behavior: 'smooth' });
  
  // Refresh icons
  if (window.lucide) {
      lucide.createIcons();
  }
}

function showWebsitePreview() {
  if (!currentResults || !currentResults.website_html) {
    alert('Preview pending...');
    return;
  }
  const modal = document.getElementById('websiteModal');
  const frame = document.getElementById('websitePreview');
  frame.innerHTML = '';
  const iframe = document.createElement('iframe');
  iframe.srcdoc = currentResults.website_html;
  frame.appendChild(iframe);
  modal.classList.add('active');
}

function closeWebsitePreview() {
  document.getElementById('websiteModal').classList.remove('active');
}

function scrollToForm() {
    document.getElementById('generationForm').scrollIntoView({ behavior: 'smooth' });
}

window.addEventListener('click', (e) => {
    if (e.target.id === 'websiteModal') closeWebsitePreview();
});

// Mock connection check
window.addEventListener('DOMContentLoaded', async () => {
    try {
        await fetch(`${API_URL}/health`);
    } catch(e) {
        console.warn('Backend offline');
    }
});
