with open('scratch/js_diff.diff', 'r', encoding='utf-8', errors='ignore') as f:
    diff_lines = f.readlines()

print("Carousel logic diff sections:")
hunk_header = ""
for line in diff_lines:
    if line.startswith('@@'):
        hunk_header = line.strip()
    if any(k in line for k in ['carousel', 'Draggable', 'cards3D', 'openLightbox', 'currentIndex']):
        if hunk_header:
            print(f"\n{hunk_header}")
            hunk_header = ""
        print(line.strip())
