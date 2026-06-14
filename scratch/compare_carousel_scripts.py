import subprocess

def get_script_carousel(commit):
    res = subprocess.run(['git', 'show', f'{commit}:index.html'], capture_output=True, text=True, encoding='utf-8', errors='ignore')
    lines = res.stdout.splitlines()
    start = -1
    for idx, line in enumerate(lines):
        if 'CARRUSEL 3D COVERFLOW' in line or 'LOGICA DEL CARRUSEL 3D' in line:
            start = idx
            break
    if start == -1:
        return ""
    end = -1
    for idx in range(start, len(lines)):
        if '</script>' in lines[idx]:
            end = idx
            break
    if end == -1:
        return "\n".join(lines[start:start+200])
    return "\n".join(lines[start:end])

def main():
    orig = get_script_carousel('9bfee93')
    curr = get_script_carousel('HEAD')
    
    with open('scratch/carousel_orig.js', 'w', encoding='utf-8') as f:
        f.write(orig)
    with open('scratch/carousel_curr.js', 'w', encoding='utf-8') as f:
        f.write(curr)
        
    print("Carousel scripts written. Running diff...")
    res = subprocess.run(['git', 'diff', '--no-index', 'scratch/carousel_orig.js', 'scratch/carousel_curr.js'], capture_output=True, text=True, encoding='utf-8', errors='ignore')
    with open('scratch/carousel_diff.diff', 'w', encoding='utf-8') as f:
        f.write(res.stdout)
    print("Diff written to scratch/carousel_diff.diff")

if __name__ == '__main__':
    main()
