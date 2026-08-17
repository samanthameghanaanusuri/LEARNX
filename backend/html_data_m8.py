def get_module_data():
    return {
        "title": "HTML for Real-World Web Pages",
        "description": "Move beyond isolated tags. Discover how to architect complete, SEO-friendly, responsive-ready webpage structures.",
        "order_index": 8,
        "lessons": [
            {
                "title": "Page Architecture and SEO",
                "slug": "real-world-html-seo",
                "content": "Building a real webpage requires combining elements into a logical, maintainable architecture while catering to search engines.\\n\\n### The Viewport Meta Tag\\nTo ensure your page renders correctly on mobile devices, you must include the viewport meta tag inside `<head>`:\\n`<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">`\\nThis tells the browser to match the screen's width and set initial zoom to 1.\\n\\n### SEO Fundamentals\\nSearch Engine Optimization relies heavily on your HTML structure:\\n- **Title Tag**: The most important SEO element. Should be concise and descriptive.\\n- **Meta Description**: `<meta name=\"description\" content=\"...\">`. Shown as the snippet in Google results. Does not directly boost ranking, but boosts Click-Through Rate (CTR).\\n- **Heading Hierarchy**: Search engines use `<h1>`, `<h2>`, etc., to understand the topic of your page.\\n\\n### Open Graph Basics\\nOpen Graph (OG) meta tags control how your page appears when shared on social media (Facebook, Twitter, LinkedIn).\\n- `<meta property=\"og:title\" content=\"My Article\">`\\n- `<meta property=\"og:image\" content=\"image.jpg\">`\\n\\n### Reusable Patterns\\nA standard landing page usually consists of:\\n1. `<header>` (Logo, Nav)\\n2. `<main>` containing multiple `<section>`s (Hero, Features, Testimonials)\\n3. `<footer>` (Links, Copyright)",
                "order_index": 1,
                "examples": [
                    {
                        "title": "SEO and Social Ready Head",
                        "explanation": "A complete head element prepared for mobile, search engines, and social media sharing.",
                        "code": '''<head>\\n    <meta charset=\"UTF-8\">\\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\\n    <title>Buy the Super Widget 3000</title>\\n    <meta name=\"description\" content=\"The best widget for your everyday needs. Buy now for 50% off.\">\\n    <!-- Open Graph for Social Media -->\\n    <meta property=\"og:title\" content=\"Super Widget 3000\">\\n    <meta property=\"og:image\" content=\"https://site.com/widget.jpg\">\\n</head>''',
                        "language": "html",
                        "order_index": 1
                    },
                    {
                        "title": "Landing Page Architecture",
                        "explanation": "The semantic skeleton of a standard SaaS landing page.",
                        "code": '''<body>\\n    <header>\\n        <nav>...</nav>\\n    </header>\\n    <main>\\n        <section id=\"hero\">\\n            <h1>Revolutionize Your Workflow</h1>\\n        </section>\\n        <section id=\"features\">\\n            <h2>Features</h2>\\n            <!-- Feature articles go here -->\\n        </section>\\n    </main>\\n    <footer>...</footer>\\n</body>''',
                        "language": "html",
                        "order_index": 2
                    }
                ],
                "exercises": [
                    {
                        "title": "Add the Viewport Tag",
                        "description": "Inside the `head`, add the required `meta` tag for responsive design (name='viewport', content='width=device-width, initial-scale=1.0').",
                        "difficulty": "Medium",
                        "starter_code": '''<head></head>''',
                        "language": "html",
                        "order_index": 1,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"></head>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "SEO Description",
                        "description": "Add a `meta` tag to provide a page description (name='description', content='A great site').",
                        "difficulty": "Medium",
                        "starter_code": '''<head></head>''',
                        "language": "html",
                        "order_index": 2,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<head><meta name=\"description\" content=\"A great site\"></head>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Open Graph Image",
                        "description": "Add an Open Graph meta tag to set the sharing image (property='og:image', content='share.png').",
                        "difficulty": "Hard",
                        "starter_code": '''<head></head>''',
                        "language": "html",
                        "order_index": 3,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<head><meta property=\"og:image\" content=\"share.png\"></head>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Hero Section",
                        "description": "Create a `section` with id='hero'. Inside it, place an `h1` ('Welcome') and an `a` link pointing to '/signup' ('Join Now').",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 4,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<section id=\"hero\"><h1>Welcome</h1><a href=\"/signup\">Join Now</a></section>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Combine Head Architecture",
                        "description": "Create a complete `head` containing a `title` ('Shop'), the viewport `meta`, and a description `meta` ('Buy stuff').",
                        "difficulty": "Hard",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 5,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<head><title>Shop</title><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><meta name=\"description\" content=\"Buy stuff\"></head>''', "is_hidden": False, "order_index": 1}
                        ]
                    }
                ],
                "quizzes": [
                    {
                        "question_text": "Which meta tag is absolutely critical for a website to be mobile-responsive?",
                        "options": ["<meta name='mobile'>", "<meta name='viewport' content='width=device-width, initial-scale=1.0'>", "<meta name='responsive' content='true'>", "<meta name='screen' content='phone'>"],
                        "correct_answer": "<meta name='viewport' content='width=device-width, initial-scale=1.0'>",
                        "explanation": "Without the viewport tag, mobile browsers will render the page at desktop width and zoom out.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Where does the text inside the <meta name=\"description\"> tag appear?",
                        "options": ["At the top of the webpage", "In the browser tab", "As the snippet text in search engine results pages", "In a popup alert"],
                        "correct_answer": "As the snippet text in search engine results pages",
                        "explanation": "Search engines often use the description meta tag for the text shown beneath the blue link.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "What are Open Graph (og:) meta tags used for?",
                        "options": ["Opening graphics in the browser", "Controlling how URLs are displayed when shared on social media platforms", "Creating vector graphics", "Improving database queries"],
                        "correct_answer": "Controlling how URLs are displayed when shared on social media platforms",
                        "explanation": "Open Graph tags allow you to define the title, image, and description seen on platforms like Facebook and Twitter/X.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Which HTML element is considered the most heavily weighted by search engines for understanding page topic?",
                        "options": ["<title>", "<meta name=\"keywords\">", "<h1>", "<strong>"],
                        "correct_answer": "<title>",
                        "explanation": "The <title> tag is the strongest single on-page SEO signal.",
                        "difficulty": "Hard"
                    },
                    {
                        "question_text": "Is the <meta name=\"keywords\"> tag useful for modern SEO?",
                        "options": ["Yes, it is the most important tag", "No, major search engines like Google have ignored it for over a decade", "Yes, but only for Bing", "Yes, it determines your ranking directly"],
                        "correct_answer": "No, major search engines like Google have ignored it for over a decade",
                        "explanation": "Due to massive keyword stuffing abuse in the 90s/00s, it is completely ignored by Google.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Which tag defines the small icon shown in the browser tab next to the title?",
                        "options": ["<icon>", "<meta name='icon'>", "<link rel='icon'>", "<image type='favicon'>"],
                        "correct_answer": "<link rel='icon'>",
                        "explanation": "The <link> tag with rel='icon' is used to define the favicon.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "When structuring a landing page, what is the best practice for using the <h1> tag?",
                        "options": ["Use it once per page to define the main topic", "Use it for every section heading to increase SEO", "Hide it using CSS", "Put it inside the footer"],
                        "correct_answer": "Use it once per page to define the main topic",
                        "explanation": "Having a single, clear <h1> establishes a strong, unambiguous document hierarchy.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "What does 'semantic SEO' mean?",
                        "options": ["Buying ads on search engines", "Using correct HTML5 tags (like <article>, <nav>, <h2>) so bots understand the meaning of the content", "Using a lot of bold text", "Writing very long URLs"],
                        "correct_answer": "Using correct HTML5 tags (like <article>, <nav>, <h2>) so bots understand the meaning of the content",
                        "explanation": "Search engines parse HTML. Semantic tags make parsing easier and more accurate.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "In Open Graph, which attribute is used instead of 'name'?",
                        "options": ["id", "class", "property", "type"],
                        "correct_answer": "property",
                        "explanation": "OG tags use <meta property=\"...\"> instead of <meta name=\"...\">.",
                        "difficulty": "Hard"
                    },
                    {
                        "question_text": "Why should you avoid placing large amounts of CSS or JS directly inside the HTML file?",
                        "options": ["It causes errors", "It increases page load time (slowing Time to First Byte) and prevents caching, which hurts SEO", "It is illegal", "It confuses the browser parser"],
                        "correct_answer": "It increases page load time (slowing Time to First Byte) and prevents caching, which hurts SEO",
                        "explanation": "External files can be cached by the browser, reducing load times for subsequent pages.",
                        "difficulty": "Medium"
                    }
                ],
                "project": {
                    "title": "Product Landing Page Architecture",
                    "scenario": "You are building the raw HTML structure for a new tech gadget landing page.",
                    "objective": "Combine SEO head tags with a full semantic body skeleton.",
                    "requirements": "Create a `head` with a `title` ('Gadget X'), viewport meta, and an `og:title` meta. Create a `body` with a `header` (containing `nav`), a `main` section containing two `section`s, and a `footer`.",
                    "features": "SEO Meta, Open Graph, Semantic Landmarks",
                    "guidance": "Structure only. Don't worry about filling it with content, just get the scaffolding correct.",
                    "expected_behavior": "A complete, valid HTML skeleton ready for CSS and real content.",
                    "evaluation_criteria": "Presence of head, meta viewport, meta og:title, body, header, nav, main, sections, and footer.",
                    "starter_code": '''<!DOCTYPE html>\\n<html>\\n\\n</html>''',
                    "language": "html",
                    "test_cases": [
                        {"input_data": '''''', "expected_output": '''<!DOCTYPE html><html><head><title>Gadget X</title><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><meta property=\"og:title\" content=\"Gadget X\"></head><body><header><nav></nav></header><main><section></section><section></section></main><footer></footer></body></html>''', "is_hidden": False, "order_index": 1}
                    ]
                }
            }
        ]
    }
