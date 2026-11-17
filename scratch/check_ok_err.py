with open(r'B:\Rust\src\tools\clippy\tests\ui\manual_ok_err.rs', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '//~' in line:
        print(f"Line {i+1}: {line.strip()}")
        for k in range(max(0, i-2), i+1):
            print(f"  {k+1}: {lines[k]}", end='')
