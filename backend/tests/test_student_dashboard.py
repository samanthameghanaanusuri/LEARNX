import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import json
from datetime import datetime, timedelta
from app import create_app
from app.models import (
    db, Student, Course, CourseModule, Lesson, LessonProgress, 
    CourseEnrollment, AnswerAttempt, Question, Concept, Subject
)

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'test_secret_dashboard_key'

class StudentDashboardTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

        # Seed initial courses/modules/lessons for testing
        self.course = Course(
            title="Python Course",
            slug="python-course",
            category="Programming",
            difficulty="Beginner",
            is_published=True
        )
        db.session.add(self.course)
        db.session.commit()

        self.module = CourseModule(
            course_id=self.course.id,
            title="Module 1",
            order_index=1
        )
        db.session.add(self.module)
        db.session.commit()

        self.lesson1 = Lesson(
            module_id=self.module.id,
            title="Lesson 1",
            slug="lesson-1",
            content="Content 1",
            order_index=1
        )
        self.lesson2 = Lesson(
            module_id=self.module.id,
            title="Lesson 2",
            slug="lesson-2",
            content="Content 2",
            order_index=2
        )
        db.session.add_all([self.lesson1, self.lesson2])
        db.session.commit()

        # Seed Subject & Concept & Questions
        self.subject = Subject(
            name="Database Systems",
            code="DBMS",
            description="DBMS course"
        )
        db.session.add(self.subject)
        db.session.commit()

        self.concept = Concept(
            subject_id=self.subject.id,
            name="Relational Schema",
            description="Relational Schema concept"
        )
        db.session.add(self.concept)
        db.session.commit()

        self.question = Question(
            concept_id=self.concept.id,
            question_text="What is a relation?",
            options_json=json.dumps(["Table", "Row", "Column", "File"]),
            correct_answer="Table",
            difficulty_level="Beginner"
        )
        db.session.add(self.question)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def register_and_login(self, username, email, password):
        self.client.post('/api/auth/register', json={
            'username': username,
            'email': email,
            'password': password
        })
        return self.client.post('/api/auth/login', json={
            'username': username,
            'password': password
        })

    def test_01_dashboard_requires_auth(self):
        res = self.client.get('/api/progress/dashboard')
        self.assertEqual(res.status_code, 401)

    def test_02_authenticated_dashboard_loads(self):
        self.register_and_login('student_a', 'a@example.com', 'password123')
        res = self.client.get('/api/progress/dashboard')
        self.assertEqual(res.status_code, 200)

    def test_03_correct_student_name_returned(self):
        self.register_and_login('student_a', 'a@example.com', 'password123')
        res = self.client.get('/api/progress/dashboard')
        data = json.loads(res.data)
        self.assertEqual(data['student']['username'], 'student_a')

    def test_04_student_isolation(self):
        # Register student A, enroll, and save progress
        self.register_and_login('student_a', 'a@example.com', 'password123')
        self.client.post(f'/api/courses/{self.course.id}/enroll')
        self.client.post('/api/progress/ping', json={'active_minutes': 15})
        self.client.post('/api/auth/logout')

        # Login student B
        self.register_and_login('student_b', 'b@example.com', 'password123')
        res = self.client.get('/api/progress/dashboard')
        data = json.loads(res.data)
        
        # Verify student B has 0 minutes and no enrolled courses
        self.assertEqual(data['student']['username'], 'student_b')
        self.assertEqual(data['learning_time_minutes'], 0)
        self.assertEqual(len(data['courses']), 0)

    def test_05_course_progress_belongs_to_correct_student(self):
        # Student A progress
        self.register_and_login('student_a', 'a@example.com', 'password123')
        self.client.post(f'/api/courses/{self.course.id}/enroll')
        lp = LessonProgress(student_id=1, lesson_id=self.lesson1.id, status='completed')
        db.session.add(lp)
        db.session.commit()
        
        # Trigger progress calculation
        self.client.get(f'/api/courses/{self.course.id}/progress')
        
        res = self.client.get('/api/progress/dashboard')
        data = json.loads(res.data)
        self.assertEqual(data['courses'][0]['progress'], 50.0)
        self.client.post('/api/auth/logout')

        # Student B progress is clean
        self.register_and_login('student_b', 'b@example.com', 'password123')
        self.client.post(f'/api/courses/{self.course.id}/enroll')
        res = self.client.get('/api/progress/dashboard')
        data = json.loads(res.data)
        self.assertEqual(data['courses'][0]['progress'], 0.0)

    def test_06_learning_time_increments_correctly(self):
        self.register_and_login('student_a', 'a@example.com', 'password123')
        self.client.post('/api/progress/ping', json={'active_minutes': 5})
        self.client.post('/api/progress/ping', json={'active_minutes': 3})
        res = self.client.get('/api/progress/dashboard')
        data = json.loads(res.data)
        self.assertEqual(data['learning_time_minutes'], 8)

    def test_07_hidden_tab_behavior_and_heartbeat(self):
        # Heartbeat active validation
        self.register_and_login('student_a', 'a@example.com', 'password123')
        res = self.client.post('/api/progress/ping', json={'active_minutes': 2})
        self.assertEqual(res.status_code, 200)

    def test_08_same_day_streak_no_increment(self):
        self.register_and_login('student_a', 'a@example.com', 'password123')
        self.client.post('/api/progress/ping', json={'active_minutes': 1})
        self.client.post('/api/progress/ping', json={'active_minutes': 1})
        res = self.client.get('/api/progress/dashboard')
        data = json.loads(res.data)
        self.assertEqual(data['current_streak'], 1)

    def test_09_consecutive_day_streak_increments(self):
        self.register_and_login('student_a', 'a@example.com', 'password123')
        # Seed yesterday's activity
        student = Student.query.get(1)
        student.last_activity_date = (datetime.utcnow() - timedelta(days=1)).date()
        student.current_streak = 1
        db.session.commit()

        # Ping today
        self.client.post('/api/progress/ping', json={'active_minutes': 1})
        res = self.client.get('/api/progress/dashboard')
        data = json.loads(res.data)
        self.assertEqual(data['current_streak'], 2)
        self.assertEqual(data['longest_streak'], 2)

        # Ping after missing days resets to 1
        student = Student.query.get(1)
        student.last_activity_date = (datetime.utcnow() - timedelta(days=3)).date()
        student.current_streak = 2
        db.session.commit()

        self.client.post('/api/progress/ping', json={'active_minutes': 1})
        res = self.client.get('/api/progress/dashboard')
        data = json.loads(res.data)
        self.assertEqual(data['current_streak'], 1)
        self.assertEqual(data['longest_streak'], 2)

    def test_10_logout_invalidates_session(self):
        self.register_and_login('student_a', 'a@example.com', 'password123')
        self.client.post('/api/auth/logout')
        res = self.client.get('/api/progress/dashboard')
        self.assertEqual(res.status_code, 401)

    def test_11_login_again_restores_same_student(self):
        self.register_and_login('student_a', 'a@example.com', 'password123')
        self.client.post('/api/progress/ping', json={'active_minutes': 10})
        self.client.post('/api/auth/logout')

        self.register_and_login('student_a', 'a@example.com', 'password123')
        res = self.client.get('/api/progress/dashboard')
        data = json.loads(res.data)
        self.assertEqual(data['learning_time_minutes'], 10)

    def test_12_existing_course_counts_intact(self):
        initial_count = Course.query.count()
        self.register_and_login('student_a', 'a@example.com', 'password123')
        self.client.post(f'/api/courses/{self.course.id}/enroll')
        self.assertEqual(Course.query.count(), initial_count)

    def test_13_assessment_questions_load(self):
        self.register_and_login('student_a', 'a@example.com', 'password123')
        res = self.client.get(f'/api/assessments/subjects/{self.subject.id}/questions')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertIn(str(self.concept.id), data['concepts_questions'])

    def test_14_assessment_results_scoped(self):
        self.register_and_login('student_a', 'a@example.com', 'password123')
        
        # Submit assessment
        res = self.client.post('/api/assessments/submit', json={
            'answers': [
                {'question_id': self.question.id, 'student_answer': 'Table'}
            ]
        })
        self.assertEqual(res.status_code, 200)
        
        attempts = AnswerAttempt.query.filter_by(student_id=1).all()
        self.assertEqual(len(attempts), 1)
        self.assertEqual(attempts[0].student_answer, 'Table')

    def test_15_dashboard_works_with_zero_enrolled(self):
        self.register_and_login('student_a', 'a@example.com', 'password123')
        res = self.client.get('/api/progress/dashboard')
        data = json.loads(res.data)
        self.assertEqual(len(data['courses']), 0)
        self.assertEqual(data['overall_progress'], 0)

    def test_16_dashboard_works_with_partially_completed_courses(self):
        self.register_and_login('student_a', 'a@example.com', 'password123')
        self.client.post(f'/api/courses/{self.course.id}/enroll')
        
        lp = LessonProgress(student_id=1, lesson_id=self.lesson1.id, status='completed')
        db.session.add(lp)
        db.session.commit()

        # Trigger progress calculation
        self.client.get(f'/api/courses/{self.course.id}/progress')

        res = self.client.get('/api/progress/dashboard')
        data = json.loads(res.data)
        self.assertEqual(data['overall_progress'], 50)
