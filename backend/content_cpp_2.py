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
