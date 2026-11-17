import os
import re

# 1. Fix binary_long.rs line 101: `* /` -> `*/`
binary_long_path = r'library\compiler-builtins\compiler-builtins\src\int\specialized_div_rem\binary_long.rs'
if os.path.exists(binary_long_path):
    with open(binary_long_path, 'r', encoding='utf-8') as fp:
        content = fp.read()
    new_content = content.replace('        * /', '        */')
    if new_content != content:
        with open(binary_long_path, 'w', encoding='utf-8') as fp:
            fp.write(new_content)
        print("Fixed * / in binary_long.rs")

# 2. Fix if#[ and else if#[ across library and src
pat = re.compile(r'\b(else\s+if|if)#\[')

count = 0
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
                    if pat.search(content):
                        new_content, n = pat.subn(r'\1 #[', content)
                        with open(path, 'w', encoding='utf-8') as fp:
                            fp.write(new_content)
                        count += n
                        modified_files.add(path)
                except Exception as e:
                    print(f"Error {path}: {e}")

print(f"Fixed {count} instances of if#[ / else if#[ across {len(modified_files)} files.")
