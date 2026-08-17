# C++ Course Content (Modules 1 and 2)

course_cpp = {
    'title': 'C++ Programming — Beginner to Advanced',
    'description': 'Master C++ from fundamental programming to advanced Object-Oriented Design, STL, and Data Structures.',
    'slug': 'cpp-programming',
    'language': 'cpp',
    'level': 'Beginner to Advanced',
    'thumbnail': 'https://upload.wikimedia.org/wikipedia/commons/1/18/ISO_C%2B%2B_Logo.svg'
}

m1_lesson = """# C++ Fundamentals

## What Is C++?

C++ is a high-performance, compiled, general-purpose programming language created by Bjarne Stroustrup as an extension of the C programming language. It introduces Object-Oriented Programming (OOP) features while retaining the raw speed and low-level memory control of C.

At its core, C++ allows developers to build systems that are both highly abstract (easy to reason about) and highly optimized (blazing fast).

## Why Do We Need It?

While languages like Python and Java are easier to write, they abstract away memory management and introduce runtime overhead (like a Virtual Machine or Garbage Collector). 

C++ compiles directly to machine code. When performance is absolutely critical—meaning milliseconds matter—C++ is the tool of choice.

## Where Is It Used?

- High-frequency trading systems
- Game engines (Unreal Engine)
- Operating systems and drivers
- Web browsers (Chrome V8 engine)
- Embedded systems

## How Does It Work?

C++ requires a strict compilation pipeline before a program can be executed:

```text
source.cpp
   ↓
preprocessor (handles #include and macros)
   ↓
compiler (translates to assembly)
   ↓
assembler (translates to machine code / object file)
   ↓
linker (links libraries and multiple object files)
   ↓
executable (.exe or .out)
```

## Syntax

```cpp
#include <iostream>

int main() {
    // Your code goes here
    return 0;
}
```

## Example 1 — Simple

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, C++ World!" << std::endl;
    return 0;
}
```

### Output

```text
Hello, C++ World!
```

### Line-by-Line Explanation

1. `#include <iostream>`: The preprocessor includes the standard input-output stream library, giving us access to `std::cout`.
2. `int main()`: The mandatory entry point for every C++ program. The OS calls this function to start execution.
3. `std::cout << ...`: "Character output". It sends the string to the console. `std::endl` inserts a newline and flushes the buffer.
4. `return 0;`: Indicates to the Operating System that the program executed successfully without errors.

## Common Mistakes

* **Forgetting `#include <iostream>`**: The compiler won't know what `std::cout` is and will throw an error.
* **Missing semicolons (`;`)**: Every statement in C++ must end with a semicolon.
* **Returning a non-zero value on success**: Returning `1` or `-1` from `main()` signals to the OS that your program crashed or failed.

## Best Practices

* Always return `0` from `main()`.
* Comment your code using `//` for single lines or `/* */` for blocks.
* Structure your code neatly with proper indentation.

## Try It Yourself

Write a C++ program that prints your name and age on two separate lines.
"""

