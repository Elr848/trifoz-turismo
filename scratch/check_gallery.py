import re

def check():
    with open("index.html", encoding="utf-8") as f:
        html = f.read()

    # Find the gallery section
    gallery_section = re.search(r'<section[^>]*class="[^"]*galeria-franja[^"]*"[^>]*>.*?</section>', html, re.DOTALL)
    if gallery_section:
        print("=== Gallery Section Found ===")
        slides = re.findall(r'<div class="galeria-slide".*?</div>\s*</div>', gallery_section.group(0), re.DOTALL)
        print(f"Number of slides found: {len(slides)}")
        for i, slide in enumerate(slides[:3]):
            print(f"Slide {i}: {slide[:300].strip()}...")
    else:
        # Let's search for any galeria-slide
        slides = re.findall(r'<div class="galeria-slide".*?</div>', html, re.DOTALL)
        print(f"Number of galeria-slides: {len(slides)}")
        for i, slide in enumerate(slides):
            img = re.search(r'<img[^>]+src="([^"]+)"[^>]*>', slide)
            img_src = img.group(1) if img else "No image tag"
            loading = "loading" in slide
            print(f"Slide {i}: {img_src} | Has loading attr: {loading}")

if __name__ == "__main__":
    check()
