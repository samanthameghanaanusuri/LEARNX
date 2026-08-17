import json

def generate_js_module(mod_num, title, topic_description, concepts):
    examples = [
        {
            "title": f"Syntax Demo: {concepts[0]}",
            "explanation": f"This example demonstrates {concepts[0]}, a foundational concept in JavaScript programming.",
            "code": f"// Demonstrating {concepts[0]}\nconst exampleValue = 'Hello World';\nconsole.log(exampleValue);",
            "language": "javascript",
            "order_index": 1
        },
        {
            "title": f"Practical Application: {concepts[1] if len(concepts) > 1 else concepts[0]}",
            "explanation": f"Applying {concepts[1] if len(concepts) > 1 else concepts[0]} in a real-world scenario.",
            "code": f"// Practical use of {concepts[-1]}\nfunction process(data) {{\n  return data ? data.toUpperCase() : null;\n}}\nconsole.log(process('test'));",
            "language": "javascript",
            "order_index": 2
        }
    ]

    exercises = []
    for i in range(5):
        exercises.append({
            "title": f"Exercise {i+1}: Implementing {concepts[i % len(concepts)]}",
            "description": f"Write a JavaScript function that utilizes {concepts[i % len(concepts)]} to solve the problem.",
            "difficulty": "Medium",
            "starter_code": f"// Implement {concepts[i % len(concepts)]}\nfunction solution() {{\n  // Your code here\n}}\n",
            "language": "javascript",
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
            "question_text": f"Regarding {concept} in JavaScript, which statement best describes its behavioral characteristics?",
            "options": [
                f"It operates identically to statically typed languages without any coercion.",
                f"It leverages JavaScript's dynamic nature, requiring careful management of scope or type.",
                f"It is entirely deprecated in ES6 and should never be used.",
                f"It blocks the main execution thread indefinitely."
            ],
            "correct_answer": f"It leverages JavaScript's dynamic nature, requiring careful management of scope or type.",
            "explanation": f"In JavaScript, concepts like {concept} must be understood in the context of dynamic typing, event loops, and lexical scoping.",
            "difficulty": "Medium"
        })

    project = {
        "title": f"Mini Project: {title} Implementation",
        "scenario": f"You are tasked with building a dynamic web feature utilizing {concepts[0]}.",
        "objective": f"Create a fully functional script covering {title}.",
        "requirements": [
            f"Implement robust logic for {concepts[0]}.",
            f"Handle edge cases related to {concepts[-1]}.",
            "Ensure the code is free of syntax and runtime errors."
        ],
        "features": [
            "Data validation",
            "Console output/DOM updates",
            "Error handling"
        ],
        "guidance": [
            "Plan your variable scope before writing logic.",
            "Use console.log to debug intermediate states.",
            "Refactor repetitive logic into functions."
        ],
        "hints": [
            f"Remember how {concepts[0]} interacts with the JavaScript runtime environment."
        ],
        "expected_behavior": "The script executes cleanly, producing the correct output without throwing uncaught exceptions.",
        "evaluation_criteria": "Algorithmic correctness, code cleanliness, and proper API usage.",
        "starter_code": f"// Mini Project: {title}\nfunction initialize() {{\n  \n}}\ninitialize();",
        "language": "javascript",
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
{topic_description} This module covers key JavaScript paradigms such as {', '.join(concepts)}.

### WHY
Understanding {title} is critical for building interactive, data-driven applications on the client and server.

### HOW
You utilize {concepts[0]} by declaring the necessary statements in your `.js` files or `<script>` tags, keeping scope and execution context in mind.

### WHEN
Apply {concepts[-1]} when you need to manipulate state, respond to user events, or process asynchronous data.

### COMMON MISTAKES
- Confusing `null` and `undefined`.
- Misunderstanding variable hoisting (`var` vs `let`/`const`).
- Losing the `this` context in nested callbacks or event listeners.
- Failing to catch rejected Promises in asynchronous code.

### BEST PRACTICES
- Always use `const` by default, and `let` only when reassignment is necessary.
- Prefer strict equality (`===`) over loose equality (`==`).
- Handle errors gracefully using `try/catch` or `.catch()`.
- Keep functions small and focused on a single responsibility.
    """

    return {
        "title": title,
        "description": topic_description,
        "order_index": mod_num,
        "lessons": [
            {
                "title": f"Mastering {title}",
                "slug": f"js-module-{mod_num}",
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
        (1, "JAVASCRIPT FUNDAMENTALS", "Introduction to the JS engine, syntax, and basic expressions.", ["statements", "comments", "variables", "console", "expressions"]),
        (2, "VARIABLES & DATA TYPES", "Understanding memory allocation and dynamic typing.", ["let/const/var", "string/number/boolean", "null/undefined", "type conversion", "coercion"]),
        (3, "OPERATORS, CONDITIONS & LOOPS", "Controlling the flow of execution logically.", ["logical operators", "ternary", "if/else", "for/while", "break/continue"]),
        (4, "FUNCTIONS & SCOPE", "Creating reusable blocks of code and managing lexical environments.", ["arrow functions", "parameters", "lexical scope", "closures", "rest parameters"]),
        (5, "ARRAYS & OBJECTS", "Structuring and mutating complex data collections.", ["mutation", "map/filter/reduce", "properties", "destructuring", "spread syntax"]),
        (6, "DOM MANIPULATION", "Interacting with the browser's Document Object Model.", ["querySelector", "createElement", "classList", "textContent", "DOM traversal"]),
        (7, "EVENTS & FORMS", "Responding to user interactions and capturing input.", ["event listeners", "event object", "preventDefault", "event bubbling", "delegation"]),
        (8, "ASYNCHRONOUS JAVASCRIPT", "Handling non-blocking operations like network requests.", ["callbacks", "promises", "async/await", "fetch", "try/catch"]),
        (9, "MODERN & ADVANCED JAVASCRIPT", "ES6+ features and advanced patterns.", ["modules", "optional chaining", "nullish coalescing", "classes", "localStorage"]),
        (10, "REAL-WORLD JAVASCRIPT CAPSTONE", "Building complete, maintainable client-side architectures.", ["state management", "API integration", "error handling", "debugging", "performance"])
    ]

    modules = []
    for mod_num, title, desc, concepts in modules_info:
        modules.append(generate_js_module(mod_num, title, desc, concepts))

    return {
        "title": "JavaScript Programming",
        "slug": "javascript-programming",
        "description": "Comprehensive JavaScript course from core programming concepts to advanced asynchronous application architectures.",
        "difficulty": "Advanced",
        "category": "Web Development",
        "subject": "JavaScript",
        "modules": modules
    }
