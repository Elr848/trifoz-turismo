import re
import os

def analyze():
    with open("index.html", encoding="utf-8") as f:
        html = f.read()

    # Find img tags
    imgs = re.findall(r'<img\s+[^>]*src=["\']([^"\']+)["\']', html)
    # Find background images in inline styles
    bg_imgs = re.findall(r'url\([\'"]?([^\'"\)]+)[\'"]?\)', html)

    all_images = list(set(imgs + bg_imgs))
    print("=== File Size Analysis of Images ===")
    for img in sorted(all_images):
        if img.startswith("http"):
            print(f"[External] {img}")
        else:
            # clean query parameters or hashes
            clean_path = img.split("?")[0].split("#")[0]
            # convert relative to absolute/current path
            if os.path.exists(clean_path):
                sz = os.path.getsize(clean_path) / 1024
                print(f"{clean_path}: {sz:.1f} KB")
            else:
                print(f"[Not Found] {clean_path} (original: {img})")

if __name__ == "__main__":
    analyze()
