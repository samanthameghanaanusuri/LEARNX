import json
import os

data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'web_courses_data.json')
with open(data_path, 'r', encoding='utf-8') as f:
    courses = json.load(f)

for c in courses:
    if c['subject'] == 'HTML':
        print(f"Course: {c['title']}")
        for m in c['modules']:
            print(f"  Module {m['order_index']}: {m['title']}")
            for l in m['lessons']:
                print(f"    Lesson: {l['title']}")
                print(f"      Examples: {len(l['examples'])}")
                print(f"      Exercises: {len(l['exercises'])}")
                print(f"      Quizzes: {len(l['quizzes'])}")
                print(f"      Project: {l['project']['title']}")
        break
