import re

def main():
    # Read files
    with open('index.html', 'r', encoding='utf-8') as f:
        es_content = f.read()
    
    with open('index-pt.html', 'r', encoding='utf-8') as f:
        pt_content = f.read()

    # 1. Extract the main script block from index.html (the one with GSAP/Draggable/etc.)
    es_script_match = re.search(r'(<script>.*?gsap\.registerPlugin\(Draggable\).*?</script>)', es_content, re.DOTALL)
    if not es_script_match:
        print("Error: Could not find GSAP script in index.html")
        return
    es_script = es_script_match.group(1)

    # Adapt the script content for Portuguese
    es_destinations = """            const destinations = [
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
    
    es_dest_match = re.search(r'(const destinations = \[.*?\];)', es_content, re.DOTALL)
    if es_dest_match:
        es_destinations = es_dest_match.group(1)

    pt_destinations = """const destinations = [
                { title: "Cataratas do Iguaçu", subtitle: "Sinta a força das Sete Maravilhas Naturais em um passeio privado e exclusivo na floresta.", bgTitle: "CATARATAS", dest: "Cataratas do Iguaçu (Brasil)" },
                { title: "Macuco Safari", subtitle: "Navegação emocionante em barco bimotor até o coração das quedas d'água. Pura adrenalina e aventura.", bgTitle: "AVENTURA", dest: "Macuco Safari" },
                { title: "City Tour Foz", subtitle: "Descubra a diversidade da Tríplice Fronteira: o Templo Budista, a Mesquita e o Marco das Três Fronteiras.", bgTitle: "CITY TOUR", dest: "Marco das Três Fronteiras" },
                { title: "Hotéis Premium", subtitle: "Traslados exclusivos para os melhores resorts, hotéis e compras livres de impostos (Duty Free Shop).", bgTitle: "HOTEL", dest: "Traslado para Hotéis" },
                { title: "Família Tour", subtitle: "Navegação familiar premium e confortável. Desfrute do pôr do sol onde se encontram os rios Iguaçu e Paraná.", bgTitle: "FAMÍLIA", dest: "Kattamaram II" },
                { title: "Puerto Iguazú", subtitle: "Cruze a fronteira e desfrute da melhor gastronomia argentina: churrasco, vinhos finos e compras.", bgTitle: "ARGENTINA", dest: "Paseo Puerto Iguazú" },
                { title: "Ciudad del Este", subtitle: "Seu guia de compras seguro no Paraguai. Encontre eletrônicos, perfumes e marcas importadas a preços incríveis.", bgTitle: "COMPRAS", dest: "Compras Ciudad del Este" },
                { title: "Marco 3 Fronteiras", subtitle: "O único lugar no mundo onde três países se abraçam. Desfrute do pôr do sol, shows e vista panorâmica.", bgTitle: "FRONTERA", dest: "Paseo Paraguay" },
                { title: "Parque das Aves", subtitle: "Caminhe entre tucanos, araras e espécies exóticas em um santuário ecológico único integrado na mata atlântica.", bgTitle: "AVES", dest: "Parque das Aves" }
            ];"""

    pt_script = es_script.replace(es_destinations, pt_destinations)
    
    # Translate WhatsApp messages and alert inside function enviarWhatsApp
    pt_script = pt_script.replace(
        'alert("Por favor selecciona un destino de la lista.");',
        'alert("Por favor, selecione um destino da lista.");'
    ).replace(
        'let fechaFormateada = `${dia}/${mes}/${anio} a las ${hora}:${min}`;',
        'let fechaFormateada = `${dia}/${mes}/${anio} às ${hora}:${min}`;'
    ).replace(
        'mensaje = `¡Hola! Me gustaría recibir ayuda para armar un itinerario personalizado.\\n\\n*Detalles iniciales:*\\n👥 Pasajeros: ${pax}\\n📅 Fecha de llegada: ${fechaFormateada}`;',
        'mensaje = `Olá! Gostaria de receber ajuda para montar um itinerário personalizado.\\n\\n*Detalhes iniciais:*\\n👥 Passageiros: ${pax}\\n📅 Data de chegada: ${fechaFormateada}`;'
    ).replace(
        'mensaje = `¡Hola! Me gustaría solicitar un presupuesto para el siguiente tour/traslado:\\n\\n📍 Destino: ${destino}\\n👥 Pasajeros: ${pax}\\n📅 Fecha y Hora: ${fechaFormateada}`;',
        'mensaje = `Olá! Gostaria de solicitar um orçamento para o seguinte tour/traslado:\\n\\n📍 Destino: ${destino}\\n👥 Passageiros: ${pax}\\n📅 Data e Hora: ${fechaFormateada}`;'
    ).replace(
        "destino === 'Itinerario Personalizado'",
        "destino === 'Itinerario Personalizado' || destino === 'Itinerário Personalizado'"
    ).replace(
        '¡Hola! Me gustaría solicitar un presupuesto',
        'Olá! Gostaria de solicitar um orçamento'
    ).replace(
        '¡Hola! Me gustaría recibir ayuda',
        'Olá! Gostaria de receber ajuda'
    )

    # 2. Extract galeria section from index.html
    es_galeria_match = re.search(r'(<section id="galeria".*?</section>)', es_content, re.DOTALL)
    if not es_galeria_match:
        print("Error: Could not find galeria section in index.html")
        return
    es_galeria = es_galeria_match.group(1)
    
    # Translate titles/subtitles in es_galeria back to Portuguese:
    translations = {
        'Cataratas del Iguazú': 'Cataratas do Iguaçu',
        'Una de las siete maravillas naturales del mundo': 'Uma das sete maravilhas naturais do mundo',
        'Traslados al Aeropuerto': 'Translados ao Aeropuerto',
        'Puntualidad y confort 24/7 en la Triple Frontera': 'Pontualidade e conforto 24/7 na Tríplice Fronteira',
        'Templo Budista Chen Tien': 'Templo Budista Chen Tien',
        'Paz, meditación y espectaculares esculturas en Foz': 'Paz, meditação e espetaculares esculturas em Foz',
        'Mezquita Omar Ibn Al-Khattab': 'Mesquita Omar Ibn Al-Khattab',
        'Arquitectura islámica y riqueza cultural en el corazón de Foz': 'Arquitetura islâmica e riqueza cultural no coração de Foz',
        'Vistas Panorámicas': 'Vistas Panorâmicas',
        'Paisajes únicos e inolvidables de la selva': 'Paisagens únicas e inesquecíveis da mata',
        'Cultura y Sabores': 'Cultura e Sabores',
        'Experiencias gastronómicas y multiculturales locales': 'Experiências gastronômicas e multiculturais locais',
        'Duty Free Shop': 'Duty Free Shop',
        'Compras internacionales exclusivas libre de impuestos': 'Compras internacionais exclusivas livre de impostos',
        'Feirinha de Puerto Iguazú': 'Feirinha de Puerto Iguazú',
        'Sabores locales, olivas y quesos tradicionales': 'Sabores locais, azeitonas e queijos tradicionais',
        'Paseo en Kattamaram': 'Passeio de Kattamaram',
        'Navegación inolvidable en el encuentro de los ríos': 'Navegação inesquecível no encontro dos rios',
        'Dreamland Museo de Cera': 'Dreamland Museu de Cera',
        'Diversión para toda la familia con réplicas perfectas': 'Diversão para toda a família com réplicas perfeita',
        'Parque de las Aves': 'Parque das Aves',
        'Contacto directo con la fauna y aves rescatadas': 'Contato direto com a fauna e aves resgatadas',
        'Itaipú Binacional': 'Itaipu Binacional',
        'Una de las mayores obras de ingeniería del planeta': 'Uma das maiores obras de engenharia do planeta',
        'Wonder Park Show': 'Wonder Park Show',
        'Espectáculos de luces y atracciones interactivas': 'Espetáculos de luzes e atrações interativas',
        'Yup Star Foz': 'Yup Star Foz',
        'Una de las ruedas de la fortuna más grandes de América Latina': 'Uma das maiores rodas-gigantes de toda a América Latina',
        'Anterior': 'Anterior',
        'Siguiente': 'Seguinte',
    }
    
    pt_galeria = es_galeria
    for es_text, pt_text in translations.items():
        pt_galeria = pt_galeria.replace(es_text, pt_text)
        
    # 3. Extract the 3D coverflow carousel from index.html
    es_carousel_match = re.search(r'(<div class="slider-container-3d">.*?)(?=\s*<div class="contenedor-catalogo")', es_content, re.DOTALL)
    if not es_carousel_match:
        print("Error: Could not find slider-container-3d in index.html")
        return
    es_carousel = es_carousel_match.group(1)
    
    # Translate the carousel texts
    pt_carousel = es_carousel.replace('Cataratas del Iguazú', 'Cataratas do Iguaçu')
    pt_carousel = pt_carousel.replace('Atracciones Imperdibles en Foz de Iguazú', 'Passeios Imperdíveis em Foz do Iguaçu')
    pt_carousel = pt_carousel.replace('Visita guiada por la mayor maravilla natural.', 'Visita guiada pela maior maravilha natural.')
    pt_carousel = pt_carousel.replace('CONSULTAR', 'CONSULTAR')
    pt_carousel = pt_carousel.replace('Anterior', 'Anterior')
    pt_carousel = pt_carousel.replace('Siguiente', 'Seguinte')
    pt_carousel = pt_carousel.replace('Cataratas del Iguazú (Argentina)', 'Cataratas do Iguaçu (Brasil)')
    pt_carousel = pt_carousel.replace('Texto gigante en el fondo', 'Texto gigante no fundo')
    pt_carousel = pt_carousel.replace('Controles laterales flotantes', 'Controles laterais flutuantes')
    pt_carousel = pt_carousel.replace('Información del destino activo', 'Informação do destino ativo')
    pt_carousel = pt_carousel.replace('Navegación por puntos', 'Navegação por pontos')
    pt_carousel = pt_carousel.replace('Se generan dinámicamente', 'Gerados dinamicamente')
    
    # 4. Modals and lightbox at the end of the file.
    pt_footer_idx = pt_content.find('</footer>')
    if pt_footer_idx == -1:
        print("Error: </footer> not found in index-pt.html")
        return
    pt_footer_end = pt_footer_idx + len('</footer>')
    
    es_footer_idx = es_content.find('</footer>')
    if es_footer_idx == -1:
        print("Error: </footer> not found in index.html")
        return
    es_footer_end = es_footer_idx + len('</footer>')
    
    tail = es_content[es_footer_end:]
    
    # Translate the tail contents (modals, script etc.) to Portuguese:
    # First: modalIngresos
    tail = tail.replace('Asesoría en Compra de Ingresos', 'Assessoria na Compra de Ingressos')
    tail = tail.replace(
        'Te ayudamos y asesoramos de forma personalizada en la compra de tus entradas para todas las atracciones de Foz de Iguazú (Cataratas, Macuco Safari, Parque de las Aves, Itaipú, etc.).',
        'Ajudamos e orientamos você de forma personalizada na compra de seus ingressos para todas as atrações de Foz de Iguaçu (Cataratas, Macuco Safari, Parque das Aves, Itaipu, etc.).'
    )
    tail = tail.replace('¿Cómo te ayudamos?', 'Como ajudamos você?')
    tail = tail.replace('Evita estafas:', 'Evite golpes:')
    tail = tail.replace('Te indicamos los canales oficiales y páginas seguras de compra.', 'Indicamos os canais oficiais e sites seguros para a compra.')
    tail = tail.replace('Sincronización logística:', 'Sincronização de horários:')
    tail = tail.replace('Te asesoramos en la elección de días y horarios para que coordinen perfectamente con tus traslados privados.', 'Orientamos na escolha de datas e horários para que coincidam perfeitamente com os seus traslados privados.')
    tail = tail.replace('Acompañamiento Ebert:', 'Suporte do Ebert:')
    tail = tail.replace('Tu guía Ebert te ayuda con cualquier consulta sobre los ingresos directamente.', 'Seu guia Ebert ajuda você diretamente com qualquer dúvida sobre os ingressos.')
    tail = tail.replace('Consultar por WhatsApp', 'Consultar por WhatsApp')
    tail = tail.replace(
        'me%20gustar%C3%ADa%20que%20me%20asesores%20con%20la%20compra%20de%20los%20ingresos%20para%20las%20atracciones.',
        'gostaria%20de%20ajuda%20com%20a%20compra%20dos%20ingressos%20para%20as%20atra\u00e7\u00f5es.'
    )
    tail = tail.replace('Hola%20Ebert', 'Ol\u00e1%20Ebert')
    
    # Second: modalVideos
    tail = tail.replace('Galería de Videos', 'Galeria de Vídeos')
    tail = tail.replace('Show de Falconería', 'Apresentação de Falconaria')
    tail = tail.replace('Feirinha Puerto Iguazú - Parte 1', 'Feirinha Puerto Iguazú - Parte 1')
    tail = tail.replace('Feirinha Puerto Iguazú - Parte 2', 'Feirinha Puerto Iguazú - Parte 2')
    tail = tail.replace('Cultura y Gastronomía China', 'Cultura e Gastronomia Chinesa')
    tail = tail.replace('Centro de Aves El Cóndor', 'Centro de Aves El Cóndor')
    tail = tail.replace('Cerrar', 'Fechar')
    
    # Third: Replace destinations inside script block in tail
    tail_dest_match = re.search(r'(const destinations = \[.*?\];)', tail, re.DOTALL)
    if tail_dest_match:
        tail = tail.replace(tail_dest_match.group(1), pt_destinations)

    # Let's perform script string replacements for whatsapp function directly in the tail:
    tail = tail.replace(
        'alert("Por favor selecciona un destino de la lista.");',
        'alert("Por favor, selecione um destino da lista.");'
    ).replace(
        'let fechaFormateada = `${dia}/${mes}/${anio} a las ${hora}:${min}`;',
        'let fechaFormateada = `${dia}/${mes}/${anio} às ${hora}:${min}`;'
    ).replace(
        'mensaje = `¡Hola! Me gustaría recibir ayuda para armar un itinerario personalizado.\\n\\n*Detalles iniciales:*\\n👥 Pasajeros: ${pax}\\n📅 Fecha de llegada: ${fechaFormateada}`;',
        'mensaje = `Olá! Gostaria de receber ajuda para montar um itinerário personalizado.\\n\\n*Detalhes iniciais:*\\n👥 Passageiros: ${pax}\\n📅 Data de chegada: ${fechaFormateada}`;'
    ).replace(
        'mensaje = `¡Hola! Me gustaría solicitar un presupuesto para el siguiente tour/traslado:\\n\\n📍 Destino: ${destino}\\n👥 Pasajeros: ${pax}\\n📅 Fecha y Hora: ${fechaFormateada}`;',
        'mensaje = `Olá! Gostaria de solicitar um orçamento para o seguinte tour/traslado:\\n\\n📍 Destino: ${destino}\\n👥 Passageiros: ${pax}\\n📅 Data e Hora: ${fechaFormateada}`;'
    ).replace(
        "destino === 'Itinerario Personalizado'",
        "destino === 'Itinerario Personalizado' || destino === 'Itinerário Personalizado'"
    ).replace(
        '¡Hola! Me gustaría solicitar un presupuesto',
        'Olá! Gostaria de solicitar um orçamento'
    ).replace(
        '¡Hola! Me gustaría recibir ayuda',
        'Olá! Gostaria de receber ajuda'
    )
    
    # Assemble the new content of index-pt.html
    # 1. Update the slider-container-3d:
    pt_slider_match = re.search(r'(<div class="slider-container-3d">.*?)(?=\s*<div class="contenedor-catalogo")', pt_content, re.DOTALL)
    if pt_slider_match:
        pt_content = pt_content.replace(pt_slider_match.group(1), pt_carousel)
    else:
        print("Warning: Could not find slider-container-3d in index-pt.html")
        
    # 2. Remove the Accordion from pt_content:
    pt_content = re.sub(
        r'<!-- OUTRAS ATRAÇÕES \(ACORDEÃO\) -->\s*<div class="otras-atracciones-wrapper">.*?</div>\s*(?=</section>|<!-- Barra de botões horizontal -->)',
        '',
        pt_content,
        flags=re.DOTALL
    )
    
    # 3. Update the galeria section:
    pt_galeria_match = re.search(r'(<section id="galeria".*?</section>)', pt_content, re.DOTALL)
    if pt_galeria_match:
        pt_content = pt_content.replace(pt_galeria_match.group(1), pt_galeria)
        
    # 4. Replace the entire footer tail:
    new_pt_content = pt_content[:pt_footer_end] + tail
    
    # Save the updated content
    with open('index-pt.html', 'w', encoding='utf-8') as f:
        f.write(new_pt_content)
        
    print("Success syncing index-pt.html")

if __name__ == '__main__':
    main()
