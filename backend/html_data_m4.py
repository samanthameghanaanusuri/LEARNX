def get_module_data():
    return {
        "title": "Forms & User Input",
        "description": "Learn how to collect data from users using forms, various input types, and submission methods.",
        "order_index": 4,
        "lessons": [
            {
                "title": "Building Interactive Forms",
                "slug": "forms-user-input",
                "content": "Forms are the primary way users send data to a web server.\\n\\n### The `<form>` Element\\nThe `<form>` tag acts as a container for input controls. Crucial attributes:\\n- `action`: The URL where the data is sent upon submission.\\n- `method`: The HTTP method used to send data (`GET` appends data to the URL, `POST` sends data invisibly in the request body—used for sensitive data).\\n\\n### The `<input>` Element\\nThe `<input>` tag is the most versatile form element. Its `type` attribute changes its behavior:\\n- `type=\"text\"`: Standard text box.\\n- `type=\"password\"`: Masks characters.\\n- `type=\"radio\"`: Select one option from a group (must share the same `name`).\\n- `type=\"checkbox\"`: Toggle multiple options.\\n- `type=\"email\"`: Validates for email format.\\n- `type=\"submit\"`: A button that submits the form.\\n\\n### Labels and Accessibility\\nEvery input should have an associated `<label>`. This is crucial for accessibility. The `for` attribute of the label must match the `id` attribute of the input.\\n\\n### Other Controls\\n- `<textarea>`: For multi-line text input.\\n- `<select>` and `<option>`: Create a dropdown menu.\\n- `<fieldset>` and `<legend>`: Group related form elements and provide a caption.",
                "order_index": 1,
                "examples": [
                    {
                        "title": "A Complete Login Form",
                        "explanation": "A standard POST form with labels, text, password, and submit button.",
                        "code": '''<form action=\"/login\" method=\"POST\">\\n    <label for=\"username\">Username:</label>\\n    <input type=\"text\" id=\"username\" name=\"username\" required>\\n    <br>\\n    <label for=\"pwd\">Password:</label>\\n    <input type=\"password\" id=\"pwd\" name=\"password\" required>\\n    <br>\\n    <input type=\"submit\" value=\"Log In\">\\n</form>''',
                        "language": "html",
                        "order_index": 1
                    },
                    {
                        "title": "Dropdowns and Textareas",
                        "explanation": "Collecting longer feedback and choosing from a list.",
                        "code": '''<form action=\"/feedback\">\\n    <label for=\"rating\">Rating:</label>\\n    <select id=\"rating\" name=\"rating\">\\n        <option value=\"good\">Good</option>\\n        <option value=\"bad\">Bad</option>\\n    </select>\\n    <br>\\n    <label for=\"comments\">Comments:</label>\\n    <textarea id=\"comments\" name=\"comments\" rows=\"4\" cols=\"50\"></textarea>\\n</form>''',
                        "language": "html",
                        "order_index": 2
                    }
                ],
                "exercises": [
                    {
                        "title": "Create a Basic Form",
                        "description": "Create a `form` with an `action` of '/submit' and a `method` of 'POST'. Leave it empty inside.",
                        "difficulty": "Easy",
                        "starter_code": '''<!-- Write your form here -->''',
                        "language": "html",
                        "order_index": 1,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<form action=\"/submit\" method=\"POST\"></form>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Add a Labeled Text Input",
                        "description": "Inside a form, create a `label` (for 'fname') with text 'First Name:', and a text `input` with id 'fname' and name 'first_name'.",
                        "difficulty": "Medium",
                        "starter_code": '''<form>\\n\\n</form>''',
                        "language": "html",
                        "order_index": 2,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<form><label for=\"fname\">First Name:</label><input type=\"text\" id=\"fname\" name=\"first_name\"></form>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Create a Password Field",
                        "description": "Add an input of type 'password' with the name 'pwd' and id 'pwd'.",
                        "difficulty": "Easy",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 3,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<input type=\"password\" id=\"pwd\" name=\"pwd\">''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Radio Buttons Group",
                        "description": "Create two radio buttons for a 'gender' selection. Both must have the name 'gender'. The first value is 'male', second is 'female'.",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 4,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<input type=\"radio\" name=\"gender\" value=\"male\"><input type=\"radio\" name=\"gender\" value=\"female\">''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Dropdown Select",
                        "description": "Create a `select` element with the name 'cars'. Add two `option` elements: 'Volvo' (value='volvo') and 'Saab' (value='saab').",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 5,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<select name=\"cars\"><option value=\"volvo\">Volvo</option><option value=\"saab\">Saab</option></select>''', "is_hidden": False, "order_index": 1}
                        ]
                    }
                ],
                "quizzes": [
                    {
                        "question_text": "Which attribute on the <form> tag specifies where to send the form data?",
                        "options": ["method", "action", "target", "src"],
                        "correct_answer": "action",
                        "explanation": "The 'action' attribute contains the URL endpoint that receives the form data.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "What is the difference between GET and POST methods?",
                        "options": ["GET is for secure data, POST is for public data", "GET appends data to the URL, POST sends data in the HTTP body", "GET is faster, POST is slower", "There is no difference"],
                        "correct_answer": "GET appends data to the URL, POST sends data in the HTTP body",
                        "explanation": "GET is visible in the URL (good for searches), while POST is hidden in the request body (required for passwords).",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "How do you associate a <label> with an <input> for accessibility?",
                        "options": ["Wrap the label in a <div>", "Use the 'for' attribute on the label matching the 'id' of the input", "Use the 'name' attribute on both", "Place them next to each other"],
                        "correct_answer": "Use the 'for' attribute on the label matching the 'id' of the input",
                        "explanation": "The 'for' attribute creates a programmatic link to the input's 'id', allowing screen readers to announce it and clicking the label to focus the input.",
                        "difficulty": "Hard"
                    },
                    {
                        "question_text": "Which input type masks the characters typed by the user?",
                        "options": ["hidden", "secret", "password", "masked"],
                        "correct_answer": "password",
                        "explanation": "type='password' replaces typed characters with dots or asterisks.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "How do you group mutually exclusive radio buttons?",
                        "options": ["Give them the same 'id'", "Give them the same 'name'", "Put them in the same <div>", "Give them the same 'value'"],
                        "correct_answer": "Give them the same 'name'",
                        "explanation": "Radio buttons with the exact same 'name' attribute form a group where only one can be selected.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Which tag is used for multi-line text input?",
                        "options": ["<input type='text' lines='multi'>", "<textarea>", "<textbox>", "<input type='textarea'>"],
                        "correct_answer": "<textarea>",
                        "explanation": "<textarea> is a distinct element, not an input type.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Which attribute determines the key name sent to the server for a form field?",
                        "options": ["id", "class", "name", "value"],
                        "correct_answer": "name",
                        "explanation": "When submitted, form data is sent as name/value pairs. The 'name' attribute defines the key.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "What does a <fieldset> do?",
                        "options": ["Submits the form", "Groups related elements within a form, often drawing a box around them", "Styles the form automatically", "Creates a dropdown menu"],
                        "correct_answer": "Groups related elements within a form, often drawing a box around them",
                        "explanation": "<fieldset> logically groups elements, and its child <legend> provides a caption.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Which input type is specifically designed for submitting the form?",
                        "options": ["type='button'", "type='submit'", "type='send'", "type='action'"],
                        "correct_answer": "type='submit'",
                        "explanation": "type='submit' triggers the form's action and method to send the data.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Can a single form contain both text inputs and file uploads?",
                        "options": ["Yes, but it requires the enctype='multipart/form-data' attribute", "No, file uploads must be in their own form", "Yes, with no additional configuration", "No, HTML does not support file uploads"],
                        "correct_answer": "Yes, but it requires the enctype='multipart/form-data' attribute",
                        "explanation": "To upload files alongside text, the form's encoding type must be set to handle binary data.",
                        "difficulty": "Hard"
                    }
                ],
                "project": {
                    "title": "Student Registration Form",
                    "scenario": "A school needs a registration form to enroll new students.",
                    "objective": "Build a comprehensive form utilizing text, email, radio, and select inputs.",
                    "requirements": "Form posts to '/enroll'. Include labeled inputs for Name (text, id='name'), Email (email, id='email'), a 'Course' dropdown (select, name='course') with two options ('Math', 'Science'), and a submit button.",
                    "features": "Form Action, Method, Labels, Text, Email, Select, Submit",
                    "guidance": "Ensure every input has a matching label via for/id. Remember the select tag wraps option tags.",
                    "expected_behavior": "A complete, submittable registration form.",
                    "evaluation_criteria": "Presence of form, labels, text/email inputs, select dropdown, and submit.",
                    "starter_code": '''<form action=\"/enroll\" method=\"POST\">\\n\\n</form>''',
                    "language": "html",
                    "test_cases": [
                        {"input_data": '''''', "expected_output": '''<form action=\"/enroll\" method=\"POST\"><label for=\"name\">Name</label><input type=\"text\" id=\"name\" name=\"name\"><label for=\"email\">Email</label><input type=\"email\" id=\"email\" name=\"email\"><label for=\"course\">Course</label><select id=\"course\" name=\"course\"><option value=\"Math\">Math</option><option value=\"Science\">Science</option></select><input type=\"submit\" value=\"Submit\"></form>''', "is_hidden": False, "order_index": 1}
                    ]
                }
            }
        ]
    }
