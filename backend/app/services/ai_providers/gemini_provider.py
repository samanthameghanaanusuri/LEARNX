import os
import json
import time
import logging
import requests
from .base import BaseAIProvider

logger = logging.getLogger(__name__)

class GeminiProvider(BaseAIProvider):
    def __init__(self):
        self.api_key = os.environ.get('AI_API_KEY')
        self.model = os.environ.get('AI_MODEL', 'gemini-1.5-flash')
        
    def is_configured(self) -> bool:
        return bool(self.api_key)

    def generate(self, prompt: str, system_instruction: str = None) -> str:
        if not self.api_key:
            raise RuntimeError("Gemini AI is not configured (missing AI_API_KEY).")
            
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"
        headers = {"Content-Type": "application/json"}
        
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.7}
        }
        if system_instruction:
            payload["systemInstruction"] = {"parts": [{"text": system_instruction}]}
            
        try:
            t0 = time.time()
            response = requests.post(url, headers=headers, json=payload, timeout=12.0)
            response.raise_for_status()
            data = response.json()
            t1 = time.time()
            logger.info(f'[LATENCY] Gemini API call: {(t1-t0)*1000:.2f}ms')
            
            # Extract text
            try:
                return data["candidates"][0]["content"]["parts"][0]["text"]
            except (KeyError, IndexError):
                raise RuntimeError(f"Unexpected response structure from Gemini: {data}")
                
        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code
            error_text = e.response.text
            raise RuntimeError(f"Gemini API error (Status {status_code}): {error_text}") from e
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Gemini connection error: {e}") from e

    def get_provider_name(self) -> str:
        return "gemini"

    def get_model_name(self) -> str:
        return self.model


