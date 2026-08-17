# content_dbms_1.py

course_dbms_title = "Database Management Systems (DBMS) — Beginner to Advanced"
course_dbms_description = "Master database design, SQL querying, transactions, and advanced DBMS concepts from scratch."
course_dbms_language = "sql"
course_dbms_difficulty = "Beginner to Advanced"
course_dbms_slug = "dbms-mastery"

dbms_module_titles_1 = [
    "Database Fundamentals",
    "Database Architecture & Data Models",
    "Entity-Relationship (ER) Model",
    "The Relational Model",
    "SQL Fundamentals"
]

m1_lesson = """# Database Fundamentals

## WHAT IS IT?
A **Database** is an organized collection of structured information or data, typically stored electronically in a computer system. A **Database Management System (DBMS)** is software that interacts with end-users, applications, and the database itself to capture and analyze the data.

## WHY DO WE NEED IT?
Before DBMS, data was stored in simple flat files (like text files or spreadsheets). This caused massive problems: data redundancy (the same data stored multiple times), data inconsistency (updating data in one place but forgetting another), and lack of security. A DBMS solves these problems by providing a centralized, secure, and efficient way to manage data.

## WHERE IS IT USED?
1. **University Management Systems:** Storing student details, courses, enrollments, and grades.
2. **E-commerce Platforms:** Managing product inventory, customer accounts, and order history (e.g., Amazon, Shopify).

## HOW DOES IT WORK?
When a user wants to read or save data, they don't talk to the hard drive directly. Instead, they send a command to the DBMS. The DBMS processes this command, ensures the user is authorized, checks if the data follows all rules (schema), and then securely reads or writes the data to the physical storage.

## TERMINOLOGY
- **Data:** Raw, unorganized facts (e.g., "John", 21).
- **Information:** Processed data that has meaning (e.g., "John is a 21-year-old student").
- **Database (DB):** The actual container where data is stored.
- **DBMS:** The software used to manage the database (e.g., MySQL, Oracle).
- **Schema:** The logical structure or blueprint of the database.
- **Instance:** The actual data contained in the database at a specific moment in time.

## VISUAL / DIAGRAM
```text
[ Users / Apps ]
       |
       v
[ DBMS Software ]  <-- Validates, secures, and optimizes
       |
       v
[ Physical Database (Disk) ]
```

## SYNTAX
Since this is a theoretical concept, there isn't direct code syntax. However, creating a database in a Relational DBMS looks like this:
```sql
CREATE DATABASE university_db;
```

## SIMPLE EXAMPLE
Imagine a simple file system storing student data. You have one file for "Students" and another for "Library". If a student changes their address, you must manually update BOTH files. In a DBMS, the address is stored once, and both the student system and library system access the same, single source of truth.

## LINE-BY-LINE EXPLANATION
- `CREATE DATABASE` tells the DBMS to initialize a new container for data.
- `university_db;` is the name we chose for this container. The semicolon denotes the end of the command.

## REAL-WORLD EXAMPLE
In a banking system, if you transfer $100 from Account A to Account B, the DBMS ensures that either BOTH operations succeed (deduct A, add to B) or NEITHER does. A simple file system cannot guarantee this, which could lead to missing money if the computer crashes halfway through.

## OUTPUT
```text
Query OK, 1 row affected (0.01 sec)
```

## COMMON MISTAKES
- **Confusing DB with DBMS:** A database is the data itself; a DBMS is the software (like MySQL or PostgreSQL) managing it.
- **Using spreadsheets as databases:** Spreadsheets are not meant to handle millions of rows, concurrent users, or strict data relationships.
- **Ignoring Data Independence:** Tightly coupling application code to physical storage structures instead of letting the DBMS handle it.

## BEST PRACTICES
- **Use a DBMS for structured data:** If data is highly relational, always use a DBMS over flat files.
- **Limit access:** Use the DBMS's built-in user roles to ensure applications only have the permissions they strictly need.
- **Regular Backups:** Always utilize the DBMS tools to create automated backups of the data.

## TRY IT YOURSELF
Head to the exercises to test your understanding of database fundamentals, the differences between data and information, and the role of a DBMS.
"""

m2_lesson = """# Database Architecture & Data Models

## WHAT IS IT?
Database architecture refers to how a database is designed and layered to separate the user's view of data from how it is physically stored. A **Data Model** is a collection of concepts used to describe the structure of a database, providing the necessary means to achieve this abstraction.

## WHY DO WE NEED IT?
Without a structured architecture, any change to the physical storage (like moving data to a new hard drive) would require rewriting the application code. Architecture provides **Data Independence**, allowing internal changes without breaking external applications. Data models provide a standard way to think about and design data.

## WHERE IS IT USED?
1. **Corporate Enterprise Systems:** Using the Relational Data Model to handle HR, payroll, and logistics in a highly structured way.
2. **Social Media Networks:** Using Graph or Document Data Models (NoSQL) to handle highly interconnected or flexible data.

## HOW DOES IT WORK?
The standard architecture is the **Three-Schema Architecture**:
1. **Internal Level:** How data is physically stored (bytes on a disk).
2. **Conceptual Level:** The logical structure of the entire database (tables, relationships).
3. **External Level (View Level):** What specific users see (e.g., a student sees only their own grades, not the entire university table).

## TERMINOLOGY
- **Logical Data Independence:** The capacity to change the conceptual schema without having to change external schemas or application programs.
- **Physical Data Independence:** The capacity to change the internal schema without having to change the conceptual schema.
- **Relational Model:** Data represented as tables (relations).
- **Hierarchical Model:** Data represented as a tree structure.
- **NoSQL:** "Not Only SQL", models like Document, Key-Value, Column, or Graph that don't strictly use tables.

## VISUAL / DIAGRAM
```text
      [ User 1 View ]     [ User 2 View ]   <-- External Level
              \                 /
               \               /
            [ Conceptual Schema ]           <-- Conceptual Level (Logic/Tables)
                     |
            [ Internal Schema ]             <-- Internal Level (Disk/Indexes)
```

## SYNTAX
```sql
-- Creating a view (External Level)
CREATE VIEW StudentGrades AS
SELECT student_name, grade FROM Enrollments;
```

## SIMPLE EXAMPLE
Think of a restaurant. 
- **Internal level:** The kitchen, refrigerators, and raw ingredients.
- **Conceptual level:** The master recipe book detailing every dish.
- **External level:** The menu given to the customer, showing only names and prices, not how the food is cooked.

## LINE-BY-LINE EXPLANATION
- `CREATE VIEW StudentGrades AS`: We are creating an external view named `StudentGrades`.
- `SELECT student_name, grade FROM Enrollments;`: We restrict this view to only show names and grades, hiding sensitive data like Social Security Numbers that might exist in the main table.

## REAL-WORLD EXAMPLE
In an online store, the frontend website only needs to see product names, images, and prices (External View). It doesn't know or care that the database stores products across 5 different physical servers using B-tree indexing (Internal Level).

## OUTPUT
```text
View 'StudentGrades' created successfully.
```

## COMMON MISTAKES
- **Mixing levels:** Trying to write application code that references specific hard drive sectors instead of logical tables.
- **Forcing the wrong data model:** Using a strict Relational model for highly unstructured text data, or using NoSQL for complex financial transactions requiring strict ACID compliance.
- **Exposing the conceptual schema:** Giving end-users direct access to the base tables instead of using secure Views.

## BEST PRACTICES
- **Always use Views for external applications:** This adds a layer of security and logical data independence.
- **Choose the right model:** Evaluate if your data is highly structured (Relational) or flexible/hierarchical (Document/NoSQL) before building.
- **Abstract physical details:** Let the Database Administrator (DBA) worry about physical storage; developers should focus on the conceptual level.

## TRY IT YOURSELF
Move to the exercises to identify different architecture levels and data models based on real-world scenarios.
"""

