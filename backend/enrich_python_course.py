import os
import sqlite3
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.environ.get('AI_API_KEY')
if not api_key:
    print("Error: AI_API_KEY not found in environment variables.")
    exit(1)

model_name = os.environ.get('AI_MODEL', 'gemini-2.5-flash')
print(f"Using Model: {model_name}")

client = genai.Client(api_key=api_key)
db_path = os.path.join(os.path.dirname(__file__), 'instance', 'learnx.db')
print(f"Connecting to DB: {db_path}")
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Get Python Course ID (usually 1, but we can verify)
cur.execute("SELECT id FROM course WHERE title LIKE 'Python Programming%' LIMIT 1")
course_id_row = cur.fetchone()
if not course_id_row:
    print("Python course not found in database!")
    exit(1)
course_id = course_id_row[0]
print(f"Found Python Course ID: {course_id}")

# Fetch all modules for this course
cur.execute("SELECT id, title FROM course_module WHERE course_id = ? ORDER BY order_index", (course_id,))
modules = cur.fetchall()
print(f"Found {len(modules)} modules for Python course.")

if len(modules) != 15:
    print(f"WARNING: Expected exactly 15 modules, but found {len(modules)}.")

# Get all lessons for these modules
# We only want to enrich the main theory lessons, not necessarily the Practice & Knowledge Check if they are just placeholders,
# but the prompt says to enrich existing lesson content. We will apply it to all lessons that have substantial theory.
# We'll just enrich all lessons under the python course modules.
module_ids = [m[0] for m in modules]
placeholders = ','.join('?' * len(module_ids))
cur.execute(f"SELECT id, title, content FROM lesson WHERE module_id IN ({placeholders}) ORDER BY id", module_ids)
lessons = cur.fetchall()
print(f"Found {len(lessons)} lessons to process.")

prompt_template = """
You are an expert Python lecturer writing course content for a complete beginner.
You are given the title and current shallow content of a Python lesson.
Your task is to REWRITE and DEEPLY EXPAND this content into a rich, beginner-friendly format.

STRICT RULES:
1. ONLY return the HTML content. Do not include markdown codeblocks like ```html. Start directly with HTML tags.
2. The tone must be simple English, conversational, but technically accurate.
3. You must use the following structure (A through S) wherever applicable to the topic:
   - A. What is it? (Simple definition)
   - B. Why do we need it? (What problem it solves)
   - C. Real-life analogy
   - D. How does it work?
   - E. Simple syntax
   - F. Basic example (with code)
   - G. Practical example (with code)
   - H. Code explanation (step-by-step for the example)
   - I. Execution flow (what happens line-by-line when run)
   - J. Expected Output
   - K. Why that output occurs
   - L. Common beginner mistakes
   - M. Important rules
   - N. How to recognize it in code
   - O. How to use it in a problem
   - P. Logic building (Problem -> What do we know -> What do we need -> Logic -> Code)
   - Q. Connection with previously learned concepts
   - R. Quick recap
4. DO NOT change the topic. Stick strictly to the lesson title and the existing content's original intent.
5. If the existing content is just a 'Practice & Knowledge Check' placeholder or just says 'Assessment Workspace', expand it slightly to explain what the student should be practicing based on the module title, but you don't need the full A-S structure for a practice workspace. Just make it encouraging and educational.

LESSON TITLE: {title}

CURRENT CONTENT:
{content}

NEW EXPANDED HTML CONTENT:
"""

success_count = 0
for lesson_id, title, content in lessons:
    print(f"\\nProcessing Lesson ID {lesson_id}: {title}")
    
    # Check if we should skip
    if content and "<h3>A. What is it?</h3>" in content:
        print("  -> Already enriched. Skipping.")
        success_count += 1
        continue
        
    prompt = prompt_template.format(title=title, content=content)
    
    try:
        response = client.models.generate_content(
            model="gemini-3.7-flash",
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
            
        if len(new_content) < len(content) and not "Practice" in title:
            print("  -> WARNING: Generated content is shorter than original. Skipping update.")
            continue
            
        # Update database
        cur.execute("UPDATE lesson SET content = ? WHERE id = ?", (new_content, lesson_id))
        conn.commit()
        print("  -> Successfully enriched and saved!")
        success_count += 1
        
        # small delay to prevent rate limits
        time.sleep(2)
        
    except Exception as e:
        print(f"  -> ERROR processing lesson {lesson_id}: {e}")

print(f"\\nFinished processing. {success_count}/{len(lessons)} lessons successfully enriched.")
conn.close()
