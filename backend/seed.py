import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import create_app, db
from app.models import Subject, Concept, Question

def seed_database(app):
    """
    Idempotent seed for DBMS/DSA subjects, concepts, and questions.
    NEVER calls db.drop_all(). If records already exist, they are skipped.
    Safe to call on every startup.
    """
    with app.app_context():
        # Only create tables that don't exist yet — never drop
        db.create_all()

        print("Seeding database (idempotent)...")

        # 1. Subjects (get-or-create)
        dbms = Subject.query.filter_by(code='DBMS').first()
        if not dbms:
            dbms = Subject(
                name="Database Management Systems", 
                code="DBMS", 
                description="Relational model, SQL querying, normalization, and ACID transactions."
            )
            db.session.add(dbms)
        dsa = Subject.query.filter_by(code='DSA').first()
        if not dsa:
            dsa = Subject(
                name="Data Structures & Algorithms", 
                code="DSA", 
                description="Fundamental sequences, tree-structures, search heuristics, and graphs."
            )
            db.session.add(dsa)
        db.session.commit()

        def get_or_create_concept(subject_id, name, description):
            c = Concept.query.filter_by(subject_id=subject_id, name=name).first()
            if not c:
                c = Concept(subject_id=subject_id, name=name, description=description)
                db.session.add(c)
                db.session.flush()
            return c

        # 2. DBMS Concepts (get-or-create)
        c_relations = get_or_create_concept(dbms.id, "Relations", "Relational schemas, domains, attributes, and tuples.")
        c_keys = get_or_create_concept(dbms.id, "Keys", "Super keys, candidate keys, primary keys, and foreign keys.")
        c_normalization = get_or_create_concept(dbms.id, "Normalization", "Functional dependencies, 1NF, 2NF, 3NF, and BCNF normalization.")
        c_sql = get_or_create_concept(dbms.id, "SQL Querying", "Data querying, joins, filter clauses, and groupings.")
        c_transactions = get_or_create_concept(dbms.id, "Transactions & ACID", "Transactions, concurrency control, and ACID guarantees.")

        # Prerequisites (safe — append only if not already linked)
        def safe_prereq(concept, prereq):
            if prereq not in concept.prerequisites:
                concept.prerequisites.append(prereq)

        safe_prereq(c_keys, c_relations)
        safe_prereq(c_normalization, c_keys)
        safe_prereq(c_sql, c_relations)
        safe_prereq(c_transactions, c_sql)
        db.session.commit()

        # 3. DSA Concepts (get-or-create)
        c_arrays = get_or_create_concept(dsa.id, "Arrays", "Contiguous index-based memory sequences.")
        c_lists = get_or_create_concept(dsa.id, "Linked Lists", "Sequential node structures linked via pointers.")
        c_stacks_queues = get_or_create_concept(dsa.id, "Stacks & Queues", "LIFO stacks and FIFO queues.")
        c_trees = get_or_create_concept(dsa.id, "Binary Trees", "Hierarchical child-parent nodes and traversal systems.")
        c_bst = get_or_create_concept(dsa.id, "Binary Search Trees (BST)", "Ordered search trees, insertion, and in-order traversals.")
        c_graphs = get_or_create_concept(dsa.id, "Graph Basics", "Directed/undirected nodes, edges, BFS, and DFS traversals.")

        safe_prereq(c_lists, c_arrays)
        safe_prereq(c_stacks_queues, c_lists)
        safe_prereq(c_trees, c_stacks_queues)
        safe_prereq(c_bst, c_trees)
        safe_prereq(c_graphs, c_trees)
        db.session.commit()

        # 4. Questions (get-or-create by question_text)
        questions_data = [
            # DBMS: Relations
            dict(concept_id=c_relations.id, question_text="In the relational model, what represents a single record of data?",
                 options_json='["Attribute", "Tuple", "Schema", "Domain"]', correct_answer="Tuple", difficulty_level="Beginner"),
            dict(concept_id=c_relations.id, question_text="Which of the following describes the set of allowable values for a database column?",
                 options_json='["Tuple", "Relation", "Domain", "Key"]', correct_answer="Domain", difficulty_level="Beginner"),

            # DBMS: Keys
            dict(concept_id=c_keys.id, question_text="Which type of key is defined as a minimal super key?",
                 options_json='["Primary Key", "Candidate Key", "Foreign Key", "Super Key"]', correct_answer="Candidate Key", difficulty_level="Intermediate"),
            dict(concept_id=c_keys.id, question_text="A foreign key constraint enforces which of the following properties?",
                 options_json='["Entity Integrity", "Referential Integrity", "Domain Integrity", "User-Defined Integrity"]', correct_answer="Referential Integrity", difficulty_level="Intermediate"),

            # DBMS: Normalization
            dict(concept_id=c_normalization.id, question_text="A relation is in 2NF if it is in 1NF and what other condition is met?",
                 options_json='["No transitive dependencies exist", "No partial dependencies exist", "All attributes are atomic", "Every determinant is a candidate key"]', correct_answer="No partial dependencies exist", difficulty_level="Advanced"),
            dict(concept_id=c_normalization.id, question_text="Which normal form requires removing transitive functional dependencies?",
                 options_json='["1NF", "2NF", "3NF", "BCNF"]', correct_answer="3NF", difficulty_level="Advanced"),

            # DBMS: SQL Querying
            dict(concept_id=c_sql.id, question_text="Which clause is used to filter records AFTER an aggregation or grouping has occurred?",
                 options_json='["WHERE", "HAVING", "ORDER BY", "GROUP BY"]', correct_answer="HAVING", difficulty_level="Intermediate"),
            dict(concept_id=c_sql.id, question_text="What type of join returns all matching records plus non-matching records from the left table?",
                 options_json='["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN"]', correct_answer="LEFT JOIN", difficulty_level="Intermediate"),

            # DBMS: Transactions & ACID
            dict(concept_id=c_transactions.id, question_text="Which ACID property guarantees that all database operations in a transaction either succeed together or fail together?",
                 options_json='["Atomicity", "Consistency", "Isolation", "Durability"]', correct_answer="Atomicity", difficulty_level="Advanced"),
            dict(concept_id=c_transactions.id, question_text="Which transaction isolation level is the highest and prevents all concurrency anomalies?",
                 options_json='["Read Uncommitted", "Read Committed", "Repeatable Read", "Serializable"]', correct_answer="Serializable", difficulty_level="Advanced"),

            # DSA: Arrays
            dict(concept_id=c_arrays.id, question_text="What is the time complexity of looking up an element in a static array if the index is known?",
                 options_json='["O(1)", "O(log N)", "O(N)", "O(N log N)"]', correct_answer="O(1)", difficulty_level="Beginner"),
            dict(concept_id=c_arrays.id, question_text="Why does inserting an element at index 0 of an array of size N take O(N) time?",
                 options_json='["Memory allocation takes time", "We must shift all N existing elements to the right", "We must sort the array after insertion", "Array search takes O(N)"]', correct_answer="We must shift all N existing elements to the right", difficulty_level="Beginner"),

            # DSA: Linked Lists
            dict(concept_id=c_lists.id, question_text="What is the time complexity of inserting a node at the head of a singly linked list if we have a reference to the head?",
                 options_json='["O(1)", "O(log N)", "O(N)", "O(1) only if sorted"]', correct_answer="O(1)", difficulty_level="Intermediate"),
            dict(concept_id=c_lists.id, question_text="Unlike arrays, what is a primary advantage of linked lists?",
                 options_json='["Constant time random access", "Contiguous memory layout", "Dynamic size adjustment without full reallocation", "Binary search compatibility"]', correct_answer="Dynamic size adjustment without full reallocation", difficulty_level="Intermediate"),

            # DSA: Stacks & Queues
            dict(concept_id=c_stacks_queues.id, question_text="Which of the following data structures operates on a First-In-First-Out (FIFO) basis?",
                 options_json='["Stack", "Queue", "Binary Search Tree", "Min-Heap"]', correct_answer="Queue", difficulty_level="Intermediate"),
            dict(concept_id=c_stacks_queues.id, question_text="If you push 10, then push 20, then pop from a stack, what value is returned?",
                 options_json='["10", "20", "None", "30"]', correct_answer="20", difficulty_level="Intermediate"),

            # DSA: Binary Trees
            dict(concept_id=c_trees.id, question_text="What traversal visits the root node first, then the left subtree, and finally the right subtree?",
                 options_json='["In-order", "Pre-order", "Post-order", "Level-order"]', correct_answer="Pre-order", difficulty_level="Intermediate"),
            dict(concept_id=c_trees.id, question_text="What is the maximum number of leaves in a binary tree of height H (where height of root is 0)?",
                 options_json='["H", "H^2", "2^H", "2^(H+1)"]', correct_answer="2^H", difficulty_level="Intermediate"),

            # DSA: Binary Search Trees (BST)
            dict(concept_id=c_bst.id, question_text="In a Binary Search Tree (BST), what is true for every node?",
                 options_json='["Left child value is greater than node value", "Right child value is less than node value", "Left child value is less than node value, and right child value is greater", "Both children have identical values"]', correct_answer="Left child value is less than node value, and right child value is greater", difficulty_level="Advanced"),
            dict(concept_id=c_bst.id, question_text="Which tree traversal on a BST output values in sorted ascending order?",
                 options_json='["Pre-order", "In-order", "Post-order", "Breadth-First"]', correct_answer="In-order", difficulty_level="Advanced"),

            # DSA: Graph Basics
            dict(concept_id=c_graphs.id, question_text="Which traversal algorithm uses a Queue as its underlying helper data structure?",
                 options_json='["Depth-First Search (DFS)", "Breadth-First Search (BFS)", "Dijkstra\'s Algorithm", "Binary Search"]', correct_answer="Breadth-First Search (BFS)", difficulty_level="Advanced"),
            dict(concept_id=c_graphs.id, question_text="What graph representation is most memory-efficient for representing a sparse graph (few edges)?",
                 options_json='["Adjacency Matrix", "Adjacency List", "Edge Matrix", "Incidence Matrix"]', correct_answer="Adjacency List", difficulty_level="Advanced"),
        ]

        added_q = 0
        for qd in questions_data:
            existing = Question.query.filter_by(question_text=qd['question_text']).first()
            if not existing:
                db.session.add(Question(**qd))
                added_q += 1
        db.session.commit()
        print(f"Database seeded successfully. ({added_q} new questions added, {len(questions_data) - added_q} already existed.)")

if __name__ == '__main__':
    app = create_app()
    seed_database(app)
