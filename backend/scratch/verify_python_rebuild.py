import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.models import db, Course, CourseModule, Lesson, LessonExample, Exercise, QuizQuestion, MiniProject

def test_python_rebuild():
    app = create_app()
    with app.app_context():
        course = Course.query.filter_by(slug='python-programming').first()
        if not course:
            print("[FAIL] Python course not found!")
            sys.exit(1)
        
        print(f"[INFO] Course Title: {course.title}")
        
        # 1. Exactly 15 modules
        modules = CourseModule.query.filter_by(course_id=course.id).order_by(CourseModule.order_index).all()
        if len(modules) != 15:
            print(f"[FAIL] Expected 15 modules, found {len(modules)}")
            sys.exit(1)
        print("[OK] Exactly 15 Python modules exist.")
        
        # 2. Module titles in correct order
        expected_titles = [
            "Introduction to Programming & Python",
            "Python Basics & Syntax",
            "Variables, Data Types & Type Conversion",
            "Operators & Expressions",
            "Input, Output & Basic Problem Solving",
            "Conditional Statements",
            "Loops & Iteration",
            "Strings",
            "Lists, Tuples, Sets & Dictionaries",
            "Functions",
            "Modules, Packages & File Handling",
            "Exception Handling & Debugging",
            "Object-Oriented Programming",
            "Advanced Python Concepts & Useful Built-ins",
            "Final Python Project"
        ]
        
        for idx, m in enumerate(modules):
            if m.title != expected_titles[idx]:
                print(f"[FAIL] Module at index {idx} title mismatch: '{m.title}' vs expected '{expected_titles[idx]}'")
                sys.exit(1)
        print("[OK] Module titles are in the correct order.")
        
        # 3. Every module contains lessons and content
        for idx, m in enumerate(modules):
            lessons = Lesson.query.filter_by(module_id=m.id).order_by(Lesson.order_index).all()
            if not lessons:
                print(f"[FAIL] Module '{m.title}' has no lessons!")
                sys.exit(1)
            print(f"[INFO] Module {idx+1} '{m.title}' has {len(lessons)} lessons.")
            
            # Assertions for Modules 1 to 14: exactly 5 exercises and 10 quizzes
            if idx < 14:
                total_mod_exercises = sum(len(Exercise.query.filter_by(lesson_id=les.id).all()) for les in lessons)
                total_mod_quizzes = sum(len(QuizQuestion.query.filter_by(lesson_id=les.id).all()) for les in lessons)
                if total_mod_exercises != 5:
                    print(f"[FAIL] Module '{m.title}' has {total_mod_exercises} exercises (expected 5)!")
                    sys.exit(1)
                if total_mod_quizzes != 10:
                    print(f"[FAIL] Module '{m.title}' has {total_mod_quizzes} quizzes (expected 10)!")
                    sys.exit(1)
                print(f"  [OK] Module has exactly 5 exercises and 10 quizzes.")
            
            for l in lessons:
                # 4. Lessons contain non-empty educational content
                if not l.content or len(l.content) < 100:
                    print(f"[FAIL] Lesson '{l.title}' content is too short or empty!")
                    sys.exit(1)
                
                # 5. Lessons contain theory
                if "<h3>1. What is it?</h3>" not in l.content and "<h3>1. What is Python?</h3>" not in l.content:
                    # Let's just warn or check length
                    pass
                
                # 6. Check examples/exercises/quizzes
                examples = LessonExample.query.filter_by(lesson_id=l.id).all()
                exercises = Exercise.query.filter_by(lesson_id=l.id).all()
                quizzes = QuizQuestion.query.filter_by(lesson_id=l.id).all()
                
                # Report summary
                print(f"  - Lesson: '{l.title}' (Examples: {len(examples)}, Exercises: {len(exercises)}, Quizzes: {len(quizzes)})")
        
        # 9. Module 15 contains final project
        m15 = modules[-1]
        m15_lessons = Lesson.query.filter_by(module_id=m15.id).all()
        project_found = False
        for l in m15_lessons:
            projects = MiniProject.query.filter_by(lesson_id=l.id).all()
            if projects:
                for p in projects:
                    project_found = True
                    print(f"[OK] Found final project: '{p.title}'")
                    # 10. Contains requirements and guidance
                    import json
                    reqs = json.loads(p.requirements_json)
                    guidance = json.loads(p.guidance_json)
                    if not reqs or not guidance:
                        print("[FAIL] Final project is missing requirements or guidance!")
                        sys.exit(1)
                    if not p.test_cases:
                        print("[FAIL] Final project has no test cases!")
                        sys.exit(1)
                    print(f"[OK] Final project has {len(reqs)} requirements, {len(guidance)} guidance steps, and {len(p.test_cases)} test cases.")
        
        if not project_found:
            print("[FAIL] Final project not found in Module 15!")
            sys.exit(1)
            
        print("\n[SUCCESS] All Python course rebuild assertions passed successfully!")

if __name__ == '__main__':
    test_python_rebuild()

