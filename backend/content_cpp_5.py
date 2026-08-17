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
