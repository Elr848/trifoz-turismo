#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mejora de brillo y claridad - Imagen principal
Solo brillo y claridad, sin otros cambios
"""

from PIL import Image, ImageEnhance

def enhance_brightness_clarity(input_path, output_path):
    """Solo aumenta brillo y claridad de la imagen"""
    
    # Cargar con PIL para mejor control
    img = Image.open(input_path)
    print(f"Imagen original: {img.size}")
    
    # AUMENTO DE BRILLO (30%)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.30)
    
    # AUMENTO DE CLARIDAD (Contrast - 20%)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.20)
    
    # Guardar con máxima calidad
    img.save(output_path, 'JPEG', quality=95)
    
    print(f"✓ Imagen guardada")
    print(f"✓ Brillo: +30%")
    print(f"✓ Claridad: +20%")
    print(f"✓ Calidad: 95%")
    
    return True

if __name__ == "__main__":
    input_image = r"c:\Users\luisr\OneDrive\Desktop\trifoz-turismo\images\hero_principal.jpg"
    output_image = r"c:\Users\luisr\OneDrive\Desktop\trifoz-turismo\images\hero_principal.jpg"
    
    print("=" * 40)
    print("MEJORA: BRILLO Y CLARIDAD")
    print("=" * 40)
    
    enhance_brightness_clarity(input_image, output_image)
    
    print("=" * 40)
    print("✓ Completado")