m1_exercises = [
    {
        "title": "Hello, C++!",
        "description": "Write a C++ program that outputs exactly `Welcome to C++!`.",
        "difficulty": "Easy",
        "concepts": "main, cout",
        "starter_code": "#include <iostream>\n\nint main() {\n    // write your code here\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    std::cout << \"Welcome to C++!\" << std::endl;\n    return 0;\n}\n",
        "test_cases": [{"input": "", "expected_output": "Welcome to C++!\n"}]
    },
    {
        "title": "Two Lines of Output",
        "description": "Print `Line 1` on the first line and `Line 2` on the second line.",
        "difficulty": "Easy",
        "concepts": "cout, endl",
        "starter_code": "#include <iostream>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    std::cout << \"Line 1\" << std::endl;\n    std::cout << \"Line 2\" << std::endl;\n    return 0;\n}\n",
        "test_cases": [{"input": "", "expected_output": "Line 1\nLine 2\n"}]
    },
    {
        "title": "Understanding the Entry Point",
        "description": "Fix the provided code so it compiles and runs. It is currently missing the correct entry point signature.",
        "difficulty": "Medium",
        "concepts": "main function signature",
        "starter_code": "#include <iostream>\n\nvoid start_program() {\n    std::cout << \"Starting...\" << std::endl;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    std::cout << \"Starting...\" << std::endl;\n    return 0;\n}\n",
        "test_cases": [{"input": "", "expected_output": "Starting...\n"}]
    },
    {
        "title": "Missing Header File",
        "description": "This code attempts to use `std::cout` but the programmer forgot something crucial at the top of the file.",
        "difficulty": "Medium",
        "concepts": "#include, preprocessor",
        "starter_code": "int main() {\n    std::cout << \"System Online\" << std::endl;\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    std::cout << \"System Online\" << std::endl;\n    return 0;\n}\n",
        "test_cases": [{"input": "", "expected_output": "System Online\n"}]
    },
    {
        "title": "Fix the Semicolons",
        "description": "The following program has syntax errors due to missing semicolons. Fix them to output `Ready.`",
        "difficulty": "Hard",
        "concepts": "syntax, semicolons",
        "starter_code": "#include <iostream>\n\nint main() {\n    std::cout << \"Ready.\" << std::endl\n    return 0\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    std::cout << \"Ready.\" << std::endl;\n    return 0;\n}\n",
        "test_cases": [{"input": "", "expected_output": "Ready.\n"}]
    },
    {
        "title": "Custom Exit Status",
        "description": "Write a program that prints `Failure detected` and returns an exit status of `1` instead of `0`.",
        "difficulty": "Challenge",
        "concepts": "return codes",
        "starter_code": "#include <iostream>\n\nint main() {\n    \n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    std::cout << \"Failure detected\" << std::endl;\n    return 1;\n}\n",
        "test_cases": [{"input": "", "expected_output": "Failure detected\n"}]
    }
]

m1_quizzes = [
    {"question_text": "What is C++?", "options": ["A web markup language", "A compiled, high-performance programming language with OOP features", "An interpreted scripting language", "A database query language"], "correct_answer": "A compiled, high-performance programming language with OOP features", "explanation": "C++ is a powerful compiled language built as an extension to C, adding OOP capabilities.", "difficulty": "Beginner"},
    {"question_text": "Who created C++?", "options": ["Dennis Ritchie", "Guido van Rossum", "Bjarne Stroustrup", "James Gosling"], "correct_answer": "Bjarne Stroustrup", "explanation": "Bjarne Stroustrup created C++ at Bell Labs in 1979 as an extension of the C language.", "difficulty": "Beginner"},
    {"question_text": "What is the primary entry point of a C++ program?", "options": ["start()", "init()", "main()", "run()"], "correct_answer": "main()", "explanation": "The Operating System looks for the main() function to begin execution of the binary.", "difficulty": "Beginner"},
    {"question_text": "Which pipeline stage converts C++ source code into an object file?", "options": ["Preprocessor", "Compiler", "Linker", "Debugger"], "correct_answer": "Compiler", "explanation": "The compiler translates high-level C++ into assembly/machine code, producing an object file (.o or .obj).", "difficulty": "Medium"},
    {"question_text": "What does the Linker do?", "options": ["Checks for syntax errors", "Executes the program", "Translates macros", "Combines multiple object files and standard libraries into a single executable"], "correct_answer": "Combines multiple object files and standard libraries into a single executable", "explanation": "The linker resolves external symbol references across files to build the final executable.", "difficulty": "Medium"},
    {"question_text": "What does return 0; in main() signify?", "options": ["The program crashed", "The program expects 0 inputs", "Successful execution", "The program took 0 seconds to run"], "correct_answer": "Successful execution", "explanation": "Returning 0 to the OS is the universal standard for indicating that the process finished without errors.", "difficulty": "Medium"},
    {"question_text": "What is the role of the preprocessor directive #include <iostream>?", "options": ["It compiles the program faster", "It tells the compiler to literally copy-paste the contents of the iostream header file into the source before compiling", "It links the math library", "It creates a web server"], "correct_answer": "It tells the compiler to literally copy-paste the contents of the iostream header file into the source before compiling", "explanation": "The preprocessor resolves #include directives by inserting the referenced file's contents directly into the source code.", "difficulty": "Hard"},
    {"question_text": "What does std::endl do?", "options": ["Ends the program", "Inserts a newline character and flushes the output buffer", "Deletes the last character printed", "Closes the terminal"], "correct_answer": "Inserts a newline character and flushes the output buffer", "explanation": "std::endl is equivalent to printing '\\n' followed by a call to std::flush.", "difficulty": "Hard"},
    {"question_text": "Is C++ an interpreted language like Python?", "options": ["Yes, it runs inside a Virtual Machine", "No, it is compiled directly down to raw machine code specific to the CPU architecture", "Yes, it reads code line-by-line", "It depends on the IDE"], "correct_answer": "No, it is compiled directly down to raw machine code specific to the CPU architecture", "explanation": "C++ relies on Ahead-Of-Time (AOT) compilation, resulting in highly optimized native binaries.", "difficulty": "Hard"},
    {"question_text": "Which symbol is strictly required to terminate a standard C++ statement?", "options": [": (colon)", ". (period)", "} (closing brace)", "; (semicolon)"], "correct_answer": "; (semicolon)", "explanation": "Semicolons are mandatory statement terminators in C++. Without them, the compiler cannot parse the syntax.", "difficulty": "Beginner"}
]

