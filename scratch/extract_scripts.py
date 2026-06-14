import subprocess
import difflib

def get_js_block(file_content):
    # Find the script block that contains 'gsap' and starts after the body tag
    lines = file_content.splitlines()
    block_start = -1
    for idx, line in enumerate(lines):
        if '<script>' in line and idx > 2000:
            # Check if this script block has gsap inside it
            content_sample = "\n".join(lines[idx:idx+250])
            if 'gsap' in content_sample or 'carousel' in content_sample:
                block_start = idx
                break
    if block_start == -1:
        # Try finding by 'gsap.registerPlugin'
        for idx, line in enumerate(lines):
            if 'gsap.registerPlugin' in line:
                # search upwards for <script>
                for j in range(idx, 0, -1):
                    if '<script>' in lines[j]:
                        block_start = j
                        break
                break
                
    if block_start == -1:
        return []
        
    block_end = -1
    for idx in range(block_start, len(lines)):
        if '</script>' in lines[idx]:
            block_end = idx
            break
            
    if block_end == -1:
        return lines[block_start:block_start+500]
    return lines[block_start:block_end+1]

# Get file content from git
res_orig = subprocess.run(['git', 'show', '9bfee93:index.html'], capture_output=True, text=True, encoding='utf-8', errors='ignore')
res_curr = subprocess.run(['git', 'show', 'HEAD:index.html'], capture_output=True, text=True, encoding='utf-8', errors='ignore')

orig_js = get_js_block(res_orig.stdout)
curr_js = get_js_block(res_curr.stdout)

with open('scratch/js_orig.js', 'w', encoding='utf-8') as f:
    f.write("\n".join(orig_js))
with open('scratch/js_curr.js', 'w', encoding='utf-8') as f:
    f.write("\n".join(curr_js))

print(f"Extracted original JS: {len(orig_js)} lines")
print(f"Extracted current JS: {len(curr_js)} lines")

# Diff them
diff = difflib.unified_diff(orig_js, curr_js, fromfile='9bfee93:js', tofile='HEAD:js', lineterm='')
diff_content = "\n".join(list(diff))
with open('scratch/js_diff.diff', 'w', encoding='utf-8') as f:
    f.write(diff_content)

print(f"Diff written to scratch/js_diff.diff (size: {len(diff_content)} bytes)")
