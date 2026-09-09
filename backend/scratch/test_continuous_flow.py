import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.models import db, Course, CourseModule, Lesson

def test_flow():
    app = create_app()
    with app.app_context():
        course = Course.query.filter_by(slug='python-programming').first()
        if not course:
            print("[FAIL] Course python-programming not found!")
            sys.exit(1)
            
        modules = CourseModule.query.filter_by(course_id=course.id).order_by(CourseModule.order_index).all()
        print(f"[INFO] Course has {len(modules)} modules.")
        
        # Test Module 1 last lesson
        m1 = modules[0]
        m1_lessons = Lesson.query.filter_by(module_id=m1.id).order_by(Lesson.order_index).all()
        last_l1 = m1_lessons[-1]
        print(f"[INFO] Module 1 last lesson: {last_l1.title} (ID: {last_l1.id})")
        
        # Manually compute next lesson using our new courses.py logic
        current_module = last_l1.module
        next_lesson_id = None
        next_module_title = None
        course_completed = False
        
        next_lesson = Lesson.query.filter_by(module_id=current_module.id).filter(Lesson.order_index > last_l1.order_index).order_by(Lesson.order_index.asc()).first()
        
        if next_lesson:
            next_lesson_id = next_lesson.id
            next_module_title = current_module.title
        else:
            next_module = CourseModule.query.filter_by(course_id=current_module.course_id).filter(CourseModule.order_index > current_module.order_index).order_by(CourseModule.order_index.asc()).first()
            if next_module:
                first_lesson = Lesson.query.filter_by(module_id=next_module.id).order_by(Lesson.order_index.asc()).first()
                if first_lesson:
                    next_lesson_id = first_lesson.id
                    next_module_title = next_module.title
                else:
                    course_completed = True
            else:
                course_completed = True
                
        print(f"[INFO] Next module title: {next_module_title}")
        print(f"[INFO] Next lesson ID: {next_lesson_id}")
        print(f"[INFO] Course completed: {course_completed}")
        
        # Assertions
        assert next_lesson_id is not None, "Next lesson ID should not be None for Module 1 last lesson!"
        assert next_module_title == "Python Basics & Syntax", "Next module should be Python Basics & Syntax"
        assert not course_completed, "Course should not be completed after Module 1"
        
        # Test Module 15 (last module) last lesson
        m15 = modules[-1]
        m15_lessons = Lesson.query.filter_by(module_id=m15.id).order_by(Lesson.order_index).all()
        last_l15 = m15_lessons[-1]
        print(f"[INFO] Module 15 last lesson: {last_l15.title} (ID: {last_l15.id})")
        
        current_module = last_l15.module
        next_lesson_id = None
        next_module_title = None
        course_completed = False
        
        next_lesson = Lesson.query.filter_by(module_id=current_module.id).filter(Lesson.order_index > last_l15.order_index).order_by(Lesson.order_index.asc()).first()
        
        if next_lesson:
            next_lesson_id = next_lesson.id
            next_module_title = current_module.title
        else:
            next_module = CourseModule.query.filter_by(course_id=current_module.course_id).filter(CourseModule.order_index > current_module.order_index).order_by(CourseModule.order_index.asc()).first()
            if next_module:
                first_lesson = Lesson.query.filter_by(module_id=next_module.id).order_by(Lesson.order_index.asc()).first()
                if first_lesson:
                    next_lesson_id = first_lesson.id
                    next_module_title = next_module.title
                else:
                    course_completed = True
            else:
                course_completed = True
                
        print(f"[INFO] After Module 15 - Next lesson ID: {next_lesson_id}")
        print(f"[INFO] After Module 15 - Course completed: {course_completed}")
        
        assert next_lesson_id is None, "After Module 15 last lesson, there should be no next lesson"
        assert course_completed, "After Module 15 last lesson, the course should be completed"
        
        print("[SUCCESS] All continuous flow logic assertions passed!")

if __name__ == '__main__':
    test_flow()
