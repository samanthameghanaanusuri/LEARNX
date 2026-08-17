import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get('AI_API_KEY')
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
try:
    resp = requests.get(url)
    data = resp.json()
    if 'models' in data:
        for m in data['models']:
            if 'generateContent' in m.get('supportedGenerationMethods', []):
                print(m['name'])
    else:
        print("Response:", data)
except Exception as e:
    print("Error:", e)
