"""Centralized Groq AI client wrapper with retry logic."""

import time
import logging
from groq import Groq
from ..config import settings

logger = logging.getLogger(__name__)


class AIClient:
    """Singleton-like AI client for Groq API calls."""

    def __init__(self):
        if not settings.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not configured")
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        self.model = settings.GROQ_MODEL
        self.max_retries = 3
        self.base_delay = 1.0

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int = 2048,
        temperature: float = 0.7,
        retry_count: int = 0,
    ) -> str:
        """
        Generate content using Groq API with exponential backoff retry.

        Args:
            system_prompt: System message for the AI
            user_prompt: User message/query
            max_tokens: Maximum tokens in response
            temperature: Sampling temperature (0-1)
            retry_count: Current retry attempt (internal use)

        Returns:
            Generated text response

        Raises:
            Exception: If all retries are exhausted
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return response.choices[0].message.content

        except Exception as e:
            if retry_count < self.max_retries:
                delay = self.base_delay * (2**retry_count)
                logger.warning(
                    f"API call failed (attempt {retry_count + 1}/"
                    f"{self.max_retries}). Retrying in {delay}s: {e}"
                )
                time.sleep(delay)
                return self.generate(
                    system_prompt,
                    user_prompt,
                    max_tokens,
                    temperature,
                    retry_count + 1,
                )
            logger.error(f"API call failed after {self.max_retries} retries: {e}")
            raise


# Global instance (lazy-loaded)
_ai_client: AIClient | None = None


def get_ai_client() -> AIClient:
    """Get or create the global AI client instance."""
    global _ai_client
    if _ai_client is None:
        _ai_client = AIClient()
    return _ai_client
