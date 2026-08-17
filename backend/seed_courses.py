import os
import json
from app import create_app
from app.models import (
    db, Course, CourseModule, Lesson, LessonExample, 
    Exercise, QuizQuestion, Concept, Subject, TestCase,
    MiniProject, ProjectTestCase
)
from course_data_1 import COURSE_MODULES_1_TO_15
from course_data_2 import COURSE_MODULES_16_TO_30
from java_course_data_1 import COURSE_MODULES_1_TO_15 as JAVA_MODULES_1_TO_15
from java_course_data_2 import COURSE_MODULES_16_TO_30 as JAVA_MODULES_16_TO_30

app = create_app()

def seed_course_data(course_slug, course_title, course_description, subject_code, subject_name, subject_desc, modules_data, lang_key):
    # 1. Find or create Course
    course = Course.query.filter_by(slug=course_slug).first()
    if not course:
        print(f"Creating Course: {course_title}...")
        course = Course(
            title=course_title,
            slug=course_slug,
            description=course_description,
            category="Programming",
            difficulty="Beginner to Advanced",
            is_published=True
        )
        db.session.add(course)
        db.session.commit()
    else:
        print(f"Course {course_title} already exists. Updating attributes...")
        course.title = course_title
        course.description = course_description
        db.session.commit()

    # 2. Find or create Subject
    subject = Subject.query.filter_by(code=subject_code).first()
    if not subject:
        print(f"Creating Subject: {subject_name} ({subject_code})...")
        subject = Subject(
            name=subject_name,
            code=subject_code,
            description=subject_desc
        )
        db.session.add(subject)
        db.session.commit()

    prev_concept = None
    for i, module_data in enumerate(modules_data):
        # 3. Find or create CourseModule
        module = CourseModule.query.filter_by(course_id=course.id, order_index=i + 1).first()
        if not module:
            module = CourseModule(
                course_id=course.id,
                title=module_data['title'],
                description=f"Learn everything about {module_data['title']} in {subject_name}.",
                order_index=i + 1
            )
            db.session.add(module)
            db.session.commit()
        else:
            module.title = module_data['title']
            module.description = f"Learn everything about {module_data['title']} in {subject_name}."
            db.session.commit()

        # 4. Find or create Concept
        concept = Concept.query.filter_by(name=module_data['concept'], subject_id=subject.id).first()
        if not concept:
            concept = Concept(
                subject_id=subject.id,
                name=module_data['concept'],
                description=f"Understanding {module_data['title']}"
            )
            db.session.add(concept)
            db.session.commit()
        
        # Link prerequisite chain
        if prev_concept:
            if prev_concept not in concept.prerequisites:
                concept.prerequisites.append(prev_concept)
                db.session.commit()
        prev_concept = concept

        # 5. Find or create Lesson
        lesson_title = f"Mastering {module_data['title']}"
        lesson_slug = f"{module_data['title'].lower().replace(' ', '-').replace('&', 'and').replace(',', '').replace('(', '').replace(')', '')}-lesson-{lang_key}"
        
        lesson = Lesson.query.filter_by(module_id=module.id, order_index=1).first()
        lesson_content = (
            f"<h3>{lesson_title}</h3><p>{module_data['theory']}</p>"
            f"<h4>Common Mistakes</h4><ul>" + 
            "".join([f"<li>{m}</li>" for m in module_data['mistakes']]) + "</ul>"
        )
        
        if not lesson:
            lesson = Lesson(
                module_id=module.id,
                concept_id=concept.id,
                title=lesson_title,
                slug=lesson_slug,
                content=lesson_content,
                order_index=1,
                estimated_minutes=20
            )
            db.session.add(lesson)
            db.session.commit()
        else:
            lesson.title = lesson_title
            lesson.concept_id = concept.id
            lesson.slug = lesson_slug
            lesson.content = lesson_content
            db.session.commit()

        # 6. Idempotently seed LessonExamples (clear and recreate)
        LessonExample.query.filter_by(lesson_id=lesson.id).delete()
        examples_list = module_data.get('examples', [module_data[k] for k in ['ex1', 'ex2'] if k in module_data])
        for idx, ex in enumerate(examples_list):
            example = LessonExample(
                lesson_id=lesson.id,
                title=ex['title'],
                explanation=ex['explanation'],
                code=ex['code'],
                language=lang_key,
                order_index=idx + 1
            )
            db.session.add(example)

        # 7. Idempotently seed Exercises & Test Cases
        exercises_list = module_data.get('exercises', [module_data['exercise']] if 'exercise' in module_data else [])
        for ex_idx, ex_data in enumerate(exercises_list):
            exercise = Exercise.query.filter_by(lesson_id=lesson.id, title=ex_data['title']).first()
            ex_lang = ex_data.get('language', lang_key)
            if not exercise:
                exercise = Exercise(
                    lesson_id=lesson.id,
                    concept_id=concept.id,
                    title=ex_data['title'],
                    description=ex_data['desc'],
                    difficulty=ex_data.get('difficulty', 'Medium'),
                    starter_code=ex_data['starter'],
                    expected_output=ex_data['expected'],
                    language=ex_lang,
                    order_index=ex_idx + 1
                )
                db.session.add(exercise)
                db.session.flush()
            else:
                exercise.concept_id = concept.id
                exercise.description = ex_data['desc']
                exercise.difficulty = ex_data.get('difficulty', 'Medium')
                exercise.starter_code = ex_data['starter']
                exercise.expected_output = ex_data['expected']
                exercise.language = ex_lang
                db.session.commit()

            # Recreate test cases
            TestCase.query.filter_by(exercise_id=exercise.id).delete()
            tc_list = ex_data.get('test_cases', [
                {'input': '', 'expected': ex_data['expected'], 'is_hidden': False},
                {'input': '', 'expected': ex_data['expected'], 'is_hidden': True}
            ])
            for tc_idx, tc_item in enumerate(tc_list):
                tc = TestCase(
                    exercise_id=exercise.id,
                    input_data=tc_item.get('input', ''),
                    expected_output=tc_item['expected'],
                    is_hidden=tc_item.get('is_hidden', False),
                    order_index=tc_idx + 1
                )
                db.session.add(tc)

        # 8. Idempotently seed Quizzes (clear and recreate)
        QuizQuestion.query.filter_by(lesson_id=lesson.id).delete()
        quizzes_data = module_data.get('quizzes', [module_data.get('quiz')] if module_data.get('quiz') else [])
        for q_data in quizzes_data:
            quiz = QuizQuestion(
                lesson_id=lesson.id,
                concept_id=concept.id,
                question_text=q_data['question'],
                options=q_data['options'],
                correct_answer=q_data['correct'],
                explanation=q_data['explanation'],
                difficulty=q_data['difficulty']
            )
            db.session.add(quiz)

        # 9. Idempotently seed Mini Projects & Project Test Cases
        projects_data = module_data.get('projects', [module_data['project']] if 'project' in module_data else [])
        for p_idx, p_data in enumerate(projects_data):
            project = MiniProject.query.filter_by(lesson_id=lesson.id, title=p_data['title']).first()
            if not project:
                project = MiniProject(
                    lesson_id=lesson.id,
                    concept_id=concept.id,
                    title=p_data['title'],
                    objective=p_data['objective'],
                    scenario=p_data['scenario'],
                    requirements_json=json.dumps(p_data.get('requirements', [])),
                    features_json=json.dumps(p_data.get('features', [])),
                    required_concepts=p_data.get('required_concepts', ''),
                    architecture=p_data.get('architecture', ''),
                    guidance_json=json.dumps(p_data.get('guidance', [])),
                    hints_json=json.dumps(p_data.get('hints', [])),
                    workflow=p_data.get('workflow', ''),
                    expected_behavior=p_data['expected_behavior'],
                    evaluation_criteria=p_data['evaluation_criteria'],
                    starter_code=p_data.get('starter', ''),
                    language=lang_key,
                    order_index=p_idx + 1
                )
                db.session.add(project)
                db.session.flush()
            else:
                project.concept_id = concept.id
                project.objective = p_data['objective']
                project.scenario = p_data['scenario']
                project.requirements_json = json.dumps(p_data.get('requirements', []))
                project.features_json = json.dumps(p_data.get('features', []))
                project.required_concepts = p_data.get('required_concepts', '')
                project.architecture = p_data.get('architecture', '')
                project.guidance_json = json.dumps(p_data.get('guidance', []))
                project.hints_json = json.dumps(p_data.get('hints', []))
                project.workflow = p_data.get('workflow', '')
                project.expected_behavior = p_data['expected_behavior']
                project.evaluation_criteria = p_data['evaluation_criteria']
                project.starter_code = p_data.get('starter', '')
                project.language = lang_key
                db.session.commit()

            # Recreate project test cases
            ProjectTestCase.query.filter_by(project_id=project.id).delete()
            ptc_list = p_data.get('test_cases', [])
            for ptc_idx, ptc_item in enumerate(ptc_list):
                ptc = ProjectTestCase(
                    project_id=project.id,
                    input_data=ptc_item.get('input', ''),
                    expected_output=ptc_item['expected'],
                    description=ptc_item.get('description', f'Test {ptc_idx+1}'),
                    is_hidden=ptc_item.get('is_hidden', False),
                    order_index=ptc_idx + 1
                )
                db.session.add(ptc)

        print(f"Seeded module {i+1}/{len(modules_data)} for {course_title}: {module_data['title']}")
    
    db.session.commit()

def seed_courses():
    with app.app_context():
        # Ensure database tables exist
        db.create_all()

        # 1. Seed Python Course
        python_modules = COURSE_MODULES_1_TO_15 + COURSE_MODULES_16_TO_30
        seed_course_data(
            course_slug="python-programming",
            course_title="Python Programming — Beginner to Advanced",
            course_description="Master Python from the basics to advanced concepts like OOP, Decorators, and Algorithms. Includes quizzes, exercises, and knowledge tracing.",
            subject_code="PYTHON",
            subject_name="Python Language",
            subject_desc="Python programming concepts",
            modules_data=python_modules,
            lang_key="python"
        )

        # 2. Seed Java Course
        java_modules = JAVA_MODULES_1_TO_15 + JAVA_MODULES_16_TO_30
        seed_course_data(
            course_slug="java-programming",
            course_title="Java Programming — Beginner to Advanced",
            course_description="Master Java from syntax primitives to object-oriented inheritance, generics, multithreading, and SQL database connectivity.",
            subject_code="JAVA",
            subject_name="Java Language",
            subject_desc="Java programming concepts",
            modules_data=java_modules,
            lang_key="java"
        )

        print("All courses seeded successfully!")

if __name__ == '__main__':
    seed_courses()
