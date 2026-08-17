from flask import Blueprint, jsonify, request, session
from app.models import (
    db, Course, CourseModule, Lesson, LessonExample, Exercise, 
    QuizQuestion, CourseEnrollment, LessonProgress, ExerciseSubmission,
    KnowledgeState, KnowledgeStateHistory, Student, TestCase,
    MiniProject, ProjectTestCase, ProjectSubmission
)
from app.services.knowledge_tracing import BayesianKnowledgeTracing
from app.services.executor import CodeExecutor
from app.services.web_executor import WebCodeExecutor
import json
from datetime import datetime

courses_bp = Blueprint('courses', __name__)

def get_auth_student():
    student_id = session.get('student_id')
    if not student_id:
        # Fallback to X-Student-ID header for development/API compatibility
        student_id = request.headers.get('X-Student-ID')
    if not student_id:
        return None
    try:
        return int(student_id)
    except (TypeError, ValueError):
        return None

@courses_bp.route('/', methods=['GET'], strict_slashes=False)
@courses_bp.route('', methods=['GET'], strict_slashes=False)
def get_courses():
    courses = Course.query.filter_by(is_published=True).all()
    return jsonify([c.to_dict() for c in courses]), 200

@courses_bp.route('/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return jsonify(course.to_dict()), 200

@courses_bp.route('/<int:course_id>/modules', methods=['GET'])
def get_course_modules(course_id):
    modules = CourseModule.query.filter_by(course_id=course_id).order_by(CourseModule.order_index).all()
    result = []
    for mod in modules:
        mod_dict = mod.to_dict()
        # Fetch lessons for module
        lessons = Lesson.query.filter_by(module_id=mod.id).order_by(Lesson.order_index).all()
        mod_dict['lessons'] = [l.to_dict() for l in lessons]
        result.append(mod_dict)
    return jsonify(result), 200

@courses_bp.route('/lessons/<int:lesson_id>', methods=['GET'])
def get_lesson(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    lesson_dict = lesson.to_dict()
    
    examples = LessonExample.query.filter_by(lesson_id=lesson_id).order_by(LessonExample.order_index).all()
    lesson_dict['examples'] = [ex.to_dict() for ex in examples]
    
    student_id = get_auth_student()
    exercises = Exercise.query.filter_by(lesson_id=lesson_id).order_by(Exercise.order_index).all()
    ex_list = []
    for ex in exercises:
        ex_dict = ex.to_dict()
        tcs = TestCase.query.filter_by(exercise_id=ex.id).order_by(TestCase.order_index).all()
        ex_dict['test_cases'] = [tc.to_dict(include_hidden=False) for tc in tcs]
        if student_id:
            sub = ExerciseSubmission.query.filter_by(student_id=student_id, exercise_id=ex.id).order_by(ExerciseSubmission.submitted_at.desc()).first()
            if sub:
                ex_dict['user_submission'] = sub.to_dict()
        ex_list.append(ex_dict)
    lesson_dict['exercises'] = ex_list
    
    quizzes = QuizQuestion.query.filter_by(lesson_id=lesson_id).all()
    # Strip correct answers from quizzes sent to client
    quiz_list = []
    for q in quizzes:
        q_dict = q.to_dict()
        q_dict.pop('correct_answer', None)
        quiz_list.append(q_dict)
    lesson_dict['quizzes'] = quiz_list

    projects = MiniProject.query.filter_by(lesson_id=lesson_id).order_by(MiniProject.order_index).all()
    lesson_dict['projects'] = [p.to_dict() for p in projects]

    return jsonify(lesson_dict), 200

@courses_bp.route('/<int:course_id>/enroll', methods=['POST'])
def enroll_course(course_id):
    student_id = get_auth_student()
    if not student_id:
        return jsonify({'error': 'Unauthorized'}), 401
    
    course = Course.query.get_or_404(course_id)
    enrollment = CourseEnrollment.query.filter_by(student_id=student_id, course_id=course.id).first()
    
    if not enrollment:
        enrollment = CourseEnrollment(student_id=student_id, course_id=course.id)
        db.session.add(enrollment)
        db.session.commit()
        return jsonify({'message': 'Successfully enrolled', 'enrollment': enrollment.to_dict()}), 201
    
    return jsonify({'message': 'Already enrolled', 'enrollment': enrollment.to_dict()}), 200

@courses_bp.route('/<int:course_id>/progress', methods=['GET'])
def get_progress(course_id):
    student_id = get_auth_student()
    if not student_id:
        return jsonify({'error': 'Unauthorized'}), 401
        
    enrollment = CourseEnrollment.query.filter_by(student_id=student_id, course_id=course_id).first()
    if not enrollment:
        return jsonify({'error': 'Not enrolled in this course'}), 403

    modules = CourseModule.query.filter_by(course_id=course_id).all()
    module_ids = [m.id for m in modules]
    lessons = Lesson.query.filter(Lesson.module_id.in_(module_ids)).all()
    
    total_lessons = len(lessons)
    completed = 0
    lesson_statuses = {}
    
    for l in lessons:
        prog = LessonProgress.query.filter_by(student_id=student_id, lesson_id=l.id).first()
        status = prog.status if prog else 'not_started'
        lesson_statuses[l.id] = status
        if status == 'completed':
            completed += 1

    percentage = (completed / total_lessons * 100) if total_lessons > 0 else 0
    enrollment.progress_percentage = percentage
    db.session.commit()
    
    # Deterministic Next Lesson
    next_lesson = None
    for m in sorted(modules, key=lambda x: x.order_index):
        for l in sorted([les for les in lessons if les.module_id == m.id], key=lambda x: x.order_index):
            if lesson_statuses.get(l.id) != 'completed':
                next_lesson = l.to_dict()
                break
        if next_lesson:
            break

    return jsonify({
        'progress_percentage': percentage,
        'completed_lessons': completed,
        'total_lessons': total_lessons,
        'lesson_statuses': lesson_statuses,
        'next_lesson': next_lesson
    }), 200

@courses_bp.route('/lessons/<int:lesson_id>/complete', methods=['POST'])
def complete_lesson(lesson_id):
    student_id = get_auth_student()
    if not student_id:
        return jsonify({'error': 'Unauthorized'}), 401
        
    try:
        lesson = Lesson.query.get_or_404(lesson_id)
        
        # Verify exercises requirement
        exercises = Exercise.query.filter_by(lesson_id=lesson_id).all()
        for ex in exercises:
            sub = ExerciseSubmission.query.filter_by(student_id=student_id, exercise_id=ex.id).filter(ExerciseSubmission.score > 0).first()
            if not sub:
                return jsonify({
                    'success': False,
                    'error': 'Incomplete requirements',
                    'message': f"Please complete practice exercise: '{ex.title}' before marking lesson complete."
                }), 400

        # Verify mini project requirement
        projects = MiniProject.query.filter_by(lesson_id=lesson_id).all()
        for proj in projects:
            p_sub = ProjectSubmission.query.filter_by(student_id=student_id, project_id=proj.id, status='passed').first()
            if not p_sub:
                return jsonify({
                    'success': False,
                    'error': 'Incomplete requirements',
                    'message': f"Please pass mini project: '{proj.title}' before marking lesson complete."
                }), 400

        prog = LessonProgress.query.filter_by(student_id=student_id, lesson_id=lesson_id).first()
        if not prog:
            prog = LessonProgress(student_id=student_id, lesson_id=lesson_id)
            db.session.add(prog)
        
        prog.status = 'completed'
        prog.completion_percentage = 100
        prog.completed_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({'message': 'Lesson marked as completed'}), 200
    except Exception as e:
        db.session.rollback()
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': 'Database operation failed'
        }), 500

