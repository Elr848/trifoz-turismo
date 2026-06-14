import subprocess

def check_preloads():
    for fpath in ['index.html', 'index-pt.html']:
        res = subprocess.run(['git', 'show', f'9bfee93:{fpath}'], capture_output=True, text=True, encoding='utf-8')
        lines = res.stdout.splitlines()
        print(f"=== {fpath} preloads ===")
        for idx, line in enumerate(lines[:50]):
            if 'preload' in line:
                print(f"  L{idx+1}: {line}")

if __name__ == '__main__':
    check_preloads()
