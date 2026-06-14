# -*- coding: utf-8 -*-
import os
import re

def verify_file(filename):
    print(f"=== VERIFYING {filename} ===")
    if not os.path.exists(filename):
        print("File not found!")
        return
        
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 1. Check for JS syntax errors (e.g. unclosed comments, cut-off strings)
    # We check if 'acordeonConte' is still in the file
    if 'acordeonConte ' in content or 'acordeonConte  ' in content:
        print("FAIL: Found unclosed 'acordeonConte' string!")
    else:
        print("PASS: No truncated acordeonConte JS string found.")
        
    # 2. Extract and check all images
    sources = []
    for m in re.finditer(r'src=["\'](images/[^"\']+)["\']', content):
        sources.append(m.group(1))
    for m in re.finditer(r'srcset=["\'](images/[^"\']+)["\']', content):
        # Could contain commas
        for url in m.group(1).split(','):
            url = url.strip().split()[0]
            sources.append(url)
    for m in re.finditer(r'url\(["\']?(images/[^"\'\)]+)["\']?\)', content):
        sources.append(m.group(1))
        
    sources = list(set(sources))
    missing = []
    images_dir = r"c:\Users\luisr\OneDrive\Desktop\trifoz-turismo"
    for src in sorted(sources):
        full_path = os.path.join(images_dir, src.replace('/', '\\'))
        if not os.path.exists(full_path):
            missing.append(src)
            
    if missing:
        print(f"FAIL: Found {len(missing)} missing files referenced:")
        for m in missing:
            print(f"  - {m}")
    else:
        print(f"PASS: All {len(sources)} image references exist in folder.")

verify_file(r"c:\Users\luisr\OneDrive\Desktop\trifoz-turismo\index.html")
verify_file(r"c:\Users\luisr\OneDrive\Desktop\trifoz-turismo\index-pt.html")
