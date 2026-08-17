from flask import Blueprint, request, jsonify
from app.models import db, Student, Question, Concept, AnswerAttempt, KnowledgeState, KnowledgeStateHistory
from app.services.knowledge_tracing import BayesianKnowledgeTracing

performance_bp = Blueprint('performance', __name__)

@performance_bp.route('/attempt', methods=['POST'])
def record_attempt():
    data = request.json or {}
    student_id = data.get('student_id')
    question_id = data.get('question_id')
    student_answer = data.get('student_answer')

    if not student_id or not question_id or student_answer is None:
        return jsonify({'error': 'Missing required fields: student_id, question_id, student_answer'}), 400

    try:
        student = Student.query.get(student_id)
        if not student:
            return jsonify({'error': 'Student not found'}), 404

        question = Question.query.get(question_id)
        if not question:
            return jsonify({'error': 'Question not found'}), 404

        concept = Concept.query.get(question.concept_id)
        if not concept:
            return jsonify({'error': 'Concept not found'}), 404

        # Determine correctness: exact match or normalized case-insensitive match
        is_correct = (str(student_answer).strip().lower() == str(question.correct_answer).strip().lower())

        # Create AnswerAttempt
        attempt = AnswerAttempt(
            student_id=student_id,
            question_id=question_id,
            student_answer=str(student_answer),
            is_correct=is_correct
        )
        db.session.add(attempt)
        db.session.flush() # Flush to assign ID

        # Retrieve student's previous mastery state
        ks = KnowledgeState.query.filter_by(student_id=student_id, concept_id=concept.id).first()
        bkt = BayesianKnowledgeTracing()
        bkt_params = bkt.get_params()

        if ks:
            previous_mastery = ks.mastery_score
        else:
            previous_mastery = bkt_params['p_init']

        # Update using BKT equations
        updated_mastery = bkt.update_mastery(previous_mastery, is_correct)

        # Persist updated KnowledgeState
        if ks:
            ks.mastery_score = updated_mastery
        else:
            ks = KnowledgeState(
                student_id=student_id,
                concept_id=concept.id,
                mastery_score=updated_mastery
            )
            db.session.add(ks)

        # Record history
        history = KnowledgeStateHistory(
            student_id=student_id,
            concept_id=concept.id,
            previous_mastery=previous_mastery,
            updated_mastery=updated_mastery,
            question_id=question_id,
            answer_correct=is_correct
        )
        db.session.add(history)
        db.session.commit()

        return jsonify({
            'concept': concept.to_dict(),
            'correctness': is_correct,
            'previous_mastery': previous_mastery,
            'updated_mastery': updated_mastery,
            'mastery_change': updated_mastery - previous_mastery
        }), 200
    except Exception as e:
        db.session.rollback()
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': 'Database operation failed'
        }), 500

@performance_bp.route('/knowledge-state/<int:student_id>/<int:subject_id>', methods=['GET'])
def get_knowledge_state(student_id, subject_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    concepts = Concept.query.filter_by(subject_id=subject_id).all()
    bkt = BayesianKnowledgeTracing()
    p_init = bkt.get_params()['p_init']

    results = []
    for c in concepts:
        ks = KnowledgeState.query.filter_by(student_id=student_id, concept_id=c.id).first()
        attempts_count = AnswerAttempt.query.join(Question).filter(
            AnswerAttempt.student_id == student_id,
            Question.concept_id == c.id
        ).count()

        if ks:
            mastery_score = ks.mastery_score
            last_updated = ks.last_updated.isoformat()
            status = "Mastered" if mastery_score >= 0.6 else "Weak"
        else:
            mastery_score = p_init
            last_updated = None
            status = "Unassessed"

        results.append({
            'concept_id': c.id,
            'concept_name': c.name,
            'mastery_score': mastery_score,
            'mastery_status': status,
            'last_updated': last_updated,
            'evidence_count': attempts_count
        })

    return jsonify({'concepts': results}), 200

@performance_bp.route('/knowledge-history/<int:student_id>/<int:concept_id>', methods=['GET'])
def get_knowledge_history(student_id, concept_id):
    history = KnowledgeStateHistory.query.filter_by(
        student_id=student_id,
        concept_id=concept_id
    ).order_by(KnowledgeStateHistory.timestamp.asc()).all()

    trajectory = [{
        'id': h.id,
        'previous_mastery': h.previous_mastery,
        'updated_mastery': h.updated_mastery,
        'answer_correct': h.answer_correct,
        'question_id': h.question_id,
        'timestamp': h.timestamp.isoformat()
    } for h in history]

    return jsonify({'trajectory': trajectory}), 200
