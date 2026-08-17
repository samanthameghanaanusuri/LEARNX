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


m3_lesson = """# Input, Output & Control Flow

## What Is It?

Input and Output (I/O) allow a program to communicate with the outside world. In C++, `std::cin` reads input from the keyboard, and `std::cout` writes output to the screen. 

Control Flow refers to the statements (`if`, `else`, `switch`) that dictate the path the execution takes based on conditions. Instead of running top-to-bottom blindly, the program can make decisions.

## Why Do We Need It?

A program without input always does the exact same thing every time it runs. A program without output is useless because we can't see the result. 

Control flow is what gives a program "logic." If a user tries to withdraw more money than they have, an `if` statement allows us to reject the transaction instead of allowing negative balances.

## Where Is It Used?

- ATM Machines: `if (balance >= withdrawal_amount) { dispenseCash(); } else { showError(); }`
- Video Games: `if (health <= 0) { showGameOver(); }`
- Forms: Reading a user's name and age via `cin`.

## How Does It Work?

1. **Input**: `cin` reads characters from the terminal buffer and automatically converts them into the target variable's type.
2. **Evaluation**: An `if` statement evaluates a boolean expression (e.g., `age >= 18`).
3. **Branching**: If the expression evaluates to `true` (1), the block of code inside `{ }` executes. If `false` (0), the program skips it and moves to the `else` block (if one exists).

## Syntax

```cpp
#include <iostream>

int main() {
    int age;
    std::cout << "Enter your age: ";
    std::cin >> age; // Reads input into 'age'

    if (age >= 18) {
        std::cout << "You are an adult." << std::endl;
    } else if (age >= 13) {
        std::cout << "You are a teenager." << std::endl;
    } else {
        std::cout << "You are a child." << std::endl;
    }

    return 0;
}
```

## Example 1 — Beginner (Grade Checker)

```cpp
#include <iostream>

int main() {
    int score;
    std::cout << "Enter score (0-100): ";
    std::cin >> score;

    if (score >= 90) {
        std::cout << "Grade: A" << std::endl;
    } else if (score >= 80) {
        std::cout << "Grade: B" << std::endl;
    } else if (score >= 70) {
        std::cout << "Grade: C" << std::endl;
    } else {
        std::cout << "Grade: F" << std::endl;
    }

    return 0;
}
```

### Output

```text
Enter score (0-100): 85
Grade: B
```

### Line-by-Line Explanation

1. `std::cin >> score;`: The program halts and waits for the user to type a number and press Enter.
2. `if (score >= 90)`: The CPU checks if 85 is greater than or equal to 90. It is false, so it skips this block.
3. `else if (score >= 80)`: It checks if 85 is greater than or equal to 80. This is true! It executes the block and skips the rest of the `else` chain.

## Example 2 — Real World (ATM Menu using Switch)

```cpp
#include <iostream>

int main() {
    int choice;
    std::cout << "1. View Balance\\n2. Withdraw\\n3. Deposit\\n";
    std::cout << "Enter choice: ";
    std::cin >> choice;

    switch (choice) {
        case 1:
            std::cout << "Your balance is $500." << std::endl;
            break;
        case 2:
            std::cout << "Withdrawal processed." << std::endl;
            break;
        case 3:
            std::cout << "Deposit processed." << std::endl;
            break;
        default:
            std::cout << "Invalid choice!" << std::endl;
    }

    return 0;
}
```

### Output

```text
1. View Balance
2. Withdraw
3. Deposit
Enter choice: 2
Withdrawal processed.
```

### Explanation

`switch` is highly optimized for comparing a single variable against multiple constant values. The `break` statement is critical; without it, execution "falls through" and executes the subsequent cases even if they don't match.

## Common Mistakes

* **Using `=` instead of `==`**: `if (x = 5)` assigns 5 to x and always evaluates to true. You must use `if (x == 5)`.
* **Forgetting `break` in a `switch`**: This causes "fall-through" bugs where multiple menu options execute at once.
* **Reading strings with spaces using `cin >>`**: `cin >> name` stops reading at the first space. To read a full name, use `std::getline(std::cin, name);` (requires `#include <string>`).

## Best Practices

* Always validate user input. If you expect a number, what happens if they type letters?
* Use `switch` when checking a single integer/char against specific values. Use `if-else` for ranges (e.g., `score >= 90`).
* Keep `if` blocks small and readable.

## Try It Yourself

Write a program that takes an integer and prints whether it is "Even" or "Odd". Use the modulo operator (`%`).
"""

m3_exercises = [
    {
        "title": "Even or Odd",
        "description": "Read an integer from the user. Print `Even` if it is divisible by 2, otherwise print `Odd`.",
        "difficulty": "Easy",
        "concepts": "cin, if-else, modulo",
        "starter_code": "#include <iostream>\n\nint main() {\n    int num;\n    std::cin >> num;\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int num;\n    std::cin >> num;\n    if (num % 2 == 0) {\n        std::cout << \"Even\" << std::endl;\n    } else {\n        std::cout << \"Odd\" << std::endl;\n    }\n    return 0;\n}\n",
        "test_cases": [
            {"input": "4", "expected_output": "Even\n"},
            {"input": "7", "expected_output": "Odd\n"},
            {"input": "0", "expected_output": "Even\n"}
        ]
    },
    {
        "title": "Maximum of Two",
        "description": "Read two integers. Print the larger of the two.",
        "difficulty": "Easy",
        "concepts": "if-else, relational operators",
        "starter_code": "#include <iostream>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int a, b;\n    std::cin >> a >> b;\n    if (a > b) std::cout << a << std::endl;\n    else std::cout << b << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "10 20", "expected_output": "20\n"},
            {"input": "50 15", "expected_output": "50\n"}
        ]
    },
    {
        "title": "Leap Year Checker",
        "description": "A year is a leap year if it is divisible by 4, except for end-of-century years which must be divisible by 400. Write a program to read a year and print `Leap Year` or `Not a Leap Year`.",
        "difficulty": "Medium",
        "concepts": "nested if, logical operators",
        "starter_code": "#include <iostream>\n\nint main() {\n    int year;\n    std::cin >> year;\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int year;\n    std::cin >> year;\n    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {\n        std::cout << \"Leap Year\" << std::endl;\n    } else {\n        std::cout << \"Not a Leap Year\" << std::endl;\n    }\n    return 0;\n}\n",
        "test_cases": [
            {"input": "2024", "expected_output": "Leap Year\n"},
            {"input": "1900", "expected_output": "Not a Leap Year\n"},
            {"input": "2000", "expected_output": "Leap Year\n"},
            {"input": "2023", "expected_output": "Not a Leap Year\n"}
        ]
    },
    {
        "title": "Simple Calculator",
        "description": "Read two numbers and a character operator (+, -, *, /). Print the result. If division by zero is attempted, print `Error`.",
        "difficulty": "Medium",
        "concepts": "switch, arithmetic",
        "starter_code": "#include <iostream>\n\nint main() {\n    double a, b;\n    char op;\n    std::cin >> a >> op >> b;\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    double a, b;\n    char op;\n    std::cin >> a >> op >> b;\n    switch(op) {\n        case '+': std::cout << a + b << std::endl; break;\n        case '-': std::cout << a - b << std::endl; break;\n        case '*': std::cout << a * b << std::endl; break;\n        case '/': \n            if (b == 0) std::cout << \"Error\" << std::endl;\n            else std::cout << a / b << std::endl;\n            break;\n        default: std::cout << \"Error\" << std::endl;\n    }\n    return 0;\n}\n",
        "test_cases": [
            {"input": "10 + 5", "expected_output": "15\n"},
            {"input": "10 / 0", "expected_output": "Error\n"},
            {"input": "4 * 3", "expected_output": "12\n"}
        ]
    },
    {
        "title": "Vowel or Consonant",
        "description": "Read a single character. Print `Vowel` if it is a, e, i, o, or u (case-insensitive). Print `Consonant` otherwise. Use a switch statement.",
        "difficulty": "Hard",
        "concepts": "switch fall-through",
        "starter_code": "#include <iostream>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    char c;\n    std::cin >> c;\n    c = tolower(c);\n    switch(c) {\n        case 'a': case 'e': case 'i': case 'o': case 'u':\n            std::cout << \"Vowel\" << std::endl;\n            break;\n        default:\n            std::cout << \"Consonant\" << std::endl;\n    }\n    return 0;\n}\n",
        "test_cases": [
            {"input": "E", "expected_output": "Vowel\n"},
            {"input": "z", "expected_output": "Consonant\n"}
        ]
    },
    {
        "title": "Triangle Validity",
        "description": "Read three angles of a triangle. Print `Valid` if they sum to exactly 180 and all angles are > 0. Otherwise print `Invalid`.",
        "difficulty": "Challenge",
        "concepts": "logical AND, conditions",
        "starter_code": "#include <iostream>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int a, b, c;\n    std::cin >> a >> b >> c;\n    if (a > 0 && b > 0 && c > 0 && (a + b + c == 180)) {\n        std::cout << \"Valid\" << std::endl;\n    } else {\n        std::cout << \"Invalid\" << std::endl;\n    }\n    return 0;\n}\n",
        "test_cases": [
            {"input": "60 60 60", "expected_output": "Valid\n"},
            {"input": "90 90 0", "expected_output": "Invalid\n"},
            {"input": "100 40 50", "expected_output": "Invalid\n"}
        ]
    }
]

m3_quizzes = [
    {"question_text": "What does the extraction operator (>>) do in std::cin >> x?", "options": ["Extracts data from the variable and prints it", "Shifts the bits of x to the right", "Reads formatted data from the standard input stream and stores it in the variable", "Clears the input buffer"], "correct_answer": "Reads formatted data from the standard input stream and stores it in the variable", "explanation": "cin >> takes data from the console buffer and converts it to match the type of the target variable.", "difficulty": "Beginner"},
    {"question_text": "What is the difference between == and = in C++?", "options": ["They are identical", "== is for assignment, = is for comparison", "= is for assignment, == is for equality comparison", "= is for integers, == is for strings"], "correct_answer": "= is for assignment, == is for equality comparison", "explanation": "= assigns the right side value to the left side variable. == evaluates if both sides are equal, returning true or false.", "difficulty": "Beginner"},
    {"question_text": "If x is 5 and y is 10, what does the expression (x > 0 && y < 5) evaluate to?", "options": ["true", "false", "5", "10"], "correct_answer": "false", "explanation": "While x > 0 is true, y < 5 is false. The logical AND (&&) requires BOTH sides to be true. Thus, the whole expression is false.", "difficulty": "Medium"},
    {"question_text": "What happens if you omit the 'break' statement inside a switch case?", "options": ["The program crashes", "The compiler throws a syntax error", "Execution falls through to the next case automatically, executing its code as well", "The switch statement ends immediately"], "correct_answer": "Execution falls through to the next case automatically, executing its code as well", "explanation": "Without break, a switch continues executing every subsequent line of code regardless of case labels.", "difficulty": "Medium"},
    {"question_text": "Which control flow structure is specifically designed for checking a single variable against many distinct, constant integer/character values?", "options": ["if-else chain", "switch statement", "ternary operator", "for loop"], "correct_answer": "switch statement", "explanation": "The switch statement compiles into a highly efficient jump table for comparing a single variable against constants.", "difficulty": "Medium"},
    {"question_text": "What is the result of the ternary expression (10 > 5) ? 100 : 200?", "options": ["10", "5", "100", "200"], "correct_answer": "100", "explanation": "The ternary operator (condition ? true_val : false_val) evaluates the condition. Since 10 > 5 is true, it returns the first value, 100.", "difficulty": "Hard"},
    {"question_text": "What happens when std::cin encounters a space character while reading into a std::string?", "options": ["It reads the space and continues", "It crashes", "It stops reading; cin uses whitespace as a delimiter", "It ignores the space and reads the next word into the same string"], "correct_answer": "It stops reading; cin uses whitespace as a delimiter", "explanation": "cin >> string only reads up to the first space. To read a full sentence with spaces, std::getline must be used.", "difficulty": "Hard"},
    {"question_text": "If an if statement has no curly braces {}, how many statements are considered part of the if block?", "options": ["None", "Exactly one (the immediately following statement)", "All statements until a blank line", "All statements until an else"], "correct_answer": "Exactly one (the immediately following statement)", "explanation": "Without braces, only the very next statement is bound to the if condition. This often causes hidden bugs during refactoring.", "difficulty": "Hard"},
    {"question_text": "What does the logical OR operator (||) do?", "options": ["Returns true only if both operands are true", "Returns true if at least one operand is true", "Returns true if both operands are false", "Reverses the boolean value"], "correct_answer": "Returns true if at least one operand is true", "explanation": "|| acts as a logical OR. It evaluates to true if either the left side, the right side, or both sides are true.", "difficulty": "Beginner"},
    {"question_text": "What is printed? `int x = 5; if(x = 10) cout << x;`", "options": ["5", "10", "Nothing", "Compiler error"], "correct_answer": "10", "explanation": "This is a classic trap. x = 10 ASSIGNS 10 to x. The assignment operation returns the value 10, which evaluates to true. So it prints 10.", "difficulty": "Hard"}
]

m4_lesson = """# Loops & Problem Solving

## What Is It?

A loop is a control flow structure that repeats a block of code as long as a specified condition remains true. 

C++ provides three main loop structures:
- `while`: Loops as long as a condition is true. Checked *before* execution.
- `do-while`: Executes *at least once*, then loops as long as a condition is true. Checked *after* execution.
- `for`: A compact loop designed for counting, bundling initialization, condition, and incrementing together.

## Why Do We Need It?

Without loops, performing a repetitive task requires copying and pasting code. If you need to print "Hello" 10,000 times, you would need 10,000 lines of code.

Loops allow us to write the logic once and tell the CPU to execute it repeatedly. They are the backbone of searching data, processing files, running game engines, and rendering graphics.

## Where Is It Used?

- Video Games: The main "Game Loop" constantly reads controller input, updates physics, and renders the screen 60 times a second.
- Data Processing: Reading thousands of lines from a CSV file.
- Servers: A web server constantly loops, waiting for incoming network requests.

## How Does It Work?

1. **Initialization**: Set up a counter variable (e.g., `int i = 0`).
2. **Condition**: Check if the loop should run (e.g., `i < 5`). If true, proceed. If false, exit the loop entirely.
3. **Execution**: Run the code inside the loop body.
4. **Update**: Modify the counter (e.g., `i++`).
5. Repeat from Step 2.

## Syntax

```cpp
// FOR LOOP
for (int i = 0; i < 5; i++) {
    // executes 5 times (0, 1, 2, 3, 4)
}

// WHILE LOOP
int count = 0;
while (count < 5) {
    // executes 5 times
    count++;
}
```

## Example 1 — Beginner (Counting)

```cpp
#include <iostream>

int main() {
    // Prints 1 through 5
    for (int i = 1; i <= 5; i++) {
        std::cout << "Count: " << i << std::endl;
    }
    return 0;
}
```

### Output

```text
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```

### Line-by-Line Explanation

1. `int i = 1`: Creates a loop variable `i` starting at 1.
2. `i <= 5`: The condition. As long as `i` is 5 or less, the loop runs.
3. `std::cout...`: Prints the current value of `i`.
4. `i++`: Increments `i` by 1 at the end of the block.

## Example 2 — Real World (Input Validation)

```cpp
#include <iostream>

int main() {
    int password;
    
    do {
        std::cout << "Enter the secret pin (1234): ";
        std::cin >> password;
    } while (password != 1234);

    std::cout << "Access Granted!" << std::endl;
    return 0;
}
```

### Output

```text
Enter the secret pin (1234): 9999
Enter the secret pin (1234): 0000
Enter the secret pin (1234): 1234
Access Granted!
```

### Explanation

We use a `do-while` loop because we *must* ask the user for their pin at least once. If they get it wrong (`password != 1234`), the loop repeats. It traps the user until they provide valid input.

## Common Mistakes

* **Infinite Loops**: Forgetting to update the loop variable (e.g., forgetting `count++`) means the condition will never become false. The program will freeze forever.
* **Off-by-One Errors**: Using `<=` instead of `<` when accessing arrays, causing the loop to run one time too many and crash the program.
* **Semicolon after the for loop**: `for(int i=0; i<5; i++);` — The semicolon creates an empty loop body. It counts to 5 and does nothing else.

## Best Practices

* Use `for` loops when you know exactly how many times you want to iterate.
* Use `while` loops when you are waiting for a condition to change (e.g., waiting for a network packet).
* Use `break` to escape a loop early, and `continue` to skip the rest of the current iteration and jump to the next one.

## Try It Yourself

Write a `for` loop that calculates the sum of all numbers from 1 to 100.
"""

m4_exercises = [
    {
        "title": "Sum of First N Numbers",
        "description": "Read an integer N. Calculate and print the sum of all integers from 1 to N using a loop.",
        "difficulty": "Easy",
        "concepts": "for loop, accumulators",
        "starter_code": "#include <iostream>\n\nint main() {\n    int n;\n    std::cin >> n;\n    int sum = 0;\n    // write loop here\n    std::cout << sum << std::endl;\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int n;\n    std::cin >> n;\n    int sum = 0;\n    for(int i = 1; i <= n; i++) {\n        sum += i;\n    }\n    std::cout << sum << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "5", "expected_output": "15\n"},
            {"input": "10", "expected_output": "55\n"},
            {"input": "100", "expected_output": "5050\n"}
        ]
    },
    {
        "title": "Multiplication Table",
        "description": "Read an integer. Print its multiplication table from 1 to 10 in the format `N x i = Result`.",
        "difficulty": "Easy",
        "concepts": "for loop",
        "starter_code": "#include <iostream>\n\nint main() {\n    int n;\n    std::cin >> n;\n    // loop 1 to 10\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int n;\n    std::cin >> n;\n    for(int i = 1; i <= 10; i++) {\n        std::cout << n << \" x \" << i << \" = \" << (n * i) << std::endl;\n    }\n    return 0;\n}\n",
        "test_cases": [
            {"input": "5", "expected_output": "5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n5 x 5 = 25\n5 x 6 = 30\n5 x 7 = 35\n5 x 8 = 40\n5 x 9 = 45\n5 x 10 = 50\n"}
        ]
    },
    {
        "title": "Factorial Calculator",
        "description": "Read a positive integer N. Calculate its factorial (N!). For example, 5! = 5 * 4 * 3 * 2 * 1 = 120.",
        "difficulty": "Medium",
        "concepts": "while loop, multiplication accumulator",
        "starter_code": "#include <iostream>\n\nint main() {\n    int n;\n    std::cin >> n;\n    long long fact = 1;\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int n;\n    std::cin >> n;\n    long long fact = 1;\n    for(int i = 1; i <= n; i++) {\n        fact *= i;\n    }\n    std::cout << fact << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "5", "expected_output": "120\n"},
            {"input": "0", "expected_output": "1\n"},
            {"input": "10", "expected_output": "3628800\n"}
        ]
    },
    {
        "title": "Prime Number Checker",
        "description": "Read a positive integer. Print `Prime` if it is a prime number, otherwise print `Not Prime`. (Note: 1 is not prime).",
        "difficulty": "Medium",
        "concepts": "loops, logic flags, modulo",
        "starter_code": "#include <iostream>\n\nint main() {\n    int n;\n    std::cin >> n;\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int n;\n    std::cin >> n;\n    if (n <= 1) {\n        std::cout << \"Not Prime\\n\";\n        return 0;\n    }\n    bool isPrime = true;\n    for(int i = 2; i * i <= n; i++) {\n        if (n % i == 0) {\n            isPrime = false;\n            break;\n        }\n    }\n    if (isPrime) std::cout << \"Prime\\n\";\n    else std::cout << \"Not Prime\\n\";\n    return 0;\n}\n",
        "test_cases": [
            {"input": "7", "expected_output": "Prime\n"},
            {"input": "10", "expected_output": "Not Prime\n"},
            {"input": "1", "expected_output": "Not Prime\n"},
            {"input": "97", "expected_output": "Prime\n"}
        ]
    },
    {
        "title": "Reverse a Number",
        "description": "Read an integer. Print the number with its digits reversed. For example, 12345 becomes 54321.",
        "difficulty": "Hard",
        "concepts": "while loop, digit extraction",
        "starter_code": "#include <iostream>\n\nint main() {\n    int n;\n    std::cin >> n;\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int n;\n    std::cin >> n;\n    int reversed = 0;\n    while (n > 0) {\n        int digit = n % 10;\n        reversed = (reversed * 10) + digit;\n        n /= 10;\n    }\n    std::cout << reversed << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "12345", "expected_output": "54321\n"},
            {"input": "100", "expected_output": "1\n"}
        ]
    },
    {
        "title": "Square Pattern",
        "description": "Read an integer N. Print an N x N square of asterisks (*).",
        "difficulty": "Hard",
        "concepts": "nested loops",
        "starter_code": "#include <iostream>\n\nint main() {\n    int n;\n    std::cin >> n;\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int n;\n    std::cin >> n;\n    for(int i=0; i<n; i++) {\n        for(int j=0; j<n; j++) {\n            std::cout << \"*\";\n        }\n        std::cout << std::endl;\n    }\n    return 0;\n}\n",
        "test_cases": [
            {"input": "3", "expected_output": "***\n***\n***\n"},
            {"input": "5", "expected_output": "*****\n*****\n*****\n*****\n*****\n"}
        ]
    },
    {
        "title": "Fibonacci Sequence",
        "description": "Read an integer N. Print the first N terms of the Fibonacci sequence, separated by spaces. The sequence starts 0 1 1 2 3 5...",
        "difficulty": "Challenge",
        "concepts": "sequence generation, state tracking",
        "starter_code": "#include <iostream>\n\nint main() {\n    int n;\n    std::cin >> n;\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int n;\n    std::cin >> n;\n    long long a = 0, b = 1;\n    for (int i = 0; i < n; i++) {\n        std::cout << a << \" \";\n        long long next = a + b;\n        a = b;\n        b = next;\n    }\n    std::cout << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "5", "expected_output": "0 1 1 2 3 \n"},
            {"input": "10", "expected_output": "0 1 1 2 3 5 8 13 21 34 \n"}
        ]
    }
]

