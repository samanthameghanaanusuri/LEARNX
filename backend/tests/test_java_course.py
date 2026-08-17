import unittest
import json
from app import create_app
from config import Config
from app.models import (
    db, Student, Course, CourseModule, Lesson, Exercise, 
    MiniProject, TestCase, ProjectTestCase, ExerciseSubmission, 
    ProjectSubmission, Subject, Concept
)
from app.services.executor import CodeExecutor

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class JavaCourseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            
            # Clean database to avoid unique constraint collisions
            Student.query.delete()
            Course.query.delete()
            Subject.query.delete()
            Concept.query.delete()
            db.session.commit()
            
            # Create a test student
            self.student = Student(username='javastudent', email='java@learnx.io')
            self.student.set_password('password123')
            db.session.add(self.student)
            db.session.commit()
            self.student_id = self.student.id

            # Create Subject and Concept
            self.subject = Subject(name='Java Language', code='JAVA')
            db.session.add(self.subject)
            db.session.commit()
            
            self.concept = Concept(subject_id=self.subject.id, name='Java Loops')
            db.session.add(self.concept)
            db.session.commit()

            # Create Java Course
            self.course = Course(
                title='Java Programming Test',
                slug='java-programming-test',
                category='Programming',
                description='Master Java',
                difficulty='Beginner',
                is_published=True
            )
            db.session.add(self.course)
            db.session.commit()

            # Create Module
            self.module = CourseModule(
                course_id=self.course.id,
                title='Java Loops Module',
                description='Loops module description',
                order_index=1
            )
            db.session.add(self.module)
            db.session.commit()

            # Create Lesson
            self.lesson = Lesson(
                module_id=self.module.id,
                concept_id=self.concept.id,
                title='Mastering Java Loops',
                slug='mastering-java-loops-test',
                content='HTML content for loops theory...',
                order_index=1
            )
            db.session.add(self.lesson)
            db.session.commit()

            # Create Coding Exercise
            self.exercise = Exercise(
                lesson_id=self.lesson.id,
                concept_id=self.concept.id,
                title='Print numbers 1 to N',
                description='Read N from input and print 1 to N space-separated.',
                difficulty='Easy',
                starter_code='import java.util.Scanner;\npublic class Solution {\n    public static void main(String[] args) {\n        // Code here\n    }\n}',
                expected_output='1 2 3 ',
                language='java',
                order_index=1
            )
            db.session.add(self.exercise)
            db.session.commit()

            # Create Test Cases for Exercise
            self.tc1 = TestCase(
                exercise_id=self.exercise.id,
                input_data='3\n',
                expected_output='1 2 3 ',
                is_hidden=False,
                order_index=1
            )
            self.tc2 = TestCase(
                exercise_id=self.exercise.id,
                input_data='5\n',
                expected_output='1 2 3 4 5 ',
                is_hidden=True,
                order_index=2
            )
            db.session.add_all([self.tc1, self.tc2])
            db.session.commit()

            # Create Mini Project
            self.project = MiniProject(
                lesson_id=self.lesson.id,
                concept_id=self.concept.id,
                title='Looping pattern architect',
                objective='Print dynamic pattern',
                scenario='Create pattern output',
                requirements_json='["Requirement 1"]',
                features_json='["Feature 1"]',
                guidance_json='["Guidance 1"]',
                hints_json='["Hint 1"]',
                starter_code='public class Solution {\n    public static void main(String[] args) {\n        // Pattern\n    }\n}',
                language='java',
                expected_behavior='Sorted pattern log',
                evaluation_criteria='String equality check'
            )
            db.session.add(self.project)
            db.session.commit()

            # Project Test Cases
            self.ptc1 = ProjectTestCase(
                project_id=self.project.id,
                input_data='3\n',
                expected_output='*\n**\n***\n',
                description='Size 3 pattern',
                is_hidden=False,
                order_index=1
            )
            db.session.add(self.ptc1)
            db.session.commit()

            self.lesson_id = self.lesson.id
            self.exercise_id = self.exercise.id
            self.project_id = self.project.id

    def tearDown(self):
        with self.app.app_context():
            db.session.rollback()
            db.session.remove()
            db.drop_all()

    def test_code_executor_valid_java(self):
        code = (
            "public class Solution {\n"
            "    public static void main(String[] args) {\n"
            "        System.out.println(\"Hello Java LEARNX\");\n"
            "    }\n"
            "}"
        )
        executor = CodeExecutor(language='java', code=code)
        res = executor.execute()
        self.assertEqual(res['status'], 'success')
        self.assertEqual(res['stdout'].strip(), 'Hello Java LEARNX')
        self.assertIsNone(res['error_type'])

    def test_code_executor_java_compile_error(self):
        code = (
            "public class Solution {\n"
            "    public static void main(String[] args) {\n"
            "        System.out.println(\"Hello Java LEARNX\")\n"  # missing semicolon
            "    }\n"
            "}"
        )
        executor = CodeExecutor(language='java', code=code)
        res = executor.execute()
        self.assertEqual(res['status'], 'compile_error')
        self.assertEqual(res['error_type'], 'compile_error')
        self.assertIn(';', res['stderr'])

    def test_code_executor_java_runtime_error(self):
        code = (
            "public class Solution {\n"
            "    public static void main(String[] args) {\n"
            "        int x = 10 / 0;\n"
            "    }\n"
            "}"
        )
        executor = CodeExecutor(language='java', code=code)
        res = executor.execute()
        self.assertEqual(res['status'], 'runtime_error')
        self.assertEqual(res['error_type'], 'arithmeticexception')
        self.assertIn('ArithmeticException', res['stderr'])

    def test_submit_exercise_java_success(self):
        with self.client.session_transaction() as sess:
            sess['student_id'] = self.student_id

        code = (
            "import java.util.Scanner;\n"
            "public class Solution {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        if (sc.hasNextInt()) {\n"
            "            int n = sc.nextInt();\n"
            "            for (int i = 1; i <= n; i++) {\n"
            "                System.out.print(i + \" \");\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}"
        )

        res = self.client.post(
            f'/api/courses/exercises/{self.exercise_id}/submit',
            json={'code': code},
            headers={'X-Student-ID': str(self.student_id)}
        )
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['passed'], 2)

    def test_submit_project_java_success(self):
        with self.client.session_transaction() as sess:
            sess['student_id'] = self.student_id

        code = (
            "import java.util.Scanner;\n"
            "public class Solution {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        if (sc.hasNextInt()) {\n"
            "            int n = sc.nextInt();\n"
            "            for (int i = 1; i <= n; i++) {\n"
            "                for (int j = 1; j <= i; j++) {\n"
            "                    System.out.print(\"*\");\n"
            "                }\n"
            "                System.out.println();\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}"
        )

        res = self.client.post(
            f'/api/courses/projects/{self.project_id}/submit',
            json={'code': code},
            headers={'X-Student-ID': str(self.student_id)}
        )
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['status'], 'passed')
        self.assertEqual(data['passed_tests'], 1)

if __name__ == '__main__':
    unittest.main()
