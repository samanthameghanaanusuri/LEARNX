def get_module_data():
    return {
        "title": "Advanced Forms & Validation",
        "description": "Ensure data integrity by mastering browser-native form validation, advanced input types, and UX principles.",
        "order_index": 7,
        "lessons": [
            {
                "title": "Native Validation and Complex Inputs",
                "slug": "advanced-forms-validation",
                "content": "HTML5 offers powerful built-in form validation, reducing the need for complex JavaScript for basic checks.\\n\\n### Validation Attributes\\n- `required`: Forces the user to fill out the field before submitting.\\n- `minlength` and `maxlength`: Restricts the string length.\\n- `min` and `max`: Restricts the numerical or date range.\\n- `pattern`: Uses a Regular Expression (Regex) to validate the input (e.g., ensuring a zip code is 5 digits).\\n- `step`: Specifies the legal number intervals.\\n\\n### Advanced Input Types\\n- `type=\"range\"`: A slider control.\\n- `type=\"color\"`: A color picker.\\n- `type=\"date\"`, `type=\"time\"`: Native date/time pickers.\\n- `type=\"file\"`: Allows file uploads. (Remember: The `<form>` must have `enctype=\"multipart/form-data\"`).\\n\\n### Bypassing Validation\\nThe `novalidate` attribute on a `<form>` tag tells the browser to skip native validation (often used when relying on custom JavaScript validation).\\n\\n**Best Practice:** Client-side HTML validation improves User Experience (UX) by catching errors instantly, but you **must always** validate data on the server-side as well, because client-side HTML validation can easily be bypassed by a malicious user.",
                "order_index": 1,
                "examples": [
                    {
                        "title": "A Validated Form",
                        "explanation": "A form requiring a username between 3 and 10 characters, and an age between 18 and 99.",
                        "code": '''<form action=\"/register\" method=\"POST\">\\n    <label for=\"uname\">Username:</label>\\n    <input type=\"text\" id=\"uname\" name=\"uname\" required minlength=\"3\" maxlength=\"10\">\\n    \\n    <label for=\"age\">Age (18+):</label>\\n    <input type=\"number\" id=\"age\" name=\"age\" required min=\"18\" max=\"99\">\\n    \\n    <input type=\"submit\" value=\"Register\">\\n</form>''',
                        "language": "html",
                        "order_index": 1
                    },
                    {
                        "title": "Regex Pattern Validation",
                        "explanation": "Using a pattern to ensure the user inputs exactly 5 digits for a ZIP code.",
                        "code": '''<form>\\n    <label for=\"zip\">ZIP Code:</label>\\n    <input type=\"text\" id=\"zip\" name=\"zip\" pattern=\"[0-9]{5}\" title=\"Five digit zip code\" required>\\n    <input type=\"submit\">\\n</form>''',
                        "language": "html",
                        "order_index": 2
                    }
                ],
                "exercises": [
                    {
                        "title": "Require an Input",
                        "description": "Add the attribute to the text input so the form cannot be submitted if it is empty.",
                        "difficulty": "Medium",
                        "starter_code": '''<form><input type=\"text\" name=\"user\"><input type=\"submit\"></form>''',
                        "language": "html",
                        "order_index": 1,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<form><input type=\"text\" name=\"user\" required><input type=\"submit\"></form>''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Min and Max Length",
                        "description": "Update the password input to require a minimum of 8 characters and a maximum of 20 characters.",
                        "difficulty": "Medium",
                        "starter_code": '''<input type=\"password\" id=\"pwd\">''',
                        "language": "html",
                        "order_index": 2,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<input type=\"password\" id=\"pwd\" minlength=\"8\" maxlength=\"20\">''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Number Ranges",
                        "description": "Create a number input with the name 'quantity'. It must be between 1 and 5 inclusive.",
                        "difficulty": "Medium",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 3,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<input type=\"number\" name=\"quantity\" min=\"1\" max=\"5\">''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "Pattern Validation",
                        "description": "Create a text input for a Username (name='user'). It must match the pattern `[A-Za-z]{3}` (exactly 3 letters).",
                        "difficulty": "Hard",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 4,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<input type=\"text\" name=\"user\" pattern=\"[A-Za-z]{3}\">''', "is_hidden": False, "order_index": 1}
                        ]
                    },
                    {
                        "title": "File Upload Setup",
                        "description": "Create a form that points to '/upload' with POST. Set the proper `enctype`. Inside, create a file input named 'doc'.",
                        "difficulty": "Hard",
                        "starter_code": '''''',
                        "language": "html",
                        "order_index": 5,
                        "test_cases": [
                            {"input_data": '''''', "expected_output": '''<form action=\"/upload\" method=\"POST\" enctype=\"multipart/form-data\"><input type=\"file\" name=\"doc\"></form>''', "is_hidden": False, "order_index": 1}
                        ]
                    }
                ],
                "quizzes": [
                    {
                        "question_text": "Which attribute prevents a form from being submitted if the input field is empty?",
                        "options": ["mandatory", "required", "needed", "validate"],
                        "correct_answer": "required",
                        "explanation": "The 'required' boolean attribute instructs the browser to enforce that the field has a value.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "To restrict a number input to only allow values between 10 and 50, which attributes are used?",
                        "options": ["minlength and maxlength", "start and end", "min and max", "bottom and top"],
                        "correct_answer": "min and max",
                        "explanation": "min and max restrict numerical and date ranges, whereas minlength and maxlength restrict string character counts.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "What does the 'pattern' attribute do?",
                        "options": ["Provides a background pattern for the input box", "Forces the input to match a specified Regular Expression", "Fills the input with placeholder text", "Sets the color scheme of the form"],
                        "correct_answer": "Forces the input to match a specified Regular Expression",
                        "explanation": "The pattern attribute takes a regex string that the browser uses to validate the input value.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Why must you still validate form data on the backend/server, even if you use HTML5 validation attributes?",
                        "options": ["Because HTML5 validation only works on Chrome", "Because client-side HTML validation can be easily bypassed by modifying the DOM or sending direct HTTP requests", "Because servers require more CPU power", "Because HTML5 validation is deprecated"],
                        "correct_answer": "Because client-side HTML validation can be easily bypassed by modifying the DOM or sending direct HTTP requests",
                        "explanation": "Client-side validation is strictly for User Experience. Security and data integrity must always be enforced on the server.",
                        "difficulty": "Hard"
                    },
                    {
                        "question_text": "What is the correct enctype for a form that contains an <input type='file'>?",
                        "options": ["application/x-www-form-urlencoded", "text/plain", "multipart/form-data", "application/json"],
                        "correct_answer": "multipart/form-data",
                        "explanation": "This encoding type is required for the form to send binary file data alongside text.",
                        "difficulty": "Hard"
                    },
                    {
                        "question_text": "Which attribute tells the browser to skip all native HTML validation upon submission?",
                        "options": ["novalidate", "skip-validation", "formnovalidate", "ignore"],
                        "correct_answer": "novalidate",
                        "explanation": "Placing 'novalidate' on the <form> tag disables the browser's native validation popups.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Which input type displays a slider widget?",
                        "options": ["slider", "range", "scroll", "scale"],
                        "correct_answer": "range",
                        "explanation": "<input type='range'> provides a UI slider for selecting a number within a range.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "What does the 'step' attribute do on a number input?",
                        "options": ["Sets the maximum allowed value", "Specifies the legal number intervals (e.g., step='5' allows 0, 5, 10)", "Increases the size of the input box", "Creates a multi-step form wizard"],
                        "correct_answer": "Specifies the legal number intervals (e.g., step='5' allows 0, 5, 10)",
                        "explanation": "Step determines the granularity of the input values allowed.",
                        "difficulty": "Medium"
                    },
                    {
                        "question_text": "Which attribute provides a hint inside the input box that disappears when the user starts typing?",
                        "options": ["hint", "placeholder", "default", "value"],
                        "correct_answer": "placeholder",
                        "explanation": "The placeholder attribute shows light text to guide the user.",
                        "difficulty": "Easy"
                    },
                    {
                        "question_text": "Should a placeholder attribute replace a <label>?",
                        "options": ["Yes, it looks cleaner", "No, because placeholders disappear when typing and screen readers may not read them reliably", "Only on mobile devices", "Yes, it saves space in the database"],
                        "correct_answer": "No, because placeholders disappear when typing and screen readers may not read them reliably",
                        "explanation": "Placeholders are not an accessible alternative to explicit labels.",
                        "difficulty": "Medium"
                    }
                ],
                "project": {
                    "title": "Job Application Portal Form",
                    "scenario": "You are building a secure, validated job application form.",
                    "objective": "Combine patterns, constraints, and file uploads.",
                    "requirements": "Create a POST form to '/apply' that handles files. Include an email input (required), a Phone input (pattern='[0-9]{10}', required), a Years of Experience input (number, min=0, max=50), and a Resume upload (file). Include a submit button.",
                    "features": "Validation, Pattern, Min/Max, File Upload, Multipart EncType",
                    "guidance": "Don't forget the enctype on the form. Use proper input types and validation attributes.",
                    "expected_behavior": "A heavily constrained form ready for a backend.",
                    "evaluation_criteria": "Correct form enctype, required fields, pattern syntax, and number constraints.",
                    "starter_code": '''<form>\\n\\n</form>''',
                    "language": "html",
                    "test_cases": [
                        {"input_data": '''''', "expected_output": '''<form action=\"/apply\" method=\"POST\" enctype=\"multipart/form-data\"><input type=\"email\" name=\"email\" required><input type=\"text\" name=\"phone\" pattern=\"[0-9]{10}\" required><input type=\"number\" name=\"experience\" min=\"0\" max=\"50\"><input type=\"file\" name=\"resume\"><input type=\"submit\"></form>''', "is_hidden": False, "order_index": 1}
                    ]
                }
            }
        ]
    }
