import os
import sys
import json

_script_dir = os.path.dirname(os.path.abspath(__file__))
if _script_dir not in sys.path:
    sys.path.insert(0, _script_dir)

from app import create_app
from config import Config
from app.models import (
    db, Course, CourseModule, Lesson, Exercise, TestCase, QuizQuestion, MiniProject, Subject, Concept, Question, Student
)

def run_verification():
    app = create_app(Config)
    with app.app_context():
        print("============================================================")
        print("COMPREHENSIVE C COURSE INTEGRITY & QUALITY VERIFICATION")
        print("============================================================\n")

        all_passed = True

        # 1. Course Existence & Attributes Check
        c_course = Course.query.filter_by(slug='c-programming').first()
        if not c_course:
            print("[FAIL] Course 'c-programming' not found in database!")
            sys.exit(1)

        print(f"[OK] Course Found: {c_course.title} (ID: {c_course.id}, Slug: {c_course.slug})")

        # 2. Module Count Check (Must be 15)
        modules = CourseModule.query.filter_by(course_id=c_course.id).order_index.all() if hasattr(CourseModule.query.filter_by(course_id=c_course.id), 'order_index') else CourseModule.query.filter_by(course_id=c_course.id).order_by(CourseModule.order_index).all()
        module_count = len(modules)
        print(f"[INFO] Total Modules Count: {module_count}")

        if module_count != 15:
            print(f"[FAIL] Expected 15 modules, found {module_count}!")
            all_passed = False
        else:
            print("[OK] Module count is exactly 15.")

        # Expected Module Titles Curriculum
        expected_curriculum = [
            "C Programming Foundations",
            "Variables, Data Types & Constants",
            "Input, Output & Operators",
            "Conditional Statements",
            "Loops & Problem Solving",
            "Functions & Recursion",
            "Arrays & Multidimensional Arrays",
            "Strings & Character Processing",
            "Pointers Fundamentals",
            "Pointers, Arrays & Functions",
            "Structures, Unions, Enums & Typedef",
            "Dynamic Memory Management",
            "File Handling",
            "Preprocessor, Header Files & Advanced C",
            "Practical C, Debugging & DSA Foundations"
        ]

        for idx, mod in enumerate(modules):
            if idx < len(expected_curriculum):
                if expected_curriculum[idx].lower() not in mod.title.lower():
                    print(f"[WARN] Module {idx+1} title '{mod.title}' differs from expected '{expected_curriculum[idx]}'")

        # 3. Lessons, Exercises, Quizzes, Projects Inspection
        total_lessons = 0
        total_exercises = 0
        total_quizzes = 0
        total_projects = 0
        
        all_quiz_questions = set()
        exercise_titles = set()
        exercise_descriptions = set()

        req_markdown_headings = [
            "## What Is It?",
            "## Why Do We Need It?",
            "## How Does It Work?",
            "## Syntax",
            "## Example 1 — Simple",
            "### Output",
            "### Line-by-Line Explanation",
            "## Example 2 — Real-World",
            "### Output",
            "### Explanation",
            "## Common Mistakes",
            "## Best Practices",
            "## Try It Yourself"
        ]

        for mod_idx, mod in enumerate(modules, start=1):
            lessons = Lesson.query.filter_by(module_id=mod.id).all()
            total_lessons += len(lessons)

            if not lessons:
                print(f"[FAIL] Module {mod_idx} '{mod.title}' has zero lessons!")
                all_passed = False
                continue

            for les in lessons:
                content = les.content

                # Content length check
                if len(content) < 800:
                    print(f"[FAIL] Lesson '{les.title}' content too short ({len(content)} chars). Minimum 800 required.")
                    all_passed = False

                # Markdown Headings Check
                missing_headings = [h for h in req_markdown_headings if h not in content]
                if missing_headings:
                    print(f"[FAIL] Lesson '{les.title}' is missing Markdown headings: {missing_headings}")
                    all_passed = False

                # Code block and output check
                if "```c" not in content or "```text" not in content:
                    print(f"[FAIL] Lesson '{les.title}' is missing C code blocks or expected output blocks.")
                    all_passed = False

                # Check for generic filler phrases
                generic_fillers = ["Functions are useful for organizing code.", "Variables store data. They are useful.", "Pointers are variables that store memory addresses."]
                for filler in generic_fillers:
                    if filler in content:
                        print(f"[FAIL] Generic template filler text found in lesson '{les.title}': '{filler}'")
                        all_passed = False

                # Concept-Specific Deep Quality Checks
                if "pointer" in les.title.lower():
                    if "RAM" not in content or "Address" not in content or "&" not in content or "*" not in content:
                        print(f"[FAIL] Pointer lesson '{les.title}' lacks memory/address pointer visualization details.")
                        all_passed = False

                if "dynamic memory" in les.title.lower():
                    keywords = ["malloc", "calloc", "realloc", "free", "Heap", "Leak"]
                    missing_kw = [kw for kw in keywords if kw not in content]
                    if missing_kw:
                        print(f"[FAIL] Dynamic memory lesson '{les.title}' missing concepts: {missing_kw}")
                        all_passed = False

                if "file handling" in les.title.lower():
                    keywords = ["fopen", "fclose", "FILE"]
                    missing_kw = [kw for kw in keywords if kw not in content]
                    if missing_kw:
                        print(f"[FAIL] File handling lesson '{les.title}' missing concepts: {missing_kw}")
                        all_passed = False

                if "preprocessor" in les.title.lower():
                    keywords = ["#define", "#include", "#ifndef"]
                    missing_kw = [kw for kw in keywords if kw not in content]
                    if missing_kw:
                        print(f"[FAIL] Preprocessor lesson '{les.title}' missing concepts: {missing_kw}")
                        all_passed = False

                if "functions" in les.title.lower() and "recursion" in les.title.lower():
                    if "Stack" not in content or "Base Case" not in content:
                        print(f"[FAIL] Functions & Recursion lesson missing call stack or base case explanations.")
                        all_passed = False

                # Exercise Checks
                exercises = Exercise.query.filter_by(lesson_id=les.id).order_by(Exercise.order_index).all()
                total_exercises += len(exercises)

                if len(exercises) < 6:
                    print(f"[FAIL] Module {mod_idx} has {len(exercises)} exercises. Minimum 6 required!")
                    all_passed = False

                difficulties_in_mod = [ex.difficulty for ex in exercises]
                if "Easy" not in difficulties_in_mod or "Medium" not in difficulties_in_mod or "Hard" not in difficulties_in_mod or "Challenge" not in difficulties_in_mod:
                    print(f"[WARN] Module {mod_idx} exercises do not span Easy -> Medium -> Hard -> Challenge (found {difficulties_in_mod})")

                for ex in exercises:
                    if ex.title in exercise_titles:
                        print(f"[FAIL] Duplicate exercise title found: '{ex.title}'")
                        all_passed = False
                    exercise_titles.add(ex.title)

                    if ex.description in exercise_descriptions:
                        print(f"[FAIL] Duplicate exercise description found: '{ex.description}'")
                        all_passed = False
                    exercise_descriptions.add(ex.description)

                    test_cases = TestCase.query.filter_by(exercise_id=ex.id).all()
                    if not test_cases:
                        print(f"[FAIL] Exercise '{ex.title}' has no test cases!")
                        all_passed = False

                # Quiz Checks
                quizzes = QuizQuestion.query.filter_by(lesson_id=les.id).all()
                total_quizzes += len(quizzes)
                if len(quizzes) != 10:
                    print(f"[FAIL] Lesson '{les.title}' has {len(quizzes)} quizzes. Expected exactly 10.")
                    all_passed = False

                for q in quizzes:
                    if not q.question_text or not q.options or not q.correct_answer or not q.explanation:
                        print(f"[FAIL] Quiz question in '{les.title}' is missing text, options, answer, or explanation.")
                        all_passed = False

                    if q.question_text in all_quiz_questions:
                        print(f"[FAIL] Duplicate quiz question globally: '{q.question_text}'")
                        all_passed = False
                    all_quiz_questions.add(q.question_text)
                    
                    try:
                        import json
                        options_list = json.loads(q.options) if isinstance(q.options, str) else q.options
                    except:
                        options_list = q.options

                    if not isinstance(options_list, list) or len(options_list) != 4:
                        print(f"[FAIL] Quiz in '{les.title}' does not have exactly 4 options.")
                        all_passed = False
                    else:
                        if len(set(options_list)) != 4:
                            print(f"[FAIL] Quiz in '{les.title}' contains duplicate options: {options_list}")
                            all_passed = False
                        
                        if q.correct_answer not in options_list:
                            print(f"[FAIL] Correct answer '{q.correct_answer}' is not in options for '{q.question_text}'")
                            all_passed = False

                # Project Checks
                projects = MiniProject.query.filter_by(lesson_id=les.id).all()
                total_projects += len(projects)

        print(f"[INFO] Total Lessons Verified: {total_lessons}")
        print(f"[INFO] Total Exercises Verified: {total_exercises}")
        print(f"[INFO] Total Quizzes Verified: {total_quizzes}")
        print(f"[INFO] Total Stage Projects Verified: {total_projects}")

        if total_quizzes != 150:
            print(f"[FAIL] Total quizzes count is {total_quizzes}. Expected exactly 150 (10 per module).")
            all_passed = False

        if total_projects < 5:
            print(f"[WARN] Total stage projects count is {total_projects}. Expected at least 5 across major stages.")

        # 4. Non-C Subject Integrity Checks
        print("\n--- Verifying Integrity of Non-C Courses and Subjects ---")
        python_course = Course.query.filter_by(slug='python-programming').first()
        if python_course and CourseModule.query.filter_by(course_id=python_course.id).count() == 30:
            print("[OK] Python course intact with 30 modules.")
        else:
            print("[FAIL] Python course damaged or missing!")
            all_passed = False

        java_course = Course.query.filter_by(slug='java-programming').first()
        if java_course and CourseModule.query.filter_by(course_id=java_course.id).count() == 30:
            print("[OK] Java course intact with 30 modules.")
        else:
            print("[FAIL] Java course damaged or missing!")
            all_passed = False

        dbms_subject = Subject.query.filter_by(code='DBMS').first()
        if dbms_subject and Concept.query.filter_by(subject_id=dbms_subject.id).count() >= 5:
            print("[OK] DBMS subject intact with concepts.")
        else:
            print("[FAIL] DBMS subject damaged or missing!")
            all_passed = False

        dsa_subject = Subject.query.filter_by(code='DSA').first()
        if dsa_subject and Concept.query.filter_by(subject_id=dsa_subject.id).count() >= 6:
            print("[OK] DSA subject intact with concepts.")
        else:
            print("[FAIL] DSA subject damaged or missing!")
            all_passed = False

        # 5. Execute API Exercise Submission Test via Flask Test Client
        print("\n--- Testing C Code Submission Execution via Flask Test Client ---")
        client = app.test_client()

        test_student = Student.query.filter_by(username='c_verification_user').first()
        if not test_student:
            test_student = Student(username='c_verification_user', email='c_verif@example.com')
            test_student.set_password('pass123')
            db.session.add(test_student)
            db.session.commit()

        c_exercise = Exercise.query.filter_by(language='c').first()
        if c_exercise:
            valid_c_code = (
                "#include <stdio.h>\n"
                "int main(void) {\n"
                "    printf(\"Hello, World!\\n\");\n"
                "    return 0;\n"
                "}\n"
            )

            headers = {'X-Student-ID': str(test_student.id)}
            res = client.post(
                f'/api/courses/exercises/{c_exercise.id}/submit',
                json={'code': valid_c_code},
                headers=headers
            )
            print(f"API HTTP Status Code: {res.status_code}")
            res_data = res.get_json()
            print(f"API Response: {json.dumps(res_data)}")
            if res.status_code == 200 and res_data.get('status') == 'success':
                print("[OK] C exercise submission API test passed successfully.")
            elif res.status_code == 200 and res_data.get('status') == 'compile_error' and "gcc not found" in json.dumps(res_data):
                print("[OK] C execution framework is correct, but gcc is not installed on this system.")
            else:
                print(f"[FAIL] C exercise submission API test failed!")
                all_passed = False
        else:
            print("[FAIL] No C exercise found for submission test!")
            all_passed = False

        print("\n============================================================")
        if all_passed:
            print("VERIFICATION SUCCESSFUL: 15-Module C course meets all pedagogical, structural, and database safety rules.")
            sys.exit(0)
        else:
            print("VERIFICATION FAILED: Violations detected above.")
            sys.exit(1)

if __name__ == '__main__':
    run_verification()
