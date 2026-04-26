"""
Unit tests for WebsiteGeneratorAI service.
"""

import json
import pytest
from app.services.website_gen_ai import WebsiteGeneratorAI


def test_generate_website_returns_html(mock_ai_client, monkeypatch):
    monkeypatch.setattr('app.services.website_gen_ai.get_ai_client', lambda: mock_ai_client)

    # Mock AI response to return JSON with required fields
    mock_ai_client.generate.return_value = json.dumps({
        "hero_headline": "Test Headline",
        "hero_subheadline": "Test subheadline",
        "primary_color": "#123456",
        "secondary_color": "#654321",
        "accent_color": "#abcdef",
        "background_color": "#ffffff",
        "text_color": "#000000",
        "features": [{"title": "F1", "description": "D1", "icon": "★"}],
        "benefits": ["B1"],
        "testimonial": {"quote": "Q", "author": "A", "role": "R"},
        "cta_text": "Get Started",
        "cta_secondary_text": "Learn More",
        "footer_tagline": "Footer",
        "layout_variant": "modern_grid",
    })

    gen = WebsiteGeneratorAI()
    result = gen.generate_website("TestCo", "Tag", "Tech", "professional", num_vibes=1)
    assert "html" in result
    assert "palette" in result
    assert "<html" in result["html"].lower()


def test_generate_website_fallback_on_error(monkeypatch):
    # Simulate AI client raising an exception
    def failing_client():
        raise RuntimeError("API down")

    monkeypatch.setattr('app.services.website_gen_ai.get_ai_client', failing_client)

    gen = WebsiteGeneratorAI()
    result = gen.generate_website("TestCo", "Tag", "Tech", "professional")
    assert "html" in result
    assert "<html" in result["html"].lower()
