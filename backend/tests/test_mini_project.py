import unittest
import json
from app import create_app
from config import Config
from app.models import db, Student, Course, CourseModule, Lesson, MiniProject, ProjectTestCase, ProjectSubmission, KnowledgeStateHistory, LessonProgress, Exercise, ExerciseSubmission, Subject, Concept

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class MiniProjectTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            
            # Create student
            self.student = Student(username='teststudent', email='test@learnx.io', password_hash='hash')
            db.session.add(self.student)
            db.session.flush()
            self.student_id = self.student.id

            # Create concept
            subject = Subject(name='Test Subject', code='TEST')
            db.session.add(subject)
            db.session.flush()
            
            concept = Concept(subject_id=subject.id, name='Test Concept')
            db.session.add(concept)
            db.session.flush()

            # Create lesson and mini project
            course = Course(title='Python Test Course', slug='python-test', category='Programming', description='Test Course', difficulty='Beginner')
            db.session.add(course)
            db.session.flush()

            module = CourseModule(course_id=course.id, title='Test Module', description='Module', order_index=1)
            db.session.add(module)
            db.session.flush()

            self.lesson = Lesson(module_id=module.id, title='Test Lesson', slug='test-lesson', content='Lesson Content', order_index=1)
            db.session.add(self.lesson)
            db.session.flush()

            self.project = MiniProject(
                lesson_id=self.lesson.id,
                concept_id=concept.id,
                title='Test Banner Generator',
                objective='Generate system banner',
                scenario='Build CLI banner',
                requirements_json='[]',
                features_json='[]',
                guidance_json='[]',
                starter_code='def generate_banner(app, ver, status):\n    pass\n',
                language='python',
                expected_behavior='Banner output',
                evaluation_criteria='Exact string match'
            )
            db.session.add(self.project)
            db.session.flush()

            self.tc1 = ProjectTestCase(
                project_id=self.project.id,
                input_data='learnx\n1.0\nONLINE\n',
                expected_output='====================\nLEARNX v1.0 [ONLINE]\n====================',
                description='Standard Banner',
                is_hidden=False,
                order_index=1
            )
            self.tc2 = ProjectTestCase(
                project_id=self.project.id,
                input_data='portal\n2.5\nINIT\n',
                expected_output='==================\nPORTAL v2.5 [INIT]\n==================',
                description='Hidden Banner',
                is_hidden=True,
                order_index=2
            )
            db.session.add_all([self.tc1, self.tc2])
            db.session.commit()

            self.lesson_id = self.lesson.id
            self.project_id = self.project.id
            self.tc2_id = self.tc2.id

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_lesson_includes_projects(self):
        res = self.client.get(f'/api/courses/lessons/{self.lesson_id}')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn('projects', data)
        self.assertEqual(len(data['projects']), 1)
        self.assertEqual(data['projects'][0]['title'], 'Test Banner Generator')

    def test_get_project_by_id(self):
        res = self.client.get(f'/api/courses/projects/{self.project_id}')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['id'], self.project_id)
        self.assertEqual(data['title'], 'Test Banner Generator')

    def test_submit_project_pass(self):
        passing_code = (
            "import sys\n"
            "data = sys.stdin.read().split()\n"
            "if len(data) >= 3:\n"
            "    app_name, version, status = data[0], data[1], data[2]\n"
            "    line = f'{app_name.upper()} v{version} [{status}]'\n"
            "    border = '=' * len(line)\n"
            "    print(f'{border}\\n{line}\\n{border}')\n"
        )
        
        headers = {'X-Student-ID': str(self.student_id)}
        res = self.client.post(
            f'/api/courses/projects/{self.project_id}/submit',
            headers=headers,
            json={'code': passing_code}
        )
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['status'], 'passed')
        self.assertEqual(data['passed_tests'], 2)
        self.assertEqual(data['score'], 1.0)
        self.assertEqual(len(data['feedback']), 2)

        with self.app.app_context():
            history = KnowledgeStateHistory.query.filter_by(student_id=self.student_id, project_id=self.project_id).first()
            self.assertIsNotNone(history)
            self.assertEqual(history.evidence_source, 'project_submission')

    def test_submit_project_fail(self):
        failing_code = "print('Wrong Output')"
        headers = {'X-Student-ID': str(self.student_id)}
        res = self.client.post(
            f'/api/courses/projects/{self.project_id}/submit',
            headers=headers,
            json={'code': failing_code}
        )
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['status'], 'failed')
        self.assertEqual(data['passed_tests'], 0)
        self.assertEqual(data['score'], 0.0)

        # Check hidden test case details are not exposed in results
        hidden_res = [r for r in data['results'] if r['test_case_id'] == self.tc2_id][0]
        self.assertNotIn('input', hidden_res)
        self.assertNotIn('expected', hidden_res)

    def test_project_progress_history_preservation(self):
        headers = {'X-Student-ID': str(self.student_id)}
        # Submit twice
        self.client.post(f'/api/courses/projects/{self.project_id}/submit', headers=headers, json={'code': "print('1')"})
        self.client.post(f'/api/courses/projects/{self.project_id}/submit', headers=headers, json={'code': "print('2')"})

        res = self.client.get(f'/api/courses/projects/{self.project_id}/progress', headers=headers)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(len(data['history']), 2)

    def test_complete_lesson_enforcement(self):
        headers = {'X-Student-ID': str(self.student_id)}
        
        # Calling complete before project/exercise pass must fail with 400
        res = self.client.post(f'/api/courses/lessons/{self.lesson_id}/complete', headers=headers)
        self.assertEqual(res.status_code, 400)
        data = res.get_json()
        self.assertIn('message', data)

    def test_submit_web_project_pass(self):
        with self.app.app_context():
            # Create a web project
            web_project = MiniProject(
                lesson_id=self.lesson_id,
                title='Test Web Project',
                objective='Render Hello',
                scenario='Build web app',
                requirements_json='[]',
                features_json='[]',
                guidance_json='[]',
                starter_code='<h1>Starter</h1>',
                language='html',
                expected_behavior='Render page',
                evaluation_criteria='DOM check'
            )
            db.session.add(web_project)
            db.session.flush()
            
            tc = ProjectTestCase(
                project_id=web_project.id,
                input_data="return document.querySelector('h1').textContent === 'Hello';",
                expected_output='true',
                description='Check hello header',
                is_hidden=False,
                order_index=1
            )
            db.session.add(tc)
            db.session.commit()
            web_project_id = web_project.id

        headers = {'X-Student-ID': str(self.student_id)}
        res = self.client.post(
            f'/api/courses/projects/{web_project_id}/submit',
            headers=headers,
            json={'code': '<h1>Hello</h1>'}
        )
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['status'], 'passed')
        self.assertEqual(data['passed_tests'], 1)
        self.assertEqual(data['score'], 1.0)

if __name__ == '__main__':
    unittest.main()
