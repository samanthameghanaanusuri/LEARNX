import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.environ.get('AI_API_KEY')
model_name = os.environ.get('AI_MODEL', 'gemini-2.5-flash')

print(f"Key loaded: {bool(api_key)}")
print(f"Model: {model_name}")

try:
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents="Explain what a Python variable is in one sentence."
    )
    print("SUCCESS!")
    print(response.text)
except Exception as e:
    import traceback
    print("FAILED!")
    traceback.print_exc()
