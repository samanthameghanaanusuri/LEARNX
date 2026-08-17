import os
import sys

_script_dir = os.path.dirname(os.path.abspath(__file__))
if _script_dir not in sys.path:
    sys.path.insert(0, _script_dir)

from app import create_app
from config import Config
from app.models import (
    db, Course, CourseModule, Lesson, LessonExample, Exercise,
    TestCase, QuizQuestion, MiniProject, ProjectTestCase
)

import css_course_content
import js_course_content

def update_course_in_place(course_slug, new_data):
    course = Course.query.filter_by(slug=course_slug).first()
    if not course:
        print(f"[FATAL] Course with slug '{course_slug}' not found.")
        return False
        
    print(f"\nUpdating {course.title} (ID: {course.id})")
    
    stats = {
        'modules': 0, 'lessons': 0, 'examples': 0,
        'exercises': 0, 'quizzes': 0, 'projects': 0
    }
    
    course.description = new_data['description']
    
    existing_modules = CourseModule.query.filter_by(course_id=course.id).order_by(CourseModule.order_index).all()
    if len(existing_modules) != len(new_data['modules']):
        print(f"[FATAL] Module count mismatch for {course.title}. Expected {len(existing_modules)}, got {len(new_data['modules'])}.")
        return False
        
    for mod_idx, new_mod in enumerate(new_data['modules']):
        db_mod = existing_modules[mod_idx]
        db_mod.title = new_mod['title']
        db_mod.description = new_mod['description']
        stats['modules'] += 1
        
        existing_lessons = Lesson.query.filter_by(module_id=db_mod.id).order_by(Lesson.order_index).all()
        if len(existing_lessons) != len(new_mod['lessons']):
            print(f"[FATAL] Lesson count mismatch in module {db_mod.id}")
            return False
            
        for les_idx, new_les in enumerate(new_mod['lessons']):
            db_les = existing_lessons[les_idx]
            db_les.title = new_les['title']
            db_les.slug = new_les['slug']
            db_les.content = new_les['content']
            stats['lessons'] += 1
            
            # Examples
            existing_examples = LessonExample.query.filter_by(lesson_id=db_les.id).order_by(LessonExample.order_index).all()
            for ex_idx, new_ex in enumerate(new_les['examples']):
                if ex_idx < len(existing_examples):
                    db_ex = existing_examples[ex_idx]
                    db_ex.title = new_ex['title']
                    db_ex.explanation = new_ex['explanation']
                    db_ex.code = new_ex['code']
                    db_ex.language = new_ex['language']
                else:
                    db_ex = LessonExample(
                        lesson_id=db_les.id,
                        title=new_ex['title'],
                        explanation=new_ex['explanation'],
                        code=new_ex['code'],
                        language=new_ex['language'],
                        order_index=new_ex['order_index']
                    )
                    db.session.add(db_ex)
                stats['examples'] += 1
                
            # Exercises
            existing_exercises = Exercise.query.filter_by(lesson_id=db_les.id).order_by(Exercise.order_index).all()
            for ex_idx, new_ex in enumerate(new_les['exercises']):
                if ex_idx < len(existing_exercises):
                    db_ex = existing_exercises[ex_idx]
                    db_ex.title = new_ex['title']
                    db_ex.description = new_ex['description']
                    db_ex.difficulty = new_ex['difficulty']
                    db_ex.starter_code = new_ex['starter_code']
                    db_ex.language = new_ex['language']
                else:
                    db_ex = Exercise(lesson_id=db_les.id, order_index=ex_idx+1, language=new_ex['language'], title=new_ex['title'], description=new_ex['description'], difficulty=new_ex['difficulty'], starter_code=new_ex['starter_code'])
                    db.session.add(db_ex)
                stats['exercises'] += 1
                
                TestCase.query.filter_by(exercise_id=db_ex.id).delete()
                for tc_data in new_ex['test_cases']:
                    tc = TestCase(
                        exercise_id=db_ex.id,
                        input_data=tc_data.get('input_data', ''),
                        expected_output=tc_data['expected_output'],
                        is_hidden=tc_data.get('is_hidden', False),
                        order_index=tc_data.get('order_index', 1)
                    )
                    db.session.add(tc)
                    
            # Quizzes
            existing_quizzes = QuizQuestion.query.filter_by(lesson_id=db_les.id).order_by(QuizQuestion.id).all()
            for q_idx, new_q in enumerate(new_les['quizzes']):
                if q_idx < len(existing_quizzes):
                    db_q = existing_quizzes[q_idx]
                    db_q.question_text = new_q['question_text']
                    db_q.options = new_q['options']
                    db_q.correct_answer = new_q['correct_answer']
                    db_q.explanation = new_q['explanation']
                    db_q.difficulty = new_q['difficulty']
                stats['quizzes'] += 1
                
            # Project
            existing_projects = MiniProject.query.filter_by(lesson_id=db_les.id).all()
            if existing_projects:
                db_proj = existing_projects[0]
                new_proj = new_les['project']
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
                db_proj.language = new_proj['language']
                stats['projects'] += 1
                
                ProjectTestCase.query.filter_by(project_id=db_proj.id).delete()
                for pt_data in new_proj['test_cases']:
                    pt = ProjectTestCase(
                        project_id=db_proj.id,
                        input_data=pt_data.get('input_data', ''),
                        expected_output=pt_data['expected_output'],
                        is_hidden=pt_data.get('is_hidden', False),
                        order_index=pt_data.get('order_index', 1)
                    )
                    db.session.add(pt)
    print(f"Updated {stats}")
    return True

def get_counts():
    counts = {}
    for slug in ['css-responsive-design', 'javascript-programming']:
        course = Course.query.filter_by(slug=slug).first()
        if not course: continue
        mods = CourseModule.query.filter_by(course_id=course.id).count()
        less = Lesson.query.join(CourseModule).filter(CourseModule.course_id == course.id).count()
        ex = Exercise.query.join(Lesson).join(CourseModule).filter(CourseModule.course_id == course.id).count()
        q = QuizQuestion.query.join(Lesson).join(CourseModule).filter(CourseModule.course_id == course.id).count()
        p = MiniProject.query.join(Lesson).join(CourseModule).filter(CourseModule.course_id == course.id).count()
        counts[slug] = {'modules': mods, 'lessons': less, 'exercises': ex, 'quizzes': q, 'projects': p}
    return counts

if __name__ == '__main__':
    app = create_app(Config)
    with app.app_context():
        print("BEFORE UPDATE COUNTS:")
        before = get_counts()
        for k, v in before.items():
            print(f"{k}: {v}")
            
        css_success = update_course_in_place('css-responsive-design', css_course_content.get_course_data())
        js_success = update_course_in_place('javascript-programming', js_course_content.get_course_data())
        
        if css_success and js_success:
            db.session.commit()
            print("Successfully updated DB in-place.")
        else:
            db.session.rollback()
            print("Failed to update.")
            
        print("\\nAFTER UPDATE COUNTS:")
        after = get_counts()
        for k, v in after.items():
            print(f"{k}: {v}")
