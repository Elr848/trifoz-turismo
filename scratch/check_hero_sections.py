import subprocess

def main():
    result = subprocess.run(
        ['git', 'show', '9bfee93:index.html'],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    lines = result.stdout.splitlines()
    output = []
    for i, line in enumerate(lines):
        if 'class="hero"' in line or 'class=\'hero\'' in line:
            output.append(f"Hero start line: {i+1}")
            output.append("\n".join(lines[i:i+15]))
        if '</section>' in line:
            output.append(f"Section close line: {i+1}: {line}")
            
    with open('scratch/check_hero_sections_out.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(output))

if __name__ == '__main__':
    main()
