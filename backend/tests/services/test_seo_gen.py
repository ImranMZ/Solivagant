"""
Unit tests for SEOGenerator service.
"""

import json
import pytest
from app.services.seo_gen import SEOGenerator


def test_generate_seo_returns_dict(mock_ai_client, monkeypatch):
    monkeypatch.setattr('app.services.seo_gen.get_ai_client', lambda: mock_ai_client)
    mock_ai_client.generate.return_value = json.dumps({
        "title": "TestCo | Great Tagline",
        "description": "A great description for SEO.",
        "keywords": ["test", "brand"],
        "og_title": "TestCo",
        "og_description": "Great tagline",
        "twitter_card": "summary_large_image",
    })

    gen = SEOGenerator()
    seo = gen.generate_seo("TestCo", "Great Tagline", "Tech")
    assert isinstance(seo, dict)
    assert "title" in seo
    assert "keywords" in seo


def test_generate_seo_fallback_on_error(monkeypatch):
    def failing():
        raise RuntimeError("API down")
    monkeypatch.setattr('app.services.seo_gen.get_ai_client', failing)

    gen = SEOGenerator()
    seo = gen.generate_seo("TestCo", "Tag", "Tech")
    assert "title" in seo
    assert "keywords" in seo
