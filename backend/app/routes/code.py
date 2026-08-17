from flask import Blueprint, jsonify, request, session
from app.models import db, ExerciseSubmission
from app.services.executor import CodeExecutor
from app.routes.courses import get_auth_student

code_bp = Blueprint('code', __name__)

@code_bp.route('/run', methods=['POST'])
def run_code():
    data = request.json
    language = data.get('language')
    code = data.get('code')
    stdin = data.get('stdin', '')

    if not language or not code:
        return jsonify({'error': 'Language and code are required.'}), 400

    executor = CodeExecutor(language=language, code=code, stdin=stdin)
    response = executor.execute()
    
    return jsonify(response), 200

@code_bp.route('/history/<int:exercise_id>', methods=['GET'])
def get_code_history(exercise_id):
    student_id = get_auth_student()
    if not student_id:
        return jsonify({'error': 'Unauthorized'}), 401

    submissions = ExerciseSubmission.query.filter_by(
        student_id=student_id, 
        exercise_id=exercise_id
    ).order_by(ExerciseSubmission.submitted_at.desc()).all()
    
    return jsonify([sub.to_dict() for sub in submissions]), 200
