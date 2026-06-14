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
        if '.card-back {' in line:
            chunk = "\n".join(lines[i:i+25])
            print(chunk.encode('ascii', errors='ignore').decode('ascii'))
            found = True
            break
    if not found:
        print("Not found")

if __name__ == '__main__':
    main()
