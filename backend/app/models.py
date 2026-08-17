from datetime import datetime
import json
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# Self-referential table for concept prerequisites (DAG)
concept_prerequisites = db.Table('concept_prerequisites',
    db.Column('concept_id', db.Integer, db.ForeignKey('concept.id', ondelete='CASCADE'), primary_key=True),
    db.Column('prerequisite_id', db.Integer, db.ForeignKey('concept.id', ondelete='CASCADE'), primary_key=True)
)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    learning_time_minutes = db.Column(db.Integer, default=0)
    current_streak = db.Column(db.Integer, default=0)
    longest_streak = db.Column(db.Integer, default=0)
    last_activity_date = db.Column(db.Date, nullable=True)

    # Relationships
    attempts = db.relationship('AnswerAttempt', backref='student', lazy=True, cascade="all, delete-orphan")
    knowledge_states = db.relationship('KnowledgeState', backref='student', lazy=True, cascade="all, delete-orphan")
    knowledge_state_histories = db.relationship('KnowledgeStateHistory', backref='student', lazy=True, cascade="all, delete-orphan")
    diagnoses = db.relationship('Diagnosis', backref='student', lazy=True, cascade="all, delete-orphan")
    interventions = db.relationship('Intervention', backref='student', lazy=True, cascade="all, delete-orphan")
    password_reset_tokens = db.relationship('PasswordResetToken', backref='student', lazy=True, cascade="all, delete-orphan")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'learning_time_minutes': self.learning_time_minutes,
            'current_streak': self.current_streak,
            'longest_streak': self.longest_streak,
            'last_activity_date': self.last_activity_date.isoformat() if self.last_activity_date else None,
            'created_at': self.created_at.isoformat()
        }

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False) # e.g. DBMS, DSA
    description = db.Column(db.Text, nullable=True)

    concepts = db.relationship('Concept', backref='subject', lazy=True, cascade="all, delete-orphan")
    diagnoses = db.relationship('Diagnosis', backref='subject', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'description': self.description
        }

class Concept(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id', ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    # Prerequisites DAG relationship
    prerequisites = db.relationship(
        'Concept',
        secondary=concept_prerequisites,
        primaryjoin="Concept.id==concept_prerequisites.c.concept_id",
        secondaryjoin="Concept.id==concept_prerequisites.c.prerequisite_id",
        backref=db.backref('depended_upon_by', lazy='dynamic'),
        lazy='subquery'
    )

    questions = db.relationship('Question', backref='concept', lazy=True, cascade="all, delete-orphan")
    knowledge_states = db.relationship('KnowledgeState', backref='concept', lazy=True, cascade="all, delete-orphan")
    interventions = db.relationship('Intervention', backref='concept', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'subject_id': self.subject_id,
            'name': self.name,
            'description': self.description,
            'prerequisites': [prereq.id for prereq in self.prerequisites]
        }

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    concept_id = db.Column(db.Integer, db.ForeignKey('concept.id', ondelete='CASCADE'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    options_json = db.Column(db.Text, nullable=False) # JSON encoded list of strings
    correct_answer = db.Column(db.String(256), nullable=False) # Option text or option index
    difficulty_level = db.Column(db.String(20), nullable=False) # e.g. Beginner, Intermediate, Advanced

    attempts = db.relationship('AnswerAttempt', backref='question', lazy=True, cascade="all, delete-orphan")

    @property
    def options(self):
        return json.loads(self.options_json)

    @options.setter
    def options(self, val):
        self.options_json = json.dumps(val)

    def to_dict(self):
        return {
            'id': self.id,
            'concept_id': self.concept_id,
            'question_text': self.question_text,
            'options': self.options,
            'difficulty_level': self.difficulty_level
        }

class AnswerAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), nullable=False)
    student_answer = db.Column(db.String(256), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'question_id': self.question_id,
            'student_answer': self.student_answer,
            'is_correct': self.is_correct,
            'timestamp': self.timestamp.isoformat()
        }

class KnowledgeState(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'), nullable=False)
    concept_id = db.Column(db.Integer, db.ForeignKey('concept.id', ondelete='CASCADE'), nullable=False)
    mastery_score = db.Column(db.Float, nullable=False, default=0.0) # range 0.0 to 1.0
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'concept_id': self.concept_id,
            'mastery_score': self.mastery_score,
            'last_updated': self.last_updated.isoformat()
        }

class Diagnosis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id', ondelete='CASCADE'), nullable=False)
    root_cause_concept_id = db.Column(db.Integer, db.ForeignKey('concept.id', ondelete='CASCADE'), nullable=False)
    prerequisite_weakness_ids_json = db.Column(db.Text, nullable=False) # JSON encoded list of concept IDs
    diagnostic_summary = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    interventions = db.relationship('Intervention', backref='diagnosis', lazy=True, cascade="all, delete-orphan")

    @property
    def prerequisite_weakness_ids(self):
        return json.loads(self.prerequisite_weakness_ids_json)

    @prerequisite_weakness_ids.setter
    def prerequisite_weakness_ids(self, val):
        self.prerequisite_weakness_ids_json = json.dumps(val)

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'subject_id': self.subject_id,
            'root_cause_concept_id': self.root_cause_concept_id,
            'prerequisite_weakness_ids': self.prerequisite_weakness_ids,
            'diagnostic_summary': self.diagnostic_summary,
            'timestamp': self.timestamp.isoformat()
        }

