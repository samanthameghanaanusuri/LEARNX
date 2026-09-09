import os
import json
import logging
from flask import current_app
from app.models import Course, Lesson, Concept, KnowledgeState, AnswerAttempt, ExerciseSubmission
from .ai_providers.manager import ProviderManager, last_diagnostic_error

logger = logging.getLogger(__name__)

BEGINNER_THRESHOLD = 0.40
INTERMEDIATE_THRESHOLD = 0.70

provider_manager = ProviderManager()

def get_full_learning_context(course_id=None, lesson_id=None):
    course_title = "Python Programming"
    lesson_title = "General Programming Concepts"
    concept_name = "Programming Fundamentals"
    course_topics = []

    lesson = None
    if lesson_id:
        try:
            lesson = Lesson.query.get(int(lesson_id))
        except (ValueError, TypeError):
            lesson = None

    if lesson:
        lesson_title = lesson.title
        if lesson.concept_id:
            c = Concept.query.get(lesson.concept_id)
            if c:
                concept_name = c.name
        if lesson.module and lesson.module.course:
            course = lesson.module.course
            course_title = course.title
            for m in course.modules:
                for l in m.lessons:
                    course_topics.append(l.title)
    elif course_id:
        try:
            course = Course.query.get(int(course_id))
            if course:
                course_title = course.title
                for m in course.modules:
                    for l in m.lessons:
                        course_topics.append(l.title)
        except (ValueError, TypeError):
            pass

    if not course_topics:
        course_topics = ["Variables", "Data Types", "Control Flow", "Functions", "Loops", "Classes", "Methods"]

    return {
        "course_title": course_title,
        "lesson_title": lesson_title,
        "concept_name": concept_name,
        "course_topics": course_topics
    }

def check_question_relevance(question: str, ctx: dict) -> tuple:
    if not question:
        return False, "Question is empty."

    q_lower = question.lower().strip()

    # 1. Obvious Off-Topic Triggers (reject immediately)
    off_topic_words = [
        "biryani", "recipe", "cook", "cooking", "pizza", "burger", "chicken", "curry", "pasta", "dish", "food",
        "narendra modi", "modi", "biden", "trump", "politics", "political", "election", "prime minister", "president",
        "movie", "film", "actor", "actress", "celebrity", "bollywood", "hollywood", "romantic story", "love story",
        "cricket", "cricket score", "ipl", "match score", "football", "world cup",
        "joke", "tell me a joke", "relationship advice", "best phone", "phone to buy", "weather today"
    ]
    for ot in off_topic_words:
        if ot in q_lower:
            return False, f"Question is about '{ot}' which is unrelated to {ctx['course_title']}."

    # 2. Strong Programming & Course Context Matchers (allow immediately)
    relevant_indicators = [
        "python", "java", "c++", "cpp", "css", "html", "javascript", "js", "sql", "dbms", "dsa",
        "code", "coding", "program", "programming", "programmer", "developer", "software",
        "variable", "loop", "for", "while", "function", "method", "class", "object", "array", "list", "tuple",
        "dict", "dictionary", "string", "int", "float", "boolean", "if", "else", "elif", "switch", "syntax",
        "indent", "indentation", "error", "exception", "bug", "debug", "compiler", "interpreter", "print",
        "recursion", "algorithm", "database", "query", "exercise", "hint", "quiz", "lesson", "course",
        "concept", "mastery", "practice", "explain", "difference", "example", "how to", "why", "used for",
        "machine learning", "data science", "web development", "backend", "frontend", "fail", "failing",
        "help", "understand", "learn", "study", "what is", "where is", "can python", "can java", "can c++"
    ]

    for word in ctx["course_title"].lower().split():
        if len(word) > 2 and word not in ["and", "the", "for", "with"]:
            relevant_indicators.append(word)
    for word in ctx["lesson_title"].lower().split():
        if len(word) > 2 and word not in ["and", "the", "for", "with", "lesson"]:
            relevant_indicators.append(word)

    for ind in relevant_indicators:
        if ind in q_lower:
            return True, f"Relevant to course context ({ind})"

    # 3. Learning Intent Patterns
    learning_patterns = ["what should", "how do", "why do", "explain", "give me", "show me", "can i", "is it possible"]
    if any(pat in q_lower for pat in learning_patterns):
        return True, "Relevant learning intent question"

    return False, "Question does not relate to the current learning context."

def get_lesson_context(lesson_id):
    if not lesson_id:
        return "Unknown Lesson"
    lesson = Lesson.query.get(lesson_id)
    if lesson:
        course = lesson.module.course if lesson.module else None
        concept_name = Concept.query.get(lesson.concept_id).name if lesson.concept_id else "None"
        return f"Course: {course.title if course else 'Unknown'}\nLesson: {lesson.title}\nConcepts: {concept_name}"
    return "Unknown Lesson"