m3_lesson = """# Entity-Relationship (ER) Model

## WHAT IS IT?
The **Entity-Relationship (ER) Model** is a high-level conceptual data model used to define the data elements and relationships for a specified system. It is used to design the logical structure of a database before any code is written, typically represented visually as an **ER Diagram**.

## WHY DO WE NEED IT?
Jumping straight into writing SQL code without a blueprint is a recipe for disaster. The ER model allows database designers, developers, and non-technical stakeholders (like business managers) to communicate and agree on what data needs to be stored and how it relates to each other.

## WHERE IS IT USED?
1. **Software Architecture Planning:** Designing the database schema during the early stages of the Software Development Life Cycle (SDLC).
2. **Business Requirements Gathering:** Mapping out business entities (like Customers, Orders, Products) to ensure all data requirements are captured.

## HOW DOES IT WORK?
The model revolves around three core concepts:
- **Entities:** Real-world objects (e.g., Student, Course).
- **Attributes:** Properties describing the entity (e.g., Student's Name, Age).
- **Relationships:** How entities interact (e.g., a Student ENROLLS in a Course).
You draw these out using specific shapes, forming a comprehensive diagram.

## TERMINOLOGY
- **Entity:** An object that exists and is distinguishable (Noun).
- **Entity Set:** A collection of similar entities (e.g., all students).
- **Attribute:** A property of an entity.
- **Primary Key:** A unique attribute that identifies a specific entity (e.g., Student ID).
- **Cardinality:** The maximum number of relationship instances an entity can participate in (1:1, 1:N, M:N).
- **Weak Entity:** An entity that cannot exist without a parent entity.

## VISUAL / DIAGRAM
```text
[ STUDENT ] --(1)----< ENROLLS >----(N)-- [ COURSE ]
    |                                         |
   (ID)                                     (Code)
  (Name)                                    (Title)
```
- Rectangles = Entities
- Diamonds = Relationships
- Ovals = Attributes (parentheses used here for ASCII representation)

## SYNTAX
ER models are visual, not code. However, they directly translate to SQL schema definitions.
```sql
-- Entity: STUDENT
CREATE TABLE Student (
    ID INT PRIMARY KEY,
    Name VARCHAR(100)
);
```

## SIMPLE EXAMPLE
Consider a Library.
- **Entities:** `BOOK`, `MEMBER`.
- **Relationship:** `BORROWS`.
- **Cardinality:** One `MEMBER` can borrow Many `BOOKS` (1:N). But a specific physical copy of a `BOOK` can only be borrowed by One `MEMBER` at a time.

## LINE-BY-LINE EXPLANATION
- `CREATE TABLE Student (`: We translate the Entity 'STUDENT' into a Table.
- `ID INT PRIMARY KEY,`: We translate the unique attribute into a Primary Key.
- `Name VARCHAR(100)`: We translate a standard attribute into a column.

## REAL-WORLD EXAMPLE
In an Uber-like app:
- Entities: `Rider`, `Driver`, `Trip`.
- Relationships: A `Rider` REQUESTS a `Trip`. A `Driver` ACCEPTS a `Trip`.
- Weak Entity: `Payment` (a payment cannot exist without a `Trip`).

## OUTPUT
```text
ER diagram successfully translated to relational schema.
```

## COMMON MISTAKES
- **Confusing Entities with Attributes:** Making "Phone Number" an entity when it should just be an attribute of "User".
- **Incorrect Cardinality:** Defining a 1:1 relationship between Students and Courses, implying a student can only ever take one course in their entire life.
- **Missing Primary Keys:** Forgetting to define a unique identifier for an entity set.

## BEST PRACTICES
- **Use Nouns for Entities and Verbs for Relationships:** e.g., `CUSTOMER` -> `PLACES` -> `ORDER`.
- **Identify Keys Early:** Always figure out how you will uniquely identify a record.
- **Keep it Conceptual:** Don't worry about foreign keys or specific data types (like VARCHAR) during the ER modeling phase; focus on the business logic.

## TRY IT YOURSELF
Practice mapping out entities, attributes, and relationships in the upcoming exercises.
"""

