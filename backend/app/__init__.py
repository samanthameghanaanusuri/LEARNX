from flask import Flask, send_from_directory
from flask_cors import CORS
from app.models import db
from config import Config
import os

def create_app(config_class=Config):
    # Set up static folder pointing to the frontend directory relative to the runner
    # We want Flask to serve frontend static files directly
    frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../frontend'))
    
    app = Flask(__name__, static_folder=frontend_dir, static_url_path='')
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    CORS(app, supports_credentials=True)

    # Serve landing page on root index
    @app.route('/')
    def serve_index():
        return send_from_directory(app.static_folder, 'index.html')

    # Serve specific static html pages
    @app.route('/<path:path>')
    def serve_pages(path):
        if os.path.exists(os.path.join(app.static_folder, path)):
            return send_from_directory(app.static_folder, path)
        return send_from_directory(app.static_folder, 'index.html')

    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.concepts import concepts_bp
    from app.routes.assessments import assessments_bp
    from app.routes.diagnosis import diagnosis_bp
    from app.routes.intervention import intervention_bp
    from app.routes.progress import progress_bp
    from app.routes.performance import performance_bp
    from app.routes.courses import courses_bp
    from app.routes.code import code_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(concepts_bp, url_prefix='/api/concepts')
    app.register_blueprint(assessments_bp, url_prefix='/api/assessments')
    app.register_blueprint(diagnosis_bp, url_prefix='/api/diagnosis')
    app.register_blueprint(intervention_bp, url_prefix='/api/intervention')
    app.register_blueprint(progress_bp, url_prefix='/api/progress')
    app.register_blueprint(performance_bp, url_prefix='/api/performance')
    app.register_blueprint(courses_bp, url_prefix='/api/courses')
    app.register_blueprint(code_bp, url_prefix='/api/code')
    
    from app.routes.ai_agent import ai_bp
    app.register_blueprint(ai_bp, url_prefix='/api/ai')

    return app
