import re

def fix_quote_hash(text):
    def repl(m):
        prefix = m.group(1)
        if prefix == 'r' or prefix.endswith('html') or prefix.endswith('http') or prefix.endswith('https'):
            return m.group(0)
        return prefix + ' #'

    return re.sub(r'([a-zA-Z0-9_]+)#', repl, text)

for p in [
    'src/tools/rustfmt/config_proc_macro/src/item_enum.rs',
    'src/tools/rustfmt/config_proc_macro/src/utils.rs',
]:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    fixed = fix_quote_hash(content)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(fixed)
    print('Fixed:', p)

