with open('scratch/carousel_orig.js', 'r', encoding='utf-8', errors='ignore') as f:
    orig = f.read()
with open('scratch/carousel_curr.js', 'r', encoding='utf-8', errors='ignore') as f:
    curr = f.read()

print("Occurrences in orig:")
for i, line in enumerate(orig.splitlines()):
    if 'dragProxy3D' in line:
        print(f"  L{i+1}: {line}")

print("\nOccurrences in curr:")
for i, line in enumerate(curr.splitlines()):
    if 'dragProxy3D' in line:
        print(f"  L{i+1}: {line}")
