import sys
import traceback
import os

# Ensure backend directory is in path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from seed_courses import seed_courses
from seed_web_courses import seed_web_courses
from app import create_app
from app.models import db, Course, CourseModule, Lesson

def main():
    print("Starting LEARNX production database seed process...")
    try:
        app = create_app()
        with app.app_context():
            print("Database connected")
            db.create_all()
            
            print("\n--- Seeding Programming Courses ---")
            seed_courses()
            print("Standard courses seeded")
            
            print("\n--- Seeding Web Development Courses ---")
            seed_web_courses()
            print("Web courses seeded")
            
            # Print final counts
            courses = Course.query.count()
            modules = CourseModule.query.count()
            lessons = Lesson.query.count()
            print("\nDatabase Summary:")
            print(f"Total courses: {courses}")
            print(f"Total modules: {modules}")
            print(f"Total lessons: {lessons}")
            
    except Exception as e:
        print("\n[ERROR] A database error occurred during seeding!", file=sys.stderr)
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
