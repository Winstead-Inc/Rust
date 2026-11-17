import os
import re

pattern = re.compile(r'\.\.=>')
count = 0
modified_files = 0

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
                    if pattern.search(content):
                        new_content, n = pattern.subn('.. =>', content)
                        with open(path, 'w', encoding='utf-8') as fp:
                            fp.write(new_content)
                        count += n
                        modified_files += 1
                except Exception as e:
                    print(f"Error processing {path}: {e}")

print(f"Fixed {count} occurrences of '..=>' in {modified_files} files.")
