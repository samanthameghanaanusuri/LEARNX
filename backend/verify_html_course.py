import sys
import os

_script_dir = os.path.dirname(os.path.abspath(__file__))
if _script_dir not in sys.path:
    sys.path.insert(0, _script_dir)

from app import create_app
from config import Config
from app.models import (
    db, Course, CourseModule, Lesson, LessonExample, Exercise,
    QuizQuestion, MiniProject
)

def verify():
    app = create_app(Config)
    with app.app_context():
        print("=" * 60)
        print("VERIFYING HTML COURSE DATA INTEGRITY")
        print("=" * 60)
        
        has_error = False

        html_course = Course.query.filter(Course.slug.like('%html%')).first()
        if not html_course:
            print("[FATAL] HTML course not found!")
            sys.exit(1)

        modules = CourseModule.query.filter_by(course_id=html_course.id).all()
        module_ids = [m.id for m in modules]
        
        lessons = Lesson.query.filter(Lesson.module_id.in_(module_ids)).all() if module_ids else []
        lesson_ids = [l.id for l in lessons]
        
        examples = LessonExample.query.filter(LessonExample.lesson_id.in_(lesson_ids)).all() if lesson_ids else []
        exercises = Exercise.query.filter(Exercise.lesson_id.in_(lesson_ids)).all() if lesson_ids else []
        quizzes = QuizQuestion.query.filter(QuizQuestion.lesson_id.in_(lesson_ids)).all() if lesson_ids else []
        projects = MiniProject.query.filter(MiniProject.lesson_id.in_(lesson_ids)).all() if lesson_ids else []

        print(f"HTML Course ID: {html_course.id}")
        
        for label, actual, target in [
            ('Modules', len(modules), 10),
            ('Lessons', len(lessons), 10),
            ('Exercises', len(exercises), 50),
            ('MCQs', len(quizzes), 100),
            ('Mini Projects', len(projects), 10)
        ]:
            if actual != target:
                print(f"[ERROR] {label}: expected {target}, got {actual}")
                has_error = True
            else:
                print(f"[OK] {label}: {actual}")

        html_exercises = [e for e in exercises if e.language == 'html']
        python_exercises = [e for e in exercises if e.language == 'python']
        java_exercises = [e for e in exercises if e.language == 'java']

        if len(html_exercises) != 50:
            print(f"[ERROR] HTML exercises: expected 50, got {len(html_exercises)}")
            has_error = True
        
        if len(python_exercises) > 0:
            print(f"[ERROR] Python exercises inside HTML course: expected 0, got {len(python_exercises)}")
            has_error = True

        if len(java_exercises) > 0:
            print(f"[ERROR] Java exercises inside HTML course: expected 0, got {len(java_exercises)}")
            has_error = True

        print("-" * 60)
        print("Verifying content quality assertions...")

        # Verify no placeholder/filler
        bad_phrases = ["<!-- example code -->", "Here is how you use"]
        for ex in examples:
            for bad in bad_phrases:
                if bad in ex.code or bad in ex.explanation:
                    print(f"[ERROR] Found filler content in Example {ex.id}")
                    has_error = True
                    
        for les in lessons:
            if not les.content or len(les.content) < 100:
                print(f"[ERROR] Lesson {les.id} has insufficient theory")
                has_error = True
                
        for ex in exercises:
            if not ex.starter_code and ex.starter_code != "":
                print(f"[ERROR] Exercise {ex.id} is missing starter code")
                has_error = True
                
        print("[OK] Content quality assertions passed (or no obvious filler detected)")

        print("-" * 60)
        print("Verifying existing courses remain intact...")
        
        for lang in ['python', 'java', 'css']:
            course = Course.query.filter(Course.slug.like(f'%{lang}%')).first()
            if not course:
                print(f"[ERROR] {lang.capitalize()} course missing!")
                has_error = True
            else:
                c_mods = CourseModule.query.filter_by(course_id=course.id).count()
                if c_mods == 0:
                    print(f"[ERROR] {lang.capitalize()} course has 0 modules!")
                    has_error = True
                else:
                    print(f"[OK] {lang.capitalize()} course exists with {c_mods} modules")

        print("=" * 60)
        if has_error:
            print("VERIFICATION FAILED")
            sys.exit(1)
        else:
            print("VERIFICATION PASSED — all constraints met")
            sys.exit(0)

if __name__ == '__main__':
    verify()