m4_quizzes = [
    {"question_text": "What is an infinite loop?", "options": ["A loop that can process infinite data", "A loop whose termination condition never evaluates to false, causing the program to freeze or crash", "A loop running on the cloud", "A loop inside another loop"], "correct_answer": "A loop whose termination condition never evaluates to false, causing the program to freeze or crash", "explanation": "If a loop condition always remains true (e.g., forgetting to increment a counter), the CPU will execute the block forever.", "difficulty": "Beginner"},
    {"question_text": "Which loop is guaranteed to execute its body AT LEAST once, regardless of the condition?", "options": ["for loop", "while loop", "do-while loop", "infinite loop"], "correct_answer": "do-while loop", "explanation": "The do-while loop evaluates its condition at the BOTTOM of the loop, meaning the body executes before the first check.", "difficulty": "Beginner"},
    {"question_text": "In a for loop: `for(A; B; C)`, what does part B represent?", "options": ["Initialization", "The loop condition (evaluated before each iteration)", "The increment/decrement step", "The loop body"], "correct_answer": "The loop condition (evaluated before each iteration)", "explanation": "A is initialization, B is the condition that keeps the loop running, and C is the update step executed at the end of each iteration.", "difficulty": "Medium"},
    {"question_text": "What does the 'break' statement do inside a loop?", "options": ["Pauses the loop for 1 second", "Immediately terminates the loop entirely and jumps to the code following the loop", "Skips the current iteration and goes to the next one", "Restarts the loop from 0"], "correct_answer": "Immediately terminates the loop entirely and jumps to the code following the loop", "explanation": "break completely destroys the loop's execution context, breaking out of it immediately.", "difficulty": "Medium"},
    {"question_text": "What does the 'continue' statement do inside a loop?", "options": ["Pauses the loop", "Terminates the loop entirely", "Immediately skips the rest of the current iteration's body and jumps straight to the next iteration evaluation", "Does nothing"], "correct_answer": "Immediately skips the rest of the current iteration's body and jumps straight to the next iteration evaluation", "explanation": "continue is useful for bypassing specific iterations (like skipping even numbers) without destroying the entire loop.", "difficulty": "Medium"},
    {"question_text": "What is the output of this loop: `for(int i=0; i<3; i++) { if(i==1) continue; std::cout << i; }`", "options": ["012", "01", "02", "12"], "correct_answer": "02", "explanation": "When i is 1, 'continue' triggers, skipping the cout statement. Thus, only 0 and 2 are printed.", "difficulty": "Hard"},
    {"question_text": "What is a nested loop?", "options": ["A loop that runs infinitely", "A loop placed inside the body of another loop", "A loop that counts backwards", "A loop containing an if statement"], "correct_answer": "A loop placed inside the body of another loop", "explanation": "Nested loops (like a for loop inside a for loop) are critical for working with 2D matrices, images, and grids.", "difficulty": "Beginner"},
    {"question_text": "If an outer loop runs N times, and an inner loop runs M times, how many times does the inner loop body execute in total?", "options": ["N + M", "N", "M", "N * M"], "correct_answer": "N * M", "explanation": "For every single iteration of the outer loop, the inner loop executes completely. Thus, they multiply.", "difficulty": "Medium"},
    {"question_text": "What happens in a while loop if the condition is false initially?", "options": ["It executes once and then stops", "The compiler throws an error", "The loop body never executes at all", "It becomes an infinite loop"], "correct_answer": "The loop body never executes at all", "explanation": "A while loop checks its condition before executing. If it's false on the first check, it bypasses the block completely.", "difficulty": "Medium"},
    {"question_text": "What is the fundamental difference between extracting digits of a number (n % 10) versus dividing the number (n / 10)?", "options": ["They are the same", "Modulo extracts the last digit; integer division removes the last digit", "Modulo removes the first digit; division extracts it", "Modulo throws an error on negative numbers"], "correct_answer": "Modulo extracts the last digit; integer division removes the last digit", "explanation": "123 % 10 yields 3. 123 / 10 yields 12. Combining these in a while loop allows processing a number digit-by-digit.", "difficulty": "Hard"}
]


m5_lesson = """# Functions

## What Is It?

A function is a self-contained block of code designed to perform a specific task. You give it data (parameters), it does some work, and it optionally gives you data back (return value).

## Why Do We Need It?

Without functions, a program is just one giant block of code in `main()`. This leads to:
1. **Spaghetti Code**: Unreadable, unmanageable code.
2. **Duplication**: If you need to calculate a percentage in 10 different places, you have to copy-paste the math 10 times. If the formula changes, you must fix it in 10 places.

Functions allow **Modular Programming**. You write the logic once, name it, and call it as many times as you want.

## Where Is It Used?

- `std::cout` is a function.
- Math operations like `sqrt(25)` or `pow(2, 8)` are functions.
- Game physics engines have functions like `calculateGravity()`.

## How Does It Work?

1. **Declaration**: Tell the compiler the function's name, what it takes, and what it returns.
2. **Definition**: Write the actual code inside the function.
3. **Call**: In `main()`, invoke the function by its name and pass arguments to it.

When a function is called, the CPU pushes a "frame" onto the Call Stack. When the function finishes, that frame is popped off, and execution returns to where it left off.

## Syntax

```cpp
// ReturnType FunctionName(ParameterType parameterName)
int addNumbers(int a, int b) {
    return a + b;
}
```

## Example 1 — Beginner

```cpp
#include <iostream>

// Function Declaration & Definition
void greetUser(std::string name) {
    std::cout << "Hello, " << name << "!" << std::endl;
}

int main() {
    // Function Calls
    greetUser("Alice");
    greetUser("Bob");
    return 0;
}
```

### Output

```text
Hello, Alice!
Hello, Bob!
```

### Line-by-Line Explanation

1. `void`: Indicates this function does not return any data to the caller.
2. `greetUser(std::string name)`: The function requires a string argument to run.
3. In `main()`, we call it twice. The execution jumps to `greetUser`, runs the `cout`, and then jumps back.

## Example 2 — Real World (Pass by Reference)

```cpp
#include <iostream>

// The '&' means we are passing by REFERENCE, not by value.
void applyDiscount(double& price, double discount) {
    price = price - (price * discount);
}

int main() {
    double itemPrice = 100.0;
    
    // We pass the actual memory address of itemPrice
    applyDiscount(itemPrice, 0.20); // 20% discount
    
    std::cout << "Final Price: $" << itemPrice << std::endl;
    return 0;
}
```

### Output

```text
Final Price: $80
```

### Explanation

By default, C++ passes by **Value** (it makes a complete copy of the variable). If we modify the copy, the original is untouched. 
By adding `&` (Pass by **Reference**), we give the function direct access to the original variable in memory. Thus, the modification persists.

## Common Mistakes

* **Calling a function before it is declared**: C++ reads top-to-bottom. If you call `calculate()` in `main()` but define it below `main()`, the compiler will panic. You must put a declaration above `main()`.
* **Returning local variables by reference**: Never return a reference to a variable created inside a function. When the function ends, that variable is destroyed, and the reference points to dead memory.
* **Forgetting the return statement**: If a function promises to return an `int`, it must return an `int`.

## Best Practices

* Functions should do **exactly one thing**. Don't write a `calculateAndPrintAndSaveToFile()` function. 
* Use pass-by-reference-to-const (`const std::string& text`) for large objects to avoid the performance hit of copying data, while ensuring the function cannot modify the original.

## Try It Yourself

Write a function `int square(int x)` that returns the square of a number, and call it from `main()`.
"""

m5_exercises = [
    {
        "title": "Square of a Number",
        "description": "Write a function `square` that takes an integer and returns its square. Read an integer in `main`, call the function, and print the result.",
        "difficulty": "Easy",
        "concepts": "functions, return values",
        "starter_code": "#include <iostream>\n\n// Write square function here\n\nint main() {\n    int n;\n    std::cin >> n;\n    // call square and print\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint square(int x) {\n    return x * x;\n}\n\nint main() {\n    int n;\n    std::cin >> n;\n    std::cout << square(n) << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "5", "expected_output": "25\n"},
            {"input": "-4", "expected_output": "16\n"}
        ]
    },
    {
        "title": "Maximum of Three",
        "description": "Write a function `max3(int a, int b, int c)` that returns the largest of three integers.",
        "difficulty": "Easy",
        "concepts": "functions, logic",
        "starter_code": "#include <iostream>\n\n// Write max3 function here\n\nint main() {\n    int a, b, c;\n    std::cin >> a >> b >> c;\n    // call max3 and print\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint max3(int a, int b, int c) {\n    int max = a;\n    if (b > max) max = b;\n    if (c > max) max = c;\n    return max;\n}\n\nint main() {\n    int a, b, c;\n    std::cin >> a >> b >> c;\n    std::cout << max3(a, b, c) << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "10 50 30", "expected_output": "50\n"},
            {"input": "-5 -2 -10", "expected_output": "-2\n"}
        ]
    },
    {
        "title": "Pass by Reference Swap",
        "description": "Write a `void swapNumbers(int& a, int& b)` function that swaps the values of two integers. The main function will print them after calling your function.",
        "difficulty": "Medium",
        "concepts": "pass by reference",
        "starter_code": "#include <iostream>\n\n// Write swapNumbers here\n\nint main() {\n    int x, y;\n    std::cin >> x >> y;\n    swapNumbers(x, y);\n    std::cout << x << \" \" << y << std::endl;\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nvoid swapNumbers(int& a, int& b) {\n    int temp = a;\n    a = b;\n    b = temp;\n}\n\nint main() {\n    int x, y;\n    std::cin >> x >> y;\n    swapNumbers(x, y);\n    std::cout << x << \" \" << y << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "10 20", "expected_output": "20 10\n"},
            {"input": "99 1", "expected_output": "1 99\n"}
        ]
    },
    {
        "title": "Default Arguments",
        "description": "Write a function `printMessage` that takes a `std::string` and an `int times`. Set a default value of `1` for `times`. The function should print the string that many times, each on a new line.",
        "difficulty": "Medium",
        "concepts": "default parameters",
        "starter_code": "#include <iostream>\n#include <string>\n\n// Write printMessage here\n\nint main() {\n    printMessage(\"Hello\");\n    printMessage(\"C++\", 3);\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <string>\n\nvoid printMessage(std::string msg, int times = 1) {\n    for (int i = 0; i < times; i++) {\n        std::cout << msg << std::endl;\n    }\n}\n\nint main() {\n    printMessage(\"Hello\");\n    printMessage(\"C++\", 3);\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "Hello\nC++\nC++\nC++\n"}
        ]
    },
    {
        "title": "Function Overloading",
        "description": "Write two functions named `multiply`. One takes two `int`s and returns an `int`. The other takes two `double`s and returns a `double`.",
        "difficulty": "Hard",
        "concepts": "overloading",
        "starter_code": "#include <iostream>\n\n// Write overloaded multiply functions here\n\nint main() {\n    std::cout << multiply(5, 4) << std::endl;\n    std::cout << multiply(2.5, 4.0) << std::endl;\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint multiply(int a, int b) {\n    return a * b;\n}\n\ndouble multiply(double a, double b) {\n    return a * b;\n}\n\nint main() {\n    std::cout << multiply(5, 4) << std::endl;\n    std::cout << multiply(2.5, 4.0) << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "20\n10\n"}
        ]
    },
    {
        "title": "Factorial Recursion",
        "description": "Write a recursive function `int factorial(int n)` that calculates N!. A recursive function calls itself. Base case: if n <= 1, return 1.",
        "difficulty": "Challenge",
        "concepts": "recursion, call stack",
        "starter_code": "#include <iostream>\n\n// Write recursive factorial here\n\nint main() {\n    int n;\n    std::cin >> n;\n    std::cout << factorial(n) << std::endl;\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint factorial(int n) {\n    if (n <= 1) return 1;\n    return n * factorial(n - 1);\n}\n\nint main() {\n    int n;\n    std::cin >> n;\n    std::cout << factorial(n) << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "5", "expected_output": "120\n"},
            {"input": "1", "expected_output": "1\n"}
        ]
    }
]

m5_quizzes = [
    {"question_text": "What is the primary benefit of functions in programming?", "options": ["They make the program run significantly faster", "They eliminate the need for variables", "They allow code modularity, reusability, and easier debugging", "They prevent infinite loops"], "correct_answer": "They allow code modularity, reusability, and easier debugging", "explanation": "Functions prevent spaghetti code by breaking complex logic into manageable, reusable blocks.", "difficulty": "Beginner"},
    {"question_text": "What does a 'void' return type mean?", "options": ["The function returns an empty string", "The function does not return any data to the caller", "The function deletes variables", "The function crashes the program"], "correct_answer": "The function does not return any data to the caller", "explanation": "void literally means 'nothing'. The function performs an action (like printing) but yields no data back.", "difficulty": "Beginner"},
    {"question_text": "By default, how does C++ pass arguments to functions?", "options": ["Pass by reference", "Pass by pointer", "Pass by value (a full copy is made)", "Pass by constant"], "correct_answer": "Pass by value (a full copy is made)", "explanation": "Unless explicitly specified with '&', C++ copies the exact value of the variable into the function's local scope.", "difficulty": "Medium"},
    {"question_text": "What symbol is used to pass a variable by reference?", "options": ["*", "->", "&", "#"], "correct_answer": "&", "explanation": "Adding '&' to the parameter type (e.g., int& x) passes the actual memory address, allowing the function to modify the original variable.", "difficulty": "Medium"},
    {"question_text": "What is function overloading?", "options": ["Calling a function too many times, causing a stack overflow", "Creating multiple functions with the exact same name but different parameter types or counts", "Writing a function that is too long", "Overriding a base class method"], "correct_answer": "Creating multiple functions with the exact same name but different parameter types or counts", "explanation": "C++ allows functions to share a name (like 'print') as long as the compiler can distinguish them by their arguments.", "difficulty": "Medium"},
    {"question_text": "What is a recursive function?", "options": ["A function that returns a boolean", "A function that runs infinitely", "A function that calls itself inside its own body", "A function that deletes itself"], "correct_answer": "A function that calls itself inside its own body", "explanation": "Recursion involves a function calling itself to solve smaller sub-problems until it hits a base condition.", "difficulty": "Hard"},
    {"question_text": "What happens if a recursive function lacks a base case?", "options": ["It returns 0", "It runs perfectly", "It causes a Stack Overflow crash because it calls itself infinitely, exhausting RAM", "The compiler fixes it automatically"], "correct_answer": "It causes a Stack Overflow crash because it calls itself infinitely, exhausting RAM", "explanation": "Every function call consumes stack memory. Infinite recursion rapidly depletes this memory, crashing the process.", "difficulty": "Hard"},
    {"question_text": "Where must default arguments be placed in a function parameter list?", "options": ["At the very beginning", "At the very end (right-most parameters)", "Anywhere", "They are not allowed in C++"], "correct_answer": "At the very end (right-most parameters)", "explanation": "C++ requires all default arguments to trail non-default arguments so the compiler can reliably map provided arguments left-to-right.", "difficulty": "Medium"},
    {"question_text": "If you have `void calc(int a = 1, int b = 2)`, what happens if you call `calc(5)`?", "options": ["a=1, b=5", "a=5, b=2", "It throws a syntax error", "a=5, b=5"], "correct_answer": "a=5, b=2", "explanation": "The provided argument '5' is assigned to the first parameter 'a'. 'b' falls back to its default value '2'.", "difficulty": "Hard"},
    {"question_text": "What is the Call Stack?", "options": ["A data structure that tracks memory allocations on the heap", "A hidden structure that keeps track of active function calls, returning execution to the correct place when a function ends", "A library of standard functions", "An array of errors"], "correct_answer": "A hidden structure that keeps track of active function calls, returning execution to the correct place when a function ends", "explanation": "The stack pushes a frame every time a function is called, ensuring the CPU knows exactly where to resume execution.", "difficulty": "Hard"}
]

m6_lesson = """# Arrays, Strings & Vectors

## What Is It?

An Array is a contiguous block of memory that holds multiple variables of the same data type. 

Instead of declaring `int score1, score2, score3;`, you declare `int scores[3];`.

A `std::string` is essentially a dynamic array of characters managed for you.

A `std::vector` is a modern C++ data structure (part of the Standard Template Library). It acts like an array but **automatically resizes itself** when you add more elements.

## Why Do We Need It?

Imagine building a system to track the grades of 10,000 students. You cannot declare 10,000 individual variables. You need a data structure that groups them together under a single name, allowing you to use loops to process them.

Vectors are heavily preferred over raw arrays in modern C++ because raw arrays have a fixed size. If you make an array of size 10 and try to add an 11th element, the program crashes. Vectors grow dynamically.

## Where Is It Used?

- Video Games: Tracking a list of all active enemies on screen (using a `vector`).
- Data Processing: Storing the pixels of an image (using a 2D array).
- Text Processing: Storing user input, passwords, and file contents (using `string`).

## How Does It Work?

1. **Memory Allocation**: Arrays grab a sequential chunk of RAM. 
2. **0-Indexing**: The first element is always at index 0. If an array holds 5 elements, the valid indices are 0, 1, 2, 3, and 4.
3. **Vectors**: Under the hood, a vector is a pointer to an array. When it fills up, the vector asks the OS for a larger chunk of memory, copies the old data over, and deletes the old array.

## Syntax

```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
    // Fixed Array
    int ages[3] = {18, 20, 22};

    // String
    std::string name = "Alice";

    // Vector (Dynamic Array)
    std::vector<int> scores;
    scores.push_back(90); // Adds 90 to the end

    return 0;
}
```

## Example 1 — Raw Arrays

```cpp
#include <iostream>

int main() {
    int grades[4] = {85, 90, 78, 92};

    int sum = 0;
    for (int i = 0; i < 4; i++) {
        sum += grades[i];
    }

    std::cout << "Average: " << sum / 4.0 << std::endl;
    return 0;
}
```

### Output

```text
Average: 86.25
```

### Line-by-Line Explanation

1. `int grades[4]`: Asks the OS for 16 bytes (4 ints * 4 bytes) of contiguous RAM.
2. `grades[i]`: The `[]` operator calculates the memory address by taking the start of the array and shifting forward by `i` elements.

## Example 2 — Vectors (Modern C++)

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<std::string> inventory;

    // Add items
    inventory.push_back("Sword");
    inventory.push_back("Shield");
    inventory.push_back("Potion");

    // Print all items
    for (int i = 0; i < inventory.size(); i++) {
        std::cout << "Item: " << inventory[i] << std::endl;
    }

    // Remove the last item
    inventory.pop_back(); 

    std::cout << "Inventory size now: " << inventory.size() << std::endl;
    return 0;
}
```

### Output

```text
Item: Sword
Item: Shield
Item: Potion
Inventory size now: 2
```

### Explanation

Unlike raw arrays, we didn't specify a size for `inventory`. `push_back()` automatically handles memory resizing. `.size()` dynamically returns the current element count. This prevents massive bounds-checking bugs.

## Common Mistakes

* **Out-of-Bounds Access**: Array of size 5 has valid indices 0 to 4. Accessing `arr[5]` will read corrupt memory or cause a Segmentation Fault.
* **Returning local arrays from functions**: Arrays degrade into pointers. Returning a local array returns a pointer to dead memory.
* **Using C-style char arrays instead of `std::string`**: `char name[5] = "Bob"` forces you to manage null terminators manually. Use `std::string`.

## Best Practices

* Use `std::vector` instead of raw arrays for 99% of modern C++ development.
* Use `std::string` instead of raw `char[]`.
* If passing vectors to functions, pass by reference `void process(std::vector<int>& vec)` to avoid copying megabytes of memory.

## Try It Yourself

Create a vector of integers, add three numbers to it using `push_back`, and print the sum.
"""

m6_exercises = [
    {
        "title": "Raw Array Basics",
        "description": "Create an integer array of size 5 containing the numbers 10, 20, 30, 40, 50. Print the 3rd element.",
        "difficulty": "Easy",
        "concepts": "arrays, zero-indexing",
        "starter_code": "#include <iostream>\n\nint main() {\n    // create array and print\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int arr[5] = {10, 20, 30, 40, 50};\n    std::cout << arr[2] << std::endl;\n    return 0;\n}\n",
        "test_cases": [{"input": "", "expected_output": "30\n"}]
    },
    {
        "title": "Vector Basics",
        "description": "Read an integer N. Read N integers and store them in a `std::vector`. Finally, print the size of the vector.",
        "difficulty": "Easy",
        "concepts": "vector, push_back, size",
        "starter_code": "#include <iostream>\n#include <vector>\n\nint main() {\n    int n;\n    std::cin >> n;\n    std::vector<int> vec;\n    // read N times\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <vector>\n\nint main() {\n    int n;\n    std::cin >> n;\n    std::vector<int> vec;\n    for(int i = 0; i < n; i++) {\n        int val;\n        std::cin >> val;\n        vec.push_back(val);\n    }\n    std::cout << vec.size() << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "3 10 20 30", "expected_output": "3\n"}
        ]
    },
    {
        "title": "Search an Array",
        "description": "Read 5 integers into an array. Read a target integer. Print `Found` if the target is in the array, else print `Not Found`.",
        "difficulty": "Medium",
        "concepts": "array traversal, linear search",
        "starter_code": "#include <iostream>\n\nint main() {\n    int arr[5];\n    // read 5 elements\n    int target;\n    // read target\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int arr[5];\n    for(int i=0; i<5; i++) std::cin >> arr[i];\n    int target;\n    std::cin >> target;\n    bool found = false;\n    for(int i=0; i<5; i++) {\n        if(arr[i] == target) found = true;\n    }\n    if(found) std::cout << \"Found\\n\";\n    else std::cout << \"Not Found\\n\";\n    return 0;\n}\n",
        "test_cases": [
            {"input": "1 2 3 4 5 3", "expected_output": "Found\n"},
            {"input": "10 20 30 40 50 99", "expected_output": "Not Found\n"}
        ]
    },
    {
        "title": "String Reversal",
        "description": "Read a single word (`std::string`). Print the word in reverse order.",
        "difficulty": "Medium",
        "concepts": "std::string, reverse iteration",
        "starter_code": "#include <iostream>\n#include <string>\n\nint main() {\n    std::string str;\n    std::cin >> str;\n    // print in reverse\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <string>\n\nint main() {\n    std::string str;\n    std::cin >> str;\n    for(int i = str.length() - 1; i >= 0; i--) {\n        std::cout << str[i];\n    }\n    std::cout << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "hello", "expected_output": "olleh\n"},
            {"input": "C++", "expected_output": "++C\n"}
        ]
    },
    {
        "title": "Max Element in Vector",
        "description": "Read an integer N. Then read N integers into a vector. Find and print the maximum value in the vector.",
        "difficulty": "Hard",
        "concepts": "vector traversal, max algorithm",
        "starter_code": "#include <iostream>\n#include <vector>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <vector>\n\nint main() {\n    int n; std::cin >> n;\n    std::vector<int> vec;\n    for(int i=0; i<n; i++) {\n        int val; std::cin >> val;\n        vec.push_back(val);\n    }\n    if(n > 0) {\n        int max = vec[0];\n        for(int i=1; i<n; i++) {\n            if(vec[i] > max) max = vec[i];\n        }\n        std::cout << max << std::endl;\n    }\n    return 0;\n}\n",
        "test_cases": [
            {"input": "4 10 50 20 5", "expected_output": "50\n"}
        ]
    },
    {
        "title": "2D Array - Matrix Addition",
        "description": "Create two 2x2 matrices (read 4 integers for each). Add them together and print the resulting 2x2 matrix (row by row).",
        "difficulty": "Challenge",
        "concepts": "2D arrays, nested loops",
        "starter_code": "#include <iostream>\n\nint main() {\n    int m1[2][2], m2[2][2];\n    // read matrices\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int m1[2][2], m2[2][2];\n    for(int i=0; i<2; i++) for(int j=0; j<2; j++) std::cin >> m1[i][j];\n    for(int i=0; i<2; i++) for(int j=0; j<2; j++) std::cin >> m2[i][j];\n    \n    for(int i=0; i<2; i++) {\n        for(int j=0; j<2; j++) {\n            std::cout << m1[i][j] + m2[i][j] << \" \";\n        }\n        std::cout << std::endl;\n    }\n    return 0;\n}\n",
        "test_cases": [
            {"input": "1 2 3 4 5 6 7 8", "expected_output": "6 8 \n10 12 \n"}
        ]
    }
]

