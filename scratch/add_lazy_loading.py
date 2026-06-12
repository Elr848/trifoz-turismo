import re

def add_lazy_to_gallery(filepath):
    print(f"Adding lazy loading to {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Find the gallery block
    # We want to find each <div class="galeria-slide"> (without active) and add loading="lazy" to its img tag.
    # Pattern to match galeria-slide without 'active'
    
    parts = re.split(r'(<div class="galeria-slide">)', html)
    modified = False
    
    if len(parts) > 1:
        new_html = parts[0]
        for i in range(1, len(parts), 2):
            slide_header = parts[i]
            slide_body = parts[i+1]
            
            # Find the first <img> tag inside this slide body and add loading="lazy" if not already present
            img_match = re.search(r'<img\s+([^>]+)>', slide_body)
            if img_match:
                img_attributes = img_match.group(1)
                if 'loading="lazy"' not in img_attributes:
                    new_attributes = img_attributes + ' loading="lazy"'
                    slide_body = slide_body.replace(img_match.group(0), f'<img {new_attributes}>', 1)
                    modified = True
            
            new_html += slide_header + slide_body
        html = new_html

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Successfully added loading=\"lazy\" to gallery images in {filepath}.")
    else:
        print(f"No changes made to {filepath}.")

if __name__ == "__main__":
    add_lazy_to_gallery("index.html")
    add_lazy_to_gallery("index-pt.html")
