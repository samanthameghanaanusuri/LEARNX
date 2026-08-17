import json
import os
from app import create_app
from config import Config
from app.models import (
    db, Course, CourseModule, Lesson, LessonExample, Exercise,
    TestCase, QuizQuestion, MiniProject, ProjectTestCase, Subject, Concept
)

def seed_web_courses():
    app = create_app(Config)
    with app.app_context():
        # Load generated data
        data_path = os.path.join(os.path.dirname(__file__), 'web_courses_data.json')
        with open(data_path, 'r', encoding='utf-8') as f:
            courses = json.load(f)

        for course_data in courses:
            subject_name = course_data['subject']
            subject_code = subject_name.upper()
            
            subject = Subject.query.filter_by(code=subject_code).first()
            if not subject:
                subject = Subject(name=subject_name, code=subject_code, description=f'{subject_name} subject')
                db.session.add(subject)
                db.session.flush()

            course = Course.query.filter_by(slug=course_data['slug']).first()
            if not course:
                course = Course(
                    title=course_data['title'],
                    slug=course_data['slug'],
                    description=course_data['description'],
                    category="Web Development",
                    difficulty=course_data['difficulty'],
                    is_published=True
                )
                db.session.add(course)
                db.session.flush()

            for mod_data in course_data['modules']:
                module = CourseModule.query.filter_by(course_id=course.id, title=mod_data['title']).first()
                if not module:
                    module = CourseModule(
                        course_id=course.id,
                        title=mod_data['title'],
                        description=mod_data['description'],
                        order_index=mod_data['order_index']
                    )
                    db.session.add(module)
                    db.session.flush()

                for les_data in mod_data['lessons']:
                    # Ensure concept exists
                    concept = Concept.query.filter_by(subject_id=subject.id, name=les_data['title']).first()
                    if not concept:
                        concept = Concept(subject_id=subject.id, name=les_data['title'], description=f"Concept for {les_data['title']}")
                        db.session.add(concept)
                        db.session.flush()
                        
                    lesson = Lesson.query.filter_by(module_id=module.id, title=les_data['title']).first()
                    if not lesson:
                        lesson = Lesson(
                            module_id=module.id,
                            concept_id=concept.id,
                            title=les_data['title'],
                            slug=les_data['slug'],
                            content=les_data['content'],
                            order_index=les_data['order_index']
                        )
                        db.session.add(lesson)
                        db.session.flush()

                    # Examples
                    for ex_idx, ex_data in enumerate(les_data['examples']):
                        example = LessonExample.query.filter_by(lesson_id=lesson.id, title=ex_data['title']).first()
                        if not example:
                            example = LessonExample(
                                lesson_id=lesson.id,
                                title=ex_data['title'],
                                explanation=ex_data['explanation'],
                                code=ex_data['code'],
                                language=ex_data['language'],
                                order_index=ex_idx + 1
                            )
                            db.session.add(example)
                    
                    # Exercises
                    for ex_data in les_data['exercises']:
                        exercise = Exercise.query.filter_by(lesson_id=lesson.id, title=ex_data['title']).first()
                        if not exercise:
                            exercise = Exercise(
                                lesson_id=lesson.id,
                                concept_id=concept.id,
                                title=ex_data['title'],
                                description=ex_data['description'],
                                difficulty=ex_data['difficulty'],
                                starter_code=ex_data['starter_code'],
                                expected_output='true',
                                language=ex_data['language'],
                                order_index=ex_data['order_index']
                            )
                            db.session.add(exercise)
                            db.session.flush()

                            for tc_data in ex_data['test_cases']:
                                tc = TestCase(
                                    exercise_id=exercise.id,
                                    input_data=tc_data['input_data'],
                                    expected_output=tc_data['expected_output'],
                                    is_hidden=tc_data['is_hidden'],
                                    order_index=tc_data.get('order_index', 1)
                                )
                                db.session.add(tc)

                    # Quizzes
                    for q_data in les_data['quizzes']:
                        quiz = QuizQuestion.query.filter_by(lesson_id=lesson.id, question_text=q_data['question_text']).first()
                        if not quiz:
                            quiz = QuizQuestion(
                                lesson_id=lesson.id,
                                concept_id=concept.id,
                                question_text=q_data['question_text'],
                                options=q_data['options'],
                                correct_answer=q_data['correct_answer'],
                                explanation=q_data['explanation'],
                                difficulty=q_data['difficulty']
                            )
                            db.session.add(quiz)

                    # Mini Project
                    proj_data = les_data['project']
                    project = MiniProject.query.filter_by(lesson_id=lesson.id, title=proj_data['title']).first()
                    if not project:
                        project = MiniProject(
                            lesson_id=lesson.id,
                            concept_id=concept.id,
                            title=proj_data['title'],
                            scenario=proj_data['scenario'],
                            objective=proj_data['objective'],
                            requirements=proj_data['requirements'],
                            features=proj_data['features'],
                            guidance=proj_data['guidance'],
                            expected_behavior=proj_data['expected_behavior'],
                            evaluation_criteria=proj_data['evaluation_criteria'],
                            starter_code=proj_data['starter_code'],
                            language=proj_data['language']
                        )
                        db.session.add(project)
                        db.session.flush()

                        for pt_idx, pt_data in enumerate(proj_data['test_cases']):
                            pt = ProjectTestCase(
                                project_id=project.id,
                                input_data=pt_data['input_data'],
                                expected_output=pt_data['expected_output'],
                                is_hidden=pt_data['is_hidden'],
                                order_index=pt_idx + 1
                            )
                            db.session.add(pt)

        db.session.commit()
        print("Web courses seeded successfully.")

if __name__ == "__main__":
    seed_web_courses()
