import re

def apply_pt():
    with open("index-pt.html", "r", encoding="utf-8") as f:
        html_pt = f.read()

    # Find the original destinations array from index-pt.html
    dest_match = re.search(r'const destinations = \[(.*?)\];', html_pt, re.DOTALL)
    if dest_match:
        dest_array_content = dest_match.group(1)
        print("Found original PT destinations array.")
    else:
        print("Warning: Could not find original PT destinations array.")
        return

    # Let's inspect the HTML of index-pt.html to see if we can keep its Portuguese section, but with structural updates.
    # What are the structural updates?
    # 1. Add data-src to <div class="card-item-3d">
    # 2. Add loading="lazy" to gallery slides (already done in our previous turn!)
    # 3. Replace the <script> block with the new optimized JS, but using the PT destinations array.
    
    # Let's do the script block replacement first
    # Find script block in ES (which is now updated)
    with open("index.html", "r", encoding="utf-8") as f:
        html_es = f.read()
        
    es_script_match = re.search(r'<script>(.*?)</script>', html_es, re.DOTALL)
    pt_script_match = re.search(r'<script>(.*?)</script>', html_pt, re.DOTALL)
    
    if es_script_match and pt_script_match:
        es_script = es_script_match.group(1)
        # In es_script, replace the destinations array with the PT one
        # Let's find 'const destinations = [...];' in es_script
        es_dest_pattern = re.compile(r'const destinations = \[(.*?)\];', re.DOTALL)
        new_pt_script = es_dest_pattern.sub(f"const destinations = [{dest_array_content}];", es_script)
        
        # Replace script in html_pt
        html_pt = html_pt.replace(pt_script_match.group(0), f"<script>{new_pt_script}</script>")
        print("Replaced script tag in PT file.")
    else:
        print("Error with script match.")
        return

    # Now let's update the card-item-3d elements in index-pt.html to include data-src
    # Example: <div class="card-item-3d" data-index="0"> -> <div class="card-item-3d" data-index="0" data-src="...">
    # Let's find all cards in index-pt.html and add data-src matching their background image
    card_pattern = re.compile(r'<div class="card-item-3d" data-index="(\d+)">\s*<div class="card-back" style="background: url\(\'([^\']+)\'\)', re.DOTALL)
    
    def card_repl(match):
        idx = match.group(1)
        src = match.group(2)
        return f'<div class="card-item-3d" data-index="{idx}" data-src="{src}">\n                        <div class="card-back" style="background: url(\'{src}\')'

    html_pt = card_pattern.sub(card_repl, html_pt)
    print("Updated 3D cards in PT file to include data-src.")

    with open("index-pt.html", "w", encoding="utf-8") as f:
        f.write(html_pt)
    print("PT file updated successfully!")

if __name__ == "__main__":
    apply_pt()
