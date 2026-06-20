import re

def main():
    with open('index-en.html', 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = {
        # Dropdown Triggers
        '<span>¿A dónde vas?</span>': '<span>Where are you going?</span>',
        
        # Dropdown Items - Desktop
        '✨ Necesito\n                                    ayuda con el itinerario': '✨ I need help with the itinerary',
        'data-value="Cataratas de Iguazú (Brasil)"': 'data-value="Iguazu Falls (Brazil)"',
        'Cataratas de Iguazú (Brasil)</li>': 'Iguazu Falls (Brazil)</li>',
        'data-value="Iguazu Falls (Argentina)"': 'data-value="Iguazu Falls (Argentina)"',
        'Iguazu Falls (Arg)</li>': 'Iguazu Falls (Argentina)</li>',
        'data-value="Parque de las Aves"': 'data-value="Bird Park"',
        '🦜 Parque de las Aves</li>': '🦜 Bird Park</li>',
        'data-value="Hito de las 3 Fronteras"': 'data-value="Three Borders Landmark"',
        '🏛️ Hito de las 3\n                                    Fronteras</li>': '🏛️ Three Borders Landmark</li>',
        'data-value="Itaipú Binacional"': 'data-value="Itaipu Binacional"',
        '⚡ Itaipú Binacional</li>': '⚡ Itaipu Binacional</li>',
        'data-value="Macuco Safari"': 'data-value="Macuco Safari"',
        '🚤 Macuco Safari</li>': '🚤 Macuco Safari</li>',
        'data-value="Roda Gigante Yup Star"': 'data-value="Yup Star Ferris Wheel"',
        '🎡 Rueda Gigante Yup Star\n                                </li>': '🎡 Yup Star Ferris Wheel</li>',
        'data-value="Museo de Cera Dreamland"': 'data-value="Dreamland Wax Museum"',
        '🎭 Museo de Cera\n                                    Dreamland</li>': '🎭 Dreamland Wax Museum</li>',
        'data-value="Ciudad del Este (Paraguay)"': 'data-value="Ciudad del Este (Paraguay)"',
        'class="country-tag">PY</span> Ciudad del Este</li>': 'class="country-tag">PY</span> Ciudad del Este (Paraguay)</li>',
        
        'data-value="Aeropuerto de Foz de Iguazú"': 'data-value="Foz do Iguaçu Airport"',
        'Aeropuerto de Foz de Iguazú</li>': 'Foz do Iguaçu Airport</li>',
        'data-value="Aeropuerto de Puerto Iguazú"': 'data-value="Puerto Iguazú Airport"',
        'Aeropuerto de Puerto Iguazú</li>': 'Puerto Iguazú Airport</li>',
        'data-value="Aeropuerto de Ciudad del Este"': 'data-value="Ciudad del Este Airport"',
        'Aeropuerto de Ciudad del Este</li>': 'Ciudad del Este Airport</li>',
        'data-value="Traslado para Hoteles"': 'data-value="Hotel Transfers"',
        '🏨 Traslado para Hoteles\n                                    (BR / AR / PY)</li>': '🏨 Hotel Transfers (BR / AR / PY)</li>',
        
        # Dropdown Items - Mobile
        'Necesito ayuda con\n                            el itinerario': 'I need help with the itinerary',
        'data-value="Cataratas de Iguazú (Brasil)">Cataratas de Iguazú (Brasil)': 'data-value="Iguazu Falls (Brazil)">Iguazu Falls (Brazil)',
        'data-value="Iguazu Falls (Argentina)">Iguazu Falls\n                            (Arg)</li>': 'data-value="Iguazu Falls (Argentina)">Iguazu Falls (Argentina)</li>',
        'data-value="Parque de las Aves">Parque de las Aves</li>': 'data-value="Bird Park">Bird Park</li>',
        'data-value="Hito de las Tres Fronteras">Hito de las 3 Fronteras</li>': 'data-value="Three Borders Landmark">Three Borders Landmark</li>',
        'data-value="Itaipú Binacional">Itaipú Binacional</li>': 'data-value="Itaipu Binacional">Itaipu Binacional</li>',
        'data-value="Macuco Safari">Macuco Safari</li>': 'data-value="Macuco Safari">Macuco Safari</li>',
        'data-value="Ciudad del Este">Ciudad del Este (Paraguay)</li>': 'data-value="Ciudad del Este (Paraguay)">Ciudad del Este (Paraguay)</li>',
        'data-value="Aeropuerto de Foz de Iguazú">✈️ <span\n                                class="country-tag">BR</span> Aeropuerto de Foz de Iguazú</li>': 'data-value="Foz do Iguaçu Airport">✈️ <span class="country-tag">BR</span> Foz do Iguaçu Airport</li>',
        'data-value="Aeropuerto de Puerto Iguazú">✈️ <span\n                                class="country-tag">AR</span> Aeropuerto de Puerto Iguazú</li>': 'data-value="Puerto Iguazú Airport">✈️ <span class="country-tag">AR</span> Puerto Iguazú Airport</li>',
        'data-value="Aeropuerto de Ciudad del Este">✈️ <span\n                                class="country-tag">PY</span> Aeropuerto de Ciudad del Este</li>': 'data-value="Ciudad del Este Airport">✈️ <span class="country-tag">PY</span> Ciudad del Este Airport</li>',
        'data-value="Traslado para Hoteles">🏨 Traslado para Hoteles (BR / AR /\n                            PY)</li>': 'data-value="Hotel Transfers">🏨 Hotel Transfers (BR / AR / PY)</li>',
        
        # DateTime & Buttons
        '<span class="booking-field-label">Fecha &amp; Hora</span>': '<span class="booking-field-label">Date &amp; Time</span>',
        '<span class="booking-mobile-label">Fecha &amp; Hora</span>': '<span class="booking-mobile-label">Date &amp; Time</span>',
        'MÁS INFORMACIÓN': 'MORE INFORMATION',
        'Hacer una consulta': 'Make an inquiry',
        '<b>SOLICITAR CONSULTA</b>': '<b>SEND INQUIRY</b>',
        'Maravilla del Mundo • Paseo Privado': 'Natural Wonder • Private Tour',
        
        # Youtube buttons and section details
        'Ver Aventura Macuco\n                        Safari': 'Watch Macuco Safari Adventure',
        '<h2>EXPLORA FOZ DE IGUASÚ CON NOSOTROS</h2>': '<h2>EXPLORE FOZ DO IGUAÇU WITH US</h2>',
        'Naturaleza &amp; Paseos</h3>': 'Nature &amp; Tours</h3>',
        'Tours guiados por las\n                            Cataratas y los rincones más bellos de la región.': 'Guided tours of the Falls and the most beautiful spots in the region.',
        'Una de las siete maravillas naturales del mundo': 'One of the seven natural wonders of the world',
        'Traslados al Aeropuerto': 'Airport Transfers',
    }

    for src, dst in replacements.items():
        if src in content:
            content = content.replace(src, dst)
        else:
            # Try a single-line cleanup version for spacing issues
            src_clean = re.sub(r'\s+', ' ', src).strip()
            # Do a regex replace
            pattern = re.escape(src_clean).replace(r'\ ', r'\s+')
            content, count = re.subn(pattern, dst, content)

    # Let's check some custom JS values that might need translations
    # The setupCustomDropdown dropdown triggers:
    content = content.replace(
        "setupCustomDropdown('trigger-destino', 'menu-destino', 'booking-destino');",
        "setupCustomDropdown('trigger-destino', 'menu-destino', 'booking-destino');\n            // Set initial trigger label in English\n            document.getElementById('trigger-destino').querySelector('span').textContent = 'Where are you going?';"
    ).replace(
        "setupCustomDropdown('trigger-destino-m', 'menu-destino-m', 'booking-destino-m');",
        "setupCustomDropdown('trigger-destino-m', 'menu-destino-m', 'booking-destino-m');\n            // Set initial trigger label in English\n            document.getElementById('trigger-destino-m').querySelector('span').textContent = 'Where are you going?';"
    )

    with open('index-en.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("English translation updates finished successfully")

if __name__ == '__main__':
    main()
