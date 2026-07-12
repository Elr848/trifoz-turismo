/**
 * MOBILE OPTIMIZATION JS - Trifoz Turismo
 * Optimizado para modo escritorio en móviles y rendimiento
 */

(function() {
    'use strict';

    // Detectar si es dispositivo táctil
    const isTouchDevice = window.matchMedia('(pointer: coarse)').matches;
    
    // Detectar si está en modo escritorio forzado en móvil
    const isForcedDesktop = isTouchDevice && window.innerWidth >= 769;
    
    // Detectar preferencia de movimiento reducido
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // ==========================================================================
    // OPTIMIZACIONES PARA MODO ESCRITORIO EN MÓVILES
    // ==========================================================================
    
    if (isForcedDesktop && !prefersReducedMotion) {
        // Desactivar animaciones pesadas para mejorar rendimiento
        document.documentElement.classList.add('force-desktop-mode');
        
        // Reducir la frecuencia de actualización del carrusel
        window.CAROUSEL_UPDATE_INTERVAL = 100; // ms
        
        // Optimizar eventos táctiles
        optimizeTouchEvents();
    }

    // ==========================================================================
    // OPTIMIZACIÓN DE EVENTOS TÁCTILES
    // ==========================================================================
    
    function optimizeTouchEvents() {
        // Eliminar delay táctil de 300ms
        const touchElements = document.querySelectorAll('.card, .card-item-3d, .nav-btn-3d-cf, .dot-3d, .card-btn-action');
        
        touchElements.forEach(el => {
            el.style.touchAction = 'manipulation';
            
            // Prevenir doble-tap zoom
            let lastTouchEnd = 0;
            el.addEventListener('touchend', (e) => {
                const now = Date.now();
                if (now - lastTouchEnd <= 300) {
                    e.preventDefault();
                }
                lastTouchEnd = now;
            }, { passive: false });
        });
    }

    // ==========================================================================
    // OPTIMIZACIÓN DE IMÁGENES
    // ==========================================================================
    
    function optimizeImages() {
        // Lazy loading nativo para imágenes
        const images = document.querySelectorAll('img:not([loading])');
        images.forEach(img => {
            img.loading = 'lazy';
            img.decoding = 'async';
        });
        
        // Optimizar imágenes del carrusel 3D
        const carouselImages = document.querySelectorAll('.card-item-3d .card-back');
        carouselImages.forEach(card => {
            const style = card.style.backgroundImage;
            if (style) {
                // Precargar imagen cuando la tarjeta está cerca del centro
                const url = style.match(/url\(["']?([^"')]+)["']?\)/);
                if (url && url[1]) {
                    const preloadLink = document.createElement('link');
                    preloadLink.rel = 'preload';
                    preloadLink.as = 'image';
                    preloadLink.href = url[1];
                    document.head.appendChild(preloadLink);
                }
            }
        });
    }

    // ==========================================================================
    // OPTIMIZACIÓN DEL CARRUSEL 3D
    // ==========================================================================
    
    let carouselOptimized = false;
    
    function optimizeCarousel3D() {
        if (carouselOptimized) return;
        carouselOptimized = true;
        
        const carousel = document.getElementById('carousel');
        if (!carousel) return;
        
        // Reducir la complejidad cuando hay muchas tarjetas
        const cards = carousel.querySelectorAll('.card-item-3d');
        
        // Intersection Observer para pausar animaciones de tarjetas fuera de vista
        const observerOptions = {
            root: carousel.parentElement,
            threshold: 0.1
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                const card = entry.target;
                if (entry.isIntersecting) {
                    card.style.visibility = 'visible';
                } else {
                    // Ocultar tarjetas muy lejanas para mejorar rendimiento
                    const rect = card.getBoundingClientRect();
                    const carouselRect = carousel.getBoundingClientRect();
                    if (rect.right < carouselRect.left - 200 || rect.left > carouselRect.right + 200) {
                        card.style.visibility = 'hidden';
                    }
                }
            });
        }, observerOptions);
        
        cards.forEach(card => observer.observe(card));
        
        // Optimizar eventos de drag/swipe
        let isDragging = false;
        let startX = 0;
        let currentX = 0;
        
        carousel.addEventListener('touchstart', (e) => {
            isDragging = true;
            startX = e.touches[0].clientX;
            carousel.style.transition = 'none';
        }, { passive: true });
        
        carousel.addEventListener('touchmove', (e) => {
            if (!isDragging) return;
            currentX = e.touches[0].clientX;
            const diff = currentX - startX;
            // Limitar el movimiento
            carousel.style.transform = `translateX(${diff * 0.5}px)`;
        }, { passive: true });
        
        carousel.addEventListener('touchend', () => {
            if (!isDragging) return;
            isDragging = false;
            carousel.style.transition = '';
            carousel.style.transform = '';
            
            const diff = currentX - startX;
            if (Math.abs(diff) > 50) {
                // Trigger navegación
                if (diff > 0) {
                    document.getElementById('prevBtn3D')?.click();
                } else {
                    document.getElementById('nextBtn3D')?.click();
                }
            }
        });
    }

    // ==========================================================================
    // BOTÓN WHATSAPP FLOTANTE
    // ==========================================================================
    
    function addWhatsAppButton() {
        // Verificar si ya existe
        if (document.querySelector('.whatsapp-float-btn')) return;
        
        const whatsappBtn = document.createElement('a');
        whatsappBtn.href = 'https://wa.me/5545933003337';
        whatsappBtn.className = 'whatsapp-float-btn';
        whatsappBtn.target = '_blank';
        whatsappBtn.rel = 'noopener noreferrer';
        whatsappBtn.setAttribute('aria-label', 'Contactar por WhatsApp');
        whatsappBtn.innerHTML = `
            <i class="fab fa-whatsapp"></i>
            <span class="whatsapp-tooltip">Chatea con nosotros</span>
        `;
        
        document.body.appendChild(whatsappBtn);
        
        // Agregar estilos inline para el botón
        const style = document.createElement('style');
        style.textContent = `
            .whatsapp-float-btn {
                position: fixed;
                bottom: 20px;
                right: 20px;
                width: 60px;
                height: 60px;
                background: linear-gradient(135deg, #25d366 0%, #128c7e 100%);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 4px 20px rgba(37, 211, 102, 0.4);
                z-index: 9999;
                transition: all 0.3s ease;
                text-decoration: none;
            }
            
            .whatsapp-float-btn:hover {
                transform: scale(1.1);
                box-shadow: 0 6px 30px rgba(37, 211, 102, 0.6);
            }
            
            .whatsapp-float-btn i {
                font-size: 28px;
                color: white;
            }
            
            .whatsapp-tooltip {
                position: absolute;
                right: 70px;
                background: #333;
                color: white;
                padding: 8px 12px;
                border-radius: 6px;
                font-size: 13px;
                white-space: nowrap;
                opacity: 0;
                visibility: hidden;
                transition: all 0.3s ease;
            }
            
            .whatsapp-float-btn:hover .whatsapp-tooltip {
                opacity: 1;
                visibility: visible;
            }
            
            @media (max-width: 768px) {
                .whatsapp-float-btn {
                    width: 55px;
                    height: 55px;
                    bottom: 80px;
                    right: 15px;
                }
                
                .whatsapp-float-btn i {
                    font-size: 24px;
                }
                
                .whatsapp-tooltip {
                    display: none;
                }
            }
        `;
        document.head.appendChild(style);
    }

    // ==========================================================================
    // INICIALIZACIÓN
    // ==========================================================================
    
    function init() {
        // Optimizar imágenes
        optimizeImages();
        
        // Agregar botón WhatsApp
        addWhatsAppButton();
        
        // Optimizar carrusel cuando esté disponible
        if (document.getElementById('carousel')) {
            optimizeCarousel3D();
        }
        
        // Observar cambios en el DOM para optimizar elementos dinámicos
        const observer = new MutationObserver((mutations) => {
            mutations.forEach((mutation) => {
                if (mutation.type === 'childList') {
                    mutation.addedNodes.forEach((node) => {
                        if (node.nodeType === 1) { // Elemento
                            if (node.id === 'carousel' || node.querySelector('#carousel')) {
                                setTimeout(optimizeCarousel3D, 100);
                            }
                        }
                    });
                }
            });
        });
        
        observer.observe(document.body, { childList: true, subtree: true });
    }

    // Ejecutar cuando el DOM esté listo
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // También ejecutar cuando la página esté completamente cargada
    window.addEventListener('load', () => {
        // Aplicar optimizaciones adicionales después de carga
        document.body.classList.add('page-fully-loaded');
    });

})();
