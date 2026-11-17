import os, re

pattern = re.compile(r'\b(\d+)\s+\.(?!\.)(?=\s*[,);\]}\+\-\*\/<>=!|&]|\s*$)')

count = 0
for base in ['library', 'src']:
    for root, _, files in os.walk(base):
        for f in files:
            if f.endswith('.rs'):
                p = os.path.join(root, f)
                with open(p, 'r', encoding='utf-8', errors='ignore') as fl:
                    content = fl.read()
                new_content = pattern.sub(r'\1.', content)
                if new_content != content:
                    with open(p, 'w', encoding='utf-8') as fl:
                        fl.write(new_content)
                    count += 1
print(f'Fixed float dots in {count} files.')
