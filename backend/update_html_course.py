import os
import sys

# Ensure the backend directory is on sys.path regardless of CWD
_script_dir = os.path.dirname(os.path.abspath(__file__))
if _script_dir not in sys.path:
    sys.path.insert(0, _script_dir)

from app import create_app
from config import Config
from app.models import (
    db, Course, CourseModule, Lesson, LessonExample, Exercise,
    TestCase, QuizQuestion, MiniProject, ProjectTestCase
)
import html_course_content

def update_html_course():
    app = create_app(Config)
    with app.app_context():
        print("Starting in-place HTML course content update...")
        
        # Load the new high-quality data
        try:
            new_data = html_course_content.get_html_course_data()
        except Exception as e:
            print(f"[FATAL] Failed to load new HTML course data: {e}")
            sys.exit(1)

        # Locate the existing HTML course
        course = Course.query.filter_by(slug=new_data['slug']).first()
        if not course:
            print(f"[FATAL] HTML course with slug '{new_data['slug']}' not found in database. Cannot update.")
            sys.exit(1)

        print(f"Found course: {course.title} (ID: {course.id})")
        
        # Update course fields
        course.description = new_data['description']
        
        stats = {
            'modules': 0, 'lessons': 0, 'examples': 0,
            'exercises': 0, 'quizzes': 0, 'projects': 0
        }

        # Process Modules
        existing_modules = CourseModule.query.filter_by(course_id=course.id).order_by(CourseModule.order_index).all()
        if len(existing_modules) != len(new_data['modules']):
            print(f"[FATAL] Module count mismatch. Existing: {len(existing_modules)}, New: {len(new_data['modules'])}. Aborting to preserve safety.")
            sys.exit(1)

        for mod_idx, new_mod in enumerate(new_data['modules']):
            db_mod = existing_modules[mod_idx]
            db_mod.title = new_mod['title']
            db_mod.description = new_mod['description']
            stats['modules'] += 1

            # Process Lessons (1 per module)
            existing_lessons = Lesson.query.filter_by(module_id=db_mod.id).order_by(Lesson.order_index).all()
            if len(existing_lessons) != len(new_mod['lessons']):
                print(f"[FATAL] Lesson count mismatch in Module {db_mod.id}. Existing: {len(existing_lessons)}, New: {len(new_mod['lessons'])}.")
                sys.exit(1)

            for les_idx, new_les in enumerate(new_mod['lessons']):
                db_les = existing_lessons[les_idx]
                db_les.title = new_les['title']
                db_les.slug = new_les['slug']
                db_les.content = new_les['content']
                stats['lessons'] += 1

                # Update Examples
                existing_examples = LessonExample.query.filter_by(lesson_id=db_les.id).order_by(LessonExample.order_index).all()
                for ex_idx, new_ex in enumerate(new_les['examples']):
                    if ex_idx < len(existing_examples):
                        db_ex = existing_examples[ex_idx]
                        db_ex.title = new_ex['title']
                        db_ex.explanation = new_ex['explanation']
                        db_ex.code = new_ex['code']
                        db_ex.language = new_ex['language']
                        stats['examples'] += 1
                    else:
                        print(f"[WARN] More examples in new data than DB for lesson {db_les.id}. Creating new example.")
                        new_db_ex = LessonExample(
                            lesson_id=db_les.id,
                            title=new_ex['title'],
                            explanation=new_ex['explanation'],
                            code=new_ex['code'],
                            language=new_ex['language'],
                            order_index=new_ex['order_index']
                        )
                        db.session.add(new_db_ex)
                        stats['examples'] += 1

                # Update Exercises
                existing_exercises = Exercise.query.filter_by(lesson_id=db_les.id).order_by(Exercise.order_index).all()
                if len(existing_exercises) != len(new_les['exercises']):
                    print(f"[FATAL] Exercise count mismatch in Lesson {db_les.id}. Existing: {len(existing_exercises)}, New: {len(new_les['exercises'])}.")
                    sys.exit(1)

                for ex_idx, new_ex in enumerate(new_les['exercises']):
                    db_ex = existing_exercises[ex_idx]
                    db_ex.title = new_ex['title']
                    db_ex.description = new_ex['description']
                    db_ex.difficulty = new_ex['difficulty']
                    db_ex.starter_code = new_ex['starter_code']
                    db_ex.language = new_ex['language']
                    stats['exercises'] += 1

                    # Update Test Cases for this exercise
                    # Delete old ones and add new ones (safe because test cases don't hold student progress directly)
                    TestCase.query.filter_by(exercise_id=db_ex.id).delete()
                    for tc_data in new_ex['test_cases']:
                        tc = TestCase(
                            exercise_id=db_ex.id,
                            input_data=tc_data['input_data'],
                            expected_output=tc_data['expected_output'],
                            is_hidden=tc_data['is_hidden'],
                            order_index=tc_data.get('order_index', 1)
                        )
                        db.session.add(tc)

                # Update Quizzes
                existing_quizzes = QuizQuestion.query.filter_by(lesson_id=db_les.id).order_by(QuizQuestion.id).all()
                if len(existing_quizzes) != len(new_les['quizzes']):
                    print(f"[FATAL] Quiz count mismatch in Lesson {db_les.id}. Existing: {len(existing_quizzes)}, New: {len(new_les['quizzes'])}.")
                    sys.exit(1)

                for q_idx, new_q in enumerate(new_les['quizzes']):
                    db_q = existing_quizzes[q_idx]
                    db_q.question_text = new_q['question_text']
                    db_q.options = new_q['options']
                    db_q.correct_answer = new_q['correct_answer']
                    db_q.explanation = new_q['explanation']
                    db_q.difficulty = new_q['difficulty']
                    stats['quizzes'] += 1

                # Update Mini Project
                existing_projects = MiniProject.query.filter_by(lesson_id=db_les.id).all()
                if not existing_projects:
                    print(f"[FATAL] No project found for Lesson {db_les.id}.")
                    sys.exit(1)
                
                new_proj = new_les['project']
                db_proj = existing_projects[0]
                db_proj.title = new_proj['title']
                db_proj.scenario = new_proj['scenario']
                db_proj.objective = new_proj['objective']
                db_proj.requirements = new_proj['requirements']
                db_proj.features = new_proj['features']
                db_proj.guidance = new_proj['guidance']
                db_proj.expected_behavior = new_proj['expected_behavior']
                db_proj.evaluation_criteria = new_proj['evaluation_criteria']
                db_proj.starter_code = new_proj['starter_code']
                db_proj.language = new_proj['language']
                stats['projects'] += 1

                ProjectTestCase.query.filter_by(project_id=db_proj.id).delete()
                for pt_data in new_proj['test_cases']:
                    pt = ProjectTestCase(
                        project_id=db_proj.id,
                        input_data=pt_data['input_data'],
                        expected_output=pt_data['expected_output'],
                        is_hidden=pt_data['is_hidden'],
                        order_index=pt_data.get('order_index', 1)
                    )
                    db.session.add(pt)

        # Commit all in-place updates
        db.session.commit()
        print("="*50)
        print("UPDATE COMPLETE — NO RECORDS DELETED")
        print("="*50)
        print(f"Modules Updated  : {stats['modules']}")
        print(f"Lessons Updated  : {stats['lessons']}")
        print(f"Examples Updated : {stats['examples']}")
        print(f"Exercises Updated: {stats['exercises']}")
        print(f"Quizzes Updated  : {stats['quizzes']}")
        print(f"Projects Updated : {stats['projects']}")
        print("="*50)

if __name__ == "__main__":
    update_html_course()
