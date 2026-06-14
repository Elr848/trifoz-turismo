import subprocess

def check_images_list():
    result = subprocess.run(
        ['git', 'show', '9bfee93:index.html'],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    lines = result.stdout.splitlines()
    for i, line in enumerate(lines):
        if 'const imagesList' in line or 'let imagesList' in line or 'imagesList = [' in line:
            print(f"Found imagesList at L{i+1}")
            print("\n".join(lines[i:i+40]))
            break

if __name__ == '__main__':
    check_images_list()