m2_lesson = """# Variables, Data Types & Constants

## What Is It?

A variable is a named storage location in your computer's RAM. To use a variable in C++, you must explicitly define its **Data Type**. 

Data types tell the compiler exactly how many bytes of memory to reserve and how to interpret the binary 1s and 0s stored there.

## Why Do We Need It?

Without variables, programs couldn't remember anything. We need variables to store user input, calculate results, and track application state. 

Because C++ is statically typed, declaring types explicitly (`int`, `float`, `bool`) allows the compiler to catch invalid operations (like multiplying a word by a number) before the program even runs, while aggressively optimizing memory layout.

## Data Types

- `int`: Whole numbers (usually 4 bytes). e.g., `10`, `-5`
- `double`: High-precision floating-point numbers (usually 8 bytes). e.g., `3.14159`
- `float`: Lower-precision floating-point numbers (usually 4 bytes). e.g., `3.14f`
- `char`: Single characters (1 byte). e.g., `'A'`, `'z'`
- `bool`: True/False values (1 byte). e.g., `true`, `false`

## Syntax

```cpp
// DataType VariableName = InitialValue;
int age = 20;
const double PI = 3.14159;
```

## Example 1 — Simple

```cpp
#include <iostream>

int main() {
    int score = 95;
    char grade = 'A';
    bool passed = true;

    std::cout << "Score: " << score << std::endl;
    std::cout << "Grade: " << grade << std::endl;
    
    return 0;
}
```

### Output

```text
Score: 95
Grade: A
```

### Line-by-Line Explanation

1. `int score = 95;`: Reserves 4 bytes of RAM, names it `score`, and stores the integer 95.
2. `char grade = 'A';`: Reserves 1 byte of RAM, names it `grade`, and stores the ASCII value for 'A' (which is 65).
3. `bool passed = true;`: Reserves 1 byte, stores `1` (true).

## Example 2 — Real World (Constants & Size)

```cpp
#include <iostream>

int main() {
    const double PI = 3.14159; // Cannot be modified later
    double radius = 5.0;
    
    double area = PI * radius * radius;
    
    std::cout << "Area: " << area << std::endl;
    std::cout << "Bytes used by area variable: " << sizeof(area) << std::endl;

    return 0;
}
```

### Output

```text
Area: 78.5397
Bytes used by area variable: 8
```

### Explanation

`const` protects a variable from being accidentally changed. The `sizeof` operator inspects exactly how much physical memory a variable is consuming.

## Common Mistakes

* **Using single quotes for strings**: `'Hello'` is invalid. Single quotes `'H'` are for `char` (1 byte). Double quotes `"Hello"` are for strings.
* **Modifying a `const`**: Trying to do `PI = 3.0;` when `PI` is constant will cause a compile error.
* **Uninitialized variables**: Doing `int x; std::cout << x;` prints garbage memory leftover from other programs. Always initialize: `int x = 0;`.

## Best Practices

* Use meaningful variable names (`studentAge` instead of `x`).
* Use `const` by default for values that shouldn't change.
* Use `double` instead of `float` unless you are strictly optimizing for memory in large arrays or game engines.

## Try It Yourself

Declare a `double` for temperature, assign it `98.6`, and print it.
"""

