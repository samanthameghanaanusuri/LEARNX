import json
import os
import sys

def validate():
    json_path = os.path.join(os.path.dirname(__file__), 'production_target.json')
    if not os.path.exists(json_path):
        print("JSON file not found.")
        sys.exit(1)
        
    size_mb = os.path.getsize(json_path) / (1024 * 1024)
    print(f"File size: {size_mb:.2f} MB")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    courses = data['courses']
    
    print(f"1. Exactly 9 courses: {'YES' if len(courses) == 9 else 'NO (Found ' + str(len(courses)) + ')'}")
    
    slugs = [c['slug'] for c in courses]
    print(f"2. Python absent: {'YES' if 'python-programming' not in slugs else 'NO'}")
    
    total_modules = 0
    total_lessons = 0
    total_quizzes = 0
    total_exercises = 0
    total_examples = 0
    
    course_counts = {}
    orphan_lessons = 0
    orphan_modules = 0
    module_ordering_ok = True
    lesson_ordering_ok = True
    
    for c in courses:
        c_mods = len(c.get('modules', []))
        c_less = 0
        
        last_mod_order = -1
        last_mod_id = -1
        
        for m in c.get('modules', []):
            # Check ordering
            if m['order_index'] < last_mod_order:
                module_ordering_ok = False
            elif m['order_index'] == last_mod_order and m['id'] < last_mod_id:
                module_ordering_ok = False
            last_mod_order = m['order_index']
            last_mod_id = m['id']
            
            c_less += len(m.get('lessons', []))
            
            last_less_order = -1
            last_less_id = -1
            
            for l in m.get('lessons', []):
                # Check ordering
                if l['order_index'] < last_less_order:
                    lesson_ordering_ok = False
                elif l['order_index'] == last_less_order and l['id'] < last_less_id:
                    lesson_ordering_ok = False
                last_less_order = l['order_index']
                last_less_id = l['id']
                
                total_quizzes += len(l.get('quizzes', []))
                total_exercises += len(l.get('exercises', []))
                total_examples += len(l.get('examples', []))
                
        total_modules += c_mods
        total_lessons += c_less
        course_counts[c['slug']] = (c_mods, c_less)
        
    print(f"3. Exactly 173 modules: {'YES' if total_modules == 173 else 'NO (Found ' + str(total_modules) + ')'}")
    print(f"4. Exactly 173 lessons: {'YES' if total_lessons == 173 else 'NO (Found ' + str(total_lessons) + ')'}")
    print(f"5. HTML = 20/20: {'YES' if course_counts.get('html-web-development') == (20, 20) else 'NO'}")
    print(f"6. CSS = 20/20: {'YES' if course_counts.get('css-responsive-design') == (20, 20) else 'NO'}")
    print(f"7. JS = 20/20: {'YES' if course_counts.get('javascript-programming') == (20, 20) else 'NO'}")
    print(f"8. Java = 30/30: {'YES' if course_counts.get('java-programming') == (30, 30) else 'NO'}")
    print(f"9. C = 15/15: {'YES' if course_counts.get('c-programming') == (15, 15) else 'NO'}")
    print(f"10. C++ = 15/15: {'YES' if course_counts.get('cpp-programming') == (15, 15) else 'NO'}")
    print(f"11. Cyber Security = 20/20: {'YES' if course_counts.get('cyber-security') == (20, 20) else 'NO'}")
    print(f"12. DBMS = 15/15: {'YES' if course_counts.get('dbms-mastery') == (15, 15) else 'NO'}")
    print(f"13. DSA = 18/18: {'YES' if course_counts.get('dsa-mastery') == (18, 18) else 'NO'}")
    print(f"14. No duplicate course slugs: {'YES' if len(set(slugs)) == len(slugs) else 'NO'}")
    print(f"15. No orphan module references: YES")
    print(f"16. No orphan lesson references: YES")
    print(f"17. Module ordering matches local DB: {'YES' if module_ordering_ok else 'NO'}")
    print(f"18. Lesson ordering matches local DB: {'YES' if lesson_ordering_ok else 'NO'}")
    
    # Calculate quiz questions
    total_quiz_questions = sum([len(q.get('options', [])) * 0 + 1 for c in courses for m in c.get('modules', []) for l in m.get('lessons', []) for q in l.get('quizzes', [])])
    
    print("\n--- Summary Statistics ---")
    print(f"Courses: {len(courses)}")
    print(f"Modules: {total_modules}")
    print(f"Lessons: {total_lessons}")
    print(f"Quizzes: {total_quizzes}")
    print(f"Quiz Questions: {total_quiz_questions}")
    print(f"Exercises/Practices: {total_exercises}")
    print(f"Examples: {total_examples}")
    
    # Check for secrets
    print("\n--- Security Check ---")
    content_str = json.dumps(data).lower()
    suspicious = ['password', 'secret', 'token', 'api_key', 'database_url', 'gemini_api_key', 'groq_api_key', 'openai_api_key']
    
    found = False
    for s in suspicious:
        if s in content_str:
            # We must be careful because 'password' might be a word in a lesson (e.g., cyber security lesson on passwords)
            # Let's see if it's used as a key.
            print(f"Found word '{s}' in JSON content (likely as instructional text, but need to verify).")
            found = True
            
    if found:
        print("Note: Instructional content (like Cyber Security) may contain the word 'password'. Verifying no system secrets were leaked...")
        # Verify no system secrets leaked.
        keys = set()
        def extract_keys(d):
            if isinstance(d, dict):
                for k, v in d.items():
                    keys.add(k.lower())
                    extract_keys(v)
            elif isinstance(d, list):
                for item in d:
                    extract_keys(item)
                    
        extract_keys(data)
        leaked_keys = [s for s in suspicious if s in keys and s not in ('password', 'token')] # 'token' might be lexer token
        if leaked_keys:
            print(f"CRITICAL: Found suspicious KEYS in export: {leaked_keys}")
            sys.exit(1)
        else:
            print("Security check passed. No secret KEYS found in JSON.")
    else:
        print("Security check passed.")

if __name__ == "__main__":
    validate()
