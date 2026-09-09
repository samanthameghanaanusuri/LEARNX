import os
import sqlite3
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.environ.get('AI_API_KEY')
if not api_key:
    print("Error: AI_API_KEY not found in environment variables.")
    exit(1)

model_name = os.environ.get('AI_MODEL', 'gemini-3.7-flash')
client = genai.Client(api_key=api_key)
db_path = os.path.join(os.path.dirname(__file__), 'instance', 'learnx.db')
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT id FROM course WHERE title LIKE '%Java Programming%' LIMIT 1")
course_id = cur.fetchone()[0]

cur.execute("SELECT id FROM course_module WHERE course_id = ? ORDER BY order_index", (course_id,))
module_ids = [m[0] for m in cur.fetchall()]

placeholders = ','.join('?' * len(module_ids))
cur.execute(f"SELECT id, title, content FROM lesson WHERE module_id IN ({placeholders}) ORDER BY id LIMIT 3", module_ids)
lessons = cur.fetchall()

prompt_template = """
You are performing a CONCEPT AUDIT for a Java course lesson.
You are given the lesson title and the current shallow lesson content.

Identify:
1. What concepts are currently taught.
2. What GENUINELY RELEVANT core sub-concepts, syntax rules, dry runs, common mistakes, or logic building are MISSING for a complete beginner learning this exact topic.

Do not write the lesson. Just output the audit in this exact format:

[LESSON TOPIC]
(the topic)

[OLD CONCEPTS]
- ...

[MISSING RELEVANT CONCEPTS]
- ...

[MISSING RULES]
- ...

[MISSING EXAMPLES]
- ...

[MISSING TRACING]
- ...

[MISSING COMMON MISTAKES]
- ...

[MISSING LOGIC BUILDING]
- ...

LESSON TITLE: {title}
CURRENT CONTENT: {content}
"""

with open("audit_results.md", "w", encoding="utf-8") as f:
    f.write("# Java Course Concept Audit (First 3 Lessons)\\n\\n")
    
    for lesson_id, title, content in lessons:
        print(f"Auditing Lesson ID {lesson_id}: {title}...")
        prompt = prompt_template.format(title=title, content=content)
        
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )
            audit_result = response.text.strip()
            f.write(f"## Lesson: {title}\\n\\n")
            f.write(f"{audit_result}\\n\\n---\\n\\n")
            print("Done.")
            time.sleep(2)
        except Exception as e:
            print(f"Error: {e}")

conn.close()
print("Audit saved to audit_results.md")
