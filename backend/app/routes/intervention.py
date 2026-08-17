from flask import Blueprint, request, jsonify, session
from app.models import Intervention, Concept
from app.services.recovery_engine import evaluate_recovery_attempt
import json

intervention_bp = Blueprint('intervention', __name__)

@intervention_bp.route('/active', methods=['GET'])
def get_active_intervention():
    student_id = session.get('student_id') or request.headers.get('X-Student-ID')
    if not student_id:
        return jsonify({'error': 'Unauthorized'}), 401

    try:
        student_id = int(student_id)
    except ValueError:
        return jsonify({'error': 'Invalid student identifier'}), 400

    # Retrieve latest active or in-progress intervention
    intervention = Intervention.query.filter(
        Intervention.student_id == student_id,
        Intervention.status.in_(['assigned', 'in_progress'])
    ).order_by(Intervention.timestamp.desc()).first()

    if not intervention:
        return jsonify({'intervention': None, 'message': 'No active recovery interventions.'}), 200

    concept = Concept.query.get(intervention.concept_id)
    
    # Parse json content
    content_data = {}
    try:
        content_data = json.loads(intervention.intervention_content)
    except Exception:
        content_data = {"guide": intervention.intervention_content, "post_question": "", "options": []}

    int_dict = intervention.to_dict()
    int_dict['concept_name'] = concept.name if concept else 'Unknown'
    int_dict['content_parsed'] = content_data

    return jsonify({'intervention': int_dict}), 200

@intervention_bp.route('/complete', methods=['POST'])
def complete_intervention():
    student_id = session.get('student_id') or request.headers.get('X-Student-ID')
    if not student_id:
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.json or {}
    intervention_id = data.get('intervention_id')
    student_answer = data.get('student_answer')

    if not intervention_id or student_answer is None:
        return jsonify({'error': 'Missing intervention_id or student_answer'}), 400

    try:
        success, message = evaluate_recovery_attempt(intervention_id, student_answer)
        
        return jsonify({
            'success': success,
            'message': message
        }), 200
    except Exception as e:
        from app.models import db
        db.session.rollback()
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': 'Database operation failed'
        }), 500
