import os
import shutil
from app import create_app, db
from app.models import Course, CourseModule, Lesson, Exercise, QuizQuestion, TestCase
from content_cyber import (
    course_title,
    course_description,
    course_language,
    course_difficulty,
    cyber_lessons,
    cyber_exercises_list,
    cyber_quizzes_list,
    cyber_module_titles
)

def backup_db():
    db_path = 'instance/learnx.db'
    backup_path = 'instance/learnx.db.bak'
    if os.path.exists(db_path):
        print(f"Backing up database from {db_path} to {backup_path}...")
        shutil.copy2(db_path, backup_path)
    else:
        print(f"Warning: Database {db_path} not found for backup.")

def add_cybersecurity_course():
    app = create_app()
    with app.app_context():
        # DO NOT DROP ALL OR CREATE ALL
        
        # Backup first
        backup_db()
        
        try:
            print("Starting additive insertion of Cyber Security course...")
            course_slug = "cyber-security"
            
            # 1. Check if course already exists to avoid duplication
            existing = Course.query.filter_by(slug=course_slug).first()
            if existing:
                print(f"Course {course_slug} already exists. Deleting it to re-insert cleanly (only the Cyber Security course will be deleted).")
                db.session.delete(existing)
                db.session.flush()

            # 2. Add Course
            print(f"Adding course: {course_title}")
            new_course = Course(
                title=course_title,
                slug=course_slug,
                description=course_description,
                category=course_language,
                difficulty=course_difficulty,
                is_published=True
            )
            db.session.add(new_course)
            db.session.flush()

            # 3. Add Modules, Lessons, Exercises, Quizzes
            num_modules = len(cyber_module_titles)
            for i in range(num_modules):
                mod_title = cyber_module_titles[i]
                mod_order = i + 1
                lesson_content = cyber_lessons[i]
                mod_exercises = cyber_exercises_list[i]
                mod_quizzes = cyber_quizzes_list[i]
                
                print(f"  Adding Module {mod_order}: {mod_title}")
                new_module = CourseModule(
                    course_id=new_course.id,
                    title=mod_title,
                    description=f"Module {mod_order} of Cyber Security",
                    order_index=mod_order
                )
                db.session.add(new_module)
                db.session.flush()

                # Add Lesson
                new_lesson = Lesson(
                    module_id=new_module.id,
                    title=f"Lesson: {mod_title.split(': ')[-1]}",
                    slug=f"cyber-lesson-{mod_order}",
                    content=lesson_content,
                    order_index=1
                )
                db.session.add(new_lesson)
                db.session.flush()

                # Add Exercises
                for ex_order, ex_data in enumerate(mod_exercises, 1):
                    new_exercise = Exercise(
                        lesson_id=new_lesson.id,
                        title=ex_data['title'],
                        description=ex_data['description'],
                        difficulty=ex_data['difficulty'],
                        starter_code=ex_data.get('starter_code', ''),
                        expected_output=ex_data.get('solution_code', ''),
                        language="text",
                        order_index=ex_order
                    )
                    db.session.add(new_exercise)
                    db.session.flush()

                    for tc_idx, tc in enumerate(ex_data.get('test_cases', []), 1):
                        new_tc = TestCase(
                            exercise_id=new_exercise.id,
                            input_data=tc.get('input', ''),
                            expected_output=tc.get('expected_output', ''),
                            is_hidden=tc.get('is_hidden', False),
                            order_index=tc_idx
                        )
                        db.session.add(new_tc)

                # Add Quizzes
                for q_data in mod_quizzes:
                    new_quiz = QuizQuestion(
                        lesson_id=new_lesson.id,
                        question_text=q_data['question_text'],
                        options=q_data['options'],
                        correct_answer=q_data['correct_answer'],
                        explanation=q_data['explanation'],
                        difficulty=q_data['difficulty']
                    )
                    db.session.add(new_quiz)

            db.session.commit()
            print("SUCCESS: Cyber Security course added without modifying existing data!")

        except Exception as e:
            db.session.rollback()
            print(f"ERROR: Transaction failed. Rolled back all changes. Exception: {str(e)}")

if __name__ == '__main__':
    add_cybersecurity_course()