class Intervention(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    diagnosis_id = db.Column(db.Integer, db.ForeignKey('diagnosis.id', ondelete='CASCADE'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'), nullable=False)
    concept_id = db.Column(db.Integer, db.ForeignKey('concept.id', ondelete='CASCADE'), nullable=False)
    intervention_type = db.Column(db.String(50), nullable=False) # e.g. text_guide, interactive_code, video_summary
    intervention_content = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='assigned') # assigned, in_progress, completed
    post_intervention_mastery = db.Column(db.Float, nullable=True) # mastery score after reassessment
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'diagnosis_id': self.diagnosis_id,
            'student_id': self.student_id,
            'concept_id': self.concept_id,
            'intervention_type': self.intervention_type,
            'intervention_content': self.intervention_content,
            'status': self.status,
            'post_intervention_mastery': self.post_intervention_mastery,
            'timestamp': self.timestamp.isoformat()
        }

class KnowledgeStateHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'), nullable=False)
    concept_id = db.Column(db.Integer, db.ForeignKey('concept.id', ondelete='CASCADE'), nullable=False)
    previous_mastery = db.Column(db.Float, nullable=False)
    updated_mastery = db.Column(db.Float, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), nullable=True)
    quiz_question_id = db.Column(db.Integer, db.ForeignKey('quiz_question.id', ondelete='CASCADE'), nullable=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id', ondelete='CASCADE'), nullable=True)
    project_id = db.Column(db.Integer, db.ForeignKey('mini_project.id', ondelete='CASCADE'), nullable=True)
    answer_correct = db.Column(db.Boolean, nullable=False) # Legacy binary correct
    evidence_score = db.Column(db.Float, nullable=True)    # Fractional score (0.0 to 1.0)
    evidence_source = db.Column(db.String(50), nullable=True) # e.g. "coding_submission", "project_submission"
    passed_tests = db.Column(db.Integer, nullable=True)
    total_tests = db.Column(db.Integer, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'concept_id': self.concept_id,
            'previous_mastery': self.previous_mastery,
            'updated_mastery': self.updated_mastery,
            'question_id': self.question_id,
            'quiz_question_id': self.quiz_question_id,
            'exercise_id': self.exercise_id,
            'project_id': self.project_id,
            'answer_correct': self.answer_correct,
            'evidence_score': self.evidence_score,
            'evidence_source': self.evidence_source,
            'passed_tests': self.passed_tests,
            'total_tests': self.total_tests,
            'timestamp': self.timestamp.isoformat()
        }

class PasswordResetToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'), nullable=False)
    token_hash = db.Column(db.String(256), nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)
    used = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'expires_at': self.expires_at.isoformat(),
            'used': self.used,
            'created_at': self.created_at.isoformat()
        }

