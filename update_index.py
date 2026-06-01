import sys

try:
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the end of </footer>
    footer_end = content.find('</footer>')
    if footer_end == -1:
        print("Error: </footer> not found")
        sys.exit(1)

    footer_end += len('</footer>')

    # Find the start of </body>
    body_end = content.find('</body>', footer_end)
    if body_end == -1:
        print("Error: </body> not found")
        sys.exit(1)

    # Extract the SVG from the existing content to keep it
    svg_start = content.find('<svg', footer_end, body_end)
    svg_end = content.find('</svg>', svg_start, body_end)
    
    if svg_start != -1 and svg_end != -1:
        svg_content = content[svg_start:svg_end + 6]
    else:
        # Fallback SVG if not found
        svg_content = """<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor" aria-hidden="true">
            <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946C.003 5.37 5.374 0 12.001 0c3.21.002 6.225 1.251 8.492 3.522 2.268 2.27 3.513 5.287 3.511 8.495-.003 6.632-5.371 12.003-12.001 12.003-2.002-.001-3.971-.5-5.713-1.448L0 24zm6.59-21.135c-.457-.015-.783-.023-1.018-.023-.925 0-1.442.474-1.684.776-.395.496-.92 1.488-.92 3.326 0 2.443 1.776 4.795 2.023 5.121.246.327 3.428 5.485 8.423 7.45 2.872 1.132 4.025 1.157 5.064.985 1.258-.208 2.656-.99 3.033-1.954.377-.963.377-1.791.264-1.954-.113-.163-.414-.261-.867-.487-.453-.226-2.656-1.312-3.07-1.463-.415-.151-.717-.226-.981.17-.264.395-.981 1.226-1.207 1.49-.226.264-.453.296-.906.07-4.004-2.007-5.263-6.027-5.461-6.37-.197-.343-.021-.528.15-.699.153-.153.34-.395.508-.593.17-.198.226-.339.34-.565.113-.226.056-.424-.028-.593-.085-.17-.717-1.725-.981-2.361-.258-.62-.519-.534-.717-.544z" />
        </svg>"""

    new_script = """
    <script>
        /* =========================================
           BOOKING SYSTEM - VERSIÓN CORREGIDA Y ROBUSTA
           ========================================= */

        let paxCount = 2;

        // Función para cambiar pasajeros (Desktop)
        function changePax(delta) {
            const paxDisplay = document.getElementById('pax-display');
            if (!paxDisplay) return;
            
            let current = parseInt(paxDisplay.textContent) || 2;
            current = Math.min(8, Math.max(1, current + delta));
            paxDisplay.textContent = current;
        }

        // Función para cambiar pasajeros (Mobile)
        function changePaxM(delta) {
            const paxDisplayM = document.getElementById('pax-display-m');
            if (!paxDisplayM) return;
            
            let current = parseInt(paxDisplayM.textContent) || 2;
            current = Math.min(8, Math.max(1, current + delta));
            paxDisplayM.textContent = current;
        }

        // Enviar reserva Desktop
        function enviarReservaWhatsApp() {
            const destino = document.getElementById('booking-destino')?.value;
            const pax = document.getElementById('pax-display')?.textContent || '2';
            const dtRaw = document.getElementById('booking-datetime')?.value;

            if (!destino) {
                alert('Por favor, seleccione un destino.');
                return;
            }
            if (!dtRaw) {
                alert('Por favor, seleccione fecha y hora.');
                return;
            }

            const dt = new Date(dtRaw);
            const pad = n => String(n).padStart(2, '0');
            
            const msg = `¡Hola! Me interesa un traslado para *${destino}* para *${pax} personas* el día *${pad(dt.getDate())}/${pad(dt.getMonth()+1)}* a las *${pad(dt.getHours())}:${pad(dt.getMinutes())}*. ¿Me podrías dar más información?`;

            const url = `https://wa.me/5545933003337?text=${encodeURIComponent(msg)}`;
            window.open(url, '_blank', 'noopener,noreferrer');
        }

        // Enviar reserva Mobile
        function enviarReservaMovil() {
            const destino = document.getElementById('booking-destino-m')?.value;
            const pax = document.getElementById('pax-display-m')?.textContent || '2';
            const dtRaw = document.getElementById('booking-datetime-m')?.value;

            if (!destino) {
                alert('Por favor, seleccione un destino.');
                return;
            }
            if (!dtRaw) {
                alert('Por favor, seleccione fecha y hora.');
                return;
            }

            const dt = new Date(dtRaw);
            const pad = n => String(n).padStart(2, '0');
            
            const msg = `¡Hola! Me interesa un traslado para *${destino}* para *${pax} personas* el día *${pad(dt.getDate())}/${pad(dt.getMonth()+1)}* a las *${pad(dt.getHours())}:${pad(dt.getMinutes())}*. ¿Me podrías dar más información?`;

            const url = `https://wa.me/5545933003337?text=${encodeURIComponent(msg)}`;
            window.open(url, '_blank', 'noopener,noreferrer');
        }

        // Abrir panel móvil
        function abrirFormularioMovil() {
            const panel = document.getElementById('booking-mobile-panel');
            const overlay = document.getElementById('booking-overlay');
            if (panel && overlay) {
                panel.classList.add('open');
                overlay.classList.add('open');
                document.body.style.overflow = 'hidden';
            }
        }

        // Cerrar panel móvil
        function cerrarFormularioMovil() {
            const panel = document.getElementById('booking-mobile-panel');
            const overlay = document.getElementById('booking-overlay');
            if (panel && overlay) {
                panel.classList.remove('open');
                overlay.classList.remove('open');
                document.body.style.overflow = '';
            }
        }

        // ====================== INICIALIZACIÓN ======================
        document.addEventListener('DOMContentLoaded', function () {

            // Setear fecha por defecto
            function setDefaultDatetime() {
                const tomorrow = new Date();
                tomorrow.setDate(tomorrow.getDate() + 1);
                const pad = n => String(n).padStart(2, '0');
                const val = `${tomorrow.getFullYear()}-${pad(tomorrow.getMonth() + 1)}-${pad(tomorrow.getDate())}T09:00`;

                const dtEl = document.getElementById('booking-datetime');
                const dtElM = document.getElementById('booking-datetime-m');
                
                if (dtEl && !dtEl.value) dtEl.value = val;
                if (dtElM && !dtElM.value) dtElM.value = val;
            }
            setDefaultDatetime();

            // Botones de pasajeros Desktop
            document.getElementById('pax-minus')?.addEventListener('click', (e) => {
                e.preventDefault();
                changePax(-1);
            });
            document.getElementById('pax-plus')?.addEventListener('click', (e) => {
                e.preventDefault();
                changePax(1);
            });

            // Botones de pasajeros Mobile
            document.querySelectorAll('.booking-mobile-pax-btn').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    const action = btn.getAttribute('data-pax-action');
                    changePaxM(action === 'minus' ? -1 : 1);
                });
            });

            // Submit Desktop
            document.getElementById('booking-submit-btn')?.addEventListener('click', enviarReservaWhatsApp);

            // Submit Mobile
            document.querySelector('.booking-mobile-cta')?.addEventListener('click', enviarReservaMovil);

            // Abrir panel móvil (botón flotante)
            const waFlotante = document.querySelector('.whatsapp-flotante');
            if (waFlotante) {
                waFlotante.addEventListener('click', function(e) {
                    e.preventDefault();
                    abrirFormularioMovil();
                });
            }

            // Cerrar panel móvil
            document.querySelector('.booking-mobile-close')?.addEventListener('click', cerrarFormularioMovil);
            document.getElementById('booking-overlay')?.addEventListener('click', cerrarFormularioMovil);

            // Click en campos del booking bar (desktop)
            document.getElementById('booking-destino-wrapper')?.addEventListener('click', () => {
                document.getElementById('booking-destino')?.focus();
            });
            document.getElementById('booking-datetime-wrapper')?.addEventListener('click', () => {
                document.getElementById('booking-datetime')?.showPicker?.() || document.getElementById('booking-datetime')?.focus();
            });
        });
    </script>
    <a href="#" class="whatsapp-flotante" data-wa-button>
        """ + svg_content + """
    </a>
"""

    new_content = content[:footer_end] + "\n" + new_script + "\n" + content[body_end:]

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("Success")

except Exception as e:
    print(f"Error: {e}")
