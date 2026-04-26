"""
Unit tests for LogoGenerator service.
"""

import pytest
from app.services.logo_gen import LogoGenerator


def test_generate_logo_svg_returns_svg(mock_ai_client, monkeypatch):
    # Patch the AI client used inside LogoGenerator
    monkeypatch.setattr('app.services.logo_gen.get_ai_client', lambda: mock_ai_client)

    # Mock AI response to include an SVG block
    mock_ai_client.generate.return_value = """
    ```svg
    <svg viewBox=\"0 0 400 400\"><rect width=\"400\" height=\"400\" fill=\"#fff\"/></svg>
    ```
    """

    gen = LogoGenerator()
    svg = gen.generate_logo_svg("TestCo", "Tech", "minimalist")
    assert "<svg" in svg
    assert "viewBox=\"0 0 400 400\"" in svg


def test_get_logo_data_url_encodes_svg(mock_ai_client, monkeypatch):
    monkeypatch.setattr('app.services.logo_gen.get_ai_client', lambda: mock_ai_client)
    mock_ai_client.generate.return_value = """
    ```svg
    <svg viewBox=\"0 0 400 400\"><rect width=\"400\" height=\"400\" fill=\"#fff\"/></svg>
    ```
    """
    gen = LogoGenerator()
    data_url = gen.get_logo_data_url("TestCo", "Tech")
    assert data_url.startswith("data:image/svg+xml;base64,")
    # Decode to ensure it's the same SVG content
    import base64
    svg_bytes = base64.b64decode(data_url.split(",")[1])
    assert b"<svg" in svg_bytes
