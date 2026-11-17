path = r'B:\Rust\src\tools\clippy\tests\ui\question_mark.rs'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if '//~^^^ question_mark' in line and i > 0 and 'let Some(' in lines[i-1]:
        new_lines.append(line.replace('//~^^^ question_mark', '//~^ question_mark'))
    elif '//~^ question_mark' in line and i > 0 and lines[i-1].strip() == '{':
        new_lines.append(line.replace('//~^ question_mark', '//~^^ question_mark'))
    else:
        new_lines.append(line)

with open(path, 'w', encoding='utf-8', newline='\n') as f:
    f.writelines(new_lines)

print("Updated question_mark.rs")
