"""
Refactor Trifoz HTML: external CSS/JS, strict CSP, SEO cleanup.
Run: python refactor_csp.py
"""
from __future__ import annotations

import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))

CSP = (
    "default-src 'self'; "
    "script-src 'self' https://www.youtube.com https://cdnjs.cloudflare.com; "
    "style-src 'self' https://fonts.googleapis.com https://cdnjs.cloudflare.com; "
    "font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com; "
    "img-src 'self' data: https://flagcdn.com https://upload.wikimedia.org https://i.ytimg.com; "
    "connect-src 'self' https://wa.me; "
    "frame-src https://www.youtube.com https://www.youtube-nocookie.com; "
    "object-src 'none'; "
    "base-uri 'self'; "
    "form-action 'self'; "
    "frame-ancestors 'none'; "
    "upgrade-insecure-requests; "
    "block-all-mixed-content;"
)

SEO = {
    "es": {
        "file": "index.html",
        "canonical": "https://trifoz-turismo.com/",
        "og_locale": "es_AR",
        "og_locale_alt": ["pt_BR", "en_US"],
    },
    "pt": {
        "file": "index-pt.html",
        "canonical": "https://trifoz-turismo.com/index-pt.html",
        "og_locale": "pt_BR",
        "og_locale_alt": ["es_AR", "en_US"],
    },
    "en": {
        "file": "index-en.html",
        "canonical": "https://trifoz-turismo.com/index-en.html",
        "og_locale": "en_US",
        "og_locale_alt": ["es_AR", "pt_BR"],
    },
}

HREFLANG = [
    ('es', 'https://trifoz-turismo.com/'),
    ('pt-br', 'https://trifoz-turismo.com/index-pt.html'),
    ('en', 'https://trifoz-turismo.com/index-en.html'),
    ('x-default', 'https://trifoz-turismo.com/'),
]

MODAL_CSS = """
/* ── Modals & lightbox (CSP-safe, no inline styles) ── */
#lightboxModal,
#modalIngresos,
#modalVideos {
    display: none;
    position: fixed;
    inset: 0;
    z-index: 99999;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    opacity: 0;
    transition: opacity 0.4s ease;
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
}

#lightboxModal {
    background: rgba(5, 5, 15, 0.95);
}

#modalIngresos,
#modalVideos {
    background: rgba(5, 5, 15, 0.85);
}

.modal-close-btn {
    position: absolute;
    top: 15px;
    right: 20px;
    font-size: 1.8rem;
    cursor: pointer;
    color: #fff;
    z-index: 10;
    user-select: none;
}

#closeLightbox {
    top: 20px;
    right: 20px;
    font-size: 2.5rem;
    font-family: sans-serif;
    z-index: 100000;
}

.lightbox-nav {
    position: absolute;
    color: #fff;
    font-size: 2.5rem;
    cursor: pointer;
    user-select: none;
    z-index: 100000;
    padding: 15px;
}

#prevLightbox { left: 20px; }
#nextLightbox { right: 20px; }

.lightbox-inner {
    max-width: 90%;
    max-height: 85%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
}

#lightboxImg {
    max-width: 100%;
    max-height: 75vh;
    object-fit: contain;
    border-radius: 12px;
    border: 2px solid rgba(0, 210, 255, 0.4);
    box-shadow: 0 0 40px rgba(0, 210, 255, 0.3);
    transition: transform 0.3s ease;
    cursor: pointer;
}

#lightboxCaption {
    color: #00d2ff;
    font-family: 'Montserrat', sans-serif;
    font-size: 1rem;
    margin-top: 15px;
    font-weight: 700;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 1px;
    text-shadow: 0 2px 10px rgba(0, 210, 255, 0.4);
}

.modal-panel {
    background: rgba(12, 10, 26, 0.95);
    border: 2px solid rgba(0, 210, 255, 0.4);
    box-shadow: 0 0 30px rgba(0, 210, 255, 0.25);
    border-radius: 20px;
    width: 90%;
    padding: 30px;
    position: relative;
    cursor: default;
    color: #fff;
    font-family: 'Open Sans', sans-serif;
    box-sizing: border-box;
}

#modalIngresos .modal-panel { max-width: 500px; }
#modalVideos .modal-panel { max-width: 600px; max-height: 85vh; overflow-y: auto; }

.modal-title {
    color: #00d2ff;
    font-family: 'Montserrat', sans-serif;
    font-weight: 900;
    font-size: 1.4rem;
    margin: 0 0 20px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.modal-title--center { text-align: center; }

.modal-text {
    line-height: 1.6;
    font-size: 1rem;
    color: #ccd1e0;
    margin-bottom: 15px;
}

.modal-subtitle {
    color: #ffd700;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    margin-bottom: 10px;
    font-size: 1.05rem;
}

.modal-list {
    padding-left: 20px;
    line-height: 1.6;
    color: #ccd1e0;
    margin-bottom: 25px;
}

.modal-list li { margin-bottom: 8px; }

.btn-wa-modal {
    text-decoration: none;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    background: #25d366;
    color: #fff;
    font-family: 'Montserrat', sans-serif;
    font-weight: 900;
    font-size: 0.85rem;
    text-transform: uppercase;
    padding: 12px;
    border-radius: 30px;
    box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
    transition: all 0.3s;
}

.btn-wa-modal:hover {
    background: #20ba5a;
    transform: translateY(-2px);
}

.btn-wa-modal i { font-size: 1.2rem; }

.video-grid { display: flex; flex-direction: column; gap: 20px; }

.video-card-item {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 12px;
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.video-card-title {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 0.9rem;
    color: #ffd700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.video-card-item video {
    width: 100%;
    border-radius: 8px;
    border: 1.5px solid rgba(0, 210, 255, 0.3);
    background: #000;
    max-height: 240px;
    object-fit: contain;
}

.modal-footer-actions { text-align: center; margin-top: 25px; }

.btn-modal-dismiss {
    background: linear-gradient(135deg, #00d2ff 0%, #e0a0ff 100%);
    border: none;
    color: #fff;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 0.85rem;
    text-transform: uppercase;
    padding: 10px 24px;
    border-radius: 20px;
    cursor: pointer;
    box-shadow: 0 4px 10px rgba(0, 210, 255, 0.3);
}

/* Hover effects (replace inline onmouseover) */
.macuco-card-img { transition: transform 0.5s; }
.macuco-card-img:hover { transform: scale(1.03); }

.info-side-image:hover {
    border-color: rgba(224, 160, 255, 0.8) !important;
    transform: translateY(-5px);
}

.footer-copy-note { margin-top: 10px; }
"""