# ==========================================
# PHASE 3: COURSE ENGINE MODELS
# ==========================================

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.String(50), nullable=False)
    thumbnail = db.Column(db.String(255), nullable=True)
    is_published = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    modules = db.relationship('CourseModule', backref='course', lazy=True, cascade="all, delete-orphan")
    enrollments = db.relationship('CourseEnrollment', backref='course', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'description': self.description,
            'category': self.category,
            'difficulty': self.difficulty,
            'thumbnail': self.thumbnail,
            'is_published': self.is_published,
            'created_at': self.created_at.isoformat()
        }

class CourseModule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    order_index = db.Column(db.Integer, nullable=False)

    lessons = db.relationship('Lesson', backref='module', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'course_id': self.course_id,
            'title': self.title,
            'description': self.description,
            'order_index': self.order_index
        }

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('course_module.id', ondelete='CASCADE'), nullable=False)
    concept_id = db.Column(db.Integer, db.ForeignKey('concept.id', ondelete='SET NULL'), nullable=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    order_index = db.Column(db.Integer, nullable=False)
    estimated_minutes = db.Column(db.Integer, default=5)

    examples = db.relationship('LessonExample', backref='lesson', lazy=True, cascade="all, delete-orphan")
    exercises = db.relationship('Exercise', backref='lesson', lazy=True, cascade="all, delete-orphan")
    quizzes = db.relationship('QuizQuestion', backref='lesson', lazy=True, cascade="all, delete-orphan")
    mini_projects = db.relationship('MiniProject', backref='lesson', lazy=True, cascade="all, delete-orphan")
    progress_records = db.relationship('LessonProgress', backref='lesson', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'module_id': self.module_id,
            'concept_id': self.concept_id,
            'title': self.title,
            'slug': self.slug,
            'content': self.content,
            'order_index': self.order_index,
            'estimated_minutes': self.estimated_minutes
        }

class LessonExample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    explanation = db.Column(db.Text, nullable=True)
    code = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(50), nullable=False)
    order_index = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'lesson_id': self.lesson_id,
            'title': self.title,
            'explanation': self.explanation,
            'code': self.code,
            'language': self.language,
            'order_index': self.order_index
        }

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id', ondelete='CASCADE'), nullable=False)
    concept_id = db.Column(db.Integer, db.ForeignKey('concept.id', ondelete='SET NULL'), nullable=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.String(50), nullable=False)
    starter_code = db.Column(db.Text, nullable=True)
    expected_output = db.Column(db.Text, nullable=True)
    language = db.Column(db.String(50), nullable=False)
    order_index = db.Column(db.Integer, nullable=False)

    submissions = db.relationship('ExerciseSubmission', backref='exercise', lazy=True, cascade="all, delete-orphan")
    test_cases = db.relationship('TestCase', backref='exercise', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'lesson_id': self.lesson_id,
            'concept_id': self.concept_id,
            'title': self.title,
            'description': self.description,
            'difficulty': self.difficulty,
            'starter_code': self.starter_code,
            'expected_output': self.expected_output,
            'language': self.language,
            'order_index': self.order_index
        }

class QuizQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id', ondelete='CASCADE'), nullable=False)
    concept_id = db.Column(db.Integer, db.ForeignKey('concept.id', ondelete='SET NULL'), nullable=True)
    question_text = db.Column(db.Text, nullable=False)
    options_json = db.Column(db.Text, nullable=False) # JSON encoded options
    correct_answer = db.Column(db.String(255), nullable=False)
    explanation = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.String(50), nullable=False)

    @property
    def options(self):
        return json.loads(self.options_json)

    @options.setter
    def options(self, val):
        self.options_json = json.dumps(val)

    def to_dict(self):
        return {
            'id': self.id,
            'lesson_id': self.lesson_id,
            'concept_id': self.concept_id,
            'question_text': self.question_text,
            'options': self.options,
            'explanation': self.explanation,
            'difficulty': self.difficulty
        }

class CourseEnrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id', ondelete='CASCADE'), nullable=False)
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_accessed_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    completed_at = db.Column(db.DateTime, nullable=True)
    progress_percentage = db.Column(db.Float, default=0.0)

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'course_id': self.course_id,
            'started_at': self.started_at.isoformat() if self.started_at else None,
            'last_accessed_at': self.last_accessed_at.isoformat() if self.last_accessed_at else None,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None,
            'progress_percentage': self.progress_percentage
        }

class LessonProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id', ondelete='CASCADE'), nullable=False)
    status = db.Column(db.String(50), default='not_started', nullable=False) # not_started, in_progress, completed
    completion_percentage = db.Column(db.Float, default=0.0)
    completed_at = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'lesson_id': self.lesson_id,
            'status': self.status,
            'completion_percentage': self.completion_percentage,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None
        }

class ExerciseSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id', ondelete='CASCADE'), nullable=False)
    code = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False) # success, compile_error, runtime_error, timeout
    test_result = db.Column(db.Text, nullable=True) # JSON output of individual test case results
    passed_tests = db.Column(db.Integer, nullable=True, default=0)
    total_tests = db.Column(db.Integer, nullable=True, default=0)
    score = db.Column(db.Float, nullable=True, default=0.0) # Fractional score 0.0 to 1.0
    execution_time_ms = db.Column(db.Integer, nullable=True)
    error_type = db.Column(db.String(50), nullable=True)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'exercise_id': self.exercise_id,
            'code': self.code,
            'language': self.language,
            'status': self.status,
            'test_result': self.test_result,
            'passed_tests': self.passed_tests,
            'total_tests': self.total_tests,
            'score': self.score,
            'execution_time_ms': self.execution_time_ms,
            'error_type': self.error_type,
            'submitted_at': self.submitted_at.isoformat() if self.submitted_at else None
        }

class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id', ondelete='CASCADE'), nullable=False)
    input_data = db.Column(db.Text, nullable=True)
    expected_output = db.Column(db.Text, nullable=False)
    is_hidden = db.Column(db.Boolean, default=False, nullable=False)
    order_index = db.Column(db.Integer, nullable=False)

    def to_dict(self, include_hidden=False):
        data = {
            'id': self.id,
            'exercise_id': self.exercise_id,
            'is_hidden': self.is_hidden,
            'order_index': self.order_index
        }
        if not self.is_hidden or include_hidden:
            data['input_data'] = self.input_data
            data['expected_output'] = self.expected_output
        return data


# ==========================================
# MINI PROJECT MODELS
# ==========================================

