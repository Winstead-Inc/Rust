import os
import re

pat_signed = re.compile(r'(\b\d+(?:\.\d+)?)[eE]\s*([+-])\s*(\d+\b)')
pat_unsigned = re.compile(r'(\b\d+(?:\.\d+)?)[eE]\s+(\d+\b)')

total_signed = 0
total_unsigned = 0
modified_files = set()

for target_dir in ['library', 'compiler', 'src', 'tests']:
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
                    if pat_signed.search(content):
                        new_content, n = pat_signed.subn(r'\1e\2\3', content)
                        content = new_content
                        total_signed += n
                        changed = True

                    if pat_unsigned.search(content):
                        new_content, n = pat_unsigned.subn(r'\1e\2', content)
                        content = new_content
                        total_unsigned += n
                        changed = True

                    if changed:
                        with open(path, 'w', encoding='utf-8') as fp:
                            fp.write(content)
                        modified_files.add(path)
                except Exception as e:
                    print(f"Error {path}: {e}")

print(f"Fixed {total_signed} signed and {total_unsigned} unsigned scientific float errors in {len(modified_files)} files.")