@courses_bp.route('/lessons/<int:lesson_id>/quiz', methods=['POST'])
def submit_quiz(lesson_id):
    student_id = get_auth_student()
    if not student_id:
        return jsonify({'error': 'Unauthorized'}), 401

    try:
        data = request.json
        question_id = data.get('quiz_question_id')
        answer = data.get('answer')
        
        if not question_id or answer is None:
            return jsonify({'error': 'Missing quiz_question_id or answer'}), 400

        quiz = QuizQuestion.query.get_or_404(question_id)
        if quiz.lesson_id != lesson_id:
            return jsonify({'error': 'Quiz does not belong to this lesson'}), 400

        is_correct = (quiz.correct_answer == answer)
        
        # Update BKT Evidence
        if quiz.concept_id:
            _update_bkt(student_id, quiz.concept_id, is_correct, quiz_question_id=quiz.id, evidence_score=1.0 if is_correct else 0.0, evidence_source="quiz_submission")

        return jsonify({
            'correct': is_correct,
            'explanation': quiz.explanation,
            'correct_answer': quiz.correct_answer if not is_correct else None
        }), 200
    except Exception as e:
        db.session.rollback()
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': 'Database operation failed'
        }), 500

@courses_bp.route('/exercises/<int:exercise_id>/submit', methods=['POST'])
def submit_exercise(exercise_id):
    student_id = get_auth_student()
    if not student_id:
        return jsonify({'error': 'Unauthorized'}), 401

    try:
        data = request.json
        code = data.get('code')
        if not code:
            return jsonify({'error': 'Code is required'}), 400

        exercise = Exercise.query.get_or_404(exercise_id)
        test_cases = TestCase.query.filter_by(exercise_id=exercise.id).order_by(TestCase.order_index).all()
        
        if not test_cases:
            return jsonify({'error': 'No test cases configured for this exercise.'}), 400

        passed = 0
        total = len(test_cases)
        results = []
        total_exec_time = 0
        final_error = None
        final_status = 'success'

        if exercise.language in ['html', 'css', 'javascript']:
            web_executor = WebCodeExecutor(language=exercise.language, code=code, test_cases=test_cases)
            web_results = web_executor.execute_all()
            for tc_res in web_results:
                results.append(tc_res)
                total_exec_time += tc_res.get('execution_time_ms', 0)
                if tc_res['passed']:
                    passed += 1
                else:
                    if not final_error:
                        final_error = tc_res['status']
                        final_status = tc_res['status']
        else:
            for tc in test_cases:
                executor = CodeExecutor(language=exercise.language, code=code, stdin=tc.input_data)
                response = executor.execute()
                total_exec_time += response.get('execution_time_ms', 0)
                
                is_pass = False
                tc_status = response['status']
                
                if tc_status == 'success':
                    # Normalize CRLF to LF and strip trailing whitespace
                    actual_out = response['stdout'].replace('\r\n', '\n').strip()
                    expected_out = tc.expected_output.replace('\r\n', '\n').strip()
                    
                    if actual_out == expected_out:
                        is_pass = True
                        passed += 1
                    else:
                        tc_status = 'wrong_answer'
                        if not final_error:
                            final_error = 'wrong_answer'
                            final_status = 'wrong_answer'
                else:
                    if not final_error:
                        final_error = response['error_type']
                        final_status = tc_status

                tc_res = {
                    'test_case_id': tc.id,
                    'passed': is_pass,
                    'status': tc_status,
                    'execution_time_ms': response.get('execution_time_ms', 0)
                }
                
                # Reveal output only if not hidden
                if not tc.is_hidden:
                    tc_res['input'] = tc.input_data
                    tc_res['expected'] = tc.expected_output
                    tc_res['actual_stdout'] = response.get('stdout', '')
                    tc_res['actual_stderr'] = response.get('stderr', '')
                results.append(tc_res)

        score = passed / total if total > 0 else 0.0
        
        submission = ExerciseSubmission(
            student_id=student_id,
            exercise_id=exercise.id,
            code=code,
            language=exercise.language,
            status=final_status,
            test_result=json.dumps(results),
            passed_tests=passed,
            total_tests=total,
            score=score,
            execution_time_ms=total_exec_time,
            error_type=final_error
        )
        db.session.add(submission)
        
        # Update BKT Evidence
        if exercise.concept_id:
            _update_bkt(
                student_id, 
                exercise.concept_id, 
                is_correct=(passed == total), 
                exercise_id=exercise.id,
                evidence_score=score,
                evidence_source="coding_submission",
                passed_tests=passed,
                total_tests=total
            )

        db.session.commit()
        
        return jsonify({
            'status': final_status, 
            'passed': passed,
            'total': total,
            'score': score,
            'results': results,
            'execution_time_ms': total_exec_time
        }), 200
    except Exception as e:
        db.session.rollback()
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': 'Database operation failed'
        }), 500


