import os
import sqlite3
import time
import json
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

def get_java_lessons():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT id FROM course WHERE title LIKE '%Java Programming%' LIMIT 1")
    row = cur.fetchone()
    if not row:
        print("Java course not found.")
        return []
    course_id = row[0]
    
    cur.execute('''
        SELECT l.id, m.title, l.title, l.content, m.order_index, l.order_index
        FROM lesson l
        JOIN course_module m ON l.module_id = m.id
        WHERE m.course_id = ?
        ORDER BY m.order_index, l.order_index
    ''', (course_id,))
    lessons = cur.fetchall()
    conn.close()
    return lessons

def update_lesson_content(lesson_id, new_content):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("UPDATE lesson SET content = ? WHERE id = ?", (new_content, lesson_id))
    conn.commit()
    conn.close()

AUDIT_PROMPT = """
You are performing a STRICT CONCEPT AUDIT for a Java course curriculum.
The learner starts from absolute zero.

Module Topic: {module_title}
Lesson Title: {lesson_title}
Current Content:
{current_content}

IDENTIFY:
1. What concepts are currently taught in the text?
2. What GENUINELY RELEVANT foundational concepts, rules, execution flow, mistakes, and logic-building are MISSING for an absolute beginner learning this topic?

Do NOT write the lesson. Output exactly in this format:

[OLD CONCEPTS]
- ...

[MISSING RELEVANT CONCEPTS]
- ...
"""

GENERATE_PROMPT = """
You are a master Java teacher. Write the HTML content for this lesson.
The learner knows NOTHING about programming initially. Build understanding from first principles.

Module Topic: {module_title}
Lesson Title: {lesson_title}

Existing Content:
{current_content}

Concept Audit identifying what is missing:
{audit_text}

INSTRUCTIONS:
1. Write the new lesson in HTML format.
2. Teach deeply but use simple, beginner-friendly English.
3. Integrate the missing concepts identified in the audit.
4. For early modules, explain what programming is, how Java works, etc.
5. If the module is the Capstone Project, explain the architecture and synthesize previous knowledge. Do NOT force projects into early modules.
6. Include Code Examples, Dry Runs (step-by-step tracing), and Common Mistakes where applicable.
7. DO NOT use generic padding.
8. Output ONLY valid HTML for the lesson content. Do NOT include ```html markdown blocks.
9. Start with an <h3>{lesson_title}</h3> tag.
"""

VALIDATE_PROMPT = """
You are an independent educational validator.
Review the following NEW Java lesson content against the OLD content to ensure genuine concept expansion.

Old Content:
{current_content}

New Content:
{new_content}

Module Context: {module_title}
Lesson Title: {lesson_title}

EVALUATE:
1. Does it genuinely cover missing beginner sub-concepts?
2. Is it free from generic word-padding?
3. Does it explain code, execution flow, and mistakes properly where applicable?
4. Is it technically correct and free of unrelated advanced jargon?

Return ONLY the word "PASS" if it meets all quality criteria.
Return ONLY the word "REJECT" followed by a newline and the reason if it fails.
"""

def process_lessons():
    lessons = get_java_lessons()
    print(f"Total Java lessons found: {len(lessons)}")
    
    successful = 0
    skipped = 0
    failed = 0
    
    for l_id, m_title, l_title, content, m_idx, l_idx in lessons:
        if "<!-- V4_ENRICHED -->" in content:
            skipped += 1
            continue
            
        print(f"\\nProcessing Module {m_idx}, Lesson {l_idx}: {l_title}")
        
        try:
            # 1. Audit
            print("  -> Generating Audit...")
            audit_response = client.models.generate_content(
                model=model_name,
                contents=AUDIT_PROMPT.format(module_title=m_title, lesson_title=l_title, current_content=content)
            )
            audit_text = audit_response.text.strip()
            
            # 2. Generate
            print("  -> Generating Deep Content...")
            gen_response = client.models.generate_content(
                model=model_name,
                contents=GENERATE_PROMPT.format(module_title=m_title, lesson_title=l_title, current_content=content, audit_text=audit_text)
            )
            new_content = gen_response.text.strip()
            if new_content.startswith("```html"):
                new_content = new_content[7:]
            if new_content.endswith("```"):
                new_content = new_content[:-3]
            new_content = new_content.strip()
            
            # 3. Validate
            print("  -> Validating...")
            val_response = client.models.generate_content(
                model=model_name,
                contents=VALIDATE_PROMPT.format(module_title=m_title, lesson_title=l_title, current_content=content, new_content=new_content)
            )
            val_result = val_response.text.strip()
            
            if val_result.startswith("PASS"):
                new_content += "\\n<!-- V4_ENRICHED -->"
                update_lesson_content(l_id, new_content)
                print("  -> PASS & Saved.")
                successful += 1
            else:
                print(f"  -> REJECTED. Reason: {val_result}")
                failed += 1
                
            time.sleep(3) # Small delay to respect rate limits
            
        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                print("\\nRATE LIMIT (429) REACHED. Stopping safely.")
                break
            elif "503" in err_str:
                print(f"  -> ERROR 503 (High Demand). Skipping for now.")
                failed += 1
                time.sleep(5)
            else:
                print(f"  -> ERROR processing lesson {l_id}: {e}")
                failed += 1
                
    remaining = len(lessons) - (successful + skipped + failed)
    print("\\n--- JAVA CONTENT ENRICHMENT V4 REPORT ---")
    print(f"Total Java modules: {len(set([m for _, m, _, _, _, _ in lessons]))}")
    print(f"Total Java lessons: {len(lessons)}")
    print(f"Successfully enriched this run: {successful}")
    print(f"Already Enriched (Skipped): {skipped}")
    print(f"Rejected/Failed: {failed}")
    print(f"Remaining (Due to 429 limit): {remaining}")
    if remaining > 0:
        print("NOTE: Script stopped due to Gemini free tier quota. Run again later to resume.")

if __name__ == "__main__":
    process_lessons()
