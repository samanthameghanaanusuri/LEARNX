import os
import sys
import json
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import (
    Course, CourseModule, Lesson, LessonExample, Exercise, TestCase,
    QuizQuestion, MiniProject, ProjectTestCase, Subject, Concept, concept_prerequisites
)

def get_db_driver(engine):
    return engine.url.drivername

def sync_production_courses():
    # 3. Refuse unless RUN_COURSE_RESTORE is set
    restore_mode = os.environ.get('RUN_COURSE_RESTORE')
    if restore_mode not in ['true', 'dry-run']:
        print("FATAL: RUN_COURSE_RESTORE must be 'true' or 'dry-run'.")
        sys.exit(1)
        
    is_dry_run = (restore_mode == 'dry-run')
    
    # 4. Refuse unless DATABASE_URL exists
    if not os.environ.get('DATABASE_URL'):
        print("FATAL: DATABASE_URL environment variable is missing.")
        sys.exit(1)
        
    # 5. Create Flask app context (NEVER nested)
    app = create_app()
    with app.app_context():
        # 7. Print SQLAlchemy DB driver
        driver = get_db_driver(db.engine)
        print(f"Database Driver: {driver}")
        
        # 8 & 9. Confirm PostgreSQL, refuse SQLite (unless ALLOW_SQLITE_TEST=1)
        allow_sqlite = os.environ.get('ALLOW_SQLITE_TEST') == '1'
        if 'sqlite' in driver:
            if not allow_sqlite:
                print("FATAL: SQLite driver detected. Production restore requires PostgreSQL.")
                sys.exit(1)
            else:
                print("WARNING: SQLite detected, but ALLOW_SQLITE_TEST=1 is set. Proceeding for testing.")
        else:
            if 'postgres' not in driver.lower():
                print(f"FATAL: Expected PostgreSQL, but got {driver}.")
                sys.exit(1)
            print("Confirmed PostgreSQL connection.")
            
        # 10. Refuse if production_target.json is missing
        json_path = os.path.join(os.path.dirname(__file__), 'production_target.json')
        if not os.path.exists(json_path):
            print(f"FATAL: {json_path} not found.")
            sys.exit(1)
            
        # 1. Load JSON
        print("Loading payload...")
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # 11. Validate JSON payload
        courses = data.get('courses', [])
        if len(courses) != 9:
            print(f"FATAL: Payload contains {len(courses)} courses instead of 9.")
            sys.exit(1)
            
        slugs = [c['slug'] for c in courses]
        if 'python-programming' in slugs:
            print("FATAL: python-programming found in payload.")
            sys.exit(1)
            
        if len(set(slugs)) != len(slugs):
            print("FATAL: Duplicate course slugs in payload.")
            sys.exit(1)
            
        total_modules = sum(len(c.get('modules', [])) for c in courses)
        total_lessons = sum(len(m.get('lessons', [])) for c in courses for m in c.get('modules', []))
        if total_modules != 173:
            print(f"FATAL: Expected 173 modules, found {total_modules}")
            sys.exit(1)
        if total_lessons != 173:
            print(f"FATAL: Expected 173 lessons, found {total_lessons}")
            sys.exit(1)
            
        print("JSON validation passed.")
        
        if is_dry_run:
            print("\n*** DRY RUN MODE *** (No changes will be saved)")
            
        # 12. Begin Transaction (already handled by db.session, we just won't commit on error)
        try:
            # 3. Safely remove Python
            python_course = Course.query.filter_by(slug='python-programming').first()
            if python_course:
                print(f"Found Python course (ID: {python_course.id}). Deleting...")
                if not is_dry_run:
                    db.session.delete(python_course)
                    db.session.flush()
            else:
                print("Python course not found in database. Skipping deletion.")

            # Helper function to extract dict without related lists
            def get_kwargs(item, exclude=None):
                exclude = exclude or []
                return {k: v for k, v in item.items() if isinstance(v, (str, int, float, bool, type(None))) and k not in exclude}

            # Import Subjects and Concepts
            print("Restoring Subjects and Concepts...")
            for s_data in data.get('subjects', []):
                subj = Subject.query.get(s_data['id'])
                if not subj:
                    subj = Subject(**get_kwargs(s_data))
                    if not is_dry_run:
                        db.session.add(subj)
                else:
                    for k, v in get_kwargs(s_data).items():
                        setattr(subj, k, v)
                        
            if not is_dry_run:
                db.session.flush()

            for c_data in data.get('concepts', []):
                conc = Concept.query.get(c_data['id'])
                if not conc:
                    conc = Concept(**get_kwargs(c_data, exclude=['prerequisites']))
                    if not is_dry_run:
                        db.session.add(conc)
                else:
                    for k, v in get_kwargs(c_data, exclude=['prerequisites']).items():
                        setattr(conc, k, v)
                        
            if not is_dry_run:
                db.session.flush()
                
            # Concept prereqs
            if not is_dry_run:
                db.session.execute(concept_prerequisites.delete()) # clear existing to safely insert
                for cp in data.get('concept_prereqs', []):
                    db.session.execute(concept_prerequisites.insert().values(concept_id=cp['concept_id'], prerequisite_id=cp['prerequisite_id']))
                db.session.flush()

            # 4 & 5. Restore Courses
            print("Restoring Courses...")
            for c_data in courses:
                print(f"  Processing {c_data['slug']}...")
                course = Course.query.get(c_data['id'])
                if not course:
                    course = Course(**get_kwargs(c_data, exclude=['created_at']))
                    if not is_dry_run:
                        db.session.add(course)
                else:
                    for k, v in get_kwargs(c_data, exclude=['created_at']).items():
                        setattr(course, k, v)
                        
                if not is_dry_run:
                    db.session.flush()
                    
                # Modules
                for m_data in c_data['modules']:
                    mod = CourseModule.query.get(m_data['id'])
                    if not mod:
                        mod = CourseModule(**get_kwargs(m_data))
                        if not is_dry_run:
                            db.session.add(mod)
                    else:
                        for k, v in get_kwargs(m_data).items():
                            setattr(mod, k, v)
                            
                    if not is_dry_run:
                        db.session.flush()
                        
                    # Lessons
                    for l_data in m_data['lessons']:
                        les = Lesson.query.get(l_data['id'])
                        if not les:
                            les = Lesson(**get_kwargs(l_data))
                            if not is_dry_run:
                                db.session.add(les)
                        else:
                            for k, v in get_kwargs(l_data).items():
                                setattr(les, k, v)
                                
                        if not is_dry_run:
                            db.session.flush()
                            
                        # Examples
                        for ex_data in l_data['examples']:
                            example = LessonExample.query.get(ex_data['id'])
                            if not example:
                                example = LessonExample(**get_kwargs(ex_data))
                                if not is_dry_run:
                                    db.session.add(example)
                            else:
                                for k, v in get_kwargs(ex_data).items():
                                    setattr(example, k, v)
                                    
                        # Exercises
                        for exr_data in l_data['exercises']:
                            exercise = Exercise.query.get(exr_data['id'])
                            if not exercise:
                                exercise = Exercise(**get_kwargs(exr_data))
                                if not is_dry_run:
                                    db.session.add(exercise)
                            else:
                                for k, v in get_kwargs(exr_data).items():
                                    setattr(exercise, k, v)
                                    
                            if not is_dry_run:
                                db.session.flush()
                                
                            for tc_data in exr_data['test_cases']:
                                tc = TestCase.query.get(tc_data['id'])
                                if not tc:
                                    tc = TestCase(**get_kwargs(tc_data))
                                    if not is_dry_run:
                                        db.session.add(tc)
                                else:
                                    for k, v in get_kwargs(tc_data).items():
                                        setattr(tc, k, v)
                                        
                        # Quizzes
                        for q_data in l_data['quizzes']:
                            quiz = QuizQuestion.query.get(q_data['id'])
                            if not quiz:
                                quiz = QuizQuestion(**get_kwargs(q_data, exclude=['options', 'correct_answer']))
                                quiz.options = q_data['options'] # Set JSON setter
                                quiz.correct_answer = q_data['correct_answer']
                                if not is_dry_run:
                                    db.session.add(quiz)
                            else:
                                for k, v in get_kwargs(q_data, exclude=['options', 'correct_answer']).items():
                                    setattr(quiz, k, v)
                                quiz.options = q_data['options']
                                quiz.correct_answer = q_data['correct_answer']
                                
                        # MiniProjects
                        for mp_data in l_data['projects']:
                            proj = MiniProject.query.get(mp_data['id'])
                            mp_kwargs = get_kwargs(mp_data, exclude=['requirements', 'features', 'guidance', 'hints', 'required_concepts'])
                            if not proj:
                                proj = MiniProject(**mp_kwargs)
                                proj.requirements = mp_data.get('requirements', [])
                                proj.features = mp_data.get('features', [])
                                proj.guidance = mp_data.get('guidance', [])
                                proj.hints = mp_data.get('hints', [])
                                if isinstance(mp_data.get('required_concepts'), list):
                                    proj.required_concepts = json.dumps(mp_data['required_concepts'])
                                else:
                                    proj.required_concepts = mp_data.get('required_concepts')
                                if not is_dry_run:
                                    db.session.add(proj)
                            else:
                                for k, v in mp_kwargs.items():
                                    setattr(proj, k, v)
                                proj.requirements = mp_data.get('requirements', [])
                                proj.features = mp_data.get('features', [])
                                proj.guidance = mp_data.get('guidance', [])
                                proj.hints = mp_data.get('hints', [])
                                if isinstance(mp_data.get('required_concepts'), list):
                                    proj.required_concepts = json.dumps(mp_data['required_concepts'])
                                else:
                                    proj.required_concepts = mp_data.get('required_concepts')
                                    
                            if not is_dry_run:
                                db.session.flush()
                                
                            for ptc_data in mp_data['test_cases']:
                                ptc = ProjectTestCase.query.get(ptc_data['id'])
                                if not ptc:
                                    ptc = ProjectTestCase(**get_kwargs(ptc_data))
                                    if not is_dry_run:
                                        db.session.add(ptc)
                                else:
                                    for k, v in get_kwargs(ptc_data).items():
                                        setattr(ptc, k, v)
                                        
            if not is_dry_run:
                # Need to update sequences in PostgreSQL so new inserts don't fail later
                if 'postgres' in driver.lower():
                    print("Updating PostgreSQL sequences...")
                    tables = [
                        ('subject', 'id'), ('concept', 'id'), ('course', 'id'), 
                        ('course_module', 'id'), ('lesson', 'id'), ('lesson_example', 'id'),
                        ('exercise', 'id'), ('test_case', 'id'), ('quiz_question', 'id'),
                        ('mini_project', 'id'), ('project_test_case', 'id')
                    ]
                    for table, pk in tables:
                        seq = f"{table}_{pk}_seq"
                        # Reset sequence to max id + 1
                        query = text(f"SELECT setval('{seq}', (SELECT COALESCE(MAX({pk}), 1) FROM {table}));")
                        db.session.execute(query)

            if is_dry_run:
                print("Dry-run complete. Rolling back transaction.")
                db.session.rollback()
            else:
                db.session.commit()
                print("Transaction committed successfully.")
                
        except Exception as e:
            print(f"FATAL ERROR during transaction: {e}")
            db.session.rollback()
            print("Transaction completely rolled back.")
            sys.exit(1)

if __name__ == "__main__":
    sync_production_courses()