m6_quizzes = [
    {"question_text": "What is the index of the first element in a C++ array?", "options": ["1", "0", "-1", "It depends on the compiler"], "correct_answer": "0", "explanation": "C++ arrays are 0-indexed. The index actually represents an offset from the memory address of the first element.", "difficulty": "Beginner"},
    {"question_text": "What happens if you try to access arr[10] on an array declared as int arr[5]?", "options": ["The compiler expands the array automatically", "It returns NULL", "It causes undefined behavior, potentially reading corrupt memory or crashing (Segmentation Fault)", "It loops around to the beginning"], "correct_answer": "It causes undefined behavior, potentially reading corrupt memory or crashing (Segmentation Fault)", "explanation": "Raw C++ arrays do not perform bounds checking. Accessing out of bounds blindly reads random RAM.", "difficulty": "Medium"},
    {"question_text": "What is the primary advantage of std::vector over raw arrays?", "options": ["Vectors are much faster", "Vectors are built into the hardware", "Vectors automatically resize themselves in memory when elements are added", "Vectors use less memory"], "correct_answer": "Vectors automatically resize themselves in memory when elements are added", "explanation": "Vectors manage their own dynamic memory on the heap, growing seamlessly via push_back().", "difficulty": "Medium"},
    {"question_text": "Which method is used to add an element to the END of a std::vector?", "options": ["append()", "push_back()", "insert_end()", "add()"], "correct_answer": "push_back()", "explanation": "push_back() appends the element and handles resizing the underlying array if necessary.", "difficulty": "Beginner"},
    {"question_text": "What is a std::string fundamentally?", "options": ["A primitive hardware type", "An integer mapping to a dictionary", "A dynamic array of characters (chars) with built-in management functions", "A linked list of characters"], "correct_answer": "A dynamic array of characters (chars) with built-in management functions", "explanation": "std::string wraps a raw char array, abstracting away the pain of memory allocation and null terminators.", "difficulty": "Medium"},
    {"question_text": "How do you get the number of elements currently stored in a vector named 'vec'?", "options": ["length(vec)", "vec.size()", "sizeof(vec)", "vec.count"], "correct_answer": "vec.size()", "explanation": "The .size() member function returns the number of active elements in the vector.", "difficulty": "Beginner"},
    {"question_text": "If `std::vector<int> v(10);`, what is the initial size of the vector?", "options": ["0", "1", "10", "Undefined"], "correct_answer": "10", "explanation": "The constructor `vector<int> v(10)` pre-allocates and initializes the vector with 10 elements (all zeroes by default).", "difficulty": "Hard"},
    {"question_text": "What does vec.pop_back() do?", "options": ["Removes the first element", "Removes the last element", "Reverses the vector", "Clears the entire vector"], "correct_answer": "Removes the last element", "explanation": "pop_back() removes the final element, decreasing the vector's logical size by 1.", "difficulty": "Medium"},
    {"question_text": "Why should you pass a large vector to a function as `const std::vector<int>&`?", "options": ["To convert it to an array", "To allow the function to delete it", "To pass it by reference, avoiding the massive performance penalty of copying megabytes of data, while ensuring it is read-only", "Because it is required by syntax"], "correct_answer": "To pass it by reference, avoiding the massive performance penalty of copying megabytes of data, while ensuring it is read-only", "explanation": "Pass by value creates a full copy. Pass by reference (`&`) passes the address. `const` prevents modification.", "difficulty": "Hard"},
    {"question_text": "Can a 2D array (e.g., int matrix[3][3]) have different row lengths?", "options": ["Yes", "No, standard C++ 2D arrays must be perfectly rectangular", "Only if dynamically allocated", "Only if filled with zeroes"], "correct_answer": "No, standard C++ 2D arrays must be perfectly rectangular", "explanation": "A raw 2D array allocates a single rectangular block of contiguous memory. Jagged arrays require arrays of pointers or vector of vectors.", "difficulty": "Hard"}
]


m7_lesson = """# Pointers & References

## What Is It?

A **Pointer** is a variable that stores a *memory address*, rather than a standard value like `5` or `"Hello"`.
A **Reference** is an alias (an alternative name) for an existing variable.

## Why Do We Need It?

When you pass large objects (like a 3D Game Model) to a function, copying it by value consumes massive memory and CPU time. Pointers and references allow you to hand the function the "address" of the model, so the function can look at the original data directly.

Pointers are also the foundation of dynamic memory (the Heap) and Data Structures like Linked Lists and Trees.

## Where Is It Used?

- Hardware drivers: Writing directly to specific memory addresses on a graphics card.
- Game Engines: A Bullet object stores a pointer to the Player object so it knows who shot it.
- STL Vectors: Under the hood, vectors use pointers to manage their dynamically allocated memory blocks.

## How Does It Work?

Imagine memory as a giant wall of mailboxes. Each mailbox has a unique number (the address) and can hold something inside (the value).

```text
age = 20

Memory
+---------+
| Address | Value
+---------+
| 1000    | 20
+---------+
```

When you declare `int* ptr = &age;`, you are creating a new mailbox that stores the address `1000`.

```text
ptr = 1000

ptr
 |
 v
1000
 |
 v
20
```

- `&age`: Retrieves the address (1000).
- `ptr`: The pointer variable holding the address (1000).
- `*ptr`: **Dereferences** the pointer. It travels to address 1000 and grabs the value (20).

## Syntax

```cpp
int age = 20;

// Pointer
int* ptr = &age; 
// ptr holds the memory address of age

// Reference
int& ref = age;  
// ref is now literally just another name for age
```

## Example 1 — Beginner (Pointer Basics)

```cpp
#include <iostream>

int main() {
    int score = 95;
    int* ptr = &score; // ptr stores the address of score

    std::cout << "Score value: " << score << std::endl;
    std::cout << "Memory address of score: " << &score << std::endl;
    std::cout << "Value stored in ptr: " << ptr << std::endl;
    std::cout << "Value pointed to by ptr (*ptr): " << *ptr << std::endl;

    // Modifying via pointer
    *ptr = 100;
    std::cout << "New score value: " << score << std::endl;

    return 0;
}
```

### Output

```text
Score value: 95
Memory address of score: 0x7ffeefbff5bc
Value stored in ptr: 0x7ffeefbff5bc
Value pointed to by ptr (*ptr): 95
New score value: 100
```

### Line-by-Line Explanation

1. `&score`: Extracts the physical RAM address (printed in hexadecimal, like `0x7ffeef...`).
2. `int* ptr`: Declares a variable designed specifically to hold integer addresses.
3. `*ptr`: The dereference operator. It looks inside the address and interacts with the actual integer.
4. `*ptr = 100`: This changes the value at the address. Since `ptr` points to `score`, `score` becomes 100.

## Example 2 — Real World (References vs Pointers in Functions)

```cpp
#include <iostream>

// Pass by Pointer (Requires dereferencing)
void modifyPointer(int* p) {
    if (p != nullptr) {
        *p = 50;
    }
}

// Pass by Reference (Cleaner, safer)
void modifyReference(int& r) {
    r = 99;
}

int main() {
    int val = 10;

    modifyPointer(&val);
    std::cout << val << std::endl; // 50

    modifyReference(val);
    std::cout << val << std::endl; // 99

    return 0;
}
```

### Output

```text
50
99
```

### Explanation

References are generally preferred in modern C++ because they are guaranteed to refer to a valid object (you can't have a `null` reference), and the syntax is cleaner (no `*` or `&` needed when using them). Pointers are necessary when you might need to point to "nothing" (`nullptr`) or change what you are pointing to later.

## Common Mistakes

* **Dereferencing `nullptr` or an uninitialized pointer**: This causes an immediate Segmentation Fault crash.
* **Returning a pointer to a local variable**: The local variable is destroyed when the function ends, leaving a "dangling pointer" pointing to dead memory.
* **Confusing `*`**: In a declaration (`int* p`), it means "pointer type". In an expression (`*p = 5`), it means "dereference".

## Best Practices

* Always initialize pointers to `nullptr` if you don't have an address to give them yet.
* Prefer References over Pointers when passing arguments to functions, unless you specifically need the ability to pass "null".

## Try It Yourself

Declare a variable `double pi = 3.14;`. Create a pointer to it. Print the address, and then print the value by dereferencing the pointer.
"""

m7_exercises = [
    {
        "title": "Pointer Basics",
        "description": "Declare an integer variable with value 42. Create a pointer to it. Print the integer's value by dereferencing the pointer.",
        "difficulty": "Easy",
        "concepts": "pointers, dereferencing",
        "starter_code": "#include <iostream>\n\nint main() {\n    // your code\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int num = 42;\n    int* ptr = &num;\n    std::cout << *ptr << std::endl;\n    return 0;\n}\n",
        "test_cases": [{"input": "", "expected_output": "42\n"}]
    },
    {
        "title": "Swap with Pointers",
        "description": "Write a function `void swap(int* a, int* b)` that swaps the values. In `main`, declare two ints, read them, call swap, and print them.",
        "difficulty": "Easy",
        "concepts": "pointers, function arguments",
        "starter_code": "#include <iostream>\n\n// Write swap here\n\nint main() {\n    int x, y;\n    std::cin >> x >> y;\n    // call swap\n    std::cout << x << \" \" << y << std::endl;\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nvoid swap(int* a, int* b) {\n    int temp = *a;\n    *a = *b;\n    *b = temp;\n}\n\nint main() {\n    int x, y;\n    std::cin >> x >> y;\n    swap(&x, &y);\n    std::cout << x << \" \" << y << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "15 8", "expected_output": "8 15\n"}
        ]
    },
    {
        "title": "Reference Alias",
        "description": "Read an integer into `x`. Create a reference `r` to `x`. Multiply `r` by 2. Print `x`. Notice how changing `r` changes `x`.",
        "difficulty": "Medium",
        "concepts": "references",
        "starter_code": "#include <iostream>\n\nint main() {\n    int x;\n    std::cin >> x;\n    // create reference, modify, print\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int x;\n    std::cin >> x;\n    int& r = x;\n    r *= 2;\n    std::cout << x << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "50", "expected_output": "100\n"}
        ]
    },
    {
        "title": "Pointer to Array",
        "description": "Arrays decay to pointers. Read 3 integers into an array. Create a pointer to the array. Print the 2nd element using pointer arithmetic `*(ptr + 1)`.",
        "difficulty": "Medium",
        "concepts": "pointer arithmetic, array decay",
        "starter_code": "#include <iostream>\n\nint main() {\n    int arr[3];\n    std::cin >> arr[0] >> arr[1] >> arr[2];\n    // pointer and output\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int arr[3];\n    std::cin >> arr[0] >> arr[1] >> arr[2];\n    int* ptr = arr;\n    std::cout << *(ptr + 1) << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "100 200 300", "expected_output": "200\n"}
        ]
    },
    {
        "title": "Find Max via Pointers",
        "description": "Write a function `int* findMax(int* a, int* b)` that returns a pointer to the larger integer. Read two ints in main, call it, and dereference the result to print.",
        "difficulty": "Hard",
        "concepts": "returning pointers",
        "starter_code": "#include <iostream>\n\n// Write findMax here\n\nint main() {\n    int x, y;\n    std::cin >> x >> y;\n    // call and print\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint* findMax(int* a, int* b) {\n    if (*a > *b) return a;\n    return b;\n}\n\nint main() {\n    int x, y;\n    std::cin >> x >> y;\n    int* maxPtr = findMax(&x, &y);\n    std::cout << *maxPtr << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "99 150", "expected_output": "150\n"}
        ]
    },
    {
        "title": "Dangling Pointer Fix",
        "description": "The starter code returns a pointer to a local variable. This is a severe bug. Fix the function by returning a pointer to the static or heap variable, or simply pass by reference.",
        "difficulty": "Challenge",
        "concepts": "dangling pointers, scope",
        "starter_code": "#include <iostream>\n\n// FIX THIS:\nint* badFunction(int val) {\n    int local = val * 2;\n    return &local; \n}\n\nint main() {\n    int* result = badFunction(10);\n    std::cout << *result << std::endl;\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\n// Fixed by passing reference to output parameter\nvoid goodFunction(int val, int& out) {\n    out = val * 2;\n}\n\nint main() {\n    int result;\n    goodFunction(10, result);\n    std::cout << result << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "20\n"}
        ]
    }
]

m7_quizzes = [
    {"question_text": "What does a pointer store?", "options": ["An integer value", "A floating-point value", "The memory address of another variable", "A reference to a string"], "correct_answer": "The memory address of another variable", "explanation": "A pointer's sole purpose is to hold the physical or virtual RAM address of data, not the data itself.", "difficulty": "Beginner"},
    {"question_text": "Which operator is used to retrieve the memory address of a variable?", "options": ["* (dereference)", "& (address-of)", "% (modulo)", "-> (arrow)"], "correct_answer": "& (address-of)", "explanation": "The ampersand (&) asks the compiler for the address of the variable rather than its value.", "difficulty": "Beginner"},
    {"question_text": "What does the dereference operator (*) do?", "options": ["Multiplies the pointer by 2", "Follows the address stored in the pointer to access or modify the actual data living there", "Deletes the memory", "Nullifies the pointer"], "correct_answer": "Follows the address stored in the pointer to access or modify the actual data living there", "explanation": "Dereferencing '*ptr' allows you to 'look inside' the mailbox whose address the pointer holds.", "difficulty": "Medium"},
    {"question_text": "What is the difference between a pointer and a reference?", "options": ["They are exactly the same", "Pointers must be initialized immediately; references can be uninitialized", "Pointers can be reassigned to point elsewhere and can be null. References must be initialized immediately, cannot be null, and cannot be reassigned.", "References are for C, pointers are for C++"], "correct_answer": "Pointers can be reassigned to point elsewhere and can be null. References must be initialized immediately, cannot be null, and cannot be reassigned.", "explanation": "References are strict, permanent aliases. Pointers are independent variables that hold addresses and can be manipulated.", "difficulty": "Medium"},
    {"question_text": "What is a 'nullptr'?", "options": ["A pointer that holds the number 0", "A keyword explicitly indicating a pointer is empty and currently points to no valid memory", "A pointer that has been deleted", "A reference to a null string"], "correct_answer": "A keyword explicitly indicating a pointer is empty and currently points to no valid memory", "explanation": "nullptr is a type-safe way in modern C++ to signify that a pointer is deliberately pointing nowhere.", "difficulty": "Medium"},
    {"question_text": "What happens if you dereference an uninitialized pointer (`int* p; *p = 5;`)?", "options": ["The compiler safely creates an int for you", "The program ignores it", "The program attempts to write to a garbage address, usually resulting in a Segmentation Fault", "The pointer becomes nullptr automatically"], "correct_answer": "The program attempts to write to a garbage address, usually resulting in a Segmentation Fault", "explanation": "Uninitialized variables hold garbage. Using garbage as a memory address means you are writing to a random RAM location.", "difficulty": "Hard"},
    {"question_text": "If `int arr[5];`, what does the name `arr` evaluate to when passed to a function?", "options": ["The size of the array", "A full copy of the array", "A pointer to the first element (`&arr[0]`)", "The value of the first element"], "correct_answer": "A pointer to the first element (`&arr[0]`)", "explanation": "In C++, array names 'decay' into pointers to their 0th element. This is why arrays are not copied when passed to functions.", "difficulty": "Hard"},
    {"question_text": "If `int* ptr` points to an array, what does `ptr + 1` do?", "options": ["Adds 1 to the integer value", "Increments the address by 1 byte", "Increments the address by `sizeof(int)` bytes, pointing to the next element", "Moves the pointer to the end of the array"], "correct_answer": "Increments the address by `sizeof(int)` bytes, pointing to the next element", "explanation": "Pointer arithmetic is scaled by the type's size. Adding 1 to an int pointer moves it forward by 4 bytes (typically).", "difficulty": "Hard"},
    {"question_text": "What is a 'dangling pointer'?", "options": ["A pointer initialized to nullptr", "A pointer pointing to memory that has been freed or has gone out of scope", "A pointer that points to another pointer", "A pointer that is too large for the CPU"], "correct_answer": "A pointer pointing to memory that has been freed or has gone out of scope", "explanation": "Accessing a dangling pointer causes undefined behavior because the memory belongs to something else now.", "difficulty": "Medium"},
    {"question_text": "Can a reference be changed to alias a different variable after it is created?", "options": ["Yes, using the = operator", "Yes, using the & operator", "No, a reference is permanently bound to its initial variable", "Only inside a loop"], "correct_answer": "No, a reference is permanently bound to its initial variable", "explanation": "Once `int& ref = x;` is executed, `ref` is permanently tied to `x`. `ref = y;` just assigns the value of `y` into `x`.", "difficulty": "Hard"}
]

m8_lesson = """# Object-Oriented Programming (OOP)

## What Is It?

Object-Oriented Programming (OOP) is a programming paradigm built around the concept of "Objects". An Object is a container that holds both **Data** (attributes/variables) and **Behaviors** (methods/functions).

A **Class** is the blueprint. An **Object** is the actual thing built from that blueprint.

## Why Do We Need It?

Without OOP, data and the functions that manipulate that data are completely separate. If you are building a banking system, you have separate arrays for account numbers, names, and balances, and you have separate functions that take those arrays. It becomes chaotic.

OOP allows you to bundle everything into a `BankAccount` object. The object knows its own balance, and it has its own `deposit()` function. This maps programming directly to how we view the real world.

## Where Is It Used?

- GUI Applications: A `Button` class has `width`, `height`, and an `onClick()` method.
- Video Games: A `Zombie` class has `health` and a `bite()` method.
- Databases: A `User` class has `passwordHash` and a `login()` method.

## How Does It Work?

1. **Definition**: You write a `class` blueprint.
2. **Encapsulation**: You use Access Modifiers. `private` hides internal data from the outside world. `public` defines the interface others can use.
3. **Instantiation**: In `main()`, you create an instance of the class (the Object).
4. **Constructors**: Special functions that automatically run when the object is created to set up its initial state.

## Syntax

```cpp
class ClassName {
private:
    // hidden variables
public:
    // constructor
    ClassName() { ... }
    
    // accessible functions
    void method() { ... }
};
```

## Example 1 — Beginner (BankAccount)

```cpp
#include <iostream>
#include <string>

class BankAccount {
private:
    // Hidden internal state
    std::string owner;
    double balance;

public:
    // Constructor (called automatically when created)
    BankAccount(std::string name, double initialBalance) {
        owner = name;
        balance = initialBalance;
    }

    // Public method
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            std::cout << "Deposited $" << amount << std::endl;
        }
    }

    void printBalance() {
        std::cout << owner << "'s balance: $" << balance << std::endl;
    }
};

int main() {
    // Instantiating an object
    BankAccount myAccount("Alice", 100.0);
    
    myAccount.printBalance();
    myAccount.deposit(50.0);
    myAccount.printBalance();

    // myAccount.balance = 10000; // ERROR! balance is private.

    return 0;
}
```

### Output

```text
Alice's balance: $100
Deposited $50
Alice's balance: $150
```

### Line-by-Line Explanation

1. `private:`: The `balance` cannot be directly modified by `main()`. This prevents someone from maliciously writing `myAccount.balance = 999999;`.
2. `BankAccount(...)`: The Constructor. It has no return type and exactly matches the class name. It initializes the object.
3. `myAccount.deposit(...)`: We ask the object to modify its own data safely.

## Example 2 — Real World (Encapsulation)

```cpp
#include <iostream>

class Temperature {
private:
    double celsius;

public:
    // Setter (Mutator)
    void setCelsius(double c) {
        if (c < -273.15) {
            std::cout << "Error: Below absolute zero!" << std::endl;
        } else {
            celsius = c;
        }
    }

    // Getter (Accessor)
    double getFahrenheit() {
        return (celsius * 9.0 / 5.0) + 32.0;
    }
};

int main() {
    Temperature temp;
    temp.setCelsius(25.0);
    std::cout << "Fahrenheit: " << temp.getFahrenheit() << std::endl;
    
    temp.setCelsius(-300.0); // Safety check prevents this

    return 0;
}
```

### Output

```text
Fahrenheit: 77
Error: Below absolute zero!
```

### Explanation

This demonstrates **Encapsulation**. The class fiercely protects its internal state (`celsius`). It forces the outside world to go through a "Setter" function, which acts as a security guard to validate the data.

## Common Mistakes

* **Forgetting the semicolon at the end of the class**: `class MyClass { ... };` — The trailing semicolon is mandatory.
* **Making everything public**: If all variables are public, you lose the safety benefits of OOP. Use getters/setters.
* **Creating an object incorrectly**: `BankAccount acc();` does NOT create an object. It looks like a function declaration to the compiler. Use `BankAccount acc;` or `BankAccount acc("Name");`.

## Best Practices

* Keep data (`variables`) `private`.
* Keep methods (`functions`) `public` only if the outside world needs them.
* Use Constructors to ensure an object is always created in a valid state.

## Try It Yourself

Create a `Rectangle` class with `private` width and height. Add a constructor to set them, and a `public` method `getArea()` that returns the area.
"""

