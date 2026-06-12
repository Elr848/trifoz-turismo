import re

pasted_code = """<section class="attractions">
        <div style="display: flex; flex-direction: column; align-items: center; margin-bottom: 15px; gap: 6px;">
            <a href="https://www.youtube.com/shorts/Ulz_WJArmqA" target="_blank" rel="noopener noreferrer" class="libras-round-button" aria-label="Video LIBRAS">
                <img src="images/una.jpeg" alt="LIBRAS" class="libras-btn-img" loading="lazy">
            </a>
            <span style="font-family: 'Montserrat', sans-serif; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; color: #ffd700; letter-spacing: 1.5px; text-shadow: 0 2px 4px rgba(0,0,0,0.6);">Invitación</span>
        </div>
        <div style="text-align: center; margin-bottom: 15px; padding: 0 20px;">
            <h2 class="subtitulo-amarillo" style="font-size: clamp(1.4rem, 6vw, 2.2rem); margin-bottom: 5px;">
                Atracciones Imperdibles en Foz de Iguazú
            </h2>
        </div>
        <div class="slider-container-3d">
            <div class="bg-text-back">CATARATAS</div>
            
            <div class="nav-btn-container-3d">
                <button class="nav-btn-3d-cf" id="prevBtn3D" aria-label="Anterior">
                    <svg viewBox="0 0 24 24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg>
                </button>
                <button class="nav-btn-3d-cf" id="nextBtn3D" aria-label="Siguiente">
                    <svg viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
                </button>
            </div>

            <div class="carousel-viewport-3d">
                <div class="carousel-3d-wrapper" id="carousel">
                    
                    <div class="card-item-3d" data-index="0" data-src="images/cataratas mejorada.jpg">
                        <div class="card-back" style="background: url('images/cataratas mejorada.jpg') no-repeat center center / cover; padding: 0;"></div>
                    </div>

                    <div class="card-item-3d" data-index="1" data-src="images/macuco_safari_real.jpg">
                        <div class="card-back" style="background: url('images/macuco_safari_real.jpg') no-repeat center center / cover; padding: 0;"></div>
                    </div>

                    <div class="card-item-3d" data-index="2" data-src="images/buda.jpeg">
                        <div class="card-back" style="background: url('images/buda.jpeg') no-repeat center center / cover; padding: 0;"></div>
                    </div>

                    <div class="card-item-3d" data-index="3" data-src="images/dutty.jpeg">
                        <div class="card-back" style="background: url('images/dutty.jpeg') no-repeat center center / cover; padding: 0;"></div>
                    </div>

                    <div class="card-item-3d" data-index="4" data-src="images/Kattamaram (2).jpeg">
                        <div class="card-back" style="background: url('images/Kattamaram (2).jpeg') no-repeat center center / cover; padding: 0;"></div>
                    </div>

                    <div class="card-item-3d" data-index="5" data-src="images/dutty.jpeg">
                        <div class="card-back" style="background: url('images/dutty.jpeg') no-repeat center center / cover; padding: 0;"></div>
                    </div>

                    <div class="card-item-3d" data-index="6" data-src="images/china.webp">
                        <div class="card-back" style="background: url('images/china.webp') no-repeat center center / cover; padding: 0;"></div>
                    </div>

                    <div class="card-item-3d" data-index="7" data-src="images/marco_real.jpg">
                        <div class="card-back" style="background: url('images/marco_real.jpg') no-repeat center center / cover; padding: 0;"></div>
                    </div>

                    <div class="card-item-3d" data-index="8" data-src="images/pda.webp">
                        <div class="card-back" style="background: url('images/pda.webp') no-repeat center center / cover; padding: 0;"></div>
                    </div>

                </div>
            </div>

            <div class="active-info-container" style="display: flex; flex-direction: column; align-items: center; gap: 15px; margin-top: 25px;">
                <div class="active-info-title-row">
                    <span class="title-line"></span>
                    <h3 class="active-title-3d" id="activeTitle">Cataratas del Iguazú</h3>
                    <span class="title-line"></span>
                </div>
                <p class="active-subtitle-3d" id="activeSubtitle" style="margin: 0; max-width: 600px; line-height: 1.4;">Maravilla del Mundo • Paseo Privado</p>
                <button class="card-btn-action" id="activeCardBtn" data-dest="Cataratas del Iguazú (Argentina)">CONSULTAR</button>
            </div>

            <div class="navigation-dots-3d" id="dotsContainer3D"></div>
        </div>

        <div class="contenedor-catalogo" style="display: flex; justify-content: center; align-items: center; padding: 40px 15px; width: 100%;">
            <div class="video-card card" style="max-width: 650px; width: 100%; margin: 0 auto; box-shadow: 0 15px 35px rgba(0, 35, 102, 0.1); background: rgba(255, 255, 255, 0.85); border-radius: 16px; border: 1.5px solid rgba(255, 255, 255, 0.4); overflow: hidden; display: flex; flex-direction: column;">
                <div class="card-image" style="width: 100%; overflow: hidden;">
                    <img src="images/macuco_safari_real.jpg" alt="Macuco Safari" width="800" height="500" loading="lazy"
                        style="width: 100%; height: auto; display: block; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.03)'" onmouseout="this.style.transform='scale(1)'">
                </div>
                <div class="card-content" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 35px 25px; gap: 20px; text-align: center; background: rgba(255, 255, 255, 0.95);">
                    <div style="text-align: center;">
                        <h3 style="font-family: 'Montserrat', sans-serif; font-weight: 900; letter-spacing: 2px; font-size: clamp(1.4rem, 4vw, 1.85rem); margin: 0 0 10px 0; color: #002366; text-transform: uppercase;">MACUCO SAFARI</h3>
                        <p style="color: #333333; font-size: clamp(0.9rem, 2vw, 1.05rem); margin: 0; line-height: 1.5; max-width: 600px;">Aventura extrema en las caídas de agua.</p>
                    </div>
                    <a href="https://youtu.be/1dUpxFeU_u4?si=1p_wqlZU0Bks6DNa" target="_blank"
                        rel="noopener noreferrer" class="btn-video-elegant" style="text-decoration: none; display: inline-flex; align-items: center; gap: 8px; font-family: 'Montserrat', sans-serif; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px; color: #fff; background: rgba(255, 0, 0, 0.85); padding: 12px 25px; border-radius: 30px; box-shadow: 0 4px 15px rgba(255,0,0,0.4); transition: all 0.3s;" onmouseover="this.style.background='#ff0000'; this.style.transform='translateY(-2px)';" onmouseout="this.style.background='rgba(255, 0, 0, 0.85)'; this.style.transform='translateY(0)';">
                        <i class="fab fa-youtube" style="color: #fff; font-size: 1.1rem;"></i> Ver Aventura Macuco Safari
                    </a>
                </div>
            </div>
        </div>
    </section>

    <div class="horizontal-button-bar">
        <a href="#galeria" class="btn-horizontal-bar" aria-label="Galería de Fotos">
            <i class="fas fa-images"></i>
            <span>Galería</span>
        </a>
        <a href="https://www.youtube.com/shorts/Ulz_WJArmqA" target="_blank" rel="noopener noreferrer" class="btn-horizontal-bar" aria-label="Atendemos en LIBRAS">
            <img src="images/libras_hd.png" alt="LIBRAS" style="width: 22px; height: 22px; border-radius: 50%; object-fit: cover; vertical-align: middle;">
            <span>LIBRAS</span>
        </a>
        <button class="btn-horizontal-bar" id="btn-ingresos" aria-label="Compra de Ingresos">
            <i class="fas fa-ticket-alt"></i>
            <span>Ingresos</span>
        </button>
        <button class="btn-horizontal-bar" id="btn-videos" aria-label="Videos de Trifoz">
            <i class="fas fa-video"></i>
            <span>Videos</span>
        </button>
    </div>

    <section class="informacion-turismo" style="max-width: 1200px; padding: 80px 20px; margin: 0 auto; text-align: center;">
        <h2 style="color: var(--amarillo); font-size: clamp(1.8rem, 5vw, 2.5rem); text-transform: uppercase; font-family: 'Oswald', sans-serif; letter-spacing: 2px; text-shadow: 2px 2px 5px rgba(0,0,0,0.8); margin-bottom: 10px;">¿Por qué elegir Trifoz Turismo?</h2>
        <p class="subtitulo-info" style="color: #fff; font-size: clamp(1rem, 2.5vw, 1.25rem); font-weight: 500; opacity: 0.95; margin-bottom: 50px; text-shadow: 1px 1px 3px rgba(0,0,0,0.8);">Tu viaje soñado en la Triple Frontera, con confort premium y un servicio diseñado exclusivamente para ti.</p>

        <div class="info-content-wrapper" style="display: flex; flex-direction: column; gap: 40px; align-items: center; width: 100%;">
            <div class="info-side-image" onmouseover="this.style.borderColor='rgba(224, 160, 255, 0.8)'; this.style.transform='translateY(-5px)';" onmouseout="this.style.borderColor='rgba(0, 210, 255, 0.4)'; this.style.transform='translateY(0)';" style="width: 95%; max-width: 580px; aspect-ratio: 1.52; height: auto; position: relative; border-radius: 20px; overflow: hidden; box-shadow: 0 15px 35px rgba(0,0,0,0.5); border: 2px solid rgba(0, 210, 255, 0.4); transition: all 0.4s ease; margin: 0 auto;">
                <div class="car-slides" style="width: 100%; height: 100%; position: relative;">
                    <div class="car-slide active" style="position: absolute; inset: 0; opacity: 1; transition: opacity 1.2s ease-in-out; z-index: 1;">
                        <img src="images/1.1.jpeg" alt="Vehículo premium Trifoz Turismo" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; transform: scale(1.02); transition: transform 5s ease-out;">
                        <div style="position: absolute; inset: 0; background: rgba(0, 0, 0, 0.35); z-index: 2; pointer-events: none;"></div>
                    </div>
                    <div class="car-slide" style="position: absolute; inset: 0; opacity: 0; transition: opacity 1.2s ease-in-out; z-index: 1;">
                        <img src="images/car2 - copia.jpeg" alt="Vehículo premium Trifoz Turismo" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; transform: scale(1.02); transition: transform 5s ease-out;">
                        <div style="position: absolute; inset: 0; background: rgba(0, 0, 0, 0.35); z-index: 2; pointer-events: none;"></div>
                    </div>
                </div>
                <div style="position: absolute; bottom: 15px; right: 15px; z-index: 5; display: flex; gap: 6px;">
                    <span class="car-dot active" style="width: 6px; height: 6px; border-radius: 50%; background: #00d2ff; box-shadow: 0 0 6px #00d2ff; cursor: pointer;"></span>
                    <span class="car-dot" style="width: 6px; height: 6px; border-radius: 50%; background: rgba(255,255,255,0.4); cursor: pointer;"></span>
                </div>
            </div>
            
            <div class="info-box">
                <div class="columna">
                    <h2>EXPLORA FOZ DO IGUAÇU CON NOSOTROS</h2>
                    <p>
                        Descubrir la inmensidad de las Cataratas y la biodiversidad única de la selva paranaense es una experiencia unforgettable. Nos complace acompañarte de forma cercana y segura, ofreciendo un servicio de traslados privados diseñado a tu medida.
                    </p>
                </div>
                <div class="columna">
                    <p>
                        Nos encargamos de toda la logística: desde recogidas puntuales en los aeropuertos de la región hasta los cruces fronterizos hacia Argentina y Paraguay, facilitando los trámites aduaneros para que tu única preocupación sea disfrutar de la naturaleza. Además, organizamos paseos confortables dentro del territorio brasileño, garantizando itinerarios flexibles tanto para viajeros individuales como para familias y grupos organizados. Nuestro guiado incluye comunicación accesible en español, portugués y LIBRAS, buscando siempre brindar un trato cálido y humano.
                    </p>
                    <div style="border-top: 1px solid rgba(255, 255, 255, 0.15); padding-top: 20px; margin-top: 20px;">
                        <h3 style="color: #00d2ff; font-family: 'Montserrat', sans-serif; font-weight: 800; font-size: 1.1rem; margin: 0 0 8px 0; text-transform: uppercase; letter-spacing: 0.5px;">Naturaleza &amp; Paseos</h3>
                        <p style="font-size: 0.95rem; opacity: 0.85; margin: 0; line-height: 1.4;">Tours guiados por las Cataratas y los rincones más bellos de la región.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="galeria" class="galeria-franja">
        <div class="galeria-overlay"></div>
        <div class="galeria-slides-container" style="width: 100%; height: 100%; position: relative;">
            <div class="galeria-slide active">
                <img src="images/cataratas.jpg" alt="Cataratas del Iguazú" class="galeria-img">
                <div class="galeria-content">
                    <span class="galeria-title">Cataratas del Iguazú</span>
                    <span class="galeria-subtitle">Una de las siete maravillas naturales del mundo</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/aeroporto.jpg" alt="Traslados al Aeropuerto" class="galeria-img" loading="lazy">
                <div class="galeria-content">
                    <span class="galeria-title">Traslados al Aeropuerto</span>
                    <span class="galeria-subtitle">Puntualidad y confort 24/7 en la Triple Frontera</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/templo_budista.webp" alt="Templo Budista Chen Tien" class="galeria-img" loading="lazy">
                <div class="galeria-content">
                    <span class="galeria-title">Templo Budista Chen Tien</span>
                    <span class="galeria-subtitle">Paz, meditación y espectaculares esculturas en Foz</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/mezquita1.jpg" alt="Mezquita Omar Ibn Al-Khattab" class="galeria-img" style="object-fit: contain; background-color: #050510;" loading="lazy">
                <div class="galeria-content">
                    <span class="galeria-title">Mezquita Omar Ibn Al-Khattab</span>
                    <span class="galeria-subtitle">Arquitectura islámica y riqueza cultural en el corazón de Foz</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/cataratas_panorama.webp" alt="Vistas Panorámicas" class="galeria-img" loading="lazy">
                <div class="galeria-content">
                    <span class="galeria-title">Vistas Panorámicas</span>
                    <span class="galeria-subtitle">Paisajes únicos e inolvidables de la selva</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/china.webp" alt="Cultura y Sabores" class="galeria-img" loading="lazy">
                <div class="galeria-content">
                    <span class="galeria-title">Cultura y Sabores</span>
                    <span class="galeria-subtitle">Experiencias gastronómicas y multiculturales locales</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/dutty.jpeg" alt="Duty Free Shop" class="galeria-img" loading="lazy">
                <div class="galeria-content">
                    <span class="galeria-title">Duty Free Shop</span>
                    <span class="galeria-subtitle">Compras internacionales exclusivas libre de impuestos</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/feirinha argentina.jpeg" alt="Feirinha de Puerto Iguazú" class="galeria-img" loading="lazy">
                <div class="galeria-content">
                    <span class="galeria-title">Feirinha de Puerto Iguazú</span>
                    <span class="galeria-subtitle">Sabores locales, olivas y quesos tradicionales</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/Kattamaram (2).jpeg" alt="Paseo en Kattamaram" class="galeria-img" loading="lazy">
                <div class="galeria-content">
                    <span class="galeria-title">Paseo en Kattamaram</span>
                    <span class="galeria-subtitle">Navegación inolvidable en el encuentro de los ríos</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/museo_de_cera.webp" alt="Dreamland Museo de Cera" class="galeria-img" loading="lazy">
                <div class="galeria-content">
                    <span class="galeria-title">Dreamland Museo de Cera</span>
                    <span class="galeria-subtitle">Diversión para toda la familia con réplicas perfectas</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/pda.webp" alt="Parque de las Aves" class="galeria-img" loading="lazy">
                <div class="galeria-content">
                    <span class="galeria-title">Parque de las Aves</span>
                    <span class="galeria-subtitle">Contacto directo con la fauna y aves rescatadas</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/usina hidrelectrica.jpeg" alt="Itaipú Binacional" class="galeria-img" loading="lazy">
                <div class="galeria-content">
                    <span class="galeria-title">Itaipú Binacional</span>
                    <span class="galeria-subtitle">Una de las mayores obras de ingeniería del planeta</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/wonder_park_v2.jpg" alt="Wonder Park Show" class="galeria-img" loading="lazy">
                <div class="galeria-content">
                    <span class="galeria-title">Wonder Park Show</span>
                    <span class="galeria-subtitle">Espectáculos de luces y atracciones interactivas</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/yup star.jpeg" alt="Yup Star Foz" class="galeria-img" loading="lazy">
                <div class="galeria-content">
                    <span class="galeria-title">Yup Star Foz</span>
                    <span class="galeria-subtitle">Una de las ruedas de la fortuna más grandes de América Latina</span>
                </div>
            </div>
        </div>
        <button class="galeria-nav-btn prev" aria-label="Anterior">&#x276E;</button>
        <button class="galeria-nav-btn next" aria-label="Siguiente">&#x276F;</button>
        <div class="galeria-dots"></div>
    </section>

    <footer>
        <div class="social-buttons-footer">
            <a href="mailto:trifozturismo@gmail.com" class="btn-social btn-email" aria-label="Enviar Email"><i class="fa-solid fa-envelope"></i></a>
            <a href="https://www.facebook.com/share/1Qr8RiKxrz/" target="_blank" rel="noopener noreferrer" class="btn-social btn-facebook" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
            <a href="https://www.instagram.com/trifoz.turismo" target="_blank" rel="noopener noreferrer" class="btn-social btn-instagram" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
        </div>
        <p>© 2026 Trifoz Turismo • Guía Turístico Ebert • Foz de Iguazú</p>
    </footer>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/Draggable.min.js"></script>

    <script>
        document.addEventListener('DOMContentLoaded', function () {
            // --- CONFIGURACIÓN INICIAL DE LOGÍSTICA ---
            function setDefaultDatetime() {
                const tomorrow = new Date();
                tomorrow.setDate(tomorrow.getDate() + 1);
                const pad = n => String(n).padStart(2, '0');
                const val = `${tomorrow.getFullYear()}-${pad(tomorrow.getMonth() + 1)}-${pad(tomorrow.getDate())}T09:00`;
                const dtEl = document.getElementById('booking-datetime');
                const dtElM = document.getElementById('booking-datetime-m');
                if (dtEl && !dtEl.value) dtEl.value = val;
                if (dtElM && !dtElM.value) dtElM.value = val;

                function openPicker() {
                    try { if (typeof this.showPicker === 'function') this.showPicker(); } catch (e) { }
                }
                dtEl?.addEventListener('click', openPicker);
                dtElM?.addEventListener('click', openPicker);
            }
            setDefaultDatetime();

            // --- CONTADORES DE PASAJEROS ---
            const displayDesktop = document.getElementById('pax-display');
            document.getElementById('pax-minus')?.addEventListener('click', function (e) {
                e.preventDefault();
                let val = parseInt(displayDesktop.textContent) || 2;
                if (val > 1) displayDesktop.textContent = val - 1;
            });
            document.getElementById('pax-plus')?.addEventListener('click', function (e) {
                e.preventDefault();
                let val = parseInt(displayDesktop.textContent) || 2;
                if (val < 8) displayDesktop.textContent = val + 1;
            });

            const displayMobile = document.getElementById('pax-display-m');
            document.getElementById('pax-minus-m')?.addEventListener('click', function (e) {
                e.preventDefault();
                let val = parseInt(displayMobile.textContent) || 2;
                if (val > 1) displayMobile.textContent = val - 1;
            });
            document.getElementById('pax-plus-m')?.addEventListener('click', function (e) {
                e.preventDefault();
                let val = parseInt(displayMobile.textContent) || 2;
                if (val < 8) displayMobile.textContent = val + 1;
            });

            // --- PANEL MÓVIL ---
            const panel = document.getElementById('booking-mobile-panel');
            const overlay = document.getElementById('booking-overlay');
            document.getElementById('booking-mobile-trigger')?.addEventListener('click', function (e) {
                e.preventDefault();
                panel.classList.add('open');
                overlay.classList.add('open');
            });
            function cerrarPanel() { panel.classList.remove('open'); overlay.classList.remove('open'); }
            document.getElementById('booking-mobile-close')?.addEventListener('click', cerrarPanel);
            overlay?.addEventListener('click', cerrarPanel);

            // --- DROPDOWNS SELECCIÓN ---
            function setupCustomDropdown(triggerId, menuId, inputId) {
                const trigger = document.getElementById(triggerId);
                const menu = document.getElementById(menuId);
                const input = document.getElementById(inputId);
                if (!trigger || !menu || !input) return;

                trigger.setAttribute('tabindex', '0');
                trigger.setAttribute('role', 'button');
                trigger.setAttribute('aria-haspopup', 'listbox');

                trigger.addEventListener('click', function (e) {
                    e.stopPropagation();
                    document.querySelectorAll('.dropdown-menu').forEach(m => { if (m !== menu) m.classList.remove('show'); });
                    menu.classList.toggle('show');
                });

                trigger.addEventListener('keydown', function (e) {
                    if (e.key === 'Enter' || e.key === ' ') {
                        e.preventDefault();
                        trigger.click();
                    }
                });

                menu.addEventListener('click', function (e) {
                    const item = e.target.closest('.dropdown-item');
                    if (item) {
                        input.value = item.getAttribute('data-value');
                        const span = trigger.querySelector('span');
                        if (span) {
                            span.textContent = item.textContent.replace(/BR|AR|PY/g, '').trim();
                        }
                        menu.classList.remove('show');
                        trigger.focus();
                    }
                });
            }
            setupCustomDropdown('trigger-destino', 'menu-destino', 'booking-destino');
            setupCustomDropdown('trigger-destino-m', 'menu-destino-m', 'booking-destino-m');

            document.addEventListener('click', function () {
                document.querySelectorAll('.dropdown-menu').forEach(m => m.classList.remove('show'));
            });

            // --- ENVÍO WHATSAPP ---
            function enviarWhatsApp(isMobile) {
                let destino = document.getElementById(isMobile ? 'booking-destino-m' : 'booking-destino').value;
                let pax = document.getElementById(isMobile ? 'pax-display-m' : 'pax-display').textContent;
                let fechaRaw = document.getElementById(isMobile ? 'booking-datetime-m' : 'booking-datetime').value;

                if (!destino) {
                    alert("Por favor selecciona un destino de la lista.");
                    return;
                }

                let fechaObj = new Date(fechaRaw);
                let dia = String(fechaObj.getDate()).padStart(2, '0');
                let mes = String(fechaObj.getMonth() + 1).padStart(2, '0');
                let anio = fechaObj.getFullYear();
                let hora = String(fechaObj.getHours()).padStart(2, '0');
                let min = String(fechaObj.getMinutes()).padStart(2, '0');
                let fechaFormateada = `${dia}/${mes}/${anio} a las ${hora}:${min}`;

                let mensaje = "";
                if (destino === 'Itinerario Personalizado') {
                    mensaje = `¡Hola! Me gustaría recibir ayuda para armar un itinerario personalizado.\n\n*Detalles iniciales:*\n👥 Pasajeros: ${pax}\n📅 Fecha de llegada: ${fechaFormateada}`;
                } else {
                    mensaje = `¡Hola! Me gustaría solicitar un presupuesto para el siguiente tour/traslado:\n\n📍 Destino: ${destino}\n👥 Pasajeros: ${pax}\n📅 Fecha y Hora: ${fechaFormateada}`;
                }

                let numero = "5545933003337";
                let url = `https://wa.me/${numero}?text=${encodeURIComponent(mensaje)}`;
                window.open(url, '_blank');
            }

            document.getElementById('booking-submit-btn')?.addEventListener('click', function (e) {
                e.preventDefault();
                enviarWhatsApp(false);
            });

            document.getElementById('booking-submit-btn-m')?.addEventListener('click', function (e) {
                e.preventDefault();
                enviarWhatsApp(true);
            });

            // --- INTERACCIÓN TOUCH TARJETAS CATÁLOGO ---
            document.querySelectorAll('.card').forEach(card => {
                if (!card.classList.contains('video-card')) {
                    card.addEventListener('click', function () {
                        document.querySelectorAll('.card').forEach(c => { if (c !== card) c.classList.remove('touch-active'); });
                        card.classList.toggle('touch-active');
                    });
                }
            });

            // ==========================================================================
            // NÚCLEO OPTIMIZADO: CARRUSEL 3D COVERFLOW (SOLUCIÓN NOTEBOOK LAPTOP)
            // ==========================================================================
            gsap.registerPlugin(Draggable);

            const carousel = document.getElementById('carousel');
            const cards3D = document.querySelectorAll('.card-item-3d');
            const dotsContainer = document.getElementById('dotsContainer3D');
            const numCards3D = cards3D.length;
            
            let currentIndex = 4; 
            let autoplayTimeout3D = null;
            let lastActiveIndex = -1;
            const dragProxy3D = document.createElement("div");

            const destinations = [
                { title: "Cataratas del Iguazú", subtitle: "Siente la fuerza de las Siete Maravillas Naturales en un recorrido privado y exclusivo en la selva.", bgTitle: "CATARATAS", dest: "Cataratas del Iguazú (Argentina)" },
                { title: "Macuco Safari", subtitle: "Navegación extrema en bote bimotor hasta el corazón de las caídas de agua. Emoción y adrenalina pura.", bgTitle: "AVENTURA", dest: "Macuco Safari" },
                { title: "City Tour Foz", subtitle: "Descubre la diversidad de la Triple Frontera: el Templo Budista, la Mezquita y el Hito de las 3 Fronteras.", bgTitle: "CITY TOUR", dest: "Hito de las 3 Fronteras" },
                { title: "Premium Hotel", subtitle: "Traslados exclusivos a los mejores resorts, hoteles y paseos de compras libres de impuestos (Duty Free).", bgTitle: "HOTEL", dest: "Traslado para Hoteles" },
                { title: "Familia Tour", subtitle: "Navegación familiar premium y confortable. Disfruta del atardecer donde se unen los ríos Paraná e Iguazú.", bgTitle: "FAMILIA", dest: "Kattamaram II" },
                { title: "Puerto de Iguazú", subtitle: "Cruza la frontera y disfruta de la mejor gastronomía argentina: parrilladas, vinos selectos y compras.", bgTitle: "ARGENTINA", dest: "Paseo Puerto Iguazú" },
                { title: "Ciudad del Este", subtitle: "Tu guía de compras seguro en Paraguay. Encuentra tecnología, perfumes y marcas exclusivas a precios increíbles.", bgTitle: "COMPRAS", dest: "Compras Ciudad del Este" },
                { title: "Marco 3 Fronteras", subtitle: "El único lugar en el mundo donde tres países se abrazan. Disfruta de un atardecer mágico, shows y vista panorámica.", bgTitle: "FRONTERA", dest: "Paseo Paraguay" },
                { title: "Parque de las Aves", subtitle: "Camina entre tucanes, guacamayos y especies exóticas en un santuario ecológico único integrado en la selva.", bgTitle: "AVES", dest: "Parque de las Aves" }
            ];

            // Inicializar puntos de navegación
            dotsContainer.innerHTML = '';
            for (let i = 0; i < numCards3D; i++) {
                const dot = document.createElement('span');
                dot.className = `dot-3d ${i === currentIndex ? 'is-active' : ''}`;
                dot.addEventListener('click', () => {
                    if (i === currentIndex) return;
                    currentIndex = i;
                    updateLayout();
                    startAutoplay3D();
                });
                dotsContainer.appendChild(dot);
            }

            let cardWidth, cardHeight, xOffset, zDepth, yRotation;

            function updateLayoutParameters() {
                const w = window.innerWidth;
                if (w < 480) {
                    cardWidth = 130; cardHeight = 200; xOffset = 70; zDepth = -120; yRotation = 45;
                } else if (w < 768) {
                    cardWidth = 160; cardHeight = 250; xOffset = 100; zDepth = -140; yRotation = 50;
                } else if (w < 1024) {
                    cardWidth = 195; cardHeight = 295; xOffset = 125; zDepth = -160; yRotation = 55;
                } else {
                    cardWidth = 220; cardHeight = 330; xOffset = 150; zDepth = -180; yRotation = 55;
                }
                carousel.style.setProperty('--card-width', `${cardWidth}px`);
                carousel.style.setProperty('--card-height', `${cardHeight}px`);
                updateLayout();
            }

            function updateLayout() {
                cards3D.forEach((card, index) => {
                    const diff = index - currentIndex;
                    if (diff === 0) {
                        gsap.to(card, { x: 0, z: 0, rotationY: 0, duration: 0.5, ease: "power2.out", overwrite: "auto" });
                        card.style.zIndex = 10;
                        card.style.filter = "brightness(100%)";
                        card.style.opacity = "1";
                        card.classList.add('is-active');
                        
                        if (index !== lastActiveIndex) {
                            lastActiveIndex = index;
                            updateActiveInfoText(index);
                        }
                    } else if (diff > 0) {
                        gsap.to(card, { x: diff * xOffset, z: zDepth, rotationY: -yRotation, duration: 0.5, ease: "power2.out", overwrite: "auto" });
                        card.style.zIndex = 10 - diff;
                        card.style.filter = "brightness(45%)";
                        card.style.opacity = diff > 2 ? "0" : "1";
                        card.classList.remove('is-active');
                    } else {
                        gsap.to(card, { x: diff * xOffset, z: zDepth, rotationY: yRotation, duration: 0.5, ease: "power2.out", overwrite: "auto" });
                        card.style.zIndex = 10 + diff;
                        card.style.filter = "brightness(45%)";
                        card.style.opacity = diff < -2 ? "0" : "1";
                        card.classList.remove('is-active');
                    }
                });
            }

            function updateActiveInfoText(index) {
                document.querySelectorAll('.dot-3d').forEach((dot, idx) => {
                    dot.classList.toggle('is-active', idx === index);
                });
                
                gsap.to(".active-info-container", {
                    y: 10, opacity: 0, duration: 0.2,
                    onComplete: () => {
                        document.getElementById("activeTitle").textContent = destinations[index].title;
                        document.getElementById("activeSubtitle").textContent = destinations[index].subtitle;
                        document.getElementById("activeCardBtn")?.setAttribute("data-dest", destinations[index].dest);
                        gsap.to(".active-info-container", { y: 0, opacity: 1, duration: 0.3, ease: "power2.out" });
                    }
                });
                
                gsap.to(".bg-text-back", {
                    opacity: 0, scale: 0.95, duration: 0.2,
                    onComplete: () => {
                        document.querySelector(".bg-text-back").textContent = destinations[index].bgTitle;
                        gsap.to(".bg-text-back", { opacity: 0.04, scale: 1, duration: 0.3, ease: "power2.out" });
                    }
                });
            }

            document.getElementById('prevBtn3D')?.addEventListener('click', () => {
                currentIndex = (currentIndex - 1 + numCards3D) % numCards3D;
                updateLayout();
                startAutoplay3D();
            });
            document.getElementById('nextBtn3D')?.addEventListener('click', () => {
                currentIndex = (currentIndex + 1) % numCards3D;
                updateLayout();
                startAutoplay3D();
            });

            // UNIFICACIÓN ESTRATÉGICA DEL MANEJO DE CLICS (Previene el congelamiento en PC)
            cards3D.forEach((card, index) => {
                card.addEventListener('click', (e) => {
                    if (e.target.closest('.card-btn-action') || e.target.closest('a')) return;
                    e.preventDefault();
                    
                    if (index !== currentIndex) {
                        currentIndex = index;
                        updateLayout();
                        startAutoplay3D();
                    } else {
                        // Solo abre el Lightbox si ya es la tarjeta activa en el centro
                        openLightbox(index);
                    }
                });
            });

            // ACCIÓN DEL BOTÓN CENTRAL DE RESERVA DE TARJETA ACTIVA
            document.querySelectorAll('.card-btn-action, #activeCardBtn').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    const destination = btn.getAttribute('data-dest');
                    if(!destination) return;
                    
                    const isMobile = window.innerWidth < 768;
                    document.getElementById('booking-destino').value = destination;
                    document.getElementById('booking-destino-m').value = destination;
                    
                    const cleanDestName = destination.replace(/BR|AR|PY/g, '').trim();
                    document.getElementById('trigger-destino').querySelector('span').textContent = cleanDestName;
                    document.getElementById('trigger-destino-m').querySelector('span').textContent = cleanDestName;
                    
                    if (isMobile) {
                        panel.classList.add('open');
                        overlay.classList.add('open');
                    } else {
                        const bBar = document.querySelector('.booking-bar');
                        bBar?.scrollIntoView({ behavior: 'smooth', block: 'center' });
                        if (bBar) {
                            bBar.style.transform = 'scale(1.03)';
                            bBar.style.boxShadow = '0 0 30px rgba(0, 210, 255, 0.5)';
                            setTimeout(() => { bBar.style.transform = ''; bBar.style.boxShadow = ''; }, 1200);
                        }
                    }
                });
            });

            // DRAGGABLE POR PROXY
            let startDragX = 0;
            Draggable.create(dragProxy3D, {
                trigger: ".carousel-viewport-3d",
                type: "x",
                onDragStart: function() { stopAutoplay3D(); startDragX = this.x; },
                onDragEnd: function() {
                    const change = this.x - startDragX;
                    if (change > 40) currentIndex = (currentIndex - 1 + numCards3D) % numCards3D;
                    else if (change < -40) currentIndex = (currentIndex + 1) % numCards3D;
                    updateLayout();
                    gsap.set(dragProxy3D, { x: 0 });
                    startAutoplay3D();
                }
            });

            // SOPORTE RUEDA MOUSE (Ajustado para no bloquear el scroll de la notebook)
            document.querySelector('.carousel-viewport-3d')?.addEventListener('wheel', (e) => {
                if (Math.abs(e.deltaX) > 10 || Math.abs(e.deltaY) > 15) {
                    e.preventDefault();
                    stopAutoplay3D();
                    if (e.deltaY > 0 || e.deltaX > 0) currentIndex = (currentIndex + 1) % numCards3D;
                    else currentIndex = (currentIndex - 1 + numCards3D) % numCards3D;
                    updateLayout();
                    startAutoplay3D();
                }
            }, { passive: false });

            function startAutoplay3D() {
                clearInterval(autoplayTimeout3D);
                autoplayTimeout3D = setInterval(() => {
                    currentIndex = (currentIndex + 1) % numCards3D;
                    updateLayout();
                }, 5000);
            }
            function stopAutoplay3D() { clearInterval(autoplayTimeout3D); }

            updateLayoutParameters();
            window.addEventListener('resize', updateLayoutParameters);
            startAutoplay3D();

            // --- LIGHTBOX MODAL ---
            const lightbox = document.getElementById('lightboxModal');
            const lightboxImg = document.getElementById('lightboxImg');
            const lightboxCaption = document.getElementById('lightboxCaption');

            function openLightbox(index) {
                const targetCard = cards3D[index];
                if (!targetCard) return;
                const src = targetCard.getAttribute('data-src');
                if (!src) return;

                lightboxImg.src = src;
                lightboxCaption.textContent = destinations[index] ? destinations[index].title : "Trifoz Turismo";
                lightbox.style.display = 'flex';
                setTimeout(() => lightbox.style.opacity = '1', 50);
                stopAutoplay3D();
            }

            function closeLightbox() {
                lightbox.style.opacity = '0';
                setTimeout(() => { lightbox.style.display = 'none'; startAutoplay3D(); }, 400);
            }

            lightbox?.addEventListener('click', closeLightbox);
            document.getElementById('closeLightbox')?.addEventListener('click', closeLightbox);

            // --- GALERÍA KEN BURNS INFRAESTRUCTURA ---
            (function() {
                const slides = document.querySelectorAll('.galeria-slide');
                const gDots = document.querySelector('.galeria-dots');
                let gIdx = 0, gInterval;
                
                if (gDots && slides.length) {
                    gDots.innerHTML = '';
                    slides.forEach((_, idx) => {
                        const dot = document.createElement('span');
                        dot.className = `galeria-dot ${idx === 0 ? 'active' : ''}`;
                        dot.addEventListener('click', () => { showSlide(idx); });
                        gDots.appendChild(dot);
                    });
                }
                
                function showSlide(index) {
                    if (!slides.length) return;
                    slides[gIdx].classList.remove('active');
                    document.querySelectorAll('.galeria-dot')[gIdx]?.classList.remove('active');
                    gIdx = (index + slides.length) % slides.length;
                    slides[gIdx].classList.add('active');
                    document.querySelectorAll('.galeria-dot')[gIdx]?.classList.add('active');
                }

                function nextSlide() { showSlide(gIdx + 1); }
                function prevSlide() { showSlide(gIdx - 1); }
                
                document.querySelector('.galeria-nav-btn.prev')?.addEventListener('click', () => { prevSlide(); startG(); });
                document.querySelector('.galeria-nav-btn.next')?.addEventListener('click', () => { nextSlide(); startG(); });
                
                function startG() { clearInterval(gInterval); gInterval = setInterval(nextSlide, 6000); }
                startG();
            })();

            // --- INTERMITENCIA AUTOPLAY VEHÍCULOS ---
            (function() {
                const carSlides = document.querySelectorAll('.car-slide');
                const carDots = document.querySelectorAll('.car-dot');
                let carIdx = 0;
                if (carSlides.length > 1) {
                    setInterval(() => {
                        carSlides[carIdx].style.opacity = '0';
                        carSlides[carIdx].classList.remove('active');
                        if (carDots[carIdx]) carDots[carIdx].className = 'car-dot';
                        carIdx = (carIdx + 1) % carSlides.length;
                        carSlides[carIdx].style.opacity = '1';
                        carSlides[carIdx].classList.add('active');
                        if (carDots[carIdx]) carDots[carIdx].className = 'car-dot active';
                    }, 4000);
                }
            })();

            // --- MODALES EXTRA (INGRESOS / VIDEOS) ---
            (function() {
                const mIngresos = document.getElementById('modalIngresos');
                const mVideos = document.getElementById('modalVideos');
                
                document.getElementById('btn-ingresos')?.addEventListener('click', () => {
                    mIngresos.style.display = 'flex'; setTimeout(() => mIngresos.style.opacity = '1', 50);
                });
                document.getElementById('btn-videos')?.addEventListener('click', () => {
                    mVideos.style.display = 'flex'; setTimeout(() => mVideos.style.opacity = '1', 50);
                });

                function closeM(modal) {
                    if (!modal) return;
                    modal.style.opacity = '0';
                    setTimeout(() => {
                        modal.style.display = 'none';
                        modal.querySelectorAll('video').forEach(v => v.pause());
                    }, 400);
                }

                document.getElementById('closeIngresos')?.addEventListener('click', () => closeM(mIngresos));
                document.getElementById('closeVideos')?.addEventListener('click', () => closeM(mVideos));
                mIngresos?.addEventListener('click', (e) => { if (e.target === mIngresos) closeM(mIngresos); });
                mVideos?.addEventListener('click', (e) => { if (e.target === mVideos) closeM(mVideos); });
            })();
        });
    </script>"""

# Write a python script to replace the content of index.html between <section class="attractions"> and the </script> tag at the end.
with open("index.html", "r", encoding="utf-8") as f:
    html_es = f.read()

# Replace using regex
pattern = re.compile(r'<section class="attractions">.*?</script>', re.DOTALL)
if pattern.search(html_es):
    new_html_es = pattern.sub(pasted_code, html_es)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_html_es)
    print("ES file updated successfully!")
else:
    print("Error: Pattern not found in ES file!")

# Now do the same for PT file, but we should make sure we keep the Portuguese texts!
# Wait, let's write a python script to translate the labels to Portuguese in the pasted code for the PT file.
