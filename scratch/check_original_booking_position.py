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
    # Print lines from 2370 to 2410
    output.append("=== lines 2370 to 2410 ===")
    for idx in range(2370, 2410):
        if idx < len(lines):
            output.append(f"{idx+1}: {lines[idx]}")
            
    with open('scratch/check_original_booking_position.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(output))

if __name__ == '__main__':
    main()