m8_exercises = [
    {
        "title": "Create a Class",
        "description": "Create a `Dog` class with a `public` method `bark()` that prints `Woof!`. Instantiate the class in `main()` and call the method.",
        "difficulty": "Easy",
        "concepts": "classes, objects, methods",
        "starter_code": "#include <iostream>\n\n// Write Dog class here\n\nint main() {\n    // create object and call bark\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nclass Dog {\npublic:\n    void bark() {\n        std::cout << \"Woof!\" << std::endl;\n    }\n};\n\nint main() {\n    Dog myDog;\n    myDog.bark();\n    return 0;\n}\n",
        "test_cases": [{"input": "", "expected_output": "Woof!\n"}]
    },
    {
        "title": "Rectangle Area",
        "description": "Create a `Rectangle` class. It should have `public` integers `width` and `height`, and a `getArea()` method. In main, read width and height, set them, and print the area.",
        "difficulty": "Easy",
        "concepts": "attributes, methods",
        "starter_code": "#include <iostream>\n\nclass Rectangle {\npublic:\n    int width;\n    int height;\n    // write getArea()\n};\n\nint main() {\n    int w, h;\n    std::cin >> w >> h;\n    // setup rectangle and print area\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nclass Rectangle {\npublic:\n    int width;\n    int height;\n    int getArea() {\n        return width * height;\n    }\n};\n\nint main() {\n    int w, h;\n    std::cin >> w >> h;\n    Rectangle rect;\n    rect.width = w;\n    rect.height = h;\n    std::cout << rect.getArea() << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "5 4", "expected_output": "20\n"},
            {"input": "10 10", "expected_output": "100\n"}
        ]
    },
    {
        "title": "Encapsulation & Setters",
        "description": "Update `Rectangle` to make `width` and `height` `private`. Create `public` methods `setWidth(int)` and `setHeight(int)`. If a negative value is passed, set it to 0. Print the area.",
        "difficulty": "Medium",
        "concepts": "private, setters, encapsulation",
        "starter_code": "#include <iostream>\n\nclass Rectangle {\nprivate:\n    int width;\n    int height;\npublic:\n    // write setters and getArea\n};\n\nint main() {\n    Rectangle rect;\n    int w, h;\n    std::cin >> w >> h;\n    // use setters and print area\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nclass Rectangle {\nprivate:\n    int width;\n    int height;\npublic:\n    void setWidth(int w) {\n        if (w < 0) width = 0; else width = w;\n    }\n    void setHeight(int h) {\n        if (h < 0) height = 0; else height = h;\n    }\n    int getArea() {\n        return width * height;\n    }\n};\n\nint main() {\n    Rectangle rect;\n    int w, h;\n    std::cin >> w >> h;\n    rect.setWidth(w);\n    rect.setHeight(h);\n    std::cout << rect.getArea() << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "5 5", "expected_output": "25\n"},
            {"input": "-5 10", "expected_output": "0\n"}
        ]
    },
    {
        "title": "Using a Constructor",
        "description": "Create a `Student` class. Make `name` (string) and `score` (int) private. Create a constructor that takes both. Add a `print()` method that outputs `Name: [name], Score: [score]`. In main, instantiate and call print.",
        "difficulty": "Medium",
        "concepts": "constructors",
        "starter_code": "#include <iostream>\n#include <string>\n\nclass Student {\n// write class\n};\n\nint main() {\n    std::string n;\n    int s;\n    std::cin >> n >> s;\n    // instantiate and print\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <string>\n\nclass Student {\nprivate:\n    std::string name;\n    int score;\npublic:\n    Student(std::string n, int s) {\n        name = n;\n        score = s;\n    }\n    void print() {\n        std::cout << \"Name: \" << name << \", Score: \" << score << std::endl;\n    }\n};\n\nint main() {\n    std::string n;\n    int s;\n    std::cin >> n >> s;\n    Student stu(n, s);\n    stu.print();\n    return 0;\n}\n",
        "test_cases": [
            {"input": "Alice 95", "expected_output": "Name: Alice, Score: 95\n"}
        ]
    },
    {
        "title": "Method Overloading",
        "description": "Add two `print()` methods to a `Message` class. One takes no parameters and prints `Default`. The other takes a `string` and prints that string.",
        "difficulty": "Hard",
        "concepts": "method overloading",
        "starter_code": "#include <iostream>\n#include <string>\n\n// Write Message class\n\nint main() {\n    Message m;\n    m.print();\n    m.print(\"Custom\");\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <string>\n\nclass Message {\npublic:\n    void print() {\n        std::cout << \"Default\" << std::endl;\n    }\n    void print(std::string text) {\n        std::cout << text << std::endl;\n    }\n};\n\nint main() {\n    Message m;\n    m.print();\n    m.print(\"Custom\");\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "Default\nCustom\n"}
        ]
    },
    {
        "title": "Destructor Demo",
        "description": "Create a `Connection` class. Its constructor should print `Connected`. It should have a Destructor `~Connection()` that prints `Disconnected`. Instantiate it in a block scope `{}` in main to see it destroyed automatically.",
        "difficulty": "Challenge",
        "concepts": "destructors, object lifecycle",
        "starter_code": "#include <iostream>\n\n// Write Connection class\n\nint main() {\n    std::cout << \"Start\" << std::endl;\n    {\n        Connection c;\n    }\n    std::cout << \"End\" << std::endl;\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nclass Connection {\npublic:\n    Connection() {\n        std::cout << \"Connected\" << std::endl;\n    }\n    ~Connection() {\n        std::cout << \"Disconnected\" << std::endl;\n    }\n};\n\nint main() {\n    std::cout << \"Start\" << std::endl;\n    {\n        Connection c;\n    }\n    std::cout << \"End\" << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "Start\nConnected\nDisconnected\nEnd\n"}
        ]
    }
]

m8_quizzes = [
    {"question_text": "What is the primary purpose of Object-Oriented Programming (OOP)?", "options": ["To make code run faster on the CPU", "To bundle data and the functions that operate on that data into single, cohesive 'Objects', mapping closely to real-world concepts", "To remove the need for pointers", "To allow programming without functions"], "correct_answer": "To bundle data and the functions that operate on that data into single, cohesive 'Objects', mapping closely to real-world concepts", "explanation": "OOP organizes complex software by creating self-contained modules (objects) that manage their own state and behavior.", "difficulty": "Beginner"},
    {"question_text": "What is the difference between a Class and an Object?", "options": ["They are synonyms", "A Class is the blueprint/template, an Object is the actual instance created from that blueprint", "A Class is a variable, an Object is a function", "An Object is a blueprint, a Class is the instance"], "correct_answer": "A Class is the blueprint/template, an Object is the actual instance created from that blueprint", "explanation": "You write a 'Car' class once. You instantiate multiple 'Car' objects (red car, blue car) in memory.", "difficulty": "Beginner"},
    {"question_text": "What does the 'private' access modifier do?", "options": ["Hides the variables/methods so they cannot be accessed or modified from outside the class", "Deletes the variables", "Makes the variables accessible to everyone", "Encrypts the data in memory"], "correct_answer": "Hides the variables/methods so they cannot be accessed or modified from outside the class", "explanation": "Private enforces encapsulation. Main() cannot directly touch a private variable; it must use a public method.", "difficulty": "Medium"},
    {"question_text": "What is Encapsulation?", "options": ["Writing all code in one file", "The concept of hiding the internal state of an object and requiring all interaction to occur through public methods", "Inheriting traits from a parent class", "Creating multiple objects"], "correct_answer": "The concept of hiding the internal state of an object and requiring all interaction to occur through public methods", "explanation": "Encapsulation protects the integrity of the object's data, preventing external code from putting it into an invalid state.", "difficulty": "Medium"},
    {"question_text": "What is a Constructor?", "options": ["A tool used to build the C++ compiler", "A special method that destroys the object", "A special method that is automatically called exactly once when an object is created, used for initialization", "A regular function that must be called manually"], "correct_answer": "A special method that is automatically called exactly once when an object is created, used for initialization", "explanation": "Constructors ensure that an object starts its life with valid data (e.g., setting starting balance to 0).", "difficulty": "Medium"},
    {"question_text": "How do you define a constructor for a class named `Player`?", "options": ["void Player()", "Player()", "init()", "constructor()"], "correct_answer": "Player()", "explanation": "A constructor has the exact same name as the class and strictly NO return type (not even void).", "difficulty": "Hard"},
    {"question_text": "What is a Destructor?", "options": ["A function that crashes the program", "A special method (starting with ~) that runs automatically when an object goes out of scope or is deleted, used for cleanup", "A tool to delete files", "A function to clear the console"], "correct_answer": "A special method (starting with ~) that runs automatically when an object goes out of scope or is deleted, used for cleanup", "explanation": "Destructors (e.g., ~Player()) are critical for releasing resources like open files or dynamic heap memory before the object dies.", "difficulty": "Hard"},
    {"question_text": "What does the 'this' keyword represent inside a class method?", "options": ["The current class blueprint", "A pointer to the specific object instance that invoked the method", "The main function", "A global variable"], "correct_answer": "A pointer to the specific object instance that invoked the method", "explanation": "'this' allows an object to refer to itself, often used to resolve naming conflicts between parameters and class attributes.", "difficulty": "Hard"},
    {"question_text": "Why is the trailing semicolon mandatory at the end of a class definition? `class A {};`", "options": ["Because C++ is an old language", "Because you can declare object instances immediately after the closing brace before the semicolon", "To indicate the end of the file", "It is actually optional"], "correct_answer": "Because you can declare object instances immediately after the closing brace before the semicolon", "explanation": "C/C++ allows syntax like `class A {} obj;`. Because of this, the compiler demands the semicolon to know the declaration is complete.", "difficulty": "Hard"},
    {"question_text": "If a class attribute is public, can it be accessed directly via `obj.attribute`?", "options": ["Yes, from anywhere", "No, only from within the class", "Only by child classes", "Only if it is a constant"], "correct_answer": "Yes, from anywhere", "explanation": "Public members break encapsulation and allow direct read/write access from main() or other functions.", "difficulty": "Beginner"}
]


m9_lesson = """# Inheritance & Polymorphism

## What Is It?

**Inheritance** allows one class (the Derived Class) to inherit all the attributes and methods of another class (the Base Class).
**Polymorphism** (meaning "many forms") allows functions to treat derived classes as if they were base classes, while still executing the derived class's unique behavior.

## Why Do We Need It?

Without inheritance, if you are coding a game with a `Zombie` and a `Vampire`, you would have to write `health`, `speed`, and `takeDamage()` twice. If you add a `Skeleton`, you write it a third time.

With inheritance, you create a base `Enemy` class containing `health` and `takeDamage()`. `Zombie` and `Vampire` just *inherit* from `Enemy` and only add what makes them unique.

Without polymorphism, you'd need separate arrays: `Zombie[] zombies` and `Vampire[] vampires`. With polymorphism, you can have one `Enemy* enemies[]` array, loop through it, and call `->attack()`. Each enemy will automatically use its correct attack!

## Where Is It Used?

- Game Engines: A `GameObject` base class is inherited by `Player`, `Enemy`, and `Prop`.
- UI Frameworks: A `Widget` base class is inherited by `Button`, `TextBox`, and `Label`.
- Simulators: A `Vehicle` base class is inherited by `Car` and `Airplane`.

## How Does It Work?

1. **Inheritance**: Defined using a colon `:`. e.g., `class Car : public Vehicle`.
2. **Virtual Functions**: By marking a base class method as `virtual`, you tell the compiler: "If a derived class overrides this method, use the derived version instead of mine, even if accessed through a base class pointer."
3. **Override**: The derived class rewrites the virtual function.

## Syntax

```cpp
class Base {
public:
    virtual void speak() {
        // base behavior
    }
};

class Derived : public Base {
public:
    void speak() override {
        // unique behavior
    }
};
```

## Example 1 — Beginner (Inheritance)

```cpp
#include <iostream>
#include <string>

// Base Class
class Animal {
public:
    std::string name;
    
    void sleep() {
        std::cout << name << " is sleeping (Zzz...)" << std::endl;
    }
};

// Derived Class
class Dog : public Animal {
public:
    void bark() {
        std::cout << name << " says Woof!" << std::endl;
    }
};

int main() {
    Dog myDog;
    myDog.name = "Rex"; // Inherited attribute
    myDog.sleep();      // Inherited method
    myDog.bark();       // Unique method
    
    return 0;
}
```

### Output

```text
Rex is sleeping (Zzz...)
Rex says Woof!
```

### Line-by-Line Explanation

1. `class Dog : public Animal`: Dog inherits from Animal.
2. `myDog.name`: Even though `name` wasn't explicitly written inside `Dog`, it exists because it was inherited from `Animal`.

## Example 2 — Real World (Polymorphism)

```cpp
#include <iostream>
#include <vector>

class Enemy {
public:
    // Virtual allows derived classes to override it dynamically
    virtual void attack() {
        std::cout << "Enemy attacks!" << std::endl;
    }
};

class Zombie : public Enemy {
public:
    void attack() override {
        std::cout << "Zombie bites you!" << std::endl;
    }
};

class Archer : public Enemy {
public:
    void attack() override {
        std::cout << "Archer shoots an arrow!" << std::endl;
    }
};

int main() {
    Zombie z;
    Archer a;
    
    // An array of base class pointers pointing to derived objects!
    std::vector<Enemy*> enemies;
    enemies.push_back(&z);
    enemies.push_back(&a);
    
    // Polymorphism in action
    for (int i = 0; i < enemies.size(); i++) {
        enemies[i]->attack();
    }
    
    return 0;
}
```

### Output

```text
Zombie bites you!
Archer shoots an arrow!
```

### Explanation

Even though the array thinks it is holding generic `Enemy*` pointers, when `attack()` is called, C++ looks at the actual object in memory. Because `attack()` is `virtual`, it dynamically routes the call to the correct `Zombie` or `Archer` method at runtime (Virtual Dispatch).

## Common Mistakes

* **Forgetting `virtual`**: If `attack()` wasn't virtual, the loop would print "Enemy attacks!" twice, completely ignoring the derived methods.
* **Inheriting `private` members**: Private members ARE inherited, but they are NOT directly accessible by the derived class. If `Animal` has private `health`, `Dog` cannot type `health = 100`. It must use a public/protected setter.
* **Slicing**: If you push objects into a `std::vector<Enemy>` (by value, not by pointer), they will be "sliced". The Zombie gets chopped down into a generic Enemy, losing its Zombie traits. Always use pointers/references for polymorphism.

## Best Practices

* Use `override` keyword when overriding a virtual method. It forces the compiler to check that you are actually overriding it properly.
* Base classes with virtual functions MUST have a `virtual` destructor to ensure derived classes are cleaned up properly.
* Use `protected` instead of `private` if you want derived classes to directly access base attributes.

## Try It Yourself

Create a `Shape` base class with a virtual `getArea()` method. Derive `Rectangle` and `Circle` from it.
"""

m9_exercises = [
    {
        "title": "Basic Inheritance",
        "description": "Create a `Vehicle` base class with `int speed`. Create a `Car` derived class with `void honk()` (prints `Beep`). Instantiate Car, set speed to 60, and call honk.",
        "difficulty": "Easy",
        "concepts": "inheritance",
        "starter_code": "#include <iostream>\n\n// classes\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nclass Vehicle {\npublic:\n    int speed;\n};\n\nclass Car : public Vehicle {\npublic:\n    void honk() {\n        std::cout << \"Beep\" << std::endl;\n    }\n};\n\nint main() {\n    Car c;\n    c.speed = 60;\n    c.honk();\n    std::cout << c.speed << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "Beep\n60\n"}
        ]
    },
    {
        "title": "Protected Access",
        "description": "Create `Person` with a `protected: int age`. Create `Student : public Person`. In Student, create `void setAge(int a)` and `void printAge()`. Use them in main.",
        "difficulty": "Easy",
        "concepts": "protected modifier",
        "starter_code": "#include <iostream>\n\n// classes\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nclass Person {\nprotected:\n    int age;\n};\n\nclass Student : public Person {\npublic:\n    void setAge(int a) {\n        age = a;\n    }\n    void printAge() {\n        std::cout << age << std::endl;\n    }\n};\n\nint main() {\n    Student s;\n    s.setAge(20);\n    s.printAge();\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "20\n"}
        ]
    },
    {
        "title": "Method Overriding",
        "description": "Create `Animal` with `virtual void speak() { cout << \"?\"; }`. Create `Cat` that overrides speak to print `Meow`. Call speak via a Cat object.",
        "difficulty": "Medium",
        "concepts": "override",
        "starter_code": "#include <iostream>\n\n// classes\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nclass Animal {\npublic:\n    virtual void speak() {\n        std::cout << \"?\\n\";\n    }\n};\n\nclass Cat : public Animal {\npublic:\n    void speak() override {\n        std::cout << \"Meow\\n\";\n    }\n};\n\nint main() {\n    Cat c;\n    c.speak();\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "Meow\n"}
        ]
    },
    {
        "title": "Polymorphism in Action",
        "description": "Following the previous exercise, in `main`, create an `Animal*` pointer. Point it to a `Cat` object. Call `ptr->speak()`. Ensure it prints `Meow` due to virtual dispatch.",
        "difficulty": "Medium",
        "concepts": "virtual dispatch, base pointers",
        "starter_code": "#include <iostream>\n\n// classes\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nclass Animal {\npublic:\n    virtual void speak() {\n        std::cout << \"?\\n\";\n    }\n};\n\nclass Cat : public Animal {\npublic:\n    void speak() override {\n        std::cout << \"Meow\\n\";\n    }\n};\n\nint main() {\n    Cat c;\n    Animal* ptr = &c;\n    ptr->speak();\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "Meow\n"}
        ]
    },
    {
        "title": "Constructor Calling Order",
        "description": "Create `Base` with a constructor that prints `Base built`. Create `Derived` with a constructor that prints `Derived built`. Instantiate `Derived`. Observe the output order.",
        "difficulty": "Hard",
        "concepts": "constructor inheritance",
        "starter_code": "#include <iostream>\n\n// classes\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nclass Base {\npublic:\n    Base() { std::cout << \"Base built\\n\"; }\n};\n\nclass Derived : public Base {\npublic:\n    Derived() { std::cout << \"Derived built\\n\"; }\n};\n\nint main() {\n    Derived d;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "Base built\nDerived built\n"}
        ]
    },
    {
        "title": "Pure Virtual (Abstract Class)",
        "description": "Create a `Shape` class with a pure virtual function `virtual void draw() = 0;`. You cannot instantiate it. Create `Square` that overrides draw to print `[ ]`. Instantiate Square and call draw.",
        "difficulty": "Challenge",
        "concepts": "abstract classes, pure virtual",
        "starter_code": "#include <iostream>\n\n// classes\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nclass Shape {\npublic:\n    virtual void draw() = 0;\n};\n\nclass Square : public Shape {\npublic:\n    void draw() override {\n        std::cout << \"[ ]\\n\";\n    }\n};\n\nint main() {\n    Square sq;\n    sq.draw();\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "[ ]\n"}
        ]
    }
]

