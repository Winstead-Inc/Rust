import os, re

hits = []
for root, dirs, files in os.walk('src/tools/clippy/clippy_lints'):
    for f in files:
        if f.endswith('.rs'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                for line_no, line in enumerate(fp, 1):
                    # Check for explicit hardcoded brace newline in string literals
                    if r'{\n' in line or r'{{\n' in line:
                        hits.append((p, line_no, line.strip()))

print(f"Total occurrences of {{\\n in clippy_lints: {len(hits)}")
for h in hits:
    print(f"  {h[0]}:{h[1]}: {h[2][:120]}")
