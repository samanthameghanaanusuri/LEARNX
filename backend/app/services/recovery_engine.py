from app.models import db, Intervention, KnowledgeState, Concept, Diagnosis

# Pre-defined recovery content guides and post-intervention test questions
RECOVERY_GUIDES = {
    # DBMS
    "Relations": {
        "content": (
            "### Recovery Study Guide: Relations in DBMS\n\n"
            "A **relation** is a two-dimensional table in a relational database. Key components include:\n"
            "- **Attributes (Columns)**: Named fields representing properties of the relation (e.g., StudentID, Name).\n"
            "- **Tuples (Rows)**: A single record or data point containing values for each attribute.\n"
            "- **Domain**: The set of allowable values for each attribute (e.g., integers for Age).\n"
            "- **Schema**: The logical structure defining the relation name and its attributes (e.g., `Student(StudentID: Int, Name: VarChar)`).\n\n"
            "Remember: Tuples in a relation are unique, and order of columns or rows does not matter."
        ),
        "post_question": "Does the order of tuples (rows) in a relation affect its semantic meaning?",
        "options": ["Yes, rows must be sorted by primary key", "No, relation tuples are mathematically unordered sets", "Yes, rows must be in insertion order"],
        "correct": "No, relation tuples are mathematically unordered sets"
    },
    "Keys": {
        "content": (
            "### Recovery Study Guide: Database Keys\n\n"
            "Keys are attributes that establish relationships and identify records:\n"
            "- **Super Key**: Any set of attributes that uniquely identifies a tuple.\n"
            "- **Candidate Key**: A minimal super key (no redundant attributes). A table can have multiple candidate keys.\n"
            "- **Primary Key**: The candidate key selected by the database designer to uniquely identify records. Cannot be NULL.\n"
            "- **Foreign Key**: An attribute in a table that references the Primary Key of another table, enforcing referential integrity."
        ),
        "post_question": "Which of the following keys can contain NULL values?",
        "options": ["Primary Key", "Foreign Key", "Candidate Key"],
        "correct": "Foreign Key"
    },
    "Normalization": {
        "content": (
            "### Recovery Study Guide: Database Normalization\n\n"
            "Normalization reduces data redundancy and prevents anomalies:\n"
            "- **1NF (First Normal Form)**: All attributes must contain atomic (indivisible) values. No repeating groups.\n"
            "- **2NF (Second Normal Form)**: Must be in 1NF, and all non-key attributes must be fully functionally dependent on the entire primary key (no partial dependencies).\n"
            "- **3NF (Third Normal Form)**: Must be in 2NF, and no non-key attribute can be transitively dependent on the primary key."
        ),
        "post_question": "If a relation has a composite primary key (A, B) and a non-key attribute C depends only on A, which normal form is violated?",
        "options": ["1NF", "2NF", "3NF"],
        "correct": "2NF"
    },
    "SQL Querying": {
        "content": (
            "### Recovery Study Guide: SQL Querying Foundations\n\n"
            "SQL allows retrieving and manipulating data:\n"
            "- **SELECT**: Identifies columns to fetch.\n"
            "- **FROM**: Identifies tables.\n"
            "- **WHERE**: Filters rows based on a condition.\n"
            "- **GROUP BY**: Groups rows sharing property values to run aggregate functions (COUNT, SUM, AVG).\n"
            "- **JOIN**: Combines columns from multiple tables using shared keys."
        ),
        "post_question": "Which SQL clause is used to filter records AFTER grouping has occurred?",
        "options": ["WHERE", "HAVING", "ORDER BY"],
        "correct": "HAVING"
    },
    "Transactions & ACID": {
        "content": (
            "### Recovery Study Guide: Transactions & ACID Properties\n\n"
            "A transaction is a unit of work. Relational databases guarantee ACID properties:\n"
            "- **Atomicity**: All operations succeed, or none do (All-or-Nothing).\n"
            "- **Consistency**: Database transitions from one valid state to another, maintaining constraints.\n"
            "- **Isolation**: Concurrent transactions run independently without interference.\n"
            "- **Durability**: Committed changes persist even in the event of a system crash."
        ),
        "post_question": "Which ACID property guarantees that database changes persist after a crash?",
        "options": ["Atomicity", "Isolation", "Durability"],
        "correct": "Durability"
    },
    
    # DSA
    "Arrays": {
        "content": (
            "### Recovery Study Guide: Arrays\n\n"
            "An **Array** is a contiguous block of memory storing elements of the same type:\n"
            "- **Indexing**: Accessing an element by index takes $O(1)$ time because memory offset is calculated directly.\n"
            "- **Insertion/Deletion**: Takes $O(n)$ time in the worst case because elements must be shifted.\n"
            "- **Size**: Fixed at initialization in static arrays."
        ),
        "post_question": "What is the time complexity of searching for a value in an unsorted array of size N?",
        "options": ["O(1)", "O(log N)", "O(N)"],
        "correct": "O(N)"
    },
    "Linked Lists": {
        "content": (
            "### Recovery Study Guide: Linked Lists\n\n"
            "A **Linked List** is a linear data structure of nodes connected by pointers:\n"
            "- **Node**: Contains a data field and a reference (pointer) to the next node.\n"
            "- **Dynamic Size**: Easily grows/shrinks without reallocation.\n"
            "- **Sequential Access**: No random access. Accessing the K-th element takes $O(k)$ time.\n"
            "- **Insertion**: $O(1)$ time if pointer to insertion spot is known."
        ),
        "post_question": "What is the time complexity to insert a node at the head of a singly linked list?",
        "options": ["O(1)", "O(N)", "O(log N)"],
        "correct": "O(1)"
    },
    "Stacks & Queues": {
        "content": (
            "### Recovery Study Guide: Stacks & Queues\n\n"
            "- **Stack**: Last-In-First-Out (LIFO) structure. Operations: `push` (add) and `pop` (remove from top).\n"
            "- **Queue**: First-In-First-Out (FIFO) structure. Operations: `enqueue` (add to back) and `dequeue` (remove from front)."
        ),
        "post_question": "Which data structure is best suited to perform a Undo/Redo operations history log?",
        "options": ["Stack", "Queue", "Linked List"],
        "correct": "Stack"
    },
    "Binary Trees": {
        "content": (
            "### Recovery Study Guide: Binary Trees\n\n"
            "A **Binary Tree** is a hierarchical structure where each node has at most two children (left and right):\n"
            "- **Root**: Topmost node.\n"
            "- **Leaves**: Nodes with no children.\n"
            "- **Depth/Height**: Number of edges from root to node."
        ),
        "post_question": "What is the maximum number of nodes in a binary tree of height H (where height of root is 0)?",
        "options": ["H^2", "2^(H+1) - 1", "2^H"],
        "correct": "2^(H+1) - 1"
    },
    "Binary Search Trees (BST)": {
        "content": (
            "### Recovery Study Guide: Binary Search Trees (BST)\n\n"
            "A BST is a binary tree with the ordering property:\n"
            "- For any node, all values in its **left** subtree are **less** than the node's value.\n"
            "- All values in its **right** subtree are **greater** than the node's value.\n"
            "Average search, insertion, and deletion time is $O(\log n)$. Worst case is $O(n)$ if the tree is skewed."
        ),
        "post_question": "Which traversal of a BST visits nodes in sorted ascending order?",
        "options": ["Pre-order traversal", "In-order traversal", "Post-order traversal"],
        "correct": "In-order traversal"
    },
    "Graph Basics": {
        "content": (
            "### Recovery Study Guide: Graph Basics\n\n"
            "A graph is a set of vertices (nodes) and edges connecting them:\n"
            "- **Directed vs. Undirected**: Edges have direction or are bidirectional.\n"
            "- **Representation**: Adjacency Matrix ($V \times V$ table) or Adjacency List (array of linked lists).\n"
            "- **Traversal**: Breadth-First Search (BFS) using a Queue, Depth-First Search (DFS) using a Stack/Recursion."
        ),
        "post_question": "Which algorithm is commonly used to find the shortest path in an unweighted graph?",
        "options": ["Depth-First Search (DFS)", "Breadth-First Search (BFS)", "Kruskal's Algorithm"],
        "correct": "Breadth-First Search (BFS)"
    }
}

