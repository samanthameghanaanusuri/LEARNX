import urllib.request
import urllib.parse
import json
import uuid

BASE_URL = 'http://127.0.0.1:5000/api'

def post_json(url, data, headers=None):
    if headers is None: headers = {}
    headers['Content-Type'] = 'application/json'
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        print(e.read().decode())
        raise

def get_json(url, headers=None):
    if headers is None: headers = {}
    req = urllib.request.Request(url, headers=headers, method='GET')
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode())

def run_test():
    # 1. Register a new student
    username = f"testuser_{uuid.uuid4().hex[:8]}"
    email = f"{username}@example.com"
    password = "password123"

    print(f"Registering student {username}...")
    res = post_json(f"{BASE_URL}/auth/register", {
        "username": username,
        "email": email,
        "password": password
    })
    
    student_id = res['student']['id']
    headers = {'X-Student-ID': str(student_id)}
    print(f"Registered with student ID {student_id}")

    # 2. Get subjects and pick one
    res = get_json(f"{BASE_URL}/concepts/subjects")
    subjects = res.get('subjects', [])
    if not subjects:
        print("No subjects found.")
        return
    subject_id = subjects[0]['id']
    print(f"Using subject ID {subject_id}")

    # 3. Get assessment questions
    res = get_json(f"{BASE_URL}/assessments/subjects/{subject_id}/questions", headers=headers)
    concepts_questions = res.get('concepts_questions', {})
    
    answers = []
    for cid, cinfo in concepts_questions.items():
        for q in cinfo['questions']:
            # Provide wrong answers deliberately
            answers.append({
                "question_id": q['id'],
                "student_answer": "totally wrong answer 123"
            })
            
    if not answers:
        print("No questions found for subject.")
        return
        
    print(f"Submitting {len(answers)} wrong answers to trigger diagnosis...")
    res = post_json(f"{BASE_URL}/assessments/submit", {"answers": answers}, headers=headers)
    print("Submit Response Keys:", list(res.keys()))

    # 4. Check if Diagnosis was created via dashboard history API
    print("\nFetching diagnosis history...")
    res = get_json(f"{BASE_URL}/diagnosis/history", headers=headers)
    history = res.get('history', [])
    print(f"Found {len(history)} diagnoses.")
    if len(history) > 0:
        print("Latest Diagnosis:")
        print(json.dumps(history[0], indent=2))
        return "SUCCESS"
    else:
        print("FAILURE: No diagnosis found in history.")
        return "FAILURE"

if __name__ == '__main__':
    result = run_test()
    print("\nTest Result:", result)
