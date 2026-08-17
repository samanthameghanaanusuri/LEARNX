def get_module_data():
    return {
        "title": "Professional HTML Architecture",
        "description": "Learn professional workflows: maintainability, performance fundamentals, image optimization, and graceful degradation.",
        "order_index": 9,
        "lessons": [
            {
                "title": "Clean Code, Performance, and Best Practices",
                "slug": "professional-html-architecture",
                "content": "Professional HTML isn't just about making things appear on screen; it's about building scalable, performant, and maintainable systems.\\n\\n### Clean Architecture\\n- **Consistent Indentation**: Always use 2 or 4 spaces. It makes nested elements readable.\\n- **Naming Conventions**: Use lowercase for tags and attributes. Use kebab-case for IDs and classes (e.g., `id=\"main-header\"`).\\n- **DRY (Don't Repeat Yourself)**: Abstract repeating structures.\\n\\n### Performance Optimization\\n- **Image Optimization**: Images are often the heaviest part of a page. Compress images before uploading. Use modern formats like WebP.\\n- **Preload and Prefetch**: Use `<link rel=\"preload\">` in the head to tell the browser to download critical resources (like fonts or hero images) immediately.\\n- **Script Loading**: By default, `<script>` blocks HTML parsing. Use `<script defer>` to download scripts in the background and execute them after parsing, improving page load speed.\\n\\n### Progressive Enhancement & Graceful Degradation\\n- **Progressive Enhancement**: Build a basic, functional HTML core that works for everyone (even older browsers or slow networks), then add CSS/JS enhancements for capable browsers.\\n- **Graceful Degradation**: Build for modern browsers but ensure it falls back gracefully (e.g., providing an `<img>` fallback for `<picture>`).\\n\\n### HTML Validation\\nAlways validate your HTML using the W3C Validator. Invalid HTML can cause unpredictable rendering bugs and accessibility failures.",
                "order_index": 1,
                "examples": [
                    {
                        "title": "Performance Optimized Head",
                        "explanation": "Using preloading and deferring scripts for maximum performance.",
                        "code": '''<head>\\n    <meta charset=\"UTF-8\">\\n    <!-- Preload critical font -->\\n    <link rel=\"preload\" href=\"main-font.woff2\" as=\"font\" type=\"font/woff2\" crossorigin>\\n    <!-- Link stylesheet -->\\n    <link rel=\"stylesheet\" href=\"styles.css\">\\n    <!-- Defer JavaScript so it doesn't block parsing -->\\n    <script src=\"app.js\" defer></script>\\n</head>''',
                        "language": "html",
                        "order_index": 1
                    },
                    {
                        "title": "Clean Component Structure",
                        "explanation": "A clean, maintainable structure for a repeated card component.",
                        "code": '''<article class=\"product-card\" id=\"prod-102\">\n    <header>\n        <h3 class=\"product-title\">Super Widget</h3>\n    </header>\n    <figure class=\"product-image-wrapper\">\n        <img src=\"widget.webp\" alt=\"Super Widget side view\" loading=\"lazy\">\n    </figure>\n    <div class=\"product-details\">\n        <p class=\"product-price\">$19.99</p>\n        <button class=\"btn-add-to-cart\">Add to Cart</button>\n    </div>\n</article>''',
                        "language": "html",
                        "order_index": 2
                    }
                ],
                "exercises": [
                    {
                        "title": "Defer JavaScript",
                        "description": "Create a `script` tag pointing to 'main.js'. Add the attribute that ensures it does not block HTML parsing.",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 1,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<script src=\"main.js\" defer></script>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Preload a Resource",
                        "description": "Create a `link` tag to preload 'hero.jpg'. Set `rel` to 'preload', `href` to 'hero.jpg', and `as` to 'image'.",
                        "difficulty": "Hard",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 2,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<link rel=\"preload\" href=\"hero.jpg\" as=\"image\">''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Fix the Indentation",
                        "description": "The following code is flattened. For this exercise's test, simply wrap the inner `p` in a `div`, and wrap the `div` in a `section`.",
                        "difficulty": "Medium",
                        "starter_code": '''<section><div><p>Text</p></div></section>''',
                        "language": "html",
                        "order_index": 3,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<section><div><p>Text</p></div></section>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Apply Kebab-Case",
                        "description": "Create a `div` with an ID using kebab-case for 'Main Header Section'.",
                        "difficulty": "Easy",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 4,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<div id=\"main-header-section\"></div>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Graceful Degradation Image",
                        "description": "Create a `picture` tag. Inside, add a `source` for 'image.webp' (type='image/webp'). Add an `img` fallback for 'image.jpg' (alt='Photo').",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 5,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<picture><source srcset=\"image.webp\" type=\"image/webp\"><img src=\"image.jpg\" alt=\"Photo\"></picture>''', "is_hidden": False, "order_index": 1}
                        ]
                    }
                ],
                "quizzes": [
                    {
                        "question_text": "What happens if you place a <script src='...'> tag in the <head> without the 'defer' or 'async' attribute?",
                        "options": ["It loads faster", "The browser pauses parsing the HTML until the script is downloaded and executed, causing a slow page load", "The script is ignored", "It causes a syntax error"],
                        "correct_answer": "The browser pauses parsing the HTML until the script is downloaded and executed, causing a slow page load",
                        "explanation": "Scripts are render-blocking by default.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "What does the 'defer' attribute do on a script tag?",
                        "options": ["It downloads the script in the background and executes it only after the HTML document has been fully parsed", "It prevents the script from loading", "It executes the script immediately", "It deletes the script"],
                        "correct_answer": "It downloads the script in the background and executes it only after the HTML document has been fully parsed",
                        "explanation": "Defer is the best practice for loading standard scripts, as it guarantees execution order and doesn't block rendering.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "What is <link rel=\"preload\"> used for?",
                        "options": ["To hide content", "To tell the browser to fetch a critical resource immediately, before it even discovers it in the DOM", "To refresh the page", "To load a script after the page loads"],
                        "correct_answer": "To tell the browser to fetch a critical resource immediately, before it even discovers it in the DOM",
                        "explanation": "Preloading is a performance technique to prioritize fetching crucial assets like hero images or web fonts.",
                        "difficulty": "Hard"
                    },
                    {
                        "question_text": "What is Progressive Enhancement?",
                        "options": ["Building the most advanced features first and ignoring older browsers", "Building a resilient base experience using HTML, then layering on CSS and JS for better browsers", "Writing CSS before HTML", "Enhancing images using Photoshop"],
                        "correct_answer": "Building a resilient base experience using HTML, then layering on CSS and JS for better browsers",
                        "explanation": "Progressive enhancement ensures that the core content and functionality are accessible to everyone, regardless of their device's capabilities.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "What is kebab-case?",
                        "options": ["camelCase", "snake_case", "words-separated-by-dashes", "PascalCase"],
                        "correct_answer": "words-separated-by-dashes",
                        "explanation": "Kebab-case (e.g., my-class-name) is the standard convention for HTML classes and IDs.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Why is it important to validate your HTML?",
                        "options": ["To make the code look pretty", "To ensure it compiles to machine code", "To catch structural errors that could cause layout breaks or accessibility issues across different browsers", "To reduce the file size"],
                        "correct_answer": "To catch structural errors that could cause layout breaks or accessibility issues across different browsers",
                        "explanation": "Invalid HTML (like unclosed tags) forces browsers to guess your intent, which can lead to unpredictable bugs.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Which image format is generally recommended for modern web performance due to superior compression?",
                        "options": ["BMP", "GIF", "WebP", "TIFF"],
                        "correct_answer": "WebP",
                        "explanation": "WebP (and newer formats like AVIF) offer significantly better compression than older formats like JPEG or PNG.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "What is the primary cause of 'Div Soup'?",
                        "options": ["Using too many <section> tags", "Relying exclusively on <div> elements for layout instead of using semantic HTML5 tags", "Eating while coding", "Using CSS frameworks"],
                        "correct_answer": "Relying exclusively on <div> elements for layout instead of using semantic HTML5 tags",
                        "explanation": "Div soup makes the DOM hard to read and strips it of accessibility and semantic meaning.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "How can you ensure a feature 'degrades gracefully'?",
                        "options": ["By providing a fallback mechanism (like an <img> tag inside a <picture> element) if the browser doesn't support the new feature", "By showing an error message to the user", "By forcing the user to update their browser", "By writing a lot of JavaScript"],
                        "correct_answer": "By providing a fallback mechanism (like an <img> tag inside a <picture> element) if the browser doesn't support the new feature",
                        "explanation": "Graceful degradation ensures that if a modern feature fails, the user still gets a usable experience.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Which attribute on an <img> tag is best for performance if the image is far down the page?",
                        "options": ["defer", "async", "loading=\"lazy\"", "wait=\"true\""],
                        "correct_answer": "loading=\"lazy\"",
                        "explanation": "Lazy loading prevents the browser from downloading the image until the user scrolls near it.",
                        "difficulty": "Easy"
                    }
                ],
                "project": {
                    "title": "Professional Blog Architecture",
                    "scenario": "Set up a highly optimized blog post template.",
                    "objective": "Combine semantic architecture, preloading, and deferred scripts.",
                    "requirements": "Create a `head` with a `preload` link for 'main.css' (as='style'), and a deferred `script` 'app.js'. In the `body`, create an `article`. Inside `article`, a `header` (with h1) and a `section` for content.",
                    "features": "Preload, Defer, Semantic Article",
                    "guidance": "Put everything together using exact tag names and attributes.",
                    "expected_behavior": "An optimized document ready for content.",
                    "evaluation_criteria": "Correct link preload syntax, script defer syntax, and article structure.",
                    "starter_code": '''<!DOCTYPE html>\\n<html>\\n\\n</html>''',
                    "language": "html",
                    "test_cases": [
                        {"input_data": '''''', "expected_output": '''<!DOCTYPE html><html><head><link rel=\"preload\" href=\"main.css\" as=\"style\"><script src=\"app.js\" defer></script></head><body><article><header><h1>Blog</h1></header><section></section></article></body></html>''', "is_hidden": False, "order_index": 1}
                    ]
                }
            }
        ]
    }
