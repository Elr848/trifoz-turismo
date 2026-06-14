import re
import subprocess
import os

def check_html_js(html_path):
    print(f"\nChecking JS in {html_path}...")
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Extract script tags with their attributes and contents
    script_tags = re.findall(r'<script\b([^>]*)\b>(.*?)</script>', html_content, re.DOTALL)
    
    valid_blocks = 0
    invalid_blocks = 0
    
    for idx, (attrs, content) in enumerate(script_tags):
        # Skip external scripts
        if 'src=' in attrs:
            continue
        # Skip JSON-LD
        if 'type="application/ld+json"' in attrs or 'type=\'application/ld+json\'' in attrs:
            continue
        if not content.strip():
            continue
            
        temp_js_path = f"scratch/temp_check_{idx}.js"
        with open(temp_js_path, 'w', encoding='utf-8') as js_f:
            js_f.write(content)
            
        res = subprocess.run(['node', '--check', temp_js_path], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"  [ERROR] Script block {idx} (attributes: {attrs.strip()}):")
            print(res.stderr)
            invalid_blocks += 1
        else:
            print(f"  [OK] Script block {idx} (attributes: {attrs.strip()}) is syntactically valid.")
            valid_blocks += 1
            
        try:
            os.remove(temp_js_path)
        except Exception:
            pass
            
    print(f"Summary for {html_path}: {valid_blocks} valid, {invalid_blocks} invalid.")

if __name__ == '__main__':
    check_html_js('index.html')
    check_html_js('index-pt.html')