m9_quizzes = [
    {"question_text": "What is Inheritance in OOP?", "options": ["Combining multiple objects into an array", "A mechanism where a new class acquires the properties and methods of an existing class", "Hiding variables from the user", "Deleting old classes"], "correct_answer": "A mechanism where a new class acquires the properties and methods of an existing class", "explanation": "Inheritance establishes an 'is-a' relationship (e.g., a Dog is an Animal), allowing code reuse.", "difficulty": "Beginner"},
    {"question_text": "Which access modifier allows derived classes to access a base class member, but keeps it hidden from the rest of the program (main)?", "options": ["public", "private", "protected", "virtual"], "correct_answer": "protected", "explanation": "Protected is the middle-ground. It acts like 'private' to the outside world, but like 'public' to child classes.", "difficulty": "Medium"},
    {"question_text": "If Class B inherits from Class A, what is the order of constructor execution when creating a Class B object?", "options": ["B runs, then A runs", "A runs, then B runs", "Only B runs", "They run simultaneously"], "correct_answer": "A runs, then B runs", "explanation": "The base (foundation) must be built before the derived (roof) can be added. Destructors run in the reverse order.", "difficulty": "Medium"},
    {"question_text": "What does the 'virtual' keyword do to a base class function?", "options": ["Makes the function run faster", "Deletes the function", "Enables runtime polymorphism, instructing the compiler to dynamically look up and execute the derived class's overridden version", "Prevents derived classes from overriding it"], "correct_answer": "Enables runtime polymorphism, instructing the compiler to dynamically look up and execute the derived class's overridden version", "explanation": "Without 'virtual', a base class pointer will blindly call the base class function, ignoring the actual object type.", "difficulty": "Hard"},
    {"question_text": "What is an Abstract Class in C++?", "options": ["A class with no variables", "A class containing at least one 'pure virtual' function (e.g., = 0), preventing it from being instantiated directly", "A class that only contains private methods", "A class that has been deleted"], "correct_answer": "A class containing at least one 'pure virtual' function (e.g., = 0), preventing it from being instantiated directly", "explanation": "Abstract classes serve strictly as interfaces/blueprints. You can't create an instance of a generic 'Shape', only specific shapes like 'Square'.", "difficulty": "Hard"},
    {"question_text": "What is the correct syntax for a pure virtual function?", "options": ["virtual void func();", "void func() pure;", "virtual void func() = 0;", "virtual 0 func();"], "correct_answer": "virtual void func() = 0;", "explanation": "The '= 0' syntax explicitly tells the compiler this function has no implementation in the base class and MUST be overridden.", "difficulty": "Medium"},
    {"question_text": "What does the 'override' keyword do?", "options": ["Forces the program to crash", "Nothing, it is just a comment", "Tells the compiler to verify that the function is genuinely overriding a virtual function from the base class, catching typo bugs", "Replaces the base class entirely"], "correct_answer": "Tells the compiler to verify that the function is genuinely overriding a virtual function from the base class, catching typo bugs", "explanation": "If you misspell 'update()' as 'updat()', the compiler will throw an error thanks to the 'override' keyword.", "difficulty": "Medium"},
    {"question_text": "What is 'Object Slicing'?", "options": ["Breaking an object into smaller objects", "When a derived object is copied into a base object variable (by value), 'slicing' off all derived-specific attributes and methods", "When a class inherits from two classes", "Deleting an object"], "correct_answer": "When a derived object is copied into a base object variable (by value), 'slicing' off all derived-specific attributes and methods", "explanation": "If you do `Base b = Derived();`, the compiler cuts away the Derived parts to fit it into the Base box. Always use pointers/references to prevent this.", "difficulty": "Hard"},
    {"question_text": "Why must base classes with virtual functions have a virtual destructor?", "options": ["To compile faster", "To ensure that deleting a derived object via a base pointer properly calls the derived destructor, preventing memory leaks", "Because all functions must be virtual", "To hide the data"], "correct_answer": "To ensure that deleting a derived object via a base pointer properly calls the derived destructor, preventing memory leaks", "explanation": "If `delete basePtr;` is called and the destructor isn't virtual, only the Base destructor runs. The Derived part leaks.", "difficulty": "Hard"},
    {"question_text": "What is Multiple Inheritance?", "options": ["A class having multiple functions", "A single class inheriting from more than one base class simultaneously (e.g., class FlyingCar : public Car, public Airplane)", "Inheriting the same class twice", "Creating an array of classes"], "correct_answer": "A single class inheriting from more than one base class simultaneously (e.g., class FlyingCar : public Car, public Airplane)", "explanation": "C++ supports multiple inheritance, allowing extreme flexibility, though it can lead to complexity (like the Diamond Problem).", "difficulty": "Beginner"}
]

m10_lesson = """# Advanced OOP & Operator Overloading

## What Is It?

Advanced OOP involves deep memory management rules, combining objects (Composition), and redefining how standard operators (`+`, `-`, `==`) work with your custom classes.

**Operator Overloading** allows you to make `Vector2D a + Vector2D b` work intuitively, rather than calling `a.add(b)`.

The **Rule of Three** (and Rule of Five in modern C++) dictates how you must handle copying and destroying objects if your class manually manages dynamic heap memory.

## Why Do We Need It?

When you create a class that uses `new` to allocate heap memory, standard C++ behavior becomes extremely dangerous. If you copy the object (`Object B = A`), C++ performs a "Shallow Copy". Both objects now point to the exact same RAM address. When they are destroyed, the program attempts to `delete` the same memory twice, causing a fatal crash.

You must implement Custom Copy Constructors and Assignment Operators (Deep Copies) to prevent this.

## Where Is It Used?

- Math Libraries: Overloading `*` so you can multiply `Matrix * Matrix` easily.
- Custom String Classes: Handling dynamic character arrays safely.
- Game Engines: Composing a `Player` out of `HealthComponent` and `PhysicsComponent`.

## How Does It Work?

1. **Operator Overloading**: You write a function named `operator+`. When the compiler sees `A + B`, it calls `A.operator+(B)`.
2. **Copy Constructor**: Automatically called when an object is created as a copy of another. `MyClass B = A;`
3. **Deep Copy**: Inside the copy constructor, you allocate *new* memory and copy the actual data over, rather than just copying the pointer address.

## Syntax (Operator Overloading)

```cpp
class Vector2D {
public:
    int x, y;
    
    // Overloading the + operator
    Vector2D operator+(const Vector2D& other) {
        Vector2D result;
        result.x = this->x + other.x;
        result.y = this->y + other.y;
        return result;
    }
};
```

## Example 1 — Beginner (Operator Overloading)

```cpp
#include <iostream>

class Score {
public:
    int points;
    
    Score(int p) { points = p; }

    // Overload the + operator
    Score operator+(const Score& rhs) {
        return Score(this->points + rhs.points);
    }
};

int main() {
    Score p1(10);
    Score p2(20);
    
    // Looks like normal math!
    Score total = p1 + p2;
    
    std::cout << "Total: " << total.points << std::endl;
    return 0;
}
```

### Output

```text
Total: 30
```

### Line-by-Line Explanation

1. `Score operator+(const Score& rhs)`: We define what `+` means. `rhs` stands for Right Hand Side.
2. `p1 + p2`: The compiler translates this to `p1.operator+(p2)`.
3. It creates and returns a new `Score` object with the summed points.

## Example 2 — Real World (The Danger of Shallow Copies)

```cpp
#include <iostream>

class DynamicArray {
public:
    int* data;
    
    DynamicArray(int val) {
        data = new int; // Allocate heap memory
        *data = val;
    }

    // THE FIX: Deep Copy Constructor
    DynamicArray(const DynamicArray& other) {
        data = new int; // Allocate NEW memory
        *data = *(other.data); // Copy the value, not the address
    }

    ~DynamicArray() {
        delete data; // Free memory
    }
};

int main() {
    DynamicArray arr1(50);
    
    // Uses the Copy Constructor
    DynamicArray arr2 = arr1; 
    
    // If we didn't have a Deep Copy Constructor, 
    // arr1 and arr2 would point to the same memory.
    // When main() ends, both destructors run, crashing the program!
    
    std::cout << "arr2 value: " << *(arr2.data) << std::endl;
    return 0;
}
```

### Output

```text
arr2 value: 50
```

### Explanation

By default, C++ does a "shallow copy", just copying the memory addresses. If both `arr1` and `arr2` share the exact same `data` pointer, the destructor will call `delete` on it twice (Double-Free Error). The Custom Copy Constructor forces a "Deep Copy", allocating fresh, separate memory.

## Common Mistakes

* **Forgetting to return a value in an operator overload**: `operator+` must return the new resulting object.
* **Double Free Error**: Failing to implement the Rule of Three when managing dynamic memory.
* **Overusing Operator Overloading**: Don't overload `+` to do subtraction. It makes code impossible to read.

## Best Practices

* **The Rule of Three**: If your class needs a custom Destructor (to delete memory), it almost certainly needs a custom Copy Constructor and a custom Copy Assignment Operator (`operator=`).
* Use `const` references (`const MyClass& rhs`) in operator overloading to prevent unnecessary copying and accidental modification.

## Try It Yourself

Overload the `==` operator for the `Score` class to return `true` if their points are equal.
"""

m10_exercises = [
    {
        "title": "Overload Addition",
        "description": "Create a `Point` class with `int x, y`. Overload the `+` operator to add two points together. Print the resulting x and y.",
        "difficulty": "Easy",
        "concepts": "operator overloading",
        "starter_code": "#include <iostream>\n\nclass Point {\npublic:\n    int x, y;\n    // overload +\n};\n\nint main() {\n    Point p1; p1.x=5; p1.y=10;\n    Point p2; p2.x=3; p2.y=4;\n    // add and print\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nclass Point {\npublic:\n    int x, y;\n    Point operator+(const Point& other) {\n        Point res;\n        res.x = x + other.x;\n        res.y = y + other.y;\n        return res;\n    }\n};\n\nint main() {\n    Point p1; p1.x=5; p1.y=10;\n    Point p2; p2.x=3; p2.y=4;\n    Point p3 = p1 + p2;\n    std::cout << p3.x << \" \" << p3.y << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "8 14\n"}
        ]
    },
    {
        "title": "Overload Equality",
        "description": "In the `Point` class, overload the `==` operator to return `bool true` if both x and y are identical. Print `Equal` or `Not Equal`.",
        "difficulty": "Easy",
        "concepts": "operator overloading",
        "starter_code": "#include <iostream>\n\nclass Point {\npublic:\n    int x, y;\n    // overload ==\n};\n\nint main() {\n    Point p1; p1.x=5; p1.y=10;\n    Point p2; p2.x=5; p2.y=10;\n    // check equality\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nclass Point {\npublic:\n    int x, y;\n    bool operator==(const Point& other) {\n        return (x == other.x && y == other.y);\n    }\n};\n\nint main() {\n    Point p1; p1.x=5; p1.y=10;\n    Point p2; p2.x=5; p2.y=10;\n    if (p1 == p2) std::cout << \"Equal\\n\";\n    else std::cout << \"Not Equal\\n\";\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "Equal\n"}
        ]
    },
    {
        "title": "Composition",
        "description": "Create an `Engine` class with `void start() { cout << \"Vroom\\n\"; }`. Create a `Car` class that CONTAINS an `Engine` as an attribute. Call `engine.start()` from inside `Car`'s `drive()` method.",
        "difficulty": "Medium",
        "concepts": "composition",
        "starter_code": "#include <iostream>\n\n// classes\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nclass Engine {\npublic:\n    void start() { std::cout << \"Vroom\\n\"; }\n};\n\nclass Car {\nprivate:\n    Engine engine;\npublic:\n    void drive() {\n        engine.start();\n    }\n};\n\nint main() {\n    Car c;\n    c.drive();\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "Vroom\n"}
        ]
    },
    {
        "title": "Static Members",
        "description": "Create a `User` class. Add a `static int totalUsers` that increments in the constructor. Instantiate 3 users and print `totalUsers`.",
        "difficulty": "Medium",
        "concepts": "static",
        "starter_code": "#include <iostream>\n\nclass User {\npublic:\n    static int totalUsers;\n    // constructor\n};\n\nint User::totalUsers = 0;\n\nint main() {\n    // code\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nclass User {\npublic:\n    static int totalUsers;\n    User() {\n        totalUsers++;\n    }\n};\n\nint User::totalUsers = 0;\n\nint main() {\n    User u1;\n    User u2;\n    User u3;\n    std::cout << User::totalUsers << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "3\n"}
        ]
    },
    {
        "title": "Deep Copy Required",
        "description": "Fix the shallow copy bug. Add a deep Copy Constructor to `Buffer` that allocates new memory for `data`.",
        "difficulty": "Hard",
        "concepts": "copy constructor, deep copy",
        "starter_code": "#include <iostream>\n\nclass Buffer {\npublic:\n    int* data;\n    Buffer(int val) {\n        data = new int;\n        *data = val;\n    }\n    // WRITE COPY CONSTRUCTOR HERE\n\n    ~Buffer() { delete data; }\n};\n\nint main() {\n    Buffer b1(99);\n    Buffer b2 = b1;\n    *b2.data = 42;\n    std::cout << *b1.data << \" \" << *b2.data << std::endl;\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nclass Buffer {\npublic:\n    int* data;\n    Buffer(int val) {\n        data = new int;\n        *data = val;\n    }\n    \n    Buffer(const Buffer& other) {\n        data = new int;\n        *data = *(other.data);\n    }\n\n    ~Buffer() { delete data; }\n};\n\nint main() {\n    Buffer b1(99);\n    Buffer b2 = b1;\n    *b2.data = 42;\n    std::cout << *b1.data << \" \" << *b2.data << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "99 42\n"}
        ]
    },
    {
        "title": "Friend Function",
        "description": "Create a `Vault` class with a private `int secret = 777`. Declare a `friend void reveal(Vault& v);`. In the global reveal function, print the secret.",
        "difficulty": "Challenge",
        "concepts": "friend keyword",
        "starter_code": "#include <iostream>\n\n// classes and friend function\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nclass Vault {\nprivate:\n    int secret = 777;\n    friend void reveal(Vault& v);\n};\n\nvoid reveal(Vault& v) {\n    std::cout << v.secret << std::endl;\n}\n\nint main() {\n    Vault v;\n    reveal(v);\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "777\n"}
        ]
    }
]

m10_quizzes = [
    {"question_text": "What does Operator Overloading allow you to do?", "options": ["Speed up the CPU clock", "Create new operators that don't exist in C++ (like **)", "Redefine the behavior of existing C++ operators (like +, -, ==) so they work with your custom classes", "Bypass private access modifiers"], "correct_answer": "Redefine the behavior of existing C++ operators (like +, -, ==) so they work with your custom classes", "explanation": "Operator overloading allows custom objects to act like built-in types, making code highly readable.", "difficulty": "Beginner"},
    {"question_text": "How do you define an overload for the + operator?", "options": ["void plus()", "MyClass operator+(const MyClass& other)", "MyClass add(+)", "operator(+)(MyClass)"], "correct_answer": "MyClass operator+(const MyClass& other)", "explanation": "The 'operator' keyword followed by the symbol defines the overload. It typically takes the Right Hand Side as a parameter.", "difficulty": "Medium"},
    {"question_text": "What is a 'Shallow Copy'?", "options": ["Copying a variable but only storing half of its bits", "Copying an object's variables exactly as they are, which means pointer variables will just copy the memory address (pointing to the same shared memory)", "Creating a new object with empty data", "Copying an object securely"], "correct_answer": "Copying an object's variables exactly as they are, which means pointer variables will just copy the memory address (pointing to the same shared memory)", "explanation": "Shallow copies are dangerous for dynamic memory because two objects end up trying to delete the same memory location.", "difficulty": "Hard"},
    {"question_text": "What is a 'Deep Copy'?", "options": ["Copying data from a hard drive", "Allocating brand new dynamic memory for the new object and copying the ACTUAL VALUES over, ensuring both objects have independent memory", "Copying memory into the cache", "A copy that takes a long time"], "correct_answer": "Allocating brand new dynamic memory for the new object and copying the ACTUAL VALUES over, ensuring both objects have independent memory", "explanation": "A deep copy ensures complete independence. Destroying one object does not destroy the memory of the other.", "difficulty": "Hard"},
    {"question_text": "What is the 'Rule of Three' in C++?", "options": ["Variables must be 3 letters long", "Every class must have 3 methods", "If a class requires a custom Destructor, it almost certainly requires a custom Copy Constructor and Copy Assignment Operator to manage dynamic memory safely", "A program must be compiled 3 times"], "correct_answer": "If a class requires a custom Destructor, it almost certainly requires a custom Copy Constructor and Copy Assignment Operator to manage dynamic memory safely", "explanation": "If you are deleting memory in the destructor, you are manually managing resources, meaning default shallow copies will break your code.", "difficulty": "Medium"},
    {"question_text": "What does a 'static' class attribute mean?", "options": ["It cannot be changed", "It is stored on the hard drive", "The attribute is shared across ALL objects of that class, existing independently of any specific instance", "It is only accessible from main()"], "correct_answer": "The attribute is shared across ALL objects of that class, existing independently of any specific instance", "explanation": "Static members belong to the Class blueprint itself, not the objects. If one object changes it, it changes for all of them.", "difficulty": "Medium"},
    {"question_text": "What is 'Composition' in OOP?", "options": ["Writing code with good comments", "Building complex classes by including other classes as member variables (e.g., a Car HAS-A Engine)", "Inheriting from multiple classes", "Compressing the source code"], "correct_answer": "Building complex classes by including other classes as member variables (e.g., a Car HAS-A Engine)", "explanation": "Composition represents a 'HAS-A' relationship, which is often preferred over deep inheritance hierarchies.", "difficulty": "Beginner"},
    {"question_text": "What does the 'friend' keyword do?", "options": ["Makes two variables equal", "Grants an external function or class full access to the private and protected members of the class granting the friendship", "Sends a network request", "Prevents an object from being deleted"], "correct_answer": "Grants an external function or class full access to the private and protected members of the class granting the friendship", "explanation": "Friendship breaks encapsulation selectively, allowing tightly coupled utility functions to access private data.", "difficulty": "Hard"},
    {"question_text": "When is a Copy Constructor called automatically?", "options": ["When an object is deleted", "When an object is passed by reference", "When a new object is initialized using an existing object of the same class (`MyClass B = A;`)", "When two objects are added together"], "correct_answer": "When a new object is initialized using an existing object of the same class (`MyClass B = A;`)", "explanation": "The compiler uses the copy constructor to build B identically to A at the exact moment B is created.", "difficulty": "Medium"},
    {"question_text": "Which operator is typically overloaded to implement custom printing of an object via std::cout?", "options": ["+", "<<", ">>", "print"], "correct_answer": "<<", "explanation": "Overloading the bitwise left-shift operator (<<) as a friend function allows seamless integration with iostream (`cout << myObject`).", "difficulty": "Hard"}
]


m11_lesson = """# Templates & Exception Handling

## What Is It?

**Templates** allow you to write a function or class once, and have it work with ANY data type (`int`, `double`, `std::string`, or custom objects). It is the backbone of C++ Generic Programming.

**Exception Handling** is a structured way to handle runtime errors (like dividing by zero, or failing to open a file) without crashing the program, using `try`, `catch`, and `throw`.

## Why Do We Need It?

Without Templates, if you want a `max()` function for `int`, you write one. Then if you need it for `double`, you have to write a second overloaded one. If you need it for `char`, a third. Templates tell the compiler to generate these automatically on demand.

Without Exception Handling, errors crash the program silently, or force you to use messy `if (error_code == -1)` checks everywhere. Exceptions "throw" the error up the call stack until a `catch` block catches and resolves it safely.

## Where Is It Used?

- The entire C++ Standard Template Library (`std::vector<int>`, `std::vector<string>`) relies exclusively on templates.
- Web Servers: If a network packet fails, the server *throws* an exception, catches it, logs the error, and keeps running instead of crashing.
- Database Drivers: Throwing exceptions when the connection drops.

## How Does It Work?

1. **Templates**: You define a placeholder type (usually `T`). When you call `max<int>(5, 10)`, the compiler secretly writes a version of the function replacing `T` with `int` and compiles it.
2. **Exceptions**: Code that might fail is placed in a `try { }` block. If it fails, it executes a `throw` statement. Execution immediately halts and jumps down to the matching `catch { }` block.

## Syntax (Templates)

```cpp
template <typename T>
T getMaximum(T a, T b) {
    if (a > b) return a;
    return b;
}
```

## Syntax (Exceptions)

```cpp
try {
    // risky code
    throw std::runtime_error("Something broke!");
} catch (const std::exception& e) {
    // handle the error
    std::cout << e.what() << std::endl;
}
```

## Example 1 — Beginner (Function Templates)

```cpp
#include <iostream>

template <typename T>
T add(T a, T b) {
    return a + b;
}

int main() {
    // The compiler generates an int version
    std::cout << add<int>(5, 10) << std::endl;
    
    // The compiler generates a double version
    std::cout << add<double>(5.5, 2.2) << std::endl;
    
    // The compiler deduces the type automatically here!
    std::cout << add(100.1, 200.2) << std::endl;
    
    return 0;
}
```

### Output

```text
15
7.7
300.3
```

### Line-by-Line Explanation

1. `template <typename T>`: Tells the compiler that `T` is a generic type placeholder.
2. `add<int>(5, 10)`: We explicitly tell the compiler to build and execute the function replacing `T` with `int`.

## Example 2 — Real World (Exception Handling)

```cpp
#include <iostream>
#include <stdexcept>

double divide(double numerator, double denominator) {
    if (denominator == 0) {
        // Halt execution and throw an error object
        throw std::invalid_argument("Division by zero error!");
    }
    return numerator / denominator;
}

int main() {
    try {
        std::cout << "Result: " << divide(10.0, 2.0) << std::endl;
        std::cout << "Result: " << divide(5.0, 0.0) << std::endl;
        std::cout << "This line will never print." << std::endl;
    } 
    catch (const std::invalid_argument& e) {
        // We caught the specific error!
        std::cout << "CAUGHT EXCEPTION: " << e.what() << std::endl;
    }
    
    std::cout << "Program continues safely..." << std::endl;
    return 0;
}
```

### Output

```text
Result: 5
CAUGHT EXCEPTION: Division by zero error!
Program continues safely...
```

### Explanation

When `divide(5.0, 0.0)` is called, the `throw` statement executes. It acts like an emergency exit. It immediately ejects from the `divide()` function, ignores the next `cout`, and lands directly in the `catch` block. Because we handled it, the program doesn't crash.

## Common Mistakes

* **Putting template definitions in a `.cpp` file**: Because templates are generated on demand by the compiler, the compiler must see the full implementation when it is instantiated. Template definitions usually must go entirely in the `.h` header file.
* **Catching by value**: `catch (std::exception e)` creates an expensive copy of the error. Always catch by const reference: `catch (const std::exception& e)`.
* **Not catching an exception**: If an exception is thrown and no `catch` block exists anywhere in the call stack, the OS violently kills the program (`std::terminate`).

## Best Practices

* Use `<stdexcept>` classes (like `std::runtime_error`, `std::invalid_argument`, `std::out_of_range`) rather than throwing raw integers or strings.
* Only use exceptions for *exceptional* (rare) failures, not for normal control flow, because throwing exceptions has a performance cost.

## Try It Yourself

Write a generic template function `template <typename T> void printTwice(T val)` that prints the provided value twice on the same line.
"""

