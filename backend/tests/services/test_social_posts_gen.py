"""
Unit tests for SocialPostsGenerator service.
"""

import json
import pytest
from app.services.social_posts_gen import SocialPostsGenerator


def test_generate_posts_returns_list(mock_ai_client, monkeypatch):
    monkeypatch.setattr('app.services.social_posts_gen.get_ai_client', lambda: mock_ai_client)
    mock_ai_client.generate.return_value = json.dumps([
        {
            "platform": "twitter",
            "caption": "Test caption",
            "hashtags": ["#Test"],
            "brand_message": "Message",
            "poster_html": "<div>Mock poster</div>",
        }
    ])

    gen = SocialPostsGenerator()
    posts = gen.generate_posts("TestCo", "Tag", "professional")
    assert isinstance(posts, list)
    assert len(posts) >= 1
    assert "poster_html" in posts[0]


def test_generate_posts_fallback_on_error(monkeypatch):
    def failing():
        raise RuntimeError("API down")
    monkeypatch.setattr('app.services.social_posts_gen.get_ai_client', failing)

    gen = SocialPostsGenerator()
    posts = gen.generate_posts("TestCo", "Tag", "professional")
    assert isinstance(posts, list)
    assert all("poster_html" in p for p in posts)