m4_lesson = """# The Relational Model

## WHAT IS IT?
The **Relational Model** is a method of structuring data using relations, which are mathematical concepts that we commonly understand as two-dimensional **Tables**. It is the foundation of almost all modern Relational Database Management Systems (RDBMS) like MySQL, PostgreSQL, and Oracle.

## WHY DO WE NEED IT?
The Relational Model mathematically guarantees data integrity and provides a standardized, declarative way to query data (using SQL). It eliminates the complex pointer navigation required by older hierarchical models, making database design much simpler and more robust.

## WHERE IS IT USED?
1. **Financial Systems:** Where strict rules, relationships, and data accuracy are absolutely critical.
2. **Content Management Systems:** Like WordPress, which uses relational tables to link Posts, Users, and Comments.

## HOW DOES IT WORK?
Data is stored in tables (Relations). Each table has columns (Attributes) and rows (Tuples). Tables are linked together using special attributes called **Keys**. A Primary Key uniquely identifies a row in its own table, while a Foreign Key points to a Primary Key in another table to establish a relationship.

## TERMINOLOGY
- **Relation:** A Table.
- **Tuple:** A Row (or Record) in a table.
- **Attribute:** A Column (or Field) in a table.
- **Domain:** The set of allowable values for an attribute (e.g., Integer, Date).
- **Primary Key (PK):** An attribute (or set of attributes) that uniquely identifies a tuple.
- **Foreign Key (FK):** An attribute in one table that refers to the Primary Key of another table.
- **Degree:** The number of attributes (columns) in a relation.
- **Cardinality (Relational):** The number of tuples (rows) in a relation.

## VISUAL / DIAGRAM
```text
Relation: STUDENTS (Degree: 3, Cardinality: 2)
+-------+--------+---------+
| S_ID  | Name   | Major_ID|  <-- Attributes
+-------+--------+---------+
| 1     | Alice  | 101     |  <-- Tuple
| 2     | Bob    | 102     |  <-- Tuple
+-------+--------+---------+
   ^                 ^
 Primary Key      Foreign Key pointing to MAJORS table
```

## SYNTAX
```sql
CREATE TABLE Majors (
    Major_ID INT PRIMARY KEY,
    Major_Name VARCHAR(50)
);

CREATE TABLE Students (
    S_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Major_ID INT,
    FOREIGN KEY (Major_ID) REFERENCES Majors(Major_ID)
);
```

## SIMPLE EXAMPLE
Imagine tracking employees and departments. Instead of writing the department name "Human Resources" 500 times for 500 employees (which wastes space and risks typos), you create a `Departments` table. The `Employees` table simply stores a `Dept_ID` (Foreign Key) linking to the `Departments` table.

## LINE-BY-LINE EXPLANATION
- `Major_ID INT PRIMARY KEY,`: Defines `Major_ID` as the unique identifier for the Majors table.
- `Major_ID INT,`: Creates a column in Students to hold the reference.
- `FOREIGN KEY (Major_ID) REFERENCES Majors(Major_ID)`: Enforces referential integrity. The database will physically prevent you from inserting a student with a `Major_ID` that doesn't exist in the Majors table.

## REAL-WORLD EXAMPLE
In an e-commerce database, the `Orders` table contains a `Customer_ID` Foreign Key. If a user deletes their account from the `Customers` table, the Relational Model's integrity rules dictate what happens to their orders (e.g., block the deletion, or cascade and delete the orders too).

## OUTPUT
```text
Tables created. Referential integrity established.
```

## COMMON MISTAKES
- **Orphaned Records:** Trying to delete a parent record (a Major) while child records (Students) still reference it, violating referential integrity.
- **Choosing bad Primary Keys:** Using a person's Name as a Primary Key. Names are not unique. Always use a guaranteed unique ID (like an auto-incrementing integer or UUID).
- **Ignoring Domains:** Storing a date as a simple text string instead of a strict DATE domain, leading to invalid data like "Feb 31st".

## BEST PRACTICES
- **Always enforce Foreign Keys:** Never rely on application code to maintain relationships; let the RDBMS enforce it at the database level.
- **Use surrogate keys:** Use auto-generating, meaningless IDs for Primary Keys rather than natural data (like SSN), which might change or have privacy issues.
- **Ensure Entity Integrity:** Ensure no part of a Primary Key is ever NULL.

## TRY IT YOURSELF
Jump into the exercises to identify Keys, Domains, and relational integrity violations.
"""

m5_lesson = """# SQL Fundamentals

## WHAT IS IT?
**SQL (Structured Query Language)** is the standard language for communicating with Relational Database Management Systems. It is a declarative language, meaning you tell the database *what* you want to achieve, and the database engine figures out *how* to do it most efficiently.

## WHY DO WE NEED IT?
Without SQL, every developer would have to write complex, proprietary code in languages like C++ or Java to traverse hard drives and extract data. SQL provides a unified, highly optimized, and human-readable way to Create, Read, Update, and Delete (CRUD) data across almost all major databases.

## WHERE IS IT USED?
1. **Backend Web Development:** Applications use SQL to store user profiles and retrieve content.
2. **Data Analysis:** Data scientists and analysts write SQL queries to extract insights from massive data warehouses.

## HOW DOES IT WORK?
SQL commands are divided into categories:
- **DDL (Data Definition Language):** Defines structure (`CREATE`, `ALTER`, `DROP`).
- **DML (Data Manipulation Language):** Manipulates data (`INSERT`, `UPDATE`, `DELETE`).
- **DQL (Data Query Language):** Reads data (`SELECT`).
You send these commands to the DBMS, which parses, optimizes, and executes them.

## TERMINOLOGY
- **Query:** A request for data or information from a database table or combination of tables.
- **Keyword:** Reserved words in SQL (like `SELECT`, `FROM`).
- **Statement:** A complete SQL instruction ending with a semicolon (`;`).
- **CRUD:** Create (INSERT), Read (SELECT), Update (UPDATE), Delete (DELETE).

## VISUAL / DIAGRAM
```text
[ Developer ] -- "SELECT * FROM Users;" --> [ DBMS SQL Parser ]
                                                  |
                                            [ Query Optimizer ]
                                                  |
[ Result Set <--- Data ] <----------------- [ Execution Engine ]
```

## SYNTAX
```sql
-- DDL: Create Table
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10, 2)
);

-- DML: Insert Data
INSERT INTO employees (id, name, salary) 
VALUES (1, 'Alice', 75000.00);

-- DML: Update Data
UPDATE employees 
SET salary = 80000.00 
WHERE id = 1;

-- DML: Delete Data
DELETE FROM employees 
WHERE id = 1;
```

## SIMPLE EXAMPLE
Imagine maintaining a digital address book. 
- You buy a new blank book (`CREATE TABLE`). 
- You write down your friend's details (`INSERT`). 
- Your friend moves, so you erase the old address and write a new one (`UPDATE`). 
- You lose touch, so you cross them out entirely (`DELETE`).

## LINE-BY-LINE EXPLANATION
- `CREATE TABLE employees (...)`: Defines a new table structure. `VARCHAR(100)` means a string up to 100 characters. `DECIMAL(10,2)` means a number with 10 total digits, 2 after the decimal.
- `INSERT INTO employees ... VALUES ...`: Adds a new tuple to the relation.
- `UPDATE employees SET salary = ... WHERE id = 1`: Modifies existing data. The `WHERE` clause ensures we *only* update Alice.
- `DELETE FROM employees WHERE id = 1`: Removes the tuple from the relation entirely.

## REAL-WORLD EXAMPLE
When you change your username on a social media platform, the backend executes an `UPDATE` statement. When you delete a tweet, it executes a `DELETE` statement. When you register a new account, it executes an `INSERT` statement.

## OUTPUT
```text
Query OK, 1 row affected (0.01 sec)  -- Typical output after an INSERT/UPDATE/DELETE
```

## COMMON MISTAKES
- **Forgetting the WHERE clause in an UPDATE/DELETE:** Running `UPDATE employees SET salary = 0;` will set EVERY employee's salary to 0! Always include a `WHERE` clause.
- **String quoting errors:** SQL uses single quotes for strings (`'Alice'`), not double quotes (`"Alice"`).
- **Data type mismatches:** Trying to `INSERT` text into an `INT` column.

## BEST PRACTICES
- **Always test UPDATE and DELETE logic with a SELECT first:** Before running `DELETE FROM users WHERE age < 18`, run `SELECT * FROM users WHERE age < 18` to verify exactly what you are about to delete.
- **Use uppercase for keywords:** While SQL is generally case-insensitive, writing `SELECT id FROM table` is much more readable than `select id from table`.
- **Format your queries:** Use line breaks and indentation for complex queries to maintain readability.

## TRY IT YOURSELF
Head to the exercises to practice writing your very first DDL and DML commands.
"""

