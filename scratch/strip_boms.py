import os

count = 0
for base in ['compiler', 'library', 'src']:
    for root, dirs, files in os.walk(base):
        for f in files:
            if f.endswith('.toml'):
                p = os.path.join(root, f)
                with open(p, 'rb') as fp:
                    content = fp.read()
                if content.startswith(b'\xef\xbb\xbf'):
                    content = content[3:]
                    # Also strip any leading whitespace before [ if present
                    if content.startswith(b' ['):
                        content = content[1:]
                    with open(p, 'wb') as fp:
                        fp.write(content)
                    count += 1

print(f"Stripped BOM from {count} toml files!")
