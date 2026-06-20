def main():
    with open('index-en.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Target blocks to replace
    t1 = 'Tours &amp; Traslados Privados en la Triple Frontera'
    r1 = 'Private Tours &amp; Transfers in the Triple Frontier'

    t2 = 'Especialistas en LIBRAS • Español • Portugués<br>\n                    Incluye paseos guiados con guías certificados'
    r2 = 'Specialists in LIBRAS • Spanish • Portuguese<br>\n                    Includes guided tours with certified guides'

    t3 = '<h2>EXPLORA FOZ DO IGUAÇU CON NOSOTROS</h2>'
    r3 = '<h2>EXPLORE FOZ DO IGUAÇU WITH US</h2>'

    t4 = """                    <p>
                        Descubrir la inmensidad de las Cataratas y la biodiversidad única de la selva paranaense es una
                        experiencia inolvidable. Nos complace acompañarte de forma cercana y segura, ofreciendo un
                        servicio de traslados privados diseñado a tu medida.
                    </p>"""
    r4 = """                    <p>
                        Discovering the immensity of the Falls and the unique biodiversity of the Paraná rainforest is an
                        unforgettable experience. We are pleased to accompany you closely and safely, offering a
                        private transfer service tailored to your needs.
                    </p>"""

    t5 = """                    <p>
                        Nos encargamos de toda la logística: desde recogidas puntuales en los aeropuertos de la región
                        hasta los cruces fronterizos hacia Argentina y Paraguay, facilitando los trámites aduaneros para
                        que tu única preocupación sea disfrutar de la naturaleza. Además, organizamos paseos
                        confortables dentro del territorio brasileño, garantizando itinerarios flexibles tanto para
                        viajeros individuales como para familias y grupos organizados. Nuestro guiado incluye
                        comunicación accesible en español, portugués y LIBRAS, buscando siempre brindar un trato cálido
                        y humano.
                    </p>"""
    r5 = """                    <p>
                        We take care of all the logistics: from punctual pickups at the regional airports
                        to border crossings to Argentina and Paraguay, facilitating customs procedures so
                        your only concern is to enjoy nature. In addition, we organize comfortable tours
                        within the Brazilian territory, guaranteeing flexible itineraries for both
                        individual travelers and families or organized groups. Our guiding features
                        accessible communication in Spanish, Portuguese, and LIBRAS (Brazilian Sign Language), always seeking to provide a warm
                        and human service.
                    </p>"""

    # Perform replaces
    content = content.replace(t1, r1)
    content = content.replace(t2, r2)
    content = content.replace(t3, r3)
    content = content.replace(t4, r4)
    content = content.replace(t5, r5)

    with open('index-en.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully translated remaining paragraphs to English.")

if __name__ == '__main__':
    main()
