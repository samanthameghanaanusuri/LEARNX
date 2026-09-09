import sqlite3
import os

db_path = 'backend/instance/learnx.db' if os.path.exists('backend/instance/learnx.db') else 'backend/learnx.db'
print("Using DB:", db_path)

conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT id, title, slug FROM course WHERE id = 2 OR title LIKE '%Java%'")
print("Courses:", cur.fetchall())

cur.execute("""
    SELECT m.id, m.order_index, m.title, l.id, l.title, LENGTH(l.content)
    FROM course_module m
    LEFT JOIN lesson l ON l.module_id = m.id
    WHERE m.course_id = 2
    ORDER BY m.order_index, l.order_index
""")
modules = cur.fetchall()
print(f"Total rows for Course 2: {len(modules)}")
for row in modules:
    print(f"Module ID: {row[0]}, Order: {row[1]}, Module Title: {row[2]}, Lesson ID: {row[3]}, Lesson Title: {row[4]}, Content Size: {row[5]}")

conn.close()
