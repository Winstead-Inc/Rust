import os, re

# 1. Fix r# <ident> -> r#<ident>
for root, _, files in os.walk('compiler'):
    for f in files:
        if f.endswith('.rs'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fl:
                content = fl.read()
            new_content = re.sub(r'r#\s+([a-zA-Z0-9_]+)', r'r#\1', content)
            if new_content != content:
                with open(p, 'w', encoding='utf-8') as fl:
                    fl.write(new_content)
                print('Fixed r# in:', p)

# 2. Fix FutureReleaseError# in rustc_lint/src/builtin.rs if present
p = 'compiler/rustc_lint/src/builtin.rs'
if os.path.exists(p):
    with open(p, 'r', encoding='utf-8') as f:
        s = f.read()
    s = s.replace('FutureReleaseError#', 'FutureReleaseError # ')
    s = s.replace('FutureReleaseSemanticsChange#', 'FutureReleaseSemanticsChange # ')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)
    print('Fixed FutureReleaseError in rustc_lint/src/builtin.rs')

