from flask import Blueprint, request, jsonify, session
from app.models import Diagnosis, Subject, Concept
from app.services.diagnostic_engine import diagnose_learning_failure

diagnosis_bp = Blueprint('diagnosis', __name__)

@diagnosis_bp.route('/run', methods=['POST'])
def run_diagnosis():
    student_id = session.get('student_id') or request.headers.get('X-Student-ID')
    if not student_id:
        return jsonify({'error': 'Unauthorized'}), 401

    try:
        student_id = int(student_id)
    except ValueError:
        return jsonify({'error': 'Invalid student identifier'}), 400

    try:
        data = request.json or {}
        subject_id = data.get('subject_id')

        if not subject_id:
            return jsonify({'error': 'Missing subject_id'}), 400

        subject = Subject.query.get(subject_id)
        if not subject:
            return jsonify({'error': 'Subject not found'}), 404

        # Run the diagnostic trace
        from app.models import db
        diagnosis = diagnose_learning_failure(student_id, subject_id)
        
        if not diagnosis:
            return jsonify({
                'message': 'No active learning failures detected. Ensure you have completed assessments with less than 60% accuracy to run a diagnosis.',
                'diagnosis': None
            }), 200

        # Auto-generate a recovery intervention for the root cause concept
        from app.services.recovery_engine import create_intervention_for_diagnosis
        active_intervention = create_intervention_for_diagnosis(
            diagnosis_id=diagnosis.id,
            student_id=student_id,
            concept_id=diagnosis.root_cause_concept_id
        )

        root_concept = Concept.query.get(diagnosis.root_cause_concept_id)

        return jsonify({
            'message': 'Diagnosis complete',
            'diagnosis': diagnosis.to_dict(),
            'root_cause_concept': root_concept.to_dict() if root_concept else None,
            'intervention_id': active_intervention.id if active_intervention else None
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

@diagnosis_bp.route('/history', methods=['GET'])
def get_diagnosis_history():
    student_id = session.get('student_id') or request.headers.get('X-Student-ID')
    if not student_id:
        return jsonify({'error': 'Unauthorized'}), 401

    try:
        student_id = int(student_id)
    except ValueError:
        return jsonify({'error': 'Invalid student identifier'}), 400

    diagnoses = Diagnosis.query.filter_by(student_id=student_id).order_by(Diagnosis.timestamp.desc()).all()
    
    formatted_diagnoses = []
    for d in diagnoses:
        root_concept = Concept.query.get(d.root_cause_concept_id)
        subject = Subject.query.get(d.subject_id)
        d_dict = d.to_dict()
        d_dict['root_cause_concept_name'] = root_concept.name if root_concept else 'Unknown'
        d_dict['subject_name'] = subject.name if subject else 'Unknown'
        formatted_diagnoses.append(d_dict)

    return jsonify({'history': formatted_diagnoses}), 200