def create_intervention_for_diagnosis(diagnosis_id, student_id, concept_id):
    """
    Creates and records a new recovery intervention for a diagnosed weak concept.
    """
    concept = Concept.query.get(concept_id)
    if not concept:
        return None

    # Retrieve guide content or fallback
    guide_info = RECOVERY_GUIDES.get(concept.name, {
        "content": f"### Study Guide: {concept.name}\n\nReview this prerequisite concept.",
        "post_question": f"Is {concept.name} a fundamental concept?",
        "options": ["Yes", "No"],
        "correct": "Yes"
    })

    # Prepare intervention packet (content + post-question specs)
    intervention_content = {
        "guide": guide_info["content"],
        "post_question": guide_info["post_question"],
        "options": guide_info["options"]
    }

    import json
    intervention = Intervention(
        diagnosis_id=diagnosis_id,
        student_id=student_id,
        concept_id=concept_id,
        intervention_type="recovery_guide",
        intervention_content=json.dumps(intervention_content),
        status="assigned"
    )

    try:
        db.session.add(intervention)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    return intervention


def evaluate_recovery_attempt(intervention_id, student_answer):
    """
    Evaluates the student's answer to the recovery post-assessment.
    If correct, updates their KnowledgeState mastery score to 0.85 (Recovery).
    Updates intervention status to completed.
    """
    try:
        import json
        intervention = Intervention.query.get(intervention_id)
        if not intervention:
            return False, "Intervention not found"

        concept = Concept.query.get(intervention.concept_id)
        guide_info = RECOVERY_GUIDES.get(concept.name, None)
        if not guide_info:
            # Fallback evaluation
            correct = (student_answer.lower() == "yes")
        else:
            correct = (student_answer.strip() == guide_info["correct"].strip())

        if correct:
            # Update knowledge state for this concept
            ks = KnowledgeState.query.filter_by(
                student_id=intervention.student_id,
                concept_id=intervention.concept_id
            ).first()

            if not ks:
                ks = KnowledgeState(
                    student_id=intervention.student_id,
                    concept_id=intervention.concept_id,
                    mastery_score=0.85
                )
                db.session.add(ks)
            else:
                ks.mastery_score = max(ks.mastery_score, 0.85)

            intervention.status = "completed"
            intervention.post_intervention_mastery = 0.85
            db.session.commit()
            return True, "Recovery successful! Mastery has been updated."
        else:
            # Keep assigned or in_progress, do not update mastery
            intervention.status = "in_progress"
            db.session.commit()
            return False, "Incorrect answer. Please review the material and try again."
    except Exception as e:
        db.session.rollback()
        raise e
