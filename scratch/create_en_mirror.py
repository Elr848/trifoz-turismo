import re

def create_english_mirror():
    # Read index.html (Spanish)
    with open('index.html', 'r', encoding='utf-8') as f:
        es_content = f.read()

    # Translate head details
    en_content = es_content
    en_content = en_content.replace('<html lang="es">', '<html lang="en">')
    en_content = en_content.replace(
        '<title>Traslados Privados en Foz de Iguazú | Paseos, Aeropuerto y Triple Frontera</title>',
        '<title>Private Transfers in Foz do Iguaçu | Tours, Airport & Triple Frontier</title>'
    )
    en_content = en_content.replace(
        '<meta name="description" content="Paseos privados en Foz de Iguazú. Traslados aeropuerto 24/7 y transfer privado Triple Frontera. Especialista en LIBRAS. Guías certificados. Reserva ahora.">',
        '<meta name="description" content="Private tours in Foz do Iguaçu. 24/7 airport transfers and private transport Triple Frontier. Sign Language (LIBRAS) specialist. Certified guides. Book now.">'
    )
    en_content = en_content.replace(
        '<meta name="keywords" content="tours foz de iguazu, paseos foz de iguazu, transfer foz de iguazu, guia de turismo foz, transporte privado foz, traslado aeropuerto foz, paseos guiados cataratas, tour cataratas iguazu, guia de turismo cataratas, transfer privado brasil, traslado triple frontera, transporte turistico foz, guia LIBRAS foz, tour macuco safari, traslado puerto iguazu, transfer ciudad del este, paseos guiados Trifoz">',
        '<meta name="keywords" content="tours foz do iguacu, tours foz do iguazu, transfer foz do iguazu, tour guide foz, private transport foz, airport transfer foz, guided tours falls, iguazu falls tour, waterfalls guide, private transfer brazil, triple frontier transfer, tourist transport foz, libras guide foz, macuco safari tour, puerto iguazu transfer, ciudad del este transfer, guided tours Trifoz">'
    )
    en_content = en_content.replace(
        '<link rel="canonical" href="https://trifoz-turismo.com/" />',
        '<link rel="canonical" href="https://trifoz-turismo.com/index-en.html" />'
    )
    en_content = en_content.replace(
        '<meta property="og:url" content="https://trifoz-turismo.com/">',
        '<meta property="og:url" content="https://trifoz-turismo.com/index-en.html">'
    )
    en_content = en_content.replace(
        '<meta property="og:title" content="🥇 Traslados Privados en Foz de Iguazú | Paseos Aeropuerto &amp; Transfer Privado | Guía Ebert">',
        '<meta property="og:title" content="🥇 Private Transfers in Foz do Iguaçu | Airport Tours &amp; Private Transfer | Guide Ebert">'
    )
    en_content = en_content.replace(
        '<meta property="og:description" content="⭐ Paseos privados ✈️ Traslados aeropuerto 24/7 🚗 Transfer Triple Frontera ⭐ Guía LIBRAS ⭐ Cataratas, Macuco Safari ⭐ +55(45)933003337">',
        '<meta property="og:description" content="⭐ Private tours ✈️ 24/7 Airport transfers 🚗 Triple Frontier transfer ⭐ LIBRAS Guide ⭐ Waterfalls, Macuco Safari ⭐ +55(45)933003337">'
    )
    en_content = en_content.replace(
        '<meta property="og:image:alt" content="Paseos y traslados privados en Foz de Iguazú">',
        '<meta property="og:image:alt" content="Private tours and transfers in Foz do Iguaçu">'
    )
    en_content = en_content.replace(
        '<meta name="twitter:url" content="https://trifoz-turismo.com/">',
        '<meta name="twitter:url" content="https://trifoz-turismo.com/index-en.html">'
    )
    en_content = en_content.replace(
        '<meta name="twitter:title" content="🥇 Traslados Privados en Foz de Iguazú | Paseos Aeropuerto &amp; Transfer Privado">',
        '<meta name="twitter:title" content="🥇 Private Transfers in Foz do Iguaçu | Airport Tours &amp; Private Transfer">'
    )
    en_content = en_content.replace(
        '<meta name="twitter:description" content="⭐ Paseos privados ✈️ Traslados aeropuerto 24/7 🚗 Transfer Triple Frontera ⭐ Guía LIBRAS ⭐ +55(45)933003337">',
        '<meta name="twitter:description" content="⭐ Private tours ✈️ 24/7 Airport transfers 🚗 Triple Frontier transfer ⭐ LIBRAS Guide ⭐ +55(45)933003337">'
    )
    en_content = en_content.replace(
        '<meta name="twitter:image:alt" content="Paseos y traslados privados en Foz de Iguazú">',
        '<meta name="twitter:image:alt" content="Private tours and transfers in Foz do Iguaçu">'
    )

    # 1. Translate the destinations array and whatsapp alerts in index-en.html
    # In the main JS destinations definition:
    es_destinations = """const destinations = [
                { title: "Cataratas del Iguazú", subtitle: "Siente la fuerza de las Siete Maravillas Naturales en un recorrido privado y exclusivo en la selva.", bgTitle: "CATARATAS", dest: "Cataratas del Iguazú (Argentina)" },
                { title: "Macuco Safari", subtitle: "Navegación extrema en bote bimotor hasta el corazón de las caídas de agua. Emoción y adrenalina pura.", bgTitle: "AVENTURA", dest: "Macuco Safari" },
                { title: "City Tour Foz", subtitle: "Descubre la diversidad de la Triple Frontera: el Templo Budista, la Mezquita y el Hito de las 3 Fronteras.", bgTitle: "CITY TOUR", dest: "Hito de las 3 Fronteras" },
                { title: "Premium Hotel", subtitle: "Traslados exclusivos a los mejores resorts, hoteles y paseos de compras libres de impuestos (Duty Free).", bgTitle: "HOTEL", dest: "Traslado para Hoteles" },
                { title: "Familia Tour", subtitle: "Navegación familiar premium y confortable. Disfruta del atardecer donde se unen los ríos Paraná e Iguazú.", bgTitle: "FAMILIA", dest: "Kattamaram II" },
                { title: "Puerto de Iguazú", subtitle: "Cruza la frontera y disfruta de la mejor gastronomía argentina: parrilladas, vinos selectos y compras.", bgTitle: "ARGENTINA", dest: "Paseo Puerto Iguazú" },
                { title: "Ciudad del Este", subtitle: "Tu guía de compras seguro en Paraguay. Encuentra tecnología, perfumes y marcas exclusivas a precios increíbles.", bgTitle: "COMPRAS", dest: "Compras Ciudad del Este" },
                { title: "Marco 3 Fronteras", subtitle: "El único lugar en el mundo donde tres países se abrazan. Disfruta de un atardecer mágico, shows y vista panorámica.", bgTitle: "FRONTERA", dest: "Paseo Paraguay" },
                { title: "Parque de las Aves", subtitle: "Camina entre tucanes, guacamayos y especies exóticas en un santuario ecológico único integrado en la selva.", bgTitle: "AVES", dest: "Parque de las Aves" }
            ];"""
            
    en_destinations = """const destinations = [
                { title: "Iguazu Falls", subtitle: "Feel the force of the Seven Natural Wonders on a private and exclusive tour in the rainforest.", bgTitle: "FALLS", dest: "Cataratas del Iguazú (Argentina)" },
                { title: "Macuco Safari", subtitle: "Extreme navigation in a twin-engine boat to the heart of the waterfalls. Pure emotion and adrenaline.", bgTitle: "ADVENTURE", dest: "Macuco Safari" },
                { title: "City Tour Foz", subtitle: "Discover the diversity of the Triple Frontier: the Buddhist Temple, the Mosque, and the Three Borders Landmark.", bgTitle: "CITY TOUR", dest: "Hito de las 3 Fronteras" },
                { title: "Premium Hotel", subtitle: "Exclusive transfers to the best resorts, hotels, and duty-free shopping tours (Duty Free).", bgTitle: "HOTEL", dest: "Traslado para Hoteles" },
                { title: "Family Tour", subtitle: "Premium and comfortable family navigation. Enjoy the sunset where the Paraná and Iguazú rivers meet.", bgTitle: "FAMILY", dest: "Kattamaram II" },
                { title: "Puerto Iguazú", subtitle: "Cross the border and enjoy the best Argentine gastronomy: grills, select wines, and shopping.", bgTitle: "ARGENTINA", dest: "Paseo Puerto Iguazú" },
                { title: "Ciudad del Este", subtitle: "Your safe shopping guide in Paraguay. Find technology, perfumes, and exclusive brands at incredible prices.", bgTitle: "SHOPPING", dest: "Compras Ciudad del Este" },
                { title: "Marco 3 Fronteras", subtitle: "The only place in the world where three countries embrace. Enjoy a magical sunset, shows, and panoramic view.", bgTitle: "FRONTIER", dest: "Paseo Paraguay" },
                { title: "Bird Park", subtitle: "Walk among toucans, macaws, and exotic species in a unique ecological sanctuary integrated into the rainforest.", bgTitle: "BIRDS", dest: "Parque de las Aves" }
            ];"""

    en_content = en_content.replace(es_destinations, en_destinations)

    # Translate function enviarWhatsApp messages and alerts
    en_content = en_content.replace(
        'alert("Por favor selecciona un destino de la lista.");',
        'alert("Please select a destination from the list.");'
    ).replace(
        'let fechaFormateada = `${dia}/${mes}/${anio} a las ${hora}:${min}`;',
        'let fechaFormateada = `${dia}/${mes}/${anio} at ${hora}:${min}`;'
    ).replace(
        'mensaje = `¡Hola! Me gustaría recibir ayuda para armar un itinerario personalizado.\\n\\n*Detalles iniciales:*\\n👥 Pasajeros: ${pax}\\n📅 Fecha de llegada: ${fechaFormateada}`;',
        'mensaje = `Hello! I would like to get help to assemble a custom itinerary.\\n\\n*Initial details:*\\n👥 Passengers: ${pax}\\n📅 Arrival Date: ${fechaFormateada}`;'
    ).replace(
        'mensaje = `¡Hola! Me gustaría solicitar un presupuesto para el siguiente tour/traslado:\\n\\n📍 Destino: ${destino}\\n👥 Pasajeros: ${pax}\\n📅 Fecha y Hora: ${fechaFormateada}`;',
        'mensaje = `Hello! I would like to request a quote for the following tour/transfer:\\n\\n📍 Destination: ${destino}\\n👥 Passengers: ${pax}\\n📅 Date and Time: ${fechaFormateada}`;'
    )

    # Let's perform some clean text translations in body
    body_translations = {
        '🥇 TRASLADO PRIVADO | GUÍA CERTIFICADO': '🥇 PRIVATE TRANSFER | CERTIFIED GUIDE',
        'TRASCENDER Y CONECTAR': 'TRANSCEND & CONNECT',
        'FOZ DE IGUASÚ': 'FOZ DO IGUAÇU',
        'Servicios de traslados y paseos privados en Foz de Iguazú, Puerto Iguazú y Ciudad del Este. Guías bilingües certificados.': 'Private transfer services and tours in Foz do Iguaçu, Puerto Iguazú and Ciudad del Este. Certified bilingual guides.',
        'ESPECIALISTA EN LIBRAS': 'SIGN LANGUAGE SPECIALIST',
        'RESERVAR AHORA': 'BOOK NOW',
        
        # Booking Bar
        'Destino': 'Destination',
        'Selecciona un destino...': 'Select a destination...',
        'Selecciona un destino': 'Select a destination',
        'Pasajeros': 'Passengers',
        'Fecha y Hora': 'Date & Time',
        'SOLICITAR PRESUPUESTO': 'REQUEST QUOTE',
        
        # Booking Form Mobile
        'RESERVA TU TRASLADO PRIVADO': 'BOOK YOUR PRIVATE TRANSFER',
        'Itinerario Personalizado': 'Custom Itinerary',
        
        # Attractions Section
        'Invitación': 'Invitation',
        'Atracciones Imperdibles en Foz de Iguazú': 'Must-See Attractions in Foz do Iguaçu',
        'Texto gigante en el fondo': 'Giant background text',
        'Controles laterales flotantes': 'Floating side controls',
        'Viewport 3D': '3D Viewport',
        'Información del destino activo': 'Active destination info',
        'Cataratas del Iguazú': 'Iguazu Falls',
        'Visita guiada por la mayor maravilla natural.': 'Guided tour through the greatest natural wonder.',
        'CONSULTAR': 'INQUIRE',
        'Navegación por puntos': 'Dots navigation',
        'Se generan dinámicamente': 'Generated dynamically',
        
        # Video Macuco Card
        'Aventura extrema en las caídas de agua.': 'Extreme adventure in the waterfalls.',
        'Ver Aventura Macuco Safari': 'Watch Macuco Safari Adventure',
        
        # Horizontal Buttons Bar
        'Galería': 'Gallery',
        'Ingresos': 'Tickets',
        'Videos': 'Videos',
        
        # Info Box Section
        '¿Por qué elegir Trifoz Turismo?': 'Why Choose Trifoz Turismo?',
        'Tu viaje soñado en la Triple Frontera, con confort premium y un servicio diseñado exclusivamente para ti.': 'Your dream trip in the Triple Frontier, with premium comfort and a service designed exclusively for you.',
        'EXPLORA FOZ DE IGUASÚ CON NOSOTROS': 'EXPLORE FOZ DO IGUAÇU WITH US',
        'Descubrir la inmensidad de las Cataratas y la biodiversidad única de la selva es una experiencia inolvidable. Tenemos el agrado de acompañarte de forma cercana y segura, ofreciendo un servicio de traslados privados a medida.': 'Discovering the immensity of the Falls and the unique biodiversity of the rainforest is an unforgettable experience. We are pleased to accompany you closely and safely, offering a tailor-made private transfer service.',
        'Nos encargamos de toda la logística: desde traslados puntuales en los aeropuertos de la región hasta los cruces de fronteras a Argentina y Paraguay, facilitando los trámites aduaneros para que tu única preocupación sea disfrutar del entorno. Además, organizamos paseos confortables por el lado brasileño, garantizando flexibilidad de itinerarios para viajeros individuales, familias o grupos organizados. Nuestro guiado cuenta con comunicación accesible en español, portugués y LIBRAS, buscando siempre ofrecer una atención cálida y humana.': 'We take care of all the logistics: from punctual transfers at the regional airports to border crossings to Argentina and Paraguay, facilitating customs procedures so your only concern is to enjoy the surroundings. In addition, we organize comfortable tours on the Brazilian side, guaranteeing flexibility of itineraries for individual travelers, families, or organized groups. Our guiding features accessible communication in Spanish, Portuguese, and LIBRAS (Brazilian Sign Language), always seeking to offer warm and human service.',
        'Naturaleza & Paseos': 'Nature & Tours',
        'Paseos guiados por las Cataratas y los puntos más bellos de la región.': 'Guided tours of the Falls and the most beautiful spots in the region.',
        
        # Gallery titles
        'Una de las siete maravillas del mundo': 'One of the seven natural wonders of the world',
        'Puntualidad y confort 24/7 en la Triple Frontera': 'Punctuality and comfort 24/7 in the Triple Frontier',
        'Paz, meditación y espectaculares esculturas en Foz': 'Peace, meditation, and spectacular sculptures in Foz',
        'Arquitectura islámica y riqueza cultural en el corazón de Foz': 'Islamic architecture and cultural richness in the heart of Foz',
        'Paisajes únicos e inolvidables de la selva': 'Unique and unforgettable landscapes of the rainforest',
        'Experiencias gastronómicas y multiculturales locales': 'Local gastronomic and multicultural experiences',
        'Compras internacionales exclusivas libre de impuestos': 'Exclusive tax-free international shopping',
        'Sabores locales, olivas y quesos tradicionales': 'Local flavors, olives, and traditional cheeses',
        'Navegación inolvidable en el encuentro de los ríos': 'Unforgettable navigation at the meeting of the rivers',
        'Diversión para toda la familia con réplicas perfectas': 'Family fun with perfect replicas',
        'Contacto directo con la fauna y aves rescatadas': 'Direct contact with fauna and rescued birds',
        'Una de las mayores obras de ingeniería del planeta': 'One of the greatest engineering works on the planet',
        'Espectáculos de luces y atracciones interactivas': 'Light shows and interactive attractions',
        'Una de las ruedas de la fortuna más grandes de América Latina': 'One of the largest Ferris wheels in Latin America',
        
        # Footer
        'Trifoz Turismo. Todos los derechos reservados.': 'Trifoz Turismo. All rights reserved.',
        'Guía Ebert': 'Guide Ebert',
        
        # Modal Ingresos
        'Asesoría en Compra de Ingresos': 'Ticket Purchase Advisory',
        'Te ayudamos y asesoramos de forma personalizada en la compra de tus entradas para todas las atracciones de Foz de Iguazú (Cataratas, Macuco Safari, Parque de las Aves, Itaipú, etc.).': 'We help and advise you in a personalized way in the purchase of your tickets for all attractions in Foz do Iguaçu (Falls, Macuco Safari, Bird Park, Itaipu, etc.).',
        '¿Cómo te ayudamos?': 'How do we help you?',
        'Evita estafas:': 'Avoid scams:',
        'Te indicamos los canales oficiales y páginas seguras de compra.': 'We point you to official channels and secure purchase pages.',
        'Sincronización logística:': 'Logistics synchronization:',
        'Te asesoramos en la elección de días y horarios para que coordinen perfectamente con tus traslados privados.': 'We advise you in choosing days and times to coordinate perfectly with your private transfers.',
        'Acompañamiento Ebert:': 'Ebert Support:',
        'Tu guía Ebert te ayuda con cualquier consulta sobre los ingresos directamente.': 'Your guide Ebert helps you directly with any questions about tickets.',
        
        # Modal Videos
        'Galería de Videos': 'Video Gallery',
        'Show de Falconería': 'Falconry Show',
        'Feirinha Puerto Iguazú - Parte 1': 'Puerto Iguazú Local Market - Part 1',
        'Feirinha Puerto Iguazú - Parte 2': 'Puerto Iguazú Local Market - Part 2',
        'Cultura y Gastronomía China': 'Chinese Culture and Gastronomy',
        'Centro de Aves El Cóndor': 'El Cóndor Bird Center',
        'Cerrar': 'Close',
    }

    for es_text, en_text in body_translations.items():
        en_content = en_content.replace(es_text, en_text)

    # Let's save index-en.html
    with open('index-en.html', 'w', encoding='utf-8') as f:
        f.write(en_content)
    print("Created index-en.html")

