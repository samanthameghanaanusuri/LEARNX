import os
import sys
from app import create_app, db
from app.models import Course, CourseModule, Lesson, Exercise, QuizQuestion, MiniProject

def verify():
    app = create_app()
    with app.app_context():
        print("Starting verification of LEARNX courses...")
        
        all_courses = Course.query.all()
        if len(all_courses) == 0:
            print("\n[FATAL] No courses found in the database.")
            sys.exit(1)

        print(f"\nCourses in database ({len(all_courses)}):\n")

        has_error = False

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

            # Check specific expectations
            if 'cyber-security' in course.slug:
                if len(modules) != 20:
                    print(f"    [ERROR] Cyber Security modules: expected 20, got {len(modules)}")
                    has_error = True
                if len(quizzes) != 200:
                    print(f"    [ERROR] Cyber Security quizzes: expected 200, got {len(quizzes)}")
                    has_error = True
                if len(exercises) != 120:
                    print(f"    [ERROR] Cyber Security exercises: expected 120, got {len(exercises)}")
                    has_error = True
            elif 'c-programming' in course.slug:
                if len(modules) != 15:
                    print(f"    [ERROR] C Programming modules: expected 15, got {len(modules)}")
                    has_error = True
                if len(quizzes) != 150:
                    print(f"    [ERROR] C Programming quizzes: expected 150, got {len(quizzes)}")
                    has_error = True
            elif 'cpp' in course.slug:
                if len(modules) != 15:
                    print(f"    [ERROR] C++ Programming modules: expected 15, got {len(modules)}")
                    has_error = True
            
            print()

        print("=" * 60)
        if has_error:
            print("VERIFICATION FAILED - see errors above.")
            sys.exit(1)
        else:
            print("VERIFICATION PASSED - course data integrity verified.")
            sys.exit(0)

if __name__ == '__main__':
    verify()
