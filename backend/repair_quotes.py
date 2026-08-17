import glob
import re

files = glob.glob('backend/html_data_m*.py')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to replace double quotes used for strings that contain HTML
    # We will find keys like "code", "starter_code", "expected_output"
    
    def replacer(match):
        key = match.group(1)
        val = match.group(2)
        # Escape any triple quotes inside the value just in case
        val = val.replace("'''", r"\'\'\'")
        return f'"{key}": \'\'\'{val}\'\'\''

    # Fix "code": "...",
    content = re.sub(r'"(code)": "(.*?)"(?=,\s*"language"|,\s*"order_index"|\s*})', replacer, content, flags=re.DOTALL)
    
    # Fix "starter_code": "...",
    content = re.sub(r'"(starter_code)": "(.*?)"(?=,\s*"language")', replacer, content, flags=re.DOTALL)
    
    # Fix "expected_output": "...",
    # Note expected_output is inside a test_cases dictionary
    content = re.sub(r'"(expected_output)": "(.*?)"(?=,\s*"is_hidden")', replacer, content, flags=re.DOTALL)

    # Fix "input_data": "...",
    content = re.sub(r'"(input_data)": "(.*?)"(?=,\s*"expected_output")', replacer, content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print("Regex fix applied.")
