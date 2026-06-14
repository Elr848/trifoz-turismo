import re
import sys

def parse_diff(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    hunks = re.split(r'^@@', content, flags=re.MULTILINE)
    
    output = []
    output.append(f"Total hunks: {len(hunks)}")
    
    for idx, hunk in enumerate(hunks[1:], 1):
        lines = hunk.splitlines()
        header = lines[0]
        added = [l for l in lines if l.startswith('+') and not l.startswith('+++')]
        deleted = [l for l in lines if l.startswith('-') and not l.startswith('---')]
        
        output.append(f"\nHunk {idx}: @@ {header}")
        output.append(f"Added {len(added)} lines, Deleted {len(deleted)} lines")
        if len(deleted) > 0:
            output.append("Deleted sample:")
            for l in deleted[:15]:
                output.append("   " + l)
        if len(added) > 0:
            output.append("Added sample:")
            for l in added[:15]:
                output.append("   " + l)
                
    with open('scratch/diff_summary.txt', 'w', encoding='utf-8') as out_f:
        out_f.write("\n".join(output))

if __name__ == '__main__':
    parse_diff('scratch/diff_utf8.diff')
