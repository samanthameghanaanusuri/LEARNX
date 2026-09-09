import os
import sqlite3
import time
import traceback
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.environ.get('AI_API_KEY')
if not api_key:
    print("Error: AI_API_KEY not found in environment variables.")
    exit(1)

model_name = os.environ.get('AI_MODEL', 'gemini-3.7-flash')
print(f"Using Model: {model_name}")

client = genai.Client(api_key=api_key)
db_path = os.path.join(os.path.dirname(__file__), 'instance', 'learnx.db')
print(f"Connecting to DB: {db_path}")
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Get Java Course ID
cur.execute("SELECT id FROM course WHERE title LIKE '%Java Programming%' LIMIT 1")
course_id_row = cur.fetchone()
if not course_id_row:
    print("Java course not found in database!")
    exit(1)
course_id = course_id_row[0]
print(f"Found Java Course ID: {course_id}")

# Fetch all modules for this course
cur.execute("SELECT id, title FROM course_module WHERE course_id = ? ORDER BY order_index", (course_id,))
modules = cur.fetchall()
print(f"Found {len(modules)} modules for Java course.")

if len(modules) != 30:
    print(f"WARNING: Expected exactly 30 modules, but found {len(modules)}.")

module_ids = [m[0] for m in modules]
placeholders = ','.join('?' * len(module_ids))
cur.execute(f"SELECT id, title, content FROM lesson WHERE module_id IN ({placeholders}) ORDER BY id", module_ids)
lessons = cur.fetchall()
print(f"Found {len(lessons)} lessons to process.")

prompt_template = """
You are an expert Java lecturer teaching a complete beginner.
You are given the title and current shallow content of a Java lesson.
Your task is to REWRITE and DEEPLY EXPAND this content into a rich, beginner-friendly format.

STRICT RULES:
1. ONLY return the HTML content. Do not include markdown codeblocks like ```html. Start directly with HTML tags.
2. The tone must be simple English, conversational, but technically accurate.
3. You must use the following structure (1-19) wherever applicable to the topic:
   - 1. What is it? (Simple definition)
   - 2. Why do we need it? (What problem it solves)
   - 3. Real-life analogy
   - 4. How does it work?
   - 5. Simple syntax
   - 6. Basic example (with code)
   - 7. Practical example (with code)
   - 8. Code explanation (step-by-step for the example)
   - 9. Execution flow (what happens line-by-line when run)
   - 10. Expected Output
   - 11. Why that output occurs
   - 12. Common beginner mistakes
   - 13. Important rules
   - 14. How to recognize it in code
   - 15. How to use it in a problem
   - 16. Logic building (Problem -> What do we know -> What do we need -> Logic -> Code)
   - 17. Connection with previously learned concepts
   - 18. Quick recap
4. DO NOT change the topic. Stick strictly to the Java lesson title and the existing content's original intent.
5. If the existing content is just a 'Practice & Knowledge Check' placeholder, expand it slightly to explain what the student should be practicing based on the module title. Do not force the full 19-point structure for a practice workspace. Make it encouraging and educational.
6. Never dump code without explaining it.

LESSON TITLE: {title}

CURRENT CONTENT:
{content}

NEW EXPANDED HTML CONTENT:
"""

success_count = 0
skipped_count = 0
error_count = 0
rate_limited = False

for lesson_id, title, content in lessons:
    print(f"\\nProcessing Lesson ID {lesson_id}: {title}")
    
    # Check if we should skip
    if content and ("What is it?" in content or "Why do we need it?" in content):
        print("  -> Already enriched. Skipping.")
        skipped_count += 1
        continue
        
    prompt = prompt_template.format(title=title, content=content)
    
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        new_content = response.text.strip()
        
        # Remove potential markdown wrappers
        if new_content.startswith("```html"):
            new_content = new_content[7:]
        if new_content.startswith("```"):
            new_content = new_content[3:]
        if new_content.endswith("```"):
            new_content = new_content[:-3]
        new_content = new_content.strip()
            
        # Validation checks
        if len(new_content) < len(content) and "Practice" not in title:
            print("  -> WARNING: Generated content is shorter than original. Skipping update.")
            continue
            
        if not new_content:
            print("  -> WARNING: Generated content is empty. Skipping update.")
            continue
            
        # Update database
        cur.execute("UPDATE lesson SET content = ? WHERE id = ?", (new_content, lesson_id))
        conn.commit()
        print("  -> Successfully enriched and saved!")
        success_count += 1
        
        # Delay to prevent rapid rate limit hits
        time.sleep(2)
        
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg or "quota" in error_msg.lower():
            print(f"  -> RATE LIMIT (429) REACHED. Stopping safely.")
            rate_limited = True
            break
        else:
            print(f"  -> ERROR processing lesson {lesson_id}: {error_msg}")
            error_count += 1

print("\\n--- ENRICHMENT SUMMARY ---")
print(f"Successfully Enriched: {success_count}")
print(f"Already Enriched (Skipped): {skipped_count}")
print(f"Errors (excluding 429): {error_count}")

remaining = len(lessons) - (success_count + skipped_count)
print(f"Remaining Lessons to Process Later: {remaining}")

if rate_limited:
    print("NOTE: Script stopped due to Gemini free tier quota. Run again later to resume.")

conn.close()
