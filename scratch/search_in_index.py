with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

words = ['dragProxy', 'Draggable', 'carousel', 'openLightbox', 'imagesList']
for word in words:
    count = content.lower().count(word.lower())
    print(f"Word '{word}' count: {count}")
    if count > 0:
        print(f"Lines matching '{word}':")
        for i, line in enumerate(content.splitlines()):
            if word.lower() in line.lower():
                print(f"  L{i+1}: {line.strip()[:100]}")
