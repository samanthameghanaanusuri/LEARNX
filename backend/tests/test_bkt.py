import sys
import os
# Add backend folder to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from app.services.knowledge_tracing import BayesianKnowledgeTracing
from app import create_app, db
from app.models import Student, Subject, Concept, Question, KnowledgeState, AnswerAttempt
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class TestBayesianKnowledgeTracing(unittest.TestCase):
    def setUp(self):
        self.bkt = BayesianKnowledgeTracing(
            p_init=0.40,
            p_learn=0.10,
            p_forget=0.00,
            p_guess=0.20,
            p_slip=0.10
        )
        
        # Flask App setup for DB tests
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_case_a_repeated_correct_increases_mastery(self):
        """Case A: Repeated correct answers should generally increase mastery."""
        current = 0.40
        for i in range(5):
            updated = self.bkt.update_mastery(current, evidence=1.0)
            self.assertGreater(updated, current, f"Mastery did not increase on correct answer attempt {i+1}")
            current = updated

    def test_case_b_repeated_incorrect_decreases_mastery(self):
        """Case B: Repeated incorrect answers should generally decrease mastery."""
        current = 0.40
        for i in range(5):
            updated = self.bkt.update_mastery(current, evidence=0.0)
            self.assertLess(updated, current, f"Mastery did not decrease on incorrect answer attempt {i+1}")
            current = updated

    def test_case_c_small_attempts_no_extreme_certainty(self):
        """Case C: A small number of attempts should not immediately produce extreme certainty."""
        # Extreme certainty is defined here as score > 0.95 or score < 0.01
        m1 = self.bkt.update_mastery(0.40, evidence=1.0)
        self.assertLess(m1, 0.95, "First correct answer produced extreme high certainty")
        self.assertGreater(m1, 0.01, "First correct answer produced extreme low certainty")
        
        m2 = self.bkt.update_mastery(m1, evidence=1.0)
        self.assertLess(m2, 0.95, "Second correct answer produced extreme high certainty")
        
        m_inc = self.bkt.update_mastery(0.40, evidence=0.0)
        self.assertGreater(m_inc, 0.01, "First incorrect answer produced extreme low certainty")

    def test_case_d_different_sequences_different_states(self):
        """Case D: Two students with different answer sequences should produce different knowledge states."""
        # Seq 1: Correct, Incorrect, Correct
        s1_m = 0.40
        s1_m = self.bkt.update_mastery(s1_m, evidence=1.0)
        s1_m = self.bkt.update_mastery(s1_m, evidence=0.0)
        s1_m = self.bkt.update_mastery(s1_m, evidence=1.0)

        # Seq 2: Incorrect, Correct, Incorrect
        s2_m = 0.40
        s2_m = self.bkt.update_mastery(s2_m, evidence=0.0)
        s2_m = self.bkt.update_mastery(s2_m, evidence=1.0)
        s2_m = self.bkt.update_mastery(s2_m, evidence=0.0)

        self.assertNotEqual(s1_m, s2_m, "Different answer sequences yielded identical mastery states")

    def test_case_e_prerequisites_independently_tracked(self):
        """Case E: Prerequisite concepts should remain independently tracked."""
        # Set up a test database schema with Subject, Concept, Question
        student = Student(username="testuser", email="test@learnx.com")
        student.set_password("password123")
        
        subject = Subject(name="Test Subject", code="TSBJ", description="Testing")
        db.session.add_all([student, subject])
        db.session.commit()

        # Concept A is dependent on Concept B (B -> A)
        concept_b = Concept(subject_id=subject.id, name="Prerequisite Concept B")
        concept_a = Concept(subject_id=subject.id, name="Target Concept A")
        concept_a.prerequisites.append(concept_b)
        
        db.session.add_all([concept_a, concept_b])
        db.session.commit()

        # Create question for A and question for B
        q_a = Question(concept_id=concept_a.id, question_text="What is A?", options_json='["1","2"]', correct_answer="1", difficulty_level="Beginner")
        q_b = Question(concept_id=concept_b.id, question_text="What is B?", options_json='["1","2"]', correct_answer="2", difficulty_level="Beginner")
        db.session.add_all([q_a, q_b])
        db.session.commit()

        # Answering question on target Concept A
        # Using the POST API logic context:
        # Check initial states (should be None in database)
        ks_a_before = KnowledgeState.query.filter_by(student_id=student.id, concept_id=concept_a.id).first()
        ks_b_before = KnowledgeState.query.filter_by(student_id=student.id, concept_id=concept_b.id).first()
        
        self.assertIsNone(ks_a_before)
        self.assertIsNone(ks_b_before)

        # Log answer attempt for question A (correct answer)
        client = self.app.test_client()
        response = client.post('/api/performance/attempt', json={
            'student_id': student.id,
            'question_id': q_a.id,
            'student_answer': '1'
        })
        
        self.assertEqual(response.status_code, 200)

        # Check knowledge states in database after attempt on A
        ks_a_after = KnowledgeState.query.filter_by(student_id=student.id, concept_id=concept_a.id).first()
        ks_b_after = KnowledgeState.query.filter_by(student_id=student.id, concept_id=concept_b.id).first()

        # Mastery of A should now exist and be updated
        self.assertIsNotNone(ks_a_after)
        self.assertGreater(ks_a_after.mastery_score, 0.40)

        # Mastery of B should remain completely untracked (None)
        self.assertIsNone(ks_b_after, "Prerequisite concept B was updated when target A was answered")

if __name__ == '__main__':
    unittest.main()
