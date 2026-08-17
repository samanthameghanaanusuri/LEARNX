from flask import Blueprint, request, jsonify, session
from app.models import db, Student, Subject, Concept, KnowledgeState, KnowledgeStateHistory
from app.services.knowledge_tracing import BayesianKnowledgeTracing
from datetime import datetime

progress_bp = Blueprint('progress', __name__)

@progress_bp.route('/summary', methods=['GET'])
def get_progress_summary():
    student_id = session.get('student_id') or request.headers.get('X-Student-ID')
    if not student_id:
        return jsonify({'error': 'Unauthorized'}), 401

    try:
        student_id = int(student_id)
    except ValueError:
        return jsonify({'error': 'Invalid student identifier'}), 400

    subjects = Subject.query.all()
    bkt = BayesianKnowledgeTracing()
    p_init = bkt.get_params()['p_init']

    subject_data = []
    all_concepts_data = []

    for s in subjects:
        concepts = Concept.query.filter_by(subject_id=s.id).all()
        concept_ids = [c.id for c in concepts]

        # Load knowledge state records
        ks_records = KnowledgeState.query.filter(
            KnowledgeState.student_id == student_id,
            KnowledgeState.concept_id.in_(concept_ids)
        ).all()

        ks_map = {ks.concept_id: ks.mastery_score for ks in ks_records}
        
        sum_mastery = 0.0
        mastered_count = 0
        
        for c in concepts:
            mastery = ks_map.get(c.id, p_init)
            sum_mastery += mastery
            if mastery >= 0.6:
                mastered_count += 1
            
            all_concepts_data.append({
                'concept_id': c.id,
                'concept_name': c.name,
                'subject_name': s.name,
                'mastery_score': mastery,
                'status': "Mastered" if mastery >= 0.6 else "Weak"
            })

        avg_mastery = sum_mastery / len(concepts) if concepts else p_init

        subject_data.append({
            'subject_id': s.id,
            'subject_name': s.name,
            'subject_code': s.code,
            'avg_mastery': avg_mastery,
            'mastered_concepts': mastered_count,
            'total_concepts': len(concepts)
        })

    # Sort concepts to find strongest/weakest
    all_concepts_data.sort(key=lambda x: x['mastery_score'], reverse=True)
    strongest_concepts = all_concepts_data[:3]
    weakest_concepts = list(reversed(all_concepts_data))[:3]

    # Recently changing concepts (last 10 updates)
    recent_histories = KnowledgeStateHistory.query.filter_by(student_id=student_id)\
        .order_by(KnowledgeStateHistory.timestamp.desc())\
        .limit(10).all()

    recently_changing = []
    seen_concepts = set()
    for h in recent_histories:
        if h.concept_id not in seen_concepts:
            seen_concepts.add(h.concept_id)
            concept = Concept.query.get(h.concept_id)
            change = h.updated_mastery - h.previous_mastery
            recently_changing.append({
                'concept_id': h.concept_id,
                'concept_name': concept.name if concept else 'Unknown',
                'previous_mastery': h.previous_mastery,
                'updated_mastery': h.updated_mastery,
                'change': change,
                'timestamp': h.timestamp.isoformat()
            })

    # Pick the most recently active concept and extract its full trajectory
    trajectory_data = {}
    if recently_changing:
        target_concept_id = recently_changing[0]['concept_id']
        target_concept = Concept.query.get(target_concept_id)
        
        target_history = KnowledgeStateHistory.query.filter_by(
            student_id=student_id,
            concept_id=target_concept_id
        ).order_by(KnowledgeStateHistory.timestamp.asc()).all()

        trajectory_data = {
            'concept_name': target_concept.name if target_concept else 'Unknown',
            'points': [{
                'updated_mastery': pt.updated_mastery,
                'timestamp': pt.timestamp.isoformat(),
                'correct': pt.answer_correct
            } for pt in target_history]
        }

    return jsonify({
        'subjects': subject_data,
        'strongest_concepts': strongest_concepts,
        'weakest_concepts': weakest_concepts,
        'recently_changing': recently_changing,
        'trajectory': trajectory_data
    }), 200

