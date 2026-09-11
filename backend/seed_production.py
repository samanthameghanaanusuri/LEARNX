import os
import sys
import logging

from app import db
from app.models import Course

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def seed_production():
    logger.info("LEARNX production database initialization started.")
    
    # 1. Python
    if Course.query.filter_by(slug="python-programming").first():
        logger.info("Course already exists, skipping: python-programming")
    else:
        logger.info("Course missing, creating: python-programming")
        from seed_courses import seed_python_course_rebuild
        from python_course_rebuild import PYTHON_REBUILD_MODULES
        try:
            seed_python_course_rebuild(
                course_slug="python-programming",
                course_title="Python Programming — Beginner to Advanced",
                course_description="Master Python from the basics to advanced concepts like OOP, Decorators, and Algorithms. Includes quizzes, exercises, and knowledge tracing.",
                subject_code="PYTHON",
                subject_name="Python Language",
                subject_desc="Python programming concepts",
                modules_data=PYTHON_REBUILD_MODULES
            )
        except Exception as e:
            db.session.rollback()
            logger.error(f"Production database seeding failed: {e}")

    # 2. Java
    if Course.query.filter_by(slug="java-programming").first():
        logger.info("Course already exists, skipping: java-programming")
    else:
        logger.info("Course missing, creating: java-programming")
        from seed_courses import seed_course_data
        from java_course_data_1 import COURSE_MODULES_1_TO_15 as JAVA_MODULES_1_TO_15
        from java_course_data_2 import COURSE_MODULES_16_TO_30 as JAVA_MODULES_16_TO_30
        try:
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
        except Exception as e:
            db.session.rollback()
            logger.error(f"Production database seeding failed: {e}")

    # 3. Web courses (HTML, CSS, JS)
    web_slugs = ["html-web-development", "css-responsive-design", "javascript-programming"]
    missing_web = [slug for slug in web_slugs if not Course.query.filter_by(slug=slug).first()]
    for slug in web_slugs:
        if slug not in missing_web:
            logger.info(f"Course already exists, skipping: {slug}")
        else:
            logger.info(f"Course missing, creating: {slug}")
            
    if missing_web:
        try:
            from seed_web_courses import seed_web_courses
            seed_web_courses()
        except Exception as e:
            logger.error(f"Production database seeding failed for web courses: {e}")

    # 4. C
    if Course.query.filter_by(slug="c-programming").first():
        logger.info("Course already exists, skipping: c-programming")
    else:
        logger.info("Course missing, creating: c-programming")
        from add_c_course import add_c_course
        import content_c
        try:
            add_c_course(content_c.get_course_data())
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(f"Production database seeding failed: {e}")

    # 5. C++
    if Course.query.filter_by(slug="cpp-programming").first():
        logger.info("Course already exists, skipping: cpp-programming")
    else:
        logger.info("Course missing, creating: cpp-programming")
        try:
            from add_cpp_course import add_cpp_course
            add_cpp_course()
        except Exception as e:
            logger.error(f"Production database seeding failed for cpp: {e}")

    # 6. Cyber Security
    if Course.query.filter_by(slug="cyber-security").first():
        logger.info("Course already exists, skipping: cyber-security")
    else:
        logger.info("Course missing, creating: cyber-security")
        try:
            from add_cybersecurity_course import add_cybersecurity_course
            add_cybersecurity_course()
        except Exception as e:
            logger.error(f"Production database seeding failed for cyber security: {e}")

    # 7. DBMS and DSA
    dbms_slug = "dbms-mastery"
    dsa_slug = "dsa-mastery"
    missing_dbms_dsa = []
    for slug in [dbms_slug, dsa_slug]:
        if Course.query.filter_by(slug=slug).first():
            logger.info(f"Course already exists, skipping: {slug}")
        else:
            logger.info(f"Course missing, creating: {slug}")
            missing_dbms_dsa.append(slug)
            
    if missing_dbms_dsa:
        try:
            from add_dbms_dsa_courses import main as seed_dbms_dsa
            seed_dbms_dsa()
        except Exception as e:
            logger.error(f"Production database seeding failed for DBMS/DSA: {e}")

    logger.info("Production database initialization completed.")
