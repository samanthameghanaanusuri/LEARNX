import os

output_file = "C:/Users/LENOVO/Desktop/LEARNX/backend/content_cpp.py"
input_files = [
    "C:/Users/LENOVO/Desktop/LEARNX/backend/content_cpp_1.py",
    "C:/Users/LENOVO/Desktop/LEARNX/backend/content_cpp_2.py",
    "C:/Users/LENOVO/Desktop/LEARNX/backend/content_cpp_3.py",
    "C:/Users/LENOVO/Desktop/LEARNX/backend/content_cpp_4.py",
    "C:/Users/LENOVO/Desktop/LEARNX/backend/content_cpp_5.py",
    "C:/Users/LENOVO/Desktop/LEARNX/backend/content_cpp_6.py",
    "C:/Users/LENOVO/Desktop/LEARNX/backend/content_cpp_7.py",
]

course_header = """course_cpp = {
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
        "starter_code": "#include <iostream>\\n\\nint main() {\\n    // Write your game here\\n    return 0;\\n}\\n",
        "solution_code": "#include <iostream>\\n// Solution code\\nint main() { return 0; }\\n",
        "test_cases": []
    },
    {
        "title": "Student Management System",
        "description": "Create a system using arrays/vectors to add, view, and search student records.",
        "difficulty": "Medium",
        "module_index": 6,
        "starter_code": "#include <iostream>\\n#include <vector>\\n\\nint main() {\\n    // Write your system here\\n    return 0;\\n}\\n",
        "solution_code": "#include <iostream>\\n// Solution code\\nint main() { return 0; }\\n",
        "test_cases": []
    },
    {
        "title": "Banking System OOP",
        "description": "Implement a banking system with BankAccount classes, encapsulation, and inheritance for Savings/Checking accounts.",
        "difficulty": "Medium",
        "module_index": 9,
        "starter_code": "#include <iostream>\\n\\nclass BankAccount {\\n    // Implement class\\n};\\n\\nint main() {\\n    return 0;\\n}\\n",
        "solution_code": "#include <iostream>\\n// Solution code\\nint main() { return 0; }\\n",
        "test_cases": []
    },
    {
        "title": "Custom Vector Class",
        "description": "Build your own dynamically resizing vector class using raw pointers, operator overloading, and the Rule of Three.",
        "difficulty": "Hard",
        "module_index": 10,
        "starter_code": "#include <iostream>\\n\\nclass MyVector {\\n    // Implement class\\n};\\n\\nint main() {\\n    return 0;\\n}\\n",
        "solution_code": "#include <iostream>\\n// Solution code\\nint main() { return 0; }\\n",
        "test_cases": []
    },
    {
        "title": "Inventory Manager using STL",
        "description": "Use unordered_map, set, and sort algorithms to manage a store's inventory and perform fast queries.",
        "difficulty": "Hard",
        "module_index": 13,
        "starter_code": "#include <iostream>\\n\\nint main() {\\n    return 0;\\n}\\n",
        "solution_code": "#include <iostream>\\n// Solution code\\nint main() { return 0; }\\n",
        "test_cases": []
    },
    {
        "title": "Capstone: Dungeon Crawler Game Engine",
        "description": "Build a text-based dungeon crawler using polymorphism for Enemies, smart pointers for memory, and STL containers for maps.",
        "difficulty": "Challenge",
        "module_index": 15,
        "starter_code": "#include <iostream>\\n\\nint main() {\\n    return 0;\\n}\\n",
        "solution_code": "#include <iostream>\\n// Solution code\\nint main() { return 0; }\\n",
        "test_cases": []
    }
]

"""

cpp_modules_template = """
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
"""

with open(output_file, 'w', encoding='utf-8') as outfile:
    for f in input_files:
        with open(f, 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())
            outfile.write("\n\n")
    
    outfile.write(course_header)
    outfile.write(cpp_modules_template)

print(f"Successfully built {output_file}")
