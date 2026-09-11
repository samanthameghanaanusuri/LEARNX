from app import create_app, db
from seed_production import seed_production

app = create_app()

with app.app_context():
    # Create any new tables that don't exist yet.
    # This is safe and additive — it NEVER drops or deletes existing tables/data.
    db.create_all()
    
    # Safely seed production courses idempotently
    seed_production()

if __name__ == '__main__':
    # Start Flask development server on port 5000
    app.run(debug=True, host='127.0.0.1', port=5000)
