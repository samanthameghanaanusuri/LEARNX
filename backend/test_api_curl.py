import requests
import json
import sys

def run_tests():
    try:
        print("--- TEST B: GET /api/courses/ ---")
        r = requests.get("http://127.0.0.1:5000/api/courses/")
        print(f"Status: {r.status_code}")
        print(json.dumps(r.json(), indent=2)[:500] + "...\n")
        
        print("--- TEST C: GET /api/ai/status ---")
        r = requests.get("http://127.0.0.1:5000/api/ai/status")
        print(f"Status: {r.status_code}")
        print(json.dumps(r.json(), indent=2))
        print("\n")
        
        print("--- TEST F, G, H: POST /api/ai/ask with mock_429 ---")
        r = requests.post(
            "http://127.0.0.1:5000/api/ai/ask",
            json={"question": "What are python variables? mock_429", "course_id": 1, "lesson_id": 1},
            headers={"X-Student-ID": "1"}
        )
        print(f"Status: {r.status_code}")
        print(json.dumps(r.json(), indent=2))
        
    except Exception as e:
        print(f"Test script failed: {e}")

if __name__ == "__main__":
    run_tests()
