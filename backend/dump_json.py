import json
import os
import sys

_script_dir = os.path.dirname(os.path.abspath(__file__))
if _script_dir not in sys.path:
    sys.path.insert(0, _script_dir)

import html_course_content

def update_json():
    json_path = os.path.join(_script_dir, 'web_courses_data.json')
    
    with open(json_path, 'r', encoding='utf-8') as f:
        courses = json.load(f)
        
    new_data = html_course_content.get_html_course_data()
    
    for i, c in enumerate(courses):
        if c['slug'] == new_data['slug'] or 'html' in c['slug'].lower():
            courses[i] = new_data
            break
            
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(courses, f, indent=4)
        
    print(f"Updated {json_path}")

if __name__ == "__main__":
    update_json()