def extract_block(text: str, start_pat: str, end_tag: str) -> tuple[str, str]:
    start = text.find(start_pat)
    if start == -1:
        raise ValueError(f"Missing {start_pat}")
    content_start = start + len(start_pat)
    end = text.find(end_tag, content_start)
    if end == -1:
        raise ValueError(f"Missing {end_tag}")
    return text[:start] + text[end + len(end_tag) :], text[content_start:end].strip()


def extract_main_script(text: str) -> tuple[str, str]:
    marker = '<script>\n        document.addEventListener'
    alt = '<script>\n        document.addEventListener(\'DOMContentLoaded\''
    idx = text.find(marker)
    if idx == -1:
        idx = text.find('<script>\n        document.addEventListener(\'DOMContentLoaded\'')
    if idx == -1:
        raise ValueError("Main script block not found")
    end = text.find('    </script>\n\n    <!-- Lightbox Modal -->', idx)
    if end == -1:
        end = text.find('    </script>\n\n    <!-- Lightbox Modal -->'.replace('\n', '\r\n'), idx)
    if end == -1:
        # fallback: last big script before lightbox
        end = text.find('\n    </script>\n\n    <!-- Lightbox', idx)
    content = text[idx + len('<script>\n') : end].strip()
    new_text = text[:idx] + text[end + len('\n    </script>') :]
    return new_text, content


def strip_modals_to_clean_html(text: str) -> tuple[str, str]:
    start = text.find('    <!-- Lightbox Modal -->')
    end = text.find('</body>')
    if start == -1 or end == -1:
        raise ValueError("Modal section not found")
    modals = text[start:end].strip()
    body = text[:start].rstrip() + '\n\n' + text[end:]
    return body, modals


