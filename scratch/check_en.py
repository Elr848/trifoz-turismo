def main():
    with open('index-en.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to check if any Spanish words are still left in key elements
    keywords = [
        '¿A dónde vas?',
        'Necesito ayuda',
        'Cataratas de Iguazú',
        'Parque de las Aves',
        'Hito de las 3 Fronteras',
        'Hito de las Tres Fronteras',
        'Itaipú Binacional',
        'Rueda Gigante',
        'Roda Gigante',
        'Museo de Cera',
        'Aeropuerto de',
        'Traslado para Hoteles',
        'MÁS INFORMACIÓN',
        'Fecha & Hora',
        'Fecha y Hora',
        'SOLICITAR CONSULTA',
        'Hacer una consulta'
    ]
    
    for kw in keywords:
        count = content.count(kw)
        if count > 0:
            print(f'Found "{kw}" {count} times')
        else:
            print(f'Clean: "{kw}"')

if __name__ == '__main__':
    main()