# EXERCISES
m1_exercises = [
    {
        "title": "DBMS vs File Systems",
        "description": "Which of the following is a key advantage of a DBMS over a traditional flat-file system?\nA) It allows data to be stored as plain text without any structure.\nB) It provides centralized control, reducing data redundancy and inconsistency.\nC) It eliminates the need for computer hardware.\nD) It is always faster for reading a single string of text.",
        "difficulty": "EASY",
        "starter_code": "Type A, B, C, or D here.",
        "solution_code": "B",
        "test_cases": [{"input": "", "expected_output": "B", "is_hidden": False}]
    },
    {
        "title": "Identifying Data vs Information",
        "description": "Consider the following statement: 'The average grade of students in the DBMS course is 85%.'\nIs this considered 'Data' or 'Information'?\nA) Data\nB) Information",
        "difficulty": "EASY+",
        "starter_code": "Type A or B here.",
        "solution_code": "B",
        "test_cases": [{"input": "", "expected_output": "B", "is_hidden": False}]
    },
    {
        "title": "Database Schema vs Instance",
        "description": "If a university database defines a 'Student' table with columns (ID, Name, Age), is this definition part of the Database Schema or the Database Instance?\nA) Schema\nB) Instance",
        "difficulty": "MEDIUM",
        "starter_code": "Type A or B here.",
        "solution_code": "A",
        "test_cases": [{"input": "", "expected_output": "A", "is_hidden": False}]
    },
    {
        "title": "Roles in DBMS",
        "description": "Who is primarily responsible for authorizing access to the database, coordinating its use, and acquiring software/hardware resources?\nA) End User\nB) Database Administrator (DBA)\nC) Application Programmer\nD) System Analyst",
        "difficulty": "MEDIUM+",
        "starter_code": "Type A, B, C, or D here.",
        "solution_code": "B",
        "test_cases": [{"input": "", "expected_output": "B", "is_hidden": False}]
    },
    {
        "title": "Data Redundancy Impact",
        "description": "If a student's address is stored in the 'Library' file and the 'Academic' file in a non-DBMS file system, and the student moves, what specific problem occurs if only the 'Library' file is updated?\nA) Data Isolation\nB) Data Inconsistency\nC) Concurrency Anomaly\nD) Security Violation",
        "difficulty": "HARD",
        "starter_code": "Type A, B, C, or D here.",
        "solution_code": "B",
        "test_cases": [{"input": "", "expected_output": "B", "is_hidden": False}]
    },
    {
        "title": "DBMS Command Recognition",
        "description": "When an application requests to read data, what acts as the intermediary software layer that validates and executes the request?\nA) The Operating System\nB) The Hard Drive Controller\nC) The DBMS Software\nD) The Physical Database",
        "difficulty": "CHALLENGE",
        "starter_code": "Type A, B, C, or D here.",
        "solution_code": "C",
        "test_cases": [{"input": "", "expected_output": "C", "is_hidden": False}]
    }
]

m2_exercises = [
    {
        "title": "Three-Schema Architecture Levels",
        "description": "Which level of the Three-Schema Architecture describes the physical storage structure of the database?\nA) External Level\nB) Conceptual Level\nC) Internal Level",
        "difficulty": "EASY",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "C",
        "test_cases": [{"input": "", "expected_output": "C", "is_hidden": False}]
    },
    {
        "title": "Data Independence Concept",
        "description": "The ability to change the conceptual schema without altering external schemas (Views) is known as:\nA) Physical Data Independence\nB) Logical Data Independence\nC) Isolation Level",
        "difficulty": "EASY+",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "B",
        "test_cases": [{"input": "", "expected_output": "B", "is_hidden": False}]
    },
    {
        "title": "Identifying Data Models",
        "description": "Which data model organizes data into a tree-like structure with parent-child relationships?\nA) Relational Model\nB) Hierarchical Model\nC) Network Model",
        "difficulty": "MEDIUM",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "B",
        "test_cases": [{"input": "", "expected_output": "B", "is_hidden": False}]
    },
    {
        "title": "Views in Architecture",
        "description": "In a hospital database, a receptionist has a UI that only shows patient names and appointment times, hiding medical records. Which architectural level does this represent?\nA) External Level\nB) Conceptual Level\nC) Internal Level",
        "difficulty": "MEDIUM+",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "A",
        "test_cases": [{"input": "", "expected_output": "A", "is_hidden": False}]
    },
    {
        "title": "NoSQL vs Relational",
        "description": "If a social media company needs to store highly interconnected data like 'User A is friends with User B who liked Post C', which specific NoSQL data model is most appropriate?\nA) Document Store\nB) Key-Value Store\nC) Graph Database",
        "difficulty": "HARD",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "C",
        "test_cases": [{"input": "", "expected_output": "C", "is_hidden": False}]
    },
    {
        "title": "Architecture Implications",
        "description": "If the DBA decides to move the database from standard HDDs to SSDs and adds a B-Tree index, which level of data independence ensures the application's SQL queries do not need to be rewritten?\nA) Physical Data Independence\nB) Logical Data Independence",
        "difficulty": "CHALLENGE",
        "starter_code": "Type A or B here.",
        "solution_code": "A",
        "test_cases": [{"input": "", "expected_output": "A", "is_hidden": False}]
    }
]