def clean_modals_html(modals: str) -> str:
    """Replace inline styles with CSS classes for CSP compliance."""
    modals = modals.replace(
        '<div id="lightboxModal"\n        style="display: none; position: fixed; inset: 0; background: rgba(5, 5, 15, 0.95); backdrop-filter: blur(15px); -webkit-backdrop-filter: blur(15px); z-index: 99999; justify-content: center; align-items: center; cursor: pointer; opacity: 0; transition: opacity 0.4s ease;">',
        '<div id="lightboxModal">',
    )
    modals = re.sub(
        r'<div style="position: absolute; top: 20px; right: 20px;[^"]*"[^>]*id="closeLightbox"[^>]*>',
        '<div class="modal-close-btn" id="closeLightbox">',
        modals,
    )
    modals = re.sub(
        r'<div style="position: absolute; left: 20px;[^"]*"[^>]*id="prevLightbox" onclick="event\.stopPropagation\(\);">',
        '<div class="lightbox-nav" id="prevLightbox">',
        modals,
    )
    modals = re.sub(
        r'<div style="position: absolute; right: 20px;[^"]*"[^>]*id="nextLightbox" onclick="event\.stopPropagation\(\);">',
        '<div class="lightbox-nav" id="nextLightbox">',
        modals,
    )
    modals = re.sub(
        r'<div\s+style="max-width: 90%; max-height: 85%;[^"]*">',
        '<div class="lightbox-inner">',
        modals,
        count=1,
    )
    modals = re.sub(
        r'<img loading="lazy" id="lightboxImg" src="" alt="Zoom"\s+style="[^"]*">',
        '<img loading="lazy" id="lightboxImg" src="" alt="Zoom">',
        modals,
    )
    modals = re.sub(
        r'<div id="lightboxCaption"\s+style="[^"]*">',
        '<div id="lightboxCaption">',
        modals,
    )

    modals = re.sub(
        r'<div id="modalIngresos"\s+style="[^"]*">',
        '<div id="modalIngresos">',
        modals,
    )
    modals = re.sub(
        r'<div id="modalVideos"\s+style="[^"]*">',
        '<div id="modalVideos">',
        modals,
    )

    # modal panels - first ingresos, second videos
    parts = modals.split('<div id="modalIngresos">', 1)
    if len(parts) == 2:
        head, rest = parts
        ing, rest2 = rest.split('<div id="modalVideos">', 1)
        ing = re.sub(
            r'<div\s+style="background: rgba\(12, 10, 26, 0\.95\);[^"]*">',
            '<div class="modal-panel">',
            ing,
            count=1,
        )
        ing = re.sub(
            r'<div style="position: absolute; top: 15px; right: 20px;[^"]*"[^>]*id="closeIngresos"[^>]*>',
            '<div class="modal-close-btn" id="closeIngresos">',
            ing,
        )
        vid = re.sub(
            r'<div\s+style="background: rgba\(12, 10, 26, 0\.95\);[^"]*">',
            '<div class="modal-panel">',
            rest2,
            count=1,
        )
        vid = re.sub(
            r'<div style="position: absolute; top: 15px; right: 20px;[^"]*"[^>]*id="closeVideos"[^>]*>',
            '<div class="modal-close-btn" id="closeVideos">',
            vid,
        )
        modals = head + '<div id="modalIngresos">' + ing + '<div id="modalVideos">' + vid

    # Generic replacements for repeated modal content patterns
    modals = re.sub(
        r'<h3 style="color: #00d2ff;[^"]*">',
        '<h3 class="modal-title">',
        modals,
    )
    modals = re.sub(
        r'<h3 class="modal-title"([^>]*)>\s*\n?\s*Videos',
        '<h3 class="modal-title modal-title--center"\\1>Videos',
        modals,
        count=1,
    )
    modals = re.sub(r'<p style="line-height: 1\.6;[^"]*">', '<p class="modal-text">', modals)
    modals = re.sub(
        r'<p style="color: #ffd700;[^"]*">',
        '<p class="modal-subtitle">',
        modals,
    )
    modals = re.sub(r'<ul style="padding-left: 20px;[^"]*">', '<ul class="modal-list">', modals)
    modals = re.sub(r'<li style="margin-bottom: 8px;">', '<li>', modals)

    modals = re.sub(
        r'<a href="https://wa\.me/[^"]+"\s+target="_blank"\s+rel="noopener noreferrer"\s+style="[^"]*"\s+onmouseover="[^"]*"\s+onmouseout="[^"]*">',
        lambda m: m.group(0).split(' style=')[0].replace(
            '<a href="', '<a class="btn-wa-modal" href="'
        ) + ' target="_blank" rel="noopener noreferrer">',
        modals,
        count=1,
    )
    # simpler wa link fix
    modals = re.sub(
        r'(<a href="https://wa\.me/5545933003337[^"]*")\s+target="_blank"\s+rel="noopener noreferrer"\s+style="[^"]*"\s+onmouseover="[^"]*"\s+onmouseout="[^"]*">',
        r'\1 class="btn-wa-modal" target="_blank" rel="noopener noreferrer">',
        modals,
    )

    modals = re.sub(
        r'<div style="display: flex; flex-direction: column; gap: 20px;">',
        '<div class="video-grid">',
        modals,
    )
    modals = re.sub(
        r'<div\s+style="background: rgba\(255, 255, 255, 0\.03\); border: 1px solid rgba\(255, 255, 255, 0\.1\); border-radius: 12px; padding: 12px; display: flex; flex-direction: column; gap: 8px;">',
        '<div class="video-card-item">',
        modals,
    )
    modals = re.sub(
        r'<span\s+style="font-family: \'Montserrat\', sans-serif; font-weight: 700; font-size: 0\.9rem; color: #ffd700; text-transform: uppercase; letter-spacing: 0\.5px;">',
        '<span class="video-card-title">',
        modals,
    )
    modals = re.sub(
        r'(<video src="[^"]+" controls preload="metadata")\s+style="[^"]*">',
        r'\1>',
        modals,
    )
    modals = re.sub(
        r'<div style="text-align: center; margin-top: 25px;">\s*<button onclick="document\.getElementById\(\'closeVideos\'\)\.click\(\)"\s+style="[^"]*">',
        '<div class="modal-footer-actions"><button type="button" class="btn-modal-dismiss" id="btnCloseVideosFooter">',
        modals,
    )
    return modals


