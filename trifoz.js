
/** Load Font Awesome without inline event handlers (CSP-safe). */
(function loadFontAwesome() {
    if (document.querySelector('link[data-fa]')) return;
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css';
    link.integrity = 'sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw==';
    link.crossOrigin = 'anonymous';
    link.referrerPolicy = 'no-referrer';
    link.setAttribute('data-fa', '1');
    document.head.appendChild(link);
})();

document.addEventListener('DOMContentLoaded', function () {
            const i18nEl = document.getElementById('trifoz-i18n');
            const i18n = i18nEl ? JSON.parse(i18nEl.textContent) : {};
            const destinations = i18n.destinations || [];

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
                    alert(i18n.alertSelectDestination || "Select a destination.");
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
                const customValues = i18n.customItineraryValues || ['Itinerario Personalizado'];
                if (customValues.includes(destino)) {
                    mensaje = (i18n.msgCustomItinerary || '')
                        .replace('{pax}', pax)
                        .replace('{fecha}', fechaFormateada);
                } else {
                    mensaje = (i18n.msgQuote || '')
                        .replace('{destino}', destino)
                        .replace('{pax}', pax)
                        .replace('{fecha}', fechaFormateada);
                }

                let numero = "5545933003337";
                let url = `https://wa.me/${numero}?text=${encodeURIComponent(mensaje)}`;
                window.open(url, '_blank', 'noopener,noreferrer');
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
                    this.classList.toggle('active');
                    acordeonContenido.classList.toggle('open');
                });
            }

            // ==========================================================================
            // LOGICA DEL CARRUSEL 3D COVERFLOW (ESPEJO & RESPONSIVE)
            // ==========================================================================
            gsap.registerPlugin(Draggable);

            const carousel = document.getElementById('carousel');
            const cards3D = document.querySelectorAll('.card-item-3d');
            const dotsContainer = document.getElementById('dotsContainer3D');
            const numCards3D = cards3D.length;

            let currentIndex = 4; // Iniciar al centro (quinta tarjeta de nueve)
            let autoplayTimeout3D = null;
            let lastActiveIndex = -1;
            const dragProxy3D = document.createElement("div");

            // Datos de los destinos para las transiciones de texto

            // Generar puntos de navegación (dots)
            dotsContainer.innerHTML = '';
            for (let i = 0; i < numCards3D; i++) {
                const dot = document.createElement('span');
                dot.className = `dot-3d ${i === currentIndex ? 'is-active' : ''}`;
                dot.setAttribute('data-index', i);
                dot.addEventListener('click', () => {
                    if (i === currentIndex) return;
                    currentIndex = i;
                    updateLayout();
                    stopAutoplay3D();
                    startAutoplay3D();
                });
                dotsContainer.appendChild(dot);
            }

            // Parámetros responsive de Coverflow
            let cardWidth, cardHeight, xOffset, zDepth, yRotation;

            function updateLayoutParameters() {
                const w = window.innerWidth;

                if (w < 480) {
                    cardWidth = 150;    // Vertical en móviles
                    cardHeight = 240;   // Proporción ~5:8
                    xOffset = 70;
                    zDepth = -120;
                    yRotation = 45;
                } else if (w < 768) {
                    cardWidth = 180;    // Tablets verticales
                    cardHeight = 290;
                    xOffset = 100;
                    zDepth = -140;
                    yRotation = 50;
                } else if (w <= 1200) {
                    // 💻 OPTIMIZADO PARA NOTEBOOKS: Tarjetas verticales grandes y visibles
                    cardWidth = 240;
                    cardHeight = 380;
                    xOffset = 150;      // Separación equilibrada para laptops
                    zDepth = -160;
                    yRotation = 45;     // Rotación suave para que se aprecie toda la foto
                } else {
                    cardWidth = 260;    // Pantallas grandes de escritorio
                    cardHeight = 420;
                    xOffset = 180;
                    zDepth = -180;
                    yRotation = 50;
                }

                carousel.style.setProperty('--card-width', `${cardWidth}px`);
                carousel.style.setProperty('--card-height', `${cardHeight}px`);

                updateLayout();
            }

            function updateLayout() {
                cards3D.forEach((card, index) => {
                    const diff = index - currentIndex;

                    if (diff === 0) {
                        // AL CENTRO: Plana y enfrente
                        gsap.to(card, {
                            x: 0,
                            z: 0,
                            rotationY: 0,
                            duration: 0.6,
                            ease: "power2.out",
                            overwrite: "auto"
                        });
                        card.style.zIndex = 10;
                        card.style.filter = "brightness(100%)";
                        card.style.opacity = "1";
                        card.classList.add('is-active');

                        if (index !== lastActiveIndex) {
                            lastActiveIndex = index;
                            updateActiveInfoText(index);
                        }
                    }
                    else if (diff > 0) {
                        // A LA DERECHA: Quiebre hacia adentro
                        gsap.to(card, {
                            x: diff * xOffset,
                            z: zDepth,
                            rotationY: -yRotation,
                            duration: 0.6,
                            ease: "power2.out",
                            overwrite: "auto"
                        });
                        card.style.zIndex = 10 - diff;
                        card.style.filter = "brightness(45%)"; // Más oscuras las del fondo
                        card.style.opacity = diff > 2 ? "0" : "1";
                        card.classList.remove('is-active');
                    }
                    else {
                        // A LA IZQUIERDA: Quiebre inverso
                        gsap.to(card, {
                            x: diff * xOffset,
                            z: zDepth,
                            rotationY: yRotation,
                            duration: 0.6,
                            ease: "power2.out",
                            overwrite: "auto"
                        });
                        card.style.zIndex = 10 + diff;
                        card.style.filter = "brightness(45%)";
                        card.style.opacity = diff < -2 ? "0" : "1";
                        card.classList.remove('is-active');
                    }
                });
            }

            // Actualiza la info de texto y dots
            function updateActiveInfoText(index) {
                // Actualizar clases de los puntos de navegación
                document.querySelectorAll('.dot-3d').forEach((dot, idx) => {
                    if (idx === index) {
                        dot.classList.add('is-active');
                    } else {
                        dot.classList.remove('is-active');
                    }
                });

                // Animación de los textos inferiores
                gsap.to(".active-info-container", {
                    y: 10,
                    opacity: 0,
                    duration: 0.25,
                    onComplete: () => {
                        document.getElementById("activeTitle").textContent = destinations[index].title;
                        document.getElementById("activeSubtitle").textContent = destinations[index].subtitle;
                        const activeBtn = document.getElementById("activeCardBtn");
                        if (activeBtn) {
                            activeBtn.setAttribute("data-dest", destinations[index].dest);
                        }

                        gsap.to(".active-info-container", {
                            y: 0,
                            opacity: 1,
                            duration: 0.35,
                            ease: "power2.out"
                        });
                    }
                });

                gsap.to(".bg-text-back", {
                    opacity: 0,
                    scale: 0.95,
                    duration: 0.25,
                    onComplete: () => {
                        document.querySelector(".bg-text-back").textContent = destinations[index].bgTitle;

                        gsap.to(".bg-text-back", {
                            opacity: 0.04,
                            scale: 1,
                            duration: 0.45,
                            ease: "power2.out"
                        });
                    }
                });
            }

            // Botones de Navegación anterior / siguiente (Cíclico)
            document.getElementById('prevBtn3D')?.addEventListener('click', () => {
                currentIndex = (currentIndex - 1 + numCards3D) % numCards3D;
                updateLayout();
                stopAutoplay3D();
                startAutoplay3D();
            });
            document.getElementById('nextBtn3D')?.addEventListener('click', () => {
                currentIndex = (currentIndex + 1) % numCards3D;
                updateLayout();
                stopAutoplay3D();
                startAutoplay3D();
            });

            // Registrar eventos para click en tarjetas
            cards3D.forEach((card, index) => {
                card.addEventListener('click', (e) => {
                    if (e.target.closest('.card-btn-action') || e.target.closest('a')) return;

                    if (index !== currentIndex) {
                        currentIndex = index;
                        updateLayout();
                        stopAutoplay3D();
                        startAutoplay3D();
                    }
                });
            });

            // Registrar evento para botones de RESERVAR
            document.querySelectorAll('.card-btn-action').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    const destination = btn.getAttribute('data-dest');
                    const isMobile = window.innerWidth < 768;
                    const destInputDesktop = document.getElementById('booking-destino');
                    const destInputMobile = document.getElementById('booking-destino-m');
                    const triggerDesktop = document.getElementById('trigger-destino');
                    const triggerMobile = document.getElementById('trigger-destino-m');

                    if (destInputDesktop) destInputDesktop.value = destination;
                    if (destInputMobile) destInputMobile.value = destination;
                    if (triggerDesktop && triggerDesktop.querySelector('span')) triggerDesktop.querySelector('span').textContent = destination.replace(/BR|AR|PY/g, '').trim();
                    if (triggerMobile && triggerMobile.querySelector('span')) triggerMobile.querySelector('span').textContent = destination.replace(/BR|AR|PY/g, '').trim();

                    const bookingSection = document.querySelector('.booking-bar-wrapper') || document.querySelector('.booking-bar');
                    if (bookingSection) bookingSection.scrollIntoView({ behavior: 'smooth', block: 'center' });

                    const bookingBar = document.querySelector('.booking-bar');
                    if (bookingBar) {
                        bookingBar.style.transition = 'all 0.5s ease';
                        bookingBar.style.transform = 'scale(1.03)';
                        bookingBar.style.boxShadow = '0 0 30px rgba(0, 210, 255, 0.5)';
                        setTimeout(() => {
                            bookingBar.style.transform = '';
                            bookingBar.style.boxShadow = '';
                        }, 1500);
                    }

                    if (isMobile) {
                        const mobPanel = document.getElementById('booking-mobile-panel');
                        const mobOverlay = document.getElementById('booking-overlay');
                        if (mobPanel && mobOverlay) {
                            mobPanel.classList.add('open');
                            mobOverlay.classList.add('open');
                        }
                    }
                });
            });

            // Registrar eventos de arrastre virtual proxy
            let startDragX = 0;
            Draggable.create(dragProxy3D, {
                trigger: ".carousel-viewport-3d",
                type: "x",
                allowContextMenu: true,
                onDragStart: function () {
                    stopAutoplay3D();
                    startDragX = this.x;
                },
                onDragEnd: function () {
                    const change = this.x - startDragX;
                    const limit = 40; // Sensibilidad justa para cambiar de tarjeta

                    if (change > limit) {
                        currentIndex = (currentIndex - 1 + numCards3D) % numCards3D;
                    } else if (change < -limit) {
                        currentIndex = (currentIndex + 1) % numCards3D;
                    }
                    updateLayout();
                    gsap.set(dragProxy3D, { x: 0 });
                    startAutoplay3D();
                }
            });

            // Soporte para la rueda del ratón
            const sliderViewport3D = document.querySelector('.carousel-viewport-3d');
            sliderViewport3D?.addEventListener('wheel', (e) => {
                if (Math.abs(e.deltaY) > 5) {
                    e.preventDefault();
                    stopAutoplay3D();
                    if (e.deltaY > 0) {
                        currentIndex = (currentIndex + 1) % numCards3D;
                        updateLayout();
                    } else {
                        currentIndex = (currentIndex - 1 + numCards3D) % numCards3D;
                        updateLayout();
                    }
                    startAutoplay3D();
                }
            }, { passive: false });

            // Autoplay cíclico
            function startAutoplay3D() {
                stopAutoplay3D();
                autoplayTimeout3D = setTimeout(() => {
                    currentIndex = (currentIndex + 1) % numCards3D;
                    updateLayout();
                    startAutoplay3D();
                }, 5000);
            }

            function stopAutoplay3D() {
                clearTimeout(autoplayTimeout3D);
            }

            // Inicialización
            updateLayoutParameters();
            window.addEventListener('resize', updateLayoutParameters);
            startAutoplay3D();
        });

        // Lógica de la Galería Ken Burns
        (function () {
            const slides = document.querySelectorAll('.galeria-slide');
            const dotsContainer = document.querySelector('.galeria-dots');
            const prevBtn = document.querySelector('.galeria-nav-btn.prev');
            const nextBtn = document.querySelector('.galeria-nav-btn.next');
            let currentIdx = 0;
            let slideInterval;

            // Generar los puntos de navegación (dots) dinámicamente según la cantidad real de slides
            if (dotsContainer && slides.length) {
                dotsContainer.innerHTML = '';
                slides.forEach((_, idx) => {
                    const dot = document.createElement('span');
                    dot.className = `galeria-dot ${idx === 0 ? 'active' : ''}`;
                    dot.setAttribute('data-index', idx);
                    dot.addEventListener('click', () => {
                        showSlide(idx);
                        startAutoplay();
                    });
                    dotsContainer.appendChild(dot);
                });
            }

            function showSlide(index) {
                if (!slides.length) return;
                const activeDots = document.querySelectorAll('.galeria-dot');

                slides[currentIdx].classList.remove('active');
                if (activeDots[currentIdx]) activeDots[currentIdx].classList.remove('active');

                currentIdx = (index + slides.length) % slides.length;

                slides[currentIdx].classList.add('active');
                if (activeDots[currentIdx]) activeDots[currentIdx].classList.add('active');
            }

            function nextSlide() {
                showSlide(currentIdx + 1);
            }

            function prevSlide() {
                showSlide(currentIdx - 1);
            }

            function startAutoplay() {
                stopAutoplay();
                slideInterval = setInterval(nextSlide, 6000);
            }

            function stopAutoplay() {
                clearInterval(slideInterval);
            }

            if (prevBtn && nextBtn) {
                prevBtn.addEventListener('click', () => {
                    prevSlide();
                    startAutoplay();
                });
                nextBtn.addEventListener('click', () => {
                    nextSlide();
                    startAutoplay();
                });
            }

            startAutoplay();

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
                        startAutoplay();
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

        // Lógica de transición para la tarjeta de vehículos
        (function () {
            const carSlides = document.querySelectorAll('.car-slide');
            const carDots = document.querySelectorAll('.car-dot');
            let carIdx = 0;
            if (carSlides.length > 1) {
                setInterval(() => {
                    if (!carSlides[carIdx]) return;
                    carSlides[carIdx].style.opacity = '0';
                    carSlides[carIdx].classList.remove('active');
                    if (carDots[carIdx]) {
                        carDots[carIdx].style.background = 'rgba(255,255,255,0.4)';
                        carDots[carIdx].style.boxShadow = 'none';
                    }

                    carIdx = (carIdx + 1) % carSlides.length;

                    if (!carSlides[carIdx]) return;
                    carSlides[carIdx].style.opacity = '1';
                    carSlides[carIdx].classList.add('active');
                    if (carDots[carIdx]) {
                        carDots[carIdx].style.background = '#00d2ff';
                        carDots[carIdx].style.boxShadow = '0 0 6px #00d2ff';
                    }
                }, 4000);
            }
        })();

        // Lógica de la Galería Lightbox Modal para el Carrusel 3D
        (function () {
            const lightbox = document.getElementById('lightboxModal');
            const lightboxImg = document.getElementById('lightboxImg');
            const lightboxCaption = document.getElementById('lightboxCaption');
            const prevBtn = document.getElementById('prevLightbox');
            const nextBtn = document.getElementById('nextLightbox');

            const carouselCards = document.querySelectorAll('.card-item-3d');
            let imagesList = [];

            carouselCards.forEach((card, idx) => {
                const cardBack = card.querySelector('.card-back');
                if (cardBack) {
                    const bgStyle = cardBack.style.backgroundImage;
                    const match = bgStyle.match(/url\(['"]?([^'"]+)['"]?\)/);
                    if (match) {
                        const title = destinations[idx] ? destinations[idx].title : "Trifoz Turismo";
                        imagesList.push({ src: match[1], title: title });
                    }
                }
            });

            let currentImgIdx = 0;

            function openLightbox(index) {
                currentImgIdx = index;
                const imgData = imagesList[currentImgIdx];
                if (!imgData) return;

                lightboxImg.src = imgData.src;
                lightboxCaption.textContent = imgData.title;

                lightbox.style.display = 'flex';
                setTimeout(() => {
                    lightbox.style.opacity = '1';
                }, 50);
            }

            function closeLightbox() {
                lightbox.style.opacity = '0';
                setTimeout(() => {
                    lightbox.style.display = 'none';
                }, 400);
            }

            function nextImage(e) {
                if (e) e.stopPropagation();
                currentImgIdx = (currentImgIdx + 1) % imagesList.length;
                openLightbox(currentImgIdx);
            }

            function prevImage(e) {
                if (e) e.stopPropagation();
                currentImgIdx = (currentImgIdx - 1 + imagesList.length) % imagesList.length;
                openLightbox(currentImgIdx);
            }

            // Eventos de clic en tarjetas 3D
            carouselCards.forEach((card, idx) => {
                card.addEventListener('click', (e) => {
                    if (card.classList.contains('is-active')) {
                        openLightbox(idx);
                    } else {
                        currentIndex = idx;
                        updateLayout();
                        stopAutoplay3D();
                        startAutoplay3D();
                    }
                });
            });

            // Cierre haciendo click en el fondo o en la imagen misma
            lightbox.addEventListener('click', closeLightbox);
            lightboxImg.addEventListener('click', closeLightbox);

            // Flechas prev/next reales para navegación
            if (prevBtn) {
                prevBtn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    prevImage();
                });
            }
            if (nextBtn) {
                nextBtn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    nextImage();
                });
            }

            // Teclado
            document.addEventListener('keydown', (e) => {
                if (lightbox.style.display === 'flex') {
                    if (e.key === 'Escape') closeLightbox();
                    if (e.key === 'ArrowRight') nextImage();
                    if (e.key === 'ArrowLeft') prevImage();
                }
            });
            // Modales de la Barra Flotante
            (function () {
                const modalIngresos = document.getElementById('modalIngresos');
                const modalVideos = document.getElementById('modalVideos');
                const btnIngresos = document.getElementById('btn-ingresos');
                const btnVideos = document.getElementById('btn-videos');
                const closeIngresos = document.getElementById('closeIngresos');
                const closeVideos = document.getElementById('closeVideos');

                if (btnIngresos && modalIngresos) {
                    btnIngresos.addEventListener('click', () => {
                        modalIngresos.style.display = 'flex';
                        setTimeout(() => modalIngresos.style.opacity = '1', 50);
                    });
                }
                if (btnVideos && modalVideos) {
                    btnVideos.addEventListener('click', () => {
                        modalVideos.style.display = 'flex';
                        setTimeout(() => modalVideos.style.opacity = '1', 50);
                    });
                }

                function closeModal(modal) {
                    if (!modal) return;
                    modal.style.opacity = '0';
                    setTimeout(() => {
                        modal.style.display = 'none';
                        // Pausar todos los videos que se estén reproduciendo
                        modal.querySelectorAll('video').forEach(video => {
                            video.pause();
                        });
                    }, 400);
                }

                closeIngresos?.addEventListener('click', () => closeModal(modalIngresos));
                closeVideos?.addEventListener('click', () => closeModal(modalVideos));

                modalIngresos?.addEventListener('click', (e) => {
                    if (e.target === modalIngresos) closeModal(modalIngresos);
                });
                modalVideos?.addEventListener('click', (e) => {
                    if (e.target === modalVideos) closeModal(modalVideos);
                });

            const btnCloseVideosFooter = document.getElementById('btnCloseVideosFooter');
            if (btnCloseVideosFooter && i18n.btnCloseVideos) {
                btnCloseVideosFooter.textContent = i18n.btnCloseVideos;
            }
            btnCloseVideosFooter?.addEventListener('click', () => {
                document.getElementById('closeVideos')?.click();
            });

            })();

        }); // Fin DOMContentLoaded
