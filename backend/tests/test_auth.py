import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import json
from datetime import datetime, timedelta
import secrets
import hashlib
from app import create_app
from app.models import db, Student, PasswordResetToken

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'test_secret'

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

        # Seed a test user
        self.student = Student(username='test_user', email='test@example.com')
        self.student.set_password('old_password123')
        db.session.add(self.student)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register_password_length(self):
        # Test password less than 8 characters
        response = self.client.post('/api/auth/register', json={
            'username': 'new_user',
            'email': 'new@example.com',
            'password': 'short'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('at least 8 characters long', data['error'])

    def test_forgot_password_valid_email(self):
        response = self.client.post('/api/auth/forgot-password', json={
            'email': 'test@example.com'
        })
        self.assertEqual(response.status_code, 200)
        
        # Verify token was created in DB
        token_record = PasswordResetToken.query.filter_by(student_id=self.student.id).first()
        self.assertIsNotNone(token_record)
        self.assertFalse(token_record.used)

    def test_forgot_password_invalid_email(self):
        response = self.client.post('/api/auth/forgot-password', json={
            'email': 'doesnotexist@example.com'
        })
        # Should return 200 to prevent email enumeration
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('receive a password reset link', data['message'])

    def test_reset_password_success(self):
        # Generate token directly
        raw_token = secrets.token_urlsafe(32)
        token_hash = hashlib.sha256(raw_token.encode('utf-8')).hexdigest()
        expires_at = datetime.utcnow() + timedelta(hours=1)
        
        reset_token = PasswordResetToken(
            student_id=self.student.id,
            token_hash=token_hash,
            expires_at=expires_at
        )
        db.session.add(reset_token)
        db.session.commit()

        response = self.client.post('/api/auth/reset-password', json={
            'token': raw_token,
            'new_password': 'new_secure_password'
        })
        
        self.assertEqual(response.status_code, 200)
        
        # Verify token is marked as used
        db.session.refresh(reset_token)
        self.assertTrue(reset_token.used)
        
        # Verify old password fails
        login_response = self.client.post('/api/auth/login', json={
            'username': 'test_user',
            'password': 'old_password123'
        })
        self.assertEqual(login_response.status_code, 401)
        
        # Verify new password works
        login_response = self.client.post('/api/auth/login', json={
            'username': 'test_user',
            'password': 'new_secure_password'
        })
        self.assertEqual(login_response.status_code, 200)

    def test_reset_password_expired_token(self):
        raw_token = secrets.token_urlsafe(32)
        token_hash = hashlib.sha256(raw_token.encode('utf-8')).hexdigest()
        expires_at = datetime.utcnow() - timedelta(hours=1) # Expired 1 hour ago
        
        reset_token = PasswordResetToken(
            student_id=self.student.id,
            token_hash=token_hash,
            expires_at=expires_at
        )
        db.session.add(reset_token)
        db.session.commit()

        response = self.client.post('/api/auth/reset-password', json={
            'token': raw_token,
            'new_password': 'new_secure_password'
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('expired', data['error'])

    def test_reset_password_reused_token(self):
        raw_token = secrets.token_urlsafe(32)
        token_hash = hashlib.sha256(raw_token.encode('utf-8')).hexdigest()
        expires_at = datetime.utcnow() + timedelta(hours=1)
        
        reset_token = PasswordResetToken(
            student_id=self.student.id,
            token_hash=token_hash,
            expires_at=expires_at,
            used=True # Already used
        )
        db.session.add(reset_token)
        db.session.commit()

        response = self.client.post('/api/auth/reset-password', json={
            'token': raw_token,
            'new_password': 'new_secure_password'
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('already used', data['error'])

if __name__ == '__main__':
    unittest.main()
