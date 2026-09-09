MODULE_DATA = {
    "title": "Introduction to Programming & Python",
    "concept": "IntroProgramming",
    "lessons": [
        {
            "title": "Introduction to Computers and Python",
            "concept": "ProgrammingBasics",
            "theory": """
<h3>A. What is this?</h3>
<p>Programming is the process of writing down a set of instructions for a computer to follow. Think of it like giving someone a recipe to bake a cake, step by step. Python is one of the languages we use to write these instructions. It is designed to be extremely easy to read, almost like plain English.</p>

<h3>B. Why do we need it?</h3>
<p>Computers are incredibly fast, but they are not smart on their own. They don't know how to solve problems. We need programming to translate our human ideas and logic into simple steps that a computer can execute. Without programming, a computer is just a piece of metal.</p>

<h3>C. Real-life analogy</h3>
<p>Imagine you are giving directions to a friend visiting your house: "Walk down the street, take the second left, and it's the third house on the right." You are "programming" their path. If you make a mistake and say "right" instead of "left", your friend gets lost. In programming, that wrong direction is called a <strong>bug</strong>!</p>

<h3>D. How does it work?</h3>
<p>You write text called <strong>source code</strong> using Python. A special software called the <strong>Python Interpreter</strong> reads your code line by line from top to bottom. It translates your English-like text into a secret binary language (0s and 1s) that the computer hardware understands, and then the computer performs the action immediately.</p>

<h3>E. Syntax</h3>
<p>Syntax is the grammar of a programming language. Just as English has rules (like ending sentences with a period), Python has rules. For example, to make the computer print a message on the screen, we use the <code>print()</code> command.</p>

<h3>F. First simple example</h3>
<pre><code>print("Hello, World!")</code></pre>

<h3>G. Second practical example</h3>
<pre><code>print("Welcome to LEARNX!")
print("Let's learn Python together.")</code></pre>

<h3>H. Code explanation</h3>
<p>Let's look at <code>print("Hello, World!")</code> step by step:</p>
<ul>
    <li><code>print</code> is a built-in command that tells Python to show something on the screen.</li>
    <li><code>()</code> The parentheses hold the data we want to print.</li>
    <li><code>"Hello, World!"</code> The quotation marks tell Python that this is literal text (a string of characters), not a command.</li>
</ul>

<h3>I. Execution flow</h3>
<p>When you run the second example:</p>
<ol>
    <li>The interpreter reads line 1. It sees the print command and outputs <strong>Welcome to LEARNX!</strong> to the screen.</li>
    <li>The interpreter moves to line 2. It sees another print command and outputs <strong>Let's learn Python together.</strong> on a new line.</li>
    <li>The script reaches the end and the program finishes.</li>
</ol>

<h3>J. Output</h3>
<pre><code>Welcome to LEARNX!
Let's learn Python together.</code></pre>

<h3>K. Why this output?</h3>
<p>Because the <code>print()</code> command always takes the text inside the quotes and displays it in the console. By default, every <code>print()</code> command automatically hits "Enter" at the end, which is why the second message appears on a new line.</p>

<h3>L. Common mistakes</h3>
<ul>
    <li><strong>Forgetting the quotes:</strong> <code>print(Hello World)</code> will crash because Python thinks 'Hello' is a command, not text.</li>
    <li><strong>Capitalizing print:</strong> <code>Print("Hello")</code> will crash. Python is strictly case-sensitive. It only understands lowercase <code>print</code>.</li>
    <li><strong>Missing a parenthesis:</strong> <code>print("Hello"</code> will cause a Syntax Error because the grammar rule is broken.</li>
</ul>

<h3>M. Important rules</h3>
<ul>
    <li>Python reads code line by line, from top to bottom.</li>
    <li>Python is case-sensitive (capitalization matters).</li>
    <li>Text must always be wrapped in quotation marks.</li>
</ul>

<h3>N. When should I use it?</h3>
<p>Use <code>print()</code> whenever you want to display information to the user, or when you want to check what a value is while trying to fix your code (debugging).</p>

<h3>O. When should I NOT use it?</h3>
<p>You shouldn't use <code>print()</code> if you want the computer to remember a value for later calculations. Printing just shows it on the screen and throws it away. (We will learn how to remember values in Module 3).</p>

<h3>P. Code reading</h3>
<p>When reading code, always start at line 1. Imagine you are the computer. What does this line tell you to do? Do it. Then move to the next line. If a line has an error, stop immediately.</p>

<h3>Q. Logic building</h3>
<p>Problem: Print your first name on one line and your last name on the next.</p>
<ul>
    <li><strong>What do we know?</strong> We know how to show text using <code>print()</code>.</li>
    <li><strong>What do we need?</strong> We need two lines of output.</li>
    <li><strong>What operation is required?</strong> Two separate <code>print()</code> commands, one after the other.</li>
</ul>

<h3>R. Concept connection</h3>
<p>This is the foundation. Every single Python script you write in the future will use the concepts of top-to-bottom execution and strict syntax grammar introduced here.</p>

<h3>S. Quick recap</h3>
<p>Programming is writing instructions. Python is a readable language executed line-by-line by an interpreter. The <code>print()</code> command displays text on the screen, but you must follow syntax rules like using lowercase and adding quotes around text.</p>
""",
            "examples": [
                {
                    "title": "Basic Hello World",
                    "explanation": "Outputs a message using the built-in print command.",
                    "code": "print(\"Welcome to Python!\")"
                }
            ],
            "exercises": [],
            "quizzes": []
        },
        {
            "title": "Module 1 Practice & Knowledge Check",
            "concept": "PythonIntroduction",
            "theory": """
<h3>Module 1 Assessment Workspace</h3>
<p>Apply the concepts of programming, instruction execution, and simple print statements in this workspace. Review the 5 exercises in the Practice Lab and test your understanding with the 10 quiz questions below.</p>
""",
            "examples": [],
            "exercises": [
                {
                    "title": "Print Greeting",
                    "desc": "Write a script that prints exactly 'Hello World' to the console.",
                    "starter": "# Write your code below\n",
                    "expected": "Hello World",
                    "test_cases": [
                        {"input": "", "expected": "Hello World\n", "is_hidden": False}
                    ]
                },
                {
                    "title": "Print LearnX",
                    "desc": "Write a script that prints exactly 'LEARNX' to the console.",
                    "starter": "# Write your code below\n",
                    "expected": "LEARNX",
                    "test_cases": [
                        {"input": "", "expected": "LEARNX\n", "is_hidden": False}
                    ]
                },
                {
                    "title": "Print Python 3",
                    "desc": "Write a script that prints exactly 'Python 3' to the console.",
                    "starter": "# Write your code below\n",
                    "expected": "Python 3",
                    "test_cases": [
                        {"input": "", "expected": "Python 3\n", "is_hidden": False}
                    ]
                },
                {
                    "title": "Multi-line Print",
                    "desc": "Print 'Line 1' on the first line and 'Line 2' on the second line.",
                    "starter": "# Write your code below\n",
                    "expected": "Line 1\nLine 2",
                    "test_cases": [
                        {"input": "", "expected": "Line 1\nLine 2\n", "is_hidden": False}
                    ]
                },
                {
                    "title": "Coding is Fun",
                    "desc": "Print the exact message 'Coding is fun!'. Watch out for punctuation.",
                    "starter": "# Write code here\n",
                    "expected": "Coding is fun!",
                    "test_cases": [
                        {"input": "", "expected": "Coding is fun!\n", "is_hidden": False}
                    ]
                }
            ],
            "quizzes": [
                {
                    "question": "What is programming in simple terms?",
                    "options": [
                        "Writing instructions for a computer to follow",
                        "Designing hardware computer chips",
                        "Repairing physical electrical circuits",
                        "Searching web search engines"
                    ],
                    "correct": "Writing instructions for a computer to follow",
                    "explanation": "Programming is composing structured logic that guides computer operations.",
                    "difficulty": "Beginner"
                },
                {
                    "question": "What is a 'bug' in computer programming?",
                    "options": [
                        "An physical insect inside the laptop case",
                        "An error or mistake in code that causes unintended behavior",
                        "A useful feature requested by the user",
                        "A compiler package dependency"
                    ],
                    "correct": "An error or mistake in code that causes unintended behavior",
                    "explanation": "A bug is any syntax or logical flaw that causes a program to fail or act incorrectly.",
                    "difficulty": "Beginner"
                },
                {
                    "question": "Who created the Python programming language?",
                    "options": [
                        "Dennis Ritchie",
                        "James Gosling",
                        "Guido van Rossum",
                        "Bjarne Stroustrup"
                    ],
                    "correct": "Guido van Rossum",
                    "explanation": "Guido van Rossum developed Python and released it in 1991.",
                    "difficulty": "Beginner"
                },
                {
                    "question": "What does a Python interpreter do?",
                    "options": [
                        "Compiles code into offline executable file libraries",
                        "Reads and executes Python code line-by-line",
                        "Translates Python into Javascript scripts",
                        "Deletes files to free memory space"
                    ],
                    "correct": "Reads and executes Python code line-by-line",
                    "explanation": "Interpretive environments execute commands line-by-line directly at runtime.",
                    "difficulty": "Beginner"
                },
                {
                    "question": "In Python, which character is used to indicate a single-line comment?",
                    "options": ["//", "#", "/*", "--"],
                    "correct": "#",
                    "explanation": "# tells the interpreter to ignore the rest of that line.",
                    "difficulty": "Beginner"
                },
                {
                    "question": "What will print('Welcome') output to the console?",
                    "options": [
                        "'Welcome'",
                        "Welcome",
                        "print('Welcome')",
                        "SyntaxError"
                    ],
                    "correct": "Welcome",
                    "explanation": "The print function outputs the string inside, excluding boundary quotes.",
                    "difficulty": "Beginner"
                },
                {
                    "question": "If the interpreter encounters a syntax error on line 4 of a 10-line script, what happens?",
                    "options": [
                        "It ignores line 4 and executes the rest",
                        "It executes lines 1 to 3, then stops and displays an error",
                        "It compiles the program anyway",
                        "It runs the lines backwards"
                    ],
                    "correct": "It executes lines 1 to 3, then stops and displays an error",
                    "explanation": "An interpreted flow stops execution the instant it hits an error.",
                    "difficulty": "Intermediate"
                },
                {
                    "question": "Which of the following is correct Python file extension?",
                    "options": [".pt", ".py", ".pyt", ".txt"],
                    "correct": ".py",
                    "explanation": "Python script files use the extension '.py'.",
                    "difficulty": "Beginner"
                },
                {
                    "question": "What happens if you type Print('Hello') with a capital P?",
                    "options": [
                        "It executes normally",
                        "It raises a NameError because Python is case-sensitive",
                        "It raises a SyntaxError",
                        "It prints 'Hello'"
                    ],
                    "correct": "It raises a NameError because Python is case-sensitive",
                    "explanation": "Python is case-sensitive. The interpreter will search for a variable or function named 'Print' and raise a NameError.",
                    "difficulty": "Intermediate"
                },
                {
                    "question": "Why is Python popular for beginners?",
                    "options": [
                        "Its syntax is clean, readable and matches plain English",
                        "It does not require memory",
                        "It runs only on supercomputers",
                        "It requires writing hundreds of lines of boilerplate setup code"
                    ],
                    "correct": "Its syntax is clean, readable and matches plain English",
                    "explanation": "Python prioritizes readability and minimizes boilerplate setups.",
                    "difficulty": "Beginner"
                }
            ]
        }
    ]
}