m11_exercises = [
    {
        "title": "Template Function",
        "description": "Write a template function `T multiply(T a, T b)`. In main, call it with two `int`s and then with two `double`s. Print both results.",
        "difficulty": "Easy",
        "concepts": "templates",
        "starter_code": "#include <iostream>\n\n// template here\n\nint main() {\n    // code\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\ntemplate <typename T>\nT multiply(T a, T b) {\n    return a * b;\n}\n\nint main() {\n    int ix, iy; std::cin >> ix >> iy;\n    double dx, dy; std::cin >> dx >> dy;\n    std::cout << multiply(ix, iy) << \"\\n\";\n    std::cout << multiply(dx, dy) << \"\\n\";\n    return 0;\n}\n",
        "test_cases": [
            {"input": "5 4\n2.5 4.0", "expected_output": "20\n10\n"}
        ]
    },
    {
        "title": "Class Template",
        "description": "Create a `Box` class template that holds a single value of type `T`. Create a getter and setter. In main, create a `Box<int>` and a `Box<std::string>`, set them, and print.",
        "difficulty": "Medium",
        "concepts": "class templates",
        "starter_code": "#include <iostream>\n#include <string>\n\n// template class\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <string>\n\ntemplate <typename T>\nclass Box {\nprivate:\n    T item;\npublic:\n    void set(T val) { item = val; }\n    T get() { return item; }\n};\n\nint main() {\n    Box<int> intBox;\n    intBox.set(100);\n    Box<std::string> strBox;\n    strBox.set(\"C++\");\n    std::cout << intBox.get() << \" \" << strBox.get() << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "100 C++\n"}
        ]
    },
    {
        "title": "Basic Exception",
        "description": "Write a program that throws an `int` exception if a user inputs a negative number. Catch it and print `Error Caught`. Otherwise, print `Valid`.",
        "difficulty": "Medium",
        "concepts": "try, catch, throw",
        "starter_code": "#include <iostream>\n\nint main() {\n    int n;\n    std::cin >> n;\n    // try catch block\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int n;\n    std::cin >> n;\n    try {\n        if (n < 0) throw -1;\n        std::cout << \"Valid\\n\";\n    } catch (int e) {\n        std::cout << \"Error Caught\\n\";\n    }\n    return 0;\n}\n",
        "test_cases": [
            {"input": "50", "expected_output": "Valid\n"},
            {"input": "-5", "expected_output": "Error Caught\n"}
        ]
    },
    {
        "title": "Standard Exceptions",
        "description": "Write a `checkAge(int age)` function. If age < 18, `throw std::invalid_argument(\"Too young\")`. Catch it in main using `const std::invalid_argument&` and print its `.what()` message.",
        "difficulty": "Hard",
        "concepts": "stdexcept",
        "starter_code": "#include <iostream>\n#include <stdexcept>\n\n// function\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <stdexcept>\n\nvoid checkAge(int age) {\n    if (age < 18) throw std::invalid_argument(\"Too young\");\n    std::cout << \"Welcome\\n\";\n}\n\nint main() {\n    int a;\n    std::cin >> a;\n    try {\n        checkAge(a);\n    } catch (const std::invalid_argument& e) {\n        std::cout << e.what() << std::endl;\n    }\n    return 0;\n}\n",
        "test_cases": [
            {"input": "20", "expected_output": "Welcome\n"},
            {"input": "15", "expected_output": "Too young\n"}
        ]
    },
    {
        "title": "Multiple Catch Blocks",
        "description": "Read an int. If it is 1, throw an `int`. If it is 2, throw a `std::string`. If it is 3, throw a `std::runtime_error`. Write three catch blocks to handle them and print `Caught Int`, `Caught String`, or `Caught Runtime`.",
        "difficulty": "Hard",
        "concepts": "exception routing",
        "starter_code": "#include <iostream>\n#include <string>\n#include <stdexcept>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <string>\n#include <stdexcept>\n\nint main() {\n    int type;\n    std::cin >> type;\n    try {\n        if (type == 1) throw 404;\n        if (type == 2) throw std::string(\"Error\");\n        if (type == 3) throw std::runtime_error(\"Fail\");\n    } catch (int e) {\n        std::cout << \"Caught Int\\n\";\n    } catch (std::string& e) {\n        std::cout << \"Caught String\\n\";\n    } catch (const std::runtime_error& e) {\n        std::cout << \"Caught Runtime\\n\";\n    }\n    return 0;\n}\n",
        "test_cases": [
            {"input": "1", "expected_output": "Caught Int\n"},
            {"input": "2", "expected_output": "Caught String\n"},
            {"input": "3", "expected_output": "Caught Runtime\n"}
        ]
    },
    {
        "title": "Custom Exception Class",
        "description": "Create a `class MyException : public std::exception` and override `const char* what() const noexcept`. Throw it, catch it, and print the what() message.",
        "difficulty": "Challenge",
        "concepts": "custom exceptions, inheritance",
        "starter_code": "#include <iostream>\n#include <exception>\n\n// classes\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <exception>\n\nclass MyException : public std::exception {\npublic:\n    const char* what() const noexcept override {\n        return \"Custom Failure!\";\n    }\n};\n\nint main() {\n    try {\n        throw MyException();\n    } catch (const MyException& e) {\n        std::cout << e.what() << std::endl;\n    }\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "Custom Failure!\n"}
        ]
    }
]

m11_quizzes = [
    {"question_text": "What is the main benefit of C++ Templates?", "options": ["They compress the source code size", "They allow you to write generic code (functions/classes) once that works with any data type, avoiding repetitive code duplication", "They make the program run faster at runtime", "They encrypt the code"], "correct_answer": "They allow you to write generic code (functions/classes) once that works with any data type, avoiding repetitive code duplication", "explanation": "Templates are the core of Generic Programming. The compiler automatically writes the type-specific versions of the code for you.", "difficulty": "Beginner"},
    {"question_text": "In `template <typename T>`, what does `T` represent?", "options": ["Time", "A generic placeholder for a data type (like int, double, or a custom class) that will be determined later", "A variable name", "A boolean flag"], "correct_answer": "A generic placeholder for a data type (like int, double, or a custom class) that will be determined later", "explanation": "T is universally used as the placeholder name, standing for 'Type'.", "difficulty": "Beginner"},
    {"question_text": "When does the C++ compiler generate the actual usable code for a template?", "options": ["During program execution", "When the IDE is opened", "At compile-time, ONLY when the template is actually instantiated/called with a specific type", "It never generates code"], "correct_answer": "At compile-time, ONLY when the template is actually instantiated/called with a specific type", "explanation": "If you write a template but never call it, the compiler deletes it. If you call it with an `int`, the compiler writes an `int` version into the binary.", "difficulty": "Medium"},
    {"question_text": "What happens when a `throw` statement is executed?", "options": ["The program prints an error and continues", "The program ignores it", "Normal execution halts immediately, and the program begins unwinding the call stack looking for a matching `catch` block", "The program crashes instantly with no chance to recover"], "correct_answer": "Normal execution halts immediately, and the program begins unwinding the call stack looking for a matching `catch` block", "explanation": "Throwing an exception acts as a hard abort for the current function, searching upwards for a safety net (catch block).", "difficulty": "Medium"},
    {"question_text": "What happens if an exception is thrown but never caught anywhere in the program?", "options": ["The program restarts", "The OS safely ignores it", "The C++ runtime calls `std::terminate()`, violently crashing the program", "The compiler fixes it"], "correct_answer": "The C++ runtime calls `std::terminate()`, violently crashing the program", "explanation": "Uncaught exceptions are fatal. The OS forcefully shuts down the process.", "difficulty": "Medium"},
    {"question_text": "What is the purpose of the `try` block?", "options": ["To try compiling the code", "To enclose risky code that might throw an exception, so that any thrown exceptions can be caught by subsequent `catch` blocks", "To test the performance of a function", "To catch syntax errors"], "correct_answer": "To enclose risky code that might throw an exception, so that any thrown exceptions can be caught by subsequent `catch` blocks", "explanation": "A try block sets up a protected zone. If anything goes wrong inside, the catch block takes over.", "difficulty": "Beginner"},
    {"question_text": "Why should you catch exceptions by `const reference` (e.g., `catch (const std::exception& e)`)?", "options": ["It is required by the compiler", "To prevent the exception from modifying the program", "To avoid the overhead of copying the exception object and to prevent object slicing if catching derived exception types", "Because references are faster to type"], "correct_answer": "To avoid the overhead of copying the exception object and to prevent object slicing if catching derived exception types", "explanation": "Catching by value creates a full copy of the error. If a derived error was thrown, it gets sliced down to the base class.", "difficulty": "Hard"},
    {"question_text": "Which standard library header provides predefined exception classes like `std::runtime_error`?", "options": ["<iostream>", "<exception>", "<stdexcept>", "<error>"], "correct_answer": "<stdexcept>", "explanation": "The stdexcept header defines the most commonly used, descriptive exception classes in C++.", "difficulty": "Hard"},
    {"question_text": "What does the `e.what()` function do when an exception is caught?", "options": ["Asks the user for input", "Returns a C-style string containing the descriptive error message associated with the exception", "Deletes the exception", "Prints the stack trace"], "correct_answer": "Returns a C-style string containing the descriptive error message associated with the exception", "explanation": "The what() virtual function is the standard way to retrieve the text message passed when the exception was thrown.", "difficulty": "Medium"},
    {"question_text": "Can a template function deduce its type automatically without explicitly specifying `<int>`?", "options": ["No, never", "Yes, the compiler can usually deduce the template type based on the arguments passed to the function", "Only for classes", "Only in C++20"], "correct_answer": "Yes, the compiler can usually deduce the template type based on the arguments passed to the function", "explanation": "If you call `add(5, 10)`, the compiler sees two ints and implicitly deduces `T` as `int`.", "difficulty": "Hard"}
]

m12_lesson = """# STL Containers

## What Is It?

The **Standard Template Library (STL)** is a massive, heavily optimized library built into C++. 

**Containers** are the data structures provided by the STL. They are generic (templates) and can hold any data type. Instead of writing your own Linked List, Hash Map, or Dynamic Array from scratch, you use the STL's proven, bug-free, blazing-fast implementations.

## Why Do We Need It?

Writing a memory-safe, dynamically resizing Hash Map in C++ takes hundreds of lines of code and is highly prone to bugs. The STL provides `std::unordered_map` out of the box.

Knowing *when* to use which container is the hallmark of a senior C++ developer.

## The Core Containers

1. **`std::vector` (Dynamic Array)**
   - **Pros**: Fast random access `O(1)`. Fast insertion at the end. Excellent CPU cache locality (fastest overall).
   - **Cons**: Very slow to insert or delete elements in the *middle* `O(N)`, because all following elements must be shifted in memory.
   
2. **`std::list` (Doubly Linked List)**
   - **Pros**: Lightning fast insertions and deletions *anywhere* `O(1)` (if you have an iterator).
   - **Cons**: No random access. You cannot do `list[5]`. You must traverse element by element. Poor cache locality.

3. **`std::deque` (Double Ended Queue)**
   - **Pros**: Fast insertion and deletion at BOTH the front and back `O(1)`. Supports random access.
   - **Cons**: Memory is stored in chunks, slightly slower than a contiguous vector.

4. **`std::map` and `std::unordered_map` (Dictionaries)**
   - **Pros**: Maps Keys to Values (e.g., `"Alice" -> 95`). `map` keeps keys sorted (uses a Red-Black Tree). `unordered_map` uses hashing (extremely fast `O(1)` lookups).

5. **`std::set`**
   - **Pros**: Stores unique elements. Automatically rejects duplicates. Sorted.

## Example 1 — Beginner (Vector vs List)

```cpp
#include <iostream>
#include <vector>
#include <list>

int main() {
    std::vector<int> v = {10, 20, 30};
    v.push_back(40);
    // v[1] is instantly 20 (Random Access)

    std::list<int> l = {10, 20, 30};
    l.push_back(40);
    l.push_front(5); 
    // l[1] DOES NOT COMPILE! No random access.

    std::cout << "Vector [1]: " << v[1] << std::endl;
    
    // To read the list, we must iterate (covered next module)
    std::cout << "List front: " << l.front() << std::endl;

    return 0;
}
```

### Output

```text
Vector [1]: 20
List front: 5
```

### Explanation

`vector` is the default choice for 95% of tasks. You only switch to `list` if you are constantly inserting data into the *middle* of millions of records.

## Example 2 — Real World (Unordered Map)

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

int main() {
    // A dictionary mapping a String (Name) to an Int (Score)
    std::unordered_map<std::string, int> grades;

    // Insert data
    grades["Alice"] = 95;
    grades["Bob"] = 82;
    grades["Charlie"] = 90;

    // O(1) lightning fast lookup!
    std::string search = "Bob";
    std::cout << search << "'s grade is: " << grades[search] << std::endl;

    return 0;
}
```

### Output

```text
Bob's grade is: 82
```

### Explanation

Under the hood, `unordered_map` runs a Hash Function on the word "Bob" to instantly calculate exactly where his score is stored in RAM. It avoids searching through the other records entirely.

## Common Mistakes

* **Using `list` by default**: Because of CPU caching architecture, a `vector` is actually faster than a `list` in almost all real-world scenarios, even when inserting in the middle of small data sets. Always default to `vector`.
* **Accessing non-existent map keys**: If you check `grades["Dave"]` and Dave isn't in the map, C++ will silently *create* a record for Dave with a score of 0. You must use `.count("Dave")` or `.find()` to check if a key exists first.

## Best Practices

* Know your Big-O complexities.
* Need sorted unique data? Use `std::set`.
* Need blazing fast key-value lookups? Use `std::unordered_map`.
* Need LIFO (Last In, First Out)? Use `std::stack`.
* Need FIFO (First In, First Out)? Use `std::queue`.

## Try It Yourself

Create a `std::set<int>`. Insert `10`, `20`, `10`, `30`. Print the size of the set. (It should be 3, because duplicates are rejected).
"""

m12_exercises = [
    {
        "title": "Set Uniqueness",
        "description": "Create a `std::set<int>`. Insert 5, 10, 5, 20, 10. Print the size of the set.",
        "difficulty": "Easy",
        "concepts": "std::set",
        "starter_code": "#include <iostream>\n#include <set>\n\nint main() {\n    // code\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <set>\n\nint main() {\n    std::set<int> s;\n    s.insert(5);\n    s.insert(10);\n    s.insert(5);\n    s.insert(20);\n    s.insert(10);\n    std::cout << s.size() << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "3\n"}
        ]
    },
    {
        "title": "Deque Push/Pop",
        "description": "Create a `std::deque<int>`. Push 10 to the back. Push 20 to the front. Push 30 to the back. Print the front element, then the back element.",
        "difficulty": "Easy",
        "concepts": "std::deque",
        "starter_code": "#include <iostream>\n#include <deque>\n\nint main() {\n    // code\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <deque>\n\nint main() {\n    std::deque<int> d;\n    d.push_back(10);\n    d.push_front(20);\n    d.push_back(30);\n    std::cout << d.front() << \" \" << d.back() << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "20 30\n"}
        ]
    },
    {
        "title": "Map Dictionary",
        "description": "Create a `std::unordered_map<string, int>`. Insert `Apple` -> 5, `Banana` -> 3. Read a fruit name from input and print its value.",
        "difficulty": "Medium",
        "concepts": "unordered_map",
        "starter_code": "#include <iostream>\n#include <string>\n#include <unordered_map>\n\nint main() {\n    // code\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <string>\n#include <unordered_map>\n\nint main() {\n    std::unordered_map<std::string, int> m;\n    m[\"Apple\"] = 5;\n    m[\"Banana\"] = 3;\n    std::string q;\n    std::cin >> q;\n    std::cout << m[q] << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "Apple", "expected_output": "5\n"},
            {"input": "Banana", "expected_output": "3\n"}
        ]
    },
    {
        "title": "Stack LIFO",
        "description": "Create a `std::stack<int>`. Push 1, 2, 3. Pop an element. Print the new `.top()` element.",
        "difficulty": "Medium",
        "concepts": "std::stack, LIFO",
        "starter_code": "#include <iostream>\n#include <stack>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <stack>\n\nint main() {\n    std::stack<int> s;\n    s.push(1);\n    s.push(2);\n    s.push(3);\n    s.pop();\n    std::cout << s.top() << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "2\n"}
        ]
    },
    {
        "title": "Queue FIFO",
        "description": "Create a `std::queue<string>`. Push `Alice`, `Bob`, `Charlie`. Pop an element. Print the `.front()` element.",
        "difficulty": "Hard",
        "concepts": "std::queue, FIFO",
        "starter_code": "#include <iostream>\n#include <string>\n#include <queue>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <string>\n#include <queue>\n\nint main() {\n    std::queue<std::string> q;\n    q.push(\"Alice\");\n    q.push(\"Bob\");\n    q.push(\"Charlie\");\n    q.pop();\n    std::cout << q.front() << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "Bob\n"}
        ]
    },
    {
        "title": "Map Safe Search",
        "description": "Map `Red`->1, `Blue`->2. Read a color. Use `.count()` to check if it exists. If yes, print the value. If no, print `Not Found` to avoid accidentally creating it.",
        "difficulty": "Challenge",
        "concepts": "map bounds checking",
        "starter_code": "#include <iostream>\n#include <string>\n#include <unordered_map>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <string>\n#include <unordered_map>\n\nint main() {\n    std::unordered_map<std::string, int> m;\n    m[\"Red\"] = 1;\n    m[\"Blue\"] = 2;\n    std::string color;\n    std::cin >> color;\n    \n    if (m.count(color) > 0) {\n        std::cout << m[color] << std::endl;\n    } else {\n        std::cout << \"Not Found\" << std::endl;\n    }\n    return 0;\n}\n",
        "test_cases": [
            {"input": "Blue", "expected_output": "2\n"},
            {"input": "Green", "expected_output": "Not Found\n"}
        ]
    }
]

m12_quizzes = [
    {"question_text": "What is the primary advantage of a std::vector over a std::list?", "options": ["Vectors use less code", "Vectors support O(1) random access (e.g., vec[50]) and have highly efficient CPU cache locality because memory is contiguous", "Vectors can hold strings, lists cannot", "Vectors automatically sort their elements"], "correct_answer": "Vectors support O(1) random access (e.g., vec[50]) and have highly efficient CPU cache locality because memory is contiguous", "explanation": "Contiguous memory is incredibly fast for the CPU to read. Lists scatter their nodes across the heap, causing cache misses.", "difficulty": "Medium"},
    {"question_text": "When is a std::list mathematically faster than a std::vector?", "options": ["When reading the first element", "When sorting", "When heavily inserting or deleting elements directly in the middle of a massive dataset", "When iterating sequentially"], "correct_answer": "When heavily inserting or deleting elements directly in the middle of a massive dataset", "explanation": "Inserting into the middle of a vector requires shifting all subsequent elements. A list just re-routes two pointers (O(1)).", "difficulty": "Hard"},
    {"question_text": "Which STL container maps Keys to Values and allows O(1) lightning-fast lookups via hashing?", "options": ["std::vector", "std::map", "std::unordered_map", "std::set"], "correct_answer": "std::unordered_map", "explanation": "unordered_map uses a Hash Table, providing O(1) lookups. std::map uses a Tree, providing slower O(log N) lookups but keeping keys sorted.", "difficulty": "Medium"},
    {"question_text": "What happens if you insert duplicate values into a std::set?", "options": ["The program crashes", "The set stores both copies", "The set simply ignores the duplicate, maintaining only unique elements", "The set throws an exception"], "correct_answer": "The set simply ignores the duplicate, maintaining only unique elements", "explanation": "A set mathematically represents a collection of distinct objects. Duplicates are silently discarded.", "difficulty": "Beginner"},
    {"question_text": "Which container operates strictly on a Last-In, First-Out (LIFO) principle?", "options": ["std::queue", "std::stack", "std::vector", "std::list"], "correct_answer": "std::stack", "explanation": "A stack is like a stack of plates. The last plate you put on top is the first one you take off (pop).", "difficulty": "Beginner"},
    {"question_text": "Which container operates strictly on a First-In, First-Out (FIFO) principle?", "options": ["std::queue", "std::stack", "std::deque", "std::map"], "correct_answer": "std::queue", "explanation": "A queue is like a line at a grocery store. The first person in line is the first one served.", "difficulty": "Beginner"},
    {"question_text": "What makes a std::deque different from a std::vector?", "options": ["A deque only holds integers", "A deque allows fast O(1) insertion and deletion at BOTH the front and the back, whereas vector is only fast at the back", "A deque is sorted automatically", "A deque does not allow random access"], "correct_answer": "A deque allows fast O(1) insertion and deletion at BOTH the front and the back, whereas vector is only fast at the back", "explanation": "Deque stands for Double-Ended Queue. It manages memory in chunks to allow fast growth in both directions.", "difficulty": "Hard"},
    {"question_text": "If you query `map[\"key\"]` and the key does not exist, what does std::map do?", "options": ["Returns a nullptr", "Throws an exception", "Silently creates a new entry with that key and a default-constructed value (e.g., 0 for ints)", "Crashes the program"], "correct_answer": "Silently creates a new entry with that key and a default-constructed value (e.g., 0 for ints)", "explanation": "This is a notorious trap. If you just want to check if a key exists, use `map.count(\"key\")` or `map.find(\"key\")` to avoid polluting the map.", "difficulty": "Hard"},
    {"question_text": "What is the Big-O time complexity of accessing an element by index in a std::vector (e.g., vec[100])?", "options": ["O(N)", "O(log N)", "O(N^2)", "O(1)"], "correct_answer": "O(1)", "explanation": "Because vectors are contiguous arrays, the CPU calculates the exact memory address instantly via math (BaseAddress + Index * Size).", "difficulty": "Medium"},
    {"question_text": "Which header must be included to use std::stack?", "options": ["<vector>", "<container>", "<stack>", "<list>"], "correct_answer": "<stack>", "explanation": "Each STL container resides in its own intuitively named header file.", "difficulty": "Beginner"}
]


