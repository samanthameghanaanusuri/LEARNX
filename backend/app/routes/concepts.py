from flask import Blueprint, jsonify
from app.models import Subject, Concept

concepts_bp = Blueprint('concepts', __name__)

@concepts_bp.route('/subjects', methods=['GET'])
def get_subjects():
    subjects = Subject.query.all()
    return jsonify({'subjects': [s.to_dict() for s in subjects]}), 200

@concepts_bp.route('/subjects/<int:subject_id>/map', methods=['GET'])
def get_subject_map(subject_id):
    subject = Subject.query.get(subject_id)
    if not subject:
        return jsonify({'error': 'Subject not found'}), 404
    
    concepts = Concept.query.filter_by(subject_id=subject_id).all()
    concept_list = [c.to_dict() for c in concepts]
    
    return jsonify({
        'subject': subject.to_dict(),
        'concepts': concept_list
    }), 200
