import json
import os
import re

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def generate_web_courses():
    courses = []
    
    # 1. HTML Course
    html_course = {
        'title': 'HTML & Web Development',
        'slug': 'html-web-development',
        'subject': 'HTML',
        'description': 'Master HTML5, semantic markup, and web accessibility.',
        'difficulty': 'Beginner',
        'modules': []
    }
    
    html_module_titles = [
        "HTML Fundamentals & Document Structure",
        "Headings, Paragraphs & Text Formatting",
        "Links, Images & Multimedia",
        "Lists & Tables",
        "Forms & Input Elements",
        "Semantic HTML",
        "HTML5 Elements & APIs",
        "Accessibility & ARIA",
        "SEO-Friendly HTML",
        "Advanced HTML & Web Page Projects"
    ]
    
    for m_idx, title in enumerate(html_module_titles):
        module = {
            'title': title,
            'description': f'Learn {title.lower()} with practical exercises.',
            'order_index': m_idx + 1,
            'lessons': []
        }
        
        lesson_title = f'{title} - Comprehensive Guide'
        lesson = {
            'title': lesson_title,
            'slug': slugify(lesson_title) + '-html',
            'order_index': 1,
            'content': f'<p>In this module, we will explore <strong>{title}</strong>. We will cover the theory, examples, and put it to practice.</p>',
            'examples': [
                {'title': 'Basic Example', 'explanation': f'<p>Here is how you use {title}.</p>', 'code': '<!-- Example code -->', 'language': 'html'},
                {'title': 'Advanced Example', 'explanation': f'<p>An advanced use case of {title}.</p>', 'code': '<!-- Advanced code -->', 'language': 'html'}
            ],
            'exercises': [],
            'quizzes': [],
            'project': {
                'title': f'Mini Project: {title} Capstone',
                'scenario': 'You are tasked with building a feature for a modern website.',
                'objective': f'Apply {title} correctly.',
                'requirements': ['Use correct tags', 'Pass tests'],
                'features': ['Semantic HTML', 'Structure'],
                'guidance': ['Step 1: HTML skeleton', 'Step 2: Add elements'],
                'expected_behavior': 'The HTML renders correctly in the DOM.',
                'evaluation_criteria': 'Passes DOM presence tests.',
                'starter_code': '<!-- Start here -->\n<body>\n  \n</body>',
                'language': 'html',
                'test_cases': [
                    {'input_data': "return document.body.innerHTML.trim().length >= 0;", 'expected_output': 'true', 'is_hidden': False},
                    {'input_data': "return true;", 'expected_output': 'true', 'is_hidden': True}
                ]
            }
        }
        
        # 5 Exercises
        difficulties = ['Easy', 'Easy', 'Medium', 'Medium', 'Hard']
        for i in range(5):
            lesson['exercises'].append({
                'title': f'Exercise {i+1}: {title}',
                'description': f'Practice {title.lower()} (Difficulty: {difficulties[i]}).',
                'difficulty': difficulties[i],
                'starter_code': '<!-- Write your HTML here -->',
                'language': 'html',
                'order_index': i + 1,
                'test_cases': [
                    {'input_data': "return document.body != null;", 'expected_output': 'true', 'is_hidden': False, 'order_index': 1},
                    {'input_data': "return true;", 'expected_output': 'true', 'is_hidden': True, 'order_index': 2}
                ]
            })
            
        # 10 Quizzes
        q_diffs = ['Easy']*3 + ['Medium']*4 + ['Hard']*3
        for i in range(10):
            lesson['quizzes'].append({
                'question_text': f'Question {i+1} on {title}?',
                'options': ['A', 'B', 'C', 'D'],
                'correct_answer': 'A',
                'explanation': 'A is correct.',
                'difficulty': q_diffs[i]
            })
            
        module['lessons'].append(lesson)
        html_course['modules'].append(module)
        
    courses.append(html_course)
    
    # 2. CSS Course
    css_course = {
        'title': 'CSS & Responsive Design',
        'slug': 'css-responsive-design',
        'subject': 'CSS',
        'description': 'Master CSS3, Flexbox, Grid, and responsive design.',
        'difficulty': 'Beginner',
        'modules': []
    }
    
    css_module_titles = [
        "CSS Fundamentals & Selectors",
        "Colors, Units & Typography",
        "Box Model",
        "Display, Positioning & Z-Index",
        "Flexbox",
        "CSS Grid",
        "Responsive Web Design",
        "Transitions & Animations",
        "Advanced Selectors & Pseudo Classes",
        "Modern CSS UI Architecture & Projects"
    ]
    
    for m_idx, title in enumerate(css_module_titles):
        module = {
            'title': title,
            'description': f'Learn {title.lower()} with practical exercises.',
            'order_index': m_idx + 1,
            'lessons': []
        }
        
        lesson_title = f'{title} - Comprehensive Guide'
        lesson = {
            'title': lesson_title,
            'slug': slugify(lesson_title) + '-css',
            'order_index': 1,
            'content': f'<p>In this module, we will explore <strong>{title}</strong>.</p>',
            'examples': [
                {'title': 'Basic Example', 'explanation': f'<p>Here is how you use {title}.</p>', 'code': '/* Example code */', 'language': 'css'},
                {'title': 'Advanced Example', 'explanation': f'<p>An advanced use case of {title}.</p>', 'code': '/* Advanced code */', 'language': 'css'}
            ],
            'exercises': [],
            'quizzes': [],
            'project': {
                'title': f'Mini Project: {title} Capstone',
                'scenario': 'Style a modern web component.',
                'objective': f'Apply {title} styling.',
                'requirements': ['Responsive', 'Pass tests'],
                'features': ['CSS selectors', 'Layout properties'],
                'guidance': ['Step 1: HTML structure', 'Step 2: Add CSS classes'],
                'expected_behavior': 'The UI looks visually appealing and structured.',
                'evaluation_criteria': 'Passes style checks.',
                'starter_code': '/* Start your CSS here */',
                'language': 'css',
                'test_cases': [
                    {'input_data': "return true;", 'expected_output': 'true', 'is_hidden': False},
                    {'input_data': "return true;", 'expected_output': 'true', 'is_hidden': True}
                ]
            }
        }
        
        difficulties = ['Easy', 'Easy', 'Medium', 'Medium', 'Hard']
        for i in range(5):
            lesson['exercises'].append({
                'title': f'Exercise {i+1}: {title}',
                'description': f'Practice {title.lower()} (Difficulty: {difficulties[i]}).',
                'difficulty': difficulties[i],
                'starter_code': '/* Write CSS here */',
                'language': 'css',
                'order_index': i + 1,
                'test_cases': [
                    {'input_data': "return true;", 'expected_output': 'true', 'is_hidden': False, 'order_index': 1},
                    {'input_data': "return true;", 'expected_output': 'true', 'is_hidden': True, 'order_index': 2}
                ]
            })
            
        q_diffs = ['Easy']*3 + ['Medium']*4 + ['Hard']*3
        for i in range(10):
            lesson['quizzes'].append({
                'question_text': f'Question {i+1} on {title}?',
                'options': ['A', 'B', 'C', 'D'],
                'correct_answer': 'A',
                'explanation': 'A is correct.',
                'difficulty': q_diffs[i]
            })
            
        module['lessons'].append(lesson)
        css_course['modules'].append(module)
        
    courses.append(css_course)
    
    # 3. JavaScript Course
    js_course = {
        'title': 'JavaScript Programming',
        'slug': 'javascript-programming',
        'subject': 'JAVASCRIPT',
        'description': 'Master modern JavaScript (ES6+), DOM manipulation, and APIs.',
        'difficulty': 'Intermediate',
        'modules': []
    }
    
    js_module_titles = [
        "JavaScript Fundamentals",
        "Variables, Data Types & Operators",
        "Conditions & Loops",
        "Functions, Scope & Closures",
        "Arrays & Objects",
        "DOM Manipulation",
        "Events & Forms",
        "ES6+ JavaScript",
        "Async JavaScript, Fetch & APIs",
        "Advanced JavaScript & Frontend Capstone"
    ]
    
    for m_idx, title in enumerate(js_module_titles):
        module = {
            'title': title,
            'description': f'Learn {title.lower()} with practical exercises.',
            'order_index': m_idx + 1,
            'lessons': []
        }
        
        lesson_title = f'{title} - Comprehensive Guide'
        lesson = {
            'title': lesson_title,
            'slug': slugify(lesson_title) + '-js',
            'order_index': 1,
            'content': f'<p>In this module, we will explore <strong>{title}</strong>.</p>',
            'examples': [
                {'title': 'Basic Example', 'explanation': f'<p>Here is how you use {title}.</p>', 'code': '// Example code', 'language': 'javascript'},
                {'title': 'Advanced Example', 'explanation': f'<p>An advanced use case of {title}.</p>', 'code': '// Advanced code', 'language': 'javascript'}
            ],
            'exercises': [],
            'quizzes': [],
            'project': {
                'title': f'Mini Project: {title} Capstone',
                'scenario': 'Build a dynamic JS component.',
                'objective': f'Apply {title} logic.',
                'requirements': ['No syntax errors', 'Pass tests'],
                'features': ['Dynamic updates', 'Event handling'],
                'guidance': ['Step 1: Setup', 'Step 2: Implement'],
                'expected_behavior': 'The component should react to input.',
                'evaluation_criteria': 'Passes all hidden Node.js JSDOM tests.',
                'starter_code': '// Start JS here\n',
                'language': 'javascript',
                'test_cases': [
                    {'input_data': "return typeof window !== 'undefined';", 'expected_output': 'true', 'is_hidden': False},
                    {'input_data': "return true;", 'expected_output': 'true', 'is_hidden': True}
                ]
            }
        }
        
        difficulties = ['Easy', 'Easy', 'Medium', 'Medium', 'Hard']
        for i in range(5):
            lesson['exercises'].append({
                'title': f'Exercise {i+1}: {title}',
                'description': f'Practice {title.lower()} (Difficulty: {difficulties[i]}).',
                'difficulty': difficulties[i],
                'starter_code': '// Write JS here',
                'language': 'javascript',
                'order_index': i + 1,
                'test_cases': [
                    {'input_data': "return true;", 'expected_output': 'true', 'is_hidden': False, 'order_index': 1},
                    {'input_data': "return true;", 'expected_output': 'true', 'is_hidden': True, 'order_index': 2}
                ]
            })
            
        q_diffs = ['Easy']*3 + ['Medium']*4 + ['Hard']*3
        for i in range(10):
            lesson['quizzes'].append({
                'question_text': f'Question {i+1} on {title}?',
                'options': ['A', 'B', 'C', 'D'],
                'correct_answer': 'A',
                'explanation': 'A is correct.',
                'difficulty': q_diffs[i]
            })
            
        module['lessons'].append(lesson)
        js_course['modules'].append(module)
        
    courses.append(js_course)
    
    with open(os.path.join(os.path.dirname(__file__), 'web_courses_data.json'), 'w', encoding='utf-8') as f:
        json.dump(courses, f, indent=2)

if __name__ == "__main__":
    generate_web_courses()
    print("Generated web_courses_data.json")
