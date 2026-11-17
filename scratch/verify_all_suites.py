import subprocess
import sys

suites = [
    'if_not_else',
    'entry',
    'question_mark',
    'manual_ok_err',
    'single_element_loop',
    'unit_arg',
]

all_passed = True
for s in suites:
    print(f"\n=================== TESTING: {s} ===================")
    cmd = [sys.executable, 'x.py', 'test', 'src/tools/clippy', '--test-args', s]
    res = subprocess.run(cmd, text=True)
    if res.returncode != 0:
        print(f"FAILED on suite: {s}")
        all_passed = False
        break
    else:
        print(f"PASSED suite: {s}")

if all_passed:
    print("\n**************************************************")
    print("ALL 6 CLIPPY TEST SUITES PASSED 100% CLEANLY!")
    print("**************************************************")
