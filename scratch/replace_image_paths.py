import re

replacements = {
    "images/pda.png": "images/pda.webp",
    "images/templo budista 1.png": "images/templo_budista.webp",
    "images/mezquita 1.png": "images/mezquita1.jpg",
    "images/china 1.png": "images/china.webp",
    "images/museo de cera.png": "images/museo_de_cera.webp",
    "images/cataratas_panorama.png": "images/cataratas_panorama.webp",
    "images/plataforma.jpeg": "images/plataforma_opt.jpg"
}

def replace_in_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False
    for old_val, new_val in replacements.items():
        if old_val in content:
            content = content.replace(old_val, new_val)
            print(f"  Replaced '{old_val}' with '{new_val}'")
            modified = True
            
    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Saved changes to {filepath}.")
    else:
        print(f"No replacements needed for {filepath}.")

if __name__ == "__main__":
    replace_in_file("index.html")
    replace_in_file("index-pt.html")