def _update_bkt(student_id, concept_id, is_correct, quiz_question_id=None, exercise_id=None, project_id=None, evidence_score=None, evidence_source="quiz_submission", passed_tests=None, total_tests=None, auto_commit=True):
    try:
        bkt = BayesianKnowledgeTracing()
        ks = KnowledgeState.query.filter_by(student_id=student_id, concept_id=concept_id).first()
        
        if not ks:
            ks = KnowledgeState(student_id=student_id, concept_id=concept_id, mastery_score=bkt.p_init)
            db.session.add(ks)
            db.session.flush()

        previous_mastery = ks.mastery_score
        
        if evidence_score is None:
            evidence_score = 1.0 if is_correct else 0.0
            
        mapped_evidence = bkt.map_score_to_evidence(evidence_score, evidence_source)
        updated_mastery = bkt.update_mastery(previous_mastery, mapped_evidence)
        ks.mastery_score = updated_mastery
        
        history_record = KnowledgeStateHistory(
            student_id=student_id,
            concept_id=concept_id,
            previous_mastery=previous_mastery,
            updated_mastery=updated_mastery,
            quiz_question_id=quiz_question_id,
            exercise_id=exercise_id,
            project_id=project_id,
            answer_correct=is_correct,
            evidence_score=evidence_score,
            evidence_source=evidence_source,
            passed_tests=passed_tests,
            total_tests=total_tests
        )
        db.session.add(history_record)
        if auto_commit:
            db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


