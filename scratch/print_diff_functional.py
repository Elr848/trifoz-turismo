import subprocess

def main():
    # Run git diff between 9bfee93 and HEAD for index.html
    result = subprocess.run(
        ['git', 'diff', '9bfee93..HEAD', 'index.html'],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    with open('scratch/diff_functional_head.diff', 'w', encoding='utf-8') as f:
        f.write(result.stdout)
    print("Diff written successfully")

if __name__ == '__main__':
    main()
