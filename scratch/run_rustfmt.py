import os
import subprocess

rustfmt = os.path.abspath(r'build/x86_64-pc-windows-msvc/stage1-tools-bin/rustfmt.exe')
env = os.environ.copy()
stage1_bin = os.path.abspath(r'build/x86_64-pc-windows-msvc/stage1/bin')
stage1_lib = os.path.abspath(r'build/x86_64-pc-windows-msvc/stage1/lib/rustlib/x86_64-pc-windows-msvc/lib')
env['PATH'] = f"{stage1_bin};{stage1_lib};" + env.get('PATH', '')

target = os.path.abspath(r'scratch/test_full_lafs_matrix.rs')
res = subprocess.run([rustfmt, '--check', target], env=env, capture_output=True, text=True)
print("Returncode:", res.returncode)
if res.stdout:
    print("--- STDOUT ---")
    print(res.stdout[:2000])
if res.stderr:
    print("--- STDERR ---")
    print(res.stderr[:2000])
