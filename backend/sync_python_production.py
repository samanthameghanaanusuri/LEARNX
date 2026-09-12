# -*- coding: utf-8 -*-
import os
import sys
import logging

# Ensure backend directory is in Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import Course, CourseModule, Lesson
from seed_courses import seed_course_data
from course_data_1 import COURSE_MODULES_1_TO_15
from course_data_2 import COURSE_MODULES_16_TO_30

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("sync_python_production")

def sync_python_course():
    app = create_app()
    with app.app_context():
        logger.info("=== LEARNX Safe Python Course Synchronization ===")
        
        # 1. Combine authoritative source data
        expected_modules_data = COURSE_MODULES_1_TO_15 + COURSE_MODULES_16_TO_30
        expected_mod_count = len(expected_modules_data)
        
        # Calculate expected lesson count from expected_modules_data
        expected_les_count = sum(
            len(m.get('lessons', [])) if 'lessons' in m else 1 for m in expected_modules_data
        )

        # 2. Strict validation of source dataset count
        if expected_mod_count != 30:
            logger.error(f"CRITICAL ERROR: Authoritative source data contains {expected_mod_count} modules, expected exactly 30. Halting operation.")
            raise ValueError(f"Invalid source module count: {expected_mod_count}")

        # 3. Locate ONLY python-programming course
        course = Course.query.filter_by(slug="python-programming").first()
        if not course:
            logger.error("CRITICAL ERROR: Course slug 'python-programming' does not exist in the database. Halting operation.")
            raise RuntimeError("Course 'python-programming' not found.")

        mod_count_before = CourseModule.query.filter_by(course_id=course.id).count()
        les_count_before = Lesson.query.join(CourseModule).filter(CourseModule.course_id == course.id).count()

        logger.info(f"Python Course ID           : {course.id}")
        logger.info(f"Python Course Slug         : {course.slug}")
        logger.info(f"Expected Module Count      : {expected_mod_count}")
        logger.info(f"Actual Module Count BEFORE : {mod_count_before}")
        logger.info(f"Expected Lesson Count      : {expected_les_count}")
        logger.info(f"Actual Lesson Count BEFORE : {les_count_before}")

        if mod_count_before >= expected_mod_count:
            logger.info("Python course already has complete module architecture. Synchronization not required.")
        else:
            logger.info(f"Synchronizing Python course data (Current: {mod_count_before} -> Expected: {expected_mod_count})...")
            try:
                seed_course_data(
                    course_slug="python-programming",
                    course_title="Python Programming — Beginner to Advanced",
                    course_description="Master Python from the basics to advanced concepts like OOP, Decorators, and Algorithms. Includes quizzes, exercises, and knowledge tracing.",
                    subject_code="PYTHON",
                    subject_name="Python Language",
                    subject_desc="Python programming concepts",
                    modules_data=expected_modules_data,
                    lang_key="python"
                )
                logger.info("Synchronization succeeded.")
            except Exception as e:
                db.session.rollback()
                logger.error(f"Synchronization failed with error: {e}")
                raise e

        mod_count_after = CourseModule.query.filter_by(course_id=course.id).count()
        les_count_after = Lesson.query.join(CourseModule).filter(CourseModule.course_id == course.id).count()

        logger.info("\n=== POST-SYNCHRONIZATION METRICS ===")
        logger.info(f"Python Course ID          : {course.id}")
        logger.info(f"Expected Module Count     : {expected_mod_count}")
        logger.info(f"Actual Module Count AFTER : {mod_count_after}")
        logger.info(f"Expected Lesson Count     : {expected_les_count}")
        logger.info(f"Actual Lesson Count AFTER : {les_count_after}")

        logger.info("\n=== PYTHON MODULE LIST ===")
        modules = CourseModule.query.filter_by(course_id=course.id).order_by(CourseModule.order_index).all()
        for mod in modules:
            logger.info(f"  Module {mod.order_index:02d}: {mod.title}")

if __name__ == '__main__':
    sync_python_course()