@courses_bp.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = MiniProject.query.get_or_404(project_id)
    return jsonify(project.to_dict()), 200


@courses_bp.route('/projects/<int:project_id>/progress', methods=['GET'])
def get_project_progress(project_id):
    student_id = get_auth_student()
    if not student_id:
        return jsonify({'error': 'Unauthorized'}), 401
    
    project = MiniProject.query.get_or_404(project_id)
    submissions = ProjectSubmission.query.filter_by(student_id=student_id, project_id=project.id).order_by(ProjectSubmission.submitted_at.desc()).all()
    
    latest = submissions[0].to_dict() if submissions else None
    return jsonify({
        'status': latest['status'] if latest else 'not_started',
        'latest_submission': latest,
        'history': [s.to_dict() for s in submissions]
    }), 200


@courses_bp.route('/projects/<int:project_id>/submit', methods=['POST'])
def submit_project(project_id):
    student_id = get_auth_student()
    if not student_id:
        return jsonify({'error': 'Unauthorized'}), 401

    try:
        data = request.json or {}
        code = data.get('code')
        if not code:
            return jsonify({'error': 'Code is required'}), 400

        project = MiniProject.query.get_or_404(project_id)
        test_cases = ProjectTestCase.query.filter_by(project_id=project.id).order_by(ProjectTestCase.order_index).all()

        if not test_cases:
            return jsonify({'error': 'No test cases configured for this project.'}), 400

        passed = 0
        total = len(test_cases)
        results = []
        feedback = []
        total_exec_time = 0
        final_error = None
        
        if project.language in ['html', 'css', 'javascript']:
            web_executor = WebCodeExecutor(language=project.language, code=code, test_cases=test_cases)
            web_results = web_executor.execute_all()
            for idx, tc in enumerate(test_cases):
                tc_res_node = next((r for r in web_results if r['test_case_id'] == tc.id), None)
                is_pass = False
                tc_status = 'runtime_error'
                exec_time = 0
                tc_stderr = ''
                if tc_res_node:
                    is_pass = tc_res_node['passed']
                    tc_status = tc_res_node['status']
                    exec_time = tc_res_node['execution_time_ms']
                    if is_pass:
                        passed += 1
                    else:
                        if not final_error:
                            final_error = tc_status
                    if not tc.is_hidden:
                        tc_stderr = tc_res_node.get('actual_stderr', '')
                
                total_exec_time += exec_time
                tc_desc = tc.description or f"Feature Test {idx + 1}"
                
                feedback.append({
                    'test_case': tc_desc,
                    'passed': is_pass,
                    'status': tc_status,
                    'message': "Passed successfully" if is_pass else ("Incorrect output" if tc_status == 'wrong_answer' else (tc_stderr or 'Execution error'))
                })
                
                tc_res = {
                    'test_case_id': tc.id,
                    'description': tc_desc,
                    'passed': is_pass,
                    'status': tc_status,
                    'execution_time_ms': exec_time
                }
                if not tc.is_hidden:
                    tc_res['input'] = tc.input_data
                    tc_res['expected'] = tc.expected_output
                    tc_res['actual_stdout'] = tc_res_node.get('actual_stdout', '') if tc_res_node else ''
                    tc_res['actual_stderr'] = tc_stderr
                results.append(tc_res)
        else:
            for idx, tc in enumerate(test_cases):
                executor = CodeExecutor(language=project.language, code=code, stdin=tc.input_data)
                response = executor.execute()
                exec_time = response.get('execution_time_ms', 0)
                total_exec_time += exec_time
                
                is_pass = False
                tc_status = response['status']
                
                if tc_status == 'success':
                    actual_out = response.get('stdout', '').replace('\r\n', '\n').strip()
                    expected_out = tc.expected_output.replace('\r\n', '\n').strip()
                    if actual_out == expected_out:
                        is_pass = True
                        passed += 1
                    else:
                        tc_status = 'wrong_answer'
                        if not final_error:
                            final_error = 'wrong_answer'
                else:
                    if not final_error:
                        final_error = response.get('error_type', tc_status)

                tc_desc = tc.description or f"Feature Test {idx + 1}"
                feedback.append({
                    'test_case': tc_desc,
                    'passed': is_pass,
                    'status': tc_status,
                    'message': "Passed successfully" if is_pass else ("Incorrect output" if tc_status == 'wrong_answer' else response.get('error_type', 'Execution error'))
                })

                tc_res = {
                    'test_case_id': tc.id,
                    'description': tc_desc,
                    'passed': is_pass,
                    'status': tc_status,
                    'execution_time_ms': exec_time
                }
                if not tc.is_hidden:
                    tc_res['input'] = tc.input_data
                    tc_res['expected'] = tc.expected_output
                    tc_res['actual_stdout'] = response.get('stdout', '')
                    tc_res['actual_stderr'] = response.get('stderr', '')

                results.append(tc_res)

        score = passed / total if total > 0 else 0.0
        status = 'passed' if passed == total and total > 0 else 'failed'

        submission = ProjectSubmission(
            student_id=student_id,
            project_id=project.id,
            code=code,
            language=project.language,
            status=status,
            test_result=json.dumps(results),
            passed_tests=passed,
            total_tests=total,
            score=score,
            execution_time_ms=total_exec_time,
            feedback=feedback
        )
        db.session.add(submission)

        # Update BKT Evidence
        if project.concept_id:
            _update_bkt(
                student_id,
                project.concept_id,
                is_correct=(passed == total),
                project_id=project.id,
                evidence_score=score,
                evidence_source="project_submission",
                passed_tests=passed,
                total_tests=total
            )

        db.session.commit()

        return jsonify({
            'status': status,
            'score': score,
            'passed_tests': passed,
            'total_tests': total,
            'execution_time_ms': total_exec_time,
            'feedback': feedback,
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


@courses_bp.route('/lessons/<int:lesson_id>/quiz/bulk', methods=['POST'])
def submit_quiz_bulk(lesson_id):
    student_id = get_auth_student()
    if not student_id:
        return jsonify({'error': 'Unauthorized'}), 401

    try:
        data = request.json
        answers = data.get('answers', {})
        
        quizzes = QuizQuestion.query.filter_by(lesson_id=lesson_id).all()
        if not quizzes:
            return jsonify({'error': 'No quizzes found for this lesson'}), 404

        results = []
        correct_count = 0
        total_count = len(quizzes)
        
        for quiz in quizzes:
            ans = answers.get(str(quiz.id))
            is_correct = (quiz.correct_answer == ans)
            if is_correct:
                correct_count += 1
                
            if quiz.concept_id:
                _update_bkt(student_id, quiz.concept_id, is_correct, quiz_question_id=quiz.id, evidence_score=1.0 if is_correct else 0.0, evidence_source="quiz_submission", auto_commit=False)
                
            results.append({
                'question_id': quiz.id,
                'correct': is_correct,
                'selected_answer': ans,
                'correct_answer': quiz.correct_answer if not is_correct else None,
                'explanation': quiz.explanation
            })

        score = correct_count / total_count if total_count > 0 else 0.0
        
        # Single commit for all BKT updates in this bulk quiz
        db.session.commit()
        
        return jsonify({
            'success': True,
            'score': score,
            'correct': correct_count,
            'total': total_count,
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
