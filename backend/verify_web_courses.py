"""
verify_web_courses.py — Verifies that HTML, CSS, and JavaScript courses 
are correctly seeded in the LEARNX database.

Usage (from project root):
    python backend/verify_web_courses.py

Or (from backend/):
    python verify_web_courses.py
"""
import sys
import os

# Ensure the backend directory is on sys.path regardless of CWD
_script_dir = os.path.dirname(os.path.abspath(__file__))
if _script_dir not in sys.path:
    sys.path.insert(0, _script_dir)

from app import create_app
from config import Config
from app.models import (
    db, Course, CourseModule, Lesson, Exercise,
    QuizQuestion, MiniProject, Subject
)
from sqlalchemy import inspect as sa_inspect


def verify():
    app = create_app(Config)
    with app.app_context():
        # ── Diagnostic header ──────────────────────────────────────
        engine = db.engine
        inspector = sa_inspect(engine)
        tables = inspector.get_table_names()

        print("=" * 60)
        print("LEARNX — Web Course Verification")
        print("=" * 60)
        print(f"app.instance_path      : {app.instance_path}")
        print(f"SQLALCHEMY_DATABASE_URI : {app.config['SQLALCHEMY_DATABASE_URI']}")
        print(f"Resolved engine URL    : {engine.url}")

        db_file = engine.url.database
        if db_file:
            print(f"Database file path     : {db_file}")
            print(f"Database file exists   : {os.path.exists(db_file)}")
            if os.path.exists(db_file):
                print(f"Database file size     : {os.path.getsize(db_file)} bytes")
        print(f"Tables in database     : {len(tables)}")
        print("-" * 60)

        # ── Verify tables exist ────────────────────────────────────
        required_tables = ['subject', 'course', 'course_module', 'lesson',
                           'exercise', 'quiz_question', 'mini_project', 'test_case']
        missing_tables = [t for t in required_tables if t not in tables]
        if missing_tables:
            print(f"[FATAL] Missing tables: {missing_tables}")
            print("Run the server once to create tables: python backend/run.py")
            sys.exit(1)
        print("[OK] All required tables exist.")
        print("-" * 60)

        # ── List subjects ──────────────────────────────────────────
        subjects = Subject.query.all()
        print(f"\nSubjects in database ({len(subjects)}):")
        for s in subjects:
            print(f"  - {s.name} ({s.code})")
        print("-" * 60)

        # ── Expected counts ────────────────────────────────────────
        expected_web = {
            'HTML': {'modules': 10, 'exercises': 50, 'quizzes': 100, 'projects': 10},
            'CSS': {'modules': 10, 'exercises': 50, 'quizzes': 100, 'projects': 10},
            'JAVASCRIPT': {'modules': 10, 'exercises': 50, 'quizzes': 100, 'projects': 10},
        }
        expected_lang = {
            'HTML': 'html',
            'CSS': 'css',
            'JAVASCRIPT': 'javascript',
        }

        has_error = False
        total_web = {'modules': 0, 'exercises': 0, 'quizzes': 0, 'projects': 0}

        all_courses = Course.query.all()
        if len(all_courses) == 0:
            print("\n[FATAL] No courses found in the database.")
            print("The database has been reset. You need to re-seed:")
            print("  1. python backend/seed_courses.py")
            print("  2. python backend/seed_web_courses.py")
            sys.exit(1)

        print(f"\nCourses in database ({len(all_courses)}):\n")

        for course in all_courses:
            modules = CourseModule.query.filter_by(course_id=course.id).all()
            module_ids = [m.id for m in modules]

            lessons = Lesson.query.filter(Lesson.module_id.in_(module_ids)).all() if module_ids else []
            lesson_ids = [l.id for l in lessons]

            exercises = Exercise.query.filter(Exercise.lesson_id.in_(lesson_ids)).all() if lesson_ids else []
            quizzes = QuizQuestion.query.filter(QuizQuestion.lesson_id.in_(lesson_ids)).all() if lesson_ids else []
            projects = MiniProject.query.filter(MiniProject.lesson_id.in_(lesson_ids)).all() if lesson_ids else []

            print(f"  Course: {course.title} (slug: {course.slug})")
            print(f"    Modules      : {len(modules)}")
            print(f"    Lessons      : {len(lessons)}")
            print(f"    Exercises    : {len(exercises)}")
            print(f"    Quizzes/MCQs : {len(quizzes)}")
            print(f"    Mini Projects: {len(projects)}")

            # ── Identify web course by slug ────────────────────────
            course_key = None
            if 'html' in course.slug:
                course_key = 'HTML'
            elif 'css' in course.slug:
                course_key = 'CSS'
            elif 'javascript' in course.slug or 'js' in course.slug:
                course_key = 'JAVASCRIPT'

            if course_key and course_key in expected_web:
                exp = expected_web[course_key]
                total_web['modules'] += len(modules)
                total_web['exercises'] += len(exercises)
                total_web['quizzes'] += len(quizzes)
                total_web['projects'] += len(projects)

                for label, actual, target in [
                    ('Modules', len(modules), exp['modules']),
                    ('Exercises', len(exercises), exp['exercises']),
                    ('Quizzes', len(quizzes), exp['quizzes']),
                    ('Projects', len(projects), exp['projects']),
                ]:
                    if actual != target:
                        print(f"    [ERROR] {label}: expected {target}, got {actual}")
                        has_error = True

                # ── Verify exercise language ───────────────────────
                expected_l = expected_lang[course_key]
                wrong = [e for e in exercises if e.language != expected_l]
                if wrong:
                    print(f"    [ERROR] {len(wrong)} exercises have wrong language (expected '{expected_l}')")
                    has_error = True
                else:
                    print(f"    [OK] All exercises have language='{expected_l}'")

            # ── Python / Java integrity check ──────────────────────
            elif 'python' in course.slug:
                if len(modules) != 30:
                    print(f"    [ERROR] Python modules: expected 30, got {len(modules)}")
                    has_error = True
                else:
                    print(f"    [OK] Python course intact (30 modules)")
            elif 'java' in course.slug:
                if len(modules) != 30:
                    print(f"    [ERROR] Java modules: expected 30, got {len(modules)}")
                    has_error = True
                else:
                    print(f"    [OK] Java course intact (30 modules)")

            print()

        # ── Web course totals ──────────────────────────────────────
        print("-" * 60)
        print("Web Course Totals:")
        print(f"  Modules  : {total_web['modules']}  (expected 30)")
        print(f"  Exercises: {total_web['exercises']}  (expected 150)")
        print(f"  Quizzes  : {total_web['quizzes']}  (expected 300)")
        print(f"  Projects : {total_web['projects']}  (expected 30)")

        for label, actual, target in [
            ('modules', total_web['modules'], 30),
            ('exercises', total_web['exercises'], 150),
            ('quizzes', total_web['quizzes'], 300),
            ('projects', total_web['projects'], 30),
        ]:
            if actual != target:
                print(f"  [ERROR] Total web {label}: expected {target}, got {actual}")
                has_error = True

        # ── Final verdict ──────────────────────────────────────────
        print("=" * 60)
        if has_error:
            print("VERIFICATION FAILED — see errors above.")
            sys.exit(1)
        else:
            print("VERIFICATION PASSED — all web courses match expected 10/50/100/10.")
            sys.exit(0)


if __name__ == '__main__':
    verify()
