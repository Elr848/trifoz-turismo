import subprocess

def main():
    result = subprocess.run(
        ['git', 'show', '9bfee93:index.html'],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    lines = result.stdout.splitlines()
    found = False
    for i, line in enumerate(lines):
        if 'id="btnOtrasAtracciones"' in line:
            found = True
            print(f"Found HTML accordion at line {i+1}")
            print("\n".join(lines[max(0, i-5):i+50]))
            break
    if not found:
        print("HTML accordion not found in 9bfee93")

if __name__ == '__main__':
    main()
