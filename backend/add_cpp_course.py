import os
import shutil
from app import create_app, db
from app.models import Course, CourseModule, Lesson, Exercise, QuizQuestion, MiniProject, TestCase, ProjectTestCase
from content_cpp import course_cpp, cpp_modules, cpp_projects

def backup_db():
    db_path = 'instance/learnx.db'
    backup_path = 'instance/learnx.db.bak'
    if os.path.exists(db_path):
        print(f"Backing up database from {db_path} to {backup_path}...")
        shutil.copy2(db_path, backup_path)
    else:
        print(f"Warning: Database {db_path} not found for backup.")

def add_cpp_course():
    app = create_app()
    with app.app_context():
        # DO NOT DROP ALL OR CREATE ALL
        
        # Backup first
        backup_db()
        
        try:
            print("Starting additive insertion of C++ course...")
            
            # 1. Check if course already exists to avoid duplication
            existing = Course.query.filter_by(slug=course_cpp["course_id"]).first()
            if existing:
                print(f"Course {course_cpp['course_id']} already exists. Deleting it to re-insert cleanly (only the C++ course will be deleted).")
                db.session.delete(existing)
                db.session.flush()

            # 2. Add Course
            print(f"Adding course: {course_cpp['title']}")
            new_course = Course(
                title=course_cpp['title'],
                slug=course_cpp['course_id'],
                description=course_cpp['description'],
                category=course_cpp['language'],
                difficulty=course_cpp['difficulty'],
                is_published=True
            )
            db.session.add(new_course)
            db.session.flush()

            # 3. Add Modules, Lessons, Exercises, Quizzes
            for mod_data in cpp_modules:
                print(f"  Adding Module: {mod_data['title']}")
                new_module = CourseModule(
                    course_id=new_course.id,
                    title=mod_data['title'],
                    description=mod_data['description'],
                    order_index=mod_data['order']
                )
                db.session.add(new_module)
                db.session.flush()

                # Add Lesson
                new_lesson = Lesson(
                    module_id=new_module.id,
                    title=f"Lesson: {mod_data['title']}",
                    slug=f"cpp-lesson-{mod_data['order']}",
                    content=mod_data['lesson_content'],
                    order_index=1
                )
                db.session.add(new_lesson)
                db.session.flush()

                # Add Exercises
                for ex_order, ex_data in enumerate(mod_data['exercises'], 1):
                    new_exercise = Exercise(
                        lesson_id=new_lesson.id,
                        title=ex_data['title'],
                        description=ex_data['description'],
                        difficulty=ex_data['difficulty'],
                        starter_code=ex_data['starter_code'],
                        expected_output=ex_data['solution_code'],
                        language="cpp",
                        order_index=ex_order
                    )
                    db.session.add(new_exercise)
                    db.session.flush()

                    for tc_idx, tc in enumerate(ex_data['test_cases'], 1):
                        new_tc = TestCase(
                            exercise_id=new_exercise.id,
                            input_data=tc['input'],
                            expected_output=tc['expected_output'],
                            is_hidden=tc.get('is_hidden', False),
                            order_index=tc_idx
                        )
                        db.session.add(new_tc)

                # Add Quizzes
                for q_data in mod_data['quizzes']:
                    new_quiz = QuizQuestion(
                        lesson_id=new_lesson.id,
                        question_text=q_data['question_text'],
                        options=q_data['options'],
                        correct_answer=q_data['correct_answer'],
                        explanation=q_data['explanation'],
                        difficulty=q_data['difficulty']
                    )
                    db.session.add(new_quiz)

            # 4. Add Projects
            for p_order, p_data in enumerate(cpp_projects, 1):
                print(f"  Adding Project: {p_data['title']}")
                
                # Find the lesson for this project based on module_index
                module_order = p_data['module_index']
                target_module = CourseModule.query.filter_by(course_id=new_course.id, order_index=module_order).first()
                if not target_module:
                    raise Exception(f"Module {module_order} not found for project {p_data['title']}")
                target_lesson = Lesson.query.filter_by(module_id=target_module.id).first()
                
                new_project = MiniProject(
                    lesson_id=target_lesson.id,
                    title=p_data['title'],
                    objective=p_data['description'],
                    scenario=p_data['description'],
                    requirements=["Complete the logic"],
                    features=[],
                    guidance=["Use standard practices"],
                    expected_behavior="Code executes successfully",
                    evaluation_criteria="Passes all tests",
                    starter_code=p_data['starter_code'],
                    language="cpp",
                    order_index=p_order
                )
                db.session.add(new_project)
                db.session.flush()
                
                for tc_idx, tc in enumerate(p_data['test_cases'], 1):
                    new_tc = ProjectTestCase(
                        project_id=new_project.id,
                        input_data=tc['input'],
                        expected_output=tc['expected_output'],
                        is_hidden=tc.get('is_hidden', False),
                        order_index=tc_idx
                    )
                    db.session.add(new_tc)

            db.session.commit()
            print("SUCCESS: C++ course added without modifying existing data!")

        except Exception as e:
            db.session.rollback()
            print(f"ERROR: Transaction failed. Rolled back all changes. Exception: {str(e)}")

if __name__ == '__main__':
    add_cpp_course()
