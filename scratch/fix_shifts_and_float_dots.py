import os
import re

# 1. Float dot: digit space dot not followed by dot or identifier
# e.g. `1 . {` or `0 .` -> `1.` or `0.`
pat_float_dot = re.compile(r'\b(\d+)\s+\.(?!\.)(?![a-zA-Z_])')

# 2. Right shift in expressions: `ident > > ident/number` -> `ident >> ident/number`
pat_rshift = re.compile(r'(\b[a-zA-Z0-9_]+\s*)>\s+>(\s*[a-zA-Z0-9_]+\b)')

# 3. Left shift in expressions: `ident < < ident/number` -> `ident << ident/number`
pat_lshift = re.compile(r'(\b[a-zA-Z0-9_]+\s*)<\s+<(\s*[a-zA-Z0-9_]+\b)')

count_dots = 0
count_rshift = 0
count_lshift = 0
modified_files = set()

for target in ['library', 'src', 'compiler']:
    if not os.path.exists(target):
        continue
    for root, dirs, files in os.walk(target):
        dirs[:] = [d for d in dirs if d not in ['target', 'build']]
        for f in files:
            if f.endswith('.rs'):
                path = os.path.join(root, f)
                try:
                    with open(path, 'r', encoding='utf-8') as fp:
                        content = fp.read()
                    
                    changed = False
                    if pat_float_dot.search(content):
                        new_content, n = pat_float_dot.subn(r'\1.', content)
                        content = new_content
                        count_dots += n
                        changed = True

                    if pat_rshift.search(content):
                        new_content, n = pat_rshift.subn(r'\1>>\2', content)
                        content = new_content
                        count_rshift += n
                        changed = True

                    if pat_lshift.search(content):
                        new_content, n = pat_lshift.subn(r'\1<<\2', content)
                        content = new_content
                        count_lshift += n
                        changed = True

                    if changed:
                        with open(path, 'w', encoding='utf-8') as fp:
                            fp.write(content)
                        modified_files.add(path)
                except Exception as e:
                    print(f"Error {path}: {e}")

print(f"Fixed {count_dots} float dots, {count_rshift} rshifts, {count_lshift} lshifts across {len(modified_files)} files.")
