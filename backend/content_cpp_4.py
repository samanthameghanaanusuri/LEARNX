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
