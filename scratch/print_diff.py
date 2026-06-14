import subprocess

def main():
    # Run git diff between 8b97b1e and 12adfc4 for index.html
    result = subprocess.run(
        ['git', 'diff', '8b97b1e..12adfc4', 'index.html'],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    with open('scratch/diff_utf8.diff', 'w', encoding='utf-8') as f:
        f.write(result.stdout)
    print("Diff written successfully")

if __name__ == '__main__':
    main()
