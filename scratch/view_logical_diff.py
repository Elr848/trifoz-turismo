import re

def analyze_large_diff():
    with open('scratch/diff_functional_head.diff', 'r', encoding='utf-8') as f:
        diff_text = f.read()
    
    hunks = re.split(r'^@@ ', diff_text, flags=re.MULTILINE)
    
    output = []
    output.append(f"Total hunks since 9bfee93: {len(hunks)}")
    
    css_changes = 0
    js_changes = 0
    html_changes = 0
    
    for idx, hunk in enumerate(hunks[1:], 1):
        lines = hunk.splitlines()
        header = lines[0]
        
        m = re.match(r'-(\d+),\d+ \+(\d+),\d+', header)
        orig_line = int(m.group(1)) if m else 0
        new_line = int(m.group(2)) if m else 0
        
        category = "HTML"
        if new_line < 2500:
            category = "CSS"
            css_changes += 1
        elif new_line > 3000:
            category = "JS"
            js_changes += 1
        else:
            html_changes += 1
            
        added = [l for l in lines if l.startswith('+') and not l.startswith('+++')]
        deleted = [l for l in lines if l.startswith('-') and not l.startswith('---')]
        
        if len(added) > 0 or len(deleted) > 0:
            output.append(f"\nHunk {idx} [{category}] (Original Line: {orig_line}, New Line: {new_line}):")
            output.append(f"  Added {len(added)} lines, Deleted {len(deleted)} lines")
            if len(deleted) > 0:
                output.append("  Deleted:")
                for l in deleted[:6]:
                    output.append("     " + l)
            if len(added) > 0:
                output.append("  Added:")
                for l in added[:6]:
                    output.append("     " + l)

    output.append(f"\nSummary of changes: CSS={css_changes}, HTML={html_changes}, JS={js_changes}")
    
    with open('scratch/logical_diff_summary.txt', 'w', encoding='utf-8') as out_f:
        out_f.write("\n".join(output))

if __name__ == '__main__':
    analyze_large_diff()
