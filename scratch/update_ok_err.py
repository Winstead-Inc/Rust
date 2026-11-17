path = r'B:\Rust\src\tools\clippy\tests\ui\manual_ok_err.rs'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if '//~^^^^^ manual_ok_err' in line:
        new_lines.append(line.replace('//~^^^^^ manual_ok_err', '//~^ manual_ok_err'))
    elif '//~^ manual_ok_err' in line and i > 0 and lines[i-1].strip() == '{':
        new_lines.append(line.replace('//~^ manual_ok_err', '//~^^ manual_ok_err'))
    else:
        new_lines.append(line)

with open(path, 'w', encoding='utf-8', newline='\n') as f:
    f.writelines(new_lines)

print("Updated manual_ok_err.rs")
