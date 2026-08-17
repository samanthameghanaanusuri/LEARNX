# content_dbms_3.py

dbms_module_titles_3 = [
    "Indexing",
    "Database Internals",
    "Views, Procedures & Advanced Features",
    "Database Security & Performance",
    "DBMS CAPSTONE"
]

m11_lesson = """# Indexing

## WHAT IS IT?
An **Index** is a special data structure that improves the speed of data retrieval operations on a database table at the cost of additional storage space and slower writes. It functions exactly like the index at the back of a textbook.

## WHY DO WE NEED IT?
Without an index, the DBMS must perform a **Full Table Scan**, reading every single row in the table from top to bottom to find a match. If a table has 10 million rows, finding one specific user could take seconds. With an index, it takes milliseconds.

## WHERE IS IT USED?
1. **Search Engines:** Rapidly retrieving web pages that contain specific keywords.
2. **E-commerce Catalogs:** Finding products by category or price instantly without scanning the whole database.

## HOW DOES IT WORK?
When you create an index on a column (e.g., `user_id`), the DBMS creates a separate data structure (usually a **B-Tree**) containing the sorted values of `user_id` and a pointer to the physical location of the full row on the disk. When querying, the DBMS searches the much smaller, sorted B-Tree first.

## TERMINOLOGY
- **B-Tree (Balanced Tree):** The default data structure for indexes. It stays balanced so searching takes O(log N) time.
- **Hash Index:** Used for exact matches (O(1) time) but cannot handle range queries (`<`, `>`).
- **Clustered Index:** Defines the physical sorting order of the table itself (usually the Primary Key). A table can only have one.
- **Non-Clustered Index:** A separate structure pointing back to the data rows. A table can have many.
- **Composite Index:** An index on multiple columns simultaneously (e.g., `first_name, last_name`).

## VISUAL / DIAGRAM
```text
Full Table Scan vs Index Lookup

Table (Unsorted by Name)           Index on Name (Sorted)
+----+-------+-------+             +-------+---------+
| ID | Name  | Age   |             | Name  | Pointer |
+----+-------+-------+             +-------+---------+
| 1  | Zack  | 30    |             | Alice | -> row 2|
| 2  | Alice | 25    |             | Bob   | -> row 3|
| 3  | Bob   | 40    |             | Zack  | -> row 1|
+----+-------+-------+             +-------+---------+
```

## SYNTAX
```sql
CREATE INDEX idx_user_email ON users(email);

-- Composite Index
CREATE INDEX idx_last_first ON users(last_name, first_name);
```

## SIMPLE EXAMPLE
Imagine a `users` table with 1 million rows. 
```sql
SELECT * FROM users WHERE email = 'test@example.com';
```
If `email` is not indexed, the database checks 1 million rows. If we run `CREATE INDEX idx_email ON users(email);`, the database searches the B-Tree, finds the email in ~20 steps (Log N), and fetches the exact row.

## LINE-BY-LINE EXPLANATION
- `CREATE INDEX idx_user_email`: We declare a new index and name it logically (usually `idx_table_column`).
- `ON users(email)`: We specify the table and the column we want to build the B-Tree for.

## REAL-WORLD EXAMPLE
In a massive banking app, `account_number` is the Primary Key (Clustered Index). However, customers often log in using their `phone_number`. The DBA will create a Non-Clustered Index on `phone_number` to ensure logins are instant, rather than forcing a full table scan every time someone logs in.

## OUTPUT
```text
Index 'idx_user_email' created successfully.
```

## COMMON MISTAKES
- **Over-indexing:** Creating an index on every single column. Indexes consume disk space and slow down `INSERT`, `UPDATE`, and `DELETE` operations because the index must be updated every time the data changes.
- **Indexing low cardinality columns:** Creating an index on a boolean column (e.g., `is_active`). Since there are only two possible values, an index doesn't help the optimizer narrow down the search enough to be useful.
- **Ignoring Left-Most Prefix Rule:** If you have a composite index on `(last_name, first_name)`, querying `WHERE first_name = 'John'` will NOT use the index. It only works if you query from left to right.

## BEST PRACTICES
- **Index foreign keys:** They are frequently used in `JOIN` conditions.
- **Index columns used in WHERE, ORDER BY, and GROUP BY clauses:** These benefit the most from sorted data structures.
- **Use EXPLAIN:** Always run `EXPLAIN SELECT ...` to verify if the database is actually using your index or falling back to a full table scan.

## TRY IT YOURSELF
Jump to the exercises to identify when to use an index, when to avoid them, and how to create composite indexes.
"""