from datetime import date

@progress_bp.route('/ping', methods=['POST'])
def ping_activity():
    student_id = session.get('student_id') or request.headers.get('X-Student-ID')
    if not student_id:
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.json or {}
    active_seconds = data.get('active_seconds', 0)
    
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    # Accumulate time (converting seconds to minutes roughly, or maintaining a total minutes)
    # We will assume frontend sends active_seconds, we add it up. Wait, if it's seconds, 
    # we need a floating point or track seconds. Since learning_time_minutes is Integer,
    # let's have the frontend just send minutes, or we divide here. 
    # Let's say active_minutes = active_seconds / 60
    # A better approach: frontend sends 1 if 1 minute elapsed.
    # Let's assume frontend sends active_minutes = 1.
    active_minutes = data.get('active_minutes', 0)
    student.learning_time_minutes = (student.learning_time_minutes or 0) + active_minutes

    today = date.today()
    if student.last_activity_date != today:
        if student.last_activity_date:
            delta = today - student.last_activity_date
            if delta.days == 1:
                student.current_streak = (student.current_streak or 0) + 1
            else:
                student.current_streak = 1
        else:
            student.current_streak = 1

        if student.current_streak > (student.longest_streak or 0):
            student.longest_streak = student.current_streak
            
        student.last_activity_date = today

    db.session.commit()
    return jsonify({'success': True, 'current_streak': student.current_streak, 'learning_time_minutes': student.learning_time_minutes}), 200

