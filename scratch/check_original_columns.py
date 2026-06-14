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
        if 'EXPLORA FOZ DO IGUA' in line:
            output.append(f"Found at line {i+1}")
            output.append("\n".join(lines[i:i+40]))
            break
            
    with open('scratch/check_original_columns_out.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(output))

if __name__ == '__main__':
    main()
