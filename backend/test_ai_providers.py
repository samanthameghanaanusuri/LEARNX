import unittest
import os
import json
from unittest.mock import patch, MagicMock

# Set mock env variables before importing
os.environ['AI_API_KEY'] = 'fake_gemini_key'
os.environ['OPENROUTER_API_KEY'] = 'fake_openrouter_key'

from app.services.ai_providers.manager import ProviderManager
from app.services.ai_providers.gemini_provider import GeminiProvider
from app.services.ai_providers.fallback_provider import OpenRouterProvider
import requests

class TestProviderManager(unittest.TestCase):
    def setUp(self):
        self.manager = ProviderManager()

    @patch('app.services.ai_providers.gemini_provider.GeminiProvider.generate')
    @patch('app.services.ai_providers.fallback_provider.OpenRouterProvider.generate')
    def test_gemini_success(self, mock_fallback_gen, mock_gemini_gen):
        # Setup mock return for Gemini
        mock_gemini_gen.return_value = '{"answer": "test", "concepts": ["test"], "difficulty": "test", "next_action": "test"}'
        
        result = self.manager.generate("test prompt", is_json=True)
        
        # Verify
        self.assertTrue(result["success"])
        self.assertEqual(result["answer"], "test")
        self.assertEqual(result["_provider_used"], "gemini")
        mock_gemini_gen.assert_called_once()
        mock_fallback_gen.assert_not_called()

    @patch('app.services.ai_providers.gemini_provider.GeminiProvider.generate')
    @patch('app.services.ai_providers.fallback_provider.OpenRouterProvider.generate')
    def test_gemini_429_triggers_fallback(self, mock_fallback_gen, mock_gemini_gen):
        # Setup mock exception for Gemini
        class FakeAPIError(Exception):
            code = 429
            message = "Quota exceeded"
            
        mock_gemini_gen.side_effect = FakeAPIError("Quota exceeded")
        mock_fallback_gen.return_value = '{"answer": "fallback test", "concepts": ["test"], "difficulty": "test", "next_action": "test"}'
        
        result = self.manager.generate("test prompt", is_json=True)
        
        # Verify
        self.assertTrue(result["success"])
        self.assertEqual(result["answer"], "fallback test")
        self.assertEqual(result["_provider_used"], "openrouter")
        mock_gemini_gen.assert_called_once()
        mock_fallback_gen.assert_called_once()

    @patch('app.services.ai_providers.gemini_provider.GeminiProvider.generate')
    @patch('app.services.ai_providers.fallback_provider.OpenRouterProvider.generate')
    def test_gemini_503_triggers_fallback(self, mock_fallback_gen, mock_gemini_gen):
        # Setup mock exception for Gemini
        class FakeAPIError(Exception):
            code = 503
            message = "Service Unavailable"
            
        mock_gemini_gen.side_effect = FakeAPIError("Service Unavailable")
        mock_fallback_gen.return_value = '{"answer": "fallback test 503", "concepts": ["test"], "difficulty": "test", "next_action": "test"}'
        
        result = self.manager.generate("test prompt", is_json=True)
        
        # Verify
        self.assertTrue(result["success"])
        self.assertEqual(result["answer"], "fallback test 503")
        self.assertEqual(result["_provider_used"], "openrouter")
        mock_gemini_gen.assert_called_once()
        mock_fallback_gen.assert_called_once()

    @patch('app.services.ai_providers.gemini_provider.GeminiProvider.generate')
    @patch('app.services.ai_providers.fallback_provider.OpenRouterProvider.generate')
    def test_both_providers_fail(self, mock_fallback_gen, mock_gemini_gen):
        class FakeAPIError(Exception):
            code = 429
            
        mock_gemini_gen.side_effect = FakeAPIError("Quota exceeded")
        mock_fallback_gen.side_effect = Exception("Fallback also failed")
        
        result = self.manager.generate("test prompt", is_json=True)
        
        # Verify
        self.assertFalse(result["success"])
        self.assertEqual(result["error_type"], "all_providers_unavailable")
        mock_gemini_gen.assert_called_once()
        mock_fallback_gen.assert_called_once()

    @patch('app.services.ai_providers.gemini_provider.GeminiProvider.generate')
    @patch('app.services.ai_providers.fallback_provider.OpenRouterProvider.generate')
    def test_invalid_request_no_fallback(self, mock_fallback_gen, mock_gemini_gen):
        class FakeAPIError(Exception):
            code = 400
            
        mock_gemini_gen.side_effect = FakeAPIError("Bad request")
        
        result = self.manager.generate("test prompt", is_json=True)
        
        # Verify
        self.assertFalse(result["success"])
        self.assertEqual(result["error_type"], "provider_error")
        mock_gemini_gen.assert_called_once()
        mock_fallback_gen.assert_not_called()

if __name__ == '__main__':
    unittest.main()