@progress_bp.route('/dashboard', methods=['GET'])
def get_dashboard_data():
    student_id = session.get('student_id') or request.headers.get('X-Student-ID')
    if not student_id:
        return jsonify({'error': 'Unauthorized'}), 401
    
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    from app.models import (
        CourseEnrollment, Course, CourseModule, Lesson, LessonProgress, 
        ExerciseSubmission, AnswerAttempt, KnowledgeState, KnowledgeStateHistory, Concept
    )
    
    enrollments = CourseEnrollment.query.filter_by(student_id=student.id).all()
    courses_data = []
    overall_progress = 0
    
    for e in enrollments:
        c = Course.query.get(e.course_id)
        if c:
            # Count completed and total lessons for this course
            modules = CourseModule.query.filter_by(course_id=c.id).all()
            module_ids = [m.id for m in modules]
            if module_ids:
                lessons = Lesson.query.filter(Lesson.module_id.in_(module_ids)).all()
            else:
                lessons = []
            
            total_lessons = len(lessons)
            completed_lessons = 0
            for l in lessons:
                lp = LessonProgress.query.filter_by(student_id=student.id, lesson_id=l.id).first()
                if lp and lp.status == 'completed':
                    completed_lessons += 1

            courses_data.append({
                'id': c.id,
                'title': c.title,
                'slug': c.slug,
                'progress': e.progress_percentage or 0,
                'completed_lessons': completed_lessons,
                'total_lessons': total_lessons
            })
            overall_progress += (e.progress_percentage or 0)
            
    if enrollments:
        overall_progress = overall_progress / len(enrollments)

    # Continue Learning
    last_lesson_progress = LessonProgress.query.filter_by(student_id=student.id, status='in_progress')\
        .order_by(LessonProgress.id.desc()).first()
    
    continue_learning = None
    if last_lesson_progress:
        lesson = Lesson.query.get(last_lesson_progress.lesson_id)
        if lesson:
            course = lesson.module.course
            continue_learning = {
                'course_title': course.title,
                'course_slug': course.slug,
                'module_title': lesson.module.title,
                'lesson_title': lesson.title,
                'lesson_id': lesson.id,
                'progress': last_lesson_progress.completion_percentage or 0
            }

    # Performance
    exercises_passed = ExerciseSubmission.query.filter_by(student_id=student.id, status='success').count()
    total_exercises = ExerciseSubmission.query.filter_by(student_id=student.id).count()
    
    correct_quizzes = AnswerAttempt.query.filter_by(student_id=student.id, is_correct=True).count()
    total_quizzes = AnswerAttempt.query.filter_by(student_id=student.id).count()
    
    avg_score = 0
    if total_exercises + total_quizzes > 0:
        avg_score = ((exercises_passed + correct_quizzes) / (total_exercises + total_quizzes)) * 100

    # Diagnostic - use the existing /summary logic loosely
    bkt = BayesianKnowledgeTracing()
    ks_records = KnowledgeState.query.filter_by(student_id=student.id).all()
    
    concepts_mapped = []
    for ks in ks_records:
        con = Concept.query.get(ks.concept_id)
        if con:
            concepts_mapped.append({'name': con.name, 'score': ks.mastery_score})
            
    concepts_mapped.sort(key=lambda x: x['score'], reverse=True)
    strong_concepts = [con_item['name'] for con_item in concepts_mapped if con_item['score'] >= 0.6][:3]
    weak_concepts = [con_item['name'] for con_item in reversed(concepts_mapped) if con_item['score'] < 0.6][:3]

    # Recent Activity Feed
    activities = []
    
    # 1. Lesson completions
    recent_lessons = LessonProgress.query.filter_by(student_id=student.id, status='completed')\
        .order_by(LessonProgress.completed_at.desc()).limit(5).all()
    for lp in recent_lessons:
        les = Lesson.query.get(lp.lesson_id)
        if les:
            activities.append({
                'type': 'lesson_completed',
                'description': f"Completed lesson: '{les.title}'",
                'timestamp': lp.completed_at.isoformat() if lp.completed_at else datetime.utcnow().isoformat()
            })
            
    # 2. Exercises/Quizzes submissions from BKT history
    recent_history = KnowledgeStateHistory.query.filter_by(student_id=student.id)\
        .order_by(KnowledgeStateHistory.timestamp.desc()).limit(5).all()
    for h in recent_history:
        concept = Concept.query.get(h.concept_id)
        concept_name = concept.name if concept else "Concept"
        
        if h.evidence_source == "quiz_submission":
            desc = f"Answered quiz on concept: '{concept_name}' ({'Correct' if h.answer_correct else 'Incorrect'})"
        elif h.evidence_source == "coding_submission":
            desc = f"Submitted code for exercise on concept: '{concept_name}' ({h.passed_tests}/{h.total_tests} passed)"
        elif h.evidence_source == "project_submission":
            desc = f"Submitted project for concept: '{concept_name}' ({'Passed' if h.answer_correct else 'Failed'})"
        else:
            desc = f"Active learning on concept: '{concept_name}'"
            
        activities.append({
            'type': h.evidence_source or 'activity',
            'description': desc,
            'timestamp': h.timestamp.isoformat()
        })
        
    # Sort activities by timestamp descending and take top 5
    activities.sort(key=lambda x: x['timestamp'], reverse=True)
    recent_activity_data = activities[:5]

    return jsonify({
        'student': student.to_dict(),
        'total_courses': Course.query.filter_by(is_published=True).count(),
        'courses_enrolled': len(enrollments),
        'overall_progress': round(overall_progress),
        'learning_time_minutes': student.learning_time_minutes or 0,
        'current_streak': student.current_streak or 0,
        'longest_streak': student.longest_streak or 0,
        'courses': courses_data,
        'continue_learning': continue_learning,
        'performance': {
            'exercises_attempted': total_exercises,
            'exercises_passed': exercises_passed,
            'quizzes_attempted': total_quizzes,
            'quizzes_passed': correct_quizzes,
            'average_score': round(avg_score)
        },
        'diagnostic': {
            'strong': strong_concepts,
            'weak': weak_concepts
        },
        'recent_activity': recent_activity_data
    }), 200
