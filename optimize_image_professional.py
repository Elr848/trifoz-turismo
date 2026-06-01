#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
OPTIMIZACIÓN PROFESIONAL DE IMÁGENES - NIVEL DISEÑO
Mejora calidad para celular y desktop con upscaling inteligente
"""

from PIL import Image, ImageEnhance, ImageFilter
import os
from pathlib import Path

def upscale_image(img, target_width=1920):
    """
    Upscaling inteligente de imagen con filtro de calidad
    """
    original_size = img.size
    
    # Si la imagen es muy pequeña, hacer upscaling
    if original_size[0] < target_width:
        ratio = target_width / original_size[0]
        new_size = (int(original_size[0] * ratio), int(original_size[1] * ratio))
        
        # Upscaling con LANCZOS para máxima calidad
        img = img.resize(new_size, Image.Resampling.LANCZOS)
        print(f"✓ Upscaling: {original_size} → {new_size}")
    
    return img

def reduce_noise_and_enhance(img):
    """
    Reduce pixelación/ruido y mejora la imagen
    """
    # Aplicar filtro de suavizado ligero para reducir ruido
    img = img.filter(ImageFilter.SMOOTH)
    
    # Mejorar nitidez (unsharp mask simulado)
    img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    
    return img

def enhance_colors(img):
    """
    Mejora brillo, contraste y saturación de manera profesional
    """
    # BRILLO: +20% para que sea visible en celular
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.20)
    
    # CONTRASTE: +25% para mayor definición
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.25)
    
    # SATURACIÓN: +15% para colores más vivos
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.15)
    
    # NITIDEZ: +30%
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(1.30)
    
    return img

def create_responsive_versions(input_path, output_dir):
    """
    Crea versiones responsivas: mobile, tablet, desktop
    """
    # Cargar imagen original
    img = Image.open(input_path)
    
    print("=" * 60)
    print("🎨 OPTIMIZACIÓN PROFESIONAL DE IMÁGENES")
    print("=" * 60)
    print(f"📷 Imagen original: {img.size}")
    
    # PASO 1: Upscaling
    img = upscale_image(img, target_width=1920)
    
    # PASO 2: Reducir ruido y pixelación
    print("✓ Reduciendo pixelación y ruido...")
    img = reduce_noise_and_enhance(img)
    
    # PASO 3: Mejorar colores profesionalmente
    print("✓ Mejorando brillo, contraste y saturación...")
    img = enhance_colors(img)
    
    # PASO 4: Crear versiones responsivas
    versiones = {
        'mobile': (750, 420),      # Celular - Optimizado para pantallas pequeñas
        'tablet': (1200, 675),     # Tablet - Resolución media
        'desktop': (1920, 1080),   # Desktop - Full HD
    }
    
    print("\n📱 Creando versiones responsivas:\n")
    
    for version_name, size in versiones.items():
        # Crear versión redimensionada
        img_resized = img.copy()
        
        # Calcular aspect ratio correctamente
        aspect_ratio = img.width / img.height
        target_width, target_height = size
        target_aspect = target_width / target_height
        
        if aspect_ratio > target_aspect:
            # Imagen es más ancha
            new_width = int(target_height * aspect_ratio)
            img_resized = img_resized.resize((new_width, target_height), Image.Resampling.LANCZOS)
            # Crop al centro
            crop_left = (new_width - target_width) // 2
            img_resized = img_resized.crop((crop_left, 0, crop_left + target_width, target_height))
        else:
            # Imagen es más alta
            new_height = int(target_width / aspect_ratio)
            img_resized = img_resized.resize((target_width, new_height), Image.Resampling.LANCZOS)
            # Crop al centro
            crop_top = (new_height - target_height) // 2
            img_resized = img_resized.crop((0, crop_top, target_width, crop_top + target_height))
        
        # Guardar en JPEG (calidad 92 para web)
        jpeg_path = os.path.join(output_dir, f'hero_principal_{version_name}.jpg')
        img_resized.save(jpeg_path, 'JPEG', quality=92, optimize=True)
        print(f"✓ {version_name.upper():10} (JPEG): {size[0]}x{size[1]} → {jpeg_path.split(chr(92))[-1]}")
        
        # Guardar en WebP (calidad 85 para web moderno)
        webp_path = os.path.join(output_dir, f'hero_principal_{version_name}.webp')
        img_resized.save(webp_path, 'WEBP', quality=85)
        print(f"✓ {version_name.upper():10} (WEBP): {size[0]}x{size[1]} → {webp_path.split(chr(92))[-1]}\n")
    
    # Guardar versión Full HD también como imagen principal mejorada
    main_hd = os.path.join(output_dir, 'hero_principal.jpg')
    img_desktop = img.copy()
    img_desktop.thumbnail((1920, 1080), Image.Resampling.LANCZOS)
    img_desktop.save(main_hd, 'JPEG', quality=95, optimize=True)
    print(f"✓ PRINCIPAL (JPEG): Full HD mejorada → hero_principal.jpg\n")
    
    print("=" * 60)
    print("✅ OPTIMIZACIÓN COMPLETADA")
    print("=" * 60)
    print("\n📋 MEJORAS APLICADAS:")
    print("  ✓ Upscaling inteligente (si era necesario)")
    print("  ✓ Reducción de pixelación y ruido")
    print("  ✓ Brillo: +20% (perfecto para celular)")
    print("  ✓ Contraste: +25% (mayor definición)")
    print("  ✓ Saturación: +15% (colores vivos)")
    print("  ✓ Nitidez: +30% (mayor claridad)")
    print("  ✓ Versiones responsivas (mobile/tablet/desktop)")
    print("  ✓ Formatos modernos (JPEG + WebP)")
    print("=" * 60)

if __name__ == "__main__":
    input_image = r"c:\Users\luisr\OneDrive\Desktop\trifoz-turismo\images\hero_principal.jpg"
    output_dir = r"c:\Users\luisr\OneDrive\Desktop\trifoz-turismo\images"
    
    if os.path.exists(input_image):
        create_responsive_versions(input_image, output_dir)
    else:
        print(f"❌ Error: No se encontró {input_image}")
