import glob

for p in ['src/tools/clippy/tests/ui/single_element_loop.rs', 'src/tools/clippy/tests/ui/single_element_loop_nofix.rs']:
    print("FILE:", p)
    try:
        with open(p, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if '//~' in line:
                print(f"  Line {i+1}: {line.strip()} (prev: {lines[i-1].strip()})")
    except Exception as e:
        print("  Error:", e)
