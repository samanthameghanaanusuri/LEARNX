MODULE_DATA = {
    "title": "Variables, Data Types & Type Conversion",
    "concept": "VariablesAndTypes",
    "lessons": [
        {
            "title": "Declaring Variables and Primitive Types",
            "concept": "VariablesIntro",
            "theory": """
<h3>A. What is this?</h3>
<p>A <strong>variable</strong> is a name that we use to refer to a value. Think of it as a labeled box where you can store data. <strong>Data types</strong> tell Python what <em>kind</em> of data is inside the box (like text, whole numbers, or decimal numbers). <strong>Type conversion</strong> is the process of changing data from one type into another.</p>

<h3>B. Why do we need it?</h3>
<p>Programs need to remember things. If you write a game, the computer needs to remember the player's score. Without variables, the computer would forget the score the moment it changes. We need data types so the computer knows how to handle the data—for example, you can multiply numbers, but you cannot mathematically multiply two words together.</p>

<h3>C. Real-life analogy</h3>
<p>Imagine a storage locker facility. You rent locker #42 (the variable name) and put your backpack (the data) inside. Later, you just ask for locker #42 to get your backpack. The locker size and shape might depend on what you put inside: a small box for jewelry (integer), a large bin for clothes (string).</p>

<h3>D. How does it work?</h3>
<p>You create a variable using the assignment operator (<code>=</code>). On the left is the name you invent. On the right is the data you want to store. Python looks at the data, figures out its type automatically, and saves it in memory.</p>

<h3>E. Syntax</h3>
<pre><code>variable_name = data_value</code></pre>

<h3>F. First simple example</h3>
<pre><code>age = 20
print(age)</code></pre>

<h3>G. Second practical example</h3>
<pre><code># Storing different types of data
player_name = "Alex"    # This is a string (text)
score = 150             # This is an integer (whole number)
health = 99.5           # This is a float (decimal number)
is_alive = True         # This is a boolean (True/False)

# Changing a string into an integer (Type Conversion)
level_text = "5"
level_number = int(level_text)

print(player_name)
print(level_number)
</code></pre>

<h3>H. Code explanation</h3>
<p>In the practical example:</p>
<ul>
    <li><code>player_name = "Alex"</code> creates a text variable. Text must always have quotes.</li>
    <li><code>score = 150</code> creates a number variable. No quotes!</li>
    <li><code>is_alive = True</code> creates a boolean. Notice the capital T and no quotes.</li>
    <li><code>level_number = int(level_text)</code> takes the text "5", hands it to the <code>int()</code> function, which converts it into the actual math number 5.</li>
</ul>

<h3>I. Execution flow</h3>
<p>When the code runs:</p>
<ol>
    <li>Line 2: Python allocates memory for the text "Alex" and names it <code>player_name</code>.</li>
    <li>Lines 3-5: Python does the same for the score, health, and is_alive variables.</li>
    <li>Line 8: Python saves the text "5".</li>
    <li>Line 9: Python reads "5", converts it to the number 5, and stores it in <code>level_number</code>.</li>
    <li>Lines 11-12: The <code>print()</code> statements fetch the stored data and display it.</li>
</ol>

<h3>J. Output</h3>
<pre><code>Alex
5</code></pre>

<h3>K. Why this output?</h3>
<p>The code asks Python to print whatever is inside the <code>player_name</code> box ("Alex") and whatever is inside the <code>level_number</code> box (the converted integer 5).</p>

<h3>L. Common mistakes</h3>
<ul>
    <li><strong>Putting numbers in quotes:</strong> <code>age = "20"</code> means age is a word that looks like a number. You cannot do math with it.</li>
    <li><strong>Using equal signs backwards:</strong> <code>20 = age</code> will cause a <code>SyntaxError</code>. The variable name MUST be on the left.</li>
    <li><strong>Converting letters to numbers:</strong> <code>int("apple")</code> will crash the program with a <code>ValueError</code> because "apple" cannot be turned into a number.</li>
</ul>

<h3>M. Important rules</h3>
<ul>
    <li>The name is always on the left, the data is always on the right.</li>
    <li>Python automatically knows the type of your data based on how you write it (quotes mean string, no decimal means int, decimal means float).</li>
    <li>To change a type, use <code>int()</code>, <code>float()</code>, <code>str()</code>, or <code>bool()</code>.</li>
</ul>

<h3>N. When should I use it?</h3>
<p>You must use variables constantly in programming. Any time you have data that you want to use more than once, or data that will change over time, store it in a variable.</p>

<h3>O. When should I NOT use it?</h3>
<p>If you only need to use a piece of data exactly once and it never changes, you can just type it directly. For example, <code>print(5 + 5)</code> is fine. You don't need to do <code>x = 5; y = 5; print(x + y)</code> unless you plan to reuse those numbers.</p>

<h3>P. Code reading</h3>
<p>When you see an <code>=</code> sign, don't think "equals". Think "gets". <code>score = 150</code> means "The variable score GETS the value 150."</p>

<h3>Q. Logic building</h3>
<p>Problem: You have a price of "$10" stored as text, and you want to calculate a discount, but the computer can't do math on text.</p>
<ul>
    <li><strong>What do we know?</strong> We have text "10".</li>
    <li><strong>What do we need?</strong> The number 10.</li>
    <li><strong>What operation is required?</strong> Type conversion! Use <code>int("10")</code> to convert it so you can perform math.</li>
</ul>

<h3>R. Concept connection</h3>
<p>In Module 2, we learned how to name variables (identifiers). Now we learn how to actually put data inside them and how the computer understands the differences between text and numbers.</p>

<h3>S. Quick recap</h3>
<p>Variables are named boxes for data. You assign data using <code>=</code>. Data comes in types: <code>str</code> (text), <code>int</code> (whole numbers), <code>float</code> (decimals), and <code>bool</code> (True/False). You can convert between them using functions like <code>int()</code> and <code>str()</code>.</p>
""",
            "examples": [
                {
                    "title": "Casting",
                    "explanation": "Converts string text into a math-compatible integer.",
                    "code": "num_str = \"10\"\nnum_int = int(num_str)\nprint(num_int + 5)"
                }
            ],
            "exercises": [],
            "quizzes": []
        },
        {
            "title": "Module 3 Practice & Knowledge Check",
            "concept": "PrimitiveTypes",
            "theory": """
<h3>Module 3 Assessment Workspace</h3>
<p>Review the 5 programming exercises in the Practice Lab and test your understanding of data types and casting with the 10 quiz questions below.</p>
""",
            "examples": [],
            "exercises": [
                {
                    "title": "Variable Assign",
                    "desc": "Create a variable named 'x', assign it the exact value 15, and print it.",
                    "starter": "# Write code here\n",
                    "expected": "15",
                    "test_cases": [
                        {"input": "", "expected": "15\n", "is_hidden": False}
                    ]
                },
                {
                    "title": "Float Variable",
                    "desc": "Create a variable named 'y' and assign it the decimal number 5.5. Then print 'y'.",
                    "starter": "# Write code here\n",
                    "expected": "5.5",
                    "test_cases": [
                        {"input": "", "expected": "5.5\n", "is_hidden": False}
                    ]
                },
                {
                    "title": "Cast Int to Float",
                    "desc": "The variable 'val' holds 10. Cast it to a float (which adds a decimal point) and print it.",
                    "starter": "val = 10\n# Print as float below\n",
                    "expected": "10.0",
                    "test_cases": [
                        {"input": "", "expected": "10.0\n", "is_hidden": False}
                    ]
                },
                {
                    "title": "Convert String",
                    "desc": "The variable 's' holds the text '25'. Cast it to an integer using int() and print it.",
                    "starter": "s = '25'\n# Cast and print below\n",
                    "expected": "25",
                    "test_cases": [
                        {"input": "", "expected": "25\n", "is_hidden": False}
                    ]
                },
                {
                    "title": "Boolean Output",
                    "desc": "Create a variable 'is_valid' and set it to True. Then print its type using type(is_valid).__name__.",
                    "starter": "is_valid = True\n# print type name below\nprint(type(is_valid).__name__)",
                    "expected": "bool",
                    "test_cases": [
                        {"input": "", "expected": "bool\n", "is_hidden": False}
                    ]
                }
            ],
            "quizzes": [
                {
                    "question": "What is the data type of the value 10.0?",
                    "options": ["int", "float", "str", "bool"],
                    "correct": "float",
                    "explanation": "Any number that contains a decimal point is treated as a float (floating-point number) by Python.",
                    "difficulty": "Beginner"
                },
                {
                    "question": "What will print(type('True')) output?",
                    "options": [
                        "<class 'bool'>",
                        "<class 'str'>",
                        "<class 'int'>",
                        "True"
                    ],
                    "correct": "<class 'str'>",
                    "explanation": "Because the word 'True' is wrapped in quotation marks, Python sees it as literal text (a string), not the boolean True.",
                    "difficulty": "Intermediate"
                },
                {
                    "question": "What does dynamic typing mean in Python?",
                    "options": [
                        "Variables can change their data type dynamically as they point to new values",
                        "You must declare the data type before using a variable",
                        "Variables cannot be updated after assignment",
                        "Python handles variables only in memory"
                    ],
                    "correct": "Variables can change their data type dynamically as they point to new values",
                    "explanation": "In Python, a variable `x = 5` (int) can later become `x = \"apple\"` (string) without crashing. It adapts to the data.",
                    "difficulty": "Intermediate"
                },
                {
                    "question": "What is the result of int(5.9) in Python?",
                    "options": ["6", "5", "5.9", "Raises ValueError"],
                    "correct": "5",
                    "explanation": "Casting a float to an int simply chops off (truncates) the decimal part. It does NOT round to the nearest whole number.",
                    "difficulty": "Intermediate"
                },
                {
                    "question": "Which constructor is used to convert a number into text?",
                    "options": ["int()", "float()", "str()", "bool()"],
                    "correct": "str()",
                    "explanation": "The str() function takes objects (like numbers) and converts them into string format.",
                    "difficulty": "Beginner"
                },
                {
                    "question": "What happens if you run the code: int('Hello')?",
                    "options": [
                        "Returns 0",
                        "Raises a ValueError",
                        "Returns None",
                        "Converts characters to ASCII values"
                    ],
                    "correct": "Raises a ValueError",
                    "explanation": "The text 'Hello' does not contain mathematical numbers, so the int() function crashes because it cannot convert it.",
                    "difficulty": "Intermediate"
                },
                {
                    "question": "What is the data type of the expression: 10 + 5.0?",
                    "options": ["int", "float", "str", "TypeError"],
                    "correct": "float",
                    "explanation": "When you mix an integer and a float in math, Python implicitly upgrades the integer to a float to prevent losing decimal data.",
                    "difficulty": "Intermediate"
                },
                {
                    "question": "What does bool('') (an empty string) evaluate to?",
                    "options": ["True", "False", "None", "Error"],
                    "correct": "False",
                    "explanation": "Empty structures (like empty strings, empty lists, or the number 0) evaluate as 'falsy' in Python.",
                    "difficulty": "Intermediate"
                },
                {
                    "question": "What does the code x = y = z = 5 do?",
                    "options": [
                        "Raises SyntaxError",
                        "Assigns the number 5 to variables x, y, and z simultaneously",
                        "Checks if x, y, z are equal",
                        "Only assigns 5 to z"
                    ],
                    "correct": "Assigns the number 5 to variables x, y, and z simultaneously",
                    "explanation": "Chained assignment is a shortcut in Python that copies the right-most value into all variables listed.",
                    "difficulty": "Intermediate"
                },
                {
                    "question": "What does type(None) return?",
                    "options": [
                        "<class 'NoneType'>",
                        "<class 'null'>",
                        "<class 'void'>",
                        "None"
                    ],
                    "correct": "<class 'NoneType'>",
                    "explanation": "None is a special keyword in Python representing the absolute absence of a value, and it belongs to its own class called NoneType.",
                    "difficulty": "Intermediate"
                }
            ]
        }
    ]
}
