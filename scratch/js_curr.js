    <script>
        document.addEventListener('DOMContentLoaded', function () {
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

            function setupCustomDropdown(triggerId, menuId, inputId) {
                const trigger = document.getElementById(triggerId);
                const menu = document.getElementById(menuId);
                const input = document.getElementById(inputId);
                if (!trigger || !menu || !input) return;

                // Hacer focusable con teclado
                trigger.setAttribute('tabindex', '0');
                trigger.setAttribute('role', 'button');
                trigger.setAttribute('aria-haspopup', 'listbox');

                // Clic del mouse
                trigger.addEventListener('click', function (e) {
                    e.stopPropagation();
                    document.querySelectorAll('.dropdown-menu').forEach(m => { if (m !== menu) m.classList.remove('show'); });
                    menu.classList.toggle('show');
                });

                // Teclado (ENTER o ESPACIO)
                trigger.addEventListener('keydown', function (e) {
                    if (e.key === 'Enter' || e.key === ' ') {
                        e.preventDefault();
                        trigger.click();
                    }
                });

                // Clic en items del menú
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

            // Lógica Touch para tarjetas (Mostrar/Ocultar texto al tocar)
            document.querySelectorAll('.card').forEach(card => {
                if (!card.classList.contains('video-card')) {
                    card.addEventListener('click', function (e) {
                        // Ocultamos en las demás
                        document.querySelectorAll('.card').forEach(c => {
                            if (c !== card) c.classList.remove('touch-active');
                        });
                        // Alternamos en la actual
                        card.classList.toggle('touch-active');
                    });
                }
            });

            // ACORDEÓN OTRAS ATRACCIONES
            const btnAcordeon = document.getElementById('btnOtrasAtracciones');
            const acordeonContenido = document.getElementById('acordeonContenido');
            if (btnAcordeon && acordeonContenido) {
                btnAcordeon.addEventListener('click', function () {
                    btnAcordeon.classList.toggle('active');
                    acordeonContenido.classList.toggle('open');
                    if (acordeonContenido.classList.contains('open')) {
                        acordeonContenido.style.maxHeight = acordeonContenido.scrollHeight + "px";
                    } else {
                        acordeonContenido.style.maxHeight = "0";
                    }
                });
            }
            // NÚCLEO OPTIMIZADO: CARRUSEL 3D COVERFLOW (ESPEJO & RESPONSIVE)
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
                    if (!destination) return;

                    const isMobile = window.innerWidth < 768;
                    const destInputDesktop = document.getElementById('booking-destino');
                    const destInputMobile = document.getElementById('booking-destino-m');
                    const triggerDesktop = document.getElementById('trigger-destino');
                    const triggerMobile = document.getElementById('trigger-destino-m');

                    if (destInputDesktop) destInputDesktop.value = destination;
                    if (destInputMobile) destInputMobile.value = destination;

                    const cleanDestName = destination.replace(/BR|AR|PY/g, '').trim();
                    if (triggerDesktop && triggerDesktop.querySelector('span')) triggerDesktop.querySelector('span').textContent = cleanDestName;
                    if (triggerMobile && triggerMobile.querySelector('span')) triggerMobile.querySelector('span').textContent = cleanDestName;

                    if (isMobile) {
                        const mobPanel = document.getElementById('booking-mobile-panel');
                        const mobOverlay = document.getElementById('booking-overlay');
                        if (mobPanel && mobOverlay) {
                            mobPanel.classList.add('open');
                            mobOverlay.classList.add('open');
                        }
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
                onDragStart: function () { stopAutoplay3D(); startDragX = this.x; },
                onDragEnd: function () {
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
            const prevLightboxBtn = document.getElementById('prevLightbox');
            const nextLightboxBtn = document.getElementById('nextLightbox');
            let currentLightboxIndex = 0;

            function openLightbox(index) {
                currentLightboxIndex = index;
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

            function nextLightboxImage() {
                currentLightboxIndex = (currentLightboxIndex + 1) % numCards3D;
                openLightbox(currentLightboxIndex);
            }

            function prevLightboxImage() {
                currentLightboxIndex = (currentLightboxIndex - 1 + numCards3D) % numCards3D;
                openLightbox(currentLightboxIndex);
            }

            lightbox?.addEventListener('click', (e) => {
                if (e.target === lightbox || e.target === lightboxImg || e.target === document.getElementById('closeLightbox')) {
                    closeLightbox();
                }
            });

            document.getElementById('closeLightbox')?.addEventListener('click', closeLightbox);

            prevLightboxBtn?.addEventListener('click', (e) => {
                e.stopPropagation();
                prevLightboxImage();
            });

            nextLightboxBtn?.addEventListener('click', (e) => {
                e.stopPropagation();
                nextLightboxImage();
            });

            document.addEventListener('keydown', (e) => {
                if (lightbox && lightbox.style.display === 'flex') {
                    if (e.key === 'Escape') closeLightbox();
                    if (e.key === 'ArrowRight') nextLightboxImage();
                    if (e.key === 'ArrowLeft') prevLightboxImage();
                }
            });

            // --- GALERÍA KEN BURNS INFRAESTRUCTURA ---
            (function () {
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

                // Soporte para gestos swipe táctiles en móviles para cambiar imágenes
                const galeriaFranja = document.querySelector('.galeria-franja');
                if (galeriaFranja) {
                    let touchStartX = 0;
                    let touchEndX = 0;

                    galeriaFranja.addEventListener('touchstart', (e) => {
                        touchStartX = e.changedTouches[0].screenX;
                    }, { passive: true });

                    galeriaFranja.addEventListener('touchend', (e) => {
                        touchEndX = e.changedTouches[0].screenX;
                        const diffX = touchEndX - touchStartX;
                        if (Math.abs(diffX) > 50) { // Sensibilidad del swipe
                            if (diffX < 0) {
                                nextSlide(); // Deslizar a la izquierda: siguiente
                            } else {
                                prevSlide(); // Deslizar a la derecha: anterior
                            }
                            startG();
                        }
                    }, { passive: true });
                }

                // Desplazamiento suave para enlaces de anclaje
                document.querySelectorAll('a[href^="#galeria"]').forEach(anchor => {
                    anchor.addEventListener('click', function (e) {
                        e.preventDefault();
                        const target = document.querySelector(this.getAttribute('href'));
                        if (target) {
                            target.scrollIntoView({ behavior: 'smooth' });
                        }
                    });
                });
            })();

            // --- INTERMITENCIA AUTOPLAY VEHÍCULOS ---
            (function () {
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
            (function () {
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





    </script>