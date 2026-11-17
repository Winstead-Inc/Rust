import os, re

pattern = re.compile(r'=\s*\r?\n\s*\[')

for root, dirs, files in os.walk('.'):
    if 'build' in dirs:
        dirs.remove('build')
    if '.git' in dirs:
        dirs.remove('.git')
    for f in files:
        if f.endswith('.toml'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fl:
                content = fl.read()
            new_content = pattern.sub('= [', content)
            if new_content != content:
                with open(p, 'w', encoding='utf-8') as fl:
                    fl.write(new_content)
                print('Fixed TOML:', p)
