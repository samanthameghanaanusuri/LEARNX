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
```javascript
{syntax}
```
**What does this mean?**
{syntax_explanation}

## EXAMPLE 1 — VERY SIMPLE
```javascript
{example_simple[0]}
```
*Explanation:* {example_simple[1]}

## EXAMPLE 2 — REAL-WORLD
```javascript
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
        exercises = []
        difficulties = ["Easy", "Easy", "Medium", "Medium", "Hard"]
        for i in range(5):
            exercises.append({
                "title": f"Exercise {i+1}: Implementing {concepts[i % len(concepts)]}",
                "description": f"Write a JavaScript function that utilizes {concepts[i % len(concepts)]} to solve the problem.",
                "difficulty": difficulties[i],
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
        
        lesson = build_lesson(
            title=f"Mastering {title}",
            slug=f"js-module-{mod_num}",
            what=f"{desc}\n\nAt its core, this module provides fundamental mechanisms such as **{concepts[0]}** and **{concepts[1]}**. Before jumping into frameworks like React or Vue, you must understand how native JavaScript executes.\n\nBy mastering {', '.join(concepts)}, you gain the ability to manipulate data and the DOM dynamically.",
            why=f"Mastering {title} is critical for building interactive, data-driven applications on both the client and server.\n\nWithout a deep understanding of these concepts, you will struggle to debug logic errors or handle asynchronous operations effectively.",
            where=f"These patterns are used universally across all JavaScript environments.\n\nWhether writing a simple UI toggle or a complex backend service, {concepts[0]} will be essential.",
            how=f"Implementing this concept involves a logical, step-by-step execution flow:\n\n1. **Define the Intent**: Decide what data you are manipulating or what event you are responding to.\n2. **Declare the Structure**: Write the initial statement for {concepts[0]}.\n3. **Execute Logic**: Perform operations or mutations.\n4. **Handle Output**: Log the result or update the DOM.\n\nAlways ensure your variables are properly scoped before running logic.",
            syntax=f"// Example Syntax\nconst initialValue = 'setup';\n// Apply {concepts[0]} logic here",
            syntax_explanation=f"A basic declaration illustrating standard execution flow.\n\n- `const`: Declares a block-scoped, immutable binding.\n- `=`: Assigns the value to the identifier.",
            example_simple=(f"// Simple Example\nconsole.log('Testing {concepts[0]}');", f"This demonstrates a basic usage of {concepts[0]}. Using console.log is the best way to verify your logic."),
            example_real=(f"// Real World Example\nasync function processData() {{\n  try {{\n    // Implementation of {concepts[-1]}\n    console.log('Success');\n  }} catch (e) {{\n    console.error(e);\n  }}\n}}", f"A realistic snippet handling {concepts[-1]}. Notice the use of error handling, which is crucial for production code."),
            common_mistakes=f"- **Global State Mutation**: Accidentally modifying variables outside of their intended scope.\n- **Type Coercion Issues**: Using `==` instead of `===` leading to unexpected bugs.\n- **Uncaught Errors**: Failing to handle edge cases when using {concepts[1]}.",
            best_practices=f"- **Always Use Strict Mode**: This prevents many silent errors.\n- **Prefer `const`**: Default to `const`. Only use `let` when you know the variable will be reassigned. Avoid `var` entirely.\n- **Pure Functions**: Try to write functions that don't mutate external state.",
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
        "title": "JavaScript Programming",
        "slug": "javascript-programming",
        "description": "Comprehensive JavaScript course from core programming concepts to advanced asynchronous application architectures.",
        "lang": "javascript",
        "modules": modules
    }
