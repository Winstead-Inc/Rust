with open('compiler/rustc_lint_defs/src/lib.rs', 'r', encoding='utf-8') as f:
    s = f.read()

s = s.replace('(FutureReleaseError# $issue_number', '(FutureReleaseError # $issue_number')
s = s.replace('(FutureReleaseSemanticsChange# $issue_number', '(FutureReleaseSemanticsChange # $issue_number')
s = s.replace('($description: literal# $issue_number', '($description: literal # $issue_number')

with open('compiler/rustc_lint_defs/src/lib.rs', 'w', encoding='utf-8') as f:
    f.write(s)

with open('compiler/rustc_lint_defs/src/builtin.rs', 'r', encoding='utf-8') as f:
    b = f.read()

b = b.replace('FutureReleaseError#', 'FutureReleaseError # ')
b = b.replace('FutureReleaseSemanticsChange#', 'FutureReleaseSemanticsChange # ')
b = b.replace('"#', '" # ')

with open('compiler/rustc_lint_defs/src/builtin.rs', 'w', encoding='utf-8') as f:
    f.write(b)

print('Updated rustc_lint_defs/src/lib.rs and builtin.rs successfully')

