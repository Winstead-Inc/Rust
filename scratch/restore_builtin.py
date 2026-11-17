with open('compiler/rustc_lint_defs/src/builtin.rs', 'r', encoding='utf-8') as f:
    s = f.read()

# restore raw string closings
s = s.replace('" # ,', '"#,')
s = s.replace('" #\n', '"#\n')
s = s.replace('" # ;', '"#;')

# ensure line 1638 has space
s = s.replace('"the behavior may change in a future release"#', '"the behavior may change in a future release" #')

with open('compiler/rustc_lint_defs/src/builtin.rs', 'w', encoding='utf-8') as f:
    f.write(s)

print('Restored raw strings in builtin.rs')

