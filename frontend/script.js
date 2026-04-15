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
    logo_style: document.getElementById('logoStyle').value,
    color_scheme: document.getElementById('colorScheme').value,
    website_template: document.getElementById('websiteTemplate').value
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
    currentResults = json.data;
    showLoading(false);
    displayResults(currentResults);
  } catch (error) {
    showLoading(false);
    showError(error.message);
  }
});

function showLoading(loading) {
  if (loading) {
    form.style.display = 'none';
    loadingIndicator.style.display = 'grid';
    resultsSection.style.display = 'none';
    designDetails.style.display = 'none';
  } else {
    loadingIndicator.style.display = 'none';
  }
}

function showError(message) {
  alert(`Unable to generate brand. ${message}`);
  form.style.display = 'grid';
}

function displayResults(data) {
  if (data.logo_url) {
    document.getElementById('logoImage').src = data.logo_url;
    document.getElementById('logoDownload').href = data.logo_download_url || data.logo_url;
  }

  document.getElementById('themeName').textContent = data.theme_name || 'Brand palette';
  document.getElementById('fontFamily').textContent = data.font_family || 'Inter';

  const paletteRow = document.getElementById('paletteRow');
  paletteRow.innerHTML = '';

  if (data.design_palette) {
    const palette = data.design_palette;
    const chips = [
      { label: 'Primary', color: palette.primary },
      { label: 'Secondary', color: palette.secondary },
      { label: 'Accent', color: palette.accent },
      { label: 'Surface', color: palette.surface },
    ];

    chips.forEach((item) => {
      const chip = document.createElement('div');
      chip.className = 'palette-chip';
      chip.style.background = item.color;
      chip.textContent = item.label;
      paletteRow.appendChild(chip);
    });
  }

  const paletteSuggestions = document.getElementById('paletteSuggestions');
  paletteSuggestions.innerHTML = '';
  if (Array.isArray(data.palette_suggestions)) {
    data.palette_suggestions.slice(0, 3).forEach((item) => {
      const block = document.createElement('div');
      block.className = 'palette-suggestion';
      const swatch = document.createElement('div');
      swatch.className = 'palette-swatch-small';
      swatch.style.background = item.palette.primary;
      const label = document.createElement('div');
      label.innerHTML = `<strong>${item.palette.name}</strong><br /><span style="color:#475569;">${item.palette.primary}, ${item.palette.secondary}</span>`;
      block.appendChild(swatch);
      block.appendChild(label);
      paletteSuggestions.appendChild(block);
    });
  }

  const seoMetadata = document.getElementById('seoMetadata');
  seoMetadata.innerHTML = '';
  if (data.seo_tags) {
    const seoKeys = [
      { title: 'Title', value: data.seo_tags.title },
      { title: 'Description', value: data.seo_tags.description },
      { title: 'Keywords', value: Array.isArray(data.seo_tags.keywords) ? data.seo_tags.keywords.join(', ') : data.seo_tags.keywords },
      { title: 'OG Title', value: data.seo_tags.og_title },
      { title: 'OG Description', value: data.seo_tags.og_description }
    ];

    seoKeys.forEach((item) => {
      if (item.value) {
        const p = document.createElement('p');
        p.innerHTML = `<strong>${item.title}</strong><br>${item.value}`;
        seoMetadata.appendChild(p);
      }
    });
  }

  const featureList = document.getElementById('featureList');
  featureList.innerHTML = '';
  if (Array.isArray(data.features)) {
    data.features.forEach((feature) => {
      const li = document.createElement('li');
      li.textContent = `${feature.title}: ${feature.description}`;
      featureList.appendChild(li);
    });
  }

  const brandTone = document.getElementById('brandTone');
  if (data.template_description) {
    brandTone.textContent = data.template_description;
  } else {
    brandTone.textContent = 'Modern, professional, and well structured for business growth.';
  }

  resultsSection.style.display = 'block';
  designDetails.style.display = 'grid';
}

function showWebsitePreview() {
  if (!currentResults || !currentResults.website_html) {
    alert('Website HTML is not available yet. Please generate a brand first.');
    return;
  }

  const modal = document.getElementById('websiteModal');
  const preview = document.getElementById('websitePreview');
  preview.innerHTML = '';

  const iframe = document.createElement('iframe');
  iframe.srcdoc = currentResults.website_html;
  preview.appendChild(iframe);

  modal.classList.add('active');
}

function closeWebsitePreview() {
  document.getElementById('websiteModal').classList.remove('active');
}

function resetForm() {
  form.reset();
  resultsSection.style.display = 'none';
  designDetails.style.display = 'none';
  form.style.display = 'grid';
  currentResults = null;
}

function scrollToForm() {
  document.getElementById('generationForm').scrollIntoView({ behavior: 'smooth' });
}

window.addEventListener('click', (event) => {
  const modal = document.getElementById('websiteModal');
  if (event.target === modal) {
    closeWebsitePreview();
  }
});

window.addEventListener('DOMContentLoaded', async () => {
  try {
    await fetch(`${API_URL}/health`);
  } catch (error) {
    console.warn('Cannot connect to API. Make sure the backend is running on http://localhost:8000');
  }
});