class MiniProject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id', ondelete='CASCADE'), nullable=False)
    concept_id = db.Column(db.Integer, db.ForeignKey('concept.id', ondelete='SET NULL'), nullable=True)
    title = db.Column(db.String(255), nullable=False)
    objective = db.Column(db.Text, nullable=False)
    scenario = db.Column(db.Text, nullable=False)
    requirements_json = db.Column(db.Text, nullable=False) # JSON list of string requirements
    features_json = db.Column(db.Text, nullable=False) # JSON list of string features
    required_concepts = db.Column(db.Text, nullable=True) # JSON or string
    architecture = db.Column(db.Text, nullable=True)
    guidance_json = db.Column(db.Text, nullable=False) # JSON list of guidance steps
    hints_json = db.Column(db.Text, nullable=True) # JSON list of hints
    workflow = db.Column(db.Text, nullable=True)
    expected_behavior = db.Column(db.Text, nullable=False)
    evaluation_criteria = db.Column(db.Text, nullable=False)
    starter_code = db.Column(db.Text, nullable=True)
    language = db.Column(db.String(50), default="python", nullable=False)
    order_index = db.Column(db.Integer, default=1, nullable=False)

    submissions = db.relationship('ProjectSubmission', backref='project', lazy=True, cascade="all, delete-orphan")
    test_cases = db.relationship('ProjectTestCase', backref='project', lazy=True, cascade="all, delete-orphan")

    @property
    def requirements(self):
        return json.loads(self.requirements_json) if self.requirements_json else []

    @requirements.setter
    def requirements(self, val):
        self.requirements_json = json.dumps(val)

    @property
    def features(self):
        return json.loads(self.features_json) if self.features_json else []

    @features.setter
    def features(self, val):
        self.features_json = json.dumps(val)

    @property
    def guidance(self):
        return json.loads(self.guidance_json) if self.guidance_json else []

    @guidance.setter
    def guidance(self, val):
        self.guidance_json = json.dumps(val)

    @property
    def hints(self):
        return json.loads(self.hints_json) if self.hints_json else []

    @hints.setter
    def hints(self, val):
        self.hints_json = json.dumps(val)

    def _normalize_list(self, val):
        if isinstance(val, list):
            return val
        if isinstance(val, str):
            try:
                parsed = json.loads(val)
                if isinstance(parsed, list):
                    return parsed
                elif isinstance(parsed, str):
                    return [v.strip() for v in parsed.split('\n') if v.strip()]
            except:
                pass
            return [v.strip() for v in val.split('\n') if v.strip()]
        return []

    def to_dict(self):
        # Handle required_concepts separately since it might be raw json string
        rc = []
        if self.required_concepts:
            try:
                rc = json.loads(self.required_concepts)
            except:
                rc = self.required_concepts
                
        return {
            'id': self.id,
            'lesson_id': self.lesson_id,
            'concept_id': self.concept_id,
            'title': self.title,
            'objective': self.objective,
            'scenario': self.scenario,
            'requirements': self._normalize_list(self.requirements),
            'features': self._normalize_list(self.features),
            'required_concepts': self._normalize_list(rc),
            'architecture': self.architecture,
            'guidance': self._normalize_list(self.guidance),
            'hints': self._normalize_list(self.hints),
            'workflow': self.workflow,
            'expected_behavior': self.expected_behavior,
            'evaluation_criteria': self.evaluation_criteria,
            'starter_code': self.starter_code,
            'language': self.language,
            'order_index': self.order_index
        }

class ProjectTestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('mini_project.id', ondelete='CASCADE'), nullable=False)
    input_data = db.Column(db.Text, nullable=True)
    expected_output = db.Column(db.Text, nullable=False)
    is_hidden = db.Column(db.Boolean, default=False, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    order_index = db.Column(db.Integer, nullable=False)

    def to_dict(self, include_hidden=False):
        data = {
            'id': self.id,
            'project_id': self.project_id,
            'is_hidden': self.is_hidden,
            'description': self.description,
            'order_index': self.order_index
        }
        if not self.is_hidden or include_hidden:
            data['input_data'] = self.input_data
            data['expected_output'] = self.expected_output
        return data

class ProjectSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('mini_project.id', ondelete='CASCADE'), nullable=False)
    code = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False) # not_started, in_progress, submitted, passed, failed
    test_result = db.Column(db.Text, nullable=True)
    passed_tests = db.Column(db.Integer, nullable=True, default=0)
    total_tests = db.Column(db.Integer, nullable=True, default=0)
    score = db.Column(db.Float, nullable=True, default=0.0) # Fractional score 0.0 to 1.0
    execution_time_ms = db.Column(db.Integer, nullable=True)
    feedback_json = db.Column(db.Text, nullable=True)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def feedback(self):
        return json.loads(self.feedback_json) if self.feedback_json else []

    @feedback.setter
    def feedback(self, val):
        self.feedback_json = json.dumps(val)

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'project_id': self.project_id,
            'code': self.code,
            'language': self.language,
            'status': self.status,
            'test_result': self.test_result,
            'passed_tests': self.passed_tests,
            'total_tests': self.total_tests,
            'score': self.score,
            'execution_time_ms': self.execution_time_ms,
            'feedback': self.feedback,
            'submitted_at': self.submitted_at.isoformat() if self.submitted_at else None
        }


