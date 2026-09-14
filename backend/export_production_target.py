import os
import sys
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import (
    Course, CourseModule, Lesson, LessonExample, Exercise, TestCase,
    QuizQuestion, MiniProject, ProjectTestCase, Subject, Concept, concept_prerequisites
)

def export_target():
    app = create_app()
    with app.app_context():
        
        target_slugs = [
            'java-programming', 'html-web-development', 'css-responsive-design',
            'javascript-programming', 'c-programming', 'cpp-programming',
            'cyber-security', 'dbms-mastery', 'dsa-mastery'
        ]
        
        # 1. Verification
        print("Validating course counts...")
        expected = {
            'java-programming': 30, 'html-web-development': 20, 'css-responsive-design': 20,
            'javascript-programming': 20, 'c-programming': 15, 'cpp-programming': 15,
            'cyber-security': 20, 'dbms-mastery': 15, 'dsa-mastery': 18
        }
        
        actual_courses = Course.query.filter(Course.slug.in_(target_slugs)).all()
        if len(actual_courses) != 9:
            print(f"FATAL: Expected 9 courses, found {len(actual_courses)}")
            sys.exit(1)
            
        total_modules = 0
        total_lessons = 0
        
        for c in actual_courses:
            mc = CourseModule.query.filter_by(course_id=c.id).count()
            lc = Lesson.query.join(CourseModule).filter(CourseModule.course_id == c.id).count()
            if mc != expected[c.slug]:
                print(f"FATAL: {c.slug} expected {expected[c.slug]} modules, found {mc}")
                sys.exit(1)
            total_modules += mc
            total_lessons += lc
            
        if total_modules != 173 or total_lessons != 173:
            print(f"FATAL: Expected 173 modules/lessons, got {total_modules} / {total_lessons}")
            sys.exit(1)
            
        print("Validation passed. Exporting data...")
        
        export_data = {
            "metadata": {
                "version": "1.0",
                "description": "Exact 173-module production restore payload"
            },
            "subjects": [],
            "concepts": [],
            "concept_prereqs": [],
            "courses": []
        }
        
        # Collect all subjects and concepts
        for subj in Subject.query.order_by(Subject.id).all():
            export_data["subjects"].append({
                "id": subj.id,
                "name": subj.name,
                "code": subj.code,
                "description": subj.description
            })
            
        for conc in Concept.query.order_by(Concept.id).all():
            export_data["concepts"].append({
                "id": conc.id,
                "subject_id": conc.subject_id,
                "name": conc.name,
                "description": conc.description
            })
            
        prereqs = db.session.query(concept_prerequisites).all()
        for p in prereqs:
            export_data["concept_prereqs"].append({
                "concept_id": p.concept_id,
                "prerequisite_id": p.prerequisite_id
            })
            
        # Collect courses
        for course in actual_courses:
            c_dict = course.to_dict()
            c_dict['modules'] = []
            
            modules = CourseModule.query.filter_by(course_id=course.id).order_by(CourseModule.order_index, CourseModule.id).all()
            for mod in modules:
                m_dict = mod.to_dict()
                m_dict['lessons'] = []
                
                lessons = Lesson.query.filter_by(module_id=mod.id).order_by(Lesson.order_index, Lesson.id).all()
                for les in lessons:
                    l_dict = les.to_dict()
                    l_dict['examples'] = [e.to_dict() for e in LessonExample.query.filter_by(lesson_id=les.id).order_by(LessonExample.order_index, LessonExample.id).all()]
                    
                    exercises = Exercise.query.filter_by(lesson_id=les.id).order_by(Exercise.order_index, Exercise.id).all()
                    ex_list = []
                    for ex in exercises:
                        ex_d = ex.to_dict()
                        ex_d['test_cases'] = [tc.to_dict(include_hidden=True) for tc in TestCase.query.filter_by(exercise_id=ex.id).order_by(TestCase.order_index, TestCase.id).all()]
                        ex_list.append(ex_d)
                    l_dict['exercises'] = ex_list
                    
                    l_dict['quizzes'] = [q.to_dict() for q in QuizQuestion.query.filter_by(lesson_id=les.id).order_by(QuizQuestion.id).all()]
                    
                    projects = MiniProject.query.filter_by(lesson_id=les.id).order_by(MiniProject.id).all()
                    proj_list = []
                    for proj in projects:
                        p_d = proj.to_dict()
                        p_d['test_cases'] = [pt.to_dict(include_hidden=True) for pt in ProjectTestCase.query.filter_by(project_id=proj.id).order_by(ProjectTestCase.order_index, ProjectTestCase.id).all()]
                        proj_list.append(p_d)
                    l_dict['projects'] = proj_list
                    
                    m_dict['lessons'].append(l_dict)
                c_dict['modules'].append(m_dict)
            export_data['courses'].append(c_dict)
            
        output_path = os.path.join(os.path.dirname(__file__), 'production_target.json')
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, ensure_ascii=False)
            
        print(f"Export complete: {output_path}")

if __name__ == '__main__':
    export_target()
