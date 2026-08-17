import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import json
from app import create_app
from app.models import db, Student, Course, CourseModule, Lesson, QuizQuestion

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'test_secret'

class QuizBulkAuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

        # Create test student
        self.student = Student(username='quiz_user', email='quiz@example.com')
        self.student.set_password('password123')
        db.session.add(self.student)
        db.session.commit()

        # Create course, module, lesson, quiz question
        course = Course(title="Test Course", slug="test-course", description="Desc", category="CS", difficulty="Beginner")
        db.session.add(course)
        db.session.commit()

        module = CourseModule(course_id=course.id, title="Test Module", order_index=1)
        db.session.add(module)
        db.session.commit()

        self.lesson = Lesson(module_id=module.id, title="Test Lesson", slug="test-lesson", content="Content", order_index=1)
        db.session.add(self.lesson)
        db.session.commit()

        self.quiz = QuizQuestion(lesson_id=self.lesson.id, question_text="What is 1+1?", options_json=json.dumps(["1", "2"]), correct_answer="2", difficulty="Beginner")
        db.session.add(self.quiz)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_quiz_bulk_unauthenticated_returns_401(self):
        url = f'/api/courses/lessons/{self.lesson.id}/quiz/bulk'
        response = self.client.post(url, json={
            'answers': {str(self.quiz.id): '2'}
        })
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.data)
        self.assertEqual(data.get('error'), 'Unauthorized')

    def test_quiz_bulk_authenticated_returns_200(self):
        url = f'/api/courses/lessons/{self.lesson.id}/quiz/bulk'
        # Authenticate via X-Student-ID header (standard API wrapper behavior)
        response = self.client.post(url, headers={'X-Student-ID': str(self.student.id)}, json={
            'answers': {str(self.quiz.id): '2'}
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertEqual(data.get('correct'), 1)

    def test_quiz_bulk_session_authenticated_returns_200(self):
        url = f'/api/courses/lessons/{self.lesson.id}/quiz/bulk'
        # Authenticate via session (login route)
        with self.client:
            self.client.post('/api/auth/login', json={
                'username': 'quiz_user',
                'password': 'password123'
            })
            response = self.client.post(url, json={
                'answers': {str(self.quiz.id): '2'}
            })
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertTrue(data.get('success'))

if __name__ == '__main__':
    unittest.main()
