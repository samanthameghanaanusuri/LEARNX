import os
import sys
import shutil

_script_dir = os.path.dirname(os.path.abspath(__file__))
if _script_dir not in sys.path:
    sys.path.insert(0, _script_dir)

from app import create_app
from config import Config
from app.models import (
    db, Course, CourseModule, Lesson, LessonExample, Exercise,
    TestCase, QuizQuestion, MiniProject, ProjectTestCase, Subject, Concept, Question
)

import content_c

def backup_database():
    db_path = os.path.join(_script_dir, 'instance', 'learnx.db')
    bak_path = os.path.join(_script_dir, 'instance', 'learnx.db.bak')
    if os.path.exists(db_path):
        shutil.copyfile(db_path, bak_path)
        print(f"[SAFETY BACKUP] Created backup of database at: {bak_path}")

def get_baseline_counts():
    counts = {}
    courses = ['python-programming', 'java-programming', 'html-web-development', 'css-responsive-design', 'javascript-programming']
    for slug in courses:
        c = Course.query.filter_by(slug=slug).first()
        if c:
            mod_count = CourseModule.query.filter_by(course_id=c.id).count()
            les_count = db.session.query(Lesson).join(CourseModule).filter(CourseModule.course_id == c.id).count()
            ex_count = db.session.query(Exercise).join(Lesson).join(CourseModule).filter(CourseModule.course_id == c.id).count()
            counts[slug] = (mod_count, les_count, ex_count)
        else:
            counts[slug] = None
            
    subjects = ['DBMS', 'DSA']
    for code in subjects:
        s = Subject.query.filter_by(code=code).first()
        if s:
            concept_count = Concept.query.filter_by(subject_id=s.id).count()
            q_count = db.session.query(Question).join(Concept).filter(Concept.subject_id == s.id).count()
            counts[code] = (concept_count, q_count)
        else:
            counts[code] = None
            
    return counts

def print_counts(label, counts):
    print(f"\n--- {label} ---")
    for key, val in counts.items():
        print(f"  {key}: {val}")

