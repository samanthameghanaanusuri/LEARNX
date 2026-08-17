from flask import Blueprint, request, jsonify, session
from app.models import db, Student, PasswordResetToken
import secrets
import hashlib
from datetime import datetime, timedelta


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json or {}
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400

    if len(password) < 8:
        return jsonify({'error': 'Password must be at least 8 characters long'}), 400

    try:
        if Student.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists'}), 400

        if Student.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already exists'}), 400

        student = Student(username=username, email=email)
        student.set_password(password)
        db.session.add(student)
        db.session.commit()

        session.permanent = True
        session['student_id'] = student.id
        return jsonify({'message': 'Registration successful', 'student': student.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': 'Database operation failed'
        }), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json or {}
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    student = Student.query.filter_by(username=username).first()
    if not student or not student.check_password(password):
        return jsonify({'error': 'Invalid credentials'}), 401

    session.permanent = True
    session['student_id'] = student.id
    return jsonify({'message': 'Login successful', 'student': student.to_dict()}), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('student_id', None)
    return jsonify({'message': 'Logged out successfully'}), 200

@auth_bp.route('/me', methods=['GET'])
def get_current_student():
    student_id = session.get('student_id') or request.headers.get('X-Student-ID')
    if not student_id:
        return jsonify({'error': 'Unauthorized'}), 401
    
    try:
        student_id = int(student_id)
    except ValueError:
        return jsonify({'error': 'Invalid student identifier'}), 400

    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    return jsonify({'student': student.to_dict()}), 200

@auth_bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.json or {}
    email = data.get('email')

    if not email:
        return jsonify({'error': 'Missing email address'}), 400

    try:
        student = Student.query.filter_by(email=email).first()
        
        # We should always return a successful response to prevent email enumeration attacks
        if not student:
            return jsonify({'message': 'If your email is registered, you will receive a password reset link.'}), 200

        # Generate a cryptographically secure random token
        raw_token = secrets.token_urlsafe(32)
        
        # Hash the token before storing it in the database (SHA-256 is sufficient here)
        token_hash = hashlib.sha256(raw_token.encode('utf-8')).hexdigest()
        
        # Expiration time (e.g., 1 hour from now)
        expires_at = datetime.utcnow() + timedelta(hours=1)
        
        reset_token = PasswordResetToken(
            student_id=student.id,
            token_hash=token_hash,
            expires_at=expires_at
        )
        db.session.add(reset_token)
        db.session.commit()

        # DEVELOPMENT ONLY: Print the reset link to the console
        print(f"\n=======================================================")
        print(f"DEVELOPMENT ONLY: Password reset link generated!")
        print(f"URL: http://127.0.0.1:5000/reset_password.html?token={raw_token}")
        print(f"=======================================================\n")

        return jsonify({'message': 'If your email is registered, you will receive a password reset link.'}), 200
    except Exception as e:
        db.session.rollback()
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': 'Database operation failed'
        }), 500

@auth_bp.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.json or {}
    token = data.get('token')
    new_password = data.get('new_password')

    if not token or not new_password:
        return jsonify({'error': 'Missing token or new password'}), 400

    if len(new_password) < 8:
        return jsonify({'error': 'Password must be at least 8 characters long'}), 400

    try:
        # Hash the provided token to look it up in the database
        token_hash = hashlib.sha256(token.encode('utf-8')).hexdigest()
        
        reset_record = PasswordResetToken.query.filter_by(token_hash=token_hash, used=False).first()

        if not reset_record:
            return jsonify({'error': 'Invalid or already used token'}), 400

        if reset_record.expires_at < datetime.utcnow():
            return jsonify({'error': 'Token has expired'}), 400

        # Token is valid, update the student's password
        student = Student.query.get(reset_record.student_id)
        if not student:
            return jsonify({'error': 'Student not found'}), 404

        student.set_password(new_password)
        reset_record.used = True
        
        db.session.commit()

        return jsonify({'message': 'Password has been successfully reset. You can now login.'}), 200
    except Exception as e:
        db.session.rollback()
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': 'Database operation failed'
        }), 500

