from flask import Blueprint, jsonify, request
import os
import json

roadmap_bp = Blueprint('roadmap', __name__)

ROADMAP_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../roadmap_data.json'))

def load_roadmap_data():
    if not os.path.exists(ROADMAP_FILE):
        return {}
    try:
        with open(ROADMAP_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading roadmap_data.json: {e}")
        return {}

# Slug mapping helper to support both short keys ('python') and course slugs ('python-programming')
SLUG_MAP = {
    'python-programming': 'python',
    'java-programming': 'java',
    'c-programming': 'c',
    'cpp-programming': 'cpp',
    'html-web-development': 'html',
    'css-responsive-design': 'css',
    'javascript-programming': 'javascript',
    'dbms-mastery': 'dbms',
    'dsa-mastery': 'dsa',
    'cyber-security': 'cybersecurity'
}

@roadmap_bp.route('', methods=['GET'], strict_slashes=False)
@roadmap_bp.route('/', methods=['GET'], strict_slashes=False)
def get_all_roadmaps():
    data = load_roadmap_data()
    summaries = []
    for key, val in data.items():
        summaries.append({
            'key': val.get('key'),
            'course_slug_ref': val.get('course_slug_ref'),
            'title': val.get('title'),
            'category': val.get('category'),
            'icon': val.get('icon'),
            'tagline': val.get('tagline'),
            'difficulty_progression': val.get('difficulty_progression'),
            'skill_stages_count': len(val.get('skill_stages', [])),
            'career_roles_count': len(val.get('career_directions', [])),
            'projects_count': len(val.get('projects', []))
        })
    return jsonify({'roadmaps': summaries}), 200

@roadmap_bp.route('/<key_or_slug>', methods=['GET'])
def get_roadmap_detail(key_or_slug):
    data = load_roadmap_data()
    
    # Resolve key if given a course slug
    key = SLUG_MAP.get(key_or_slug.lower(), key_or_slug.lower())
    
    roadmap = data.get(key)
    if not roadmap:
        return jsonify({'error': 'Roadmap not found', 'key': key_or_slug}), 404
        
    return jsonify({'roadmap': roadmap}), 200