m3_exercises = [
    {
        "title": "Identifying Entities",
        "description": "In a university database, which of the following is best represented as an Entity?\nA) Age\nB) Student\nC) Date of Birth",
        "difficulty": "EASY",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "B",
        "test_cases": [{"input": "", "expected_output": "B", "is_hidden": False}]
    },
    {
        "title": "Identifying Attributes",
        "description": "In an ER Diagram, what shape is used to represent an Attribute?\nA) Rectangle\nB) Diamond\nC) Oval",
        "difficulty": "EASY+",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "C",
        "test_cases": [{"input": "", "expected_output": "C", "is_hidden": False}]
    },
    {
        "title": "Cardinality Ratios",
        "description": "A single Department can have many Employees, but an Employee can only belong to one Department. What is the cardinality of the 'Employs' relationship from Department to Employee?\nA) 1:1\nB) 1:N\nC) M:N",
        "difficulty": "MEDIUM",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "B",
        "test_cases": [{"input": "", "expected_output": "B", "is_hidden": False}]
    },
    {
        "title": "Primary Keys in ER",
        "description": "An attribute that uniquely identifies an entity instance is called a:\nA) Composite Attribute\nB) Multivalued Attribute\nC) Primary Key Attribute",
        "difficulty": "MEDIUM+",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "C",
        "test_cases": [{"input": "", "expected_output": "C", "is_hidden": False}]
    },
    {
        "title": "Weak Entities",
        "description": "A 'Dependent' entity (like a child) exists only if the 'Employee' entity exists. The 'Dependent' is an example of a:\nA) Strong Entity\nB) Weak Entity\nC) Derived Entity",
        "difficulty": "HARD",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "B",
        "test_cases": [{"input": "", "expected_output": "B", "is_hidden": False}]
    },
    {
        "title": "Derived Attributes",
        "description": "An attribute like 'Age' can be calculated from 'Date of Birth'. In an ER diagram, 'Age' should be modeled as a:\nA) Key Attribute\nB) Multivalued Attribute\nC) Derived Attribute",
        "difficulty": "CHALLENGE",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "C",
        "test_cases": [{"input": "", "expected_output": "C", "is_hidden": False}]
    }
]

m4_exercises = [
    {
        "title": "Relational Terminology: Tuple",
        "description": "In the relational model, a 'Tuple' is equivalent to a:\nA) Table\nB) Column\nC) Row",
        "difficulty": "EASY",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "C",
        "test_cases": [{"input": "", "expected_output": "C", "is_hidden": False}]
    },
    {
        "title": "Relational Terminology: Attribute",
        "description": "In the relational model, an 'Attribute' is equivalent to a:\nA) Row\nB) Column\nC) Table",
        "difficulty": "EASY+",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "B",
        "test_cases": [{"input": "", "expected_output": "B", "is_hidden": False}]
    },
    {
        "title": "Foreign Keys",
        "description": "An attribute in Table A that references the Primary Key of Table B is called a:\nA) Super Key\nB) Foreign Key\nC) Composite Key",
        "difficulty": "MEDIUM",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "B",
        "test_cases": [{"input": "", "expected_output": "B", "is_hidden": False}]
    },
    {
        "title": "Degree and Cardinality",
        "description": "A relation (table) has 5 columns and 100 rows. What is the Degree of the relation?\nA) 5\nB) 100\nC) 500",
        "difficulty": "MEDIUM+",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "A",
        "test_cases": [{"input": "", "expected_output": "A", "is_hidden": False}]
    },
    {
        "title": "Entity Integrity",
        "description": "The Entity Integrity constraint states that:\nA) Foreign keys must match primary keys.\nB) No part of a Primary Key can be NULL.\nC) All columns must have a default value.",
        "difficulty": "HARD",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "B",
        "test_cases": [{"input": "", "expected_output": "B", "is_hidden": False}]
    },
    {
        "title": "Referential Integrity",
        "description": "If you try to insert a row into an 'Orders' table with a Customer_ID that does not exist in the 'Customers' table, which integrity constraint is violated?\nA) Entity Integrity\nB) Domain Integrity\nC) Referential Integrity",
        "difficulty": "CHALLENGE",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "C",
        "test_cases": [{"input": "", "expected_output": "C", "is_hidden": False}]
    }
]

m5_exercises = [
    {
        "title": "SQL Categories: DDL vs DML",
        "description": "Which of the following is a Data Manipulation Language (DML) command?\nA) CREATE TABLE\nB) UPDATE\nC) DROP DATABASE",
        "difficulty": "EASY",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "B",
        "test_cases": [{"input": "", "expected_output": "B", "is_hidden": False}]
    },
    {
        "title": "Writing a CREATE statement",
        "description": "Which statement correctly creates a table named 'cars'?\nA) CREATE TABLE cars (id INT);\nB) MAKE TABLE cars (id INT);\nC) ADD TABLE cars (id INT);",
        "difficulty": "EASY+",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "A",
        "test_cases": [{"input": "", "expected_output": "A", "is_hidden": False}]
    },
    {
        "title": "Writing an INSERT statement",
        "description": "Which syntax is correct for inserting data?\nA) INSERT INTO users (name) VALUES ('Alice');\nB) INSERT users VALUES ('Alice');\nC) ADD TO users (name) VALUES ('Alice');",
        "difficulty": "MEDIUM",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "A",
        "test_cases": [{"input": "", "expected_output": "A", "is_hidden": False}]
    },
    {
        "title": "The Danger of UPDATE",
        "description": "What happens if you run: `UPDATE products SET price = 10;` without a WHERE clause?\nA) It produces a syntax error.\nB) It updates only the first row to 10.\nC) It updates the price of EVERY product to 10.",
        "difficulty": "MEDIUM+",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "C",
        "test_cases": [{"input": "", "expected_output": "C", "is_hidden": False}]
    },
    {
        "title": "String Quoting in SQL",
        "description": "How should a string literal be properly enclosed in standard SQL?\nA) With double quotes: \"John\"\nB) With single quotes: 'John'\nC) With backticks: `John`",
        "difficulty": "HARD",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "B",
        "test_cases": [{"input": "", "expected_output": "B", "is_hidden": False}]
    },
    {
        "title": "Writing a DELETE statement",
        "description": "Which statement correctly deletes the user with ID 5?\nA) DELETE * FROM users WHERE id = 5;\nB) DELETE FROM users WHERE id = 5;\nC) REMOVE FROM users WHERE id = 5;",
        "difficulty": "CHALLENGE",
        "starter_code": "Type A, B, or C here.",
        "solution_code": "B",
        "test_cases": [{"input": "", "expected_output": "B", "is_hidden": False}]
    }
]