def get_weak_concepts(student_id):
    states = KnowledgeState.query.filter_by(student_id=student_id).all()
    return [f"{s.concept.name}" for s in states if s.mastery_score < INTERMEDIATE_THRESHOLD and s.concept]

def get_mastery_list(student_id):
    states = KnowledgeState.query.filter_by(student_id=student_id).all()
    return [f"{s.concept.name} ({s.mastery_score:.2f})" for s in states if s.concept]

def get_recent_failures(student_id):
    recent = AnswerAttempt.query.filter_by(student_id=student_id, is_correct=False).order_by(AnswerAttempt.timestamp.desc()).limit(3).all()
    return ", ".join([f"Exercise {f.exercise_id}" for f in recent]) if recent else "None"

def call_ai(prompt, is_json=True):
    return provider_manager.generate(prompt, is_json)

def ask_tutor(student_id, course_id, lesson_id, question):
    ctx = get_full_learning_context(course_id, lesson_id)
    is_relevant, reason = check_question_relevance(question, ctx)

    if not is_relevant:
        rejection_msg = f"""I'm your LEARNX Learning Agent, so I can help only with topics related to your current course and learning progress.

Your current course is **{ctx['course_title']}**.

Please ask a course-related question—for example:
• Explain this {ctx['course_title']} concept
• Help me understand this lesson
• Give me a hint for this exercise
• Explain why my code is failing"""
        return {
            "success": True,
            "available": True,
            "answer": rejection_msg,
            "concepts": [ctx['course_title']],
            "difficulty": "General",
            "next_action": f"Ask a question related to {ctx['course_title']}"
        }

    lesson_ctx = get_lesson_context(lesson_id)
    mastery = get_mastery_list(student_id)
    failures = get_recent_failures(student_id)
    
    prompt = f"""You are the LEARNX Learning Agent for the course '{ctx['course_title']}'.
Course: {ctx['course_title']}
Lesson: {ctx['lesson_title']}
Concept: {ctx['concept_name']}
Course Topics: {', '.join(ctx['course_topics'])}

Student Mastery: {', '.join(mastery) if mastery else 'None'}
Recent Failures: {failures}

Student Question: {question}

Provide an educational explanation (100-200 words maximum). Stay strictly relevant to {ctx['course_title']} and computer science learning. Adapt to the student's mastery.
Respond ONLY in valid JSON matching this schema exactly:
{{
    "answer": "Your detailed explanation here (use markdown formatting)",
    "concepts": ["Concept 1", "Concept 2"],
    "difficulty": "Beginner/Intermediate/Advanced",
    "next_action": "A brief suggestion on what the student should do next"
}}
"""
    return call_ai(prompt, is_json=True)

def explain_concept(student_id, course_id, lesson_id, concept):
    lesson_ctx = get_lesson_context(lesson_id)
    
    mastery_score = 0.0
    if student_id:
        state = KnowledgeState.query.join(Concept).filter(KnowledgeState.student_id == student_id, Concept.name == concept).first()
        if state:
            mastery_score = state.mastery_score
            
    level = "Beginner"
    if mastery_score >= INTERMEDIATE_THRESHOLD:
        level = "Advanced"
    elif mastery_score >= BEGINNER_THRESHOLD:
        level = "Intermediate"

    guidance = "simple language, step-by-step."
    if level == "Intermediate":
        guidance = "deeper reasoning, practical examples, common mistakes."
    elif level == "Advanced":
        guidance = "edge cases, implementation details, optimization, real-world application."

    prompt = f"""Concept: {concept}
Lesson: {lesson_ctx}
Mastery Level: {level} ({mastery_score:.2f})

Provide an explanation scaled for a {level} student (150-250 words maximum). Guidelines: {guidance}
You MUST provide EXACTLY two concrete examples.
Return ONLY valid JSON:
{{
    "what": "What it is",
    "why": "Why it matters",
    "how": "How it works",
    "examples": ["Example 1 string", "Example 2 string"],
    "mistake": "Common mistake",
    "check_question": "Quick check question"
}}
"""
    return call_ai(prompt, is_json=True)

