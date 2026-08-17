import json

def build_lesson(title, slug, what, why, how, syntax, example_simple, example_real, output_simple, lbl_simple, output_real, explanation_real, common_mistakes, best_practices, exercises, quizzes, project=None):
    content = f"""# {title}

## What Is It?
{what}

## Why Do We Need It?
{why}

## How Does It Work?
{how}

## Syntax
```c
{syntax}
```

## Example 1 — Simple
```c
{example_simple}
```

### Output
```text
{output_simple}
```

### Line-by-Line Explanation
{lbl_simple}

## Example 2 — Real-World
```c
{example_real}
```

### Output
```text
{output_real}
```

### Explanation
{explanation_real}

## Common Mistakes
{common_mistakes}

## Best Practices
{best_practices}

## Try It Yourself
Test your understanding by attempting the practical coding exercises in the practice lab below. Each exercise tests real implementation logic!
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
    modules = []

    # =========================================================================
    # MODULE 1: C Programming Foundations
    # =========================================================================
    m1_what = """C is a high-performance, general-purpose procedural programming language created by Dennis Ritchie at Bell Labs in 1972 for writing the Unix operating system. It sits directly above assembly language, providing human-readable structured syntax while granting complete, unmediated access to computer hardware memory and CPU instruction registers.

When you compile a C program, your human-readable source code (.c file) does not run inside an interpreter or virtual machine. Instead, it undergoes a four-stage translation pipeline: Preprocessing (handling #include and #define directives), Compilation (converting C code into machine assembly code), Assembly (assembling machine assembly into object binary files .o/.obj), and Linking (combining object files and standard C library binaries into a single executable binary).

Understanding C is foundational because virtually all modern software infrastructure—operating system kernels (Linux, macOS, Windows), database engines (PostgreSQL, SQLite, Redis), embedded microcontrollers, web browser runtimes, and interpreters for Python, JavaScript, and Ruby—are written in C or depend directly on C interfaces."""

    m1_why = """Before C existed, developers wrote operating systems and high-performance software in low-level assembly language. Assembly code is tied to specific CPU architectures, making programs non-portable and extremely tedious to write and maintain. C solved this problem by providing structured constructs (functions, loops, variables) while retaining direct hardware pointer access.

Higher-level languages like Python, Java, and C# simplify memory management using garbage collection and managed runtimes. However, this abstraction layer introduces runtime overhead and hides how memory management, CPU registers, stack frames, and hardware caches operate internally.

Learning C equips you with a clear mental model of how computer hardware executes code. It answers fundamental questions: How does memory allocation work? How does a function call execute on the CPU stack? How do process exit codes signal success or failure to the shell?"""

    m1_how = """When an operating system launches a C executable binary, the kernel creates a new process, allocates a virtual memory address space (split into Text/Code, Data, BSS, Stack, and Heap segments), and transfers execution control directly to the program's primary entry point: the `main()` function.

```
Compilation Pipeline Architecture:
Source (.c) ---> [ Preprocessor ] ---> Expanded Source
                     |
                     v
                [ Compiler ]     ---> Assembly (.s)
                     |
                     v
                [ Assembler ]    ---> Machine Object (.o)
                     |
                     v
                 [ Linker ]      ---> Executable Binary (.exe / elf)
```

Execution proceeds sequentially line by line through statements terminated by semicolons `;`. Standard library header `#include <stdio.h>` provides declarations for standard stream input/output functions like `printf()`. When main completes, returning `0` signals to the operating system shell that execution finished cleanly without runtime errors."""

    m1_syntax = """#include <stdio.h>

int main(void) {
    // Statements executed sequentially
    printf("Hello, World!\\n");
    return 0; // Signals clean process termination
}"""

    m1_ex_sim = """#include <stdio.h>

int main(void) {
    printf("Welcome to C Programming!\\n");
    return 0;
}"""

    m1_out_sim = """Welcome to C Programming!"""

    m1_lbl_sim = """- `#include <stdio.h>`: Imports standard Input/Output library header declarations, enabling access to functions like `printf()`.
- `int main(void)`: Defines the primary entry point function of every C process, specifying an integer return type.
- `{ ... }`: Curly braces enclose the function execution scope block.
- `printf("Welcome to C Programming!\n");`: Calls system library function to print string characters to standard stdout terminal output.
- `\n`: Escape sequence inserting a line feed / newline character.
- `return 0;`: Exits function returning status code 0 to operating system process table."""

    m1_ex_real = """#include <stdio.h>

int main(void) {
    printf("=================================\\n");
    printf(" LEARNX FIRMWARE BOOT SEQUENCE   \\n");
    printf(" Status: OK | Kernel: 5.15-C     \\n");
    printf(" Memory Subsystem: Initialized   \\n");
    printf("=================================\\n");
    return 0;
}"""

    m1_out_real = """=================================
 LEARNX FIRMWARE BOOT SEQUENCE   
 Status: OK | Kernel: 5.15-C     
 Memory Subsystem: Initialized   
================================="""

    m1_exp_real = """This real-world example simulates a low-level firmware startup banner printed during system boot on an embedded device. Each `printf` statement outputs a formatted text string to standard output, demonstrating how system logs and status messages are rendered line-by-line during kernel startup."""

    m1_mistakes = """1. Omitting the mandatory semicolon `;` at the end of statements, causing compilation errors.
2. Writing `Printf` or `Main` instead of lowercase `printf` and `main` (C syntax is strictly case-sensitive).
3. Forgetting `#include <stdio.h>` when using standard output functions.
4. Omitting `return 0;` inside `int main()`, leading to undefined return exit codes in older C compilers."""

    m1_best = """1. Always indent code inside function bodies consistently (use 4 spaces per nesting level).
2. Write concise comments explaining complex logic rather than repeating code syntax.
3. Always return `0` explicitly from `main()` to confirm successful exit status to OS parent process."""

    m1_exs = [
        {
            "title": "Hello World Starter",
            "description": "Write a complete C program that prints 'Hello, World!' followed by a newline.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    // Print Hello, World!\n    return 0;\n}\n",
            "language": "c",
            "order_index": 1,
            "test_cases": [{"input_data": "", "expected_output": "Hello, World!\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Multi-Line System Information Printer",
            "description": "Print two lines: Line 1 'System: LearnX C Core', Line 2 'Status: Active'.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    // Print multi-line status\n    return 0;\n}\n",
            "language": "c",
            "order_index": 2,
            "test_cases": [{"input_data": "", "expected_output": "System: LearnX C Core\nStatus: Active\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Tabular Escape Sequence Formatter",
            "description": "Use escape sequences `\\t` and `\\\"` to print: Line 1 'ID\\tName', Line 2 '1\\t\\\"C-Lang\\\"'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    // Format tabular output\n    return 0;\n}\n",
            "language": "c",
            "order_index": 3,
            "test_cases": [{"input_data": "", "expected_output": "ID\tName\n1\t\"C-Lang\"\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Process Status Code Simulator",
            "description": "Print 'Process Started' and explicitly return integer exit status 0.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    // Print and return 0\n    return 0;\n}\n",
            "language": "c",
            "order_index": 4,
            "test_cases": [{"input_data": "", "expected_output": "Process Started\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "ASCII Border Box Renderer",
            "description": "Print a 3-line ASCII box: Line 1 '***', Line 2 '* *', Line 3 '***'.",
            "difficulty": "Hard",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    // Print ASCII box\n    return 0;\n}\n",
            "language": "c",
            "order_index": 5,
            "test_cases": [{"input_data": "", "expected_output": "***\n* *\n***\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Diagnostic Log Summary Generator",
            "description": "Print 'ERROR [101]: Device Timeout' followed by 'RETRYing connection...' on separate lines.",
            "difficulty": "Challenge",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    // Print diagnostic summary\n    return 0;\n}\n",
            "language": "c",
            "order_index": 6,
            "test_cases": [{"input_data": "", "expected_output": "ERROR [101]: Device Timeout\nRETRYing connection...\n", "is_hidden": False, "order_index": 1}]
        }
    ]

    m1_quizzes = [
        {
            "question_text": "Which phase of C compilation handles #include and #define directives before actual code compilation?",
            "options": ["Assembler", "Preprocessor", "Linker", "Loader"],
            "correct_answer": "Preprocessor",
            "explanation": "The preprocessor executes first, expanding header files (#include) and macro directives (#define) into pure C source text before the compiler generates assembly.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What does returning 0 from int main() signal to the operating system?",
            "options": ["Memory allocation failure", "Successful process completion without errors", "Request for process restart", "Compilation syntax warning"],
            "correct_answer": "Successful process completion without errors",
            "explanation": "By OS standard convention, exit code 0 indicates clean process execution, while non-zero values signal specific runtime error codes.",
            "difficulty": "Beginner"
        }
    ,
        {
            "question_text": "Which of the following describes the correct order of C compilation stages?",
            "options": ["Preprocessing, Compilation, Assembly, Linking", "Compilation, Assembly, Linking, Preprocessing", "Preprocessing, Linking, Compilation, Assembly", "Linking, Preprocessing, Compilation, Assembly"],
            "correct_answer": "Preprocessing, Compilation, Assembly, Linking",
            "explanation": "The C compiler pipeline strictly follows: preprocessing (expanding macros), compilation (to assembly), assembly (to machine code), and linking (combining objects into executable).",
            "difficulty": "Medium"
        },
        {
            "question_text": "What is the primary role of the linker in the C compilation process?",
            "options": ["To check for syntax errors", "To convert assembly code into machine code", "To combine multiple object files and resolve library references into a single executable", "To expand #include directives"],
            "correct_answer": "To combine multiple object files and resolve library references into a single executable",
            "explanation": "The linker resolves external symbol references across multiple object files and links standard libraries to produce the final executable binary.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What does a non-zero return value from the main() function indicate to the operating system?",
            "options": ["Successful execution", "An execution error or abnormal termination", "The program is waiting for user input", "Memory leak detected"],
            "correct_answer": "An execution error or abnormal termination",
            "explanation": "By convention, return 0 indicates success, while any non-zero value indicates that an error occurred during execution.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What happens during the preprocessing stage?",
            "options": ["Source code is converted to machine code", "Syntax errors are detected", "Macros are expanded and header files are included directly into the source code", "The executable is generated"],
            "correct_answer": "Macros are expanded and header files are included directly into the source code",
            "explanation": "The preprocessor handles directives like #include and #define before the actual compiler even sees the code.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "Which tool translates C source code into assembly language?",
            "options": ["Preprocessor", "Compiler", "Assembler", "Linker"],
            "correct_answer": "Compiler",
            "explanation": "The compiler specifically translates high-level C code into low-level assembly instructions specific to the target CPU architecture.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What is the purpose of the #include <stdio.h> directive?",
            "options": ["To define the main function", "To include standard input/output function declarations like printf and scanf", "To link the math library", "To compile the program"],
            "correct_answer": "To include standard input/output function declarations like printf and scanf",
            "explanation": "stdio.h contains the declarations for standard I/O functions, allowing the compiler to verify their usage before linking.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What is the difference between a syntax error and a compile error?",
            "options": ["Syntax errors happen at runtime, compile errors happen before execution", "Syntax errors are caused by invalid C grammar; compile errors include syntax errors but can also involve type mismatches", "They are exactly the same thing", "Syntax errors only happen in the linker"],
            "correct_answer": "Syntax errors are caused by invalid C grammar; compile errors include syntax errors but can also involve type mismatches",
            "explanation": "Syntax errors (e.g., missing semicolons) are a subset of compile errors. Compile errors can also occur from invalid types or missing declarations.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What is an object file (.o or .obj)?",
            "options": ["A plain text file containing C code", "The final executable that can be run", "Compiled machine code for a single source file, not yet linked into an executable", "A file containing preprocessor macros"],
            "correct_answer": "Compiled machine code for a single source file, not yet linked into an executable",
            "explanation": "Object files contain machine code but still have unresolved references to external functions, which the linker will resolve later.",
            "difficulty": "Medium"
        }
    ]

    modules.append(build_lesson(
        "C Programming Foundations", "c-foundations",
        m1_what, m1_why, m1_how, m1_syntax, m1_ex_sim, m1_ex_real, m1_out_sim, m1_lbl_sim, m1_out_real, m1_exp_real, m1_mistakes, m1_best, m1_exs, m1_quizzes
    ))

    # =========================================================================
    # MODULE 2: Variables, Data Types & Constants
    # =========================================================================
    m2_what = """A variable is a named memory location allocated in physical RAM to store data values that can be read or modified during program execution. In C, variables are statically typed: every variable must be declared with a specific data type before it can be used.

C primitive data types include:
- `int`: Fixed-size integer (typically 4 bytes / 32 bits on modern systems).
- `float`: Single-precision IEEE 754 floating point number (4 bytes).
- `double`: Double-precision floating point number (8 bytes).
- `char`: Single byte storing an ASCII character code (1 byte / 8 bits).

Constants are immutable values defined using the `const` keyword or preprocessor `#define` directives that cannot be modified after initialization."""

    m2_why = """Computers process information by reading and writing binary bit patterns stored in physical RAM addresses. Without variables, software could not store calculation results, maintain program state, or process dynamic user inputs.

Static typing forces developers to specify exact data types so the compiler knows precisely how many RAM bytes to reserve and how to interpret stored binary bit sequences (e.g. distinguishing integer bit pattern `0x00000041` from float or char `'A'`).

Constants enforce code reliability by preventing accidental mutation of critical physical constants (e.g., PI, max buffer capacities, or system configuration limits)."""

    m2_how = """When you execute `int count = 10;`, the C compiler reserves 4 bytes of contiguous RAM memory for `count` and writes binary `00000000 00000000 00000000 00001010` (integer 10) into those bytes.

```
Variable RAM Memory Mapping:
Variable Identifier: count
Data Type: int (4 Bytes)
RAM Address: 0x7FFF5FBFF028
Memory Content: [ 00000000 | 00000000 | 00000000 | 00001010 ] -> Value: 10
```

The `sizeof()` operator returns the exact hardware byte size allocated for any type or variable on the host architecture. Type modifiers like `unsigned` restrict integers to non-negative numbers, doubling the positive upper bound range achievable within the same bit count."""

    m2_syntax = """int count = 10;
float temperature = 98.6f;
double pi = 3.1415926535;
char grade = 'A';

const int MAX_USERS = 100;
#define BUFFER_SIZE 1024"""

    m2_ex_sim = """#include <stdio.h>

int main(void) {
    int age = 20;
    float height = 5.9f;
    char letter = 'C';

    printf("Age: %d\\n", age);
    printf("Height: %.1f\\n", height);
    printf("Letter: %c\\n", letter);
    printf("Size of int: %zu bytes\\n", sizeof(int));
    return 0;
}"""

    m2_out_sim = """Age: 20
Height: 5.9
Letter: C
Size of int: 4 bytes"""

    m2_lbl_sim = """- `int age = 20;`: Allocates a 4-byte integer variable `age` initialized to 20.
- `float height = 5.9f;`: Allocates a 4-byte single-precision float `height`.
- `char letter = 'C';`: Stores ASCII numeric value 67 (character 'C') in 1 byte of memory.
- `sizeof(int)`: Evaluates to exact RAM byte size reserved for integer type (4 bytes)."""

    m2_ex_real = """#include <stdio.h>

#define MAX_BUFFER 1024

int main(void) {
    const float TAX_RATE = 0.07f;
    double item_price = 49.99;
    double total_cost = item_price + (item_price * TAX_RATE);

    printf("Max Buffer Capacity: %d bytes\\n", MAX_BUFFER);
    printf("Base Price: $%.2f\\n", item_price);
    printf("Total Cost (incl. 7%% Tax): $%.2f\\n", total_cost);
    return 0;
}"""

    m2_out_real = """Max Buffer Capacity: 1024 bytes
Base Price: $49.99
Total Cost (incl. 7% Tax): $53.49"""

    m2_exp_real = """Demonstrates real-world financial transaction calculations using `#define` preprocessor macros for system parameters, `const float` for immutable tax rates, and `double` for precision monetary calculations."""

    m2_mistakes = """1. Using uninitialized variables before assigning values, leading to garbage RAM readings.
2. Assigning float values to integer variables (`int x = 5.99;` truncates `x` to `5` without rounding).
3. Enclosing single characters in double quotes (`"A"` string literal) instead of single quotes (`'A'` char).
4. Reassigning values to a `const` variable (`TAX_RATE = 0.10;`), causing compilation errors."""

    m2_best = """1. Always initialize variables upon declaration (`int score = 0;`).
2. Choose appropriate types: use `double` for financial data, `size_t` for memory sizes, and `char` for text characters.
3. Capitalize macro and constant names (`MAX_CAPACITY`) to distinguish them from mutable variables."""

    m2_exs = [
        {
            "title": "Integer Variable Initializer",
            "description": "Declare an integer `items = 15` and print 'Items Count: 15'.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    // Declare and print items\n    return 0;\n}\n",
            "language": "c",
            "order_index": 1,
            "test_cases": [{"input_data": "", "expected_output": "Items Count: 15\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Double Precision Formatter",
            "description": "Declare double `gpa = 3.854` and print formatted to 2 decimal places: 'GPA: 3.85'.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    // Format double\n    return 0;\n}\n",
            "language": "c",
            "order_index": 2,
            "test_cases": [{"input_data": "", "expected_output": "GPA: 3.85\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "ASCII Code Extractor",
            "description": "Declare `char ch = 'Z'`. Print character and ASCII integer value: 'Char: Z, ASCII: 90'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    // Print char and ASCII code\n    return 0;\n}\n",
            "language": "c",
            "order_index": 3,
            "test_cases": [{"input_data": "", "expected_output": "Char: Z, ASCII: 90\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Memory sizeof Inspector",
            "description": "Print byte sizes of `char`, `int`, `double` as 'char: 1, int: 4, double: 8'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    printf(\"char: %zu, int: %zu, double: %zu\\n\", sizeof(char), sizeof(int), sizeof(double));\n    return 0;\n}\n",
            "language": "c",
            "order_index": 4,
            "test_cases": [{"input_data": "", "expected_output": "char: 1, int: 4, double: 8\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Constant Macro Tax Calculator",
            "description": "Use `#define RATE 0.10`. For price 200.0, compute tax (20.0) and print: 'Tax Amount: $20.00'.",
            "difficulty": "Hard",
            "starter_code": "#include <stdio.h>\n// Define RATE here\n\nint main(void) {\n    // Compute and print tax\n    return 0;\n}\n",
            "language": "c",
            "order_index": 5,
            "test_cases": [{"input_data": "", "expected_output": "Tax Amount: $20.00\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Explicit Type Casting Average Evaluator",
            "description": "Given integers `total = 17` and `count = 2`, cast to `(double)` to print exact average: 'Average: 8.50'.",
            "difficulty": "Challenge",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int total = 17, count = 2;\n    // Explicit cast and print\n    return 0;\n}\n",
            "language": "c",
            "order_index": 6,
            "test_cases": [{"input_data": "", "expected_output": "Average: 8.50\n", "is_hidden": False, "order_index": 1}]
        }
    ]

    m2_quizzes = [
        {
            "question_text": "What occurs when you assign floating point value 7.89 to an int variable in C?",
            "options": ["Compilation error", "The value is truncated to integer 7 without rounding", "The value rounds up to 8", "Memory segmentation fault"],
            "correct_answer": "The value is truncated to integer 7 without rounding",
            "explanation": "C integer assignment strips all decimal fractional digits, truncating 7.89 down to integer 7.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "Which operator determines the memory footprint in bytes of a data type or variable in C?",
            "options": ["lengthof", "memsize", "sizeof", "addrof"],
            "correct_answer": "sizeof",
            "explanation": "The sizeof operator reports the exact memory byte count allocated for types, variables, or expressions.",
            "difficulty": "Beginner"
        }
    ,
        {
            "question_text": "What determines the size of an int variable in C?",
            "options": ["It is always 4 bytes", "It depends on the compiler and target architecture", "It is always 8 bytes", "It depends on the value assigned to it"],
            "correct_answer": "It depends on the compiler and target architecture",
            "explanation": "The C standard guarantees an int is at least 16 bits, but it is typically 32 bits (4 bytes) on modern architectures, depending on the compiler.",
            "difficulty": "Medium"
        },
        {
            "question_text": "Which format specifier is used to print a double precision floating-point number?",
            "options": ["%d", "%f", "%lf", "%c"],
            "correct_answer": "%lf",
            "explanation": "%lf is used in scanf for double, and while %f works in printf for double (due to promotion), %lf explicitly denotes a long float (double).",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What is the purpose of the 'const' keyword?",
            "options": ["To declare a variable whose value cannot be changed after initialization", "To make a variable accessible globally", "To allocate memory on the heap", "To increase execution speed"],
            "correct_answer": "To declare a variable whose value cannot be changed after initialization",
            "explanation": "const prevents reassignment of a variable, ensuring read-only behavior throughout its scope.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What happens if you assign a floating-point value to an integer variable (e.g., int x = 3.14)?",
            "options": ["The compiler throws an error", "The value is rounded to the nearest integer (3)", "The fractional part is truncated, storing just the whole number (3)", "The variable type dynamically changes to float"],
            "correct_answer": "The fractional part is truncated, storing just the whole number (3)",
            "explanation": "C performs implicit type conversion, truncating (dropping) the decimal portion without rounding.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What is the range of a standard signed 8-bit char?",
            "options": ["0 to 255", "-128 to 127", "-256 to 255", "0 to 127"],
            "correct_answer": "-128 to 127",
            "explanation": "A signed 8-bit integer uses one bit for the sign, leaving 7 bits for the magnitude, spanning from -128 to 127.",
            "difficulty": "Hard"
        },
        {
            "question_text": "Which of the following is a valid C variable name?",
            "options": ["1st_number", "first-number", "_first_number", "first number"],
            "correct_answer": "_first_number",
            "explanation": "Variable names can contain letters, numbers, and underscores, but cannot start with a number or contain spaces/hyphens.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What is the result of sizeof(char) in C?",
            "options": ["It depends on the architecture", "Exactly 1", "Exactly 2", "Exactly 4"],
            "correct_answer": "Exactly 1",
            "explanation": "The C standard explicitly defines sizeof(char) to be exactly 1 byte across all architectures.",
            "difficulty": "Medium"
        },
        {
            "question_text": "Which data type is most appropriate to store the population of the entire world (approx 8 billion)?",
            "options": ["int", "long", "long long", "float"],
            "correct_answer": "long long",
            "explanation": "A standard 32-bit int maxes out at ~2.1 billion. A 64-bit long long safely holds up to ~9 quintillion.",
            "difficulty": "Hard"
        }
    ]

    modules.append(build_lesson(
        "Variables, Data Types & Constants", "c-variables-types-constants",
        m2_what, m2_why, m2_how, m2_syntax, m2_ex_sim, m2_ex_real, m2_out_sim, m2_lbl_sim, m2_out_real, m2_exp_real, m2_mistakes, m2_best, m2_exs, m2_quizzes
    ))

    # =========================================================================
    # MODULE 3: Input, Output & Operators
    # =========================================================================
    m3_what = """Input/Output (I/O) functions allow programs to exchange data with users via standard console streams (stdin/stdout). `printf()` prints formatted data, while `scanf()` reads formatted text from stdin.

Operators perform computations on data operands:
- Arithmetic: `+`, `-`, `*`, `/`, `%` (modulo remainder).
- Relational: `==`, `!=`, `<`, `>`, `<=`, `>=`.
- Logical: `&&` (AND), `||` (OR), `!` (NOT).
- Bitwise: `&`, `|`, `^`, `~`, `<<`, `>>`.
- Assignment & Increment: `=`, `+=`, `-=`, `++`, `--`.

Format specifiers (`%d` for int, `%f` for float, `%lf` for double, `%c` for char, `%s` for string) serve as placeholders during I/O formatting."""

    m3_why = """Programs must process external user inputs, execute mathematical calculations, and display readable outputs. Without I/O and operators, software would be static and unable to interact with external environments.

Operators form the core building blocks of mathematical formulas, condition evaluations, and hardware register manipulations.

Understanding `scanf("%d", &var)` introduces the critical concept of passing memory addresses (`&var`) so functions can write data directly into caller RAM variables."""

    m3_how = """Executing `scanf("%d", &num);` receives character input from stdin, converts ascii digits to binary integer format, and writes that binary value into the RAM memory address of `num`.

Modulo operator `%` computes the integer remainder after division (`17 % 5` equals `2`).

Logical AND `&&` evaluates true (non-zero) only when both operands are non-zero, utilizing short-circuit evaluation (if first operand is false, second operand is skipped)."""

    m3_syntax = """int x, y;
printf("Enter two numbers: ");
scanf("%d %d", &x, &y);

int sum = x + y;
int remainder = x % y;
int is_valid = (x > 0) && (y > 0);"""

    m3_ex_sim = """#include <stdio.h>

int main(void) {
    int a = 17, b = 5;
    printf("Sum: %d\\n", a + b);
    printf("Quotient: %d\\n", a / b);
    printf("Remainder: %d\\n", a % b);
    return 0;
}"""

    m3_out_sim = """Sum: 22
Quotient: 3
Remainder: 2"""

    m3_lbl_sim = """- `printf("Sum: %d\n", a + b);`: Adds 17 + 5 and formats result into `%d`.
- `a / b`: Integer division `17 / 5` truncates decimal, yielding `3`.
- `a % b`: Modulo returns division remainder (`17 % 5` leaves `2`)."""

    m3_ex_real = """#include <stdio.h>

int main(void) {
    int flags = 12; // Binary 00001100
    int is_even = (flags % 2 == 0);
    int shifted = flags << 2; // Shift left 2 bits (multiply by 4 -> 48)

    printf("Flag Value: %d | Is Even: %d\\n", flags, is_even);
    printf("Bitwise Left Shift (x4): %d\\n", shifted);
    return 0;
}"""

    m3_out_real = """Flag Value: 12 | Is Even: 1
Bitwise Left Shift (x4): 48"""

    m3_exp_real = """Demonstrates relational modulo check for parity testing and bitwise left shift operator (`<<`) for high-performance hardware integer multiplication."""

    m3_mistakes = """1. Omitting the ampersand `&` in `scanf("%d", &var);`, causing invalid memory address crashes.
2. Confusing assignment `=` with relational equality `==` (`if (x = 5)` assigns 5 and evaluates true!).
3. Expecting floating point result from integer division (`5 / 2` yields `2`, not `2.5`).
4. Using single `&` or `|` (bitwise) when logical `&&` or `||` was intended."""

    m3_best = """1. Always check `scanf` return value to confirm input parsing succeeded.
2. Parenthesize complex expressions to ensure correct operator precedence.
3. Add spaces around binary operators (`x + y`) for optimal visual readability."""

    m3_exs = [
        {
            "title": "Interactive Sum Calculator",
            "description": "Read two integers from input (e.g. '12 28') and print 'Sum = 40'.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int a, b;\n    if (scanf(\"%d %d\", &a, &b) == 2) {\n        // Print sum\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 1,
            "test_cases": [{"input_data": "12 28\n", "expected_output": "Sum = 40\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Modulo Remainder Evaluator",
            "description": "Read an integer (e.g. '19') and print 'Remainder = 4' when divided by 5.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int num;\n    if (scanf(\"%d\", &num) == 1) {\n        // Print remainder when divided by 5\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 2,
            "test_cases": [{"input_data": "19\n", "expected_output": "Remainder = 4\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Logical Range Bounds Evaluator",
            "description": "Read integer `x`. Print '1' if `(x >= 10 && x <= 50)` else print '0'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int x;\n    if (scanf(\"%d\", &x) == 1) {\n        // Check range\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 3,
            "test_cases": [{"input_data": "25\n", "expected_output": "1\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Bitwise Left Shift Doubler",
            "description": "Read integer `val` (e.g. '9') and print 'Shifted = 18' using `val << 1`.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int val;\n    if (scanf(\"%d\", &val) == 1) {\n        // Bitwise left shift\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 4,
            "test_cases": [{"input_data": "9\n", "expected_output": "Shifted = 18\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Pre vs Post Increment Evaluator",
            "description": "Initialize `a = 5`. Compute `b = ++a` and `c = a++`. Print 'a=7, b=6, c=6'.",
            "difficulty": "Hard",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int a = 5;\n    // Implement pre and post increment\n    return 0;\n}\n",
            "language": "c",
            "order_index": 5,
            "test_cases": [{"input_data": "", "expected_output": "a=7, b=6, c=6\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Ternary Max Evaluator",
            "description": "Read two integers `a` and `b` (e.g. '50 20'). Print 'Max = 50' using ternary operator `?:`.",
            "difficulty": "Challenge",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int a, b;\n    if (scanf(\"%d %d\", &a, &b) == 2) {\n        // Use ternary operator\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 6,
            "test_cases": [{"input_data": "50 20\n", "expected_output": "Max = 50\n", "is_hidden": False, "order_index": 1}]
        }
    ]

    m3_quizzes = [
        {
            "question_text": "Why must you pass &num to scanf(\"%d\", &num)?",
            "options": ["To pass variable value", "To provide the memory RAM address where scanf writes the parsed integer", "To clear input buffer", "To convert integer to string"],
            "correct_answer": "To provide the memory RAM address where scanf writes the parsed integer",
            "explanation": "scanf requires a pointer address (&num) so it can directly write parsed console input into caller RAM memory.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What is the evaluated output of integer division 11 / 4 in C?",
            "options": ["2.75", "2", "3", "Undefined error"],
            "correct_answer": "2",
            "explanation": "C integer division truncates fractional decimal digits toward zero, producing integer 2.",
            "difficulty": "Beginner"
        }
    ,
        {
            "question_text": "What is the result of the expression 5 / 2 in C?",
            "options": ["2.5", "2", "3", "Error"],
            "correct_answer": "2",
            "explanation": "When both operands are integers, C performs integer division, which truncates the fractional part.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What does the modulo operator '%' do?",
            "options": ["Calculates percentage", "Performs integer division", "Returns the remainder of integer division", "Raises a number to a power"],
            "correct_answer": "Returns the remainder of integer division",
            "explanation": "The % operator computes the remainder when the first integer is divided by the second (e.g., 5 % 2 = 1).",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What is the difference between prefix (++i) and postfix (i++) increment?",
            "options": ["There is no difference", "Prefix increments first then returns the value; postfix returns the original value then increments", "Postfix increments first then returns the value; prefix returns the original value then increments", "Prefix is used for integers, postfix for floats"],
            "correct_answer": "Prefix increments first then returns the value; postfix returns the original value then increments",
            "explanation": "Prefix evaluates to the new incremented value immediately. Postfix evaluates to the old value before incrementing.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What will printf('%5d', 12) output?",
            "options": ["12000", "00012", "   12", "12   "],
            "correct_answer": "   12",
            "explanation": "The %5d format specifies a minimum width of 5 characters, right-aligned, padded with spaces on the left.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What is required before using scanf() to read into a standard integer variable `int x`?",
            "options": ["The variable must be initialized to 0", "You must pass the variable's memory address using the & operator", "You must cast the variable to a string", "You must allocate heap memory"],
            "correct_answer": "You must pass the variable's memory address using the & operator",
            "explanation": "scanf needs the memory address (&x) to directly write the read value into the variable's memory location.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "Which operator has the highest precedence?",
            "options": ["Assignment (=)", "Addition (+)", "Multiplication (*)", "Logical AND (&&)"],
            "correct_answer": "Multiplication (*)",
            "explanation": "Multiplication (*) has higher precedence than addition (+), logical AND (&&), and assignment (=).",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What is the result of the bitwise XOR expression `5 ^ 3` (binary 0101 ^ 0011)?",
            "options": ["6", "2", "7", "1"],
            "correct_answer": "6",
            "explanation": "XOR compares bits: 0101 ^ 0011 = 0110 (decimal 6). Bits are 1 if they differ, 0 if they are the same.",
            "difficulty": "Hard"
        },
        {
            "question_text": "What is short-circuit evaluation in logical operators?",
            "options": ["The compiler removes unused variables", "Logical expressions stop evaluating as soon as the final result is determined", "The program crashes if a boolean condition is too complex", "Division by zero bypasses the operation"],
            "correct_answer": "Logical expressions stop evaluating as soon as the final result is determined",
            "explanation": "In an expression like (A && B), if A is false, B is never evaluated because the entire expression is already guaranteed to be false.",
            "difficulty": "Hard"
        }
    ]

    # Stage 1 Project definition for Module 3
    m3_project = {
        "title": "Console Calculator & Unit Converter",
        "scenario": "You are developing a lightweight command-line utility for an embedded device that performs basic arithmetic operations and metric unit conversions.",
        "objective": "Build a C program that receives operation selection code and operands, returning calculated double results formatted to 2 decimal places.",
        "requirements": ["Accept two numeric inputs and operation code", "Perform Addition (1), Subtraction (2), Multiplication (3), Division (4)", "Protect against division by zero"],
        "features": ["Arithmetic Calculation Engine", "Zero Division Guard"],
        "required_concepts": ["Variables", "Input/Output", "Operators", "Conditionals"],
        "architecture": "Single module CLI application with input validation and formatted output.",
        "guidance": ["Use scanf with %lf format specifiers for double input", "Verify divisor != 0 before dividing"],
        "hints": ["Check if b == 0 before performing division"],
        "workflow": "Input operands -> Read op code -> Branch computation -> Print result",
        "expected_behavior": "Input: '10 4 1' (Add) -> Outputs 'Result: 14.00'\nInput: '10 4 4' (Divide) -> Outputs 'Result: 2.50'",
        "evaluation_criteria": "Program accurately executes selected arithmetic operations and safely handles division.",
        "starter_code": "#include <stdio.h>\n\nint main(void) {\n    double a, b;\n    int op;\n    if (scanf(\"%lf %lf %d\", &a, &b, &op) == 3) {\n        // Implement calculator\n    }\n    return 0;\n}\n",
        "language": "c",
        "test_cases": [
            {"input_data": "10 4 1\n", "expected_output": "Result: 14.00\n", "is_hidden": False, "order_index": 1},
            {"input_data": "10 4 4\n", "expected_output": "Result: 2.50\n", "is_hidden": False, "order_index": 2}
        ]
    }

    modules.append(build_lesson(
        "Input, Output & Operators", "c-input-output-operators",
        m3_what, m3_why, m3_how, m3_syntax, m3_ex_sim, m3_ex_real, m3_out_sim, m3_lbl_sim, m3_out_real, m3_exp_real, m3_mistakes, m3_best, m3_exs, m3_quizzes, m3_project
    ))

    # =========================================================================
    # MODULE 4: Conditional Statements
    # =========================================================================
    m4_what = """Conditional statements control program decision-making by executing specific code blocks based on whether logical conditions evaluate to true or false.

C supports:
- `if`: Executes block if condition is non-zero (true).
- `if-else`: Executes first block if true, second block if false.
- `else if`: Evaluates sequential conditions in a decision ladder.
- `switch-case`: Selects execution branch based on integer or char expressions.
- Ternary operator `?:`: Short-hand inline conditional expression (`condition ? val1 : val2`).

In C, boolean logic is integral: integer `0` represents false, while ANY non-zero integer (like `1`, `-5`, or `100`) represents true."""

    m4_why = """Software must adapt dynamically to varying data conditions: authenticating passwords, validating user form inputs, processing menu choices, and handling runtime error states.

`switch-case` statements provide high-performance multi-branch dispatching by compiling directly into CPU jump tables rather than evaluating sequential `if` checks.

Mastering conditional branches ensures software safely handles all boundary edge cases."""

    m4_how = """When `if (score >= 60)` evaluates:
1. CPU executes comparison instruction setting ALU status flags.
2. If flag is non-zero (true), execution enters `{}` block.
3. If flag is zero (false), execution skips block or enters `else`.

In a `switch(choice)` block, CPU jumps directly to matching `case` label. Omitting `break;` causes execution to fall through into subsequent case labels."""

    m4_syntax = """if (score >= 90) {
    printf("Grade A\\n");
} else if (score >= 70) {
    printf("Grade B\\n");
} else {
    printf("Grade C\\n");
}

switch (option) {
    case 1:
        printf("Start Game\\n");
        break;
    case 2:
        printf("Load Game\\n");
        break;
    default:
        printf("Invalid Option\\n");
        break;
}"""

    m4_ex_sim = """#include <stdio.h>

int main(void) {
    int age = 20;
    if (age >= 18) {
        printf("Access Granted: Eligible\\n");
    } else {
        printf("Access Denied: Ineligible\\n");
    }
    return 0;
}"""

    m4_out_sim = """Access Granted: Eligible"""

    m4_lbl_sim = """- `if (age >= 18)`: Evaluates whether variable age (20) is >= 18 (true).
- `{ printf(...); }`: Executes access granted code block.
- `else`: Skipped because if condition evaluated true."""

    m4_ex_real = """#include <stdio.h>

int main(void) {
    char role = 'B';
    switch (role) {
        case 'A':
            printf("Permission Level: Administrator\\n");
            break;
        case 'B':
            printf("Permission Level: Developer\\n");
            break;
        default:
            printf("Permission Level: Guest\\n");
            break;
    }
    return 0;
}"""

    m4_out_real = """Permission Level: Developer"""

    m4_exp_real = """Demonstrates role-based access permission checking using a character switch-case block, ensuring clean multi-branch execution with `break` guards."""

    m4_mistakes = """1. Using assignment `=` instead of relational equality `==` (`if (x = 5)` sets x to 5 and evaluates true!).
2. Omitting `break;` in switch cases causing fall-through bugs into subsequent case blocks.
3. Placing semicolon immediately after if condition (`if (x > 0);`), executing body unconditionally."""

    m4_best = """1. Always use curly braces `{}` even for single-line `if` bodies.
2. Include a `default:` label in every `switch` statement to handle unexpected values.
3. Break complex conditional trees into boolean helper variables for clean maintenance."""

    m4_exs = [
        {
            "title": "Number Sign Classifier",
            "description": "Read integer input. Print 'Positive' if > 0, 'Negative' if < 0, or 'Zero' if 0.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        // Classify number sign\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 1,
            "test_cases": [{"input_data": "-7\n", "expected_output": "Negative\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Leap Year Evaluator",
            "description": "Read year (e.g. 2024). Print 'Leap Year' if divisible by 4 (and not 100 unless 400), else 'Not Leap Year'.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int year;\n    if (scanf(\"%d\", &year) == 1) {\n        // Leap year logic\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 2,
            "test_cases": [{"input_data": "2024\n", "expected_output": "Leap Year\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Score Grade Classifier",
            "description": "Read score 0-100. Print 'A' (>=90), 'B' (>=80), 'C' (>=70), 'D' (>=60), or 'F' (<60).",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int score;\n    if (scanf(\"%d\", &score) == 1) {\n        // Grade ladder\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 3,
            "test_cases": [{"input_data": "85\n", "expected_output": "B\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Switch Day Printer",
            "description": "Read day integer 1-7. Use switch to print 'Monday' (1)... or 'Invalid' if outside 1-7.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int day;\n    if (scanf(\"%d\", &day) == 1) {\n        // Switch statement\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 4,
            "test_cases": [{"input_data": "3\n", "expected_output": "Wednesday\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "2D Quadrant Classifier",
            "description": "Read x y coordinates. Print 'Q1' (x>0,y>0), 'Q2' (x<0,y>0), 'Q3' (x<0,y<0), 'Q4' (x>0,y<0), or 'Axis'.",
            "difficulty": "Hard",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int x, y;\n    if (scanf(\"%d %d\", &x, &y) == 2) {\n        // Quadrant logic\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 5,
            "test_cases": [{"input_data": "-4 5\n", "expected_output": "Q2\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Triangle Type Validator",
            "description": "Read 3 side lengths. Verify triangle inequality (a+b>c). Print 'Equilateral', 'Isosceles', 'Scalene', or 'Invalid'.",
            "difficulty": "Challenge",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int a, b, c;\n    if (scanf(\"%d %d %d\", &a, &b, &c) == 3) {\n        // Triangle type check\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 6,
            "test_cases": [{"input_data": "5 5 5\n", "expected_output": "Equilateral\n", "is_hidden": False, "order_index": 1}]
        }
    ]

    m4_quizzes = [
        {
            "question_text": "What occurs when a break statement is omitted inside a switch case block?",
            "options": ["Compilation error", "Execution falls through into subsequent case blocks", "Program process exits immediately", "Switch condition restarts"],
            "correct_answer": "Execution falls through into subsequent case blocks",
            "explanation": "Without break guards, C switch execution continues executing statements in matching lower case blocks.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "How does C evaluate the condition expression inside if (-10)?",
            "options": ["False because -10 is negative", "True because -10 is non-zero", "Syntax Error", "Undefined runtime crash"],
            "correct_answer": "True because -10 is non-zero",
            "explanation": "In C boolean evaluation, 0 is false, and ANY non-zero integer (positive or negative) evaluates as true.",
            "difficulty": "Beginner"
        }
    ,
        {
            "question_text": "What is the correct syntax for an 'if-else if' statement?",
            "options": ["if (cond) { } elseif (cond) { }", "if (cond) { } else if (cond) { }", "if (cond) { } elif (cond) { }", "if cond { } else if cond { }"],
            "correct_answer": "if (cond) { } else if (cond) { }",
            "explanation": "C requires space between else and if, and conditions must be enclosed in parentheses.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What does a 'switch' statement require for each case to prevent fall-through?",
            "options": ["A continue statement", "A return statement", "A break statement", "A semicolon"],
            "correct_answer": "A break statement",
            "explanation": "Without a break statement, execution will 'fall through' and execute the code for subsequent cases.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "Which operator evaluates a condition inline as a shorthand for if-else?",
            "options": ["Bitwise OR (|)", "Ternary operator (? :)", "Logical AND (&&)", "Switch operator (->)"],
            "correct_answer": "Ternary operator (? :)",
            "explanation": "The ternary operator (condition ? true_val : false_val) evaluates inline, returning one of two values.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What happens if a switch expression evaluates to a value not explicitly handled by any 'case'?",
            "options": ["The program crashes", "The compiler throws an error", "Execution jumps to the 'default' case if provided, otherwise the block is skipped", "The first case is executed by default"],
            "correct_answer": "Execution jumps to the 'default' case if provided, otherwise the block is skipped",
            "explanation": "The default case acts as a fallback for unhandled values. If it's missing, the switch block is safely bypassed.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "In C, what integer value represents 'true' in a boolean condition?",
            "options": ["Only 1", "Only -1", "Any non-zero value", "Any positive value"],
            "correct_answer": "Any non-zero value",
            "explanation": "C natively treats 0 as false and absolutely any non-zero value (positive or negative) as true.",
            "difficulty": "Medium"
        },
        {
            "question_text": "Can a switch statement evaluate a string variable (char array) in C?",
            "options": ["Yes, using strcmp internally", "Yes, natively", "No, switch statements in C only evaluate integer and character constant expressions", "No, unless cast to a double"],
            "correct_answer": "No, switch statements in C only evaluate integer and character constant expressions",
            "explanation": "C's switch statement strictly evaluates integral types (char, int, enum) against compile-time constants. It cannot evaluate strings.",
            "difficulty": "Hard"
        },
        {
            "question_text": "What is a common pitfall involving the assignment operator in if statements, e.g., if(x = 5)?",
            "options": ["It compares x to 5", "It causes a syntax error", "It assigns 5 to x and evaluates as true, ignoring the original value of x", "It checks if x was previously assigned"],
            "correct_answer": "It assigns 5 to x and evaluates as true, ignoring the original value of x",
            "explanation": "The single = is assignment, not comparison (==). The assignment evaluates to 5, which is non-zero (true).",
            "difficulty": "Hard"
        },
        {
            "question_text": "Is the 'else' block mandatory in an if statement?",
            "options": ["Yes", "No", "Only if there is no break statement", "Only if returning a value"],
            "correct_answer": "No",
            "explanation": "An 'if' block can stand alone. The 'else' block is completely optional.",
            "difficulty": "Beginner"
        }
    ]

    modules.append(build_lesson(
        "Conditional Statements", "c-conditional-statements",
        m4_what, m4_why, m4_how, m4_syntax, m4_ex_sim, m4_ex_real, m4_out_sim, m4_lbl_sim, m4_out_real, m4_exp_real, m4_mistakes, m4_best, m4_exs, m4_quizzes
    ))

    # =========================================================================
    # MODULE 5: Loops & Problem Solving
    # =========================================================================
    m5_what = """Loops repeatedly execute a code block until a termination condition evaluates to false.

C supports three primary loop constructs:
- `for` loop: Used when the iteration count is known in advance (`for (init; condition; update)`).
- `while` loop: Pre-test loop executing while condition remains true (`while (condition)`).
- `do-while` loop: Post-test loop guaranteeing execution at least once (`do { ... } while (condition);`).

Loop control keywords `break` (exits loop immediately) and `continue` (bypasses remaining statements in current pass and advances to next iteration) govern loop execution flow."""

    m5_why = """Computers excel at high-speed repetitive operations: processing array collections, computing mathematical algorithms (factorials, Fibonacci), reading stream buffers, and executing event polling loops.

Without loops, performing an operation 10,000 times would require duplicating code 10,000 times—a completely unmaintainable approach.

Developing loop problem-solving skills lays the algorithmic foundation for sorting algorithms, matrix transformations, and dynamic data structures."""

    m5_how = """In a `for (int i = 0; i < N; i++)` loop:
1. Init: `int i = 0` initializes loop index once.
2. Condition: `i < N` checked before each iteration.
3. Body: Code inside `{}` executes if condition is true.
4. Update: `i++` executes after body, returning to condition check.

```
For Loop Execution Sequence:
[ Init: i=0 ] ---> [ Check: i < N? ] ---(True)---> [ Execute Body ]
                         ^                                |
                         |-------[ Update: i++ ] <--------|
                         |
                      (False)
                         v
                  [ Exit Loop ]
```"""

    m5_syntax = """for (int i = 0; i < 5; i++) {
    printf("i = %d\\n", i);
}

int count = 0;
while (count < 3) {
    printf("count = %d\\n", count);
    count++;
}

int x = 10;
do {
    printf("x = %d\\n", x);
    x--;
} while (x > 8);"""

    m5_ex_sim = """#include <stdio.h>

int main(void) {
    int sum = 0;
    for (int i = 1; i <= 5; i++) {
        sum += i;
    }
    printf("Sum 1..5 = %d\\n", sum);
    return 0;
}"""

    m5_out_sim = """Sum 1..5 = 15"""

    m5_lbl_sim = """- `for (int i = 1; i <= 5; i++)`: Loop index i starts at 1, increments each step, and terminates when i exceeds 5.
- `sum += i;`: Accumulates current index i value into running variable `sum`."""

    m5_ex_real = """#include <stdio.h>

int main(void) {
    int num = 5;
    long long factorial = 1;
    int i = num;

    while (i > 0) {
        factorial *= i;
        i--;
    }
    printf("Factorial of %d = %lld\\n", num, factorial);
    return 0;
}"""

    m5_out_real = """Factorial of 5 = 120"""

    m5_exp_real = """Calculates mathematical factorial of 5 (5 * 4 * 3 * 2 * 1 = 120) using a decrementing while loop."""

    m5_mistakes = """1. Creating accidental infinite loops by forgetting to increment/decrement loop counters inside `while` bodies.
2. Off-by-one errors (using `< N` instead of `<= N` or vice-versa).
3. Placing semicolon after loop statement (`while (i < 10);`), trapping execution in an empty infinite loop."""

    m5_best = """1. Prefer `for` loops when iteration counts are known beforehand.
2. Ensure loop termination conditions are guaranteed to eventually evaluate to false.
3. Keep loop body execution blocks clean and modular."""

    m5_exs = [
        {
            "title": "Sum of First N Natural Numbers",
            "description": "Read integer N (e.g. 10). Compute sum 1..N and print 'Sum = 55'.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        // Calculate sum\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 1,
            "test_cases": [{"input_data": "10\n", "expected_output": "Sum = 55\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Multiplication Table Generator",
            "description": "Read `num` (e.g. 3). Print multiplication table 3x1=3 through 3x5=15.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int num;\n    if (scanf(\"%d\", &num) == 1) {\n        // Print table up to x5\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 2,
            "test_cases": [{"input_data": "3\n", "expected_output": "3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Digit Reverse Calculator",
            "description": "Read integer (e.g. 1234). Reverse digits using `% 10` and `/ 10` to print 'Reversed = 4321'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        // Reverse digits\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 3,
            "test_cases": [{"input_data": "1234\n", "expected_output": "Reversed = 4321\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Prime Number Validator",
            "description": "Read integer (e.g. 17). Print 'Prime' if prime, else 'Not Prime'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        // Prime test\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 4,
            "test_cases": [{"input_data": "17\n", "expected_output": "Prime\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Fibonacci Sequence Generator",
            "description": "Read terms count N (e.g. 6). Print first N terms space-separated: '0 1 1 2 3 5 '.",
            "difficulty": "Hard",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        // Print Fibonacci sequence\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 5,
            "test_cases": [{"input_data": "6\n", "expected_output": "0 1 1 2 3 5 \n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "GCD Euclid Algorithm",
            "description": "Read two integers `a` `b` (e.g. 48 18). Calculate greatest common divisor: 'GCD = 6'.",
            "difficulty": "Challenge",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int a, b;\n    if (scanf(\"%d %d\", &a, &b) == 2) {\n        // Euclid GCD algorithm\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 6,
            "test_cases": [{"input_data": "48 18\n", "expected_output": "GCD = 6\n", "is_hidden": False, "order_index": 1}]
        }
    ]

    m5_quizzes = [
        {
            "question_text": "What is the key functional difference between a while loop and a do-while loop?",
            "options": ["do-while checks condition at end, guaranteeing loop body executes at least once", "while loop runs faster in hardware", "do-while cannot use break", "while loop counts backwards"],
            "correct_answer": "do-while checks condition at end, guaranteeing loop body executes at least once",
            "explanation": "do-while is a post-test loop, evaluating the condition after executing the body, ensuring at least 1 execution pass.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What does the continue statement do when executed inside a loop?",
            "options": ["Terminates the loop entirely", "Bypasses remaining statements in current pass and advances to next iteration", "Restarts process main", "Pauses execution"],
            "correct_answer": "Bypasses remaining statements in current pass and advances to next iteration",
            "explanation": "continue immediately skips the rest of the current iteration body, jumping straight to the loop increment/condition step.",
            "difficulty": "Beginner"
        }
    ,
        {
            "question_text": "What is the main difference between a while loop and a do-while loop?",
            "options": ["A while loop uses less memory", "A do-while loop guarantees the loop body executes at least once", "A while loop is faster", "A do-while loop cannot use a break statement"],
            "correct_answer": "A do-while loop guarantees the loop body executes at least once",
            "explanation": "Because a do-while loop evaluates its condition at the bottom of the loop, the block always runs at least one time.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "Which looping construct is specifically designed for iterating a known, fixed number of times?",
            "options": ["while loop", "do-while loop", "for loop", "goto loop"],
            "correct_answer": "for loop",
            "explanation": "A for loop encapsulates initialization, condition checking, and incrementing in a single line, making it ideal for fixed-count iterations.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What does the 'continue' statement do inside a loop?",
            "options": ["Exits the entire loop immediately", "Skips the rest of the current iteration and immediately evaluates the loop condition for the next iteration", "Pauses execution for user input", "Jumps to the beginning of the program"],
            "correct_answer": "Skips the rest of the current iteration and immediately evaluates the loop condition for the next iteration",
            "explanation": "Unlike 'break' which exits the loop entirely, 'continue' just aborts the current pass and advances to the next one.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What happens if a loop condition evaluates to true endlessly (e.g., while(1))?",
            "options": ["The compiler catches the error and refuses to compile", "The program executes exactly 1000 times and then crashes", "An infinite loop occurs, executing until manually terminated or interrupted by the OS", "The loop is bypassed entirely"],
            "correct_answer": "An infinite loop occurs, executing until manually terminated or interrupted by the OS",
            "explanation": "C will happily execute an infinite loop forever unless a break statement is hit or external forces kill the process.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "In a for loop: `for(init; cond; inc)`, when is the `inc` (increment) section executed?",
            "options": ["Before the loop condition is checked for the very first time", "At the very end of each iteration, after the loop body has executed", "At the very beginning of the loop body", "Only when the condition evaluates to false"],
            "correct_answer": "At the very end of each iteration, after the loop body has executed",
            "explanation": "The loop runs its body, then executes the increment expression, and finally re-evaluates the condition.",
            "difficulty": "Medium"
        },
        {
            "question_text": "Can you declare a variable inside the initialization statement of a C99 for loop?",
            "options": ["Yes, e.g., for(int i=0; i<5; i++)", "No, variables must always be declared at the top of the function", "Only if it is a float", "Only if you include <stdlib.h>"],
            "correct_answer": "Yes, e.g., for(int i=0; i<5; i++)",
            "explanation": "Since the C99 standard, loop-scoped variable declarations inside the for loop init block are natively supported.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What is the output of this loop: `for(int i=0; i<3; i++) { if(i==1) break; printf('%d', i); }`",
            "options": ["012", "0", "1", "01"],
            "correct_answer": "0",
            "explanation": "The loop prints 0, then on the next iteration i=1, the break statement immediately terminates the entire loop before printing.",
            "difficulty": "Hard"
        },
        {
            "question_text": "Nested loops execute how?",
            "options": ["The outer loop completes all iterations before the inner loop starts", "The inner loop completes all of its iterations for every single iteration of the outer loop", "They execute in parallel asynchronously", "The inner loop executes once per outer loop iteration"],
            "correct_answer": "The inner loop completes all of its iterations for every single iteration of the outer loop",
            "explanation": "For every tick of the outer loop, the inner loop fires up and completes its entire cycle.",
            "difficulty": "Medium"
        }
    ]

    modules.append(build_lesson(
        "Loops & Problem Solving", "c-loops-problem-solving",
        m5_what, m5_why, m5_how, m5_syntax, m5_ex_sim, m5_ex_real, m5_out_sim, m5_lbl_sim, m5_out_real, m5_exp_real, m5_mistakes, m5_best, m5_exs, m5_quizzes
    ))

    # =========================================================================
    # MODULE 6: Functions & Recursion
    # =========================================================================
    m6_what = """Functions are reusable, self-contained code modules that accept input parameters, execute computations, and return a result value to the caller. A function prototype declares the function signature (return type, name, parameters) before its full definition.

Recursion occurs when a function calls itself to break down a complex problem into smaller identical sub-problems. Every recursive function requires a base case condition to terminate recursive self-invocation and prevent stack overflow memory crashes."""

    m6_why = """Functions enforce modularity, code reuse, and clean abstraction. Rather than repeating complex logic across a codebase, you encapsulate logic inside a single named function.

Variables declared inside a function reside in its local CPU call stack frame. When the function returns, its stack frame is popped off CPU RAM, destroying local variables and preventing memory pollution.

Recursion provides mathematical solutions for hierarchical problems like tree traversals, quicksort, and divide-and-conquer algorithms."""

    m6_how = """CPU Function Execution & Call Stack Mechanics:
When `add(a, b)` is invoked:
1. Arguments are copied into parameter registers (pass-by-value).
2. A new Stack Frame is pushed onto CPU Call Stack containing return address and local variables.
3. Code executes until `return result;`.
4. Result value returned, Stack Frame popped off CPU stack, restoring caller execution state.

```
Recursive Function Call Stack Traversal:
[ factorial(3) ] ---> Pushes Stack Frame (3 * factorial(2))
    [ factorial(2) ] ---> Pushes Stack Frame (2 * factorial(1))
        [ factorial(1) ] ---> Base Case Reached! Returns 1
    [ factorial(2) ] <--- Pops Stack Frame (2 * 1 = 2)
[ factorial(3) ] <--- Pops Stack Frame (3 * 2 = 6) ---> Final Return 6
```"""

    m6_syntax = """// Function prototype
int multiply(int x, int y);

// Function definition
int multiply(int x, int y) {
    return x * y;
}

// Recursive function definition
int factorial(int n) {
    if (n <= 1) return 1; // Base case
    return n * factorial(n - 1); // Recursive step
}"""

    m6_ex_sim = """#include <stdio.h>

int square(int num) {
    return num * num;
}

int main(void) {
    int res = square(6);
    printf("Square of 6 = %d\\n", res);
    return 0;
}"""

    m6_out_sim = """Square of 6 = 36"""

    m6_lbl_sim = """- `int square(int num)`: Function accepting integer `num` returning integer.
- `return num * num;`: Computes product and returns integer value to caller frame in main.
- `int res = square(6);`: Receives return value 36 and assigns to `res`."""

    m6_ex_real = """#include <stdio.h>

int fibonacci(int n) {
    if (n == 0) return 0; // Base case 1
    if (n == 1) return 1; // Base case 2
    return fibonacci(n - 1) + fibonacci(n - 2); // Recursive call
}

int main(void) {
    int term = 7;
    printf("Fibonacci Term %d = %d\\n", term, fibonacci(term));
    return 0;
}"""

    m6_out_real = """Fibonacci Term 7 = 13"""

    m6_exp_real = """Calculates Nth Fibonacci term using dual recursive calls and base case stopping conditions."""

    m6_mistakes = """1. Omitting base case in recursive functions, causing infinite self-calls and Stack Overflow crashes.
2. Expecting changes made to pass-by-value parameters inside a function to alter caller variables in main.
3. Defining functions below `main()` without placing function prototypes above `main()`."""

    m6_best = """1. Keep functions short, focused on performing one single task well.
2. Always declare prototypes at top of source files or header files.
3. Prefer iterative loop implementations over recursion if recursion depth risks overflowing stack memory."""

    m6_exs = [
        {
            "title": "Max Finder Function",
            "description": "Write function `int max(int a, int b)`. Call in main with inputs '14 27' and print 'Max = 27'.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\n// Write max function\n\nint main(void) {\n    int x, y;\n    if (scanf(\"%d %d\", &x, &y) == 2) {\n        // Print max\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 1,
            "test_cases": [{"input_data": "14 27\n", "expected_output": "Max = 27\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Even Checker Function",
            "description": "Write `int is_even(int n)`. Print '1' if even else '0' for input '42'.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\n// Write is_even function\n\nint main(void) {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        // Print result\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 2,
            "test_cases": [{"input_data": "42\n", "expected_output": "1\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Power Calculation Function",
            "description": "Write `long power(int base, int exp)`. For inputs '2 8', print '2^8 = 256'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\n// Write power function\n\nint main(void) {\n    int b, e;\n    if (scanf(\"%d %d\", &b, &e) == 2) {\n        // Compute and print\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 3,
            "test_cases": [{"input_data": "2 8\n", "expected_output": "2^8 = 256\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Recursive Sum 1 to N",
            "description": "Write recursive function `int rec_sum(int n)`. For N='5', print 'Recursive Sum = 15'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\n// Write rec_sum function\n\nint main(void) {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        // Call recursive sum\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 4,
            "test_cases": [{"input_data": "5\n", "expected_output": "Recursive Sum = 15\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Static Counter Function",
            "description": "Write function `void count_calls(void)` containing `static int c = 0;`. Call 3 times and print 'Call 1', 'Call 2', 'Call 3'.",
            "difficulty": "Hard",
            "starter_code": "#include <stdio.h>\n\n// Function with static variable\n\nint main(void) {\n    // Call 3 times\n    return 0;\n}\n",
            "language": "c",
            "order_index": 5,
            "test_cases": [{"input_data": "", "expected_output": "Call 1\nCall 2\nCall 3\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Recursive Tower of Hanoi Step Counter",
            "description": "Write recursive function `int hanoi(int n)` returning minimum moves `2^n - 1`. For n=3 print 'Moves = 7'.",
            "difficulty": "Challenge",
            "starter_code": "#include <stdio.h>\n\n// Write hanoi step counter\n\nint main(void) {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        // Print moves\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 6,
            "test_cases": [{"input_data": "3\n", "expected_output": "Moves = 7\n", "is_hidden": False, "order_index": 1}]
        }
    ]

    m6_quizzes = [
        {
            "question_text": "What happens to C local function variables when a function returns?",
            "options": ["Saved in heap memory", "Stack frame is popped off CPU stack and local variable memory is deallocated", "Converted to globals", "Persisted to disk"],
            "correct_answer": "Stack frame is popped off CPU stack and local variable memory is deallocated",
            "explanation": "Local variables exist only within their function call stack frame; when returning, the stack frame is popped off and freed.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What is essential in every recursive function to prevent Stack Overflow?",
            "options": ["A loop statement", "A base case condition returning without making further recursive calls", "A global pointer", "A double return type"],
            "correct_answer": "A base case condition returning without making further recursive calls",
            "explanation": "Base cases stop recursive depth, preventing infinite function invocations from overflowing CPU stack memory.",
            "difficulty": "Beginner"
        }
    ,
        {
            "question_text": "What is a function prototype?",
            "options": ["The actual code block of the function", "A declaration that tells the compiler the function's name, return type, and parameters before its full definition", "A macro defined by the preprocessor", "A function that returns no value"],
            "correct_answer": "A declaration that tells the compiler the function's name, return type, and parameters before its full definition",
            "explanation": "A prototype (e.g., `int add(int a, int b);`) allows the compiler to verify calls to the function before encountering its actual body.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What does a 'void' return type mean?",
            "options": ["The function returns an integer 0", "The function returns a null pointer", "The function does not return any value to the caller", "The function takes no arguments"],
            "correct_answer": "The function does not return any value to the caller",
            "explanation": "Using void as the return type specifies that the function performs an action but yields no data back.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What is the CPU call stack?",
            "options": ["A data structure that tracks memory allocations on the heap", "A memory region that manages active function calls, pushing a stack frame for each call and popping it upon return", "A global variable storage area", "A queue used for thread synchronization"],
            "correct_answer": "A memory region that manages active function calls, pushing a stack frame for each call and popping it upon return",
            "explanation": "The call stack tracks execution flow. When a function is called, its local variables and return address are pushed onto the stack.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What is recursion?",
            "options": ["A loop that never ends", "A function that calls itself to solve smaller instances of the same problem", "A function that takes another function as an argument", "A process that frees dynamic memory"],
            "correct_answer": "A function that calls itself to solve smaller instances of the same problem",
            "explanation": "Recursion involves a function repeatedly calling itself until it reaches a defined base case.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What happens if a recursive function lacks a valid base case?",
            "options": ["The compiler automatically adds one", "It runs identically to a while loop", "It creates infinite recursive calls, eventually causing a Stack Overflow crash", "It returns 0 by default"],
            "correct_answer": "It creates infinite recursive calls, eventually causing a Stack Overflow crash",
            "explanation": "Without a base case, the stack continues to grow with new function frames until memory is exhausted.",
            "difficulty": "Medium"
        },
        {
            "question_text": "In C, parameters are passed to functions by:",
            "options": ["Value, meaning copies of the variables are sent", "Reference, meaning original variables are always modified", "Global scope projection", "Pointer delegation only"],
            "correct_answer": "Value, meaning copies of the variables are sent",
            "explanation": "C natively passes arguments by value. To modify original variables, developers must explicitly pass pointers (simulate pass-by-reference).",
            "difficulty": "Hard"
        },
        {
            "question_text": "What is a local variable?",
            "options": ["A variable accessible from any file in the project", "A variable accessible anywhere within the same C file", "A variable declared inside a function or block, accessible only within that block", "A variable stored in the heap"],
            "correct_answer": "A variable declared inside a function or block, accessible only within that block",
            "explanation": "Local variables exist only within their declaring block and are destroyed when the block (e.g., function) exits.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What is the purpose of the 'return' statement?",
            "options": ["To print output to the console", "To allocate memory", "To exit the function immediately and optionally send a value back to the caller", "To restart the function"],
            "correct_answer": "To exit the function immediately and optionally send a value back to the caller",
            "explanation": "Return passes execution control (and a calculated value) back to the calling function, terminating the current function.",
            "difficulty": "Beginner"
        }
    ]

    # Stage 2 Project definition for Module 6
    m6_project = {
        "title": "Student Gradebook & Statistical Analysis Engine",
        "scenario": "You are developing a modular grading system for a university course that analyzes student numerical scores.",
        "objective": "Build a modular C application using helper functions to compute average, maximum, minimum, and pass count statistics.",
        "requirements": ["Function for calculating average score", "Functions for finding max and min values", "Function for counting passing scores (>= 60)"],
        "features": ["Statistical Calculator", "Grade Analyzer"],
        "required_concepts": ["Functions", "Arrays", "Loops", "Conditions"],
        "architecture": "Modular C application passing array pointers and size parameters to statistical analyzer functions.",
        "guidance": ["Pass array and size count into helper functions", "Use double for average score calculations"],
        "hints": ["Sum scores in a loop and divide by total count"],
        "workflow": "Read student scores array -> Call analyzer functions -> Format output report",
        "expected_behavior": "Input: '5 \\n 70 85 90 55 60' -> Outputs 'Avg: 72.00, Max: 90, Min: 55, Passed: 4'",
        "evaluation_criteria": "Functions accurately compute statistical metrics over input score datasets.",
        "starter_code": "#include <stdio.h>\n\n// Write statistical helper functions\n\nint main(void) {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        int scores[100];\n        for(int i=0; i<n; i++) scanf(\"%d\", &scores[i]);\n        // Call functions and format output\n    }\n    return 0;\n}\n",
        "language": "c",
        "test_cases": [
            {"input_data": "5\n 70 85 90 55 60\n", "expected_output": "Avg: 72.00, Max: 90, Min: 55, Passed: 4\n", "is_hidden": False, "order_index": 1}
        ]
    }

    modules.append(build_lesson(
        "Functions & Recursion", "c-functions-recursion",
        m6_what, m6_why, m6_how, m6_syntax, m6_ex_sim, m6_ex_real, m6_out_sim, m6_lbl_sim, m6_out_real, m6_exp_real, m6_mistakes, m6_best, m6_exs, m6_quizzes, m6_project
    ))

    # =========================================================================
    # MODULE 7: Arrays & Multidimensional Arrays
    # =========================================================================
    m7_what = """An array is a contiguous sequence of elements of the exact same data type stored sequentially in RAM memory addresses. Array elements are accessed using 0-based index brackets (`arr[0]` accesses first element).

Multidimensional arrays (such as 2D matrices `int matrix[rows][cols]`) extend this concept, organizing elements in row-major order contiguous memory blocks."""

    m7_why = """Managing 100 related values using individual variables (`val1, val2, ... val100`) is impossible to maintain. Arrays allow storing thousands of values under a single variable identifier, traversed efficiently using loops.

Because array memory elements are contiguous in physical RAM, CPU hardware caches pre-fetch array data into L1/L2 caches, providing maximum execution performance.

Multidimensional arrays are mandatory for graphics image buffers, game boards, scientific data grids, and linear algebra matrices."""

    m7_how = """Declaring `int arr[5];` allocates `5 * sizeof(int)` (20 bytes) of contiguous RAM memory.

```
Contiguous 1D Array RAM Layout:
Index:         [0]        [1]        [2]        [3]        [4]
RAM Address: 0x1000     0x1004     0x1008     0x100C     0x1010
Value:        [ 10 ]     [ 20 ]     [ 30 ]     [ 40 ]     [ 50 ]
```

In a 2D array `grid[2][3]`, elements are stored in row-major order: Row 0 elements followed immediately by Row 1 elements in contiguous memory: `Offset = (row * cols + col) * sizeof(type)`."""

    m7_syntax = """int numbers[5] = {10, 20, 30, 40, 50};
int val = numbers[2]; // Accesses 30

int matrix[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};
int elem = matrix[1][2]; // Accesses 6"""

    m7_ex_sim = """#include <stdio.h>

int main(void) {
    int arr[4] = {5, 10, 15, 20};
    int sum = 0;
    for (int i = 0; i < 4; i++) {
        sum += arr[i];
    }
    printf("Array Sum = %d\\n", sum);
    return 0;
}"""

    m7_out_sim = """Array Sum = 50"""

    m7_lbl_sim = """- `int arr[4] = {5, 10, 15, 20};`: Reserves 16 bytes of contiguous RAM initialized with 4 integers.
- `arr[i]`: Accesses array element at 0-based offset i."""

    m7_ex_real = """#include <stdio.h>

int main(void) {
    int grid[2][2] = {{1, 2}, {3, 4}};
    printf("2D Grid Matrix:\\n");
    for (int r = 0; r < 2; r++) {
        for (int c = 0; c < 2; c++) {
            printf("%d ", grid[r][c]);
        }
        printf("\\n");
    }
    return 0;
}"""

    m7_out_real = """2D Grid Matrix:
1 2 
3 4"""

    m7_exp_real = """Prints a 2x2 mathematical matrix grid by traversing row and column indices using nested loops."""

    m7_mistakes = """1. Accessing elements out of array bounds (`arr[5]` on a 5-element array indexed 0..4), causing buffer overflow memory corruption.
2. Attempting array copy via direct assignment `arr1 = arr2;` (illegal in C).
3. Leaving array size uninitialized during declaration."""

    m7_best = """1. Always pass array size parameters explicitly alongside array parameters in functions.
2. Define array capacity bounds using `#define MAX_SIZE 100`.
3. Initialize arrays using `{0}` to clear contents to zero."""

    m7_exs = [
        {
            "title": "Array Element Searcher",
            "description": "Read 5 array ints '10 20 30 40 50' and target '30'. Print 'Found at index 2'.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int arr[5];\n    // Read array and search target\n    return 0;\n}\n",
            "language": "c",
            "order_index": 1,
            "test_cases": [{"input_data": "10 20 30 40 50\n 30\n", "expected_output": "Found at index 2\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "In-Place Array Reverser",
            "description": "Read 4 ints '1 2 3 4'. Reverse array in-place and print space-separated: '4 3 2 1 '.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int arr[4];\n    // Reverse array\n    return 0;\n}\n",
            "language": "c",
            "order_index": 2,
            "test_cases": [{"input_data": "1 2 3 4\n", "expected_output": "4 3 2 1 \n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "2D Matrix Row Sum Calculator",
            "description": "Read 2x2 matrix values '1 2 3 4'. Print row sums: 'Row 0 = 3', 'Row 1 = 7'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int m[2][2];\n    // Matrix row sum\n    return 0;\n}\n",
            "language": "c",
            "order_index": 3,
            "test_cases": [{"input_data": "1 2 3 4\n", "expected_output": "Row 0 = 3\nRow 1 = 7\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Array Second Max Finder",
            "description": "Read 5 ints '12 45 7 89 34'. Find second largest element: 'Second Max = 45'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int arr[5];\n    // Second max algorithm\n    return 0;\n}\n",
            "language": "c",
            "order_index": 4,
            "test_cases": [{"input_data": "12 45 7 89 34\n", "expected_output": "Second Max = 45\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Matrix Transpose Generator",
            "description": "Read 2x3 matrix inputs. Output transposed 3x2 matrix elements row by row.",
            "difficulty": "Hard",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int mat[2][3], trans[3][2];\n    // Matrix transpose\n    return 0;\n}\n",
            "language": "c",
            "order_index": 5,
            "test_cases": [{"input_data": "1 2 3\n4 5 6\n", "expected_output": "1 4 \n2 5 \n3 6 \n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "2D Matrix Multiplication Engine",
            "description": "Read two 2x2 matrices A and B. Compute product matrix C = A x B and print row results.",
            "difficulty": "Challenge",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int A[2][2], B[2][2], C[2][2];\n    // Matrix multiplication\n    return 0;\n}\n",
            "language": "c",
            "order_index": 6,
            "test_cases": [{"input_data": "1 2 3 4\n 5 6 7 8\n", "expected_output": "19 22 \n43 50 \n", "is_hidden": False, "order_index": 1}]
        }
    ]

    m7_quizzes = [
        {
            "question_text": "What is the memory indexing rule for accessing array elements in C?",
            "options": ["1-based indexing", "0-based indexing (first element at index 0)", "Random offset indexing", "Hardware address indexing"],
            "correct_answer": "0-based indexing (first element at index 0)",
            "explanation": "C array indexing is 0-based, representing element offset count from the array starting memory address.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "How are 2D array elements organized in physical RAM memory in C?",
            "options": ["Column-major order", "Row-major order (rows stored sequentially in memory)", "Fragmented heap blocks", "Linked node list"],
            "correct_answer": "Row-major order (rows stored sequentially in memory)",
            "explanation": "C stores multidimensional arrays in row-major order: all elements of row 0 are followed immediately by row 1 in contiguous RAM memory.",
            "difficulty": "Beginner"
        }
    ,
        {
            "question_text": "How are array elements indexed in C?",
            "options": ["Starting from 1", "Starting from 0", "Starting from -1", "Using alphabetical characters"],
            "correct_answer": "Starting from 0",
            "explanation": "C uses zero-based indexing, meaning the first element is at index 0, representing a zero offset from the array's memory address.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "How is a 2D array arranged in physical RAM?",
            "options": ["Column-major order", "Fragmented across the heap", "Row-major order (all elements of row 0 are contiguous, followed immediately by row 1)", "As an array of pointers"],
            "correct_answer": "Row-major order (all elements of row 0 are contiguous, followed immediately by row 1)",
            "explanation": "C flattens multidimensional arrays into a single contiguous block of memory row by row.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What happens if you access an array out of bounds (e.g., arr[10] on a 5-element array)?",
            "options": ["The compiler blocks compilation", "The program gracefully returns 0", "Undefined behavior, potentially corrupting adjacent memory or causing a segmentation fault", "The array automatically expands"],
            "correct_answer": "Undefined behavior, potentially corrupting adjacent memory or causing a segmentation fault",
            "explanation": "C does not perform bounds checking. Accessing out of bounds reads/writes raw memory belonging to other variables or secure areas.",
            "difficulty": "Hard"
        },
        {
            "question_text": "If you initialize an array partially: `int arr[5] = {1, 2};`, what happens to the remaining elements?",
            "options": ["They contain random garbage values", "They are automatically initialized to 0", "It causes a compilation error", "They are initialized to NULL"],
            "correct_answer": "They are automatically initialized to 0",
            "explanation": "If an array is partially initialized at declaration, the C standard guarantees the remaining elements are set to zero.",
            "difficulty": "Medium"
        },
        {
            "question_text": "Can you assign one array to another directly using the assignment operator (arr1 = arr2)?",
            "options": ["Yes, it performs a deep copy", "Yes, it performs a shallow copy", "No, array names are constant pointers and cannot be reassigned; you must copy element-by-element or use memcpy", "No, arrays can only be passed to functions"],
            "correct_answer": "No, array names are constant pointers and cannot be reassigned; you must copy element-by-element or use memcpy",
            "explanation": "C does not support direct array assignment. You must manually copy the bytes or iterate over the elements.",
            "difficulty": "Hard"
        },
        {
            "question_text": "How do you calculate the total byte size of an array in memory?",
            "options": ["sizeof(arr)", "length(arr)", "count(arr)", "arr.size()"],
            "correct_answer": "sizeof(arr)",
            "explanation": "The sizeof operator returns the total number of bytes allocated for the array in the current scope.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "How do you determine the number of elements in an array?",
            "options": ["sizeof(arr)", "sizeof(arr) / sizeof(arr[0])", "length(arr)", "size(arr)"],
            "correct_answer": "sizeof(arr) / sizeof(arr[0])",
            "explanation": "Dividing the total array byte size by the byte size of a single element yields the element count.",
            "difficulty": "Medium"
        },
        {
            "question_text": "When an array is passed to a function, what is actually passed?",
            "options": ["A full copy of the array data", "A pointer to the first element of the array", "The size of the array", "A reference object"],
            "correct_answer": "A pointer to the first element of the array",
            "explanation": "Arrays decay into pointers when passed to functions, meaning the function receives the memory address, not a copy of the data.",
            "difficulty": "Hard"
        }
    ]

    modules.append(build_lesson(
        "Arrays & Multidimensional Arrays", "c-arrays-multidimensional",
        m7_what, m7_why, m7_how, m7_syntax, m7_ex_sim, m7_ex_real, m7_out_sim, m7_lbl_sim, m7_out_real, m7_exp_real, m7_mistakes, m7_best, m7_exs, m7_quizzes
    ))

    # =========================================================================
    # MODULE 8: Strings & Character Processing
    # =========================================================================
    m8_what = """In C, a string is not a primitive object type—it is a 1D array of `char` elements terminated by a null character `\0` (ASCII numeric code 0).

The null terminator `\0` signals to string functions where character data stops in RAM memory.

Standard library header `<string.h>` provides essential string processing functions: `strlen` (length), `strcpy` (copy), `strcat` (concatenate), `strcmp` (compare), and `strstr` (substring search)."""

    m8_why = """Text processing is universal across software development: parsing JSON payloads, processing user commands, reading config files, and formatting system logs.

Understanding C strings and `\0` reveals how memory buffer overflows occur when string buffers are inadequately allocated.

Mastering string functions prevents severe security vulnerabilities like buffer overflow stack smashing attacks."""

    m8_how = """Declaring `char name[6] = "Hello";` reserves 6 bytes in RAM memory: `'H'`, `'e'`, `'l'`, `'l'`, `'o'`, `'\0'`.

`strlen(name)` counts character array elements until encountering `\0`, returning `5`.

`strcmp("apple", "banana")` compares ASCII character codes character by character, returning a negative integer if first string is alphabetically smaller, 0 if equal, or positive integer if larger."""

    m8_syntax = """#include <string.h>

char str1[20] = "Hello";
char str2[] = "World";

strcat(str1, " ");
strcat(str1, str2); // str1 is now "Hello World"

int len = strlen(str1); // 11
int cmp = strcmp("abc", "abc"); // 0"""

    m8_ex_sim = """#include <stdio.h>
#include <string.h>

int main(void) {
    char msg[30] = "LearnX";
    strcat(msg, " C Engine");
    printf("Message: %s\\n", msg);
    printf("Length: %zu\\n", strlen(msg));
    return 0;
}"""

    m8_out_sim = """Message: LearnX C Engine
Length: 15"""

    m8_lbl_sim = """- `char msg[30] = "LearnX";`: Allocates 30-byte char buffer initialized with text and null terminator.
- `strcat(msg, " C Engine");`: Appends target text onto destination string buffer.
- `strlen(msg)`: Counts characters up to null terminator `\0` (15)."""

    m8_ex_real = """#include <stdio.h>
#include <string.h>

int main(void) {
    char role[20] = "admin";
    if (strcmp(role, "admin") == 0) {
        printf("Authentication Granted: Full System Access\\n");
    } else {
        printf("Authentication Denied: Guest Access\\n");
    }
    return 0;
}"""

    m8_out_real = """Authentication Granted: Full System Access"""

    m8_exp_real = """Compares user role string credentials against "admin" using `strcmp` to grant system access privileges."""

    m8_mistakes = """1. Using unsafe `gets()` instead of secure `fgets(buffer, size, stdin)`.
2. Forgetting to allocate 1 extra byte for `\0` (`char str[5] = "Hello";` causes buffer overflow!).
3. Comparing string contents with `str1 == str2` (this compares pointer memory addresses, NOT character contents!)."""

    m8_best = """1. Always use bounded string functions (`strncpy`, `strncat`) to prevent buffer overflow vulnerabilities.
2. Ensure destination char buffers have enough room for text plus `\0`.
3. Use `fgets()` to safely read multi-word string inputs from standard input."""

    m8_exs = [
        {
            "title": "String Length Calculator",
            "description": "Read string 'OpenAI' and print 'Length = 6' using `strlen`.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n#include <string.h>\n\nint main(void) {\n    char str[50];\n    if (scanf(\"%49s\", str) == 1) {\n        // Print length\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 1,
            "test_cases": [{"input_data": "OpenAI\n", "expected_output": "Length = 6\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Vowel Counter in String",
            "description": "Read string 'computer'. Count vowels (a,e,i,o,u) and print 'Vowels = 3'.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n#include <string.h>\n\nint main(void) {\n    char str[50];\n    if (scanf(\"%49s\", str) == 1) {\n        // Count vowels\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 2,
            "test_cases": [{"input_data": "computer\n", "expected_output": "Vowels = 3\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Palindrome Word Evaluator",
            "description": "Read word 'radar'. Check if palindrome and print 'Palindrome', else 'Not Palindrome'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n#include <string.h>\n\nint main(void) {\n    char str[50];\n    if (scanf(\"%49s\", str) == 1) {\n        // Palindrome check\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 3,
            "test_cases": [{"input_data": "radar\n", "expected_output": "Palindrome\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Uppercase String Converter",
            "description": "Read string 'hello'. Convert to uppercase in-place and print 'HELLO'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n#include <ctype.h>\n#include <string.h>\n\nint main(void) {\n    char str[50];\n    if (scanf(\"%49s\", str) == 1) {\n        // Convert to uppercase\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 4,
            "test_cases": [{"input_data": "hello\n", "expected_output": "HELLO\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Character Frequency Counter",
            "description": "Read main string and target char 'banana a'. Count target occurrences and print 'Count = 3'.",
            "difficulty": "Hard",
            "starter_code": "#include <stdio.h>\n#include <string.h>\n\nint main(void) {\n    char str[50], ch;\n    if (scanf(\"%49s %c\", str, &ch) == 2) {\n        // Count occurrences\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 5,
            "test_cases": [{"input_data": "banana a\n", "expected_output": "Count = 3\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "CSV Comma String Tokenizer",
            "description": "Read comma-separated string 'apple,banana,cherry'. Replace commas with newlines and print.",
            "difficulty": "Challenge",
            "starter_code": "#include <stdio.h>\n#include <string.h>\n\nint main(void) {\n    char str[100];\n    if (scanf(\"%99s\", str) == 1) {\n        // Tokenize by comma\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 6,
            "test_cases": [{"input_data": "apple,banana,cherry\n", "expected_output": "apple\nbanana\ncherry\n", "is_hidden": False, "order_index": 1}]
        }
    ]

    m8_quizzes = [
        {
            "question_text": "What character marks the mandatory termination of valid string arrays in C RAM memory?",
            "options": ["'\\n' (newline)", "'\\0' (null character)", "' ' (space)", "';' (semicolon)"],
            "correct_answer": "'\\0' (null character)",
            "explanation": "C strings depend on the null terminator '\\0' (ASCII 0) to signal where character data terminates in RAM memory.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "Why is testing string equality with str1 == str2 invalid in C?",
            "options": ["Causes compilation syntax error", "Compares pointer memory RAM addresses rather than character text contents", "Only compares first letter", "Modifies string data"],
            "correct_answer": "Compares pointer memory RAM addresses rather than character text contents",
            "explanation": "str1 == str2 evaluates if both array pointers hold identical RAM addresses; strcmp() must be used to compare text strings.",
            "difficulty": "Beginner"
        }
    ,
        {
            "question_text": "In C, how is a string represented in memory?",
            "options": ["As a dedicated String primitive type", "As a linked list of characters", "As a contiguous array of characters terminated by a null character ('\0')", "As a struct containing a char array and a length integer"],
            "correct_answer": "As a contiguous array of characters terminated by a null character ('\0')",
            "explanation": "C strings are simply character arrays. The null terminator '\0' is critical for string functions to know where the text ends.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What is the ASCII value of the null terminator '\0'?",
            "options": ["32 (space)", "48 (zero)", "0", "255"],
            "correct_answer": "0",
            "explanation": "The null terminator is the ASCII character with a numeric value of exactly 0.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "Which standard library function calculates the length of a string?",
            "options": ["strsize()", "length()", "strlen()", "strcnt()"],
            "correct_answer": "strlen()",
            "explanation": "strlen() counts characters in a string up to, but not including, the null terminator.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "Does strlen() include the null terminator in its count?",
            "options": ["Yes", "No", "Only for dynamic strings", "Depends on the compiler"],
            "correct_answer": "No",
            "explanation": "strlen() returns the number of visible characters. The null terminator is strictly a boundary marker.",
            "difficulty": "Medium"
        },
        {
            "question_text": "Which function safely concatenates two strings, preventing buffer overflows?",
            "options": ["strcat()", "strncat()", "append()", "concat()"],
            "correct_answer": "strncat()",
            "explanation": "strncat() accepts a length limit parameter, ensuring it won't write beyond the destination buffer's capacity.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What does strcmp('apple', 'banana') return?",
            "options": ["0", "A positive integer", "A negative integer", "True"],
            "correct_answer": "A negative integer",
            "explanation": "strcmp returns a negative value because 'a' has a lower ASCII value than 'b', meaning 'apple' comes first alphabetically.",
            "difficulty": "Hard"
        },
        {
            "question_text": "What happens if a string lacks a null terminator and you call printf('%s') on it?",
            "options": ["printf automatically stops after 10 characters", "printf throws a compile error", "printf continues reading memory past the array bounds until it randomly hits a zero byte, causing garbage output or a crash", "printf prints nothing"],
            "correct_answer": "printf continues reading memory past the array bounds until it randomly hits a zero byte, causing garbage output or a crash",
            "explanation": "Functions relying on %s trust the null terminator to stop reading memory. Without it, they read blindly out of bounds.",
            "difficulty": "Hard"
        },
        {
            "question_text": "If char name[5] = 'Hello'; what is the vulnerability here?",
            "options": ["None, it is perfectly valid", "The array is too small to hold the null terminator, causing a buffer overflow", "The string is not capitalized", "name is a reserved keyword"],
            "correct_answer": "The array is too small to hold the null terminator, causing a buffer overflow",
            "explanation": "\"Hello\" requires 6 bytes (5 for letters + 1 for '\\0'). Providing only 5 bytes means no terminator is stored.",
            "difficulty": "Hard"
        }
    ]

    modules.append(build_lesson(
        "Strings & Character Processing", "c-strings-character-processing",
        m8_what, m8_why, m8_how, m8_syntax, m8_ex_sim, m8_ex_real, m8_out_sim, m8_lbl_sim, m8_out_real, m8_exp_real, m8_mistakes, m8_best, m8_exs, m8_quizzes
    ))

    # =========================================================================
    # MODULE 9: Pointers Fundamentals
    # =========================================================================
    m9_what = """A pointer is a specialized variable whose value is the exact physical RAM memory address of another variable. Every variable in C lives at a numeric RAM address.

The address-of operator `&` extracts a variable's physical RAM memory address.

The dereference operator `*` (when placed before a pointer variable) accesses or modifies the value stored inside the memory address held by the pointer."""

    m9_why = """Pointers are C's defining power feature. Without pointers, C could not perform dynamic heap memory allocation (`malloc`), pass variables by reference to functions, build linked data structures (trees, graphs), or write operating system device drivers.

Understanding pointers transforms a developer from treating variables as abstract names to understanding how hardware RAM cells store data.

Vague statements like 'pointers store addresses' are insufficient. You must understand address extraction with `&`, pointer variable storage, and value retrieval via `*` dereferencing."""

    m9_how = """Visualizing Pointer Memory Architecture:

```
Variable Allocation:
age = 20

RAM Memory Mapping:
Address 0x1000 -> Stored Value: 20

Pointer Declaration & Assignment:
int *p = &age;

Pointer Memory Mapping:
Pointer Variable p (at Address 0x2000) -> Stored Value: 0x1000

Dereferencing (*p):
*p reads Value stored at Address 0x1000 -> Returns 20
*p = 25 writes Value 25 into Address 0x1000 -> Updates age to 25!
```

Given `int age = 20; int *p = &age;`:
1. `age` reserves 4 bytes in RAM at address `0x1000` containing integer `20`.
2. `&age` evaluates to address `0x1000`.
3. Pointer `p` stores address value `0x1000`.
4. Executing `*p = 25;` goes to address `0x1000` and overwrites value to `25`, updating `age` directly!"""

    m9_syntax = """int count = 50;
int *ptr = &count; // ptr holds address of count

printf("Value of count: %d\\n", count);
printf("Pointer ptr holds address: %p\\n", (void*)ptr);
printf("Dereferenced *ptr: %d\\n", *ptr);

*ptr = 100; // Modifies count to 100 directly!"""

    m9_ex_sim = """#include <stdio.h>

int main(void) {
    int val = 42;
    int *p = &val;

    printf("val = %d\\n", val);
    printf("*p = %d\\n", *p);

    *p = 99; // Dereference modification
    printf("Updated val = %d\\n", val);
    return 0;
}"""

    m9_out_sim = """val = 42
*p = 42
Updated val = 99"""

    m9_lbl_sim = """- `int *p = &val;`: Declares integer pointer `p` initialized with RAM address of `val`.
- `*p`: Dereferences pointer `p` to read integer value stored at target address.
- `*p = 99;`: Writes integer 99 into RAM location pointed to by `p`, modifying `val` directly."""

    m9_ex_real = """#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(void) {
    int x = 10, y = 20;
    printf("Before swap: x=%d, y=%d\\n", x, y);
    swap(&x, &y);
    printf("After swap:  x=%d, y=%d\\n", x, y);
    return 0;
}"""

    m9_out_real = """Before swap: x=10, y=20
After swap:  x=20, y=10"""

    m9_exp_real = """Uses pointers to swap two integer variables in caller's stack frame via pass-by-reference."""

    m9_mistakes = """1. Dereferencing uninitialized or NULL pointers (`int *p; *p = 5;`), causing Segmentation Fault crashes.
2. Confusing address-of operator `&` with dereference operator `*`.
3. Forgetting to pass addresses with `&` when invoking functions expecting pointer parameters."""

    m9_best = """1. Always initialize pointers to `NULL` if target variable address is not immediately bound.
2. Check `if (ptr != NULL)` before dereferencing pointers.
3. Match pointer types strictly to target data types (`int *` for `int`, `double *` for `double`)."""

    m9_exs = [
        {
            "title": "Address and Pointer Printer",
            "description": "Declare `int num = 100`, pointer `p = &num`. Print '*p = 100'.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int num = 100;\n    // Print dereferenced value\n    return 0;\n}\n",
            "language": "c",
            "order_index": 1,
            "test_cases": [{"input_data": "", "expected_output": "*p = 100\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Pointer Dereference Value Modifier",
            "description": "Read integer (e.g. 50). Use pointer `*ptr` to double the value. Print 'Modified = 100'.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int val;\n    if (scanf(\"%d\", &val) == 1) {\n        // Double val using pointer dereference\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 2,
            "test_cases": [{"input_data": "50\n", "expected_output": "Modified = 100\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Pass-By-Reference Integer Swapper",
            "description": "Read '15 30'. Pass `&x, &y` to `swap(int *a, int *b)` function. Print 'x=30, y=15'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\nvoid swap(int *a, int *b) {\n    // Implement swap\n}\n\nint main(void) {\n    int x, y;\n    if (scanf(\"%d %d\", &x, &y) == 2) {\n        swap(&x, &y);\n        printf(\"x=%d, y=%d\\n\", x, y);\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 3,
            "test_cases": [{"input_data": "15 30\n", "expected_output": "x=30, y=15\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Pointer Null Check Guard",
            "description": "Declare `int *ptr = NULL`. Print 'Pointer is NULL', bind to `int x=5` and print '*ptr = 5'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    // NULL safety check\n    return 0;\n}\n",
            "language": "c",
            "order_index": 4,
            "test_cases": [{"input_data": "", "expected_output": "Pointer is NULL\n*ptr = 5\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Double Pointer Dereferencer",
            "description": "Declare `int val=7`, `int *p=&val`, `int **pp=&p`. Use `**pp` to modify `val` to 77. Print 'val = 77'.",
            "difficulty": "Hard",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    // Double pointer dereference\n    return 0;\n}\n",
            "language": "c",
            "order_index": 5,
            "test_cases": [{"input_data": "", "expected_output": "val = 77\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "MinMax Extractor Function via Pointers",
            "description": "Write `void get_min_max(int a, int b, int *min, int *max)`. For inputs '45 12', return min=12, max=45 via pointers.",
            "difficulty": "Challenge",
            "starter_code": "#include <stdio.h>\n\n// Write get_min_max function\n\nint main(void) {\n    int a, b, min, max;\n    if (scanf(\"%d %d\", &a, &b) == 2) {\n        // Call get_min_max\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 6,
            "test_cases": [{"input_data": "45 12\n", "expected_output": "Min = 12, Max = 45\n", "is_hidden": False, "order_index": 1}]
        }
    ]

    m9_quizzes = [
        {
            "question_text": "What does dereference operator * do when applied to pointer variable *p?",
            "options": ["Returns pointer's own address", "Accesses value stored inside RAM address location held by p", "Multiplies pointer address", "Frees memory"],
            "correct_answer": "Accesses value stored inside RAM address location held by p",
            "explanation": "Dereferencing *p fetches or overwrites data stored at the memory RAM address pointed to by pointer p.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "Why is passing pointers to functions (pass-by-reference) necessary in C?",
            "options": ["Speeds up compilation", "Allows functions to modify caller's original variables directly in caller frame", "Makes variables global", "Prevents function returns"],
            "correct_answer": "Allows functions to modify caller's original variables directly in caller frame",
            "explanation": "C uses pass-by-value by default; passing pointers provides memory addresses so functions can write directly into caller RAM variables.",
            "difficulty": "Beginner"
        }
    ,
        {
            "question_text": "What does a pointer variable store?",
            "options": ["An integer value", "A floating-point value", "The RAM memory address of another variable", "A string constant"],
            "correct_answer": "The RAM memory address of another variable",
            "explanation": "Pointers are specialized variables designed exclusively to hold physical or virtual memory addresses.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "Which operator is used to get the memory address of a variable?",
            "options": ["* (Dereference)", "& (Address-of)", "% (Modulo)", "-> (Arrow)"],
            "correct_answer": "& (Address-of)",
            "explanation": "The & operator retrieves the memory address of a variable, e.g., &val yields the address where val lives.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What does the dereference operator (*) do?",
            "options": ["Multiplies two pointers together", "Retrieves or modifies the value stored at the memory address the pointer holds", "Frees the memory", "Checks if a pointer is NULL"],
            "correct_answer": "Retrieves or modifies the value stored at the memory address the pointer holds",
            "explanation": "Dereferencing a pointer follows the address to access the actual data living at that location in RAM.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What is a NULL pointer?",
            "options": ["A pointer that points to address 0, explicitly indicating it points to nothing valid", "A pointer that points to a string of zeroes", "A pointer that has been freed", "A pointer that points to negative memory"],
            "correct_answer": "A pointer that points to address 0, explicitly indicating it points to nothing valid",
            "explanation": "Setting a pointer to NULL is a universally recognized way to flag that the pointer is uninitialized or empty.",
            "difficulty": "Medium"
        },
        {
            "question_text": "If `int x = 5; int *p = &x; *p = 10;`, what is the value of x?",
            "options": ["5", "10", "Undefined", "0"],
            "correct_answer": "10",
            "explanation": "Dereferencing p (*p = 10) directly reaches into x's memory address and overwrites its value with 10.",
            "difficulty": "Hard"
        },
        {
            "question_text": "What happens if you dereference an uninitialized pointer (e.g., int *p; *p = 5;)?",
            "options": ["The compiler automatically allocates memory", "The program safely ignores it", "The program writes to a random memory address, usually resulting in a Segmentation Fault (crash)", "The pointer automatically becomes NULL"],
            "correct_answer": "The program writes to a random memory address, usually resulting in a Segmentation Fault (crash)",
            "explanation": "An uninitialized pointer holds a garbage address. Dereferencing it attempts to corrupt unknown memory, causing a crash.",
            "difficulty": "Hard"
        },
        {
            "question_text": "Why must pointers be declared with a specific data type (e.g., int * instead of just pointer p)?",
            "options": ["To make the code look organized", "Because the compiler needs to know how many bytes to read/write when dereferencing the pointer", "Because pointers can only point to integers", "So the pointer itself takes up more memory"],
            "correct_answer": "Because the compiler needs to know how many bytes to read/write when dereferencing the pointer",
            "explanation": "An address is just a starting point. The type tells the compiler how many bytes to fetch (e.g., 4 bytes for int, 8 for double).",
            "difficulty": "Hard"
        },
        {
            "question_text": "What does a double pointer (e.g., int **) hold?",
            "options": ["A pointer to an 8-byte double", "Two memory addresses at once", "The memory address of another pointer variable", "A 2D array matrix"],
            "correct_answer": "The memory address of another pointer variable",
            "explanation": "A double pointer holds the address of a pointer. This allows functions to modify the address that the target pointer holds.",
            "difficulty": "Hard"
        }
    ]

    # Stage 3 Project definition for Module 9
    m9_project = {
        "title": "Employee Management & Payroll System",
        "scenario": "You are building an employee management and payroll processing system that modifies employee salary records directly in memory using pointer parameters.",
        "objective": "Build a C application utilizing structures and pointers to modify employee payroll records via pass-by-reference.",
        "requirements": ["Define Employee structure (id, salary)", "Function passing Employee struct pointers to apply salary raises", "Format output to 2 decimal places"],
        "features": ["Payroll Updater Engine", "Pass-by-Reference Record Modifier"],
        "required_concepts": ["Pointers", "Structures", "Functions", "Formatting"],
        "architecture": "Modular C application passing struct pointers to modifier functions.",
        "guidance": ["Use arrow operator ptr->salary to update salary", "Pass &emp address to modifier function"],
        "hints": ["Use ptr->salary += raise_amount"],
        "workflow": "Read employee ID and salary -> Pass struct address to raise function -> Output updated record",
        "expected_behavior": "Input: '101 50000.00 5000.00' -> Outputs 'Employee 101 New Salary: $55000.00'",
        "evaluation_criteria": "Program successfully modifies struct records in-place using pointer arrow operator.",
        "starter_code": "#include <stdio.h>\n\ntypedef struct {\n    int id;\n    double salary;\n} Employee;\n\nvoid apply_raise(Employee *e, double raise) {\n    // Implement raise\n}\n\nint main(void) {\n    Employee emp;\n    double raise;\n    if (scanf(\"%d %lf %lf\", &emp.id, &emp.salary, &raise) == 3) {\n        apply_raise(&emp, raise);\n        printf(\"Employee %d New Salary: $%.2f\\n\", emp.id, emp.salary);\n    }\n    return 0;\n}\n",
        "language": "c",
        "test_cases": [
            {"input_data": "101 50000.00 5000.00\n", "expected_output": "Employee 101 New Salary: $55000.00\n", "is_hidden": False, "order_index": 1}
        ]
    }

    modules.append(build_lesson(
        "Pointers Fundamentals", "c-pointers-fundamentals",
        m9_what, m9_why, m9_how, m9_syntax, m9_ex_sim, m9_ex_real, m9_out_sim, m9_lbl_sim, m9_out_real, m9_exp_real, m9_mistakes, m9_best, m9_exs, m9_quizzes, m9_project
    ))

    # =========================================================================
    # MODULE 10: Pointers, Arrays & Functions
    # =========================================================================
    m10_what = """In C, arrays and pointers are fundamentally connected. An array name evaluates to a pointer pointing to its first element (`arr == &arr[0]`).

Pointer arithmetic allows incrementing or decrementing pointers to step through contiguous RAM elements. Adding `1` to an `int *` pointer increments its memory address by `sizeof(int)` bytes (typically 4 bytes).

Expressions `arr[i]` and `*(arr + i)` are 100% syntactically equivalent in C."""

    m10_why = """Understanding array-pointer equivalence explains why passing arrays to functions does not copy entire array data onto the stack. Instead, only a pointer address is passed, making array parameter passing blazingly fast regardless of array size.

Pointer arithmetic is heavily used in memory buffer processing, string manipulation algorithms, custom allocators, and graphics pixel processing engines."""

    m10_how = """If pointer `p` holds RAM address `0x1000` pointing to an `int`:
Executing `p++` advances `p` to address `0x1004` (because `sizeof(int) == 4`).

When passing `int arr[]` to `void process(int *ptr, int size)`, `ptr` receives RAM Address `&arr[0]`. Accessing `ptr[i]` or `*(ptr + i)` accesses array memory directly in caller frame.

```
Pointer Arithmetic Memory Progression:
Pointer p -> 0x1000 (*p = arr[0])
(p + 1)   -> 0x1004 (*(p + 1) = arr[1])
(p + 2)   -> 0x1008 (*(p + 2) = arr[2])
```"""

    m10_syntax = """int arr[3] = {10, 20, 30};
int *p = arr; // p points to arr[0]

printf("First: %d\\n", *p);        // 10
printf("Second: %d\\n", *(p + 1)); // 20
printf("Third: %d\\n", *(p + 2));  // 30

void print_array(const int *data, int count) {
    for (int i = 0; i < count; i++) {
        printf("%d ", *(data + i));
    }
}"""

    m10_ex_sim = """#include <stdio.h>

int main(void) {
    int numbers[3] = {100, 200, 300};
    int *ptr = numbers;

    for (int i = 0; i < 3; i++) {
        printf("Element %d via pointer = %d\\n", i, *(ptr + i));
    }
    return 0;
}"""

    m10_out_sim = """Element 0 via pointer = 100
Element 1 via pointer = 200
Element 2 via pointer = 300"""

    m10_lbl_sim = """- `int *ptr = numbers;`: Binds pointer to start address of array `numbers`.
- `*(ptr + i)`: Uses pointer arithmetic offset to dereference array elements."""

    m10_ex_real = """#include <stdio.h>

int array_sum(const int *arr, int size) {
    int total = 0;
    for (int i = 0; i < size; i++) {
        total += *(arr + i);
    }
    return total;
}

int main(void) {
    int data[4] = {5, 15, 25, 35};
    int sum = array_sum(data, 4);
    printf("Total Sum = %d\\n", sum);
    return 0;
}"""

    m10_out_real = """Total Sum = 80"""

    m10_exp_real = """Passes array pointer to function to compute total element sum using pointer arithmetic offset dereferencing."""

    m10_mistakes = """1. Expecting `sizeof(arr)` inside a function to report total array byte size (it reports pointer size 4/8 bytes!).
2. Attempting pointer arithmetic on `void *` without casting to specific byte type (`char *`).
3. Incrementing an array name (`arr++` is illegal; array names are constant pointers)."""

    m10_best = """1. Always pass explicit array size parameters alongside array pointer arguments.
2. Mark read-only array parameters with `const int *arr` to prevent unintentional mutation.
3. Prefer array indexing `arr[i]` for visual clarity unless pointer arithmetic provides performance gains."""

    m10_exs = [
        {
            "title": "Pointer Arithmetic Array Traverser",
            "description": "Read 3 ints '5 10 15'. Print space-separated elements using `*(ptr + i)`.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int arr[3];\n    // Read array and print with pointer arithmetic\n    return 0;\n}\n",
            "language": "c",
            "order_index": 1,
            "test_cases": [{"input_data": "5 10 15\n", "expected_output": "5 10 15 \n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Array Sum Function via Pointers",
            "description": "Write `int sum_ptr(const int *p, int n)`. Read 4 ints '10 20 30 40' and print 'Sum = 100'.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\n// Write sum_ptr function\n\nint main(void) {\n    int arr[4];\n    // Call sum_ptr\n    return 0;\n}\n",
            "language": "c",
            "order_index": 2,
            "test_cases": [{"input_data": "10 20 30 40\n", "expected_output": "Sum = 100\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "In-Place Array Reverse with Two Pointers",
            "description": "Read 4 ints '1 2 3 4'. Use `start` and `end` pointers to reverse array in-place. Print '4 3 2 1 '.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int arr[4];\n    // Two pointer reverse\n    return 0;\n}\n",
            "language": "c",
            "order_index": 3,
            "test_cases": [{"input_data": "1 2 3 4\n", "expected_output": "4 3 2 1 \n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Pointer Distance Calculator",
            "description": "Point `p1` to `arr[0]` and `p2` to `arr[3]`. Print pointer distance `p2 - p1`: 'Distance = 3'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int arr[5] = {10, 20, 30, 40, 50};\n    // Compute pointer distance\n    return 0;\n}\n",
            "language": "c",
            "order_index": 4,
            "test_cases": [{"input_data": "", "expected_output": "Distance = 3\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "String Pointer Copy Function",
            "description": "Write custom `void my_strcpy(char *dest, const char *src)` using `*dest++ = *src++`. Copy 'Hello' and print.",
            "difficulty": "Hard",
            "starter_code": "#include <stdio.h>\n\n// Write my_strcpy\n\nint main(void) {\n    char src[20] = \"Hello\";\n    char dest[20];\n    // Call my_strcpy and print dest\n    return 0;\n}\n",
            "language": "c",
            "order_index": 5,
            "test_cases": [{"input_data": "", "expected_output": "dest = Hello\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Generic Memory Swap Function with void*",
            "description": "Write `void swap_generic(void *a, void *b, size_t size)`. Swap two doubles 3.14 and 6.28. Print swapped values.",
            "difficulty": "Challenge",
            "starter_code": "#include <stdio.h>\n#include <string.h>\n\n// Generic byte-wise swap function\n\nint main(void) {\n    double x = 3.14, y = 6.28;\n    // Swap doubles generically\n    return 0;\n}\n",
            "language": "c",
            "order_index": 6,
            "test_cases": [{"input_data": "", "expected_output": "x = 6.28, y = 3.14\n", "is_hidden": False, "order_index": 1}]
        }
    ]

    m10_quizzes = [
        {
            "question_text": "What does adding 1 to an int * pointer (p + 1) do in C?",
            "options": ["Increments memory address by 1 byte", "Increments memory address by sizeof(int) bytes (usually 4 bytes)", "Multiplies pointer address", "Syntax error"],
            "correct_answer": "Increments memory address by sizeof(int) bytes (usually 4 bytes)",
            "explanation": "Pointer arithmetic scales offsets by the byte size of the underlying data type.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "In C syntax, how are arr[i] and *(arr + i) related?",
            "options": ["arr[i] is faster", "They are 100% syntactically equivalent", "arr[i] works on heap, *(arr + i) works on stack", "*(arr + i) is illegal"],
            "correct_answer": "They are 100% syntactically equivalent",
            "explanation": "Subscript notation arr[i] is defined in C standard as identical to *(arr + i).",
            "difficulty": "Beginner"
        }
    ,
        {
            "question_text": "What does the expression `arr` evaluate to when passed to a function?",
            "options": ["The total size of the array", "A copy of all array elements", "A pointer to the first element (&arr[0])", "The value of the first element"],
            "correct_answer": "A pointer to the first element (&arr[0])",
            "explanation": "Array names decay into pointers to their 0th element, which is why passing arrays doesn't copy data.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "If `int *p` points to an integer array, what does `p + 1` do?",
            "options": ["Adds 1 to the integer value", "Increments the memory address by 1 byte", "Increments the memory address by sizeof(int) bytes", "Moves the pointer to the end of the array"],
            "correct_answer": "Increments the memory address by sizeof(int) bytes",
            "explanation": "Pointer arithmetic is scaled by the data type. Adding 1 to an int pointer skips forward exactly one int (usually 4 bytes).",
            "difficulty": "Medium"
        },
        {
            "question_text": "How is `arr[i]` interpreted by the C compiler?",
            "options": ["As a strict bounds-checked lookup", "As a function call", "Exactly as `*(arr + i)`", "As a macro expansion"],
            "correct_answer": "Exactly as `*(arr + i)`",
            "explanation": "The array indexing syntax is literally just syntactic sugar for pointer arithmetic and dereferencing.",
            "difficulty": "Medium"
        },
        {
            "question_text": "Can you increment an array name (e.g., `arr++`)?",
            "options": ["Yes, it moves to the next element", "No, array names act as constant pointers that cannot be reassigned", "Only if the array is dynamic", "Only inside a loop"],
            "correct_answer": "No, array names act as constant pointers that cannot be reassigned",
            "explanation": "While `arr` yields an address, it is not a modifiable variable holding an address; you cannot change where `arr` points.",
            "difficulty": "Hard"
        },
        {
            "question_text": "What is the difference between `char *str = 'Hello';` and `char arr[] = 'Hello';`?",
            "options": ["They are identical", "str points to read-only memory; arr is a modifiable copy on the stack", "str is a stack array; arr is read-only", "arr requires malloc"],
            "correct_answer": "str points to read-only memory; arr is a modifiable copy on the stack",
            "explanation": "String literals are stored in read-only memory. `char *str` points directly there. `char arr[]` copies the literal onto the modifiable stack.",
            "difficulty": "Hard"
        },
        {
            "question_text": "If `int arr[5];`, what does `sizeof(arr)` evaluate to?",
            "options": ["4 or 8 (size of a pointer)", "5", "5 * sizeof(int) (usually 20 bytes)", "0"],
            "correct_answer": "5 * sizeof(int) (usually 20 bytes)",
            "explanation": "Unlike pointer decay in function calls, calling sizeof directly on an array name in its declaring scope yields the total byte size of the array.",
            "difficulty": "Hard"
        },
        {
            "question_text": "When a function signature specifies `void process(int arr[])`, what is the actual type of `arr`?",
            "options": ["A full array structure", "A constant array", "A pointer `int *arr`", "A double pointer"],
            "correct_answer": "A pointer `int *arr`",
            "explanation": "In function parameters, array syntax `int arr[]` is secretly converted to pointer syntax `int *arr` by the compiler.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What happens if you subtract two pointers pointing to the same array?",
            "options": ["It causes a syntax error", "It yields the difference in raw bytes", "It yields the number of elements between them (pointer distance)", "It yields the sum of their values"],
            "correct_answer": "It yields the number of elements between them (pointer distance)",
            "explanation": "Pointer subtraction is automatically divided by the element size, giving the logical distance in elements.",
            "difficulty": "Hard"
        }
    ]

    modules.append(build_lesson(
        "Pointers, Arrays & Functions", "c-pointers-arrays-functions",
        m10_what, m10_why, m10_how, m10_syntax, m10_ex_sim, m10_ex_real, m10_out_sim, m10_lbl_sim, m10_out_real, m10_exp_real, m10_mistakes, m10_best, m10_exs, m10_quizzes
    ))

    # =========================================================================
    # MODULE 11: Structures, Unions, Enums & Typedef
    # =========================================================================
    m11_what = """Structures (`struct`) are user-defined composite data types that group related variables of different data types together under a single compound name.

Member fields are accessed using dot operator `.` for structure instances or arrow operator `->` for pointers to structures.

Unions (`union`) share a single memory region across all member fields. Enumerations (`enum`) define human-readable integer constants. `typedef` creates clean type aliases."""

    m11_why = """Real-world data is composite. For example, a Student record consists of string `name`, integer `id`, and float `gpa`. Managing these as individual variables is unmaintainable.

Structures group heterogeneous fields into a single logical record object.

Arrow operator `ptr->field` simplifies pointer-based structure manipulation indispensable for linked lists, database records, and system buffers."""

    m11_how = """Structure RAM Layout & Member Alignment:
`struct Student s1;` allocates memory for all declared fields sequentially in RAM, subject to CPU compiler byte alignment padding.

```
Struct RAM Memory Alignment Layout:
struct Student { int id; char grade; double gpa; };
Offset 0x00: [ id (4 Bytes) ]
Offset 0x04: [ grade (1 Byte) ] + [ Padding (3 Bytes) ]
Offset 0x08: [ gpa (8 Bytes) ]
Total Memory Size: 16 Bytes (aligned to 8-byte boundary)
```

For a pointer `struct Student *ptr = &s1;`:
`ptr->gpa = 3.9;` is shorthand equivalent for `(*ptr).gpa = 3.9;`."""

    m11_syntax = """typedef struct {
    int id;
    char name[30];
    float gpa;
} Student;

Student s1 = {101, "Alice", 3.85f};
Student *ptr = &s1;

printf("ID: %d, Name: %s, GPA: %.2f\\n", ptr->id, ptr->name, ptr->gpa);

enum Status { IDLE, RUNNING, COMPLETED };
enum Status state = RUNNING;"""

    m11_ex_sim = """#include <stdio.h>

struct Point {
    int x;
    int y;
};

int main(void) {
    struct Point p1 = {10, 20};
    struct Point *ptr = &p1;

    printf("Point X = %d, Y = %d\\n", ptr->x, ptr->y);
    return 0;
}"""

    m11_out_sim = """Point X = 10, Y = 20"""

    m11_lbl_sim = """- `struct Point p1 = {10, 20};`: Instantiates struct with fields x=10, y=20.
- `ptr->x`: Uses arrow operator to dereference struct pointer and read member x."""

    m11_ex_real = """#include <stdio.h>

typedef struct {
    int account_num;
    double balance;
} BankAccount;

void deposit(BankAccount *acc, double amount) {
    acc->balance += amount;
}

int main(void) {
    BankAccount acc = {5501, 1000.00};
    deposit(&acc, 250.50);
    printf("Account %d Balance: $%.2f\\n", acc.account_num, acc.balance);
    return 0;
}"""

    m11_out_real = """Account 5501 Balance: $1250.50"""

    m11_exp_real = """Uses `typedef struct` and arrow operator inside a helper function to update bank account balance directly in memory."""

    m11_mistakes = """1. Using dot operator `ptr.x` on a struct pointer instead of arrow operator `ptr->x`.
2. Forgetting semicolon `;` after ending structure declaration brace `struct Data { ... };`.
3. Expecting `union` fields to store independent values simultaneously (unions share memory!)."""

    m11_best = """1. Use `typedef struct` to eliminate repeating `struct` keyword in declarations.
2. Pass large structures to functions by const pointer (`const Student *s`) to avoid stack copying overhead.
3. Order struct fields from largest to smallest byte size to minimize alignment padding waste."""

    m11_exs = [
        {
            "title": "Book Structure Printer",
            "description": "Define struct Book {int id; float price;}. Read '101 29.99' and print 'Book 101: $29.99'.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\n// Define struct Book\n\nint main(void) {\n    // Read and print book struct\n    return 0;\n}\n",
            "language": "c",
            "order_index": 1,
            "test_cases": [{"input_data": "101 29.99\n", "expected_output": "Book 101: $29.99\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Typedef Rectangle Area Calculator",
            "description": "Define typedef struct Rectangle {int w, h;}. Read '5 8' and print 'Area = 40'.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\n// Define typedef Rectangle\n\nint main(void) {\n    // Read width/height and compute area\n    return 0;\n}\n",
            "language": "c",
            "order_index": 2,
            "test_cases": [{"input_data": "5 8\n", "expected_output": "Area = 40\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Structure Pointer Arrow Modifier",
            "description": "Write `void update_salary(Employee *e, double inc)`. Read salary 50000 inc 5000. Print 'New Salary = 55000.00'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\ntypedef struct {\n    double salary;\n} Employee;\n\n// Write update_salary function\n\nint main(void) {\n    Employee emp;\n    double inc;\n    if (scanf(\"%lf %lf\", &emp.salary, &inc) == 2) {\n        // Update and print\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 3,
            "test_cases": [{"input_data": "50000 5000\n", "expected_output": "New Salary = 55000.00\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Array of Structs Highest Grade Finder",
            "description": "Read 2 students (id score). Student 1: 101 80, Student 2: 102 95. Print 'Top Student ID: 102'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\ntypedef struct {\n    int id;\n    int score;\n} Student;\n\nint main(void) {\n    Student list[2];\n    // Find top student\n    return 0;\n}\n",
            "language": "c",
            "order_index": 4,
            "test_cases": [{"input_data": "101 80\n 102 95\n", "expected_output": "Top Student ID: 102\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Enum State Machine Evaluator",
            "description": "Define enum State {STOP, GO}. Read integer 1 (GO). Print 'Status: Moving' for GO or 'Status: Stopped' for STOP.",
            "difficulty": "Hard",
            "starter_code": "#include <stdio.h>\n\ntypedef enum { STOP, GO } State;\n\nint main(void) {\n    int val;\n    if (scanf(\"%d\", &val) == 1) {\n        // Switch state\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 5,
            "test_cases": [{"input_data": "1\n", "expected_output": "Status: Moving\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Union Memory Footprint Inspector",
            "description": "Define union Data {int i; float f; char str[20];}. Print sizeof(union Data) to prove it equals 20 (largest field size).",
            "difficulty": "Challenge",
            "starter_code": "#include <stdio.h>\n\nunion Data {\n    int i;\n    float f;\n    char str[20];\n};\n\nint main(void) {\n    printf(\"Union Size = %zu\\n\", sizeof(union Data));\n    return 0;\n}\n",
            "language": "c",
            "order_index": 6,
            "test_cases": [{"input_data": "", "expected_output": "Union Size = 20\n", "is_hidden": False, "order_index": 1}]
        }
    ]

    m11_quizzes = [
        {
            "question_text": "What operator accesses structure members when working with a pointer to a struct?",
            "options": ["Dot operator .", "Arrow operator ->", "Scope operator ::", "Ampersand operator &"],
            "correct_answer": "Arrow operator ->",
            "explanation": "The arrow operator -> dereferences the struct pointer and accesses member fields directly (ptr->member).",
            "difficulty": "Beginner"
        },
        {
            "question_text": "How does memory allocation in a union differ from a struct?",
            "options": ["Union allocates separate memory per field", "Union shares a single memory region equal to its largest field", "Union stores data on disk", "Union cannot store integers"],
            "correct_answer": "Union shares a single memory region equal to its largest field",
            "explanation": "All union fields overlap in the exact same memory space, enabling memory savings when fields are mutually exclusive.",
            "difficulty": "Beginner"
        }
    ,
        {
            "question_text": "What is the purpose of a 'struct' in C?",
            "options": ["To create an array of identical types", "To group related variables of different data types under a single name", "To create a loop", "To declare global constants"],
            "correct_answer": "To group related variables of different data types under a single name",
            "explanation": "Structs allow developers to build complex composite data types representing real-world objects.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "How do you access a member 'age' of a struct instance 'person'?",
            "options": ["person->age", "person.age", "person::age", "person[age]"],
            "correct_answer": "person.age",
            "explanation": "The dot operator (.) is used to access fields of a direct struct variable.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "If you have a pointer to a struct (`struct Person *ptr`), how do you access the 'age' member?",
            "options": ["ptr.age", "*ptr.age", "ptr->age", "ptr::age"],
            "correct_answer": "ptr->age",
            "explanation": "The arrow operator (->) is required when accessing members through a pointer, replacing (*ptr).age.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What is 'padding' in the context of C structures?",
            "options": ["Empty space inserted by the compiler between struct members to align them for faster CPU memory access", "A security feature to prevent buffer overflows", "Extra memory allocated at the end of a struct for dynamic arrays", "Whitespace in the source code"],
            "correct_answer": "Empty space inserted by the compiler between struct members to align them for faster CPU memory access",
            "explanation": "CPUs fetch memory faster when it aligns with hardware word boundaries (e.g., 4 or 8 bytes). Compilers pad structs to ensure this alignment.",
            "difficulty": "Hard"
        },
        {
            "question_text": "How does a 'union' fundamentally differ from a 'struct'?",
            "options": ["A union cannot contain integers", "A union allocates memory for all its fields simultaneously", "All members of a union share the exact same memory location, meaning it can only hold one active value at a time", "A union is only used for networking"],
            "correct_answer": "All members of a union share the exact same memory location, meaning it can only hold one active value at a time",
            "explanation": "Unions overlay their fields in memory. Overwriting one field destroys the data in the other fields.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What is the primary use case for the 'typedef' keyword?",
            "options": ["To define macros", "To allocate memory", "To create an alias for an existing data type to simplify complex declarations", "To include header files"],
            "correct_answer": "To create an alias for an existing data type to simplify complex declarations",
            "explanation": "typedef allows you to alias complex struct declarations so you don't have to repeat the 'struct' keyword everywhere.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What does an 'enum' (enumeration) do?",
            "options": ["Assigns custom string values to variables", "Defines a set of named integer constants for better code readability", "Allocates a dynamic array", "Parses user input"],
            "correct_answer": "Defines a set of named integer constants for better code readability",
            "explanation": "Enums map readable names (like STATE_RUNNING) to integers (like 0, 1, 2) to replace hardcoded numbers.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "If a struct contains a char (1 byte) and an int (4 bytes), what is its typical size on a 32-bit system due to padding?",
            "options": ["5 bytes", "6 bytes", "8 bytes", "4 bytes"],
            "correct_answer": "8 bytes",
            "explanation": "The char uses 1 byte, followed by 3 bytes of padding, followed by the 4-byte int, totaling 8 bytes.",
            "difficulty": "Hard"
        }
    ]

    modules.append(build_lesson(
        "Structures, Unions, Enums & Typedef", "c-structures-unions-enums-typedef",
        m11_what, m11_why, m11_how, m11_syntax, m11_ex_sim, m11_ex_real, m11_out_sim, m11_lbl_sim, m11_out_real, m11_exp_real, m11_mistakes, m11_best, m11_exs, m11_quizzes
    ))

    # =========================================================================
    # MODULE 12: Dynamic Memory Management
    # =========================================================================
    m12_what = """Dynamic memory allocation enables programs to request RAM memory from the operating system heap at runtime when exact memory sizes are unknown at compile time.

C standard library `<stdlib.h>` provides four key dynamic memory allocation functions:
- `malloc(size)`: Allocates uninitialized heap bytes.
- `calloc(num, size)`: Allocates heap bytes zero-initialized to 0.
- `realloc(ptr, new_size)`: Resizes existing heap memory block.
- `free(ptr)`: Deallocates heap memory back to system heap."""

    m12_why = """Fixed stack arrays (`int arr[100];`) force developers to guess maximum sizes. If user inputs 1,000 items, fixed arrays overflow; if user inputs 2 items, fixed arrays waste memory.

Dynamic memory enables programs to expand and shrink memory dynamically based on real-time workloads.

Failing to call `free()` causes memory Leaks—consuming RAM until the system runs out of memory and crashes."""

    m12_how = """Stack vs Heap Memory Layout:

```
Process RAM Address Space Architecture:
High RAM Addresses
---------------------------------
Stack Segment (Automatic local variables, function frames; grows DOWN)
      v
      ^
Heap Segment (Dynamic allocations: malloc, calloc, realloc; grows UP)
---------------------------------
BSS / Data Segment (Globals & Statics)
---------------------------------
Text / Code Segment (Compiled Binary Machine Instructions)
Low RAM Addresses
```

`int *arr = (int*)malloc(n * sizeof(int));` requests `n * 4` heap bytes.
If allocation succeeds, OS returns non-NULL heap address. If out of memory, `malloc()` returns `NULL`.
Calling `free(arr);` releases heap memory back to OS. Setting `arr = NULL;` prevents dangling pointer bugs."""

    m12_syntax = """#include <stdlib.h>

int n = 5;
int *arr = (int *)malloc(n * sizeof(int));

if (arr == NULL) {
    printf("Memory Allocation Failed!\\n");
    return 1; // Exit
}

// Use allocated memory array
for (int i = 0; i < n; i++) {
    arr[i] = (i + 1) * 10;
}

// Free allocated heap memory
free(arr);
arr = NULL;"""

    m12_ex_sim = """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *p = (int *)malloc(sizeof(int));
    if (p != NULL) {
        *p = 500;
        printf("Heap Integer Value = %d\\n", *p);
        free(p);
        p = NULL;
    }
    return 0;
}"""

    m12_out_sim = """Heap Integer Value = 500"""

    m12_lbl_sim = """- `malloc(sizeof(int))`: Requests heap RAM memory for 1 integer.
- `if (p != NULL)`: Defensive check verifying OS granted heap memory.
- `free(p); p = NULL;`: Deallocates heap memory block and clears pointer."""

    m12_ex_real = """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int count = 3;
    int *scores = (int *)calloc(count, sizeof(int));

    if (scores == NULL) return 1;

    printf("Calloc Zero-Initialized Elements: ");
    for (int i = 0; i < count; i++) {
        printf("%d ", scores[i]);
    }
    printf("\\n");

    free(scores);
    scores = NULL;
    return 0;
}"""

    m12_out_real = """Calloc Zero-Initialized Elements: 0 0 0"""

    m12_exp_real = """Allocates 3 integer scores on heap zero-initialized to 0 using `calloc`, verifying memory before deallocating."""

    m12_mistakes = """1. Forgetting to call `free()`, creating memory leaks.
2. Using memory after calling `free()` (use-after-free bug).
3. Failing to check if `malloc()` returned `NULL` before accessing memory.
4. Calling `free()` twice on the same pointer (double-free vulnerability)."""

    m12_best = """1. Always pair every `malloc()` / `calloc()` call with a corresponding `free()`.
2. Immediately set pointers to `NULL` after freeing (`free(ptr); ptr = NULL;`).
3. Always check `if (ptr == NULL)` before accessing allocated dynamic memory."""

    m12_exs = [
        {
            "title": "Dynamic Integer Array Allocation",
            "description": "Read size N (e.g. 3) and N elements '10 20 30'. Allocate with malloc, compute sum, print 'Sum = 60', free memory.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\nint main(void) {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        // Malloc array, sum elements, print, free\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 1,
            "test_cases": [{"input_data": "3\n 10 20 30\n", "expected_output": "Sum = 60\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Calloc Zero Initialization Inspector",
            "description": "Allocate 4 ints with calloc. Print space-separated elements to verify zero initialization: '0 0 0 0 ', free memory.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\nint main(void) {\n    // Allocate calloc, print, free\n    return 0;\n}\n",
            "language": "c",
            "order_index": 2,
            "test_cases": [{"input_data": "", "expected_output": "0 0 0 0 \n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Realloc Array Expander Engine",
            "description": "Allocate 2 ints with malloc (10, 20). Realloc to 4 ints, set [2]=30, [3]=40. Print sum 'Sum = 100', free memory.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\nint main(void) {\n    // Malloc 2, realloc to 4, print sum\n    return 0;\n}\n",
            "language": "c",
            "order_index": 3,
            "test_cases": [{"input_data": "", "expected_output": "Sum = 100\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Dynamic String Duplicate Function",
            "description": "Write `char* my_strdup(const char *s)`. Duplicate 'Learnx', print duplicate, free memory.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\n// Write my_strdup\n\nint main(void) {\n    // Duplicate and print\n    return 0;\n}\n",
            "language": "c",
            "order_index": 4,
            "test_cases": [{"input_data": "", "expected_output": "Dup = Learnx\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Dynamic Struct Heap Allocator",
            "description": "Dynamically allocate `Person` struct (age=25). Print age, free memory.",
            "difficulty": "Hard",
            "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\ntypedef struct {\n    int age;\n} Person;\n\nint main(void) {\n    // Dynamically allocate Person, set age, print, free\n    return 0;\n}\n",
            "language": "c",
            "order_index": 5,
            "test_cases": [{"input_data": "", "expected_output": "Age = 25\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Dynamic 2D Matrix Heap Allocator",
            "description": "Dynamically allocate 2x2 matrix using pointer-to-pointers (`int **`). Fill values 1 2 3 4, print, free row pointers and main pointer.",
            "difficulty": "Challenge",
            "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\nint main(void) {\n    // Allocate 2D matrix on heap, print, free\n    return 0;\n}\n",
            "language": "c",
            "order_index": 6,
            "test_cases": [{"input_data": "", "expected_output": "1 2 \n3 4 \n", "is_hidden": False, "order_index": 1}]
        }
    ]

    m12_quizzes = [
        {
            "question_text": "What is the primary difference between malloc() and calloc()?",
            "options": ["malloc zeroes memory, calloc leaves garbage", "calloc zeroes memory bytes, malloc leaves uninitialized garbage bytes", "malloc works on stack, calloc on heap", "calloc cannot allocate arrays"],
            "correct_answer": "calloc zeroes memory bytes, malloc leaves uninitialized garbage bytes",
            "explanation": "calloc clears allocated heap bytes to 0, whereas malloc leaves existing uninitialized memory bits intact.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What occurs when a program allocates heap memory with malloc() but never calls free()?",
            "options": ["Compiler error", "Memory Leak (heap RAM remains consumed until process terminates)", "Automatic stack deallocation", "Disk corruption"],
            "correct_answer": "Memory Leak (heap RAM remains consumed until process terminates)",
            "explanation": "Unfreed heap memory causes memory leaks, consuming operating system RAM resources.",
            "difficulty": "Beginner"
        }
    ,
        {
            "question_text": "Which memory segment grows dynamically as the program requests memory at runtime?",
            "options": ["The Stack", "The BSS Segment", "The Heap", "The Code/Text Segment"],
            "correct_answer": "The Heap",
            "explanation": "The heap is used for dynamic memory allocation (malloc), while the stack handles automatic local variables.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What does the malloc() function do?",
            "options": ["Initializes memory to zero", "Allocates a requested number of uninitialized bytes on the heap and returns a pointer to it", "Frees memory", "Resizes an array on the stack"],
            "correct_answer": "Allocates a requested number of uninitialized bytes on the heap and returns a pointer to it",
            "explanation": "malloc (memory allocation) grabs raw heap memory. The developer is responsible for tracking and freeing it.",
            "difficulty": "Medium"
        },
        {
            "question_text": "How does calloc() differ from malloc()?",
            "options": ["calloc allocates on the stack", "calloc is faster", "calloc automatically initializes the allocated memory bytes to zero", "calloc automatically frees memory"],
            "correct_answer": "calloc automatically initializes the allocated memory bytes to zero",
            "explanation": "While malloc leaves memory with garbage values, calloc wipes the memory clean to zeros before returning it.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What is a memory leak?",
            "options": ["A hardware failure in RAM", "A situation where dynamically allocated heap memory is never freed, exhausting available RAM", "A buffer overflow that overwrites other variables", "A null pointer dereference"],
            "correct_answer": "A situation where dynamically allocated heap memory is never freed, exhausting available RAM",
            "explanation": "Losing the pointer to heap memory without calling free() creates an unrecoverable leak until the OS kills the process.",
            "difficulty": "Hard"
        },
        {
            "question_text": "What is the purpose of the realloc() function?",
            "options": ["To free memory", "To initialize memory", "To resize a previously allocated block of heap memory, preserving its existing contents", "To copy memory from stack to heap"],
            "correct_answer": "To resize a previously allocated block of heap memory, preserving its existing contents",
            "explanation": "realloc requests a larger (or smaller) memory block. If it has to move the data to a new location, it copies it automatically.",
            "difficulty": "Hard"
        },
        {
            "question_text": "What does malloc() return if the system is completely out of RAM?",
            "options": ["A random address", "The program crashes immediately", "It returns a NULL pointer", "It waits until memory is available"],
            "correct_answer": "It returns a NULL pointer",
            "explanation": "Malloc fails gracefully by returning NULL. Developers must check for NULL before using the pointer.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What is a 'dangling pointer'?",
            "options": ["A pointer that holds the address of memory that has already been freed", "A pointer that points to a string", "A pointer initialized to NULL", "A pointer to a function"],
            "correct_answer": "A pointer that holds the address of memory that has already been freed",
            "explanation": "Accessing a dangling pointer (use-after-free) causes undefined behavior because the memory might have been reassigned to something else.",
            "difficulty": "Hard"
        },
        {
            "question_text": "Why should you set a pointer to NULL immediately after calling free(p)?",
            "options": ["To free the memory twice", "To trigger garbage collection", "To prevent dangling pointer bugs by ensuring accidental dereferences safely crash rather than corrupting memory", "To save memory space"],
            "correct_answer": "To prevent dangling pointer bugs by ensuring accidental dereferences safely crash rather than corrupting memory",
            "explanation": "Setting it to NULL turns a dangerous silent corruption bug into an immediate, easy-to-detect crash.",
            "difficulty": "Hard"
        }
    ]

    # Stage 4 Project definition for Module 12
    m12_project = {
        "title": "Contact Book & Persistent Storage System",
        "scenario": "You are building a contact book management application that dynamically allocates memory for contacts and resizes array capacity as contacts are added.",
        "objective": "Build a dynamic array storage module that expands capacity using realloc when full.",
        "requirements": ["Allocate initial heap contact list using malloc", "Expand capacity dynamically with realloc", "Free heap memory cleanly without leaks"],
        "features": ["Dynamic Resizable List", "Heap Guard Engine"],
        "required_concepts": ["Dynamic Memory", "Structures", "Pointers", "Realloc"],
        "architecture": "Dynamic array heap buffer doubling capacity on overflow.",
        "guidance": ["Double capacity when count reaches current max", "Check for NULL realloc returns"],
        "hints": ["Use int *temp = realloc(arr, new_size)"],
        "workflow": "Read count -> Allocate heap array -> Expand if needed -> Output result -> Free memory",
        "expected_behavior": "Input: '3 \\n 10 20 30' -> Outputs 'Capacity: 4, Element 2: 30'",
        "evaluation_criteria": "Program successfully resizes heap memory array dynamically without leaks.",
        "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\nint main(void) {\n    int cap = 2, count = 0;\n    int *arr = (int *)malloc(cap * sizeof(int));\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        for (int i = 0; i < n; i++) {\n            if (count == cap) {\n                cap *= 2;\n                arr = (int *)realloc(arr, cap * sizeof(int));\n            }\n            scanf(\"%d\", &arr[count++]);\n        }\n        printf(\"Capacity: %d, Element 2: %d\\n\", cap, arr[2]);\n        free(arr);\n    }\n    return 0;\n}\n",
        "language": "c",
        "test_cases": [
            {"input_data": "3\n 10 20 30\n", "expected_output": "Capacity: 4, Element 2: 30\n", "is_hidden": False, "order_index": 1}
        ]
    }

    modules.append(build_lesson(
        "Dynamic Memory Management", "c-dynamic-memory-management",
        m12_what, m12_why, m12_how, m12_syntax, m12_ex_sim, m12_ex_real, m12_out_sim, m12_lbl_sim, m12_out_real, m12_exp_real, m12_mistakes, m12_best, m12_exs, m12_quizzes, m12_project
    ))

    # =========================================================================
    # MODULE 13: File Handling
    # =========================================================================
    m13_what = """File handling allows C programs to persist data permanently on disk storage rather than losing variable state when execution terminates.

C manages files via standard library `FILE *` handle pointers defined in `<stdio.h>`.

Key file operations:
- `fopen(filename, mode)`: Opens file stream (`"w"` write, `"r"` read, `"a"` append, `"wb"` binary write, `"rb"` binary read).
- `fclose(file_ptr)`: Flushes buffers and closes file stream.
- Text I/O: `fprintf`, `fscanf`, `fgets`, `fputs`.
- Binary I/O: `fwrite`, `fread`.
- File positioning: `fseek`, `ftell`, `rewind`."""

    m13_why = """Programs operating solely in RAM lose all data when powered down or closed. File handling enables saving configuration settings, user records, persistent databases, and application logs to disk files.

Binary file I/O (`fwrite`/`fread`) saves exact memory structures directly to disk with maximum performance."""

    m13_how = """`FILE *fp = fopen("data.txt", "w");` requests OS file handle.

If opening fails (e.g. file non-existent or read-only permissions), `fopen()` returns `NULL`.

`fprintf(fp, "Score: %d\n", score);` formats and writes text into file buffer.

`fclose(fp);` flushes pending write buffer data onto physical disk storage."""

    m13_syntax = """#include <stdio.h>

FILE *fp = fopen("config.txt", "w");
if (fp != NULL) {
    fprintf(fp, "Port=8080\\n");
    fclose(fp);
}

// Reading text file
fp = fopen("config.txt", "r");
if (fp != NULL) {
    char buffer[100];
    if (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("Read: %s", buffer);
    }
    fclose(fp);
}"""

    m13_ex_sim = """#include <stdio.h>

int main(void) {
    FILE *fp = fopen("test.txt", "w");
    if (fp != NULL) {
        fputs("C File I/O Engine\\n", fp);
        fclose(fp);
        printf("File written successfully.\\n");
    }
    return 0;
}"""

    m13_out_sim = """File written successfully."""

    m13_lbl_sim = """- `FILE *fp = fopen("test.txt", "w");`: Opens file handle in write mode.
- `fputs("...", fp);`: Writes string text to file stream.
- `fclose(fp);`: Flushes file write buffers to physical disk."""

    m13_ex_real = """#include <stdio.h>

typedef struct {
    int id;
    double price;
} Product;

int main(void) {
    Product p1 = {101, 49.99};
    FILE *fp = fopen("prod.bin", "wb");
    if (fp != NULL) {
        fwrite(&p1, sizeof(Product), 1, fp);
        fclose(fp);
        printf("Binary product record saved successfully.\\n");
    }
    return 0;
}"""

    m13_out_real = """Binary product record saved successfully."""

    m13_exp_real = """Writes an entire struct binary record to disk file using `fwrite`."""

    m13_mistakes = """1. Failing to check `if (fp == NULL)` after calling `fopen()`, leading to crashes if file fails to open.
2. Forgetting to call `fclose(fp)`, leading to file handle leaks and lost buffered file writes.
3. Using text mode `"w"` or `"r"` for binary struct data instead of `"wb"` or `"rb"`."""

    m13_best = """1. Always check for `NULL` file handle pointers after `fopen()`.
2. Always call `fclose()` when finished processing file streams.
3. Use `fgets()` rather than `fscanf()` for robust multi-word line parsing."""

    m13_exs = [
        {
            "title": "File Writer and Success Reporter",
            "description": "Write a program that writes 'Learnx Log' to 'app.log'. Print 'Log Saved' and close file.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    // Open app.log in write mode, write text, close, print 'Log Saved'\n    return 0;\n}\n",
            "language": "c",
            "order_index": 1,
            "test_cases": [{"input_data": "", "expected_output": "Log Saved\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "File Null Pointer Guard",
            "description": "Attempt to open non-existent file 'missing.txt' in read mode. Verify NULL and print 'File Not Found'.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    // Check NULL for missing.txt\n    return 0;\n}\n",
            "language": "c",
            "order_index": 2,
            "test_cases": [{"input_data": "", "expected_output": "File Not Found\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Formatted fprintf Record Writer",
            "description": "Write formatted record 'ID: 50, Score: 95.5' to 'score.txt' using fprintf. Print 'Score Written'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    // fprintf record to file\n    return 0;\n}\n",
            "language": "c",
            "order_index": 3,
            "test_cases": [{"input_data": "", "expected_output": "Score Written\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Binary Struct Record Writer and Reader",
            "description": "Write struct `{int code=404;}` to 'err.bin' with `fwrite`, then read back with `fread` and print 'Code = 404'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\ntypedef struct { int code; } Err;\n\nint main(void) {\n    // Write and read binary struct\n    return 0;\n}\n",
            "language": "c",
            "order_index": 4,
            "test_cases": [{"input_data": "", "expected_output": "Code = 404\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "File Position Seeker with fseek and ftell",
            "description": "Write 'abcdef' to 'seek.txt'. Use `fseek(fp, 0, SEEK_END)` and `ftell(fp)` to compute byte size. Print 'File Size = 6'.",
            "difficulty": "Hard",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    // Write text, seek end, ftell size\n    return 0;\n}\n",
            "language": "c",
            "order_index": 5,
            "test_cases": [{"input_data": "", "expected_output": "File Size = 6\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "File Line Counter Utility",
            "description": "Write 3 lines to 'lines.txt'. Reopen, read line-by-line using `fgets`, count lines, and print 'Line Count = 3'.",
            "difficulty": "Challenge",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    // Count lines using fgets\n    return 0;\n}\n",
            "language": "c",
            "order_index": 6,
            "test_cases": [{"input_data": "", "expected_output": "Line Count = 3\n", "is_hidden": False, "order_index": 1}]
        }
    ]

    m13_quizzes = [
        {
            "question_text": "Which file open mode creates a new file for writing (or truncates an existing file)?",
            "options": ["\"r\"", "\"w\"", "\"a\"", "\"rb\""],
            "correct_answer": "\"w\"",
            "explanation": "Mode \"w\" opens a text file for write operations, truncating existing content or creating a new file.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What does fopen() return if a requested file cannot be opened?",
            "options": ["-1", "NULL", "EOF", "0"],
            "correct_answer": "NULL",
            "explanation": "If fopen fails (e.g. invalid path or missing permissions), it returns a NULL pointer.",
            "difficulty": "Beginner"
        }
    ,
        {
            "question_text": "What data type is used as a handle for file operations in C?",
            "options": ["int", "FILE *", "char *", "struct File"],
            "correct_answer": "FILE *",
            "explanation": "The FILE structure pointer represents an I/O stream, tracking buffers, file position indicators, and errors.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "Which function opens a file in C?",
            "options": ["open()", "read()", "fopen()", "file_open()"],
            "correct_answer": "fopen()",
            "explanation": "fopen() bridges the program to the OS file system, returning a FILE pointer.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What happens if you open a file in 'w' (write) mode and the file already exists?",
            "options": ["An error is returned", "Data is appended to the end of the file", "The file's existing contents are immediately truncated (erased)", "The program crashes"],
            "correct_answer": "The file's existing contents are immediately truncated (erased)",
            "explanation": "Write mode ('w') destroys existing data. To preserve data, append mode ('a') must be used.",
            "difficulty": "Medium"
        },
        {
            "question_text": "Which mode should be used to read a binary file (like an image)?",
            "options": ["'r'", "'rb'", "'w'", "'wb'"],
            "correct_answer": "'rb'",
            "explanation": "'rb' specifies read-binary, preventing the OS from interpreting newline characters differently (crucial on Windows).",
            "difficulty": "Medium"
        },
        {
            "question_text": "Why is it strictly necessary to call fclose() when finished with a file?",
            "options": ["To prevent memory leaks and ensure I/O buffers are flushed to the disk", "To format the disk", "To compile the file", "To convert the file to a string"],
            "correct_answer": "To prevent memory leaks and ensure I/O buffers are flushed to the disk",
            "explanation": "fclose() writes pending buffered data to the physical disk and releases OS file locks.",
            "difficulty": "Hard"
        },
        {
            "question_text": "Which function reads a formatted string from a file, similar to scanf?",
            "options": ["fprintf()", "fscanf()", "fgets()", "fread()"],
            "correct_answer": "fscanf()",
            "explanation": "fscanf() parses data from a FILE stream using format specifiers like %d and %s.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What function is used for bulk reading raw binary data structures from a file?",
            "options": ["fgets()", "fgetc()", "fread()", "fscanf()"],
            "correct_answer": "fread()",
            "explanation": "fread() reads a specified number of bytes directly into a memory buffer without formatting.",
            "difficulty": "Hard"
        },
        {
            "question_text": "What does EOF signify in file processing?",
            "options": ["End Of File – a macro indicating no more data can be read from the stream", "Error On File – a disk hardware failure", "Execute Object File – running a binary", "End Of Formatting"],
            "correct_answer": "End Of File – a macro indicating no more data can be read from the stream",
            "explanation": "EOF (usually -1) is returned by reading functions when the file pointer reaches the end of the file.",
            "difficulty": "Beginner"
        }
    ]

    modules.append(build_lesson(
        "File Handling", "c-file-handling",
        m13_what, m13_why, m13_how, m13_syntax, m13_ex_sim, m13_ex_real, m13_out_sim, m13_lbl_sim, m13_out_real, m13_exp_real, m13_mistakes, m13_best, m13_exs, m13_quizzes
    ))

    # =========================================================================
    # MODULE 14: Preprocessor, Header Files & Advanced C
    # =========================================================================
    m14_what = """The C preprocessor runs prior to compilation, evaluating directives starting with `#`.

Directives include:
- `#define`: Defines constant macros or macro functions.
- `#include`: Includes header files (`.h`).
- `#ifndef`, `#define`, `#endif`: Include guards preventing duplicate header inclusions.
- Conditional compilation: `#ifdef`, `#else`.

Advanced C features include modular compilation across multiple source files, `extern` linkage declarations, function pointers (`int (*func_ptr)(int, int)`), and volatile/const type qualifiers."""

    m14_why = """Large C applications consist of hundreds of separate source files. Header guards prevent compilation errors caused by re-declaring types across header inclusions.

Function pointers allow passing functions as arguments to other functions, enabling event callbacks, custom comparator functions in sorting, and object-oriented polymorphism patterns in C."""

    m14_how = """Header inclusion `#include "my_header.h"` instructs preprocessor to copy contents of `my_header.h` into current file.

Include guards:
```c
#ifndef MATH_UTILS_H
#define MATH_UTILS_H
// Declarations
#endif
```
Function pointer `int (*op)(int, int) = add;` stores address of function `add()`. Executing `op(5, 10)` invokes `add(5, 10)` dynamically!"""

    m14_syntax = """#ifndef MATH_UTILS_H
#define MATH_UTILS_H

#define SQUARE(x) ((x) * (x))

typedef int (*MathFunc)(int, int);

int compute(int a, int b, MathFunc func);

#endif"""

    m14_ex_sim = """#include <stdio.h>

#define MIN(a, b) (((a) < (b)) ? (a) : (b))

int main(void) {
    int res = MIN(15, 8);
    printf("Min value = %d\\n", res);
    return 0;
}"""

    m14_out_sim = """Min value = 8"""

    m14_lbl_sim = """- `#define MIN(...)`: Preprocessor macro expanding inline before compilation."""

    m14_ex_real = """#include <stdio.h>

int add(int a, int b) { return a + b; }
int multiply(int a, int b) { return a * b; }

void run_op(int x, int y, int (*operation)(int, int)) {
    printf("Operation Result = %d\\n", operation(x, y));
}

int main(void) {
    run_op(4, 5, add);
    run_op(4, 5, multiply);
    return 0;
}"""

    m14_out_real = """Operation Result = 9
Operation Result = 20"""

    m14_exp_real = """Passes function pointers dynamically to a callback runner function."""

    m14_mistakes = """1. Omitting parentheses around macro parameters (`#define SQUARE(x) x * x` causes `SQUARE(1+2)` to expand to `1+2*1+2 = 5`!).
2. Forgetting include guards in custom `.h` header files.
3. Complex function pointer syntax errors (`int *func(int)` is a function returning pointer, `int (*func)(int)` is a function pointer!)."""

    m14_best = """1. Wrap all parameters in macro definitions with parentheses: `((x) * (x))`.
2. Always add `#ifndef HEADER_NAME_H` include guards to every header file.
3. Use `typedef` to clean up complex function pointer declarations."""

    m14_exs = [
        {
            "title": "Macro Function Parameterized Calculator",
            "description": "Define `#define CUBE(x) ((x)*(x)*(x))`. Read '3' and print 'Cube = 27'.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\n// Define CUBE macro\n\nint main(void) {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        // Print cube\n    }\n    return 0;\n}\n",
            "language": "c",
            "order_index": 1,
            "test_cases": [{"input_data": "3\n", "expected_output": "Cube = 27\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Conditional Compilation Debug Logger",
            "description": "Use `#define DEBUG`. Write `#ifdef DEBUG printf(\"[DEBUG] Active\\n\"); #endif`. Print output.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n#define DEBUG\n\nint main(void) {\n    // Conditional debug print\n    return 0;\n}\n",
            "language": "c",
            "order_index": 2,
            "test_cases": [{"input_data": "", "expected_output": "[DEBUG] Active\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Function Pointer Invoker",
            "description": "Declare function `int sub(int a, int b) { return a - b; }`. Point `int (*fptr)(int, int) = sub;`. Call with '10 4', print 'Diff = 6'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\nint sub(int a, int b) { return a - b; }\n\nint main(void) {\n    // Declare function pointer and invoke\n    return 0;\n}\n",
            "language": "c",
            "order_index": 3,
            "test_cases": [{"input_data": "10 4\n", "expected_output": "Diff = 6\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Typedef Function Pointer Dispatcher",
            "description": "Define `typedef int (*OpFunc)(int, int);`. Pass `add` function to `exec(OpFunc op, int a, int b)`. Print 'Exec = 15'.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n\ntypedef int (*OpFunc)(int, int);\nint add(int a, int b) { return a + b; }\n\nint main(void) {\n    // Dispatch via typedef function pointer\n    return 0;\n}\n",
            "language": "c",
            "order_index": 4,
            "test_cases": [{"input_data": "", "expected_output": "Exec = 15\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Const Pointer Variant Inspector",
            "description": "Demonstrate `const int *p` (points to constant int) vs `int * const p` (constant pointer address). Print 'Const Pointer Verified'.",
            "difficulty": "Hard",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int x = 10, y = 20;\n    const int *p1 = &x;\n    int * const p2 = &y;\n    printf(\"Const Pointer Verified\\n\");\n    return 0;\n}\n",
            "language": "c",
            "order_index": 5,
            "test_cases": [{"input_data": "", "expected_output": "Const Pointer Verified\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Function Pointer Array Router Engine",
            "description": "Create function pointer array `OpFunc ops[2] = {add, sub};`. Read choice '1' (sub) for '20 5' and print 'Res = 15'.",
            "difficulty": "Challenge",
            "starter_code": "#include <stdio.h>\n\ntypedef int (*OpFunc)(int, int);\nint add(int a, int b) { return a + b; }\nint sub(int a, int b) { return a - b; }\n\nint main(void) {\n    // Function pointer array router\n    return 0;\n}\n",
            "language": "c",
            "order_index": 6,
            "test_cases": [{"input_data": "1 20 5\n", "expected_output": "Res = 15\n", "is_hidden": False, "order_index": 1}]
        }
    ]

    m14_quizzes = [
        {
            "question_text": "What is the purpose of include guards (#ifndef HEADER_H, #define HEADER_H ... #endif)?",
            "options": ["Speed up execution", "Prevent a header file from being included multiple times in a compilation unit", "Make variables constant", "Link external libraries"],
            "correct_answer": "Prevent a header file from being included multiple times in a compilation unit",
            "explanation": "Include guards prevent duplicate header inclusions that cause macro redefinitions and type re-declaration errors.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What does a function pointer store in C?",
            "options": ["Return value", "Physical memory RAM address of function executable machine code", "Parameter count", "Stack frame pointer"],
            "correct_answer": "Physical memory RAM address of function executable machine code",
            "explanation": "Function pointers store the starting RAM address of a function's compiled binary machine instructions.",
            "difficulty": "Beginner"
        }
    ,
        {
            "question_text": "When are preprocessor directives (like #define) executed?",
            "options": ["During execution", "During linking", "Before the code is translated into assembly language by the compiler", "During runtime memory allocation"],
            "correct_answer": "Before the code is translated into assembly language by the compiler",
            "explanation": "The preprocessor scans the source code, expanding macros and including files, creating a pure C file for the compiler.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What is the primary danger of using #define macros instead of functions?",
            "options": ["They are slower to execute", "They use more RAM", "They lack type checking and can cause unexpected side effects if arguments are evaluated multiple times (e.g., MAX(i++, j))", "They cannot return values"],
            "correct_answer": "They lack type checking and can cause unexpected side effects if arguments are evaluated multiple times (e.g., MAX(i++, j))",
            "explanation": "Macros are literal text substitutions. Passing an increment operation can result in the increment happening twice.",
            "difficulty": "Hard"
        },
        {
            "question_text": "What is the purpose of #ifndef in a header file?",
            "options": ["To define a variable", "To include a library", "To prevent a header file from being included multiple times (header guards)", "To link an object file"],
            "correct_answer": "To prevent a header file from being included multiple times (header guards)",
            "explanation": "Include guards prevent compiler errors caused by redefining structs or macros when a header is included multiple times.",
            "difficulty": "Hard"
        },
        {
            "question_text": "What is the difference between #include <file.h> and #include \"file.h\"?",
            "options": ["<file.h> is for C, \"file.h\" is for C++", "They are identical", "<file.h> searches standard system directories, \"file.h\" searches the local directory first", "The first is a macro, the second is a function"],
            "correct_answer": "<file.h> searches standard system directories, \"file.h\" searches the local directory first",
            "explanation": "Angle brackets are used for standard libraries, quotes are used for project-local header files.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What is conditional compilation?",
            "options": ["Compiling only if the user types a password", "Using #ifdef and #endif to include or exclude blocks of code during preprocessing (e.g., for debug vs release builds)", "Compiling code in a loop", "Executing code depending on a runtime if statement"],
            "correct_answer": "Using #ifdef and #endif to include or exclude blocks of code during preprocessing (e.g., for debug vs release builds)",
            "explanation": "Conditional compilation physically removes code blocks from the source file before the compiler sees them based on macros.",
            "difficulty": "Hard"
        },
        {
            "question_text": "Can a #define macro contain multiple lines of code?",
            "options": ["No, it is strictly one line", "Yes, by using the backslash (\) line continuation character", "Yes, by enclosing it in {}", "Yes, using semicolons"],
            "correct_answer": "Yes, by using the backslash (\) line continuation character",
            "explanation": "The backslash escapes the newline, allowing the preprocessor to treat multi-line code as a single logical line.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What is a variadic macro?",
            "options": ["A macro that takes no arguments", "A macro that takes a variable number of arguments using ... and __VA_ARGS__", "A macro used for variables", "A macro that changes its return type"],
            "correct_answer": "A macro that takes a variable number of arguments using ... and __VA_ARGS__",
            "explanation": "Variadic macros are highly useful for custom logging wrappers that wrap printf.",
            "difficulty": "Hard"
        },
        {
            "question_text": "How do you permanently undefine a macro during preprocessing?",
            "options": ["#delete", "#remove", "#undef", "#clear"],
            "correct_answer": "#undef",
            "explanation": "#undef removes a previously defined macro, allowing you to redefine it differently further down the file.",
            "difficulty": "Beginner"
        }
    ]

    modules.append(build_lesson(
        "Preprocessor, Header Files & Advanced C", "c-preprocessor-header-files-advanced",
        m14_what, m14_why, m14_how, m14_syntax, m14_ex_sim, m14_ex_real, m14_out_sim, m14_lbl_sim, m14_out_real, m14_exp_real, m14_mistakes, m14_best, m14_exs, m14_quizzes
    ))

    # =========================================================================
    # MODULE 15: Practical C, Debugging & DSA Foundations
    # =========================================================================
    m15_what = """Practical real-world C development combines modular code design, command-line argument processing (`argc`, `argv`), defensive memory debugging, and foundational Data Structures & Algorithms (DSA).

A Dynamic Singly Linked List is a classic foundational data structure where each node structure contains a data payload and a pointer to the next node (`struct Node *next`).

Unlike array contiguous memory blocks, linked lists allocate memory dynamically on the heap per node, enabling `O(1)` insertions and deletions without memory shifting."""

    m15_why = """Completing C mastery requires synthesizing all foundational concepts: variables, operators, loops, functions, pointers, dynamic memory allocation (`malloc`/`free`), structures, and file I/O into real software.

Understanding linked lists provides the mental bridge to advanced computer science topics like queues, stacks, trees, and graphs.

Command-line arguments (`int main(int argc, char *argv[])`) enable utilities to receive options directly from operating system terminal shells."""

    m15_how = """Singly Linked List Heap Architecture:

```
Singly Linked List Memory Traversal:
Head Pointer (0x1000)
     |
     v
[ Node 1 ] Address: 0x1000 | Data: 10 | next: 0x2000
     |
     v
[ Node 2 ] Address: 0x2000 | Data: 20 | next: NULL
```

Command-line signature: `int main(int argc, char *argv[])`
`argc` holds total argument count; `argv[0]` holds executable name string; `argv[1]` holds first argument string."""

    m15_syntax = """#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int val;
    struct Node *next;
} Node;

Node* create_node(int value) {
    Node *new_node = (Node *)malloc(sizeof(Node));
    if (new_node != NULL) {
        new_node->val = value;
        new_node->next = NULL;
    }
    return new_node;
}"""

    m15_ex_sim = """#include <stdio.h>

int main(int argc, char *argv[]) {
    printf("Arg Count = %d\\n", argc);
    return 0;
}"""

    m15_out_sim = """Arg Count = 1"""

    m15_lbl_sim = """- `int main(int argc, char *argv[])`: Main signature receiving CLI arguments.
- `argc`: Total count of command line argument strings passed to executable."""

    m15_ex_real = """#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

int main(void) {
    Node *head = (Node *)malloc(sizeof(Node));
    Node *second = (Node *)malloc(sizeof(Node));

    head->data = 100;
    head->next = second;

    second->data = 200;
    second->next = NULL;

    printf("List: %d -> %d -> NULL\\n", head->data, head->next->data);

    free(second);
    free(head);
    return 0;
}"""

    m15_out_real = """List: 100 -> 200 -> NULL"""

    m15_exp_real = """Constructs a 2-node dynamic Singly Linked List on the heap and traverses elements."""

    m15_mistakes = """1. Dereferencing `next` pointer on a NULL node (`head->next->data` when `head->next` is NULL).
2. Losing `head` pointer of a linked list, causing memory leaks.
3. Freeing head node before reading `head->next` address during traversal."""

    m15_best = """1. Use temporary traversal pointers (`Node *curr = head;`) to traverse linked lists cleanly.
2. Free linked list nodes sequentially in a loop, storing `curr->next` before calling `free(curr)`.
3. Check `argc` count before accessing `argv[i]` command line array indices."""

    m15_exs = [
        {
            "title": "CLI Argument Reporter",
            "description": "Print 'Exec = ./app, Args = 1' for default CLI execution.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n\nint main(int argc, char *argv[]) {\n    printf(\"Exec = %s, Args = %d\\n\", \"./app\", argc);\n    return 0;\n}\n",
            "language": "c",
            "order_index": 1,
            "test_cases": [{"input_data": "", "expected_output": "Exec = ./app, Args = 1\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Linked List Node Allocator",
            "description": "Allocate dynamic Node (val=50). Print 'Node Val = 50', free node memory.",
            "difficulty": "Easy",
            "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\ntypedef struct Node {\n    int val;\n    struct Node *next;\n} Node;\n\nint main(void) {\n    // Allocate node, print val, free\n    return 0;\n}\n",
            "language": "c",
            "order_index": 2,
            "test_cases": [{"input_data": "", "expected_output": "Node Val = 50\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Linked List 3-Node Chain Constructor",
            "description": "Create 3 linked list nodes (10 -> 20 -> 30). Traverse and print '10 -> 20 -> 30 -> NULL', free nodes.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\ntypedef struct Node {\n    int data;\n    struct Node *next;\n} Node;\n\nint main(void) {\n    // Build 3 node list, traverse, print, free\n    return 0;\n}\n",
            "language": "c",
            "order_index": 3,
            "test_cases": [{"input_data": "", "expected_output": "10 -> 20 -> 30 -> NULL\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Linked List Element Search Utility",
            "description": "Build list 5 -> 15 -> 25. Search target 15. Print 'Found 15 in List', free nodes.",
            "difficulty": "Medium",
            "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\ntypedef struct Node {\n    int data;\n    struct Node *next;\n} Node;\n\nint main(void) {\n    // Search target in list\n    return 0;\n}\n",
            "language": "c",
            "order_index": 4,
            "test_cases": [{"input_data": "", "expected_output": "Found 15 in List\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Linked List Head Push Engine",
            "description": "Write `void push_head(Node **head, int val)`. Push 10 then 20. Print '20 -> 10 -> NULL', free nodes.",
            "difficulty": "Hard",
            "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\ntypedef struct Node {\n    int data;\n    struct Node *next;\n} Node;\n\n// Write push_head\n\nint main(void) {\n    Node *head = NULL;\n    // Push 10, push 20, print, free\n    return 0;\n}\n",
            "language": "c",
            "order_index": 5,
            "test_cases": [{"input_data": "", "expected_output": "20 -> 10 -> NULL\n", "is_hidden": False, "order_index": 1}]
        },
        {
            "title": "Persistent Linked List Storage Engine",
            "description": "Build 2-node list (101 -> 102). Write node data to file 'list.txt', read back line count, print 'Saved 2 Nodes'.",
            "difficulty": "Challenge",
            "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\ntypedef struct Node {\n    int id;\n    struct Node *next;\n} Node;\n\nint main(void) {\n    // Save list nodes to file, print summary\n    return 0;\n}\n",
            "language": "c",
            "order_index": 6,
            "test_cases": [{"input_data": "", "expected_output": "Saved 2 Nodes\n", "is_hidden": False, "order_index": 1}]
        }
    ]

    m15_quizzes = [
        {
            "question_text": "What field inside a Singly Linked List node enables linking to subsequent elements in memory?",
            "options": ["An index integer", "A self-referential struct pointer to next node (struct Node *next)", "A double array", "A file handle"],
            "correct_answer": "A self-referential struct pointer to next node (struct Node *next)",
            "explanation": "Nodes contain a self-referential pointer storing the RAM memory address of the next list node.",
            "difficulty": "Beginner"
        },
        {
            "question_text": "What does argv[0] contain in C command line argument processing?",
            "options": ["First user argument string", "Executable process path name string", "Total argument count", "Environment variables"],
            "correct_answer": "Executable process path name string",
            "explanation": "argv[0] holds the program executable invocation name string passed by the OS shell.",
            "difficulty": "Beginner"
        }
    ,
        {
            "question_text": "What does a Segmentation Fault signify?",
            "options": ["A syntax error", "The program tried to access a restricted or invalid memory address (e.g., dereferencing NULL)", "The program ran out of disk space", "A math division by zero error"],
            "correct_answer": "The program tried to access a restricted or invalid memory address (e.g., dereferencing NULL)",
            "explanation": "The OS triggers a SegFault when a process violates memory protection rules, killing the process instantly.",
            "difficulty": "Medium"
        },
        {
            "question_text": "Which tool is commonly used on Linux to debug Segmentation Faults and memory leaks?",
            "options": ["gcc", "make", "Valgrind", "nano"],
            "correct_answer": "Valgrind",
            "explanation": "Valgrind instruments the executable, tracking every memory allocation and memory access to pinpoint leaks and illegal reads.",
            "difficulty": "Hard"
        },
        {
            "question_text": "What is gdb?",
            "options": ["A text editor", "The GNU Debugger, used for stepping through code, setting breakpoints, and inspecting variables", "A compiler", "A memory allocator"],
            "correct_answer": "The GNU Debugger, used for stepping through code, setting breakpoints, and inspecting variables",
            "explanation": "GDB is the standard debugger for C, allowing developers to inspect process memory during live execution or post-crash (core dumps).",
            "difficulty": "Medium"
        },
        {
            "question_text": "In a Linked List data structure, what does each 'Node' contain?",
            "options": ["Only data", "Only a pointer", "Data and a pointer to the next Node in the sequence", "A pointer to a file stream"],
            "correct_answer": "Data and a pointer to the next Node in the sequence",
            "explanation": "Linked lists map disjointed heap memory blocks together using pointers, allowing dynamic resizing without contiguous memory.",
            "difficulty": "Hard"
        },
        {
            "question_text": "What is the primary advantage of a Linked List over a standard C Array?",
            "options": ["Linked lists have faster index lookups", "Linked lists use less memory", "Linked lists can easily grow dynamically and insert elements in O(1) time without shifting massive memory blocks", "Linked lists are built-in primitives"],
            "correct_answer": "Linked lists can easily grow dynamically and insert elements in O(1) time without shifting massive memory blocks",
            "explanation": "Arrays require contiguous memory and shifting to insert. Linked lists just rewire two pointers.",
            "difficulty": "Hard"
        },
        {
            "question_text": "What compiler flag is used in gcc to include debugging symbols for gdb?",
            "options": ["-O3", "-g", "-Wall", "-c"],
            "correct_answer": "-g",
            "explanation": "The -g flag embeds source code mappings into the binary so GDB can show human-readable variable names and lines.",
            "difficulty": "Medium"
        },
        {
            "question_text": "What is a 'core dump'?",
            "options": ["Deleting source code", "A snapshot of the program's working memory at the exact moment it crashed, used for post-mortem debugging", "A memory leak", "Clearing the cache"],
            "correct_answer": "A snapshot of the program's working memory at the exact moment it crashed, used for post-mortem debugging",
            "explanation": "Core dumps allow developers to load the crashed state into GDB and inspect exactly why a production server crashed.",
            "difficulty": "Hard"
        },
        {
            "question_text": "When building large projects, what tool automates the compilation of only the files that have changed?",
            "options": ["gcc", "gdb", "make (using a Makefile)", "git"],
            "correct_answer": "make (using a Makefile)",
            "explanation": "Make tracks file modification timestamps and only invokes the compiler on source files that have been updated, saving massive compilation time.",
            "difficulty": "Beginner"
        }
    ]

    # Stage 5 Capstone Project definition for Module 15
    m15_project = {
        "title": "Final Command-Line Task Manager & Record Store",
        "scenario": "You are building a comprehensive command-line Task Manager and persistent record store application in C.",
        "objective": "Combine structures, pointers, dynamic memory allocation (malloc/free), file handling (fopen/fprintf/fclose), and error handling into a robust C application.",
        "requirements": ["Use dynamic memory for storing Task records", "Implement file saving persistence", "Provide modular functions with pointer parameters", "Free all allocated memory"],
        "features": ["Dynamic Record Manager", "File Persistence Engine", "Memory Clean Deallocator"],
        "required_concepts": ["Pointers", "Dynamic Memory", "Structures", "File I/O", "Functions"],
        "architecture": "Modular C application managing dynamic struct memory records with persistent file logging.",
        "guidance": ["Define struct Task { int id; char title[50]; int priority; }", "Save records using fprintf to tasks.txt"],
        "hints": ["Check malloc and fopen returns for NULL"],
        "workflow": "Read task input -> Allocate struct -> Save to file -> Print summary -> Free memory",
        "expected_behavior": "Input: '101 Study_C 1' -> Outputs 'Task Saved: ID=101, Title=Study_C, Priority=1'",
        "evaluation_criteria": "Capstone project cleanly manages dynamic task structures and file persistence.",
        "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\ntypedef struct {\n    int id;\n    char title[50];\n    int priority;\n} Task;\n\nint main(void) {\n    Task *t = (Task *)malloc(sizeof(Task));\n    if (t != NULL && scanf(\"%d %49s %d\", &t->id, t->title, &t->priority) == 3) {\n        FILE *fp = fopen(\"tasks.txt\", \"w\");\n        if (fp != NULL) {\n            fprintf(fp, \"%d %s %d\\n\", t->id, t->title, t->priority);\n            fclose(fp);\n        }\n        printf(\"Task Saved: ID=%d, Title=%s, Priority=%d\\n\", t->id, t->title, t->priority);\n        free(t);\n    }\n    return 0;\n}\n",
        "language": "c",
        "test_cases": [
            {"input_data": "101 Study_C 1\n", "expected_output": "Task Saved: ID=101, Title=Study_C, Priority=1\n", "is_hidden": False, "order_index": 1}
        ]
    }

    modules.append(build_lesson(
        "Practical C, Debugging & DSA Foundations", "c-practical-debugging-dsa",
        m15_what, m15_why, m15_how, m15_syntax, m15_ex_sim, m15_ex_real, m15_out_sim, m15_lbl_sim, m15_out_real, m15_exp_real, m15_mistakes, m15_best, m15_exs, m15_quizzes, m15_project
    ))

    return {
        "title": "C Programming Course",
        "slug": "c-programming",
        "description": "Master C programming from foundational syntax to advanced pointers, dynamic memory management, file handling, and data structures.",
        "category": "Programming Languages",
        "difficulty": "Beginner to Advanced",
        "lang": "c",
        "modules": modules
    }
