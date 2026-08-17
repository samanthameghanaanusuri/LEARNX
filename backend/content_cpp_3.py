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