m12_lesson = """# Database Internals

## WHAT IS IT?
**Database Internals** refer to the underlying architecture and mechanisms that power a DBMS. It's the "engine under the hood" that translates your SQL text into physical disk reads and writes.

## WHY DO WE NEED IT?
While you can drive a car without knowing how an engine works, you cannot tune it for high performance. Understanding internals allows developers to write optimized queries, diagnose slow performance, and understand why certain operations (like massive JOINs) are failing or consuming too much RAM.

## WHERE IS IT USED?
1. **Database Administration (DBA):** Tuning memory buffers and cache sizes for enterprise databases.
2. **Backend Engineering:** Analyzing query execution plans to optimize a slow API endpoint.

## HOW DOES IT WORK?
When you send a SQL query:
1. **Parser:** Checks syntax and semantics (Is the SQL valid? Does the table exist?).
2. **Query Optimizer:** Analyzes multiple ways to execute the query and picks the cheapest one (Cost-Based Optimization).
3. **Execution Engine:** Executes the chosen plan, requesting data from the Storage Engine.
4. **Storage Engine:** Reads/writes data to memory buffers and disk pages.

## TERMINOLOGY
- **Page / Block:** The smallest unit of data transfer between disk and memory (often 8KB). Databases read pages, not individual rows.
- **Buffer Pool / Cache:** RAM allocated to hold frequently accessed pages to avoid slow disk I/O.
- **Execution Plan:** The step-by-step tree of operations the database will perform to get your data.
- **Cost-Based Optimizer (CBO):** Estimates the "cost" (CPU + Disk I/O) of different execution plans based on table statistics.

## VISUAL / DIAGRAM
```text
SQL Query --> [ Parser ] --> [ Optimizer (CBO) ] --> [ Execution Plan ]
                                                            |
                                                    [ Execution Engine ]
                                                            |
                     [ Memory / Buffer Pool ] <----> [ Storage Engine ] <--> [ DISK ]
```

## SYNTAX
To see the internal execution plan, use the `EXPLAIN` keyword.
```sql
EXPLAIN SELECT name FROM employees WHERE salary > 100000;
```

## SIMPLE EXAMPLE
If you query `SELECT * FROM users WHERE id = 10;`, the Parser checks the spelling. The Optimizer sees `id` is a Primary Key and decides to use an Index Lookup (cost: 1). The Execution Engine asks the Storage Engine for the row. The Storage Engine checks if the page containing row 10 is in the RAM (Buffer Pool). If yes, it returns it instantly. If no, it reads the 8KB page from the hard drive into RAM, then returns the row.

## LINE-BY-LINE EXPLANATION
- `EXPLAIN`: A special command that intercepts the query. Instead of running it and returning data, it asks the Optimizer to reveal its chosen Execution Plan.

## REAL-WORLD EXAMPLE
A developer notices a report query takes 5 minutes. They run `EXPLAIN` and see a `Nested Loop Join` doing a `Sequential Scan` (Full Table Scan) on a 10-million-row table. They realize they forgot an index on the join column. They add the index, the Optimizer switches to a `Hash Join` with an `Index Scan`, and the query drops to 2 seconds.

## OUTPUT
```text
                                QUERY PLAN
--------------------------------------------------------------------------
 Index Scan using employees_pkey on employees  (cost=0.29..8.31 rows=1)
   Index Cond: (id = 10)
```

## COMMON MISTAKES
- **Ignoring Disk I/O:** Forgetting that reading from a physical Hard Drive is 100,000x slower than reading from RAM. Bad queries force the database to constantly read from disk.
- **Stale Statistics:** The Optimizer relies on statistics (e.g., "how many rows are in this table?"). If stats are outdated, the optimizer might choose a terrible execution plan. (Fix: run `ANALYZE`).
- **SELECT * abuse:** Pulling columns you don't need forces the database to read more physical pages from the disk, filling up the Buffer Pool with useless data and evicting good data.

## BEST PRACTICES
- **Learn to read EXPLAIN outputs:** Understand the difference between a `Seq Scan` (Full scan) and an `Index Scan`.
- **Maximize Cache Hits:** Write queries that allow the database to operate mostly in RAM (Buffer Pool) rather than constantly hitting the disk.
- **Optimize for Pages:** Remember that databases fetch entire pages (8KB). Keeping rows small (avoiding massive VARCHARs when not needed) fits more rows into a single page, speeding up scans.

## TRY IT YOURSELF
Proceed to the exercises to analyze execution plans and optimize slow queries.
"""

