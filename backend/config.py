import os
from dotenv import load_dotenv

# Load local .env if it exists
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'learnx-secure-dev-key-129847')
    
    # Handle Render's postgres:// vs postgresql:// SQLAlchemy requirement
    db_url = os.environ.get('DATABASE_URL', 'sqlite:///learnx.db')
    if db_url.startswith('postgres://'):
        db_url = db_url.replace('postgres://', 'postgresql://', 1)
        
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Bayesian Knowledge Tracing parameters
    BKT_PARAMS = {
        'p_init': 0.40,
        'p_learn': 0.10,
        'p_forget': 0.00,
        'p_guess': 0.20,
        'p_slip': 0.10
    }
