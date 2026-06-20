def main():
    with open('index-en.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Global translations for key terms
    replacements = {
        'Cataratas de Iguazú': 'Iguazu Falls',
        'Parque de las Aves': 'Bird Park',
        'Hito de las 3 Fronteras': 'Three Borders Landmark',
        'Hito de las Tres Fronteras': 'Three Borders Landmark',
        'Itaipú Binacional': 'Itaipu Binational',
        'Itaipú': 'Itaipu',
        'Museo de Cera': 'Dreamland Wax Museum',
        'Traslado para Hoteles': 'Hotel Transfers',
        'Rueda Gigante Yup Star': 'Yup Star Ferris Wheel',
        'Roda Gigante Yup Star': 'Yup Star Ferris Wheel',
        '¿A dónde vas?': 'Where are you going?',
        '¿A dónde vas?': 'Where are you going?', # just in case
    }
    
    for src, dst in replacements.items():
        content = content.replace(src, dst)
        
    with open('index-en.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Done fixing remaining Spanish terms in index-en.html")

if __name__ == '__main__':
    main()