m13_lesson = """# Algorithms, Iterators & Lambdas

## What Is It?

The STL separates Containers (where data lives) from **Algorithms** (how to process data). 
**Iterators** are the bridge between them. An iterator acts like a smart pointer that traverses a container.
**Lambdas** are anonymous, inline functions introduced in Modern C++ (C++11) that allow you to write small custom logic directly inside an algorithm call.

## Why Do We Need It?

Instead of writing a custom `for` loop every time you need to find an element, sort an array, or count specific items, the STL `<algorithm>` header provides highly optimized, bug-free functions that do this in one line of code.

Lambdas prevent you from having to write an entire separate function just to tell `std::sort` how to sort a custom object.

## Where Is It Used?

- Data Analysis: `std::count_if` to find how many users are over age 18.
- Gaming: `std::sort` to rank players by score on a leaderboard.
- Anywhere: Using `std::find` instead of writing raw `for` loops.

## How Does It Work?

1. **Iterators**: Every container provides `.begin()` (points to the first element) and `.end()` (points to the space *one past the last element*).
2. **Algorithms**: You pass iterators into an algorithm (e.g., `std::sort(vec.begin(), vec.end())`).
3. **Lambdas**: Defined using `[]() {}`. The `[]` is the capture clause, `()` are parameters, `{}` is the code body.

## Syntax (Algorithms & Iterators)

```cpp
#include <vector>
#include <algorithm>

std::vector<int> v = {3, 1, 4, 1, 5};

// Sort the entire vector
std::sort(v.begin(), v.end()); 
```

## Example 1 — Beginner (Iterators and Find)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> numbers = {10, 20, 30, 40, 50};

    // Using std::find
    auto it = std::find(numbers.begin(), numbers.end(), 30);

    // Check if the iterator reached the end (meaning not found)
    if (it != numbers.end()) {
        std::cout << "Found: " << *it << std::endl;
    } else {
        std::cout << "Not Found" << std::endl;
    }

    return 0;
}
```

### Output

```text
Found: 30
```

### Line-by-Line Explanation

1. `auto it`: We use `auto` so we don't have to type out the massive type name `std::vector<int>::iterator`.
2. `std::find`: Scans from `begin()` to `end()`. If it finds `30`, it returns an iterator pointing to it.
3. `it != numbers.end()`: If it didn't find the number, `find` returns `.end()`. We check against this to verify success.
4. `*it`: We dereference the iterator to print the actual value.

## Example 2 — Real World (Lambdas and Sorting)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

class Player {
public:
    std::string name;
    int score;
    Player(std::string n, int s) : name(n), score(s) {}
};

int main() {
    std::vector<Player> leaderboard = {
        Player("Alice", 150),
        Player("Bob", 300),
        Player("Charlie", 50)
    };

    // Sort descending using a Lambda function
    std::sort(leaderboard.begin(), leaderboard.end(), 
        [](const Player& a, const Player& b) {
            return a.score > b.score; 
        }
    );

    std::cout << "1st Place: " << leaderboard[0].name << std::endl;
    std::cout << "2nd Place: " << leaderboard[1].name << std::endl;

    return 0;
}
```

### Output

```text
1st Place: Bob
2nd Place: Alice
```

### Explanation

`std::sort` normally sorts ascending. It doesn't know how to sort a custom `Player` class. We pass a Lambda function `[](const Player& a, const Player& b) { return a.score > b.score; }` as the third argument. `sort` uses this tiny inline function every time it needs to compare two players.

## Common Mistakes

* **Dereferencing `.end()`**: `.end()` points to the memory immediately *after* the last element. Dereferencing it causes a crash. The last valid element is `end() - 1`.
* **Not including `<algorithm>`**: You must include the header to use functions like `sort`, `find`, or `count`.

## Best Practices

* Use `auto` for iterators to keep code readable.
* Use `<algorithm>` instead of raw `for` loops whenever possible. It clearly communicates *intent* to other developers.
* Use lambdas for short, one-off logic (like custom sorting) rather than polluting your class with operator overloads if the logic is only needed once.

## Try It Yourself

Create a vector of integers: `5, 2, 8, 1, 9`. Use `std::sort` to sort it. Then use a range-based for loop `for(int x : vec)` to print the sorted vector.
"""

m13_exercises = [
    {
        "title": "Use std::sort",
        "description": "Read an integer N. Read N integers into a vector. Use `std::sort` to sort them ascending. Print them space-separated.",
        "difficulty": "Easy",
        "concepts": "std::sort",
        "starter_code": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nint main() {\n    // code\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nint main() {\n    int n; std::cin >> n;\n    std::vector<int> v;\n    for(int i=0; i<n; i++) {\n        int val; std::cin >> val;\n        v.push_back(val);\n    }\n    std::sort(v.begin(), v.end());\n    for(int x : v) std::cout << x << \" \";\n    std::cout << \"\\n\";\n    return 0;\n}\n",
        "test_cases": [
            {"input": "5 9 1 8 2 7", "expected_output": "1 2 7 8 9 \n"}
        ]
    },
    {
        "title": "Use std::find",
        "description": "Read 5 integers into a vector. Read a target integer. Use `std::find`. Print `Found` or `Missing`.",
        "difficulty": "Easy",
        "concepts": "std::find, iterators",
        "starter_code": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nint main() {\n    std::vector<int> v(5);\n    for(int i=0; i<5; i++) std::cin >> v[i];\n    int target; std::cin >> target;\n    auto it = std::find(v.begin(), v.end(), target);\n    if (it != v.end()) std::cout << \"Found\\n\";\n    else std::cout << \"Missing\\n\";\n    return 0;\n}\n",
        "test_cases": [
            {"input": "10 20 30 40 50 30", "expected_output": "Found\n"},
            {"input": "1 2 3 4 5 99", "expected_output": "Missing\n"}
        ]
    },
    {
        "title": "Count Occurrences",
        "description": "Read 6 integers. Read a target. Use `std::count` to find how many times the target appears. Print the count.",
        "difficulty": "Medium",
        "concepts": "std::count",
        "starter_code": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nint main() {\n    std::vector<int> v(6);\n    for(int i=0; i<6; i++) std::cin >> v[i];\n    int target; std::cin >> target;\n    int result = std::count(v.begin(), v.end(), target);\n    std::cout << result << \"\\n\";\n    return 0;\n}\n",
        "test_cases": [
            {"input": "5 5 2 5 3 5 5", "expected_output": "4\n"}
        ]
    },
    {
        "title": "Reverse a Vector",
        "description": "Read 4 integers. Use `std::reverse` to flip the vector. Print it space-separated.",
        "difficulty": "Medium",
        "concepts": "std::reverse",
        "starter_code": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nint main() {\n    std::vector<int> v(4);\n    for(int i=0; i<4; i++) std::cin >> v[i];\n    std::reverse(v.begin(), v.end());\n    for(int x : v) std::cout << x << \" \";\n    std::cout << \"\\n\";\n    return 0;\n}\n",
        "test_cases": [
            {"input": "10 20 30 40", "expected_output": "40 30 20 10 \n"}
        ]
    },
    {
        "title": "Lambda Custom Sort",
        "description": "Read 5 integers. Use `std::sort` with a custom lambda function `[](int a, int b) { return a > b; }` to sort the vector DESCENDING (highest to lowest). Print.",
        "difficulty": "Hard",
        "concepts": "lambdas, sort",
        "starter_code": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nint main() {\n    std::vector<int> v(5);\n    for(int i=0; i<5; i++) std::cin >> v[i];\n    std::sort(v.begin(), v.end(), [](int a, int b) { return a > b; });\n    for(int x : v) std::cout << x << \" \";\n    std::cout << \"\\n\";\n    return 0;\n}\n",
        "test_cases": [
            {"input": "1 9 4 7 3", "expected_output": "9 7 4 3 1 \n"}
        ]
    },
    {
        "title": "Lambda count_if",
        "description": "Read 5 integers. Use `std::count_if` with a lambda to count how many numbers are greater than 10. Print the count.",
        "difficulty": "Challenge",
        "concepts": "count_if, lambdas",
        "starter_code": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nint main() {\n    std::vector<int> v(5);\n    for(int i=0; i<5; i++) std::cin >> v[i];\n    int c = std::count_if(v.begin(), v.end(), [](int x) { return x > 10; });\n    std::cout << c << \"\\n\";\n    return 0;\n}\n",
        "test_cases": [
            {"input": "5 15 2 20 10", "expected_output": "2\n"}
        ]
    }
]

m13_quizzes = [
    {"question_text": "What is an Iterator in the C++ STL?", "options": ["A loop variable (like i in a for loop)", "An object that acts like a pointer, allowing traversal through the elements of a container (like vector or list)", "A sorting algorithm", "A lambda function"], "correct_answer": "An object that acts like a pointer, allowing traversal through the elements of a container (like vector or list)", "explanation": "Iterators bridge the gap between containers and algorithms, providing a uniform way to step through data.", "difficulty": "Beginner"},
    {"question_text": "What does `vec.begin()` return?", "options": ["The first element of the vector", "An iterator pointing to the first element of the vector", "An iterator pointing to the memory before the vector starts", "The size of the vector"], "correct_answer": "An iterator pointing to the first element of the vector", "explanation": "It returns an iterator (a pointer-like object). To get the actual value, you must dereference it `*vec.begin()`.", "difficulty": "Medium"},
    {"question_text": "What does `vec.end()` return?", "options": ["An iterator pointing to the last element of the vector", "An iterator pointing to the theoretical element exactly ONE POSITION PAST the last element of the vector", "The size of the vector", "A nullptr"], "correct_answer": "An iterator pointing to the theoretical element exactly ONE POSITION PAST the last element of the vector", "explanation": "This acts as a sentinel boundary. If an algorithm reaches `.end()`, it knows it has checked every valid element.", "difficulty": "Hard"},
    {"question_text": "Why do we use the `auto` keyword with iterators (e.g., `auto it = vec.begin();`)?", "options": ["To make the code run faster", "Because iterator type names are extremely long and complex (e.g., `std::vector<int>::iterator`), and auto tells the compiler to figure it out", "To automatically delete the iterator", "Because iterators don't have types"], "correct_answer": "Because iterator type names are extremely long and complex (e.g., `std::vector<int>::iterator`), and auto tells the compiler to figure it out", "explanation": "`auto` infers the type at compile time, saving massive amounts of typing while maintaining strict type safety.", "difficulty": "Medium"},
    {"question_text": "Which STL algorithm is used to arrange elements in ascending order?", "options": ["std::order", "std::arrange", "std::sort", "std::sequence"], "correct_answer": "std::sort", "explanation": "`std::sort(v.begin(), v.end())` uses a highly optimized Introsort (QuickSort + HeapSort) to sort data in O(N log N) time.", "difficulty": "Beginner"},
    {"question_text": "What does `std::find` return if it DOES NOT find the target element?", "options": ["-1", "nullptr", "The .end() iterator of the container", "Throws an exception"], "correct_answer": "The .end() iterator of the container", "explanation": "If it scans the whole container and hits the boundary (.end()), it returns that boundary to indicate failure.", "difficulty": "Medium"},
    {"question_text": "What is a Lambda expression in C++?", "options": ["A Greek math symbol", "An anonymous, inline function that can be defined directly at the location where it is invoked or passed as an argument", "A new type of loop", "A macro"], "correct_answer": "An anonymous, inline function that can be defined directly at the location where it is invoked or passed as an argument", "explanation": "Lambdas `[](){}` allow you to inject custom logic (like custom sorting rules) directly into algorithm calls.", "difficulty": "Medium"},
    {"question_text": "What does the `[]` at the start of a lambda expression `[](int a, int b) { ... }` represent?", "options": ["Array brackets", "The Capture Clause, allowing the lambda to access local variables from the surrounding scope", "A syntax error", "The return type"], "correct_answer": "The Capture Clause, allowing the lambda to access local variables from the surrounding scope", "explanation": "By putting `[&]` in the capture clause, the lambda can modify variables in the function that created it.", "difficulty": "Hard"},
    {"question_text": "Which algorithm counts how many elements satisfy a specific boolean condition?", "options": ["std::count", "std::count_if", "std::find_if", "std::sum_if"], "correct_answer": "std::count_if", "explanation": "`std::count_if` takes a container and a lambda returning true/false, counting every element that returns true.", "difficulty": "Medium"},
    {"question_text": "What is the time complexity of `std::binary_search` on a sorted vector?", "options": ["O(N)", "O(1)", "O(log N)", "O(N^2)"], "correct_answer": "O(log N)", "explanation": "Because it divides the search space in half each step, it finds elements in massive datasets almost instantly.", "difficulty": "Hard"}
]

m14_lesson = """# Modern C++ & Memory Management

## What Is It?

Modern C++ (C++11, 14, 17, 20) introduced massive quality-of-life improvements. The most critical is **Smart Pointers**, which automate memory management.

In older C++, developers manually used `new` (allocate memory) and `delete` (free memory). If they forgot `delete`, the program leaked memory. If they `delete`d twice, the program crashed.

## Why Do We Need It?

Manual memory management is the #1 cause of security vulnerabilities and crashes in C/C++ applications. 
Modern C++ enforces **RAII** (Resource Acquisition Is Initialization). This principle states that memory should be tied to the lifecycle of an object. When the object dies (goes out of scope), it cleans up its own memory automatically. Smart pointers implement RAII for the heap.

## Where Is It Used?

- AAA Game Engines: `std::shared_ptr` for textures so the texture is only deleted from RAM when 0 players are using it.
- Browsers: `std::unique_ptr` for DOM nodes to strictly enforce ownership and prevent memory leaks.

## How Does It Work?

1. **`std::unique_ptr`**: Owns a piece of heap memory exclusively. When the pointer goes out of scope, the memory is deleted automatically. It cannot be copied.
2. **`std::shared_ptr`**: Keeps a "Reference Count" of how many pointers point to the memory. When the count hits 0, it deletes the memory automatically.

## Syntax

```cpp
#include <memory>

// Unique Pointer (Preferred)
std::unique_ptr<int> ptr = std::make_unique<int>(100);

// Shared Pointer
std::shared_ptr<int> sPtr1 = std::make_shared<int>(200);
std::shared_ptr<int> sPtr2 = sPtr1; // Count is now 2
```

## Example 1 — Beginner (The Problem with Raw Pointers)

```cpp
#include <iostream>

void dangerousFunction() {
    int* ptr = new int(50); // Allocating heap memory

    // If an exception happens here, or if there is an early 'return',
    // the next line never runs. The memory is leaked forever.
    
    delete ptr; // Freeing memory
}

int main() {
    dangerousFunction();
    return 0;
}
```

### Line-by-Line Explanation

With raw pointers, the programmer bears 100% responsibility for executing `delete` perfectly. This is extremely error-prone.

## Example 2 — Real World (Smart Pointers & RAII)

```cpp
#include <iostream>
#include <memory>

class Resource {
public:
    Resource() { std::cout << "Resource Acquired!" << std::endl; }
    ~Resource() { std::cout << "Resource Destroyed!" << std::endl; }
    void sayHello() { std::cout << "Hello from Resource!" << std::endl; }
};

void safeFunction() {
    // std::make_unique safely allocates the Resource on the heap
    std::unique_ptr<Resource> res = std::make_unique<Resource>();
    
    res->sayHello();
    
    // As soon as safeFunction() ends, 'res' goes out of scope.
    // The unique_ptr AUTOMATICALLY calls delete on the Resource.
    // No manual delete required!
}

int main() {
    std::cout << "Starting program..." << std::endl;
    safeFunction();
    std::cout << "Ending program..." << std::endl;
    return 0;
}
```

### Output

```text
Starting program...
Resource Acquired!
Hello from Resource!
Resource Destroyed!
Ending program...
```

### Explanation

This is RAII in action. The `unique_ptr` acts as an automatic garbage collector for that specific object. Even if `safeFunction` threw an exception, the scope ends, the smart pointer's destructor fires, and the memory is safely cleaned up.

## Common Mistakes

* **Using `new` and `delete` in Modern C++**: Unless you are writing low-level custom allocators or data structures, you should almost never write `new` or `delete`. Use `std::make_unique`.
* **Copying a `unique_ptr`**: `std::unique_ptr<int> a = b;` will throw a compiler error. Unique pointers are strictly exclusively owned. To transfer ownership, you must use `std::move()`.
* **Circular Dependencies with `shared_ptr`**: If Object A holds a shared pointer to Object B, and Object B holds a shared pointer to Object A, the reference count will never reach 0, creating a memory leak. Use `std::weak_ptr` to break cycles.

## Best Practices

* **Default to `std::unique_ptr`**. It has zero performance overhead compared to a raw pointer.
* Use `std::shared_ptr` only when multiple parts of your code mathematically share ownership of the same object, and the object shouldn't be destroyed until everyone is done with it.
* Use **Range-based for loops** for readability: `for (auto& item : vector) { ... }`.

## Try It Yourself

Create a `std::unique_ptr<int>` initialized to 999. Dereference it using `*` to print the value.
"""

m14_exercises = [
    {
        "title": "Unique Pointer",
        "description": "Include `<memory>`. Create a `std::unique_ptr<int>` initialized to 42 using `std::make_unique`. Print its dereferenced value.",
        "difficulty": "Easy",
        "concepts": "smart pointers, make_unique",
        "starter_code": "#include <iostream>\n#include <memory>\n\nint main() {\n    // code\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <memory>\n\nint main() {\n    std::unique_ptr<int> ptr = std::make_unique<int>(42);\n    std::cout << *ptr << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "42\n"}
        ]
    },
    {
        "title": "Shared Pointer Counting",
        "description": "Create a `std::shared_ptr<int>` initialized to 100. Assign it to a second shared pointer. Print `.use_count()` to see how many pointers share the memory.",
        "difficulty": "Medium",
        "concepts": "shared_ptr, reference counting",
        "starter_code": "#include <iostream>\n#include <memory>\n\nint main() {\n    // code\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <memory>\n\nint main() {\n    std::shared_ptr<int> p1 = std::make_shared<int>(100);\n    std::shared_ptr<int> p2 = p1;\n    std::cout << p1.use_count() << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "2\n"}
        ]
    },
    {
        "title": "Range-Based For Loop",
        "description": "Create an array `int arr[] = {10, 20, 30};`. Use a modern range-based for loop `for(int x : arr)` to print the elements space-separated.",
        "difficulty": "Easy",
        "concepts": "modern C++, range loop",
        "starter_code": "#include <iostream>\n\nint main() {\n    int arr[] = {10, 20, 30};\n    // loop\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    int arr[] = {10, 20, 30};\n    for(int x : arr) {\n        std::cout << x << \" \";\n    }\n    std::cout << \"\\n\";\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "10 20 30 \n"}
        ]
    },
    {
        "title": "Transferring Ownership (Move)",
        "description": "You cannot copy a unique_ptr. Create `unique_ptr<int> p1 = make_unique<int>(55);`. Transfer ownership to `p2` using `std::move(p1)`. Print `*p2`.",
        "difficulty": "Hard",
        "concepts": "std::move, unique ownership",
        "starter_code": "#include <iostream>\n#include <memory>\n#include <utility>\n\nint main() {\n    std::unique_ptr<int> p1 = std::make_unique<int>(55);\n    // move to p2\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <memory>\n#include <utility>\n\nint main() {\n    std::unique_ptr<int> p1 = std::make_unique<int>(55);\n    std::unique_ptr<int> p2 = std::move(p1);\n    std::cout << *p2 << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "55\n"}
        ]
    },
    {
        "title": "auto Keyword",
        "description": "Instead of defining types, use `auto` to deduce types. `auto x = 10; auto y = 5.5; auto z = \"Hello\";`. Print them.",
        "difficulty": "Easy",
        "concepts": "auto, type deduction",
        "starter_code": "#include <iostream>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    auto x = 10;\n    auto y = 5.5;\n    auto z = \"Hello\";\n    std::cout << x << \" \" << y << \" \" << z << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "10 5.5 Hello\n"}
        ]
    },
    {
        "title": "Struct Initialization (C++11)",
        "description": "Create a `struct Point { int x = 0; int y = 0; };` using modern default member initialization. Instantiate it without setting x and y. Print x and y.",
        "difficulty": "Medium",
        "concepts": "modern initialization",
        "starter_code": "#include <iostream>\n\nstruct Point {\n    int x = 0;\n    int y = 0;\n};\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nstruct Point {\n    int x = 0;\n    int y = 0;\n};\n\nint main() {\n    Point p;\n    std::cout << p.x << \" \" << p.y << std::endl;\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "0 0\n"}
        ]
    }
]

m14_quizzes = [
    {"question_text": "What is a memory leak in C++?", "options": ["Water spilling on the motherboard", "When a variable goes out of scope", "When dynamic heap memory is allocated using 'new', but never freed using 'delete', causing the program to permanently hold onto RAM it doesn't need", "When a vector resizes automatically"], "correct_answer": "When dynamic heap memory is allocated using 'new', but never freed using 'delete', causing the program to permanently hold onto RAM it doesn't need", "explanation": "Over time, memory leaks consume all available RAM, causing the operating system to forcefully crash the program.", "difficulty": "Medium"},
    {"question_text": "What does RAII stand for in Modern C++?", "options": ["Random Access Inline Instructions", "Run At Initial Implementation", "Resource Acquisition Is Initialization (tying the lifespan of memory/resources to the scope of a stack object)", "Rapid Allocation In Interfaces"], "correct_answer": "Resource Acquisition Is Initialization (tying the lifespan of memory/resources to the scope of a stack object)", "explanation": "RAII guarantees that when a smart pointer goes out of scope, its destructor runs, safely cleaning up the heap memory.", "difficulty": "Hard"},
    {"question_text": "What does a std::unique_ptr do?", "options": ["Shares memory with other pointers", "Automatically deletes its managed heap memory when it goes out of scope, guaranteeing strict, exclusive ownership", "Points to null", "Allocates stack memory"], "correct_answer": "Automatically deletes its managed heap memory when it goes out of scope, guaranteeing strict, exclusive ownership", "explanation": "Because it guarantees exclusive ownership, the compiler completely forbids you from making a copy of a unique_ptr.", "difficulty": "Medium"},
    {"question_text": "What does a std::shared_ptr do?", "options": ["Encrypts the data", "Keeps a running count (reference count) of how many shared pointers point to the exact same memory, deleting the memory only when the count drops to 0", "Transfers ownership to another pointer", "Creates a read-only variable"], "correct_answer": "Keeps a running count (reference count) of how many shared pointers point to the exact same memory, deleting the memory only when the count drops to 0", "explanation": "Shared pointers are great for shared assets, like a texture used by 5 different models in a game.", "difficulty": "Medium"},
    {"question_text": "Which function is the safest and most efficient way to create a unique_ptr?", "options": ["std::new", "std::unique", "std::make_unique<T>()", "std::alloc"], "correct_answer": "std::make_unique<T>()", "explanation": "make_unique safely allocates the memory and wraps it in the unique_ptr in one atomic step, preventing leaks during exceptions.", "difficulty": "Beginner"},
    {"question_text": "Why does `std::unique_ptr<int> b = a;` cause a compiler error?", "options": ["Because a is an int", "Because unique_ptr is broken", "Because unique_ptrs represent exclusive ownership and physically cannot be copied. They must be MOVED using std::move()", "Because b is uninitialized"], "correct_answer": "Because unique_ptrs represent exclusive ownership and physically cannot be copied. They must be MOVED using std::move()", "explanation": "If you could copy a unique_ptr, both pointers would eventually go out of scope and delete the same memory twice.", "difficulty": "Hard"},
    {"question_text": "What does the `auto` keyword do in Modern C++?", "options": ["Writes code automatically", "Deduces the data type of a variable at compile time based on the value it is initialized with", "Deletes variables automatically", "Declares an automotive class"], "correct_answer": "Deduces the data type of a variable at compile time based on the value it is initialized with", "explanation": "Instead of `std::vector<int>::iterator it = vec.begin()`, you can safely write `auto it = vec.begin()`.", "difficulty": "Beginner"},
    {"question_text": "What is the purpose of a 'range-based for loop' (e.g., `for (int val : vec)`)?", "options": ["To loop infinitely", "To sort a vector", "To provide a clean, readable syntax for iterating over every element in a container from start to finish without using index variables", "To find a specific value"], "correct_answer": "To provide a clean, readable syntax for iterating over every element in a container from start to finish without using index variables", "explanation": "It eliminates the risk of out-of-bounds errors (off-by-one errors) and cleans up the code immensely.", "difficulty": "Medium"},
    {"question_text": "What is the 'Rule of Zero'?", "options": ["Variables should equal 0", "Arrays start at 0", "If your class uses modern smart pointers and STL containers, you shouldn't need to write a custom Destructor or Copy Constructor at all. The compiler handles it.", "You can't have zero lines of code"], "correct_answer": "If your class uses modern smart pointers and STL containers, you shouldn't need to write a custom Destructor or Copy Constructor at all. The compiler handles it.", "explanation": "Because smart pointers clean up after themselves, a class composed of smart pointers cleans up after itself automatically.", "difficulty": "Hard"},
    {"question_text": "What is a std::weak_ptr?", "options": ["A pointer that crashes", "A non-owning observer of a shared_ptr. It can view the memory, but does not increase the reference count, preventing circular dependency memory leaks", "A pointer with a short name", "A unique_ptr"], "correct_answer": "A non-owning observer of a shared_ptr. It can view the memory, but does not increase the reference count, preventing circular dependency memory leaks", "explanation": "If A points to B and B points to A via shared_ptrs, the count never reaches 0. weak_ptr breaks this cycle.", "difficulty": "Hard"}
]

