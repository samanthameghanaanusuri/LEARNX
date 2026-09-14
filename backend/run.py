import os
from app import create_app, db

app = create_app()

with app.app_context():
    # Create any new tables that don't exist yet.
    # This is safe and additive — it NEVER drops or deletes existing tables/data.
    db.create_all()
    
    # Optional one-time environment-gated production course restoration
    restore_mode = os.environ.get("RUN_COURSE_RESTORE", "").strip().lower()
    if restore_mode in ["true", "dry-run"]:
        from sync_production_courses import sync_production_courses
        print(f"=== RUN_COURSE_RESTORE={restore_mode} detected: Executing production course synchronization ===")
        sync_production_courses()
        print("=== Production course synchronization complete ===")

if __name__ == '__main__':
    # Start Flask development server on port 5000
    app.run(debug=True, host='127.0.0.1', port=5000)
