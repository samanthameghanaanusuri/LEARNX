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
```css
{syntax}
```
**What does this mean?**
{syntax_explanation}

## EXAMPLE 1 — VERY SIMPLE
```css
{example_simple[0]}
```
*Explanation:* {example_simple[1]}

## EXAMPLE 2 — REAL-WORLD
```css
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
        exercises = []
        difficulties = ["Easy", "Easy", "Medium", "Medium", "Hard"]
        for i in range(5):
            exercises.append({
                "title": f"Exercise {i+1}: Applying {concepts[i % len(concepts)]}",
                "description": f"Write CSS rules to style an element based on the concept of {concepts[i % len(concepts)]}. Ensure your code is robust.",
                "difficulty": difficulties[i],
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
                "question_text": f"You are building a responsive layout involving {concept}. Which approach is most robust?",
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
        
        lesson = build_lesson(
            title=f"Mastering {title}",
            slug=f"css-module-{mod_num}",
            what=f"{desc}\n\nAt its core, this module provides fundamental mechanisms such as **{concepts[0]}** and **{concepts[1]}**. Before attempting complex layouts, you must understand how these core CSS rules operate.\n\nBy mastering {', '.join(concepts)}, you gain the power to style, position, and animate elements predictably.",
            why=f"Mastering {title} is essential for creating visually appealing and accessible interfaces.\n\nWithout a strong understanding of CSS cascade and layout, your styles will conflict, break on different devices, and become impossible to maintain.",
            where=f"These properties are used globally across all standard web projects.\n\nWhether styling a simple button or a massive data grid, {concepts[0]} is a foundational requirement.",
            how=f"Implementing this concept involves a logical, step-by-step approach:\n\n1. **Target the Element**: Use a precise selector to find the correct DOM nodes.\n2. **Apply {concepts[0]}**: Write the declaration block with the required properties.\n3. **Manage the Cascade**: Ensure your specificity is appropriate so styles aren't overwritten.\n4. **Test Responsiveness**: Check how the element behaves across various screen sizes.\n\nAlways start simple before adding advanced properties like {concepts[-1]}.",
            syntax=f"/* Example Syntax */\n.selector {{\n  /* Declare {concepts[0]} here */\n  property: value;\n}}",
            syntax_explanation=f"The structure maps styles directly to elements.\n\n- `.selector`: Identifies the target HTML element.\n- `property`: The specific visual characteristic to change.\n- `value`: The setting for that characteristic.",
            example_simple=(f"/* Simple Example */\n.{concepts[0]}-example {{\n  display: block;\n}}", f"This demonstrates the absolute most basic usage of {concepts[0]}. Notice how simple the declaration is."),
            example_real=(f"/* Real World Example */\n.app-dashboard-card {{\n  /* Base styles */\n  display: flex;\n  /* Implementation of {concepts[-1]} */\n  margin-bottom: 1rem;\n}}", f"A realistic snippet using {concepts[-1]} for a modern application component. It's clean, modular, and reusable."),
            common_mistakes=f"- **High Specificity**: Using `#id` selectors or `!important` unnecessarily, making future overrides a nightmare.\n- **Magic Numbers**: Hardcoding pixel values instead of using relative units for {concepts[1]}.\n- **Ignoring the Cascade**: Not understanding why a style was overridden by another file.",
            best_practices=f"- **Keep Specificity Low**: Stick to class selectors (`.my-class`) whenever possible.\n- **Mobile First**: Write your base styles for mobile, then use media queries for larger screens.\n- **Use Variables**: Extract recurring values (like colors or spacing for {concepts[-1]}) into CSS custom properties.",
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
        "title": "CSS & Responsive Design",
        "slug": "css-responsive-design",
        "description": "Comprehensive CSS course from fundamental mechanics to advanced architectural patterns.",
        "lang": "css",
        "modules": modules
    }