m15_lesson = """# DSA Foundations & Capstone

## What Is It?

Data Structures and Algorithms (DSA) is the core of Computer Science. It is the study of how to organize data efficiently in RAM, and how to write mathematical steps to process that data.

Big-O Notation is a mathematical language used to describe the efficiency of an algorithm.

## Why Do We Need It?

A poorly designed algorithm might run instantly for 10 users, but take 5 years to process 1,000,000 users. Understanding DSA ensures your software scales efficiently. 

While the C++ STL provides containers (like `vector` and `map`), understanding *how* they work under the hood (Dynamic Arrays and Hash Tables) ensures you pick the right tool for the job.

## Where Is It Used?

- Databases: B-Trees (a data structure) allow rapid search through millions of records without scanning the entire hard drive.
- GPS Navigation: Dijkstra's Algorithm finds the shortest path through a Graph of roads.
- Compilers: Abstract Syntax Trees parse your source code.

## Big-O Complexity

Big-O describes how the execution time grows as the data size (N) grows.

1. **O(1) - Constant Time**: Takes the exact same time regardless of data size. (e.g., Array index lookup `arr[50]`).
2. **O(log N) - Logarithmic**: Extremely fast for massive data. (e.g., Binary Search on a sorted array).
3. **O(N) - Linear Time**: Takes twice as long for twice as much data. (e.g., Scanning an unsorted array).
4. **O(N^2) - Quadratic**: Very slow for large data. (e.g., Nested loops, Bubble Sort).

## Example 1 — Beginner (Linear Search O(N))

```cpp
#include <iostream>
#include <vector>

// Worst case: It has to check every single element. Time = O(N)
int linearSearch(const std::vector<int>& arr, int target) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == target) {
            return i; // Found! Return index
        }
    }
    return -1; // Not found
}

int main() {
    std::vector<int> nums = {5, 2, 9, 1, 6};
    std::cout << "Index: " << linearSearch(nums, 9) << std::endl;
    return 0;
}
```

### Output

```text
Index: 2
```

## Example 2 — Real World (Binary Search O(log N))

If data is sorted, we can use Binary Search. We check the middle element. If our target is smaller, we discard the entire right half of the array. We repeat this, halving the search space each time.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int binarySearch(const std::vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid + 1; // Discard left half
        else right = mid - 1;                  // Discard right half
    }
    return -1;
}

int main() {
    std::vector<int> nums = {10, 20, 30, 40, 50, 60, 70, 80};
    
    // In an array of 1,000,000 elements, Binary Search finds the answer in at most 20 steps.
    // Linear search could take 1,000,000 steps.
    std::cout << "Index of 70: " << binarySearch(nums, 70) << std::endl;
    
    return 0;
}
```

### Output

```text
Index of 70: 6
```

## Common Mistakes

* **Using Linear Search on massive datasets**: If you need to search a billion records frequently, searching from index 0 to N every time will freeze your application.
* **Using Binary Search on UNSORTED data**: Binary Search only works mathematically if the data is strictly sorted ascending or descending.
* **Choosing the wrong container**: Using a `std::vector` to frequently insert items at index 0 requires shifting all N items (O(N) time). A `std::deque` or `std::list` does this in O(1) time.

## Best Practices

* Know the Big-O time and space complexities of the STL containers you use.
* For most business applications, use `std::unordered_map` for O(1) fast lookups.
* Write clean, modular code using Classes and Smart Pointers to avoid memory leaks.

## Try It Yourself

Review your entire C++ knowledge. You are now ready to tackle the final Capstone project in the exercises!
"""

m15_exercises = [
    {
        "title": "Linear Search Implementation",
        "description": "Read N. Read N integers. Read a target. Implement a linear search loop to print the index of the target, or `-1` if not found.",
        "difficulty": "Easy",
        "concepts": "O(N) search",
        "starter_code": "#include <iostream>\n#include <vector>\n\nint main() {\n    // code\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <vector>\n\nint main() {\n    int n; std::cin >> n;\n    std::vector<int> v(n);\n    for(int i=0; i<n; i++) std::cin >> v[i];\n    int target; std::cin >> target;\n    int idx = -1;\n    for(int i=0; i<n; i++) {\n        if (v[i] == target) { idx = i; break; }\n    }\n    std::cout << idx << \"\\n\";\n    return 0;\n}\n",
        "test_cases": [
            {"input": "5 10 20 30 40 50 30", "expected_output": "2\n"},
            {"input": "3 1 2 3 99", "expected_output": "-1\n"}
        ]
    },
    {
        "title": "Bubble Sort Implementation",
        "description": "Read N, then N integers. Implement the Bubble Sort algorithm using nested loops. Print the sorted array. (Complexity: O(N^2)).",
        "difficulty": "Medium",
        "concepts": "O(N^2) sorting",
        "starter_code": "#include <iostream>\n#include <vector>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <vector>\n\nint main() {\n    int n; std::cin >> n;\n    std::vector<int> v(n);\n    for(int i=0; i<n; i++) std::cin >> v[i];\n    for(int i=0; i<n-1; i++) {\n        for(int j=0; j<n-i-1; j++) {\n            if (v[j] > v[j+1]) {\n                int temp = v[j];\n                v[j] = v[j+1];\n                v[j+1] = temp;\n            }\n        }\n    }\n    for(int x : v) std::cout << x << \" \";\n    std::cout << \"\\n\";\n    return 0;\n}\n",
        "test_cases": [
            {"input": "5 9 1 8 2 7", "expected_output": "1 2 7 8 9 \n"}
        ]
    },
    {
        "title": "Binary Search Logic",
        "description": "Given a SORTED array input, implement a Binary Search. Print `Found` or `Not Found`.",
        "difficulty": "Medium",
        "concepts": "O(log N) search",
        "starter_code": "#include <iostream>\n#include <vector>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <vector>\n\nint main() {\n    int n; std::cin >> n;\n    std::vector<int> v(n);\n    for(int i=0; i<n; i++) std::cin >> v[i];\n    int t; std::cin >> t;\n    int L=0, R=n-1; bool found=false;\n    while(L <= R) {\n        int mid = L + (R-L)/2;\n        if (v[mid] == t) { found = true; break; }\n        if (v[mid] < t) L = mid + 1;\n        else R = mid - 1;\n    }\n    if(found) std::cout<<\"Found\\n\"; else std::cout<<\"Not Found\\n\";\n    return 0;\n}\n",
        "test_cases": [
            {"input": "5 10 20 30 40 50 40", "expected_output": "Found\n"}
        ]
    },
    {
        "title": "Frequency Map",
        "description": "Read N integers. Use an `unordered_map` to count the frequency of each integer. Read a target integer, print its frequency. (O(N) processing, O(1) lookup).",
        "difficulty": "Hard",
        "concepts": "Hash Tables, O(1) lookups",
        "starter_code": "#include <iostream>\n#include <unordered_map>\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <unordered_map>\n\nint main() {\n    int n; std::cin >> n;\n    std::unordered_map<int, int> freq;\n    for(int i=0; i<n; i++) {\n        int val; std::cin >> val;\n        freq[val]++;\n    }\n    int target; std::cin >> target;\n    std::cout << freq[target] << \"\\n\";\n    return 0;\n}\n",
        "test_cases": [
            {"input": "7 1 2 2 3 2 4 1 2", "expected_output": "3\n"}
        ]
    },
    {
        "title": "CAPSTONE SUB-TASK: OOP System",
        "description": "Create a `Student` class with `string name`, `int roll`, `double gpa`. Create a `Manager` class containing a `vector<Student>`. Write an `addStudent` and a `printBest` (highest GPA) method. Run it.",
        "difficulty": "Challenge",
        "concepts": "OOP, Vectors, Algorithms",
        "starter_code": "#include <iostream>\n#include <vector>\n#include <string>\n\n// classes\n\nint main() {\n    \n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n#include <vector>\n#include <string>\n\nclass Student {\npublic:\n    std::string name;\n    int roll;\n    double gpa;\n    Student(std::string n, int r, double g) : name(n), roll(r), gpa(g) {}\n};\n\nclass Manager {\nprivate:\n    std::vector<Student> db;\npublic:\n    void addStudent(std::string n, int r, double g) {\n        db.push_back(Student(n, r, g));\n    }\n    void printBest() {\n        if (db.empty()) return;\n        Student best = db[0];\n        for (auto& s : db) {\n            if (s.gpa > best.gpa) best = s;\n        }\n        std::cout << best.name << \"\\n\";\n    }\n};\n\nint main() {\n    Manager m;\n    m.addStudent(\"Alice\", 1, 3.5);\n    m.addStudent(\"Bob\", 2, 4.0);\n    m.printBest();\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "Bob\n"}
        ]
    },
    {
        "title": "C++ COMPLETE",
        "description": "You have completed the C++ course! Print `Course Passed!` to conclude.",
        "difficulty": "Easy",
        "concepts": "completion",
        "starter_code": "#include <iostream>\n\nint main() {\n    // code\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n\nint main() {\n    std::cout << \"Course Passed!\\n\";\n    return 0;\n}\n",
        "test_cases": [
            {"input": "", "expected_output": "Course Passed!\n"}
        ]
    }
]

m15_quizzes = [
    {"question_text": "What does Big-O notation describe in Computer Science?", "options": ["The amount of hard drive space a program takes", "How the execution time (or memory usage) of an algorithm grows as the size of the input data (N) increases", "The number of lines of code in a program", "The speed of the CPU clock"], "correct_answer": "How the execution time (or memory usage) of an algorithm grows as the size of the input data (N) increases", "explanation": "Big-O focuses on the worst-case scaling behavior, ignoring minor constants and hardware specifics.", "difficulty": "Beginner"},
    {"question_text": "Which time complexity represents an algorithm that executes in exactly the same amount of time regardless of how large the dataset is?", "options": ["O(N)", "O(log N)", "O(N^2)", "O(1) Constant Time"], "correct_answer": "O(1) Constant Time", "explanation": "Accessing an array element by index (e.g., arr[50]) takes O(1) time because the CPU jumps directly to the memory address.", "difficulty": "Medium"},
    {"question_text": "What is the time complexity of searching an unsorted std::vector using a linear for-loop?", "options": ["O(1)", "O(log N)", "O(N)", "O(N^2)"], "correct_answer": "O(N)", "explanation": "In the worst case, the target is at the very end of the array, requiring the loop to execute exactly N times.", "difficulty": "Medium"},
    {"question_text": "What is the time complexity of Binary Search?", "options": ["O(1)", "O(log N) Logarithmic Time", "O(N)", "O(N log N)"], "correct_answer": "O(log N) Logarithmic Time", "explanation": "Because Binary Search halves the search space at every step, searching 1 billion items takes at most ~30 steps.", "difficulty": "Hard"},
    {"question_text": "What strict condition must be met before Binary Search can be used on an array?", "options": ["The array must contain only positive integers", "The array must be empty", "The array must be mathematically sorted (ascending or descending) beforehand", "The array must be dynamically allocated"], "correct_answer": "The array must be mathematically sorted (ascending or descending) beforehand", "explanation": "If the array isn't sorted, halving the search space provides no logical guarantees about where the target is.", "difficulty": "Medium"},
    {"question_text": "What is the time complexity of the highly-optimized `std::sort` algorithm in the C++ STL?", "options": ["O(N)", "O(N log N)", "O(N^2)", "O(1)"], "correct_answer": "O(N log N)", "explanation": "std::sort uses Introsort, which is mathematically proven to sort elements in O(N log N) time, significantly faster than O(N^2) Bubble Sort.", "difficulty": "Hard"},
    {"question_text": "Which STL container guarantees average O(1) constant time for key-value lookups?", "options": ["std::vector", "std::map", "std::unordered_map", "std::list"], "correct_answer": "std::unordered_map", "explanation": "unordered_map is backed by a Hash Table. The key is hashed to calculate the exact memory location instantly.", "difficulty": "Hard"},
    {"question_text": "In a Linked List data structure, what does a 'Node' contain?", "options": ["Only data", "Only a memory address", "The data itself, plus a pointer to the next Node in the chain", "A vector"], "correct_answer": "The data itself, plus a pointer to the next Node in the chain", "explanation": "Linked Lists are scattered in the heap. They rely on pointers to daisy-chain the pieces together.", "difficulty": "Medium"},
    {"question_text": "What is the worst-case time complexity of inserting a single element into the FRONT of a std::vector containing N elements?", "options": ["O(1)", "O(log N)", "O(N)", "O(N^2)"], "correct_answer": "O(N)", "explanation": "To make room at the front, every single existing element must be copied and shifted exactly 1 slot to the right.", "difficulty": "Hard"},
    {"question_text": "Which principle is the absolute foundation of building scalable backend systems and large-scale applications?", "options": ["Writing everything in one massive function", "Understanding Data Structures and Algorithms (DSA) to write optimal, memory-efficient, and fast-scaling logic", "Copying and pasting code from the internet", "Using global variables everywhere"], "correct_answer": "Understanding Data Structures and Algorithms (DSA) to write optimal, memory-efficient, and fast-scaling logic", "explanation": "You have now completed the C++ course! DSA separates average coders from world-class software engineers.", "difficulty": "Beginner"}
]


course_cpp = {
    "course_id": "cpp-programming",
    "title": "C++ Programming - Beginner to Advanced",
    "description": "Master C++ from basic syntax to advanced Object-Oriented Programming, memory management, and STL. Perfect for game development and high-performance applications.",
    "language": "cpp",
    "difficulty": "Intermediate",
    "order": 9,
    "icon": "SiCplusplus",
    "color": "#00599C"
}

cpp_projects = [
    {
        "title": "Number Guessing Game",
        "description": "Build a console game where the user guesses a random number using loops and conditionals.",
        "difficulty": "Easy",
        "module_index": 4,
        "starter_code": "#include <iostream>\n\nint main() {\n    // Write your game here\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n// Solution code\nint main() { return 0; }\n",
        "test_cases": []
    },
    {
        "title": "Student Management System",
        "description": "Create a system using arrays/vectors to add, view, and search student records.",
        "difficulty": "Medium",
        "module_index": 6,
        "starter_code": "#include <iostream>\n#include <vector>\n\nint main() {\n    // Write your system here\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n// Solution code\nint main() { return 0; }\n",
        "test_cases": []
    },
    {
        "title": "Banking System OOP",
        "description": "Implement a banking system with BankAccount classes, encapsulation, and inheritance for Savings/Checking accounts.",
        "difficulty": "Medium",
        "module_index": 9,
        "starter_code": "#include <iostream>\n\nclass BankAccount {\n    // Implement class\n};\n\nint main() {\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n// Solution code\nint main() { return 0; }\n",
        "test_cases": []
    },
    {
        "title": "Custom Vector Class",
        "description": "Build your own dynamically resizing vector class using raw pointers, operator overloading, and the Rule of Three.",
        "difficulty": "Hard",
        "module_index": 10,
        "starter_code": "#include <iostream>\n\nclass MyVector {\n    // Implement class\n};\n\nint main() {\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n// Solution code\nint main() { return 0; }\n",
        "test_cases": []
    },
    {
        "title": "Inventory Manager using STL",
        "description": "Use unordered_map, set, and sort algorithms to manage a store's inventory and perform fast queries.",
        "difficulty": "Hard",
        "module_index": 13,
        "starter_code": "#include <iostream>\n\nint main() {\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n// Solution code\nint main() { return 0; }\n",
        "test_cases": []
    },
    {
        "title": "Capstone: Dungeon Crawler Game Engine",
        "description": "Build a text-based dungeon crawler using polymorphism for Enemies, smart pointers for memory, and STL containers for maps.",
        "difficulty": "Challenge",
        "module_index": 15,
        "starter_code": "#include <iostream>\n\nint main() {\n    return 0;\n}\n",
        "solution_code": "#include <iostream>\n// Solution code\nint main() { return 0; }\n",
        "test_cases": []
    }
]


cpp_modules = [
    {
        "title": "Module 1: C++ Foundations & Setup",
        "description": "Learn the history of C++, compilation process, and basic syntax.",
        "order": 1,
        "lesson_content": m1_lesson,
        "exercises": m1_exercises,
        "quizzes": m1_quizzes
    },
    {
        "title": "Module 2: Variables, Data Types & Memory",
        "description": "Understand primitive types, variables, constants, and basic memory concepts.",
        "order": 2,
        "lesson_content": m2_lesson,
        "exercises": m2_exercises,
        "quizzes": m2_quizzes
    },
    {
        "title": "Module 3: I/O, Operators & Control Flow",
        "description": "Master std::cin, std::cout, operators, and if/else branching.",
        "order": 3,
        "lesson_content": m3_lesson,
        "exercises": m3_exercises,
        "quizzes": m3_quizzes
    },
    {
        "title": "Module 4: Loops & Iteration",
        "description": "Learn while, do-while, and for loops to automate repetitive tasks.",
        "order": 4,
        "lesson_content": m4_lesson,
        "exercises": m4_exercises,
        "quizzes": m4_quizzes
    },
    {
        "title": "Module 5: Functions & Modularity",
        "description": "Break code into reusable functions, understand scope, and pass by reference.",
        "order": 5,
        "lesson_content": m5_lesson,
        "exercises": m5_exercises,
        "quizzes": m5_quizzes
    },
    {
        "title": "Module 6: Arrays, Strings & Vectors",
        "description": "Store multiple items using raw arrays, std::string, and dynamic std::vector.",
        "order": 6,
        "lesson_content": m6_lesson,
        "exercises": m6_exercises,
        "quizzes": m6_quizzes
    },
    {
        "title": "Module 7: Pointers & References",
        "description": "Master memory addresses, pointers, dereferencing, and the differences from references.",
        "order": 7,
        "lesson_content": m7_lesson,
        "exercises": m7_exercises,
        "quizzes": m7_quizzes
    },
    {
        "title": "Module 8: Object-Oriented Programming (OOP)",
        "description": "Learn Classes, Objects, Encapsulation, and Constructors.",
        "order": 8,
        "lesson_content": m8_lesson,
        "exercises": m8_exercises,
        "quizzes": m8_quizzes
    },
    {
        "title": "Module 9: Inheritance & Polymorphism",
        "description": "Build class hierarchies, override methods, and use virtual functions for dynamic dispatch.",
        "order": 9,
        "lesson_content": m9_lesson,
        "exercises": m9_exercises,
        "quizzes": m9_quizzes
    },
    {
        "title": "Module 10: Advanced OOP & Operator Overloading",
        "description": "Overload operators like +, ==, <<, and understand the Rule of Three for deep copies.",
        "order": 10,
        "lesson_content": m10_lesson,
        "exercises": m10_exercises,
        "quizzes": m10_quizzes
    },
    {
        "title": "Module 11: Templates & Exception Handling",
        "description": "Write generic code with templates and gracefully handle errors with try/catch.",
        "order": 11,
        "lesson_content": m11_lesson,
        "exercises": m11_exercises,
        "quizzes": m11_quizzes
    },
    {
        "title": "Module 12: STL Containers",
        "description": "Master std::list, std::deque, std::map, std::unordered_map, and std::set.",
        "order": 12,
        "lesson_content": m12_lesson,
        "exercises": m12_exercises,
        "quizzes": m12_quizzes
    },
    {
        "title": "Module 13: Algorithms, Iterators & Lambdas",
        "description": "Use STL algorithms like sort and find, traverse with iterators, and write inline lambdas.",
        "order": 13,
        "lesson_content": m13_lesson,
        "exercises": m13_exercises,
        "quizzes": m13_quizzes
    },
    {
        "title": "Module 14: Modern C++ & Memory Management",
        "description": "Use std::unique_ptr and std::shared_ptr to automatically manage memory and prevent leaks.",
        "order": 14,
        "lesson_content": m14_lesson,
        "exercises": m14_exercises,
        "quizzes": m14_quizzes
    },
    {
        "title": "Module 15: DSA Foundations & Capstone",
        "description": "Understand Big-O complexity, searching, sorting, and combine all knowledge into the final project.",
        "order": 15,
        "lesson_content": m15_lesson,
        "exercises": m15_exercises,
        "quizzes": m15_quizzes
    }
]
