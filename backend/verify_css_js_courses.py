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
        print("VERIFYING CSS & JS COURSE DATA INTEGRITY")
        print("============================================================\n")

        courses_to_check = {
            'css-responsive-design': {'expected_mods': 10, 'expected_les': 10, 'expected_ex': 50, 'expected_q': 100, 'expected_p': 10, 'lang': 'css'},
            'javascript-programming': {'expected_mods': 10, 'expected_les': 10, 'expected_ex': 50, 'expected_q': 100, 'expected_p': 10, 'lang': 'javascript'},
            'html-web-development': {'expected_mods': 10, 'expected_les': 10, 'expected_ex': 50, 'expected_q': 100, 'expected_p': 10, 'lang': 'html'}
        }

        all_passed = True
        
        for slug, expected in courses_to_check.items():
            course = Course.query.filter_by(slug=slug).first()
            if not course:
                print(f"[FAIL] Course {slug} not found!")
                all_passed = False
                continue
                
            print(f"Course: {course.title}")
            
            mods = CourseModule.query.filter_by(course_id=course.id).count()
            les = Lesson.query.join(CourseModule).filter(CourseModule.course_id == course.id).count()
            ex = Exercise.query.join(Lesson).join(CourseModule).filter(CourseModule.course_id == course.id).all()
            ex_count = len(ex)
            q = QuizQuestion.query.join(Lesson).join(CourseModule).filter(CourseModule.course_id == course.id).all()
            q_count = len(q)
            p = MiniProject.query.join(Lesson).join(CourseModule).filter(CourseModule.course_id == course.id).all()
            p_count = len(p)
            
            if mods != expected['expected_mods']:
                print(f"  [FAIL] Modules: {mods} (Expected: {expected['expected_mods']})")
                all_passed = False
            else:
                print(f"  [OK] Modules: {mods}")

            if les != expected['expected_les']:
                print(f"  [FAIL] Lessons: {les} (Expected: {expected['expected_les']})")
                all_passed = False
            else:
                print(f"  [OK] Lessons: {les}")

            if ex_count != expected['expected_ex']:
                print(f"  [FAIL] Exercises: {ex_count} (Expected: {expected['expected_ex']})")
                all_passed = False
            else:
                print(f"  [OK] Exercises: {ex_count}")
                lang_fail = any(e.language != expected['lang'] for e in ex)
                if lang_fail:
                    print(f"  [FAIL] Exercise language mismatch for {slug}")
                    all_passed = False
                else:
                    print(f"  [OK] Exercise languages match '{expected['lang']}'")

            if q_count != expected['expected_q']:
                print(f"  [FAIL] Quizzes: {q_count} (Expected: {expected['expected_q']})")
                all_passed = False
            else:
                print(f"  [OK] Quizzes: {q_count}")

            if p_count != expected['expected_p']:
                print(f"  [FAIL] Projects: {p_count} (Expected: {expected['expected_p']})")
                all_passed = False
            else:
                print(f"  [OK] Projects: {p_count}")
                
            # Content quality basic checks
            filler_keywords = ['filler', 'generic', 'placeholder']
            has_filler = False
            for l in Lesson.query.join(CourseModule).filter(CourseModule.course_id == course.id):
                if any(k in l.content.lower() for k in filler_keywords) or len(l.content) < 50:
                    has_filler = True
            if has_filler:
                print(f"  [FAIL] Obvious filler text detected in lessons.")
                all_passed = False
            else:
                print(f"  [OK] Content quality assertions passed (or no obvious filler detected)")

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
            print("VERIFICATION PASSED — all constraints met")
            sys.exit(0)
        else:
            print("VERIFICATION FAILED")
            sys.exit(1)

if __name__ == '__main__':
    verify_courses()
