import os
import logging
from google import genai
from google.genai import types
from .base import BaseAIProvider

logger = logging.getLogger(__name__)

class GeminiProvider(BaseAIProvider):
    def __init__(self):
        self.api_key = os.environ.get('AI_API_KEY')
        self.model = os.environ.get('AI_MODEL', 'gemini-3.7-flash')
        self.client = None
        
        if self.api_key:
            try:
                self.client = genai.Client(api_key=self.api_key, http_options={'timeout': 15.0})
            except Exception as e:
                logger.exception("Gemini AI request failed during initialization")

    def is_configured(self) -> bool:
        return self.client is not None

    def generate(self, prompt: str, system_instruction: str = None) -> str:
        if not self.client:
            raise RuntimeError("Gemini AI is not configured (missing AI_API_KEY).")
            
        config = types.GenerateContentConfig(
            temperature=0.7
        )
        if system_instruction:
            config.system_instruction = system_instruction
            
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=config
            )
            return response.text
        except Exception as e:
            # We raise the raw exception to let the ProviderManager classify it
            raise e

    def get_provider_name(self) -> str:
        return "gemini"

    def get_model_name(self) -> str:
        return self.model
