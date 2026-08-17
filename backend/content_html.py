import json

def build_lesson(title, slug, what, why, where, how, syntax, syntax_explanation, example_simple, example_real, common_mistakes, best_practices, exercises, quizzes, project=None):
    content = f"""
## Why are you learning this?
{why}

## WHAT IS IT?
{what}

## WHERE IS IT USED?
{where}

## HOW DOES IT WORK?
{how}

## SYNTAX
```html
{syntax}
```
**What does this mean?**
{syntax_explanation}

## EXAMPLE 1 — VERY SIMPLE
```html
{example_simple[0]}
```
*Explanation:* {example_simple[1]}

## EXAMPLE 2 — REAL-WORLD
```html
{example_real[0]}
```
*Explanation:* {example_real[1]}

## COMMON MISTAKES
{common_mistakes}

## BEST PRACTICES
{best_practices}

## TRY IT YOURSELF
Now it's your turn. Head over to the practice lab and try the exercises!
    """
    
    return {
        "title": title,
        "slug": slug,
        "content": content,
        "exercises": exercises,
        "quizzes": quizzes,
        "project": project
    }

def get_course_data():
    modules_info = [
        (1, "FOUNDATIONS", "Introduction to HTML, the DOCTYPE, and document structure.", ["html", "head", "body", "title", "DOCTYPE"]),
        (2, "TEXT FORMATTING", "How to structure readable content.", ["headings", "paragraphs", "emphasis", "strong", "line breaks"]),
        (3, "LINKS & MEDIA", "Connecting pages and embedding visual content.", ["anchor", "href", "images", "src", "alt"]),
        (4, "CONTENT STRUCTURE", "Organizing data logically.", ["ordered lists", "unordered lists", "tables", "rows", "cells"]),
        (5, "SEMANTIC HTML", "Giving meaning to your web architecture.", ["header", "nav", "main", "footer", "article"]),
        (6, "FORMS & INPUTS", "Collecting user data interactively.", ["form", "input", "label", "button", "required"]),
        (7, "ACCESSIBILITY", "Ensuring your site is usable by everyone.", ["alt text", "keyboard navigation", "ARIA basics", "contrast", "labels"]),
        (8, "ADVANCED HTML", "Metadata, SEO, and responsive setup.", ["meta tags", "viewport", "SEO fundamentals", "open graph", "favicons"]),
        (9, "PAGE ARCHITECTURE", "Combining everything into a real wireframe.", ["sections", "asides", "layout planning", "nested elements", "document outline"]),
        (10, "CAPSTONE INTEGRATION", "Building a complete multi-page semantic website.", ["full site structure", "form submission UI", "media integration", "clean code", "deployment prep"])
    ]

    modules = []
    
    for mod_num, title, desc, concepts in modules_info:
        exercises = []
        difficulties = ["Easy", "Easy", "Medium", "Medium", "Hard"]
        for i in range(5):
            exercises.append({
                "title": f"Exercise {i+1}: Mastering {concepts[i % len(concepts)]}",
                "description": f"Use {concepts[i % len(concepts)]} correctly in an HTML snippet.",
                "difficulty": difficulties[i],
                "starter_code": f"<!-- Implement {concepts[i % len(concepts)]} here -->\n<body>\n  \n</body>",
                "language": "html",
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
                "question_text": f"Why is {concept} crucial for modern web development, particularly regarding accessibility and parsing?",
                "options": [
                    f"It makes the website load significantly faster by bypassing rendering engines.",
                    f"It provides semantic meaning or crucial structure that browsers and screen readers rely on.",
                    f"It is only used for styling purposes and has no structural impact.",
                    f"It replaces the need for JavaScript entirely."
                ],
                "correct_answer": f"It provides semantic meaning or crucial structure that browsers and screen readers rely on.",
                "explanation": f"In HTML, elements like {concept} are fundamental to the Document Object Model, providing meaning (semantics) rather than just visual appearance.",
                "difficulty": "Medium"
            })

        project = {
            "title": f"Mini Project: {title} Capstone",
            "scenario": f"You are building a web page section that strictly requires the use of {concepts[0]} and {concepts[-1]}.",
            "objective": f"Construct a semantically valid HTML fragment demonstrating {title}.",
            "requirements": [
                f"Implement {concepts[0]} properly.",
                f"Ensure {concepts[-1]} is used according to web standards.",
                "Pass the automated HTML validation checks."
            ],
            "features": [
                "Semantic structure",
                "Clean indentation",
                "Accessibility compliance"
            ],
            "guidance": [
                "Map out the structure mentally before typing tags.",
                "Use standard lowercase tag names.",
                "Always close your tags properly."
            ],
            "hints": [
                f"Review how {concepts[0]} fits into the overall document tree."
            ],
            "expected_behavior": "The browser renders the elements exactly as intended without structural quirks.",
            "evaluation_criteria": "Tag correctness, nesting validity, and semantic appropriateness.",
            "starter_code": f"<!DOCTYPE html>\n<html>\n<head>\n  <title>{title} Project</title>\n</head>\n<body>\n  <!-- Start here -->\n</body>\n</html>",
            "language": "html",
            "test_cases": [
                {
                    "input_data": "",
                    "expected_output": "true",
                    "is_hidden": False,
                    "order_index": 1
                }
            ]
        }
        
        lesson = build_lesson(
            title=f"Mastering {title}",
            slug=f"html-module-{mod_num}",
            what=f"{desc}\n\nAt its core, this module provides fundamental mechanisms such as **{concepts[0]}** and **{concepts[1]}**. Before learning any complex frameworks, you must understand how these native elements operate under the hood.\n\nBy mastering {', '.join(concepts)}, you are building the sturdy foundation required for all future development.",
            why=f"Mastering {title} is essential because HTML is the structural skeleton of every single website on the internet.\n\nWithout a firm grasp of these concepts, your code will be fragile, inaccessible to screen readers, and difficult for search engines to parse.",
            where=f"These features are used in every single `.html` file across the web. \n\nWhether you are building a massive enterprise application or a simple blog, {concepts[0]} will be present.",
            how=f"Implementing this concept involves a logical, step-by-step process:\n\n1. **Identify the Goal**: Determine exactly where {concepts[0]} is needed in your layout.\n2. **Setup the Structure**: Open the appropriate tags accurately.\n3. **Inject Content**: Place your specific data or text inside.\n4. **Verify Behavior**: Check the browser to ensure the DOM tree rendered as expected.\n\nFor example, when applying {concepts[-1]}, you always start by defining the parent container.",
            syntax=f"<!-- Example Syntax -->\n<{concepts[0]}>\n  <!-- Content goes here -->\n</{concepts[0]}>",
            syntax_explanation=f"Tags enclose content to give it meaning. \n\n- `<{concepts[0]}>`: The opening tag.\n- `</{concepts[0]}>`: The closing tag (note the forward slash).",
            example_simple=(f"<!-- Simple Example -->\n<{concepts[0]}>Hello Web</{concepts[0]}>", f"This demonstrates the absolute most basic usage of {concepts[0]}. Notice how the tag strictly wraps the content."),
            example_real=(f"<!-- Real World Example -->\n<{concepts[-1]} class=\"main-container\">\n  <{concepts[0]}>Real Application Data</{concepts[0]}>\n</{concepts[-1]}>", f"A realistic snippet using {concepts[-1]} within a modern application. Here, we add a `class` attribute for styling hooks."),
            common_mistakes=f"- **Unclosed Tags**: Forgetting to close a tag, which breaks the entire page layout.\n- **Invalid Nesting**: Placing block-level elements inside inline elements.\n- **Missing Attributes**: Forgetting crucial accessibility attributes when using {concepts[1]}.",
            best_practices=f"- **Semantic Choice**: Always use the most descriptive tag possible (e.g., `<nav>` instead of a generic `<div>`).\n- **Indentation**: Format your HTML with clean, consistent indentation so parent-child relationships are obvious visually.\n- **Validation**: Frequently run your code through an HTML validator.",
            exercises=exercises,
            quizzes=quizzes,
            project=project
        )

        modules.append({
            "title": title,
            "description": desc,
            "lessons": [lesson]
        })

    return {
        "title": "HTML & Web Development",
        "slug": "html-web-development",
        "description": "A pedagogical journey from absolute beginner to advanced semantic HTML architecture.",
        "lang": "html",
        "modules": modules
    }
