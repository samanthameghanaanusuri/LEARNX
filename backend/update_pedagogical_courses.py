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

import content_html
import content_css
import content_js

def update_pedagogical_course(course_slug, new_data):
    course = Course.query.filter_by(slug=course_slug).first()
    if not course:
        print(f"[FATAL] Course {course_slug} not found.")
        return False
        
    print(f"\n--- Updating {course.title} (ID: {course.id}) ---")
    course.description = new_data.get('description', course.description)
    
    existing_modules = CourseModule.query.filter_by(course_id=course.id).order_by(CourseModule.order_index).all()
    
    # We will match modules by index
    for mod_idx, new_mod in enumerate(new_data['modules']):
        if mod_idx < len(existing_modules):
            db_mod = existing_modules[mod_idx]
        else:
            db_mod = CourseModule(course_id=course.id, order_index=mod_idx+1)
            db.session.add(db_mod)
            db.session.flush()
            
        db_mod.title = new_mod['title']
        db_mod.description = new_mod['description']
        
        # Lessons
        existing_lessons = Lesson.query.filter_by(module_id=db_mod.id).order_by(Lesson.order_index).all()
        for les_idx, new_les in enumerate(new_mod['lessons']):
            if les_idx < len(existing_lessons):
                db_les = existing_lessons[les_idx]
            else:
                db_les = Lesson(module_id=db_mod.id, order_index=les_idx+1)
                db.session.add(db_les)
                db.session.flush()
                
            db_les.title = new_les['title']
            db_les.slug = new_les['slug']
            db_les.content = new_les['content']
            
            # Examples
            existing_examples = LessonExample.query.filter_by(lesson_id=db_les.id).order_by(LessonExample.order_index).all()
            for ex_idx, new_ex in enumerate(new_les.get('examples', [])):
                if ex_idx < len(existing_examples):
                    db_ex = existing_examples[ex_idx]
                else:
                    db_ex = LessonExample(lesson_id=db_les.id, order_index=ex_idx+1)
                    db.session.add(db_ex)
                    
                db_ex.title = new_ex['title']
                db_ex.explanation = new_ex['explanation']
                db_ex.code = new_ex['code']
                db_ex.language = new_ex.get('language', new_data['lang'])
                
            # Exercises
            existing_exercises = Exercise.query.filter_by(lesson_id=db_les.id).order_by(Exercise.order_index).all()
            for ex_idx, new_ex in enumerate(new_les.get('exercises', [])):
                if ex_idx < len(existing_exercises):
                    db_ex = existing_exercises[ex_idx]
                else:
                    db_ex = Exercise(lesson_id=db_les.id, order_index=ex_idx+1)
                    db.session.add(db_ex)
                    db.session.flush()
                    
                db_ex.title = new_ex['title']
                db_ex.description = new_ex['description']
                db_ex.difficulty = new_ex['difficulty']
                db_ex.starter_code = new_ex['starter_code']
                db_ex.language = new_ex.get('language', new_data['lang'])
                
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
                    
            # Quizzes
            existing_quizzes = QuizQuestion.query.filter_by(lesson_id=db_les.id).order_by(QuizQuestion.id).all()
            for q_idx, new_q in enumerate(new_les.get('quizzes', [])):
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
                
            # Projects (Max 1 per lesson, usually)
            if 'project' in new_les:
                new_proj = new_les['project']
                existing_projects = MiniProject.query.filter_by(lesson_id=db_les.id).all()
                if existing_projects:
                    db_proj = existing_projects[0]
                else:
                    db_proj = MiniProject(lesson_id=db_les.id)
                    db.session.add(db_proj)
                    db.session.flush()
                    
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
                db_proj.language = new_proj.get('language', new_data['lang'])
                db_proj.order_index = 1
                
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
                    
    print(f"Update for {course.title} staged successfully.")
    return True

if __name__ == '__main__':
    app = create_app(Config)
    with app.app_context():
        try:
            html_success = update_pedagogical_course('html-web-development', content_html.get_course_data())
            css_success = update_pedagogical_course('css-responsive-design', content_css.get_course_data())
            js_success = update_pedagogical_course('javascript-programming', content_js.get_course_data())
            
            if html_success and css_success and js_success:
                db.session.commit()
                print("\n[SUCCESS] Pedagogical database update committed successfully!")
            else:
                db.session.rollback()
                print("\n[FAIL] Update aborted due to errors.")
        except Exception as e:
            db.session.rollback()
            print(f"\n[EXCEPTION] {e}")
            raise