m13_lesson = """# Views, Procedures & Advanced Features

## WHAT IS IT?
Advanced DBMS features allow you to store logic inside the database itself. 
- **Views:** Virtual tables based on the result of an SQL statement.
- **Stored Procedures & Functions:** Reusable blocks of SQL code (with variables, loops, and logic) saved in the database.
- **Triggers:** Special procedures that automatically execute (fire) when an event (INSERT, UPDATE, DELETE) occurs on a table.

## WHY DO WE NEED IT?
Moving logic into the database can improve performance (reducing network traffic), enhance security (giving users access to a View instead of the base table), and ensure data consistency (using Triggers to enforce complex business rules that constraints cannot handle).

## WHERE IS IT USED?
1. **Reporting:** Creating complex Views so analysts can query simple virtual tables instead of writing 10-way JOINs.
2. **Audit Logging:** Using a Trigger to automatically write a record to an `audit_log` table every time a user changes their password.

## HOW DOES IT WORK?
- A **View** stores the *query*, not the data. When you `SELECT` from a view, the DBMS runs the underlying query on the fly.
- A **Stored Procedure** is compiled and stored. You call it via the application. It can perform multiple operations and handle transactions internally.
- A **Trigger** is attached to a specific table and listens for events (`BEFORE INSERT`, `AFTER UPDATE`, etc.).

## TERMINOLOGY
- **Virtual Table:** Another name for a View.
- **Materialized View:** A view that actually physically stores the result data on disk for faster read performance (needs refreshing).
- **PL/SQL or T-SQL:** Procedural extensions to standard SQL used to write stored procedures (allowing IF statements, loops, etc.).

## VISUAL / DIAGRAM
```text
[ Application ] -- "CALL ProcessPayroll();" --> [ Stored Procedure ]
                                                     |
                                                Update Balances
                                                Log to Audit Table
                                                Commit Transaction
```

## SYNTAX
```sql
-- Creating a View
CREATE VIEW active_users AS
SELECT id, username FROM users WHERE status = 'active';

-- Using the View
SELECT * FROM active_users;
```

## SIMPLE EXAMPLE
Imagine you have an `Employees` table with sensitive `salary` data. You want to give the HR intern access to employee names and departments, but NOT salaries. You create a View that excludes the salary column, and grant the intern permission to query *only* the View, not the base table.

## LINE-BY-LINE EXPLANATION
- `CREATE VIEW active_users AS`: Defines the name of the virtual table.
- `SELECT id, username ...`: The underlying logic. The `salary` and `password_hash` columns are explicitly left out.
- `SELECT * FROM active_users;`: You query it exactly like a normal table.

## REAL-WORLD EXAMPLE
**Trigger Example:** E-commerce inventory. When an order is placed (`INSERT INTO Orders`), an `AFTER INSERT` trigger automatically fires and runs `UPDATE Products SET stock = stock - 1`. This guarantees the stock is always decremented, even if the backend application forgets to do it.

## OUTPUT
```text
View 'active_users' created successfully.
```

## COMMON MISTAKES
- **Overusing Triggers:** Triggers run invisibly in the background. If a developer doesn't know a trigger exists, they might spend days debugging why a record is mysteriously updating itself.
- **Business Logic in DB vs App:** Putting *too much* logic in Stored Procedures makes the database a bottleneck and makes version control / testing much harder.
- **Updating Views:** Standard views are generally read-only. Trying to `UPDATE` a view spanning multiple tables will usually fail.

## BEST PRACTICES
- **Use Views for security and simplicity:** Hide complexity and sensitive data from end-users and reporting tools.
- **Use Stored Procedures for heavy data processing:** If a task requires reading 1 million rows, calculating a sum, and writing 1 row, do it in a Stored Procedure so you don't transfer 1 million rows over the network to the application layer.
- **Keep Triggers simple:** Use them for auditing and strict data integrity, not complex business workflows.

## TRY IT YOURSELF
Jump into the exercises to write Views and conceptualize Stored Procedures.
"""

