import os
import sys

# Import all modules
try:
    import html_data_m1
    import html_data_m2
    import html_data_m3
    import html_data_m4
    import html_data_m5
    import html_data_m6
    import html_data_m7
    import html_data_m8
    import html_data_m9
    import html_data_m10
except ImportError:
    pass # We will create them

def get_html_course_data():
    modules = []
    
    # We will dynamically load the modules if they exist
    for i in range(1, 11):
        try:
            mod = sys.modules.get(f'html_data_m{i}')
            if mod:
                modules.append(mod.get_module_data())
            else:
                # Import dynamically if not already imported
                mod = __import__(f'html_data_m{i}')
                modules.append(mod.get_module_data())
        except ImportError:
            print(f"Warning: html_data_m{i} not found.")
            pass
            
    course_data = {
        "title": "HTML & Web Development",
        "slug": "html-web-development",
        "description": "Master HTML from absolute beginner to advanced. Learn semantic markup, forms, media, and professional page architecture.",
        "difficulty": "Beginner",
        "category": "Web Development",
        "subject": "HTML",
        "modules": modules
    }
    return course_data
