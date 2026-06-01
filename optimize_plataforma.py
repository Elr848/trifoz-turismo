#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
OPTIMIZACIÓN PROFESIONAL - IMAGEN PLATAFORMA MEJORADA
"""

from PIL import Image, ImageEnhance, ImageFilter
import os

def upscale_image(img, target_width=1920):
    """Upscaling inteligente"""
    original_size = img.size
    if original_size[0] < target_width:
        ratio = target_width / original_size[0]
        new_size = (int(original_size[0] * ratio), int(original_size[1] * ratio))
        img = img.resize(new_size, Image.Resampling.LANCZOS)
        print(f"✓ Upscaling: {original_size} → {new_size}")
    return img

def reduce_noise_and_enhance(img):
    """Reduce pixelación y ruido"""
    img = img.filter(ImageFilter.SMOOTH)
    img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    return img

def enhance_colors(img):
    """Mejora brillo y contraste"""
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.20)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.25)
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.15)
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(1.30)
    return img

def create_responsive_versions(input_path, output_dir, base_name):
    """Crea versiones responsivas"""
    img = Image.open(input_path)
    
    print("=" * 60)
    print(f"🎨 OPTIMIZANDO: {base_name}")
    print("=" * 60)
    print(f"📷 Original: {img.size}")
    
    img = upscale_image(img, target_width=1920)
    print("✓ Reduciendo pixelación...")
    img = reduce_noise_and_enhance(img)
    print("✓ Mejorando colores...")
    img = enhance_colors(img)
    
    print("\n📱 Versiones responsivas:\n")
    
    versiones = {
        'mobile': (750, 420),
        'tablet': (1200, 675),
        'desktop': (1920, 1080),
    }
    
    for version_name, size in versiones.items():
        img_resized = img.copy()
        aspect_ratio = img.width / img.height
        target_width, target_height = size
        target_aspect = target_width / target_height
        
        if aspect_ratio > target_aspect:
            new_width = int(target_height * aspect_ratio)
            img_resized = img_resized.resize((new_width, target_height), Image.Resampling.LANCZOS)
            crop_left = (new_width - target_width) // 2
            img_resized = img_resized.crop((crop_left, 0, crop_left + target_width, target_height))
        else:
            new_height = int(target_width / aspect_ratio)
            img_resized = img_resized.resize((target_width, new_height), Image.Resampling.LANCZOS)
            crop_top = (new_height - target_height) // 2
            img_resized = img_resized.crop((0, crop_top, target_width, crop_top + target_height))
        
        jpeg_path = os.path.join(output_dir, f'{base_name}_{version_name}.jpg')
        img_resized.save(jpeg_path, 'JPEG', quality=92, optimize=True)
        print(f"✓ {version_name.upper():10} (JPEG): {size[0]}x{size[1]}")
        
        webp_path = os.path.join(output_dir, f'{base_name}_{version_name}.webp')
        img_resized.save(webp_path, 'WEBP', quality=85)
        print(f"✓ {version_name.upper():10} (WEBP): {size[0]}x{size[1]}\n")
    
    print("=" * 60)
    print("✅ OPTIMIZACIÓN COMPLETADA")
    print("=" * 60)

if __name__ == "__main__":
    input_image = r"c:\Users\luisr\OneDrive\Desktop\trifoz-turismo\images\plataforma mejorada.jpg"
    output_dir = r"c:\Users\luisr\OneDrive\Desktop\trifoz-turismo\images"
    
    if os.path.exists(input_image):
        create_responsive_versions(input_image, output_dir, "plataforma_mejorada")
    else:
        print(f"❌ No encontrada: {input_image}")