m14_lesson = """# Database Security & Performance

## WHAT IS IT?
**Database Security** involves protecting the database against unauthorized access, malicious attacks, and data loss. **Performance Tuning** involves optimizing the database schema, queries, and server configuration to serve requests as fast as possible.

## WHY DO WE NEED IT?
Databases hold a company's most valuable asset: data. A security breach can destroy a business. Furthermore, a secure database that takes 30 seconds to load a webpage is useless; performance ensures the application remains usable under heavy load.

## WHERE IS IT USED?
1. **Compliance:** Adhering to GDPR or HIPAA by encrypting sensitive columns and auditing access.
2. **Scaling:** Tuning database memory and query plans during a massive spike in user traffic (e.g., Black Friday sales).

## HOW DOES IT WORK?
Security is layered:
- **Authentication:** Verifying WHO you are (username/password).
- **Authorization:** Verifying WHAT you can do (Roles and Privileges).
- **Injection Prevention:** Ensuring user input is never treated as executable code.

Performance is layered:
- **Schema Optimization:** Normalization, choosing correct data types.
- **Index Optimization:** Adding missing indexes, dropping unused ones.
- **Query Optimization:** Rewriting SQL to avoid full table scans.

## TERMINOLOGY
- **SQL Injection (SQLi):** A cyber attack where malicious SQL statements are inserted into entry fields for execution.
- **Parameterized Queries:** A defensive coding technique where user input is treated strictly as data, never as executable code.
- **Principle of Least Privilege:** A user or application should only have the bare minimum permissions necessary to perform its job.
- **Role-Based Access Control (RBAC):** Grouping privileges into a "Role" (e.g., `Analyst_Role`) and assigning users to the Role.

## VISUAL / DIAGRAM
```text
The SQL Injection Attack:
App expects: SELECT * FROM users WHERE name = '[input]'
Attacker inputs: ' OR '1'='1
Resulting Query: SELECT * FROM users WHERE name = '' OR '1'='1'
(Since 1=1 is always true, the database returns EVERY user, bypassing security!)
```

## SYNTAX
```sql
-- Security: Granting specific privileges
CREATE ROLE data_analyst;
GRANT SELECT ON users TO data_analyst;
REVOKE DELETE ON users FROM data_analyst;
```

## SIMPLE EXAMPLE
Your backend web server connects to the database. Instead of connecting as the `root` superuser, it should connect as a specific `web_app_user`. This user should only have `SELECT`, `INSERT`, and `UPDATE` privileges on specific tables. It should have its `DROP` and `DELETE` privileges `REVOKE`d to limit damage if the app is compromised.

## LINE-BY-LINE EXPLANATION
- `CREATE ROLE`: Creates a group that can hold permissions.
- `GRANT SELECT`: Specifically allows the role to read data from the `users` table.
- `REVOKE DELETE`: Explicitly prevents the role from deleting data.

## REAL-WORLD EXAMPLE
**Parameterized Queries (in Python):**
```python
# VULNERABLE (String concatenation)
cursor.execute("SELECT * FROM users WHERE name = '" + user_input + "'")

# SECURE (Parameterized query)
cursor.execute("SELECT * FROM users WHERE name = %s", (user_input,))
```
In the secure version, the database driver sanitizes the input, ensuring that even if `user_input` contains malicious SQL, it is treated purely as a literal string.

## OUTPUT
```text
Privileges granted successfully.
```

## COMMON MISTAKES
- **Trusting User Input:** Never concatenate raw user input directly into a SQL string. This is the #1 cause of database breaches.
- **Using 'sa' or 'root' for applications:** Giving a web app full administrative access to the database.
- **Ignoring Backups:** Security also means protection against data loss. Failing to automate and test daily backups.

## BEST PRACTICES
- **Always use Parameterized Queries / Prepared Statements.**
- **Encrypt Data at Rest and in Transit:** Use TLS for connections and encrypt sensitive columns (like SSNs or passwords using bcrypt/Argon2).
- **Audit Logs:** Track who accessed or modified critical data and when.

## TRY IT YOURSELF
Navigate to the exercises to practice identifying SQL injection vulnerabilities and assigning proper RBAC roles.
"""

