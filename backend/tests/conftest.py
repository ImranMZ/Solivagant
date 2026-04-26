"""
Pytest configuration and shared fixtures for backend tests.
"""

import pytest
from unittest.mock import MagicMock, patch
import sys
import os

# Ensure the app module is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


@pytest.fixture
def mock_ai_client():
    """Mock AI client that returns predictable responses."""
    mock = MagicMock()
    mock.generate.return_value = "Mock AI response"
    return mock


@pytest.fixture
def mock_groq():
    """Patch the Groq client import at the module level."""
    with patch('app.core.ai_client.Groq') as mock_groq_class:
        mock_instance = MagicMock()
        mock_groq_class.return_value = mock_instance

        # Mock the chat.completions.create response
        mock_response = MagicMock()
        mock_message = MagicMock()
        mock_message.content = '{"mock": "response"}'
        mock_response.choices = [MagicMock(message=mock_message)]
        mock_instance.chat.completions.create.return_value = mock_response

        yield mock_groq_class, mock_instance


@pytest.fixture
def client():
    """FastAPI test client."""
    from fastapi.testclient import TestClient
    from app.main import app
    return TestClient(app)