def generate_hint(student_id, course_id, lesson_id, hint_level):
    lesson_ctx = get_lesson_context(lesson_id)
    failures = get_recent_failures(student_id)
    
    level_desc = "Level 1: Conceptual direction"
    if hint_level == 2:
        level_desc = "Level 2: Identify the relevant concept"
    elif hint_level == 3:
        level_desc = "Level 3: Partial reasoning / pseudocode"
    elif hint_level == 4:
        level_desc = "Level 4: Detailed approach"
    elif hint_level >= 5:
        level_desc = "Level 5: Complete solution guidance"

    prompt = f"""The student needs a progressive hint for the current exercise.
Lesson: {lesson_ctx}
Recent Failures: {failures}

Provide Hint Level {hint_level} (50-120 words maximum).
Instruction: {level_desc}

Return ONLY valid JSON format:
{{
    "hint": "The hint text here..."
}}
"""
    return call_ai(prompt, is_json=True)

def analyze_weaknesses(student_id):
    if not student_id:
        return {"success": True, "weaknesses": [], "analysis": "Student not identified.", "priority": [], "practice_plan": []}

    states = KnowledgeState.query.filter_by(student_id=student_id).all()
    weak_concepts = [{"concept": s.concept.name if s.concept else "Unknown", "mastery": s.mastery_score} for s in states if s.mastery_score < INTERMEDIATE_THRESHOLD]
    
    if not weak_concepts:
        return {
            "success": True, 
            "available": True,
            "weaknesses": [],
            "analysis": "Great job! We haven't identified any major weak concepts right now.",
            "priority": [],
            "practice_plan": []
        }

    prompt = f"""Weak Concepts Data:
{json.dumps(weak_concepts)}

Generate a structural analysis explaining WHY the student may be struggling and HOW to practice (150-250 words maximum).
Return ONLY valid JSON:
{{
    "weaknesses": ["Concept 1", "Concept 2"],
    "analysis": "Markdown analysis explaining why they are struggling...",
    "priority": ["Highest priority concept to revise"],
    "practice_plan": ["Step 1...", "Step 2..."]
}}
"""
    return call_ai(prompt, is_json=True)

def recommend_action(student_id):
    if not student_id:
        return {"available": False, "message": "Student not identified."}

    states = KnowledgeState.query.filter_by(student_id=student_id).all()
    weak_states = [s for s in states if s.mastery_score < INTERMEDIATE_THRESHOLD and s.concept]
    
    action = "PRACTICE"
    target_concept = "General"
    reason = "Keep practicing to improve your skills."
    
    if weak_states:
        weak_states.sort(key=lambda s: s.mastery_score)
        worst_state = weak_states[0]
        target_concept = worst_state.concept.name
        
        if worst_state.mastery_score < BEGINNER_THRESHOLD:
            action = "REVIEW_LESSON"
            reason = f"Mastery of '{target_concept}' is low ({worst_state.mastery_score:.2f}). Review lesson."
        else:
            action = "PRACTICE"
            reason = f"Need practice for '{target_concept}'."
    else:
        action = "MOVE_FORWARD"
        reason = "Mastery looks great. Ready for next topic!"

    prompt = f"""Action: {action} focusing on '{target_concept}'.
Reason: {reason}

Generate the recommendation (100-180 words maximum).
Return ONLY valid JSON:
{{
    "recommended_lesson": {{"title": "Lesson related to {target_concept}"}},
    "reason": "AI generated reason based on the system reason",
    "prerequisite_concepts": ["List of prerequisites if any"],
    "estimated_focus": "e.g., 15 minutes"
}}
"""
    return call_ai(prompt, is_json=True)

def generate_learning_plan(student_id):
    mastery = get_mastery_list(student_id)
    weak_concepts = get_weak_concepts(student_id)
    
    prompt = f"""Generate a realistic, short-term personalized learning plan.
Mastery: {', '.join(mastery) if mastery else 'None'}
Weak Concepts: {', '.join(weak_concepts) if weak_concepts else 'None'}

Provide a structured concise response.
Return ONLY valid JSON:
{{
    "today": ["Task 1", "Task 2"],
    "practice": ["Exercise A", "Exercise B"],
    "revision": ["Concept to review"],
    "next": ["Next topic to learn"]
}}
"""
    return call_ai(prompt, is_json=True)

def review_code(student_id, course_id, lesson_id, language, code, problem):
    prompt = f"""Statically review the following code. DO NOT EXECUTE THE CODE.
Problem: {problem}
Language: {language}
Code:
```
{code}
```

Analyze correctness, bugs, logic, readability (structured concise response).
First provide problem identified, a hint, and suggested improvement.
Return ONLY valid JSON:
{{
    "score": 85,
    "bugs": ["Bug 1..."],
    "strengths": ["Good variable naming..."],
    "improvements": ["Improvement 1..."],
    "concepts_to_review": ["Concept 1"],
    "corrected_code": null
}}
"""
    return call_ai(prompt, is_json=True)
