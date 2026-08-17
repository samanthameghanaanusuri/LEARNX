import os

def create_module_1():
    content = '''
def get_module_data():
    return {
        "title": "HTML Fundamentals & Document Structure",
        "description": "Understand the building blocks of the web. Learn how to structure a basic HTML document.",
        "order_index": 1,
        "lessons": [
            {
                "title": "Introduction to HTML",
                "slug": "intro-to-html",
                "content": "HTML (HyperText Markup Language) is the standard markup language for documents designed to be displayed in a web browser. It consists of a series of elements, which you use to enclose, or wrap, different parts of the content to make it appear a certain way, or act a certain way. The enclosing tags can make a word or image hyperlink to somewhere else, can italicize words, can make the font bigger or smaller, and so on.\\n\\nA basic HTML document structure includes the <!DOCTYPE html> declaration, the <html> root element, the <head> element for metadata, and the <body> element for visible content.",
                "order_index": 1,
                "examples": [
                    {
                        "title": "Basic HTML Skeleton",
                        "explanation": "This is the minimum required structure for a valid HTML5 document. The DOCTYPE tells the browser to use HTML5 standards.",
                        "code": "<!DOCTYPE html>\\n<html>\\n<head>\\n    <title>My First Page</title>\\n</head>\\n<body>\\n    <h1>Hello World!</h1>\\n    <p>Welcome to web development.</p>\\n</body>\\n</html>",
                        "language": "html"
                    },
                    {
                        "title": "HTML Tags and Elements",
                        "explanation": "An HTML element is distinguished by a start tag, some content, and an end tag.",
                        "code": "<p>This is a paragraph element.</p>\\n<a href=\\"https://google.com\\">This is a link element</a>",
                        "language": "html"
                    }
                ],
                "exercises": [
                    {
                        "title": "Create a Basic Skeleton",
                        "description": "Write the standard HTML5 skeleton. Include a title 'My Skeleton' and a body with no content.",
                        "difficulty": "Easy",
                        "starter_code": "<!-- Write your HTML here -->",
                        "language": "html",
                        "order_index": 1,
                        "test_cases": [
                            {"input_data": "", "expected_output": "<!DOCTYPE html><html><head><title>My Skeleton</title></head><body></body></html>", "is_hidden": False}
                        ]
                    },
                    {
                        "title": "Add a Paragraph",
                        "description": "Inside the body of your HTML, add a paragraph saying 'Learning HTML!'.",
                        "difficulty": "Easy",
                        "starter_code": "<!DOCTYPE html>\\n<html>\\n<head>\\n    <title>My Skeleton</title>\\n</head>\\n<body>\\n\\n</body>\\n</html>",
                        "language": "html",
                        "order_index": 2,
                        "test_cases": [
                            {"input_data": "", "expected_output": "<!DOCTYPE html><html><head><title>My Skeleton</title></head><body><p>Learning HTML!</p></body></html>", "is_hidden": False}
                        ]
                    },
                    {
                        "title": "Fix the Tags",
                        "description": "The following HTML has improperly closed tags. Fix them.",
                        "difficulty": "Medium",
                        "starter_code": "<h1>Welcome to my site</h2>\\n<p>This is a paragraph</p",
                        "language": "html",
                        "order_index": 3,
                        "test_cases": [
                            {"input_data": "", "expected_output": "<h1>Welcome to my site</h1>\\n<p>This is a paragraph</p>", "is_hidden": False}
                        ]
                    },
                    {
                        "title": "Nesting Elements",
                        "description": "Create a div element that contains a paragraph element with the text 'Nested'.",
                        "difficulty": "Medium",
                        "starter_code": "<!-- Write your nested elements here -->",
                        "language": "html",
                        "order_index": 4,
                        "test_cases": [
                            {"input_data": "", "expected_output": "<div><p>Nested</p></div>", "is_hidden": False}
                        ]
                    },
                    {
                        "title": "Multiple Paragraphs",
                        "description": "Create two consecutive paragraphs containing 'First' and 'Second'.",
                        "difficulty": "Easy",
                        "starter_code": "",
                        "language": "html",
                        "order_index": 5,
                        "test_cases": [
                            {"input_data": "", "expected_output": "<p>First</p><p>Second</p>", "is_hidden": False}
                        ]
                    }
                ],
                "quizzes": [
                    {
                        "question_text": "Which declaration defines an HTML5 document?",
                        "options": ["<doctype html>", "<!DOCTYPE html>", "<html>", "<html5>"],
                        "correct_answer": "<!DOCTYPE html>",
                        "explanation": "<!DOCTYPE html> is the correct, standard declaration for HTML5.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "What does the <head> element contain?",
                        "options": ["Visible page content", "Metadata and document title", "JavaScript only", "CSS only"],
                        "correct_answer": "Metadata and document title",
                        "explanation": "The head element contains meta-information, title, and links to scripts and styles.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Which element represents the root of an HTML document?",
                        "options": ["<body>", "<head>", "<html>", "<root>"],
                        "correct_answer": "<html>",
                        "explanation": "The <html> element is the root element that wraps all content.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "What does HTML stand for?",
                        "options": ["Hyperlinks and Text Markup Language", "HyperText Markup Language", "Home Tool Markup Language", "Hyper Tool Markup Language"],
                        "correct_answer": "HyperText Markup Language",
                        "explanation": "HTML stands for HyperText Markup Language.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Where should the <title> element be placed?",
                        "options": ["Inside <body>", "Inside <head>", "Before <!DOCTYPE html>", "Inside <footer>"],
                        "correct_answer": "Inside <head>",
                        "explanation": "The title element is metadata and belongs inside the head element.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Are HTML tags case-sensitive?",
                        "options": ["Yes, they must be uppercase", "Yes, they must be lowercase", "No, but lowercase is recommended", "No, but uppercase is recommended"],
                        "correct_answer": "No, but lowercase is recommended",
                        "explanation": "HTML tags are not case-sensitive, but W3C recommends lowercase.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Which tag is used to create a paragraph?",
                        "options": ["<p>", "<paragraph>", "<para>", "<text>"],
                        "correct_answer": "<p>",
                        "explanation": "The <p> tag defines a paragraph.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "How do you close a <p> tag?",
                        "options": ["</p>", "<p/>", "<\\p>", "It doesn't need closing"],
                        "correct_answer": "</p>",
                        "explanation": "Most HTML elements are closed with a forward slash before the tag name.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "What is an empty HTML element?",
                        "options": ["An element with no text content", "An element with no closing tag and no content", "An element that is hidden", "An element with class='empty'"],
                        "correct_answer": "An element with no closing tag and no content",
                        "explanation": "Elements like <br> or <img> have no content and no closing tag; they are empty elements.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "What is the purpose of the <body> tag?",
                        "options": ["To store metadata", "To wrap all the content visible to the user", "To define the page structure", "To contain scripts only"],
                        "correct_answer": "To wrap all the content visible to the user",
                        "explanation": "Everything inside the <body> tag is rendered on the screen by the browser.",
                        "difficulty": "Easy"
                    }
                ],
                "project": {
                    "title": "Build a Simple Profile Page Structure",
                    "scenario": "You have been asked to create the basic HTML structure for a personal profile page.",
                    "objective": "Use standard HTML5 elements to structure the page correctly with a title and basic body text.",
                    "requirements": "Must include DOCTYPE, html, head, title ('My Profile'), and a body containing a paragraph saying 'Welcome to my profile'.",
                    "features": "Valid HTML5, well-structured document",
                    "guidance": "Start with the DOCTYPE, then add your root <html> tag. Inside, add <head> and <body>.",
                    "expected_behavior": "A standard valid HTML document rendering the welcome text.",
                    "evaluation_criteria": "Correct nesting and presence of all required tags.",
                    "starter_code": "<!-- Start coding here -->",
                    "language": "html",
                    "test_cases": [
                        {"input_data": "", "expected_output": "<!DOCTYPE html><html><head><title>My Profile</title></head><body><p>Welcome to my profile</p></body></html>", "is_hidden": False}
                    ]
                }
            }
        ]
    }
'''
    with open('backend/html_course_data/module_1.py', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    create_module_1()
    print("Created module_1.py")
