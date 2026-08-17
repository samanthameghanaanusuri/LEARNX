def get_module_data():
    return {
        "title": "HTML5 APIs & Embedded Content",
        "description": "Unlock modern HTML features like responsive images, interactive dialogs, progress bars, and native disclosure widgets.",
        "order_index": 6,
        "lessons": [
            {
                "title": "Modern HTML5 Features and Media",
                "slug": "html5-apis-embedded-content",
                "content": "HTML5 introduced a wealth of native elements that previously required heavy JavaScript.\\n\\n### Interactive Elements\\n- `<details>` and `<summary>`: Creates a native accordion/disclosure widget. The `<summary>` is the clickable heading; everything else inside `<details>` is the hidden content revealed on click.\\n- `<dialog>`: Represents a modal or popup dialog box. (Usually controlled via JS `.showModal()`).\\n\\n### Data and Status\\n- `<progress>`: Represents the completion progress of a task (e.g., a file download).\\n- `<meter>`: Represents a scalar measurement within a known range (e.g., disk usage, voting gauge). Requires `min`, `max`, and `value`.\\n- `<time>`: Represents a specific period in time. The `datetime` attribute provides machine-readable format.\\n\\n### Advanced Media\\n- `<picture>` and `<source>`: Used for art direction and responsive images. You can serve different image files based on screen size or format support (e.g., serving WebP if supported, otherwise falling back to JPEG).\\n- `loading=\"lazy\"`: An attribute for `<img>` and `<iframe>` that defers loading the resource until it reaches a calculated distance from the viewport, saving bandwidth.\\n\\n**Best Practice:** Use `<picture>` when you need a completely different cropped image for mobile vs desktop, and `srcset` on `<img>` when you just want different resolutions of the same image.",
                "order_index": 1,
                "examples": [
                    {
                        "title": "Native Accordion (Details/Summary)",
                        "explanation": "Creating a collapsible section without any JavaScript.",
                        "code": '''<details>\\n    <summary>Click here for more info</summary>\\n    <p>This paragraph is hidden until the user clicks the summary element above. It's great for FAQs!</p>\\n</details>''',
                        "language": "html",
                        "order_index": 1
                    },
                    {
                        "title": "Responsive Picture Element",
                        "explanation": "Serving different images based on viewport width.",
                        "code": '''<picture>\\n    <source media=\"(min-width: 800px)\" srcset=\"large-hero.jpg\">\\n    <source media=\"(min-width: 400px)\" srcset=\"medium-hero.jpg\">\\n    <!-- Fallback for older browsers and mobile -->\\n    <img src=\"small-hero.jpg\" alt=\"Hero banner\" loading=\"lazy\">\\n</picture>''',
                        "language": "html",
                        "order_index": 2
                    }
                ],
                "exercises": [
                    {
                        "title": "Build a Native FAQ Accordion",
                        "description": "Create a `details` element. Inside, place a `summary` with the text 'What is HTML?'. Below the summary, place a `p` tag with 'HyperText Markup Language'.",
                        "difficulty": "Easy",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 1,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<details><summary>What is HTML?</summary><p>HyperText Markup Language</p></details>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Implement a Progress Bar",
                        "description": "Create a `progress` element indicating a task is 50% complete. Set `max=\"100\"` and `value=\"50\"`.",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 2,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<progress max=\"100\" value=\"50\"></progress>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Build a Disk Usage Gauge",
                        "description": "Create a `meter` element to show 80 out of 100 GB used. Set min to 0, max to 100, and value to 80.",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 3,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<meter min=\"0\" max=\"100\" value=\"80\"></meter>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Semantic Date Time",
                        "description": "Wrap the text 'January 1st, 2025' in a `time` element. Use the `datetime` attribute to specify the machine-readable date '2025-01-01'.",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 4,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<time datetime=\"2025-01-01\">January 1st, 2025</time>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Lazy Loading an Image",
                        "description": "Create an `img` tag pointing to 'heavy-image.png' (alt: 'Heavy'). Add the attribute that tells the browser to defer loading until it is near the viewport.",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 5,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<img src=\"heavy-image.png\" alt=\"Heavy\" loading=\"lazy\">''', "is_hidden": False, "order_index": 1}
                        ]
                    }
                ],
                "quizzes": [
                    {
                        "question_text": "Which combination of elements creates a native click-to-expand accordion widget?",
                        "options": ["<expand> and <content>", "<accordion> and <panel>", "<details> and <summary>", "<dialog> and <box>"],
                        "correct_answer": "<details> and <summary>",
                        "explanation": "<details> provides the widget wrapper, and <summary> provides the clickable heading.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "What is the primary difference between <progress> and <meter>?",
                        "options": ["<progress> is for task completion percentage; <meter> is for a known scalar measurement (like disk space)", "<progress> is vertical; <meter> is horizontal", "They are exactly the same", "<meter> requires JavaScript; <progress> does not"],
                        "correct_answer": "<progress> is for task completion percentage; <meter> is for a known scalar measurement (like disk space)",
                        "explanation": "While they look similar, <progress> implies an ongoing task, while <meter> represents a static measurement.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Which attribute on the <time> element provides a machine-readable format for search engines and calendars?",
                        "options": ["date", "time", "format", "datetime"],
                        "correct_answer": "datetime",
                        "explanation": "The datetime attribute allows you to present a human-friendly date while providing a strict ISO format for machines.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "When using the <picture> element, which tag is used to specify the different image resources and media queries?",
                        "options": ["<img>", "<src>", "<source>", "<media>"],
                        "correct_answer": "<source>",
                        "explanation": "The <source> tag is used inside <picture> to define criteria (like screen width) and the corresponding image file.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "What is required inside a <picture> element to ensure the image displays on older browsers that don't support <picture>?",
                        "options": ["A <fallback> tag", "A standard <img> tag at the end", "A <default> attribute", "Nothing, it works natively everywhere"],
                        "correct_answer": "A standard <img> tag at the end",
                        "explanation": "The <img> tag acts as the fallback. If the browser supports <picture>, it overrides the <img> source. If not, it just renders the <img>.",
                        "difficulty": "Hard"
                    },
                    {
                        "question_text": "What does the loading=\"lazy\" attribute do on an image?",
                        "options": ["Applies a blur effect until the image loads", "Delays loading the image until the user scrolls near it, saving bandwidth", "Loads the image in low resolution first", "Prevents the image from loading entirely"],
                        "correct_answer": "Delays loading the image until the user scrolls near it, saving bandwidth",
                        "explanation": "Native lazy loading tells the browser not to fetch off-screen images immediately.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Which element represents a modal popup box natively?",
                        "options": ["<modal>", "<popup>", "<dialog>", "<alert>"],
                        "correct_answer": "<dialog>",
                        "explanation": "<dialog> is the HTML5 standard for creating modal or non-modal popup boxes.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "How can you make a <details> element open by default when the page loads?",
                        "options": ["Add the 'open' attribute", "Set 'display: block' in CSS", "It requires JavaScript", "Add 'expanded=\"true\"'"],
                        "correct_answer": "Add the 'open' attribute",
                        "explanation": "The boolean 'open' attribute on the <details> tag forces it to render in its expanded state.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Which tag allows you to embed another HTML page inside your current page?",
                        "options": ["<object>", "<embed>", "<iframe>", "<frame>"],
                        "correct_answer": "<iframe>",
                        "explanation": "<iframe> is the standard method for embedding third-party pages, like YouTube videos.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "What happens if a browser does not support a specific HTML5 tag (like <mark>)?",
                        "options": ["The page crashes", "The browser throws an alert", "The browser treats it as an inline element (like a <span>) and renders the text anyway", "The text inside is hidden"],
                        "correct_answer": "The browser treats it as an inline element (like a <span>) and renders the text anyway",
                        "explanation": "Browsers are designed to fail gracefully. Unknown tags are parsed into the DOM as generic inline elements.",
                        "difficulty": "Medium"
                    }
                ],
                "project": {
                    "title": "Media-rich Event Page",
                    "scenario": "You are building a promo page for a web development conference.",
                    "objective": "Integrate interactive details, semantic time, and progress meters.",
                    "requirements": "Create a page with a `time` element indicating '2025-10-10'. Add a `progress` element (value 75, max 100) indicating ticket sales. Add an FAQ using `details` and `summary` (Summary: 'Location', text: 'Online').",
                    "features": "Time, Progress, Details/Summary",
                    "guidance": "Combine the elements sequentially. Ensure exact attribute usage for tests.",
                    "expected_behavior": "An interactive event snippet with functioning native widgets.",
                    "evaluation_criteria": "Correct syntax for time, progress, details, and summary.",
                    "starter_code": '''<!-- Build event snippet -->''',
                    "language": "html",
                    "test_cases": [
                        {"input_data": '''''', "expected_output": '''<time datetime=\"2025-10-10\">October 10</time><progress value=\"75\" max=\"100\"></progress><details><summary>Location</summary><p>Online</p></details>''', "is_hidden": False, "order_index": 1}
                    ]
                }
            }
        ]
    }
