import os, subprocess, re

for tool in ['cargo-clippy.exe', 'cargo-fmt.exe']:
    p = os.path.join(r'build\x86_64-pc-windows-msvc\stage1-tools-bin', tool)
    with open(p, 'rb') as f:
        data = f.read()

    dlls = set(re.findall(rb'[a-zA-Z0-9_\-\.]+\.dll', data, re.IGNORECASE))
    print("TOOL:", tool)
    for d in sorted(dlls):
        s = d.decode('ascii', errors='ignore')
        if any(k in s.lower() for k in ['std', 'rustc', 'msvc']):
            print(" ", s)
