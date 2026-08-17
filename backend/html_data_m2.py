def get_module_data():
    return {
        "title": "Links, Images & Media",
        "description": "Learn how to connect the web and embed multimedia. Cover anchor tags, images, audio, video, and iframes.",
        "order_index": 2,
        "lessons": [
            {
                "title": "Mastering Links and Multimedia",
                "slug": "links-images-media",
                "content": "The Web is built on the concept of hyperlinks, which connect pages together. Additionally, modern HTML pages are rich with images and media.\\n\\n### Links (`<a>`)\\nThe `<a>` (anchor) tag defines a hyperlink. Its most important attribute is `href` (Hypertext Reference), which indicates the link's destination.\\n- **Absolute URLs**: Point to another website (e.g., `https://google.com`).\\n- **Relative URLs**: Point to a file within a website (e.g., `/about.html`).\\n- **Target attribute**: `target=\"_blank\"` opens the link in a new tab.\\n\\n### Images (`<img>`)\\nThe `<img>` tag embeds an image. It is an empty element (no closing tag). Crucial attributes:\\n- `src`: Specifies the path to the image.\\n- `alt`: Provides alternative text for screen readers or if the image fails to load. This is vital for accessibility and SEO.\\n\\n### Figure and Figcaption\\nTo semantically group an image with a caption, use `<figure>` and `<figcaption>`.\\n\\n### Audio, Video, and Iframes\\n- `<audio>` and `<video>` tags embed sound and moving pictures. Attributes like `controls`, `autoplay`, and `loop` dictate behavior. The `<source>` tag provides the media file.\\n- `<iframe>` embeds another HTML page into the current page, commonly used for YouTube videos or Google Maps.\\n\\n**Best Practice:** Always provide `alt` text for images. For media, avoid autoplaying video with sound, as it harms user experience.",
                "order_index": 1,
                "examples": [
                    {
                        "title": "Creating Hyperlinks",
                        "explanation": "Different types of links: absolute, relative, email (mailto), and opening in a new tab.",
                        "code": '''<a href=\"https://example.com\">Visit Example (Absolute)</a>\\n<br>\\n<a href=\"/contact.html\">Contact Us (Relative)</a>\\n<br>\\n<a href=\"https://wikipedia.org\" target=\"_blank\">Wikipedia in new tab</a>\\n<br>\\n<a href=\"mailto:test@example.com\">Send an Email</a>''',
                        "language": "html",
                        "order_index": 1
                    },
                    {
                        "title": "Embedding Media",
                        "explanation": "Embedding images with captions, and basic audio/video controls.",
                        "code": '''<figure>\\n    <img src=\"https://via.placeholder.com/150\" alt=\"Placeholder grey box\">\\n    <figcaption>Fig. 1 - A generic placeholder</figcaption>\\n</figure>\\n\\n<video width=\"320\" height=\"240\" controls>\\n    <source src=\"movie.mp4\" type=\"video/mp4\">\\n    Your browser does not support the video tag.\\n</video>''',
                        "language": "html",
                        "order_index": 2
                    }
                ],
                "exercises": [
                    {
                        "title": "Create a Navigation Menu",
                        "description": "Create a `nav` element containing three links: 'Home' (linking to `/`), 'About' (linking to `/about`), and 'Contact' (linking to `/contact`).",
                        "difficulty": "Easy",
                        "starter_code": '''<!-- Create navigation here -->''',
                        "language": "html",
                        "order_index": 1,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<nav><a href=\"/\">Home</a><a href=\"/about\">About</a><a href=\"/contact\">Contact</a></nav>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Add a Profile Image",
                        "description": "Add an `img` tag pointing to `profile.jpg`. Give it an `alt` text of 'My Profile Picture' and set the `width` to '200'.",
                        "difficulty": "Easy",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 2,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<img src=\"profile.jpg\" alt=\"My Profile Picture\" width=\"200\">''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Semantic Image with Caption",
                        "description": "Wrap an image (src: 'sunset.png', alt: 'Beautiful sunset') and a caption ('A beautiful sunset over the ocean') using the `figure` and `figcaption` tags.",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 3,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<figure><img src=\"sunset.png\" alt=\"Beautiful sunset\"><figcaption>A beautiful sunset over the ocean</figcaption></figure>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Embed an Audio Player",
                        "description": "Create an `audio` player that displays controls. Use a `source` tag pointing to 'podcast.mp3' with type 'audio/mpeg'.",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 4,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<audio controls><source src=\"podcast.mp3\" type=\"audio/mpeg\"></audio>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Create Contact Links",
                        "description": "Create two links: one that emails 'support@site.com' (with text 'Email Support'), and one that calls the phone number '555-1234' (with text 'Call Us').",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 5,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<a href=\"mailto:support@site.com\">Email Support</a><a href=\"tel:555-1234\">Call Us</a>''', "is_hidden": False, "order_index": 1}
                        ]
                    }
                ],
                "quizzes": [
                    {
                        "question_text": "Which attribute of the <a> tag specifies the destination URL?",
                        "options": ["src", "link", "href", "url"],
                        "correct_answer": "href",
                        "explanation": "The href (Hypertext Reference) attribute contains the URL that the link points to.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "How do you make a link open in a new browser tab or window?",
                        "options": ["target=\"_blank\"", "new=\"tab\"", "window=\"_new\"", "open=\"blank\""],
                        "correct_answer": "target=\"_blank\"",
                        "explanation": "The target attribute with the value '_blank' instructs the browser to open the linked document in a new tab/window.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "What is the primary purpose of the 'alt' attribute on an <img> tag?",
                        "options": ["To provide a tooltip when hovering over the image", "To provide alternative text for screen readers and when the image fails to load", "To change the size of the image", "To make the image load faster"],
                        "correct_answer": "To provide alternative text for screen readers and when the image fails to load",
                        "explanation": "The alt attribute is critical for web accessibility, allowing visually impaired users to understand image content.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Which tag pairs are used to semantically group an image with its caption?",
                        "options": ["<div> and <span>", "<image> and <text>", "<figure> and <figcaption>", "<group> and <caption>"],
                        "correct_answer": "<figure> and <figcaption>",
                        "explanation": "<figure> groups the media, and <figcaption> provides the semantic caption for that media.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "What protocol is used in an href attribute to create a link that opens the user's email client?",
                        "options": ["email:", "mail:", "mailto:", "send:"],
                        "correct_answer": "mailto:",
                        "explanation": "The 'mailto:' protocol triggers the default email client with the specified email address.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Which element is used to embed another HTML document within the current one?",
                        "options": ["<embed>", "<object>", "<iframe>", "<document>"],
                        "correct_answer": "<iframe>",
                        "explanation": "<iframe> (Inline Frame) is specifically designed to embed a nested browsing context.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "To allow users to play, pause, and adjust volume on an <audio> or <video> element, which attribute must be present?",
                        "options": ["play", "media", "controls", "interactive"],
                        "correct_answer": "controls",
                        "explanation": "The 'controls' attribute tells the browser to render the default media playback controls.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "What does a relative URL point to?",
                        "options": ["A file located on a completely different website domain", "A file relative to the current document's location on the same website", "An email address", "A secure HTTPS endpoint"],
                        "correct_answer": "A file relative to the current document's location on the same website",
                        "explanation": "Relative URLs do not specify a domain; they trace a path from the current page's URL.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Which tag should be placed inside <audio> or <video> to specify the media files?",
                        "options": ["<src>", "<file>", "<media>", "<source>"],
                        "correct_answer": "<source>",
                        "explanation": "The <source> tag is used to specify multiple alternative media resources for media elements.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Is the <img> tag a block-level or inline element by default?",
                        "options": ["Block-level", "Inline", "Inline-block", "Hidden"],
                        "correct_answer": "Inline",
                        "explanation": "Images are inline elements by default, meaning they sit side-by-side with text and other inline elements.",
                        "difficulty": "Hard"
                    }
                ],
                "project": {
                    "title": "Personal Portfolio Landing Page",
                    "scenario": "You are creating the media and navigation section for your portfolio.",
                    "objective": "Combine navigation links, an accessible profile image, and a media embed.",
                    "requirements": "Create a page with a `<nav>` linking to '#home', '#projects', '#contact'. Add a `<figure>` containing a profile `<img>` (with alt text) and a `<figcaption>`. Finally, embed a welcome `<audio>` track with controls.",
                    "features": "Navigation, Semantic Image, Audio Embed",
                    "guidance": "Use anchor tags inside nav. Use figure/figcaption for the image. Ensure audio has the controls attribute.",
                    "expected_behavior": "A page with functional in-page links, a captioned image, and an audio player.",
                    "evaluation_criteria": "Presence of nav, a, figure, img, figcaption, and audio elements with proper attributes.",
                    "starter_code": '''<!-- Build portfolio landing here -->''',
                    "language": "html",
                    "test_cases": [
                        {"input_data": '''''', "expected_output": '''<nav><a href=\"#home\">Home</a><a href=\"#projects\">Projects</a><a href=\"#contact\">Contact</a></nav><figure><img src=\"me.jpg\" alt=\"My Profile\"><figcaption>Developer</figcaption></figure><audio controls><source src=\"welcome.mp3\"></audio>''', "is_hidden": False, "order_index": 1}
                    ]
                }
            }
        ]
    }
