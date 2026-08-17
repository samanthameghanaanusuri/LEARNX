import os
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError

load_dotenv()
api_key = os.environ.get('AI_API_KEY')
model = os.environ.get('AI_MODEL', 'gemini-3.7-flash')

print(f"Configured: {bool(api_key)}")
print(f"Model: {model}")

try:
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=model,
        contents="Explain Python variables in one sentence."
    )
    print("Direct Gemini Test: SUCCESS")
    print("Response:", response.text)
except APIError as e:
    print(f"AI_DEBUG_PROVIDER_ERROR status={e.code} exception=APIError message={e.message}")
except Exception as e:
    print(f"AI_DEBUG_PROVIDER_ERROR status=unknown exception={type(e).__name__} message={str(e)}")
