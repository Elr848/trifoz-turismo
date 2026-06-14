import subprocess

def main():
    # Show index.html at 8b97b1e
    result = subprocess.run(
        ['git', 'show', '8b97b1e:index.html'],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    lines = result.stdout.splitlines()
    for i, line in enumerate(lines):
        if 'class="carousel-3d-wrapper"' in line:
            start = i
            end = i + 100
            print("\n".join(lines[start:end]))
            break

if __name__ == '__main__':
    main()