# MCQs (10 per module)
m1_quizzes = [
    {
        "question_text": "What is the primary function of a Database Management System (DBMS)?",
        "options": ["To design web interfaces", "To provide an interface between users and the database", "To execute compiled C++ code", "To act as an operating system kernel"],
        "correct_answer": "To provide an interface between users and the database",
        "explanation": "A DBMS serves as middleware that securely handles data operations between end-users (or applications) and the physical database files.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Which of the following is a disadvantage of traditional file processing systems compared to a DBMS?",
        "options": ["Data Redundancy", "Lower hardware costs", "Simplicity for single-user local text files", "Lack of network requirement"],
        "correct_answer": "Data Redundancy",
        "explanation": "File systems often lead to duplicate data stored in multiple files, causing data redundancy and inconsistency. A DBMS minimizes this.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "What is the difference between a Database Schema and a Database Instance?",
        "options": ["Schema is the data; Instance is the DBMS software.", "Schema is the logical design/blueprint; Instance is the actual data at a given moment.", "Instance is the design; Schema is the data.", "There is no difference."],
        "correct_answer": "Schema is the logical design/blueprint; Instance is the actual data at a given moment.",
        "explanation": "The schema rarely changes (e.g., defining columns), whereas the instance changes constantly as users insert/delete data.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "Which property ensures that database operations are processed reliably without interference?",
        "options": ["Data Isolation", "Data Redundancy", "ACID properties managed by DBMS", "File linking"],
        "correct_answer": "ACID properties managed by DBMS",
        "explanation": "A DBMS enforces ACID (Atomicity, Consistency, Isolation, Durability) to ensure reliable transaction processing.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "Who is responsible for authorizing access, defining schemas, and ensuring database performance?",
        "options": ["Application Developer", "Database Administrator (DBA)", "End User", "Network Engineer"],
        "correct_answer": "Database Administrator (DBA)",
        "explanation": "The DBA is the specialized role tasked with managing the overall health, security, and performance of the DBMS.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Raw, unorganized facts are known as ________, while processed and meaningful facts are known as ________.",
        "options": ["Information, Data", "Data, Information", "Schema, Instance", "Instance, Schema"],
        "correct_answer": "Data, Information",
        "explanation": "Data refers to raw facts (e.g., '100'). Information is processed data with context (e.g., 'Account balance is $100').",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Which of the following is NOT a typical function of a modern DBMS?",
        "options": ["Concurrency control", "Data security management", "Compiling high-level languages to machine code", "Backup and recovery management"],
        "correct_answer": "Compiling high-level languages to machine code",
        "explanation": "Compiling code is the job of a compiler, not a DBMS. A DBMS handles data concurrency, security, and recovery.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What problem occurs when the same piece of data is updated in one file but not in another?",
        "options": ["Data Isolation", "Data Independence", "Data Inconsistency", "Data Security"],
        "correct_answer": "Data Inconsistency",
        "explanation": "Data inconsistency happens when duplicated data (redundancy) goes out of sync because one copy was updated while another was missed.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "In the context of DBMS, what does CRUD stand for?",
        "options": ["Compile, Read, Update, Delete", "Create, Read, Update, Delete", "Create, Run, Upload, Download", "Copy, Read, Undo, Drop"],
        "correct_answer": "Create, Read, Update, Delete",
        "explanation": "CRUD represents the four fundamental operations of persistent storage: Create (Insert), Read (Select), Update, Delete.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Why might a company choose NOT to use a full DBMS and stick to flat files?",
        "options": ["They need concurrent multi-user access.", "They require strict security and user roles.", "The application is extremely simple, embedded, and strictly single-user.", "They want to reduce data redundancy."],
        "correct_answer": "The application is extremely simple, embedded, and strictly single-user.",
        "explanation": "A DBMS adds overhead (CPU, memory, cost). For trivial, isolated, single-user tasks (like storing simple local app config), flat files are preferred.",
        "difficulty": "Advanced"
    }
]

m2_quizzes = [
    {
        "question_text": "What is the primary purpose of the Three-Schema Architecture?",
        "options": ["To encrypt all data.", "To achieve Data Independence.", "To create three backups of the database.", "To distribute data across three servers."],
        "correct_answer": "To achieve Data Independence.",
        "explanation": "It separates the user applications (external) from the physical database (internal), ensuring changes to one don't break the other.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "Which level of architecture describes exactly how data is physically stored on the disk?",
        "options": ["External Level", "Conceptual Level", "Internal Level", "Logical Level"],
        "correct_answer": "Internal Level",
        "explanation": "The internal schema describes the physical storage structure, including file formats, indexing techniques, and paths.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Which level hides the physical storage details and focuses on logical tables, entities, and relationships?",
        "options": ["Internal Level", "External Level", "Conceptual Level", "Physical Level"],
        "correct_answer": "Conceptual Level",
        "explanation": "The conceptual schema represents the global logical structure of the database (tables, constraints) without physical details.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "What is an External View?",
        "options": ["A monitor used by the DBA.", "A specific user's customized perspective of the database, hiding irrelevant data.", "The physical file system visible to the OS.", "A complete replica of the conceptual schema."],
        "correct_answer": "A specific user's customized perspective of the database, hiding irrelevant data.",
        "explanation": "External views restrict what different user groups can see, providing security and simplifying data access for specific tasks.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "If a DBA changes a B-Tree index to a Hash index to improve speed, but application queries do not need to be rewritten, this is an example of:",
        "options": ["Logical Data Independence", "Physical Data Independence", "Schema Redundancy", "Internal Dependence"],
        "correct_answer": "Physical Data Independence",
        "explanation": "Physical data independence means changes to the internal/physical level do not affect the conceptual or external levels.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "If you add a new column 'DateOfBirth' to the 'Students' table, but existing applications querying only 'Name' and 'Grade' do not break, this is an example of:",
        "options": ["Logical Data Independence", "Physical Data Independence", "Conceptual Dependence", "View Constraints"],
        "correct_answer": "Logical Data Independence",
        "explanation": "Logical data independence ensures that adding new logical structures (like columns) to the conceptual schema doesn't break existing external views.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "Which data model represents data in a rigid parent-child tree structure?",
        "options": ["Relational Model", "Network Model", "Hierarchical Model", "Object-Oriented Model"],
        "correct_answer": "Hierarchical Model",
        "explanation": "In a hierarchical model, data is organized in a tree structure where each child record has exactly one parent.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Which data model represents data as a collection of tables (relations)?",
        "options": ["Relational Model", "Document Model", "Hierarchical Model", "Graph Model"],
        "correct_answer": "Relational Model",
        "explanation": "The relational model uses two-dimensional tables consisting of rows and columns to structure data.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Why might a modern application choose a NoSQL Document model over a Relational model?",
        "options": ["Because NoSQL always supports strict ACID transactions better than SQL.", "Because NoSQL requires rigid schemas defined upfront.", "Because NoSQL handles unstructured, schema-less data like JSON flexibly.", "Because Relational models cannot store text."],
        "correct_answer": "Because NoSQL handles unstructured, schema-less data like JSON flexibly.",
        "explanation": "Document models (like MongoDB) do not enforce rigid table structures, making them highly flexible for rapidly changing application requirements.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "In the Three-Schema Architecture, mapping between the Conceptual and Internal levels provides which specific capability?",
        "options": ["It translates SQL into HTML.", "It allows the DBMS to know exactly where a logical table's rows are physically stored on disk.", "It prevents unauthorized users from logging in.", "It formats the output for the user's screen."],
        "correct_answer": "It allows the DBMS to know exactly where a logical table's rows are physically stored on disk.",
        "explanation": "The conceptual/internal mapping tells the DBMS how to translate logical table queries into physical file access operations.",
        "difficulty": "Intermediate"
    }
]

