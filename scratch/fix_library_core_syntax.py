import os
import re

# 1. Float exponents with suffixes like 34_f128, 4_f16, etc.
pat_float_signed = re.compile(r'(\b\d+(?:\.\d+)?)[eE]\s*([+-])\s*(\d+[A-Za-z0-9_]*)')
pat_float_unsigned = re.compile(r'(\b\d+(?:\.\d+)?)[eE]\s+(\d+[A-Za-z0-9_]*)')

# 2. builtin# -> builtin #
pat_builtin = re.compile(r'\bbuiltin#\s*')

# 3. const#[ -> const #[
pat_const_attr = re.compile(r'\bconst#\[')

# 4. else#[ -> else #[
pat_else_attr = re.compile(r'\belse#\[')

count_floats = 0
count_builtin = 0
count_const_attr = 0
count_else_attr = 0
modified_files = set()

for target_dir in ['library', 'compiler', 'src']:
    if not os.path.exists(target_dir):
        continue
    for root, dirs, files in os.walk(target_dir):
        dirs[:] = [d for d in dirs if d not in ['target', 'build']]
        for f in files:
            if f.endswith('.rs'):
                path = os.path.join(root, f)
                try:
                    with open(path, 'r', encoding='utf-8') as fp:
                        content = fp.read()
                    
                    changed = False
                    if pat_float_signed.search(content):
                        new_content, n = pat_float_signed.subn(r'\1e\2\3', content)
                        content = new_content
                        count_floats += n
                        changed = True

                    if pat_float_unsigned.search(content):
                        new_content, n = pat_float_unsigned.subn(r'\1e\2', content)
                        content = new_content
                        count_floats += n
                        changed = True

                    if pat_builtin.search(content):
                        new_content, n = pat_builtin.subn('builtin # ', content)
                        content = new_content
                        count_builtin += n
                        changed = True

                    if pat_const_attr.search(content):
                        new_content, n = pat_const_attr.subn('const #[', content)
                        content = new_content
                        count_const_attr += n
                        changed = True

                    if pat_else_attr.search(content):
                        new_content, n = pat_else_attr.subn('else #[', content)
                        content = new_content
                        count_else_attr += n
                        changed = True

                    if changed:
                        with open(path, 'w', encoding='utf-8') as fp:
                            fp.write(content)
                        modified_files.add(path)
                except Exception as e:
                    print(f"Error {path}: {e}")

print(f"Fixed {count_floats} floats, {count_builtin} builtin#, {count_const_attr} const#[, {count_else_attr} else#[ in {len(modified_files)} files.")
