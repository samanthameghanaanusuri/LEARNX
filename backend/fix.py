import glob
for f in glob.glob('content_cyber_*.py'):
    with open(f, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    changed = False
    if len(lines) > 0 and '"""' in lines[-1]:
        lines.pop()
        changed = True
    if len(lines) > 0 and '"""' in lines[-1]:
        lines.pop()
        changed = True
    if changed:
        print(f"Fixed {f}")
        with open(f, 'w', encoding='utf-8') as file:
            file.writelines(lines)
