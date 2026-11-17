for p in ['B:\\Rust\\src\\tools\\clippy\\tests\\ui\\single_element_loop.rs', 'B:\\Rust\\src\\tools\\clippy\\tests\\ui\\single_element_loop_nofix.rs']:
    with open(p, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    new_lines = []
    for i, line in enumerate(lines):
        if '//~^ single_element_loop' in line and i > 0 and lines[i-1].strip() == '{':
            new_lines.append(line.replace('//~^ single_element_loop', '//~^^ single_element_loop'))
        else:
            new_lines.append(line)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.writelines(new_lines)
print("Updated single_element_loop files")
