import os
import subprocess

rustc = os.path.abspath(r'build/x86_64-pc-windows-msvc/stage1/bin/rustc.exe')
env = os.environ.copy()
stage1_bin = os.path.abspath(r'build/x86_64-pc-windows-msvc/stage1/bin')
stage1_lib = os.path.abspath(r'build/x86_64-pc-windows-msvc/stage1/lib/rustlib/x86_64-pc-windows-msvc/lib')
env['PATH'] = f"{stage1_bin};{stage1_lib};" + env.get('PATH', '')

target = os.path.abspath(r'scratch/test_full_lafs_matrix.rs')
out_exe = os.path.abspath(r'scratch/test_full_lafs_matrix.exe')
res = subprocess.run([rustc, target, '-o', out_exe], env=env, capture_output=True, text=True)
print("Rustc Returncode:", res.returncode)
if res.stderr:
    print("Rustc Stderr:", res.stderr)

if res.returncode == 0:
    run_res = subprocess.run([out_exe], env=env, capture_output=True, text=True)
    print("Execution Returncode:", run_res.returncode)
    print("Execution Stdout:", run_res.stdout)
    if run_res.stderr:
        print("Execution Stderr:", run_res.stderr)
