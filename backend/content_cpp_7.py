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
