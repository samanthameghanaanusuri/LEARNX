import sqlite3
import os
import shutil
from datetime import datetime

def migrate():
    db_path = os.path.join('instance', 'learnx.db')
    
    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}. Skipping migration.")
        return

    # Backup the database
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = db_path + f'_migrate_student_{timestamp}.bak'
    shutil.copy2(db_path, backup_path)
    print(f"Database backed up to {backup_path}")

    # Alter the table
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if columns already exist
        cursor.execute("PRAGMA table_info(student);")
        columns = [col[1] for col in cursor.fetchall()]
        
        new_cols = [
            ("learning_time_minutes", "INTEGER DEFAULT 0"),
            ("current_streak", "INTEGER DEFAULT 0"),
            ("longest_streak", "INTEGER DEFAULT 0"),
            ("last_activity_date", "DATE NULL")
        ]
        
        for col_name, col_type in new_cols:
            if col_name not in columns:
                cursor.execute(f"ALTER TABLE student ADD COLUMN {col_name} {col_type};")
                print(f"Added column {col_name} to student table.")
            else:
                print(f"Column {col_name} already exists in student table.")
                
        conn.commit()
        print("Migration completed successfully.")
        
    except Exception as e:
        print(f"Migration failed: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    migrate()