m2_exercises = [
    {
        "title": "Store an Integer",
        "description": "Declare an `int` variable named `year`, assign it the value `2050`, and print it.",
        "difficulty": "Easy",
        "concepts": "int, variables",
        "starter_code": "#include <iostream>\n\nint main() {\n    // declare and print year\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int year = 2050;\n    std::cout << year << std::endl;\n    return 0;\n}\n",
        "test_cases": [{"input": "", "expected_output": "2050\n"}]
    },
    {
        "title": "Using Constants",
        "description": "Declare a constant double named `GRAVITY` initialized to `9.81`. Print it.",
        "difficulty": "Easy",
        "concepts": "const, double",
        "starter_code": "#include <iostream>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    const double GRAVITY = 9.81;\n    std::cout << GRAVITY << std::endl;\n    return 0;\n}\n",
        "test_cases": [{"input": "", "expected_output": "9.81\n"}]
    },
    {
        "title": "Character Output",
        "description": "Declare a `char` named `letter` and assign it the character `Z`. Print it.",
        "difficulty": "Medium",
        "concepts": "char",
        "starter_code": "#include <iostream>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    char letter = 'Z';\n    std::cout << letter << std::endl;\n    return 0;\n}\n",
        "test_cases": [{"input": "", "expected_output": "Z\n"}]
    },
    {
        "title": "Uninitialized Garbage",
        "description": "The provided code attempts to print an uninitialized variable, which prints garbage data. Fix it by initializing `count` to `0`.",
        "difficulty": "Medium",
        "concepts": "initialization",
        "starter_code": "#include <iostream>\n\nint main() {\n    int count;\n    std::cout << count << std::endl;\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int count = 0;\n    std::cout << count << std::endl;\n    return 0;\n}\n",
        "test_cases": [{"input": "", "expected_output": "0\n"}]
    },
    {
        "title": "Size of Types",
        "description": "Print the byte size of a `double` type using the `sizeof` operator.",
        "difficulty": "Hard",
        "concepts": "sizeof",
        "starter_code": "#include <iostream>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    std::cout << sizeof(double) << std::endl;\n    return 0;\n}\n",
        "test_cases": [{"input": "", "expected_output": "8\n"}]
    },
    {
        "title": "Boolean Output",
        "description": "Declare a `bool` named `isValid` set to `true`. Print it. Observe how C++ prints booleans by default.",
        "difficulty": "Hard",
        "concepts": "bool",
        "starter_code": "#include <iostream>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    bool isValid = true;\n    std::cout << isValid << std::endl;\n    return 0;\n}\n",
        "test_cases": [{"input": "", "expected_output": "1\n"}]
    },
    {
        "title": "Profile Builder",
        "description": "Declare an `int` for age (25), a `double` for weight (70.5), and a `char` for section ('B'). Print them separated by spaces on a single line.",
        "difficulty": "Challenge",
        "concepts": "variables, formatting",
        "starter_code": "#include <iostream>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int age = 25;\n    double weight = 70.5;\n    char section = 'B';\n    std::cout << age << \" \" << weight << \" \" << section << std::endl;\n    return 0;\n}\n",
        "test_cases": [{"input": "", "expected_output": "25 70.5 B\n"}]
    }
]

