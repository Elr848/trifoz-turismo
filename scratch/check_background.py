import subprocess

def main():
    result = subprocess.run(
        ['git', 'show', '9bfee93:index.html'],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    lines = result.stdout.splitlines()
    for i, line in enumerate(lines):
        if '.slider-container-3d {' in line:
            print("\n".join(lines[i:i+25]))
            break

if __name__ == '__main__':
    main()
