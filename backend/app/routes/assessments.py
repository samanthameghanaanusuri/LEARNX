from flask import Blueprint, request, jsonify, session
from app.models import db, Question, AnswerAttempt, KnowledgeState, Concept, Subject

assessments_bp = Blueprint('assessments', __name__)

@assessments_bp.route('/subjects/<int:subject_id>/questions', methods=['GET'])
def get_subject_questions(subject_id):
    # Verify subject exists
    subject = Subject.query.get(subject_id)
    if not subject:
        return jsonify({'error': 'Subject not found'}), 404

    # Fetch concepts for this subject
    concepts = Concept.query.filter_by(subject_id=subject_id).all()
    concept_ids = [c.id for c in concepts]

    # Fetch questions for these concepts
    questions = Question.query.filter(Question.concept_id.in_(concept_ids)).all()

    # Format output grouped by concept
    questions_by_concept = {}
    for c in concepts:
        questions_by_concept[c.id] = {
            'concept_name': c.name,
            'description': c.description,
            'questions': []
        }

    for q in questions:
        questions_by_concept[q.concept_id]['questions'].append(q.to_dict())

    return jsonify({
        'subject': subject.to_dict(),
        'concepts_questions': questions_by_concept
    }), 200

@assessments_bp.route('/submit', methods=['POST'])
def submit_assessment():
    student_id = session.get('student_id') or request.headers.get('X-Student-ID')
    if not student_id:
        return jsonify({'error': 'Unauthorized'}), 401

    try:
        student_id = int(student_id)
    except ValueError:
        return jsonify({'error': 'Invalid student identifier'}), 400

    try:
        data = request.json or {}
        submissions = data.get('answers', []) # List of {question_id: int, student_answer: str}

        if not submissions:
            return jsonify({'error': 'No answers submitted'}), 400

        # Update KnowledgeState for each affected concept sequentially using BKT
        from app.services.knowledge_tracing import BayesianKnowledgeTracing
        from app.models import KnowledgeStateHistory

        bkt = BayesianKnowledgeTracing()
        p_init = bkt.get_params()['p_init']
        
        # Track current mastery locally in this batch session to support sequential BKT trace
        local_mastery_map = {}
        results = []

        for sub in submissions:
            q_id = sub.get('question_id')
            ans = sub.get('student_answer')

            if q_id is None or ans is None:
                continue

            question = Question.query.get(q_id)
            if not question:
                continue

            is_correct = (str(ans).strip().lower() == str(question.correct_answer).strip().lower())

            attempt = AnswerAttempt(
                student_id=student_id,
                question_id=q_id,
                student_answer=str(ans),
                is_correct=is_correct
            )
            db.session.add(attempt)
            db.session.flush()

            concept_id = question.concept_id
            if concept_id in local_mastery_map:
                previous_mastery = local_mastery_map[concept_id]
            else:
                ks = KnowledgeState.query.filter_by(student_id=student_id, concept_id=concept_id).first()
                if ks:
                    previous_mastery = ks.mastery_score
                else:
                    previous_mastery = p_init

            # Run BKT updates
            updated_mastery_val = bkt.update_mastery(previous_mastery, is_correct)
            local_mastery_map[concept_id] = updated_mastery_val

            # Record History
            history = KnowledgeStateHistory(
                student_id=student_id,
                concept_id=concept_id,
                previous_mastery=previous_mastery,
                updated_mastery=updated_mastery_val,
                question_id=q_id,
                answer_correct=is_correct
            )
            db.session.add(history)

            results.append({
                'question_id': q_id,
                'student_answer': ans,
                'correct_answer': question.correct_answer,
                'is_correct': is_correct,
                'concept_id': concept_id
            })

        # Persist the final mastery scores to KnowledgeState
        for concept_id, final_mastery in local_mastery_map.items():
            ks = KnowledgeState.query.filter_by(student_id=student_id, concept_id=concept_id).first()
            if ks:
                ks.mastery_score = final_mastery
            else:
                ks = KnowledgeState(
                    student_id=student_id,
                    concept_id=concept_id,
                    mastery_score=final_mastery
                )
                db.session.add(ks)

        db.session.commit()

        # Trigger Diagnosis if we have a subject_id
        subject_id = None
        for r in results:
            concept = Concept.query.get(r['concept_id'])
            if concept:
                subject_id = concept.subject_id
                break

        if subject_id:
            from app.services.diagnostic_engine import diagnose_learning_failure
            from app.services.recovery_engine import create_intervention_for_diagnosis
            
            # Diagnose learning failure based on new knowledge state
            diagnosis = diagnose_learning_failure(student_id, subject_id)
            if diagnosis:
                # Auto-generate a recovery intervention for the root cause concept
                create_intervention_for_diagnosis(
                    diagnosis_id=diagnosis.id,
                    student_id=student_id,
                    concept_id=diagnosis.root_cause_concept_id
                )

        # Summary
        total = len(results)
        correct = sum(1 for r in results if r['is_correct'])

        return jsonify({
            'message': 'Assessment processed successfully',
            'summary': {
                'total_submitted': total,
                'correct_count': correct,
                'score_percent': (correct / total * 100) if total > 0 else 0,
                'concept_masteries': local_mastery_map
            },
            'results': results
        }), 200
    except Exception as e:
        db.session.rollback()
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': 'Database operation failed'
        }), 500