def update_language_selector_in_all_files():
    # Define the old selector and the new selector
    # Old selector in Spanish index.html and PT index-pt.html
    es_selector_old = """    <div class="header-idioma-container">
        <span class="label-idioma-fijo">Idioma:</span>
        <div class="lista-idioma-fija">
            <a href="index.html" class="opcion-idioma-fija activo">
                <img src="https://flagcdn.com/w20/es.png" class="mini-flag" alt="Español"> ES
            </a>
            <a href="index-pt.html" class="opcion-idioma-fija">
                <img src="https://flagcdn.com/w20/br.png" class="mini-flag" alt="Portugués"> PT
            </a>
        </div>
    </div>"""

    pt_selector_old = """    <div class="header-idioma-container">
        <span class="label-idioma-fijo">Idioma:</span>
        <div class="lista-idioma-fija">
            <a href="index.html" class="opcion-idioma-fija">
                <img src="https://flagcdn.com/w20/es.png" class="mini-flag" alt="Español"> ES
            </a>
            <a href="index-pt.html" class="opcion-idioma-fija activo">
                <img src="https://flagcdn.com/w20/br.png" class="mini-flag" alt="Portugués"> PT
            </a>
        </div>
    </div>"""

    # Spanish file new selector
    es_selector_new = """    <div class="header-idioma-container">
        <span class="label-idioma-fijo">Idioma:</span>
        <div class="lista-idioma-fija">
            <a href="index.html" class="opcion-idioma-fija activo">
                <img src="https://flagcdn.com/w20/es.png" class="mini-flag" alt="Español"> ES
            </a>
            <a href="index-pt.html" class="opcion-idioma-fija">
                <img src="https://flagcdn.com/w20/br.png" class="mini-flag" alt="Portugués"> PT
            </a>
            <a href="index-en.html" class="opcion-idioma-fija">
                <img src="https://flagcdn.com/w20/us.png" class="mini-flag" alt="English"> EN
            </a>
        </div>
    </div>"""

    # Portuguese file new selector
    pt_selector_new = """    <div class="header-idioma-container">
        <span class="label-idioma-fijo">Idioma:</span>
        <div class="lista-idioma-fija">
            <a href="index.html" class="opcion-idioma-fija">
                <img src="https://flagcdn.com/w20/es.png" class="mini-flag" alt="Español"> ES
            </a>
            <a href="index-pt.html" class="opcion-idioma-fija activo">
                <img src="https://flagcdn.com/w20/br.png" class="mini-flag" alt="Portugués"> PT
            </a>
            <a href="index-en.html" class="opcion-idioma-fija">
                <img src="https://flagcdn.com/w20/us.png" class="mini-flag" alt="English"> EN
            </a>
        </div>
    </div>"""

    # English file new selector
    en_selector_new = """    <div class="header-idioma-container">
        <span class="label-idioma-fijo">Language:</span>
        <div class="lista-idioma-fija">
            <a href="index.html" class="opcion-idioma-fija">
                <img src="https://flagcdn.com/w20/es.png" class="mini-flag" alt="Español"> ES
            </a>
            <a href="index-pt.html" class="opcion-idioma-fija">
                <img src="https://flagcdn.com/w20/br.png" class="mini-flag" alt="Portugués"> PT
            </a>
            <a href="index-en.html" class="opcion-idioma-fija activo">
                <img src="https://flagcdn.com/w20/us.png" class="mini-flag" alt="English"> EN
            </a>
        </div>
    </div>"""

    # Let's apply these selector replacements to each file
    for filename, old_sel, new_sel in [
        ('index.html', es_selector_old, es_selector_new),
        ('index-pt.html', pt_selector_old, pt_selector_new),
        ('index-en.html', es_selector_new, en_selector_new) # In index-en.html, we replace the newly copied Spanish selector
    ]:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # If normal replace doesn't match due to minor whitespace differences, let's use a regex-based replacement or clean it
        if old_sel in content:
            content = content.replace(old_sel, new_sel)
        else:
            # Fallback regex replacing inside <div class="header-idioma-container">...</div>
            content = re.sub(
                r'<div class="header-idioma-container">.*?</div>\s*</div>',
                new_sel,
                content,
                flags=re.DOTALL
            )
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated selector in {filename}")

if __name__ == '__main__':
    create_english_mirror()
    update_language_selector_in_all_files()
