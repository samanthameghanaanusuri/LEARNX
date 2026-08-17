import os
import json
import logging
import requests
from .base import BaseAIProvider

logger = logging.getLogger(__name__)

class OpenRouterProvider(BaseAIProvider):
    def __init__(self):
        self.api_key = os.environ.get('OPENROUTER_API_KEY')
        self.model = os.environ.get('OPENROUTER_MODEL', 'openai/gpt-4o-mini')

    def is_configured(self) -> bool:
        return bool(self.api_key)

    def generate(self, prompt: str, system_instruction: str = None) -> str:
        if not self.api_key:
            raise RuntimeError("OpenRouter AI is not configured (missing OPENROUTER_API_KEY).")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://learnx.com", # Required by OpenRouter
            "X-Title": "LEARNX"
        }

        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
            
        messages.append({"role": "user", "content": prompt})

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7
        }

        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=15
            )
            
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
            
        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code
            error_text = e.response.text
            # We raise a RuntimeError with the status code embedded, or just raise it.
            # ProviderManager needs to know it's a provider error.
            raise RuntimeError(f"OpenRouter API error (Status {status_code}): {error_text}") from e
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"OpenRouter connection error: {e}") from e

    def get_provider_name(self) -> str:
        return "openrouter"

    def get_model_name(self) -> str:
        return self.model