def build_i18n_from_script(script: str, lang: str) -> dict:
    alert_m = re.search(r'alert\("([^"]+)"\)', script)
    dest_m = re.search(r'const destinations = (\[[\s\S]*?\]);', script)
    custom_vals = re.findall(r"destino === '([^']+)'", script)

    i18n: dict = {
        "alertSelectDestination": alert_m.group(1) if alert_m else "",
        "customItineraryValues": custom_vals or ["Itinerario Personalizado"],
    }

    if lang == "es":
        i18n["msgCustomItinerary"] = (
            "¡Hola! Me gustaría recibir ayuda para armar un itinerario personalizado.\\n\\n"
            "*Detalles iniciales:*\\n👥 Pasajeros: {pax}\\n📅 Fecha de llegada: {fecha}"
        )
        i18n["msgQuote"] = (
            "¡Hola! Me gustaría solicitar un presupuesto para el siguiente tour/traslado:\\n\\n"
            "📍 Destino: {destino}\\n👥 Pasajeros: {pax}\\n📅 Fecha y Hora: {fecha}"
        )
        i18n["btnCloseVideos"] = "Cerrar"
    elif lang == "pt":
        i18n["msgCustomItinerary"] = (
            "Olá! Gostaria de receber ajuda para montar um itinerário personalizado.\\n\\n"
            "*Detalhes iniciais:*\\n👥 Passageiros: {pax}\\n📅 Data de chegada: {fecha}"
        )
        i18n["msgQuote"] = (
            "Olá! Gostaria de solicitar um orçamento para o seguinte tour/traslado:\\n\\n"
            "📍 Destino: {destino}\\n👥 Passageiros: {pax}\\n📅 Data e Hora: {fecha}"
        )
        i18n["btnCloseVideos"] = "Fechar"
    else:
        i18n["msgCustomItinerary"] = (
            "Hello! I would like to get help to assemble a custom itinerary.\\n\\n"
            "*Initial details:*\\n👥 Passengers: {pax}\\n📅 Arrival Date: {fecha}"
        )
        i18n["msgQuote"] = (
            "Hello! I would like to request a quote for the following tour/transfer:\\n\\n"
            "📍 Destination: {destino}\\n👥 Passengers: {pax}\\n📅 Date and Time: {fecha}"
        )
        i18n["btnCloseVideos"] = "Close"

    if dest_m:
        raw = dest_m.group(1)
        raw = re.sub(r'(\w+)\s*:', r'"\1":', raw)
        try:
            i18n["destinations"] = json.loads(raw)
        except json.JSONDecodeError:
            pass

    return i18n