def add_c_course(course_data):
    course_slug = course_data['slug']
    course = Course.query.filter_by(slug=course_slug).first()
    
    if not course:
        print(f"Creating new course: {course_data['title']}")
        course = Course(
            title=course_data['title'],
            description=course_data['description'],
            slug=course_slug,
            category=course_data.get('category', 'Programming Languages'),
            difficulty=course_data.get('difficulty', 'Beginner to Advanced'),
            is_published=True
        )
        db.session.add(course)
        db.session.flush()
    else:
        print(f"Course {course_slug} already exists. Updating existing record...")
        course.title = course_data['title']
        course.description = course_data.get('description', course.description)
        course.category = course_data.get('category', course.category)
        course.difficulty = course_data.get('difficulty', course.difficulty)
        course.is_published = True

    print(f"\n--- Processing {course.title} (ID: {course.id}) ---")
    
    existing_modules = CourseModule.query.filter_by(course_id=course.id).order_by(CourseModule.order_index).all()
    
    # Prune surplus modules if any exist beyond 15
    if len(existing_modules) > len(course_data['modules']):
        for extra_mod in existing_modules[len(course_data['modules']):]:
            print(f"Pruning surplus module: {extra_mod.title}")
            db.session.delete(extra_mod)
        db.session.flush()
        existing_modules = existing_modules[:len(course_data['modules'])]

    for mod_idx, new_mod_data in enumerate(course_data['modules']):
        if mod_idx < len(existing_modules):
            db_mod = existing_modules[mod_idx]
        else:
            db_mod = CourseModule(course_id=course.id, order_index=mod_idx+1)
            db.session.add(db_mod)
            
        db_mod.title = new_mod_data['title']
        db_mod.description = f"Module {mod_idx+1}: {new_mod_data['title']}"
        db_mod.order_index = mod_idx + 1
        db.session.flush()
        
        # Lessons for this module
        # Note: Each module in course_data has 1 lesson (or multiple if provided)
        lessons_data = [new_mod_data] if 'content' in new_mod_data else new_mod_data.get('lessons', [])
        existing_lessons = Lesson.query.filter_by(module_id=db_mod.id).order_by(Lesson.order_index).all()
        
        if len(existing_lessons) > len(lessons_data):
            for extra_les in existing_lessons[len(lessons_data):]:
                db.session.delete(extra_les)
            db.session.flush()
            existing_lessons = existing_lessons[:len(lessons_data)]
            
        for les_idx, new_les in enumerate(lessons_data):
            if les_idx < len(existing_lessons):
                db_les = existing_lessons[les_idx]
            else:
                db_les = Lesson(module_id=db_mod.id, order_index=les_idx+1)
                db.session.add(db_les)
                
            db_les.title = new_les['title']
            db_les.slug = new_les['slug']
            db_les.content = new_les['content']
            db_les.order_index = les_idx + 1
            db.session.flush()
            
            # Synchronize Exercises
            new_exs = new_les.get('exercises', [])
            existing_exercises = Exercise.query.filter_by(lesson_id=db_les.id).order_by(Exercise.order_index).all()
            
            if len(existing_exercises) > len(new_exs):
                for extra_ex in existing_exercises[len(new_exs):]:
                    db.session.delete(extra_ex)
                db.session.flush()
                existing_exercises = existing_exercises[:len(new_exs)]
                
            for ex_idx, new_ex in enumerate(new_exs):
                if ex_idx < len(existing_exercises):
                    db_ex = existing_exercises[ex_idx]
                else:
                    db_ex = Exercise(lesson_id=db_les.id, order_index=ex_idx+1)
                    db.session.add(db_ex)
                    
                db_ex.title = new_ex['title']
                db_ex.description = new_ex['description']
                db_ex.difficulty = new_ex['difficulty']
                db_ex.starter_code = new_ex['starter_code']
                db_ex.language = new_ex.get('language', course_data.get('lang', 'c'))
                db_ex.order_index = ex_idx + 1
                db.session.flush()
                
                TestCase.query.filter_by(exercise_id=db_ex.id).delete()
                for tc_idx, tc_data in enumerate(new_ex.get('test_cases', [])):
                    tc = TestCase(
                        exercise_id=db_ex.id,
                        input_data=tc_data.get('input_data', ''),
                        expected_output=tc_data['expected_output'],
                        is_hidden=tc_data.get('is_hidden', False),
                        order_index=tc_data.get('order_index', tc_idx+1)
                    )
                    db.session.add(tc)
                    
            # Synchronize Quizzes
            new_quizzes = new_les.get('quizzes', [])
            existing_quizzes = QuizQuestion.query.filter_by(lesson_id=db_les.id).order_by(QuizQuestion.id).all()
            
            if len(existing_quizzes) > len(new_quizzes):
                for extra_q in existing_quizzes[len(new_quizzes):]:
                    db.session.delete(extra_q)
                db.session.flush()
                existing_quizzes = existing_quizzes[:len(new_quizzes)]
                
            for q_idx, new_q in enumerate(new_quizzes):
                if q_idx < len(existing_quizzes):
                    db_q = existing_quizzes[q_idx]
                else:
                    db_q = QuizQuestion(lesson_id=db_les.id)
                    db.session.add(db_q)
                    
                db_q.question_text = new_q['question_text']
                db_q.options = new_q['options']
                db_q.correct_answer = new_q['correct_answer']
                db_q.explanation = new_q['explanation']
                db_q.difficulty = new_q.get('difficulty', 'Beginner')
                db.session.flush()
                
            # Synchronize Stage Projects
            if 'project' in new_les and new_les['project']:
                new_proj = new_les['project']
                existing_projects = MiniProject.query.filter_by(lesson_id=db_les.id).all()
                if existing_projects:
                    db_proj = existing_projects[0]
                else:
                    db_proj = MiniProject(lesson_id=db_les.id)
                    db.session.add(db_proj)
                    
                db_proj.title = new_proj['title']
                db_proj.scenario = new_proj['scenario']
                db_proj.objective = new_proj['objective']
                db_proj.requirements = new_proj['requirements']
                db_proj.features = new_proj['features']
                db_proj.guidance = new_proj.get('guidance', [])
                db_proj.hints = new_proj.get('hints', [])
                db_proj.expected_behavior = new_proj['expected_behavior']
                db_proj.evaluation_criteria = new_proj['evaluation_criteria']
                db_proj.starter_code = new_proj['starter_code']
                db_proj.language = new_proj.get('language', course_data.get('lang', 'c'))
                db_proj.order_index = 1
                db.session.flush()
                
                ProjectTestCase.query.filter_by(project_id=db_proj.id).delete()
                for pt_idx, pt_data in enumerate(new_proj.get('test_cases', [])):
                    pt = ProjectTestCase(
                        project_id=db_proj.id,
                        input_data=pt_data.get('input_data', ''),
                        expected_output=pt_data['expected_output'],
                        is_hidden=pt_data.get('is_hidden', False),
                        order_index=pt_data.get('order_index', pt_idx+1)
                    )
                    db.session.add(pt)
                    
    print(f"Data staging complete for {course.title}.")
    return True

if __name__ == '__main__':
    app = create_app(Config)
    with app.app_context():
        # Step 1: Backup database
        backup_database()
        
        # Step 2: Record baseline counts
        baseline = get_baseline_counts()
        print_counts("BASELINE DATABASE COUNTS (BEFORE C UPDATE)", baseline)
        
        try:
            # Step 3: Upsert C course inside transaction
            c_data = content_c.get_course_data()
            success = add_c_course(c_data)
            
            if success:
                db.session.commit()
                print("\n[SUCCESS] C Programming course committed successfully!")
            else:
                db.session.rollback()
                print("\n[FAIL] Update aborted.")
                sys.exit(1)
        except Exception as e:
            db.session.rollback()
            print(f"\n[EXCEPTION] Transaction rolled back due to error: {e}")
            raise
            
        # Step 4: Verify non-C counts are completely unchanged
        post_counts = get_baseline_counts()
        print_counts("POST-UPDATE DATABASE COUNTS", post_counts)
        
        mismatches = []
        for key in baseline:
            if baseline[key] != post_counts[key]:
                mismatches.append((key, baseline[key], post_counts[key]))
                
        if mismatches:
            print(f"\n[ERROR] Non-C database count mismatches detected: {mismatches}")
            sys.exit(1)
        else:
            print("\n[VERIFIED] All non-C subject and course database counts remain 100% unchanged!")
