import shutil, os, subprocess

src_dir = r'build\x86_64-pc-windows-msvc\stage1-tools-bin'
dst_dir = r'build\x86_64-pc-windows-msvc\stage1\bin'

tools = [
    'rustfmt.exe',
    'cargo-fmt.exe',
    'clippy-driver.exe',
    'cargo-clippy.exe',
]

for t in tools:
    s = os.path.join(src_dir, t)
    d = os.path.join(dst_dir, t)
    print(f"Copying {s} -> {d}")
    shutil.copy2(s, d)

# Also check rustdoc
rustdoc_src = os.path.join(src_dir, 'rustdoc_tool_binary.exe')
if os.path.exists(rustdoc_src):
    rustdoc_dst = os.path.join(dst_dir, 'rustdoc.exe')
    print(f"Copying {rustdoc_src} -> {rustdoc_dst}")
    shutil.copy2(rustdoc_src, rustdoc_dst)

print("Copy complete!")
