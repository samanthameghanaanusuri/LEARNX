import os
import sqlite3
import time
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError
from requests.exceptions import ConnectionError, Timeout

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

def robust_generate(prompt, retries=5):
    delay = 15
    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )
            return response.text.strip()
        except (APIError, ConnectionError, Timeout) as e:
            err_str = str(e)
            if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                print(f"    [Rate Limit 429] Retrying in {delay}s...")
                time.sleep(delay)
                delay *= 2
            elif "503" in err_str or "500" in err_str or "502" in err_str:
                print(f"    [Server Error {err_str[:10]}] Retrying in {delay}s...")
                time.sleep(delay)
                delay *= 2
            else:
                print(f"    [Network/API Error] {err_str[:50]}. Retrying in {delay}s...")
                time.sleep(delay)
                delay *= 2
    return None

AUDIT_PROMPT = """
You are creating a strictly lesson-specific CONCEPT TREE for a Java curriculum.
Module: {module_title}
Lesson: {lesson_title}

Existing Content:
{current_content}

TASKS:
1. Identify the intended topic.
2. Build a complete topic-specific concept tree for an ABSOLUTE BEGINNER. 
   - If this is Module 1, you MUST start from hardware, software, programs, compiled vs interpreted, BEFORE syntax.
   - For other topics, list concepts sequentially (e.g. repetition -> loop condition -> while -> dry-run -> mistakes).
3. Identify which of these concepts are ALREADY COVERED.
4. Identify which are MISSING and MUST BE ADDED.

Format your output exactly as:
[INTENDED TOPIC]
...
[CONCEPT TREE]
...
[ALREADY COVERED]
...
[MISSING CONCEPTS]
...
"""

GENERATE_PROMPT = """
You are a master lecturer teaching Java to an absolute beginner.
Module: {module_title}
Lesson: {lesson_title}

Existing Content:
{current_content}

Concept Audit identifying missing concepts:
{audit_text}

INSTRUCTIONS:
1. Rewrite and expand the lesson deeply in HTML.
2. Teach the MISSING CONCEPTS identified in the audit.
3. For Module 1, teach from Absolute Zero (what is a computer, what is programming) before Java syntax.
4. For Module 30, preserve Advanced Architecture concepts and define an integrating Capstone Project. Do NOT create random projects in early modules.
5. Answer: WHAT is it? WHY do we need it? HOW does it work? HOW does it execute?
6. Include Code, Line-by-Line explanation, Dry Runs (execution trace), and Common Mistakes.
7. DO NOT use generic padding, motivational filler, or repetitive sentences. Use simple English.
8. Output ONLY valid HTML. Do not wrap in ```html. Start with <h3>{lesson_title}</h3>.
"""

VALIDATE_PROMPT = """
You are an independent educational validator.
Evaluate this NEW Java lesson against the OLD content and the required concept depth.

Old Content:
{current_content}

New Content:
{new_content}

Module: {module_title}
Lesson: {lesson_title}

CHECKLIST:
1. Are meaningful concepts/sub-concepts increased?
2. Is WHY and HOW actually explained?
3. Are examples, code reasoning, and dry-runs present where required?
4. Is it technically correct and free of early advanced jargon?
5. Is the English simple and suitable for a beginner?
6. Is it free of generic word-padding and repetition?

If ANY checklist item fails, return REJECT followed by the reason.
If it is a flawless, genuine, conceptual expansion, return ONLY the word PASS.
"""

def process_lessons():
    lessons = get_java_lessons()
    print(f"Total Java lessons found: {len(lessons)}")
    
    successful = 0
    skipped = 0
    failed = 0
    
    for l_id, m_title, l_title, content, m_idx, l_idx in lessons:
        if "<!-- V5_ENRICHED -->" in content:
            skipped += 1
            continue
            
        print(f"\\nProcessing M{m_idx} L{l_idx}: {l_title}")
        
        # 1. Audit
        print("  -> Phase 1: Internal Curriculum Audit...")
        audit_text = robust_generate(AUDIT_PROMPT.format(module_title=m_title, lesson_title=l_title, current_content=content))
        if not audit_text:
            print("  -> FAILED: Audit generation exhausted retries.")
            failed += 1
            continue
            
        # 2. Generate
        print("  -> Phase 2: Deep Teaching Generation...")
        new_content = robust_generate(GENERATE_PROMPT.format(module_title=m_title, lesson_title=l_title, current_content=content, audit_text=audit_text))
        if not new_content:
            print("  -> FAILED: Lesson generation exhausted retries.")
            failed += 1
            continue
            
        if new_content.startswith("```html"):
            new_content = new_content[7:]
        if new_content.endswith("```"):
            new_content = new_content[:-3]
        new_content = new_content.strip()
        
        # 3. Validate
        print("  -> Phase 3: Independent Validation...")
        val_result = robust_generate(VALIDATE_PROMPT.format(module_title=m_title, lesson_title=l_title, current_content=content, new_content=new_content))
        if not val_result:
            print("  -> FAILED: Validation exhausted retries.")
            failed += 1
            continue
            
        if val_result.strip().startswith("PASS"):
            new_content += "\\n<!-- V5_ENRICHED -->"
            update_lesson_content(l_id, new_content)
            print("  -> PASS & Saved.")
            successful += 1
        else:
            print(f"  -> REJECTED. Reason: {val_result.strip()}")
            failed += 1
            
        time.sleep(5)
                
    print("\\n--- JAVA CONTENT ENRICHMENT V5 REPORT ---")
    print(f"Total Modules: {len(set([m for _, m, _, _, _, _ in lessons]))}")
    print(f"Total Lessons: {len(lessons)}")
    print(f"Successfully enriched: {successful}")
    print(f"Skipped (Already Enriched): {skipped}")
    print(f"Rejected/Failed: {failed}")

if __name__ == "__main__":
    process_lessons()
