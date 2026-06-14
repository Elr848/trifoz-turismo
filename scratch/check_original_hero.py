import subprocess

def check_original_hero_html():
    output = []
    for fpath in ['index.html', 'index-pt.html']:
        res = subprocess.run(['git', 'show', f'9bfee93:{fpath}'], capture_output=True, text=True, encoding='utf-8')
        lines = res.stdout.splitlines()
        for idx, line in enumerate(lines):
            if 'class="hero"' in line or "class='hero'" in line:
                output.append(f"=== {fpath} ===")
                for offset in range(0, 10):
                    if idx+offset < len(lines):
                        output.append(f"  L{idx+1+offset}: {lines[idx+offset]}")
                break
                
    with open('scratch/check_original_hero_out.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(output))

if __name__ == '__main__':
    check_original_hero_html()