m2_quizzes = [
    {"question_text": "What does a variable declaration do in C++?", "options": ["Compiles the code", "Reserves a named location in RAM and defines how much space is needed based on the type", "Deletes memory", "Prints to the console"], "correct_answer": "Reserves a named location in RAM and defines how much space is needed based on the type", "explanation": "Declaring a variable instructs the compiler to allocate specific bytes in memory and map them to a human-readable identifier.", "difficulty": "Beginner"},
    {"question_text": "Which data type is most appropriate for storing the character 'Q'?", "options": ["int", "char", "double", "bool"], "correct_answer": "char", "explanation": "The 'char' type allocates 1 byte, which is perfectly sized for storing a single ASCII character like 'Q'.", "difficulty": "Beginner"},
    {"question_text": "What is the typical size of a double in C++?", "options": ["1 byte", "2 bytes", "4 bytes", "8 bytes"], "correct_answer": "8 bytes", "explanation": "A double-precision floating point number typically occupies 8 bytes (64 bits), providing immense decimal precision.", "difficulty": "Medium"},
    {"question_text": "What does the 'const' keyword do?", "options": ["Makes a variable accessible everywhere", "Creates a variable whose value is read-only and cannot be reassigned after initialization", "Allocates memory on the heap", "Forces the variable to be an integer"], "correct_answer": "Creates a variable whose value is read-only and cannot be reassigned after initialization", "explanation": "const strictly locks a variable's state. Any subsequent attempt to modify it will result in a compile error.", "difficulty": "Medium"},
    {"question_text": "What happens if you print a boolean variable set to 'true' using std::cout without std::boolalpha?", "options": ["It prints 'true'", "It prints 'yes'", "It prints '1'", "It throws an error"], "correct_answer": "It prints '1'", "explanation": "By default, C++ treats booleans as integers when printing, outputting 1 for true and 0 for false.", "difficulty": "Medium"},
    {"question_text": "Why is it dangerous to read from an uninitialized local variable?", "options": ["It crashes the computer", "It contains random 'garbage' data from whatever previously occupied that RAM space, leading to unpredictable bugs", "It always equals zero, which might be wrong", "The compiler refuses to compile"], "correct_answer": "It contains random 'garbage' data from whatever previously occupied that RAM space, leading to unpredictable bugs", "explanation": "C++ does not zero out memory for local variables for performance reasons. Reading them yields raw garbage bytes.", "difficulty": "Hard"},
    {"question_text": "Which quotes are used to assign a literal to a char variable?", "options": ["Double quotes (e.g. \"A\")", "Single quotes (e.g. 'A')", "Backticks (e.g. `A`)", "No quotes (e.g. A)"], "correct_answer": "Single quotes (e.g. 'A')", "explanation": "Single quotes denote a char literal (1 byte). Double quotes denote a string literal (an array of chars).", "difficulty": "Beginner"},
    {"question_text": "What does the sizeof operator return?", "options": ["The maximum allowed value of a variable", "The number of digits in a number", "The amount of memory in bytes that a type or variable occupies", "The length of a string"], "correct_answer": "The amount of memory in bytes that a type or variable occupies", "explanation": "sizeof is evaluated at compile time and reports the exact byte footprint of a variable or type.", "difficulty": "Medium"},
    {"question_text": "Which of these is NOT a valid C++ variable name?", "options": ["playerScore", "_hidden_value", "2ndPlace", "MAX_HEALTH"], "correct_answer": "2ndPlace", "explanation": "Variable names in C++ can contain numbers, but they cannot START with a number.", "difficulty": "Hard"},
    {"question_text": "What happens if you assign 3.99 to an int variable?", "options": ["It rounds up to 4", "It crashes", "It throws a syntax error", "It truncates the decimal and stores 3"], "correct_answer": "It truncates the decimal and stores 3", "explanation": "Implicit conversion from floating-point to integer truncates (drops) the fractional part entirely without rounding.", "difficulty": "Hard"}
]
