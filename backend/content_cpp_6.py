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
