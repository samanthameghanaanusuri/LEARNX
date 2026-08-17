import json

def generate_css_module(mod_num, title, topic_description, concepts):
    examples = [
        {
            "title": f"Basic Example: {concepts[0]}",
            "explanation": f"This example demonstrates {concepts[0]} in action, showing how to style standard elements effectively.",
            "code": f"/* Styling for {concepts[0]} */\n.element {{\n  display: block;\n  color: #333;\n  padding: 10px;\n}}",
            "language": "css",
            "order_index": 1
        },
        {
            "title": f"Advanced Example: {concepts[1] if len(concepts) > 1 else concepts[0]}",
            "explanation": f"Understanding {concepts[1] if len(concepts) > 1 else concepts[0]} is crucial for maintainable architecture.",
            "code": f"/* Advanced {concepts[-1]} implementation */\n.container {{\n  display: flex;\n  justify-content: center;\n  align-items: center;\n}}",
            "language": "css",
            "order_index": 2
        }
    ]

    exercises = []
    for i in range(5):
        exercises.append({
            "title": f"Exercise {i+1}: Applying {concepts[i % len(concepts)]}",
            "description": f"Write CSS rules to style an element based on the concept of {concepts[i % len(concepts)]}. Ensure your code is robust.",
            "difficulty": "Medium",
            "starter_code": f"/* Add styles for {concepts[i % len(concepts)]} */\n.target-element {{\n\n}}",
            "language": "css",
            "order_index": i + 1,
            "test_cases": [
                {
                    "input_data": "",
                    "expected_output": "true",
                    "is_hidden": False,
                    "order_index": 1
                }
            ]
        })

    quizzes = []
    for i in range(10):
        concept = concepts[i % len(concepts)]
        quizzes.append({
            "question_text": f"When applying {concept}, what is the primary consideration for responsive design and maintainability?",
            "options": [
                f"Using rigid pixel values to enforce {concept}",
                f"Leveraging flexible units and appropriate specificity for {concept}",
                f"Avoiding {concept} entirely on mobile devices",
                f"Using !important on every declaration involving {concept}"
            ],
            "correct_answer": f"Leveraging flexible units and appropriate specificity for {concept}",
            "explanation": f"Best practices dictate that {concept} should integrate smoothly into the cascade without forcing !important or rigid dimensions.",
            "difficulty": "Medium"
        })

    project = {
        "title": f"Mini Project: {title} Capstone",
        "scenario": f"You are building a production feature requiring mastery of {concepts[0]} and {concepts[-1]}.",
        "objective": f"Implement a complete UI component demonstrating {title}.",
        "requirements": [
            f"Use valid CSS covering {concepts[0]}.",
            f"Ensure {concepts[-1]} is applied correctly.",
            "Pass all automated layout checks."
        ],
        "features": [
            "Responsive layout",
            "Maintainable architecture",
            "Accessibility considerations"
        ],
        "guidance": [
            "Start by sketching the box model.",
            "Apply layout properties before colors.",
            "Validate with developer tools."
        ],
        "hints": [
            f"Don't forget how {concepts[0]} interacts with the cascade."
        ],
        "expected_behavior": "The UI component renders cleanly across different viewports.",
        "evaluation_criteria": "Code clarity, visual accuracy, and proper use of the cascade.",
        "starter_code": f"/* Project: {title} */\nbody {{\n  margin: 0;\n}}",
        "language": "css",
        "test_cases": [
            {
                "input_data": "",
                "expected_output": "true",
                "is_hidden": False,
                "order_index": 1
            }
        ]
    }

    lesson_content = f"""
### WHAT
{topic_description} This covers fundamental mechanics such as {', '.join(concepts)}.

### WHY
Mastering {title} is essential for creating robust, scalable web interfaces that adapt to user preferences and screen sizes.

### HOW
To implement {concepts[0]}, you declare the appropriate CSS properties within a valid selector block.

### WHEN
Use {concepts[-1]} when building modern layouts that require dynamic adaptation rather than fixed constraints.

### COMMON MISTAKES
- Relying too heavily on `!important`.
- Misunderstanding the box model dimensions (padding/border vs content).
- Creating deeply nested, highly specific selectors that are hard to override.

### BEST PRACTICES
- Keep specificity as low as possible.
- Use semantic class names (e.g., BEM methodology).
- Test layouts on both mobile and desktop viewports.
    """

    return {
        "title": title,
        "description": topic_description,
        "order_index": mod_num,
        "lessons": [
            {
                "title": f"Mastering {title}",
                "slug": f"css-module-{mod_num}",
                "content": lesson_content,
                "order_index": 1,
                "examples": examples,
                "exercises": exercises,
                "quizzes": quizzes,
                "project": project
            }
        ]
    }

def get_course_data():
    modules_info = [
        (1, "CSS FUNDAMENTALS", "Introduction to CSS syntax, inclusion methods, and the cascade.", ["selectors", "declarations", "comments", "cascade", "inheritance"]),
        (2, "SELECTORS & SPECIFICITY", "Deep dive into targeting elements and resolving conflicts.", ["class", "ID", "pseudo-classes", "pseudo-elements", "specificity"]),
        (3, "COLORS, UNITS & TYPOGRAPHY", "Visual styling, responsive units, and text rendering.", ["hex/rgb/hsl", "rem/em", "vw/vh", "font-family", "web fonts"]),
        (4, "BOX MODEL & DISPLAY", "Understanding the rectangular boundaries and rendering flow.", ["padding", "margin", "box-sizing", "overflow", "display"]),
        (5, "POSITIONING & STACKING", "Controlling element placement outside normal document flow.", ["relative", "absolute", "fixed", "sticky", "z-index"]),
        (6, "FLEXBOX", "1D layout models for alignment and distribution.", ["flex-direction", "justify-content", "align-items", "flex-wrap", "flex-grow"]),
        (7, "CSS GRID", "2D layout models for complex dashboard designs.", ["columns/rows", "fr unit", "minmax()", "grid-template-areas", "auto-fit"]),
        (8, "RESPONSIVE DESIGN", "Adapting interfaces for all device boundaries.", ["media queries", "breakpoints", "fluid layouts", "mobile-first", "accessibility"]),
        (9, "TRANSITIONS, TRANSFORMS & ANIMATIONS", "Adding motion and interaction feedback.", ["transition", "transform", "keyframes", "hover states", "reduced-motion"]),
        (10, "ADVANCED CSS + CAPSTONE", "Modern architectural patterns and dynamic values.", ["CSS variables", "calc()", "clamp()", "nesting", "performance"])
    ]

    modules = []
    for mod_num, title, desc, concepts in modules_info:
        modules.append(generate_css_module(mod_num, title, desc, concepts))

    return {
        "title": "CSS & Responsive Design",
        "slug": "css-responsive-design",
        "description": "Comprehensive CSS course from fundamental mechanics to advanced architectural patterns.",
        "difficulty": "Intermediate",
        "category": "Web Development",
        "subject": "CSS",
        "modules": modules
    }
