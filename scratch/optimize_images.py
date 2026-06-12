from PIL import Image
import os

def compress_image(src, dest, max_size=(1600, 1600), quality=80):
    if not os.path.exists(src):
        print(f"Source not found: {src}")
        return False
    try:
        img = Image.open(src)
        # Convert RGBA to RGB if saving as JPEG or WebP without transparency
        if img.mode in ('RGBA', 'LA') and not dest.endswith('.png'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3]) # 3 is the alpha channel
            img = background
        elif img.mode == 'P':
            img = img.convert('RGB')
            
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        # Save as webp or jpeg
        if dest.endswith('.webp'):
            img.save(dest, 'WEBP', quality=quality)
        else:
            img.save(dest, 'JPEG', quality=quality, optimize=True)
            
        original_sz = os.path.getsize(src) / 1024
        new_sz = os.path.getsize(dest) / 1024
        print(f"Compressed {src} ({original_sz:.1f} KB) -> {dest} ({new_sz:.1f} KB) | Saved {original_sz - new_sz:.1f} KB ({(1 - new_sz/original_sz)*100:.1f}%)")
        return True
    except Exception as e:
        print(f"Error compressing {src}: {e}")
        return False

def main():
    targets = [
        ("images/pda.png", "images/pda.webp"),
        ("images/templo budista 1.png", "images/templo_budista.webp"),
        ("images/museo de cera.png", "images/museo_de_cera.webp"),
        ("images/cataratas_panorama.png", "images/cataratas_panorama.webp"),
        ("images/plataforma.jpeg", "images/plataforma_opt.jpg")
    ]
    for src, dest in targets:
        compress_image(src, dest)

if __name__ == "__main__":
    main()
