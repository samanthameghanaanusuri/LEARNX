import os
import json
import sys
from app import create_app
from app.models import (
    db, Course, CourseModule, Lesson, Exercise, 
    QuizQuestion, MiniProject, TestCase, Student
)
from app.services.executor import CodeExecutor

def run_verification():
    app = create_app()
    with app.app_context():
        java_course = Course.query.filter_by(slug='java-programming').first()
        if not java_course:
            print("ERROR: Java course not found!")
            sys.exit(1)

        modules = CourseModule.query.filter_by(course_id=java_course.id).all()
        module_count = len(modules)
        
        lesson_count = 0
        exercise_count = 0
        java_exercise_count = 0
        python_in_java_count = 0
        quiz_count = 0
        project_count = 0

        for m in modules:
            lessons = Lesson.query.filter_by(module_id=m.id).all()
            lesson_count += len(lessons)
            for l in lessons:
                exercises = Exercise.query.filter_by(lesson_id=l.id).all()
                exercise_count += len(exercises)
                for ex in exercises:
                    if ex.language == 'java':
                        java_exercise_count += 1
                    elif ex.language == 'python':
                        python_in_java_count += 1

                quizzes = QuizQuestion.query.filter_by(lesson_id=l.id).all()
                quiz_count += len(quizzes)

                projects = MiniProject.query.filter_by(lesson_id=l.id).all()
                project_count += len(projects)

        # 1. Output database counts in exact required format
        print("Java course:")
        print(f"Modules: {module_count}")
        print(f"Lessons: {lesson_count}")
        print(f"Exercises: {exercise_count}")
        print(f"Java exercises: {java_exercise_count}")
        print(f"Python exercises accidentally inside Java course: {python_in_java_count}")
        print(f"Quizzes: {quiz_count}")
        print(f"Mini Projects: {project_count}")
        print()

        # 2. Test one Java exercise through actual API test client
        print("--- Testing valid Java exercise via API ---")
        client = app.test_client()

        # Find or create a test student for API testing
        test_student = Student.query.filter_by(username='java_test_user').first()
        if not test_student:
            test_student = Student(username='java_test_user', email='java_test@example.com')
            test_student.set_password('pass123')
            db.session.add(test_student)
            db.session.commit()

        first_ex = Exercise.query.filter_by(title='Print Welcome message').first()
        if not first_ex:
            first_ex = Exercise.query.first()

        print(f"Exercise ID: {first_ex.id}, Title: '{first_ex.title}', Language: '{first_ex.language}'")
        
        valid_java_code = (
            "public class Solution {\n"
            "    public static void main(String[] args) {\n"
            "        System.out.println(\"Welcome to Java!\");\n"
            "    }\n"
            "}"
        )

        with client.session_transaction() as sess:
            sess['student_id'] = test_student.id

        headers = {'X-Student-ID': str(test_student.id)}

        res = client.post(
            f'/api/courses/exercises/{first_ex.id}/submit',
            json={'code': valid_java_code},
            headers=headers
        )

        print(f"API Response HTTP Status: {res.status_code}")
        res_data = res.get_json()
        print(f"API Response Body: {json.dumps(res_data, indent=2)}")
        assert res.status_code == 200, f"Expected 200, got {res.status_code}"
        assert res_data.get('status') == 'success', f"Expected status success, got {res_data.get('status')}"
        assert res_data.get('passed') == res_data.get('total'), "All test cases should pass"
        print("[OK] Valid Java exercise execution test PASSED!")
        print()

        # 3. Test intentionally invalid Java program
        print("--- Testing invalid Java code (compilation error check) ---")
        invalid_java_code = (
            "public class Solution {\n"
            "    public static void main(String[] args) {\n"
            "        System.out.println(\"Missing semicolon\")\n"
            "    }\n"
            "}"
        )

        run_res = client.post(
            '/api/code/run',
            json={'language': 'java', 'code': invalid_java_code, 'stdin': ''}
        )

        print(f"Run API Status Code: {run_res.status_code}")
        run_data = run_res.get_json()
        print(f"Run API Output: {json.dumps(run_data, indent=2)}")
        assert run_data.get('status') == 'compile_error', f"Expected compile_error, got {run_data.get('status')}"
        assert run_data.get('error_type') == 'compile_error', f"Expected error_type compile_error, got {run_data.get('error_type')}"
        assert 'SyntaxError' not in run_data.get('stderr', ''), "Should NOT return a Python SyntaxError!"
        assert ';' in run_data.get('stderr', ''), "Expected Java compiler javac stderr mentioning ';'"
        print("[OK] Invalid Java program compilation error check PASSED (Returned javac error, not Python SyntaxError)!")
        print()

if __name__ == '__main__':
    run_verification()