m15_lesson = """# DBMS CAPSTONE

## WHAT IS IT?
This is the final culmination of your database journey. You will apply everything you have learned—from ER modeling and Normalization to SQL querying, Transactions, and Indexing—to design and query a complete, realistic database system.

## WHY DO WE NEED IT?
Isolated exercises teach you the syntax of individual commands. A Capstone project forces you to think like a Database Architect. You must understand how different components interact, how to enforce data integrity across multiple tables, and how to optimize queries for a complete system.

## WHERE IS IT USED?
1. **Industry Interviews:** System Design interviews often ask you to design the database schema for systems like Twitter, Uber, or a University.
2. **Real-World Applications:** Every backend application requires a robust, well-designed relational schema as its foundation.

## HOW DOES IT WORK?
You will be given a set of business requirements for a **College Management System**. You must follow the database design lifecycle:
1. Identify Entities and Relationships (ER Model).
2. Convert the ER Model to a Relational Schema.
3. Normalize the tables to 3NF.
4. Write the DDL (`CREATE TABLE`) scripts with proper constraints.
5. Write the DML (`INSERT`) scripts to populate data.
6. Write complex `SELECT` queries to generate reports.

## THE BUSINESS REQUIREMENTS
Design a system for a College.
1. The college has multiple **Departments** (e.g., Computer Science, Mathematics).
2. Each Department has multiple **Professors**. A Professor belongs to exactly one Department.
3. The college offers multiple **Courses**. Each Course is hosted by one Department.
4. **Students** enroll in the college.
5. Students can enroll in multiple Courses, and a Course can have multiple Students (Many-to-Many).
6. When a Student completes a Course, they receive a **Grade** (A, B, C, F).

## CAPSTONE CHALLENGES

### Challenge 1: Schema Design
Design the tables. Pay close attention to the Many-to-Many relationship between Students and Courses. You will need a junction (linking) table (e.g., `Enrollments`). Ensure all Primary and Foreign Keys are correctly identified.

### Challenge 2: DDL & Constraints
Write the `CREATE TABLE` statements.
- Ensure `email` addresses are unique.
- Ensure `Grade` can only be 'A', 'B', 'C', or 'F' using a `CHECK` constraint.
- Enforce referential integrity (e.g., you cannot delete a Department if it still has Professors).

### Challenge 3: Complex Reporting (Joins & Grouping)
Write a query to generate a report showing:
- Department Name
- Total Number of Students enrolled in courses offered by that department.
- Average Grade (Assume A=4, B=3, C=2, F=0) for courses in that department.

### Challenge 4: Transactions
Write a transaction that handles a student withdrawing from a course. It must:
1. Check if the student is actually enrolled.
2. Delete the record from the `Enrollments` table.
3. Insert a record into a `Withdrawal_Logs` table for auditing.
If any step fails, the entire operation must roll back.

### Challenge 5: Optimization
Identify which columns should be indexed. For example, if administrators frequently search for students by their `last_name`, write the `CREATE INDEX` statement to optimize this lookup.

## FINAL THOUGHTS
Building a database is a balance between strict data integrity and high performance. A well-designed schema will save thousands of hours of development time and prevent catastrophic data corruption.

## TRY IT YOURSELF
Head to the Capstone Project section to begin designing and building your College Management Database!
"""

# Placeholder empty lists to satisfy compilation
m11_exercises = []
m12_exercises = []
m13_exercises = []
m14_exercises = []
m15_exercises = []

m11_quizzes = []
m12_quizzes = []
m13_quizzes = []
m14_quizzes = []
m15_quizzes = []

dbms_lessons_3 = [m11_lesson, m12_lesson, m13_lesson, m14_lesson, m15_lesson]
dbms_exercises_3 = [m11_exercises, m12_exercises, m13_exercises, m14_exercises, m15_exercises]
dbms_quizzes_3 = [m11_quizzes, m12_quizzes, m13_quizzes, m14_quizzes, m15_quizzes]
