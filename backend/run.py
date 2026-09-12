import os
from app import create_app, db

app = create_app()

with app.app_context():
    # Create any new tables that don't exist yet.
    # This is safe and additive — it NEVER drops or deletes existing tables/data.
    db.create_all()
    
    # Optional one-time environment-gated Python synchronization
    if os.environ.get("RUN_PYTHON_SYNC", "").strip().lower() == "true":
        from sync_python_production import sync_python_course
        print("=== RUN_PYTHON_SYNC=true detected: Executing Python course synchronization ===")
        sync_python_course()
        print("=== RUN_PYTHON_SYNC synchronization complete ===")

if __name__ == '__main__':
    # Start Flask development server on port 5000
    app.run(debug=True, host='127.0.0.1', port=5000)
