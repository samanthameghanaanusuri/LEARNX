import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get('AI_API_KEY')

client = genai.Client(api_key=api_key)
for model in client.models.list():
    if "generateContent" in model.supported_generation_methods:
        print(model.name)
