def get_module_data():
    return {
        "title": "Lists, Tables & Structured Data",
        "description": "Organize data effectively using ordered lists, unordered lists, description lists, and complex tables.",
        "order_index": 3,
        "lessons": [
            {
                "title": "Structuring Data with Lists and Tables",
                "slug": "lists-tables-structured-data",
                "content": "Not all content is simple paragraphs. Often, data must be structured as lists or grids (tables).\\n\\n### Lists\\nHTML supports three main types of lists:\\n1. **Unordered Lists (`<ul>`)**: Used for items where order doesn't matter (e.g., a shopping list). Items are marked with bullets. Each item is an `<li>` (List Item).\\n2. **Ordered Lists (`<ol>`)**: Used for numbered steps (e.g., a recipe). Each item is an `<li>`.\\n3. **Description Lists (`<dl>`)**: Used for key-value pairs (like a dictionary). Consists of `<dt>` (Description Term) and `<dd>` (Description Details).\\n\\n### Tables\\nTables represent tabular data in a grid. \\n- `<table>`: The container for the table.\\n- `<tr>`: Table Row.\\n- `<th>`: Table Header (bold, centered by default). Used for column or row labels.\\n- `<td>`: Table Data (a standard cell).\\n\\n**Advanced Table Structure:**\\nFor large tables and accessibility, it is best practice to group rows semantically:\\n- `<thead>`: Wraps the header rows.\\n- `<tbody>`: Wraps the primary data rows.\\n- `<tfoot>`: Wraps summary or footer rows.\\n\\n**Spanning Cells:**\\nTo make a cell span multiple columns or rows, use the `colspan` and `rowspan` attributes on `<th>` or `<td>` elements.",
                "order_index": 1,
                "examples": [
                    {
                        "title": "Nested Lists",
                        "explanation": "You can place a list inside another list item. This is commonly used for multi-level navigation menus.",
                        "code": '''<ul>\\n    <li>Fruits\\n        <ul>\\n            <li>Apple</li>\\n            <li>Banana</li>\\n        </ul>\\n    </li>\\n    <li>Vegetables</li>\\n</ul>''',
                        "language": "html",
                        "order_index": 1
                    },
                    {
                        "title": "Advanced Semantic Table",
                        "explanation": "A complete table using thead, tbody, tfoot, and spanning cells.",
                        "code": '''<table>\\n    <thead>\\n        <tr>\\n            <th>Item</th>\\n            <th>Qty</th>\\n            <th>Price</th>\\n        </tr>\\n    </thead>\\n    <tbody>\\n        <tr>\\n            <td>Apple</td>\\n            <td>2</td>\\n            <td>$1.00</td>\\n        </tr>\\n    </tbody>\\n    <tfoot>\\n        <tr>\\n            <td colspan=\"2\">Total</td>\\n            <td>$2.00</td>\\n        </tr>\\n    </tfoot>\\n</table>''',
                        "language": "html",
                        "order_index": 2
                    }
                ],
                "exercises": [
                    {
                        "title": "Create a Shopping List",
                        "description": "Create an unordered list containing three list items: 'Milk', 'Bread', and 'Eggs'.",
                        "difficulty": "Easy",
                        "starter_code": '''<!-- Write your unordered list here -->''',
                        "language": "html",
                        "order_index": 1,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<ul><li>Milk</li><li>Bread</li><li>Eggs</li></ul>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Create a Workflow",
                        "description": "Create an ordered list with three steps: 'Wake up', 'Code', 'Sleep'.",
                        "difficulty": "Easy",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 2,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<ol><li>Wake up</li><li>Code</li><li>Sleep</li></ol>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Create a Description List",
                        "description": "Create a definition list (`dl`). Add a term (`dt`) 'HTML' and its detail (`dd`) 'Markup language'.",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 3,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<dl><dt>HTML</dt><dd>Markup language</dd></dl>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Build a Simple Table",
                        "description": "Create a `table` with two rows (`tr`). The first row should have two headers (`th`): 'Name' and 'Age'. The second row should have two data cells (`td`): 'Alice' and '30'.",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 4,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<table><tr><th>Name</th><th>Age</th></tr><tr><td>Alice</td><td>30</td></tr></table>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Table with Colspan",
                        "description": "Create a `table` with a single row. Inside the row, add a `th` cell containing 'Inventory Report' that spans 3 columns.",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 5,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<table><tr><th colspan=\"3\">Inventory Report</th></tr></table>''', "is_hidden": False, "order_index": 1}
                        ]
                    }
                ],
                "quizzes": [
                    {
                        "question_text": "Which tag is used to create a bulleted (unordered) list?",
                        "options": ["<ol>", "<list>", "<ul>", "<li>"],
                        "correct_answer": "<ul>",
                        "explanation": "<ul> stands for Unordered List, which defaults to bullet points.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "What tag is used for individual items within both <ul> and <ol>?",
                        "options": ["<item>", "<li>", "<ul>", "<list-item>"],
                        "correct_answer": "<li>",
                        "explanation": "<li> stands for List Item and is required inside ul or ol tags.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "In a description list (<dl>), which tag defines the 'term' or 'name' part?",
                        "options": ["<dd>", "<dt>", "<term>", "<dl>"],
                        "correct_answer": "<dt>",
                        "explanation": "<dt> stands for Description Term.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Which element defines a row in an HTML table?",
                        "options": ["<th>", "<td>", "<tr>", "<row>"],
                        "correct_answer": "<tr>",
                        "explanation": "<tr> stands for Table Row.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "What is the semantic difference between <th> and <td>?",
                        "options": ["<th> is for column headers, <td> is for standard data", "<th> is for standard data, <td> is for headers", "They are identical, just different names", "<th> creates a row, <td> creates a column"],
                        "correct_answer": "<th> is for column headers, <td> is for standard data",
                        "explanation": "<th> (Table Header) semantically defines header cells, improving accessibility.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Which attribute merges two or more adjacent columns into a single cell?",
                        "options": ["rowspan", "merge", "colspan", "span"],
                        "correct_answer": "colspan",
                        "explanation": "The 'colspan' attribute defines how many columns a cell should span.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "To structure a table semantically, which tag wraps the header row(s)?",
                        "options": ["<header>", "<thead>", "<th>", "<top>"],
                        "correct_answer": "<thead>",
                        "explanation": "<thead> groups the header content in an HTML table.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Where is the correct place to nest a list inside another list?",
                        "options": ["Directly inside the <ul> or <ol> tag", "Inside an <li> tag", "After the </ul> tag", "It is not possible to nest lists"],
                        "correct_answer": "Inside an <li> tag",
                        "explanation": "A nested list must be a child of an <li> element, not a direct child of the parent <ul> or <ol>.",
                        "difficulty": "Hard"
                    },
                    {
                        "question_text": "Which tag is used to specify a summary footer row for a table?",
                        "options": ["<footer>", "<tbody>", "<tfoot>", "<bottom>"],
                        "correct_answer": "<tfoot>",
                        "explanation": "<tfoot> groups the footer content in a table.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Does an HTML table require <thead> and <tbody> to be valid?",
                        "options": ["Yes, always", "No, they are optional but highly recommended for complex tables", "Only if there is a <tfoot>", "No, they are deprecated in HTML5"],
                        "correct_answer": "No, they are optional but highly recommended for complex tables",
                        "explanation": "While purely optional for validity, using them provides semantic meaning and aids styling and accessibility.",
                        "difficulty": "Medium"
                    }
                ],
                "project": {
                    "title": "Student Result Dashboard",
                    "scenario": "You are tasked with presenting a student's semester grades in a structured format.",
                    "objective": "Build a semantic table using grouping tags and spanning.",
                    "requirements": "Create a table with a `thead` (Columns: 'Subject', 'Grade'). A `tbody` with two subjects ('Math', 'A') and ('Science', 'B'). A `tfoot` with a 'GPA' row where 'GPA' spans the first column, and '3.5' is in the second.",
                    "features": "Table Grouping, Colspan",
                    "guidance": "Remember to wrap your rows inside the respective grouping elements (thead, tbody, tfoot).",
                    "expected_behavior": "A grid displaying the headers, two rows of data, and a summary footer with a merged cell.",
                    "evaluation_criteria": "Presence of table, thead, tbody, tfoot, and proper use of colspan.",
                    "starter_code": '''<table>\\n\\n</table>''',
                    "language": "html",
                    "test_cases": [
                        {"input_data": '''''', "expected_output": '''<table><thead><tr><th>Subject</th><th>Grade</th></tr></thead><tbody><tr><td>Math</td><td>A</td></tr><tr><td>Science</td><td>B</td></tr></tbody><tfoot><tr><th colspan=\"1\">GPA</th><td>3.5</td></tr></tfoot></table>''', "is_hidden": False, "order_index": 1}
                    ]
                }
            }
        ]
    }