m3_quizzes = [
    {
        "question_text": "In an ER Diagram, what does a rectangle represent?",
        "options": ["Relationship", "Attribute", "Entity", "Primary Key"],
        "correct_answer": "Entity",
        "explanation": "In standard Chen notation for ER diagrams, rectangles represent Entities.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "In an ER Diagram, what does a diamond represent?",
        "options": ["Relationship", "Attribute", "Entity", "Weak Entity"],
        "correct_answer": "Relationship",
        "explanation": "Diamonds represent relationships that connect entities together (e.g., ENROLLS, MANAGES).",
        "difficulty": "Beginner"
    },
    {
        "question_text": "What is an attribute that can be broken down into smaller, meaningful subparts (like an Address broken into Street, City, Zip)?",
        "options": ["Simple Attribute", "Derived Attribute", "Composite Attribute", "Multivalued Attribute"],
        "correct_answer": "Composite Attribute",
        "explanation": "Composite attributes are composed of multiple simple attributes.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "How is a Multivalued Attribute (like 'Phone Numbers' for a person who has multiple phones) represented in an ER diagram?",
        "options": ["Dashed oval", "Double oval", "Underlined oval", "Diamond"],
        "correct_answer": "Double oval",
        "explanation": "A double oval indicates that an entity can have more than one value for that attribute.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "An attribute whose value is calculated from another attribute (like 'Age' calculated from 'Date of Birth') is called:",
        "options": ["Key Attribute", "Multivalued Attribute", "Composite Attribute", "Derived Attribute"],
        "correct_answer": "Derived Attribute",
        "explanation": "Derived attributes are not physically stored; their values are generated dynamically. They are represented by dashed ovals.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What is Cardinality in the context of ER models?",
        "options": ["The total number of attributes an entity has.", "The maximum number of relationship instances an entity can participate in.", "The number of primary keys in a table.", "The data type of an attribute."],
        "correct_answer": "The maximum number of relationship instances an entity can participate in.",
        "explanation": "Cardinality defines rules like '1 to 1', '1 to Many', or 'Many to Many' between entities.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "If a Manager can manage only one Department, and a Department has only one Manager, what is the cardinality ratio?",
        "options": ["1:N (One-to-Many)", "M:N (Many-to-Many)", "1:1 (One-to-One)", "N:1 (Many-to-One)"],
        "correct_answer": "1:1 (One-to-One)",
        "explanation": "Since the restriction applies strictly in both directions, it is a 1:1 relationship.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "What defines a 'Weak Entity'?",
        "options": ["An entity with very few attributes.", "An entity that does not have its own primary key and depends on another entity to exist.", "An entity containing invalid data.", "An entity with a 1:1 relationship."],
        "correct_answer": "An entity that does not have its own primary key and depends on another entity to exist.",
        "explanation": "A weak entity requires an identifying relationship with a strong 'owner' entity (e.g., an Employee's Dependents).",
        "difficulty": "Advanced"
    },
    {
        "question_text": "Which attribute MUST exist in every strong entity?",
        "options": ["Derived Attribute", "Composite Attribute", "Key Attribute (Primary Key)", "Multivalued Attribute"],
        "correct_answer": "Key Attribute (Primary Key)",
        "explanation": "Every strong entity must have at least one key attribute that uniquely identifies its instances.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "In ER modeling, what is an 'Entity Set'?",
        "options": ["A collection of attributes.", "A collection of relationships.", "A collection of entities of the same type.", "A mathematical set of primary keys."],
        "correct_answer": "A collection of entities of the same type.",
        "explanation": "While 'Employee' is the concept/type, the 'Entity Set' refers to the collection of all actual employee instances in the database.",
        "difficulty": "Beginner"
    }
]

