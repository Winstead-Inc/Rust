with open(r'C:/Users/0.USS-OPPENHEIMER/.gemini/antigravity/brain/992886c1-f8be-41f5-82be-515f85028334/.system_generated/steps/4765/output.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.find('FAILED TEST: tests/ui/unit_arg_fixable.rs')
idx_next = text.find('FAILED TEST: tests/ui/unit_arg.rs')
print(f"idx={idx}, idx_next={idx_next}")
section = text[idx:idx_next]
for line in section.splitlines():
    if not line.startswith('command:') and not line.startswith('"B:\\Rust'):
        print(line[:120])
