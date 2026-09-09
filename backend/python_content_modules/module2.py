MODULE_DATA = {
    "title": "Python Basics & Syntax",
    "concept": "PythonBasics",
    "lessons": [
        {
            "title": "Indentation, Comments, & Identifiers",
            "concept": "PythonIndentation",
            "theory": """
<h3>A. What is this?</h3>
<p>In Python, the way your code looks is just as important as what it does. <strong>Indentation</strong> refers to the blank spaces at the beginning of a line. <strong>Comments</strong> are sticky notes you leave in the code for humans to read, which the computer ignores. <strong>Identifiers</strong> are simply the names you invent for your data.</p>

<h3>B. Why do we need it?</h3>
<p>If all code were written on one long line, it would be impossible to read. Indentation visually organizes code into blocks so we know which lines belong together. Comments help us remember why we wrote something months later. Identifiers let us label our data so we can find it easily.</p>

<h3>C. Real-life analogy</h3>
<p>Think of a book. Indentation is like starting a new paragraph. Comments are like handwritten notes in the margins. Identifiers are like name tags on people at a party—without them, you wouldn't know how to address anyone!</p>

<h3>D. How does it work?</h3>
<ul>
    <li><strong>Indentation:</strong> Python uses exactly 4 spaces to group code. If you use 3 spaces or 5 spaces, the computer will get confused and crash.</li>
    <li><strong>Comments:</strong> When the Python interpreter sees a hashtag symbol (<code>#</code>), it completely ignores the rest of that line.</li>
    <li><strong>Identifiers:</strong> When you name something, you can use letters, numbers, and underscores (<code>_</code>), but you cannot start with a number.</li>
</ul>

<h3>E. Syntax</h3>
<pre><code># This is a comment. Python ignores this.
identifier_name = "Some Data"
if True:
    print("This line is indented with 4 spaces.")
</code></pre>

<h3>F. First simple example</h3>
<pre><code># Store the player's score
score = 100
print(score)</code></pre>

<h3>G. Second practical example</h3>
<pre><code>user_age = 25
# Check if user is an adult
if user_age > 18:
    print("Welcome!")
    print("You have full access.")</code></pre>

<h3>H. Code explanation</h3>
<p>Let's look at the second example:</p>
<ul>
    <li><code>user_age</code> is an identifier. It's a clear, readable name holding the number 25.</li>
    <li><code># Check if user is an adult</code> is a comment. It explains human logic, but Python ignores it.</li>
    <li>The two <code>print()</code> statements have 4 spaces in front of them. This tells Python: "These two lines belong inside the <code>if</code> block."</li>
</ul>

<h3>I. Execution flow</h3>
<p>When the computer runs the second example:</p>
<ol>
    <li>Line 1: Python creates <code>user_age</code> and stores 25 in it.</li>
    <li>Line 2: Python sees the <code>#</code> and skips the line entirely.</li>
    <li>Line 3: Python evaluates the condition. Since 25 > 18 is true, it enters the block below it.</li>
    <li>Line 4 & 5: Because they are indented, Python knows to execute them next, printing the messages.</li>
</ol>

<h3>J. Output</h3>
<pre><code>Welcome!
You have full access.</code></pre>

<h3>K. Why this output?</h3>
<p>The code outputs these two lines because the condition (user_age > 18) was true, and the indented block belonging to that condition contains two print statements.</p>

<h3>L. Common mistakes</h3>
<ul>
    <li><strong>Mixing spaces and tabs:</strong> If you use the Tab key for one line and 4 spaces for the next, Python will crash with an <code>IndentationError</code>. Always use 4 spaces!</li>
    <li><strong>Bad names:</strong> Naming a variable <code>1st_player</code> will crash (cannot start with a number). Naming a variable <code>class</code> will crash (it's a reserved keyword Python already uses).</li>
    <li><strong>Forgetting the hash:</strong> Writing <code>This is my comment</code> without a <code>#</code> will cause a <code>SyntaxError</code> because Python will try to execute it as code.</li>
</ul>

<h3>M. Important rules</h3>
<ul>
    <li>Always use exactly 4 spaces for an indentation block.</li>
    <li>Identifiers (names) can only contain letters, numbers, and underscores, and cannot start with a number.</li>
    <li>Python is case-sensitive: <code>Score</code> and <code>score</code> are two completely different names.</li>
</ul>

<h3>N. When should I use it?</h3>
<p>Use comments to explain <em>why</em> you wrote complex code. Use clear, descriptive identifiers (like <code>max_speed</code> instead of <code>x</code>) so anyone reading your code knows what it means immediately.</p>

<h3>O. When should I NOT use it?</h3>
<p>Don't write comments that state the obvious. For example, <code>print(age) # prints the age</code> is a useless comment that clutters your screen.</p>

<h3>P. Code reading</h3>
<p>When you look at a block of code, let your eyes scan the left edge. The spaces tell you the structure. Lines that line up vertically on the left run sequentially. Lines that are indented belong to the line above them that ends in a colon <code>:</code>.</p>

<h3>Q. Logic building</h3>
<p>Problem: Create a variable for a user's first name, and print it with a comment explaining what you did.</p>
<ul>
    <li><strong>What do we know?</strong> We know how to name variables and make comments.</li>
    <li><strong>What do we need?</strong> An identifier, a <code>#</code> comment, and a <code>print()</code>.</li>
    <li><strong>Step-by-step logic:</strong> Start with a comment. On the next line, invent a name like <code>first_name</code>. On the final line, print it.</li>
</ul>

<h3>R. Concept connection</h3>
<p>In Module 1, we learned that Python reads top-to-bottom. Now we see that indentation allows us to group lines together so Python can read blocks of code as a single unit.</p>

<h3>S. Quick recap</h3>
<p>Indentation uses 4 spaces to group code. Identifiers are names you give to your data and must follow strict naming rules. Comments use the <code>#</code> symbol and allow you to leave notes for humans that the computer ignores.</p>
""",
            "examples": [
                {
                    "title": "Code Blocks",
                    "explanation": "Demonstrates correct 4-space indentation under conditional statements.",
                    "code": "if True:\n    print(\"Indented code block\")"
                }
            ],
            "exercises": [],
            "quizzes": []
        },
        {
            "title": "Module 2 Practice & Knowledge Check",
            "concept": "IdentifiersRules",
            "theory": """
<h3>Module 2 Assessment Workspace</h3>
<p>Review the 5 programming exercises in the Practice Lab and test your understanding of indentation, identifiers, and comments with the 10 quiz questions below.</p>
""",
            "examples": [],
            "exercises": [
                {
                    "title": "Fix Indentation",
                    "desc": "Fix the indentation error by adding exactly 4 spaces before the print statement.",
                    "starter": "if True:\nprint(\"Correct\")",
                    "expected": "Correct",
                    "test_cases": [
                        {"input": "", "expected": "Correct\n", "is_hidden": False}
                    ]
                },
                {
                    "title": "Double Indentation Block",
                    "desc": "Fix the block so both print statements have exactly 4 spaces of indentation so they line up perfectly.",
                    "starter": "if True:\n  print(\"One\")\n    print(\"Two\")",
                    "expected": "One\nTwo",
                    "test_cases": [
                        {"input": "", "expected": "One\nTwo\n", "is_hidden": False}
                    ]
                },
                {
                    "title": "Write Comment",
                    "desc": "Turn the first line into a comment by adding a # at the start, so only 'Success' is printed.",
                    "starter": "this is a comment\nprint('Success')",
                    "expected": "Success",
                    "test_cases": [
                        {"input": "", "expected": "Success\n", "is_hidden": False}
                    ]
                },
                {
                    "title": "Define Identifier",
                    "desc": "Create a variable named 'score_limit' (exactly like that) and assign it the value 100. Then print 'score_limit'.",
                    "starter": "# Write code here\n",
                    "expected": "100",
                    "test_cases": [
                        {"input": "", "expected": "100\n", "is_hidden": False}
                    ]
                },
                {
                    "title": "Case Check",
                    "desc": "Create variable 'data' and assign 50. Then print 'data'. Remember Python is case-sensitive.",
                    "starter": "# Write code here\n",
                    "expected": "50",
                    "test_cases": [
                        {"input": "", "expected": "50\n", "is_hidden": False}
                    ]
                }
            ],
            "quizzes": [
                {
                    "question": "What is the standard number of spaces used for indentation in Python blocks?",
                    "options": ["2 spaces", "4 spaces", "8 spaces", "1 space"],
                    "correct": "4 spaces",
                    "explanation": "The official Python style guide (PEP 8) strictly specifies using 4 spaces per indentation level.",
                    "difficulty": "Beginner"
                },
                {
                    "question": "What error occurs if code block indentation is mismatched?",
                    "options": ["TypeError", "ValueError", "IndentationError", "NameError"],
                    "correct": "IndentationError",
                    "explanation": "Python raises an IndentationError when you use inconsistent spacing on the left side of your code.",
                    "difficulty": "Beginner"
                },
                {
                    "question": "Which of the following is a VALID identifier name in Python?",
                    "options": ["2nd_score", "score-total", "score_total", "class"],
                    "correct": "score_total",
                    "explanation": "Identifiers cannot start with numbers (2nd_score), contain hyphens (score-total), or use reserved keywords (class). Underscores are allowed.",
                    "difficulty": "Beginner"
                },
                {
                    "question": "How does Python define the end of a block of indented code?",
                    "options": [
                        "A closing brace }",
                        "A semicolon ;",
                        "When the indentation level goes back out to match the outer level",
                        "A keyword like 'end'"
                    ],
                    "correct": "When the indentation level goes back out to match the outer level",
                    "explanation": "By removing the 4 spaces on the next line (outdenting), you signal to Python that the block is finished.",
                    "difficulty": "Intermediate"
                },
                {
                    "question": "Are the variable names 'userAge' and 'userage' considered the same by Python?",
                    "options": [
                        "Yes",
                        "No, Python is case-sensitive",
                        "Only inside functions",
                        "Only if declared as global"
                    ],
                    "correct": "No, Python is case-sensitive",
                    "explanation": "Python distinguishes between uppercase and lowercase letters. An uppercase A makes it a completely different name.",
                    "difficulty": "Beginner"
                },
                {
                    "question": "What is a 'keyword' in Python?",
                    "options": [
                        "A special variable name you invent",
                        "A reserved word with special meaning to the interpreter",
                        "A comment tag",
                        "An encryption key"
                    ],
                    "correct": "A reserved word with special meaning to the interpreter",
                    "explanation": "Keywords (like if, else, print) are built-in elements of Python grammar and cannot be used as variable names.",
                    "difficulty": "Beginner"
                },
                {
                    "question": "Can you use 'import' as a variable name?",
                    "options": [
                        "Yes, always",
                        "No, it is a reserved keyword",
                        "Only if it is set to an integer",
                        "Only on Windows systems"
                    ],
                    "correct": "No, it is a reserved keyword",
                    "explanation": "Because 'import' is a command built into Python, using it as a variable name will confuse the interpreter and cause a crash.",
                    "difficulty": "Beginner"
                },
                {
                    "question": "What happens if you mix spacebar spaces and Tab key tabs in Python indentation?",
                    "options": [
                        "Python executes normally",
                        "It raises a TabError or IndentationError",
                        "It runs slower",
                        "It automatically corrects it"
                    ],
                    "correct": "It raises a TabError or IndentationError",
                    "explanation": "Mixing tabs and spaces violates Python's strict layout rules and will immediately crash the program.",
                    "difficulty": "Intermediate"
                },
                {
                    "question": "What does a line starting with the '#' symbol do?",
                    "options": [
                        "Defines a large heading",
                        "Instructs the interpreter to ignore the line (it's a comment)",
                        "Prints a message",
                        "Declares an array"
                    ],
                    "correct": "Instructs the interpreter to ignore the line (it's a comment)",
                    "explanation": "Hash symbols define comments, which are notes left for human programmers to read.",
                    "difficulty": "Beginner"
                },
                {
                    "question": "Which of the following is the correct format for multi-line block comments (docstrings)?",
                    "options": [
                        "// line 1\\n// line 2",
                        "\"\"\" line 1\\nline 2 \"\"\"",
                        "/* line 1\\nline 2 */",
                        "# line 1\\n# line 2 without hashes"
                    ],
                    "correct": "\"\"\" line 1\\nline 2 \"\"\"",
                    "explanation": "Triple quotes (either ''' or \"\"\") allow you to write text across multiple lines without needing a # on every single line.",
                    "difficulty": "Intermediate"
                }
            ]
        }
    ]
}