def patch_script_for_i18n(script: str) -> str:
    """Replace hardcoded strings with i18n loader."""
    loader = '''
    const i18nEl = document.getElementById('trifoz-i18n');
    const i18n = i18nEl ? JSON.parse(i18nEl.textContent) : {};
    const destinations = i18n.destinations || [];
'''
    script = re.sub(
        r'const destinations = \[[\s\S]*?\];',
        loader.strip(),
        script,
        count=1,
    )
    script = script.replace(
        'alert("Por favor selecciona un destino de la lista.");',
        'alert(i18n.alertSelectDestination || "Select a destination.");',
    )
    script = script.replace(
        'alert("Por favor, selecione um destino da lista.");',
        'alert(i18n.alertSelectDestination || "Select a destination.");',
    )
    script = script.replace(
        'alert("Please select a destination from the list.");',
        'alert(i18n.alertSelectDestination || "Select a destination.");',
    )

    script = re.sub(
        r"if \(destino === 'Itinerario Personalizado'[^\)]*\) \{[\s\S]*?mensaje = `[^`]+`;[\s\S]*?\} else \{[\s\S]*?mensaje = `[^`]+`;[\s\S]*?\}",
        '''const customValues = i18n.customItineraryValues || ['Itinerario Personalizado'];
                if (customValues.includes(destino)) {
                    mensaje = (i18n.msgCustomItinerary || '')
                        .replace('{pax}', pax)
                        .replace('{fecha}', fechaFormateada);
                } else {
                    mensaje = (i18n.msgQuote || '')
                        .replace('{destino}', destino)
                        .replace('{pax}', pax)
                        .replace('{fecha}', fechaFormateada);
                }''',
        script,
        count=1,
    )

    footer_btn = '''
            const btnCloseVideosFooter = document.getElementById('btnCloseVideosFooter');
            if (btnCloseVideosFooter && i18n.btnCloseVideos) {
                btnCloseVideosFooter.textContent = i18n.btnCloseVideos;
            }
            btnCloseVideosFooter?.addEventListener('click', () => {
                document.getElementById('closeVideos')?.click();
            });
'''
    script = script.replace(
        '})(); // Fin modals ingresos/videos',
        footer_btn + '\n            })(); // Fin modals ingresos/videos',
    )
    if 'btnCloseVideosFooter' not in script:
        script = script.replace(
            '            })();\n\n        }); // Fin DOMContentLoaded',
            footer_btn + '\n            })();\n\n        }); // Fin DOMContentLoaded',
        )

    return script


def remove_keywords(text: str) -> str:
    return re.sub(r'\s*<meta name="keywords"[^>]*>\s*', '\n', text, flags=re.I)


def update_csp(text: str) -> str:
    return re.sub(
        r'<meta http-equiv="Content-Security-Policy"\s+content="[^"]*">',
        f'<meta http-equiv="Content-Security-Policy"\n        content="{CSP}">',
        text,
        count=1,
    )


def build_hreflang_block() -> str:
    lines = []
    for lang, url in HREFLANG:
        lines.append(f'    <link rel="alternate" hreflang="{lang}" href="{url}" />')
    return '\n'.join(lines)


def update_seo_tags(text: str, lang: str, canonical: str) -> str:
    text = re.sub(
        r'<link rel="canonical" href="[^"]*" />',
        f'<link rel="canonical" href="{canonical}" />',
        text,
        count=1,
    )
    text = re.sub(
        r'(<link rel="alternate" hreflang=")[^"]+(" href=")[^"]+(" />)',
        lambda m: m.group(0),
        text,
    )
    # Replace entire hreflang block
    text = re.sub(
        r'    <link rel="alternate" hreflang="[^"]+" href="[^"]+" />\n(?:    <link rel="alternate" hreflang="[^"]+" href="[^"]+" />\n){2,3}',
        build_hreflang_block(),
        text,
        count=1,
    )
    text = re.sub(
        r'<meta property="og:url" content="[^"]*">',
        f'<meta property="og:url" content="{canonical}">',
        text,
        count=1,
    )
    text = re.sub(
        r'<meta name="twitter:url" content="[^"]*">',
        f'<meta name="twitter:url" content="{canonical}">',
        text,
        count=1,
    )
    cfg = SEO[lang]
    text = re.sub(
        r'<meta property="og:locale" content="[^"]*">',
        f'<meta property="og:locale" content="{cfg["og_locale"]}">',
        text,
        count=1,
    )
    # Remove old og:locale:alternate lines and add fresh
    text = re.sub(r'\s*<meta property="og:locale:alternate" content="[^"]*">\n?', '', text)
    og_alt = '\n'.join(
        f'    <meta property="og:locale:alternate" content="{loc}">'
        for loc in cfg['og_locale_alt']
    )
    text = text.replace(
        f'<meta property="og:locale" content="{cfg["og_locale"]}">',
        f'<meta property="og:locale" content="{cfg["og_locale"]}">\n{og_alt}',
        1,
    )
    return text