m4_quizzes = [
    {
        "question_text": "In the relational model, a 'Relation' is mathematically equivalent to a:",
        "options": ["Row", "Column", "Table", "Query"],
        "correct_answer": "Table",
        "explanation": "A relation is a two-dimensional table consisting of rows and columns.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "In the relational model, a 'Tuple' is mathematically equivalent to a:",
        "options": ["Table", "Row (Record)", "Column (Field)", "Index"],
        "correct_answer": "Row (Record)",
        "explanation": "A tuple represents a single distinct entity instance (a row) within a relation.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "What does the 'Degree' of a relation refer to?",
        "options": ["The number of rows/tuples.", "The number of columns/attributes.", "The number of primary keys.", "The size of the table in bytes."],
        "correct_answer": "The number of columns/attributes.",
        "explanation": "Degree is the number of attributes in a relation, which defines its structure.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What does the 'Cardinality' of a relation refer to? (Note: Context is relational model, not ER modeling)",
        "options": ["The number of columns.", "The number of primary keys.", "The number of rows/tuples.", "The number of foreign keys."],
        "correct_answer": "The number of rows/tuples.",
        "explanation": "In relational algebra/calculus, cardinality refers to the number of tuples in a relation.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "Which constraint ensures that no part of a Primary Key can ever be NULL?",
        "options": ["Referential Integrity", "Domain Integrity", "Entity Integrity", "Check Constraint"],
        "correct_answer": "Entity Integrity",
        "explanation": "Entity integrity dictates that primary keys must be valid and non-null to uniquely identify a tuple.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "Which constraint ensures that a Foreign Key value must match an existing Primary Key value in the referenced table, or be NULL?",
        "options": ["Entity Integrity", "Referential Integrity", "Domain Integrity", "Key Integrity"],
        "correct_answer": "Referential Integrity",
        "explanation": "Referential integrity guarantees that relationships between tables remain valid and consistent.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "What is a 'Candidate Key'?",
        "options": ["Any column in a table.", "An attribute or set of attributes that can uniquely identify a tuple, from which the Primary Key is chosen.", "A key that links two tables together.", "A key that allows NULL values."],
        "correct_answer": "An attribute or set of attributes that can uniquely identify a tuple, from which the Primary Key is chosen.",
        "explanation": "A table can have multiple candidate keys (e.g., SSN and EmployeeID). The designer selects one to be the actual Primary Key.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What is a 'Composite Key'?",
        "options": ["A key that uses numbers and letters.", "A primary key that consists of two or more attributes working together.", "A foreign key that points to multiple tables.", "A key that is generated automatically by the DBMS."],
        "correct_answer": "A primary key that consists of two or more attributes working together.",
        "explanation": "When a single attribute is not enough to guarantee uniqueness (like OrderID and ProductID in an OrderDetails table), multiple attributes combine to form a composite key.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What does a 'Domain' represent in the relational model?",
        "options": ["The server IP address.", "The maximum number of rows a table can hold.", "The set of allowable, valid values for a particular attribute.", "The relationship between two tables."],
        "correct_answer": "The set of allowable, valid values for a particular attribute.",
        "explanation": "A domain dictates the data type and constraints of an attribute (e.g., an Age domain must be integers between 0 and 150).",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Is the order of tuples (rows) mathematically significant in a pure relation?",
        "options": ["Yes, rows must be ordered alphabetically.", "Yes, rows must be ordered by the primary key.", "No, a relation is an unordered set of tuples.", "No, but columns must be strictly ordered."],
        "correct_answer": "No, a relation is an unordered set of tuples.",
        "explanation": "In set theory and the pure relational model, a relation is a set, and sets have no inherent order.",
        "difficulty": "Advanced"
    }
]

m5_quizzes = [
    {
        "question_text": "Which SQL command is used to add new rows of data into a table?",
        "options": ["ADD DATA", "INSERT INTO", "UPDATE", "CREATE ROW"],
        "correct_answer": "INSERT INTO",
        "explanation": "INSERT INTO is the standard DML command used to add new tuples to a relation.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Which SQL keyword is used to modify existing data in a table?",
        "options": ["MODIFY", "CHANGE", "UPDATE", "ALTER"],
        "correct_answer": "UPDATE",
        "explanation": "UPDATE modifies existing rows. ALTER is used to modify the structure of the table itself (DDL).",
        "difficulty": "Beginner"
    },
    {
        "question_text": "Why is the WHERE clause critical when executing an UPDATE or DELETE statement?",
        "options": ["Because the database will crash without it.", "Because without it, the command will apply to EVERY row in the table.", "Because it specifies which columns to show.", "Because it sorts the output."],
        "correct_answer": "Because without it, the command will apply to EVERY row in the table.",
        "explanation": "If you omit WHERE, the DBMS assumes you want to update or delete all tuples.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "Which of the following belongs to Data Definition Language (DDL)?",
        "options": ["SELECT", "INSERT", "CREATE", "DELETE"],
        "correct_answer": "CREATE",
        "explanation": "DDL commands (CREATE, ALTER, DROP) define database structure, whereas DML commands manipulate the data inside.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "How do you define a string value in a standard SQL query?",
        "options": ["With double quotes: \"string\"", "With single quotes: 'string'", "With backticks: `string`", "With brackets: [string]"],
        "correct_answer": "With single quotes: 'string'",
        "explanation": "SQL standard dictates single quotes for string literals. Double quotes are often used for identifiers (like table names with spaces).",
        "difficulty": "Beginner"
    },
    {
        "question_text": "What does the SQL statement 'DROP TABLE users;' do?",
        "options": ["Deletes all data in the users table but keeps the structure.", "Deletes the users table entirely, including its structure and all data.", "Hides the users table from other users.", "Renames the users table."],
        "correct_answer": "Deletes the users table entirely, including its structure and all data.",
        "explanation": "DROP is a destructive DDL command that removes the entire object from the schema.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What is the difference between DELETE and DROP?",
        "options": ["DELETE removes data (rows); DROP removes the structural object (table).", "DROP removes data; DELETE removes the table.", "They are exactly the same.", "DELETE is for columns; DROP is for rows."],
        "correct_answer": "DELETE removes data (rows); DROP removes the structural object (table).",
        "explanation": "DELETE is a DML command that empties rows. DROP is a DDL command that destroys the table schema.",
        "difficulty": "Advanced"
    },
    {
        "question_text": "Which SQL command is used to retrieve data from a database?",
        "options": ["FETCH", "GET", "SELECT", "PULL"],
        "correct_answer": "SELECT",
        "explanation": "SELECT is the fundamental Data Query Language (DQL) command used to read data.",
        "difficulty": "Beginner"
    },
    {
        "question_text": "If a column is defined as VARCHAR(50), what does the 50 signify?",
        "options": ["The table can have 50 rows.", "The string must be exactly 50 characters long.", "The string can be variable length, up to a maximum of 50 characters.", "The string is padded with spaces until it hits 50 bytes."],
        "correct_answer": "The string can be variable length, up to a maximum of 50 characters.",
        "explanation": "VARCHAR stands for Variable Character. It stores only what is needed, up to the defined limit.",
        "difficulty": "Intermediate"
    },
    {
        "question_text": "What is the purpose of the semicolon (;) in SQL?",
        "options": ["It is a wildcard character.", "It acts as a statement terminator, signaling the end of a command.", "It represents a comment.", "It separates columns in an INSERT statement."],
        "correct_answer": "It acts as a statement terminator, signaling the end of a command.",
        "explanation": "The semicolon tells the SQL parser that the current statement is complete and can be executed.",
        "difficulty": "Beginner"
    }
]

dbms_lessons_1 = [m1_lesson, m2_lesson, m3_lesson, m4_lesson, m5_lesson]
dbms_exercises_1 = [m1_exercises, m2_exercises, m3_exercises, m4_exercises, m5_exercises]
dbms_quizzes_1 = [m1_quizzes, m2_quizzes, m3_quizzes, m4_quizzes, m5_quizzes]
