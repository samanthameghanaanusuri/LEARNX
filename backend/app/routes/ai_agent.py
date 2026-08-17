from flask import Blueprint, jsonify, request, session
from app.services import ai_agent

ai_bp = Blueprint('ai', __name__)

def get_auth_student():
    student_id = session.get('student_id')
    if not student_id:
        student_id = request.headers.get('X-Student-ID')
    if not student_id:
        return None
    try:
        return int(student_id)
    except (TypeError, ValueError):
        return None

def make_response(result):
    status_code = 200
    if not result.get('success', True):
        error_type = result.get('error_type')
        if error_type == 'rate_limit':
            status_code = 429
        elif error_type == 'provider_unavailable':
            status_code = 503
        elif error_type == 'authentication_error':
            status_code = 401
        elif error_type in ('network_error', 'provider_error'):
            status_code = 503
        else:
            status_code = 500
    return jsonify(result), status_code

@ai_bp.route('/status', methods=['GET'])
def status():
    pm = ai_agent.provider_manager
    
    primary_configured = pm.primary.is_configured()
    fallback_configured = pm.fallback.is_configured()
    configured = primary_configured or fallback_configured
    
    # Active provider is fallback if primary is missing or last error was transient and fallback exists
    active_provider = pm.primary.get_provider_name()
    if not primary_configured and fallback_configured:
        active_provider = pm.fallback.get_provider_name()
    elif ai_agent.last_diagnostic_error["type"] in ("rate_limit", "provider_unavailable", "network_error") and fallback_configured:
        active_provider = pm.fallback.get_provider_name()

    return jsonify({
        "configured": configured,
        "primary_provider": pm.primary.get_provider_name(),
        "primary_model": pm.primary.get_model_name(),
        "fallback_provider": pm.fallback.get_provider_name(),
        "fallback_model": pm.fallback.get_model_name(),
        "primary_configured": primary_configured,
        "fallback_configured": fallback_configured,
        "active_provider": active_provider,
        "last_error_type": ai_agent.last_diagnostic_error["type"],
        "last_error_status": ai_agent.last_diagnostic_error["status"]
    }), 200

@ai_bp.route('/ask', methods=['POST'])
def ask():
    student_id = get_auth_student()
    if not student_id:
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.json or {}
    question = data.get('question')
    course_id = data.get('course_id')
    lesson_id = data.get('lesson_id')
    
    if not question:
        return jsonify({"error": "Question is required"}), 400
        
    result = ai_agent.ask_tutor(student_id, course_id, lesson_id, question)
    return make_response(result)

@ai_bp.route('/explain', methods=['POST'])
def explain():
    student_id = get_auth_student()
    if not student_id:
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.json or {}
    concept = data.get('concept')
    course_id = data.get('course_id')
    lesson_id = data.get('lesson_id')
    
    if not concept:
        return jsonify({"error": "Concept is required"}), 400
        
    result = ai_agent.explain_concept(student_id, course_id, lesson_id, concept)
    return make_response(result)

@ai_bp.route('/hint', methods=['POST'])
def hint():
    student_id = get_auth_student()
    if not student_id:
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.json or {}
    course_id = data.get('course_id')
    lesson_id = data.get('lesson_id')
    hint_level = data.get('hint_level', 1)
        
    result = ai_agent.generate_hint(student_id, course_id, lesson_id, hint_level)
    return make_response(result)

@ai_bp.route('/weaknesses', methods=['GET'])
def weaknesses():
    student_id = get_auth_student()
    if not student_id:
        return jsonify({"error": "Unauthorized"}), 401
        
    result = ai_agent.analyze_weaknesses(student_id)
    return make_response(result)

@ai_bp.route('/recommendation', methods=['GET'])
def recommendation():
    student_id = get_auth_student()
    if not student_id:
        return jsonify({"error": "Unauthorized"}), 401
        
    result = ai_agent.recommend_action(student_id)
    return make_response(result)

@ai_bp.route('/learning-plan', methods=['GET'])
def learning_plan():
    student_id = get_auth_student()
    if not student_id:
        return jsonify({"error": "Unauthorized"}), 401
        
    result = ai_agent.generate_learning_plan(student_id)
    return make_response(result)

@ai_bp.route('/code-review', methods=['POST'])
def code_review():
    student_id = get_auth_student()
    if not student_id:
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.json or {}
    language = data.get('language')
    code = data.get('code')
    problem = data.get('problem')
    course_id = data.get('course_id')
    lesson_id = data.get('lesson_id')
    
    if not all([language, code, problem]):
        return jsonify({"error": "Missing required fields"}), 400
        
    result = ai_agent.review_code(student_id, course_id, lesson_id, language, code, problem)
    return make_response(result)