def replace_fontawesome_load(text: str) -> str:
    """Remove inline onload handler; load FA from trifoz.js instead."""
    pattern = re.compile(
        r'    <link rel="preload" href="https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome/6\.4\.0/css/all\.min\.css" as="style"[^\n]*\n'
        r'(?:    [^\n]*\n)*?'
        r'    <noscript>.*?</noscript>\n',
        re.S,
    )
    return pattern.sub('', text, count=1)


def inject_assets_head(text: str) -> str:
    link = '    <link rel="stylesheet" href="trifoz.css">\n'
    if 'href="trifoz.css"' not in text:
        text = text.replace('<link rel="preconnect" href="https://wa.me">', link + '    <link rel="preconnect" href="https://wa.me">', 1)
    return text


def inject_assets_body(text: str, i18n: dict) -> str:
    i18n_json = json.dumps(i18n, ensure_ascii=False, indent=2)
    block = f'''
    <script type="application/json" id="trifoz-i18n">{i18n_json}</script>
    <script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/Draggable.min.js"></script>
    <script defer src="trifoz.js"></script>
'''
    text = re.sub(
        r'\n    <!-- Librerías de animación GSAP[\s\S]*?<script defer src="https://cdnjs\.cloudflare\.com/ajax/libs/gsap/3\.12\.2/Draggable\.min\.js"></script>\n',
        '\n',
        text,
    )
    text = re.sub(r'\n    <script>\s*document\.addEventListener[\s\S]*?    </script>\n', '\n', text)
    if 'src="trifoz.js"' not in text:
        text = text.replace('</body>', block + '\n</body>')
    return text


def fix_macuco_hover(text: str) -> str:
    text = re.sub(
        r'(<img loading="lazy" src="images/macuco_safari_hd esta es\.webp" alt="[^"]*" width="800"\s+height="500")\s+style="[^"]*"\s+onmouseover="[^"]*"\s+onmouseout="[^"]*">',
        r'\1 class="macuco-card-img">',
        text,
    )
    text = re.sub(
        r'(<div class="info-side-image")\s+onmouseover="[^"]*"\s+onmouseout="[^"]*"\s+style="([^"]*)">',
        r'\1 style="\2">',
        text,
    )
    return text


def process_file(path: str, lang: str, css_written: bool, script_src: str) -> None:
    print(f"Processing {path}...")
    with open(path, encoding='utf-8') as f:
        text = f.read()

    text, css = extract_block(text, '    <style>\n', '    </style>')
    if not css_written:
        with open(os.path.join(BASE, 'trifoz.css'), 'w', encoding='utf-8', newline='\n') as f:
            f.write(css + '\n' + MODAL_CSS)
        print('  Wrote trifoz.css')

    text, script = extract_main_script(text)
    text, modals = strip_modals_to_clean_html(text)
    modals = clean_modals_html(modals)

    # Insert modals before footer scripts area (before </body>, after footer)
    text = text.replace('    </footer>\n', '    </footer>\n\n' + modals + '\n')

    text = remove_keywords(text)
    text = update_csp(text)
    text = update_seo_tags(text, lang, SEO[lang]['canonical'])
    text = replace_fontawesome_load(text)
    text = inject_assets_head(text)
    text = fix_macuco_hover(text)

    i18n = build_i18n_from_script(script_src, lang)
    text = inject_assets_body(text, i18n)

    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    print(f'  Updated {path}')


def main():
    scripts: dict[str, str] = {}
    for lang, cfg in SEO.items():
        path = os.path.join(BASE, cfg["file"])
        with open(path, encoding="utf-8") as f:
            raw = f.read()
        _, scripts[lang] = extract_main_script(raw)

    script = patch_script_for_i18n(scripts["es"])

    fa_loader = """
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
"""
    with open(os.path.join(BASE, "trifoz.js"), "w", encoding="utf-8", newline="\n") as f:
        f.write(fa_loader + "\n" + script + "\n")
    print("Wrote trifoz.js")

    css_done = False
    for lang, cfg in SEO.items():
        path = os.path.join(BASE, cfg["file"])
        process_file(path, lang, css_done, scripts[lang])
        css_done = True

    print("Done.")


if __name__ == '__main__':
    main()
