def get_module_data():
    return {
        "title": "HTML Foundations",
        "description": "Learn the absolute basics of HTML, document structure, semantic text formatting, and how to build your first valid webpage.",
        "order_index": 1,
        "lessons": [
            {
                "title": "Introduction to HTML & Document Structure",
                "slug": "intro-html-document-structure",
                "content": "HTML (HyperText Markup Language) is the backbone of the Web. It defines the structure and meaning of web content. HTML uses 'markup' to annotate text, images, and other content for display in a Web browser.\\n\\n### Document Structure\\nEvery standard HTML page requires a specific foundational structure:\\n- `<!DOCTYPE html>`: Tells the browser this is an HTML5 document. It must be the very first line.\\n- `<html>`: The root element that wraps all content on the page.\\n- `<head>`: Contains metadata (data about data), such as the page title, character set, and links to CSS. This content is not visible on the webpage itself.\\n- `<body>`: Contains all the visible content—headings, paragraphs, images, links, etc.\\n\\n### Headings and Paragraphs\\nHTML headings communicate document hierarchy. `<h1>` represents the page's primary heading, while `<h2>`–`<h6>` represent progressively nested sections. Heading levels should not be selected merely for visual size; CSS should control presentation. Paragraphs are defined with the `<p>` tag.\\n\\n### Text Formatting\\nHTML provides semantic tags to give meaning to text:\\n- `<strong>`: Indicates strong importance (typically rendered bold).\\n- `<em>`: Indicates emphasized text (typically rendered italic).\\n- `<mark>`: Highlights text.\\n- `<del>` and `<ins>`: Represent deleted and inserted text.\\n\\n### Block vs Inline Elements\\n- **Block-level elements** (like `<h1>`, `<p>`, `<div>`) always start on a new line and take up the full width available.\\n- **Inline elements** (like `<a>`, `<span>`, `<strong>`) do not start on a new line and only take up as much width as necessary.",
                "order_index": 1,
                "examples": [
                    {
                        "title": "A Complete HTML Document",
                        "explanation": "This is a real, valid HTML5 document structure containing metadata and visible content.",
                        "code": '''<!DOCTYPE html>\\n<html lang="en">\\n<head>\\n    <meta charset="UTF-8">\\n    <title>My First Webpage</title>\\n</head>\\n<body>\\n    <h1>Welcome to Web Development</h1>\\n    <p>This is my very first webpage.</p>\\n</body>\\n</html>''',
                        "language": "html",
                        "order_index": 1
                    },
                    {
                        "title": "Semantic Text Formatting",
                        "explanation": "Using semantic formatting tags to add meaning to text, not just visual styling.",
                        "code": '''<h2>Sale Announcement</h2>\\n<p><strong>Warning:</strong> The sale ends today!</p>\\n<p>The original price was <del>$50</del>, but now it is <ins>$25</ins>.</p>\\n<p>Please remember to <em>bring your receipt</em>.</p>''',
                        "language": "html",
                        "order_index": 2
                    }
                ],
                "exercises": [
                    {
                        "title": "Create a Basic HTML Document",
                        "description": "Construct a valid HTML5 document. Set the title to 'Hello World' and add an `h1` heading containing 'Hello, HTML!' inside the body.",
                        "difficulty": "Easy",
                        "starter_code": '''<!-- Write your HTML document here -->''',
                        "language": "html",
                        "order_index": 1,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<!DOCTYPE html><html><head><title>Hello World</title></head><body><h1>Hello, HTML!</h1></body></html>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Build a Personal Introduction",
                        "description": "Create a `body` section containing an `h2` heading with your name (e.g., 'Jane Doe') and a `p` paragraph describing yourself. (For the test to pass, use 'Jane Doe' and 'I am a web developer.')",
                        "difficulty": "Easy",
                        "starter_code": '''<body>\\n\\n</body>''',
                        "language": "html",
                        "order_index": 2,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<body><h2>Jane Doe</h2><p>I am a web developer.</p></body>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Create a Properly Structured Article",
                        "description": "Inside a `body` tag, create an `h1` for an article title ('News of the Day'), followed by an `h3` subtitle ('By John Smith'), and a `p` paragraph containing 'Breaking news happened today.'",
                        "difficulty": "Easy",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 3,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<body><h1>News of the Day</h1><h3>By John Smith</h3><p>Breaking news happened today.</p></body>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Use Text Formatting Correctly",
                        "description": "Create a paragraph that contains the text 'This is highly important'. Wrap the word 'highly' in the `em` tag and the word 'important' in the `strong` tag.",
                        "difficulty": "Easy",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 4,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<p>This is <em>highly</em> <strong>important</strong></p>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Build a Simple About Me Page",
                        "description": "Combine concepts to build a full page: DOCTYPE, html, head, title ('About Me'), body. Inside body, add an `h1` 'About Me', an `h2` 'Hobbies', and a paragraph containing 'I like coding and reading.'",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 5,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<!DOCTYPE html><html><head><title>About Me</title></head><body><h1>About Me</h1><h2>Hobbies</h2><p>I like coding and reading.</p></body></html>''', "is_hidden": False, "order_index": 1}
                        ]
                    }
                ],
                "quizzes": [
                    {
                        "question_text": "Why must an HTML document begin with the <!DOCTYPE html> declaration?",
                        "options": ["To link a CSS stylesheet", "To define the page as an HTML5 document so browsers render it in standards mode", "To initialize the JavaScript engine", "To hide the document from search engines"],
                        "correct_answer": "To define the page as an HTML5 document so browsers render it in standards mode",
                        "explanation": "The doctype declaration ensures that the browser uses the latest HTML5 specifications and avoids 'quirks mode'.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Which HTML element contains metadata, such as the page title and character encoding?",
                        "options": ["<body>", "<header>", "<head>", "<meta>"],
                        "correct_answer": "<head>",
                        "explanation": "The <head> element is the container for metadata, which is not rendered directly on the visible web page.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "What is the semantic purpose of the <h1> through <h6> tags?",
                        "options": ["To make text bold and large", "To define the document's heading hierarchy and structure", "To create bold list items", "To divide the page into columns"],
                        "correct_answer": "To define the document's heading hierarchy and structure",
                        "explanation": "Headings provide structural outline for screen readers and search engines; visual sizing is a secondary side-effect handled by CSS.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "What is the difference between a block-level and an inline element?",
                        "options": ["Inline elements start on a new line; block elements do not", "Block elements start on a new line and take full width; inline elements only take necessary width", "Block elements can only contain text; inline elements can contain images", "There is no difference in modern HTML"],
                        "correct_answer": "Block elements start on a new line and take full width; inline elements only take necessary width",
                        "explanation": "Block elements form structural blocks on the page, pushing subsequent elements to a new line, whereas inline elements flow within the text.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Which tag should be used to indicate text that has strong importance or seriousness?",
                        "options": ["<b>", "<i>", "<strong>", "<em>"],
                        "correct_answer": "<strong>",
                        "explanation": "While <b> simply makes text bold, <strong> conveys semantic strong importance, which assistive technologies can interpret.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "How do you create an HTML comment?",
                        "options": ["// This is a comment", "<!-- This is a comment -->", "/* This is a comment */", "# This is a comment"],
                        "correct_answer": "<!-- This is a comment -->",
                        "explanation": "HTML comments are enclosed in <!-- and -->.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "What does the <title> tag do?",
                        "options": ["Creates a large heading on the page", "Sets the title displayed in the browser tab and search engine results", "Changes the font of the entire document", "Embeds a title image"],
                        "correct_answer": "Sets the title displayed in the browser tab and search engine results",
                        "explanation": "The <title> tag provides the text for the browser tab and is crucial for SEO.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Which of the following is considered an inline element by default?",
                        "options": ["<div>", "<p>", "<h1>", "<span>"],
                        "correct_answer": "<span>",
                        "explanation": "<span> is a generic inline container, unlike div, p, and h1 which are block-level.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "What is the correct way to indicate deleted text and newly inserted text?",
                        "options": ["<strike> and <u>", "<del> and <ins>", "<remove> and <add>", "<s> and <i>"],
                        "correct_answer": "<del> and <ins>",
                        "explanation": "<del> represents deleted text and <ins> represents inserted text, providing semantic meaning for edits.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Why should you NOT use <h3> to make a sentence bold and slightly larger if it isn't actually a sub-heading?",
                        "options": ["It breaks CSS styling", "It negatively impacts accessibility (screen readers) and SEO by breaking the document outline", "It causes syntax errors", "It makes the page load slower"],
                        "correct_answer": "It negatively impacts accessibility (screen readers) and SEO by breaking the document outline",
                        "explanation": "Headings must be used for structure, not visual styling. Misusing them confuses assistive technologies and search engines.",
                        "difficulty": "Hard"
                    }
                ],
                "project": {
                    "title": "Personal Profile Page",
                    "scenario": "You are building the foundational HTML structure for your online developer profile.",
                    "objective": "Apply document structure, headings, paragraphs, and semantic formatting.",
                    "requirements": "Create a valid HTML5 document. Include a title ('Developer Profile'). In the body, include an h1 ('My Profile'), an h2 ('About'), a paragraph describing yourself using strong and em tags, an h2 ('Skills'), and a final paragraph with closing remarks.",
                    "features": "Valid Document Outline, Semantic Formatting",
                    "guidance": "Ensure your document outline is logical (h1 followed by h2s). Don't forget the DOCTYPE.",
                    "expected_behavior": "A well-structured HTML page displaying a basic profile outline.",
                    "evaluation_criteria": "Presence of DOCTYPE, html, head, title, body, and correct heading hierarchy.",
                    "starter_code": '''<!DOCTYPE html>\\n<html>\\n<head>\\n\\n</head>\\n<body>\\n\\n</body>\\n</html>''',
                    "language": "html",
                    "test_cases": [
                        {"input_data": '''''', "expected_output": '''<!DOCTYPE html><html><head><title>Developer Profile</title></head><body><h1>My Profile</h1><h2>About</h2><p>I am a <strong>developer</strong> who loves <em>coding</em>.</p><h2>Skills</h2><p>HTML</p></body></html>''', "is_hidden": False, "order_index": 1}
                    ]
                }
            }
        ]
    }
