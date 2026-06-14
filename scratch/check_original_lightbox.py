import subprocess

def check_original_lightbox():
    result = subprocess.run(
        ['git', 'show', '9bfee93:index.html'],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    lines = result.stdout.splitlines()
    for i, line in enumerate(lines):
        if 'function openLightbox' in line:
            print(f"Found openLightbox at L{i+1}")
            print("\n".join(lines[i:i+20]))
            break

if __name__ == '__main__':
    check_original_lightbox()
