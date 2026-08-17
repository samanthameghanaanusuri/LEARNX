import os
import sys

_script_dir = os.path.dirname(os.path.abspath(__file__))
if _script_dir not in sys.path:
    sys.path.insert(0, _script_dir)

from app import create_app
from config import Config
from app.models import db, Course, CourseModule, Lesson, Exercise, QuizQuestion, MiniProject

def verify_courses():
    app = create_app(Config)
    with app.app_context():
        print("============================================================")
        print("VERIFYING PEDAGOGICAL COURSE DATA INTEGRITY")
        print("============================================================\n")

        courses_to_check = {
            'html-web-development': {'lang': 'html'},
            'css-responsive-design': {'lang': 'css'},
            'javascript-programming': {'lang': 'javascript'},
            'c-programming': {'lang': 'c'}
        }

        all_passed = True
        
        for slug, data in courses_to_check.items():
            course = Course.query.filter_by(slug=slug).first()
            if not course:
                print(f"[FAIL] Course {slug} not found!")
                all_passed = False
                continue
                
            print(f"Course: {course.title}")
            
            mods = CourseModule.query.filter_by(course_id=course.id).all()
            print(f"  [INFO] Total Modules: {len(mods)}")
            
            for mod in mods:
                lessons = Lesson.query.filter_by(module_id=mod.id).all()
                if not lessons:
                    print(f"  [FAIL] Module '{mod.title}' has no lessons.")
                    all_passed = False
                
                for les in lessons:
                    # Content check
                    req_sections = ["WHAT", "WHY", "HOW", "SYNTAX", "EXAMPLE", "COMMON MISTAKES"]
                    missing_sections = [s for s in req_sections if s not in les.content.upper()]
                    if missing_sections and "PROJECT" not in les.title.upper():
                        print(f"  [WARN] Lesson '{les.title}' may be missing sections: {missing_sections}")
                    if len(les.content) < 300:
                        print(f"  [FAIL] Lesson '{les.title}' content is too short (pedagogically insufficient).")
                        all_passed = False
                        
                    # Exercises check
                    exercises = Exercise.query.filter_by(lesson_id=les.id).order_by(Exercise.order_index).all()
                    if exercises:
                        difficulties = [ex.difficulty for ex in exercises]
                        # Progressive difficulty check
                        if "Hard" in difficulties and "Easy" in difficulties:
                            hard_idx = difficulties.index("Hard")
                            easy_idx = difficulties.index("Easy")
                            if hard_idx < easy_idx:
                                print(f"  [FAIL] Exercises in '{les.title}' do not progress logically (Hard before Easy).")
                                all_passed = False
                                
                    # Quizzes check
                    quizzes = QuizQuestion.query.filter_by(lesson_id=les.id).all()
                    for q in quizzes:
                        if "What is the syntax" in q.question_text:
                            print(f"  [WARN] Rote syntax question found: {q.question_text}")
                            
            print("-" * 60)

        # Ensure Python and Java are intact
        python_course = Course.query.filter_by(slug='python-programming').first()
        if python_course and CourseModule.query.filter_by(course_id=python_course.id).count() == 30:
            print("[OK] Python course exists with 30 modules")
        else:
            print("[FAIL] Python course is missing or damaged")
            all_passed = False
            
        java_course = Course.query.filter_by(slug='java-programming').first()
        if java_course and CourseModule.query.filter_by(course_id=java_course.id).count() == 30:
            print("[OK] Java course exists with 30 modules")
        else:
            print("[FAIL] Java course is missing or damaged")
            all_passed = False

        print("============================================================")
        if all_passed:
            print("VERIFICATION PASSED — pedagogical constraints met")
            sys.exit(0)
        else:
            print("VERIFICATION FAILED")
            sys.exit(1)

if __name__ == '__main__':
    verify_courses()
