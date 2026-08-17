from app import create_app, db
from app.models import Course, CourseModule, Lesson, QuizQuestion, Exercise

def verify():
    app = create_app()
    with app.app_context():
        # Verify old courses are untouched (we know the slugs)
        old_slugs = [
            'python-programming',
            'java-programming',
            'html-web-development',
            'css-responsive-design',
            'javascript-programming',
            'c-programming',
            'cpp-programming',
            'cyber-security'
        ]
        
        for slug in old_slugs:
            course = Course.query.filter_by(slug=slug).first()
            if not course:
                print(f"[FAIL] Missing pre-existing course: {slug}")
                return False

        print("[OK] All existing 8 courses are intact.")

        # Verify DBMS
        dbms = Course.query.filter_by(slug='dbms-mastery').first()
        if not dbms:
            print("[FAIL] DBMS course missing.")
            return False
        
        dbms_mods = CourseModule.query.filter_by(course_id=dbms.id).count()
        if dbms_mods != 15:
            print(f"[FAIL] DBMS has {dbms_mods} modules instead of 15.")
            return False
        
        dbms_lessons = Lesson.query.join(CourseModule).filter(CourseModule.course_id == dbms.id).count()
        dbms_quizzes = QuizQuestion.query.join(Lesson).join(CourseModule).filter(CourseModule.course_id == dbms.id).count()
        dbms_exs = Exercise.query.join(Lesson).join(CourseModule).filter(CourseModule.course_id == dbms.id).count()
        
        if dbms_quizzes != 150:
            print(f"[FAIL] DBMS has {dbms_quizzes} quizzes instead of 150.")
            return False
            
        print(f"[OK] DBMS verified: {dbms_mods} modules, {dbms_lessons} lessons, {dbms_exs} exercises, {dbms_quizzes} quizzes.")

        # Verify DSA
        dsa = Course.query.filter_by(slug='dsa-mastery').first()
        if not dsa:
            print("[FAIL] DSA course missing.")
            return False
        
        dsa_mods = CourseModule.query.filter_by(course_id=dsa.id).count()
        if dsa_mods != 18:
            print(f"[FAIL] DSA has {dsa_mods} modules instead of 18.")
            return False
        
        dsa_lessons = Lesson.query.join(CourseModule).filter(CourseModule.course_id == dsa.id).count()
        dsa_quizzes = QuizQuestion.query.join(Lesson).join(CourseModule).filter(CourseModule.course_id == dsa.id).count()
        dsa_exs = Exercise.query.join(Lesson).join(CourseModule).filter(CourseModule.course_id == dsa.id).count()
        
        if dsa_quizzes != 180:
            print(f"[FAIL] DSA has {dsa_quizzes} quizzes instead of 180.")
            return False
            
        print(f"[OK] DSA verified: {dsa_mods} modules, {dsa_lessons} lessons, {dsa_exs} exercises, {dsa_quizzes} quizzes.")
        return True

if __name__ == '__main__':
    verify()
