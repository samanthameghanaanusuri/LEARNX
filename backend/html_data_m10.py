def get_module_data():
    return {
        "title": "Advanced HTML Capstone",
        "description": "Integrate everything. Build complex, accessible, semantic, and highly optimized page structures from scratch.",
        "order_index": 10,
        "lessons": [
            {
                "title": "Comprehensive Real-World Integration",
                "slug": "advanced-html-capstone",
                "content": "You have reached the final module. It is time to integrate all the concepts you have learned.\\n\\n### The Complete Picture\\nA professional HTML developer considers all of the following simultaneously when writing code:\\n1. **Validity**: Does it pass the W3C validator? Are all tags closed? Are attributes quoted correctly?\\n2. **Semantics**: Did I use the correct tag for the job? (`<nav>` for navigation, `<button>` for actions, `<a>` for links, `<main>` for core content).\\n3. **Accessibility (a11y)**: Can a screen reader understand this? Are there `alt` attributes? Is the heading hierarchy logical? Are form inputs tied to labels?\\n4. **Performance**: Are scripts deferred? Are images lazy-loaded? Are critical assets preloaded?\\n5. **SEO**: Is the `<title>` present? Are viewport and description `<meta>` tags configured? Are Open Graph tags set?\\n\\n### Debugging HTML\\nWhen things look wrong, use the Browser Developer Tools (F12 or Right Click -> Inspect). You can view the rendered DOM, check computed styles, and see if tags were implicitly closed by the browser due to invalid nesting.",
                "order_index": 1,
                "examples": [
                    {
                        "title": "A Complete Production Skeleton",
                        "explanation": "A fully integrated document containing SEO, performance tweaks, accessibility, and semantics.",
                        "code": '''<!DOCTYPE html>\\n<html lang=\"en\">\\n<head>\\n    <meta charset=\"UTF-8\">\\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\\n    <title>SaaS Dashboard</title>\\n    <meta name=\"description\" content=\"Manage your data effectively.\">\\n    <link rel=\"preload\" href=\"style.css\" as=\"style\">\\n    <script src=\"app.js\" defer></script>\\n</head>\\n<body>\\n    <header>\\n        <nav aria-label=\"Primary Navigation\">\\n            <a href=\"/home\">Home</a>\\n            <a href=\"/settings\">Settings</a>\\n        </nav>\\n    </header>\\n    <main>\\n        <section id=\"dashboard-overview\">\\n            <h1>Dashboard</h1>\\n            <figure>\\n                <img src=\"chart.webp\" alt=\"Sales growth chart showing upward trend\" loading=\"lazy\">\\n                <figcaption>Q3 Sales Data</figcaption>\\n            </figure>\\n        </section>\\n    </main>\\n    <footer>\\n        <p>&copy; 2025 Company</p>\\n    </footer>\\n</body>\\n</html>''',
                        "language": "html",
                        "order_index": 1
                    },
                    {
                        "title": "Debugging Example",
                        "explanation": "A common mistake is putting block elements inside inline elements, like a <div> inside a <p>. Browsers will break the DOM to fix it.",
                        "code": '''<!-- BAD HTML: -->\\n<p>\\n    <div>This is invalid!</div>\\n</p>\\n\\n<!-- WHAT THE BROWSER ACTUALLY RENDERS: -->\\n<p></p>\\n<div>This is invalid!</div>\\n<p></p>''',
                        "language": "html",
                        "order_index": 2
                    }
                ],
                "exercises": [
                    {
                        "title": "Fix Broken Semantics",
                        "description": "Convert the invalid structure `<p><h2>Title</h2></p>` into a valid structure by using an `article` to wrap the `h2`.",
                        "difficulty": "Medium",
                        "starter_code": '''<p><h2>Title</h2></p>''',
                        "language": "html",
                        "order_index": 1,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<article><h2>Title</h2></article>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Repair an Inaccessible Form",
                        "description": "The input has no label. Add a `label` element for the input. Ensure they are programmatically linked using `for` and `id`.",
                        "difficulty": "Medium",
                        "starter_code": '''<input type=\"text\" name=\"search\">''',
                        "language": "html",
                        "order_index": 2,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<label for=\"srch\">Search</label><input type=\"text\" id=\"srch\" name=\"search\">''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Improve SEO Metadata",
                        "description": "Add a `title` ('Dashboard'), a `meta` description ('User dashboard'), and a `meta` viewport tag.",
                        "difficulty": "Medium",
                        "starter_code": '''<head></head>''',
                        "language": "html",
                        "order_index": 3,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<head><title>Dashboard</title><meta name=\"description\" content=\"User dashboard\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"></head>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Build a Complex Dashboard Structure",
                        "description": "Create a `main` element. Inside, an `aside` with a `nav` containing a link. Next to the `aside`, a `section` containing a `table` with one `tr` and one `td`.",
                        "difficulty": "Hard",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 4,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<main><aside><nav><a href=\"#\">Link</a></nav></aside><section><table><tr><td></td></tr></table></section></main>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Build a Complete Multi-Section Page",
                        "description": "Create a `body` with a `header`, a `main` (containing two `section`s), and a `footer`.",
                        "difficulty": "Hard",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 5,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<body><header></header><main><section></section><section></section></main><footer></footer></body>''', "is_hidden": False, "order_index": 1}
                        ]
                    }
                ],
                "quizzes": [
                    {
                        "question_text": "What does a11y stand for?",
                        "options": ["Alignment", "Accessibility (A, followed by 11 letters, followed by Y)", "Automated Layout Library", "Advanced 11th Year"],
                        "correct_answer": "Accessibility (A, followed by 11 letters, followed by Y)",
                        "explanation": "A11y is a common numeronym for accessibility.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Which of the following is an invalid nesting of HTML elements?",
                        "options": ["An <li> inside a <ul>", "An <a> inside a <p>", "A <div> inside a <p>", "A <p> inside a <div>"],
                        "correct_answer": "A <div> inside a <p>",
                        "explanation": "A block-level element (<div>) cannot be placed inside an inline-container element like <p>. The browser will automatically close the <p>.",
                        "difficulty": "Hard"
                    },
                    {
                        "question_text": "Why should you use <button> instead of a styled <div> for clickable actions?",
                        "options": ["Because a button is natively focusable by the keyboard and triggers on the Enter and Spacebar keys", "Because a <div> cannot have a click event", "Because a <div> takes up too much memory", "There is no reason, a <div> is fine"],
                        "correct_answer": "Because a button is natively focusable by the keyboard and triggers on the Enter and Spacebar keys",
                        "explanation": "Using native interactive elements ensures full accessibility out-of-the-box.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "How can you view the actual rendered DOM and computed styles on a webpage?",
                        "options": ["View Page Source", "Browser Developer Tools (Inspect)", "Download the HTML file", "You cannot view it"],
                        "correct_answer": "Browser Developer Tools (Inspect)",
                        "explanation": "DevTools show the live, parsed DOM, which may differ from the original source if there were HTML errors or JavaScript modifications.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Which attribute on the <html> tag specifies the language of the document, aiding screen readers?",
                        "options": ["lang", "language", "locale", "dir"],
                        "correct_answer": "lang",
                        "explanation": "<html lang=\"en\"> tells the screen reader to use English pronunciation rules.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "What is the purpose of the W3C Markup Validation Service?",
                        "options": ["To compile HTML to machine code", "To check HTML documents for conformance to standard specifications and catch structural errors", "To minify HTML files", "To host HTML files"],
                        "correct_answer": "To check HTML documents for conformance to standard specifications and catch structural errors",
                        "explanation": "The validator parses your code against the official specification to highlight errors.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "In a robust architecture, where should you place your <script> tags if you are NOT using 'defer' or 'async'?",
                        "options": ["In the <head>", "Just before the closing </body> tag", "At the very top of the file before <!DOCTYPE>", "Inside a <div>"],
                        "correct_answer": "Just before the closing </body> tag",
                        "explanation": "Placing blocking scripts at the end of the body ensures the HTML is parsed and rendered before the script halts the thread.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "What is the main difference between an absolute URL and a relative URL in an href attribute?",
                        "options": ["Absolute includes the full domain protocol (e.g., https://...); relative specifies a path relative to the current site", "Relative URLs are faster", "Absolute URLs are only for images", "They are identical"],
                        "correct_answer": "Absolute includes the full domain protocol (e.g., https://...); relative specifies a path relative to the current site",
                        "explanation": "Relative URLs are essential for portability (moving a site between environments) without breaking links.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Is it valid to have multiple <main> tags on a single page?",
                        "options": ["Yes, you can have as many as you want", "No, there should only be one visible <main> element per document", "Yes, but they must be nested", "No, <main> is deprecated"],
                        "correct_answer": "No, there should only be one visible <main> element per document",
                        "explanation": "The <main> tag represents the unique, primary content. Having multiple visible <main> elements confuses assistive tech.",
                        "difficulty": "Hard"
                    },
                    {
                        "question_text": "What happens if an <img> tag is missing the 'alt' attribute?",
                        "options": ["The image won't load", "It fails accessibility guidelines, as screen readers will likely read the raw filename instead", "The browser crashes", "Nothing, it's completely optional"],
                        "correct_answer": "It fails accessibility guidelines, as screen readers will likely read the raw filename instead",
                        "explanation": "A missing alt attribute is a critical accessibility failure.",
                        "difficulty": "Medium"
                    }
                ],
                "project": {
                    "title": "Complete Professional Portfolio Website — HTML Foundation",
                    "scenario": "Your final capstone. Build the entire skeletal foundation of a professional portfolio.",
                    "objective": "Integrate semantics, SEO, forms, and media.",
                    "requirements": "Create a fully valid HTML5 document. Include DOCTYPE, html (lang='en'), head (title, viewport, description), and body. Inside body: a header (with nav), a main (containing an intro section with a figure/img, and a contact section with a form including email/text/submit), and a footer.",
                    "features": "Complete Page Architecture, Semantics, Form, Media, SEO",
                    "guidance": "Combine everything you've learned. Ensure tags are properly nested.",
                    "expected_behavior": "A flawless, complete structural representation of a modern website.",
                    "evaluation_criteria": "Presence and correct nesting of all specified major architectural blocks.",
                    "starter_code": '''<!-- Build your capstone here -->''',
                    "language": "html",
                    "test_cases": [
                        {"input_data": '''''', "expected_output": '''<!DOCTYPE html><html lang=\"en\"><head><title>Portfolio</title><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><meta name=\"description\" content=\"My Portfolio\"></head><body><header><nav></nav></header><main><section><figure><img src=\"me.jpg\" alt=\"Me\"></figure></section><section><form><input type=\"email\" name=\"email\"><input type=\"text\" name=\"msg\"><input type=\"submit\"></form></section></main><footer></footer></body></html>''', "is_hidden": False, "order_index": 1}
                    ]
                }
            }
        ]
    }
