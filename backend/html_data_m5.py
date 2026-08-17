def get_module_data():
    return {
        "title": "Semantic HTML & Accessibility",
        "description": "Learn to write HTML that means something. Ditch div-soup for semantic tags and build accessible interfaces.",
        "order_index": 5,
        "lessons": [
            {
                "title": "Semantic Architecture and Accessibility Basics",
                "slug": "semantic-html-accessibility",
                "content": "Semantic HTML means using HTML tags that convey the meaning of the content, rather than just how it should look. This is crucial for search engines (SEO) and screen readers (Accessibility).\\n\\n### Semantic Structure Tags\\nInstead of using `<div>` for everything, HTML5 introduced tags that define the architecture of a page:\\n- `<header>`: The introductory content or navigation links at the top of a section/page.\\n- `<nav>`: A block of navigation links.\\n- `<main>`: The dominant content of the page.\\n- `<article>`: A self-contained, independent piece of content (like a blog post).\\n- `<section>`: A thematic grouping of content, typically with a heading.\\n- `<aside>`: Content tangentially related to the content around it (like a sidebar).\\n- `<footer>`: The footer for its nearest section/page.\\n\\n### Accessibility (a11y) Fundamentals\\nWeb accessibility ensures people with disabilities can use your site.\\n- **Alt Text**: Always provide descriptive `alt` attributes on images.\\n- **Heading Hierarchy**: Never skip heading levels (e.g., jumping from `<h1>` to `<h3>`). Screen readers use headings to navigate.\\n- **Keyboard Nav**: Interactive elements (links, buttons, inputs) must be focusable and operable via keyboard.\\n\\n### ARIA Basics\\nARIA (Accessible Rich Internet Applications) attributes help when native HTML isn't enough.\\n- `role`: Defines what an element is (e.g., `role=\"alert\"`).\\n- `aria-label`: Provides an accessible name for an element when there is no visible text.\\n- `aria-hidden=\"true\"`: Hides decorative elements from screen readers.",
                "order_index": 1,
                "examples": [
                    {
                        "title": "Semantic vs Non-Semantic",
                        "explanation": "Comparing a div-heavy structure with a modern, semantic HTML5 structure.",
                        "code": '''<!-- Bad: Non-Semantic Div Soup -->\\n<div class=\"header\">Welcome</div>\\n<div class=\"nav\"><a href=\"/\">Home</a></div>\\n<div class=\"main\">Content</div>\\n<div class=\"footer\">Copyright</div>\\n\\n<!-- Good: Semantic HTML -->\\n<header><h1>Welcome</h1></header>\\n<nav><a href=\"/\">Home</a></nav>\\n<main><p>Content</p></main>\\n<footer><p>Copyright</p></footer>''',
                        "language": "html",
                        "order_index": 1
                    },
                    {
                        "title": "Accessible Button with ARIA",
                        "explanation": "Using aria-label to describe an icon button that has no text.",
                        "code": '''<!-- Screen readers will read 'Close window' instead of 'X' -->\\n<button aria-label=\"Close window\">\\n    <span aria-hidden=\"true\">X</span>\\n</button>''',
                        "language": "html",
                        "order_index": 2
                    }
                ],
                "exercises": [
                    {
                        "title": "Replace Divs with Semantics",
                        "description": "Convert the given `div` layout to use `header`, `main`, and `footer` tags.",
                        "difficulty": "Easy",
                        "starter_code": '''<div id=\"header\">Site Title</div>\\n<div id=\"content\">Main Content</div>\\n<div id=\"footer\">Legal Info</div>''',
                        "language": "html",
                        "order_index": 1,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<header>Site Title</header><main>Main Content</main><footer>Legal Info</footer>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Create a Semantic Article",
                        "description": "Create an `article` element. Inside it, put a `header` containing an `h2` ('Article Title'). Below the header, add a `p` ('Article text.').",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 2,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<article><header><h2>Article Title</h2></header><p>Article text.</p></article>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Fix the Heading Hierarchy",
                        "description": "The current code jumps from h1 to h4, which is bad for accessibility. Fix it so the document outline is strictly sequential (h1 -> h2 -> h3).",
                        "difficulty": "Medium",
                        "starter_code": '''<h1>Main Title</h1>\\n<h4>Sub Section</h4>\\n<h5>Detail</h5>''',
                        "language": "html",
                        "order_index": 3,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<h1>Main Title</h1><h2>Sub Section</h2><h3>Detail</h3>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Accessible Search Button",
                        "description": "Create a `button` containing a visual magnifying glass (text: '?'). Use `aria-label` to set its accessible name to 'Search'. Use `aria-hidden=\"true\"` on the '?' span.",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 4,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<button aria-label=\"Search\"><span aria-hidden=\"true\">?</span></button>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Semantic Navigation Sidebar",
                        "description": "Create an `aside` element containing a `nav` element. The `nav` should contain a link to '#docs' with text 'Documentation'.",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 5,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<aside><nav><a href=\"#docs\">Documentation</a></nav></aside>''', "is_hidden": False, "order_index": 1}
                        ]
                    }
                ],
                "quizzes": [
                    {
                        "question_text": "What is the primary benefit of using semantic HTML elements like <main> and <article>?",
                        "options": ["They automatically style the page to look modern", "They convey meaning and structure to assistive technologies and search engines", "They execute faster in the browser", "They prevent cross-site scripting attacks"],
                        "correct_answer": "They convey meaning and structure to assistive technologies and search engines",
                        "explanation": "Semantic tags describe the 'what' and 'why' of the content, which aids SEO and accessibility tools.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Which tag should wrap the primary, unique content of a webpage?",
                        "options": ["<article>", "<content>", "<main>", "<section>"],
                        "correct_answer": "<main>",
                        "explanation": "<main> represents the dominant content of the <body>. There should only be one visible <main> element per page.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "What is the correct use case for the <aside> element?",
                        "options": ["To hide content from the user", "For content that is tangentially related to the surrounding content (e.g., a sidebar)", "To center text on the page", "To indicate deleted text"],
                        "correct_answer": "For content that is tangentially related to the surrounding content (e.g., a sidebar)",
                        "explanation": "<aside> is often used for sidebars, call-out boxes, or related links that aren't part of the main flow.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Why is skipping heading levels (e.g., h1 followed immediately by h3) considered a bad practice?",
                        "options": ["It causes CSS errors", "It breaks the semantic document outline used by screen reader users to navigate", "Browsers will refuse to render the h3", "It uses more memory"],
                        "correct_answer": "It breaks the semantic document outline used by screen reader users to navigate",
                        "explanation": "Screen readers allow users to jump between headings. A broken hierarchy causes confusion.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "When should you use the aria-label attribute?",
                        "options": ["On every single HTML element", "To provide an accessible name for an interactive element that lacks visible text", "To style a label with CSS", "To translate text to another language"],
                        "correct_answer": "To provide an accessible name for an interactive element that lacks visible text",
                        "explanation": "If a button only has an icon, aria-label tells the screen reader what the button actually does.",
                        "difficulty": "Hard"
                    },
                    {
                        "question_text": "What does aria-hidden=\"true\" do?",
                        "options": ["Hides the element visually using CSS", "Hides the element from assistive technologies like screen readers", "Hides the element from search engines only", "Deletes the element from the DOM"],
                        "correct_answer": "Hides the element from assistive technologies like screen readers",
                        "explanation": "It removes the element from the accessibility tree while leaving it visually intact.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Which element represents a standalone piece of content that could be distributed independently?",
                        "options": ["<section>", "<div>", "<article>", "<main>"],
                        "correct_answer": "<article>",
                        "explanation": "<article> is for self-contained content, like a blog post or news story.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "How should a group of navigation links be semantically enclosed?",
                        "options": ["<div class=\"nav\">", "<menu>", "<nav>", "<links>"],
                        "correct_answer": "<nav>",
                        "explanation": "The <nav> element designates a section containing navigation links.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Which of the following elements is natively focusable by the keyboard?",
                        "options": ["<p>", "<div>", "<button>", "<span>"],
                        "correct_answer": "<button>",
                        "explanation": "Interactive elements like buttons, links (with href), and inputs are naturally in the tab sequence.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "What is a common consequence of relying entirely on <div> and <span> tags?",
                        "options": ["'Div soup', which offers no semantic context to browsers or assistive technologies", "Faster rendering times", "Easier CSS styling", "Automatic accessibility compliance"],
                        "correct_answer": "'Div soup', which offers no semantic context to browsers or assistive technologies",
                        "explanation": "Divs have no semantic meaning. Overusing them harms accessibility and code readability.",
                        "difficulty": "Easy"
                    }
                ],
                "project": {
                    "title": "Accessible News Website Structure",
                    "scenario": "You are refactoring a legacy news homepage to use modern HTML5 semantics.",
                    "objective": "Build a page skeleton using header, nav, main, article, aside, and footer.",
                    "requirements": "Create a `header` containing an h1. A `nav` with two links. A `main` section. Inside `main`, an `article` containing an h2 and a p. Next to the article (still inside main), an `aside` with an h3. Finally, a `footer`.",
                    "features": "HTML5 Semantics, Accessibility Hierarchy",
                    "guidance": "Focus purely on the tag structure and ensuring headings cascade correctly (h1, then h2/h3).",
                    "expected_behavior": "A deeply nested semantic document outline.",
                    "evaluation_criteria": "Correct nesting and presence of all specified HTML5 landmarks.",
                    "starter_code": '''<body>\\n\\n</body>''',
                    "language": "html",
                    "test_cases": [
                        {"input_data": '''''', "expected_output": '''<body><header><h1>News</h1></header><nav><a href=\"#\">Local</a><a href=\"#\">World</a></nav><main><article><h2>Story</h2><p>Content</p></article><aside><h3>Ads</h3></aside></main><footer></footer></body>''', "is_hidden": False, "order_index": 1}
                    ]
                }
            }
        ]
    }
