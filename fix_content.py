with open('backend/content_c.py', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('"explanation": ""Hello" requires 6 bytes (5 for letters + 1 for \'\\0\'). Providing only 5 bytes means no terminator is stored."', '"explanation": "\\\"Hello\\\" requires 6 bytes (5 for letters + 1 for \'\\\\0\'). Providing only 5 bytes means no terminator is stored."')

with open('backend/content_c.py', 'w', encoding='utf-8') as f:
    f.write(c)

import ast
try:
    ast.parse(c)
    print("Parsed successfully!")
except SyntaxError as e:
    print(f"Syntax error at line {e.lineno}: {e.text}")
