import subprocess
import re
import difflib

def get_style_block(content):
    style_match = re.search(r'<style\b[^>]*>(.*?)</style>', content, re.DOTALL)
    if not style_match:
        return []
    style_content = style_match.group(1)
    
    # Extract only lines matching carousel/slider/3d/card
    lines = style_content.splitlines()
    matching_lines = []
    in_block = False
    block_braces = 0
    
    for line in lines:
        if '.slider-container-3d' in line or '.carousel-' in line or '.card-item-3d' in line or '.card-back' in line:
            in_block = True
        if in_block:
            matching_lines.append(line)
            block_braces += line.count('{') - line.count('}')
            if block_braces <= 0 and '}' in line:
                in_block = False
                block_braces = 0
    return matching_lines

res_orig = subprocess.run(['git', 'show', '9bfee93:index.html'], capture_output=True, text=True, encoding='utf-8', errors='ignore')
res_curr = subprocess.run(['git', 'show', 'HEAD:index.html'], capture_output=True, text=True, encoding='utf-8', errors='ignore')

orig_styles = get_style_block(res_orig.stdout)
curr_styles = get_style_block(res_curr.stdout)

print(f"Original styles matching: {len(orig_styles)} lines")
print(f"Current styles matching: {len(curr_styles)} lines")

diff = difflib.unified_diff(orig_styles, curr_styles, fromfile='9bfee93:styles', tofile='HEAD:styles', lineterm='')
with open('scratch/styles_diff.diff', 'w', encoding='utf-8') as f:
    f.write("\n".join(list(diff)))
print("Diff written to scratch/styles_diff.diff")
