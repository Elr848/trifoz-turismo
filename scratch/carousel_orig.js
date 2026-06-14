           CARRUSEL 3D COVERFLOW TRIFOZ (MODERN NEON STYLE)
           ========================================================================== */
        .slider-container-3d {
            position: relative;
            width: 95%;
            max-width: 1200px;
            margin: 15px auto 40px auto;
            border-radius: 24px; /* Redondea las puntas */
            min-height: 600px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            background: radial-gradient(circle at center, rgba(255, 255, 255, 0.25) 0%, rgba(240, 248, 255, 0.4) 60%, rgba(220, 235, 245, 0.5) 100%); /* Fondo metalizado claro y brillante */
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1.5px solid rgba(255, 255, 255, 0.45); /* Borde claro brillante */
            box-shadow: inset 0 0 20px rgba(255, 255, 255, 0.4), 0 15px 35px rgba(0, 35, 102, 0.08); /* Sombras sumamente suaves y claras */
            z-index: 5;
            padding: 20px 0 40px 0;
        }

        /* Texto gigante en el fondo */
        .bg-text-back {
            position: absolute;
            top: 12%;
            font-family: 'Oswald', sans-serif;
            font-size: clamp(4rem, 12vw, 9rem);
            font-weight: 900;
            text-transform: uppercase;
            color: rgba(0, 210, 255, 0.04); /* Cian ne├│n ultra-tenue */
            white-space: nowrap;
            pointer-events: none;
            z-index: 0;
            letter-spacing: 10px;
            user-select: none;
            will-change: transform, opacity;
        }

        .carousel-viewport-3d {
            position: relative;
            width: 100%;
            height: 450px;
            display: flex;
            justify-content: center;
            align-items: flex-start; /* Alinear arriba para dejar espacio al espejo abajo */
            padding-top: 20px;
            perspective: 800px; /* Perspectiva ajustada para el quiebre exacto */
            transform-style: preserve-3d;
            z-index: 2;
        }

        .carousel-3d-wrapper {
            position: relative;
            width: var(--card-width, 210px);
            height: var(--card-height, 320px);
            transform-style: preserve-3d;
        }

        /* Contenedor principal de la tarjeta en 3D */
        .card-item-3d {
            position: absolute;
            width: 100%;
            height: 100%;
            left: 0;
            top: 0;
            cursor: pointer;
            will-change: transform, filter, opacity;
            transform-style: preserve-3d;
            background: transparent;
            -webkit-box-reflect: below 8px linear-gradient(transparent 30%, rgba(255, 255, 255, 0.25));
            perspective: 1000px;
        }

        /* Cara del carrusel 3D (Estilo oscuro metalizado profesional) */
        .card-back {
            width: 100%;
            height: 100%;
            border-radius: 20px;
            overflow: hidden;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: clamp(16px, 4vw, 24px) clamp(14px, 3.5vw, 20px);
            border: 2px solid rgba(255, 255, 255, 0.15) !important; /* Borde met├ílico sutil */
            box-shadow: inset 0 2px 5px rgba(255, 255, 255, 0.1), inset 0 -2px 5px rgba(0, 0, 0, 0.8), 0 10px 25px rgba(0, 0, 0, 0.75) !important; /* Bisel e iluminaci├│n met├ílica */
            color: #fff;
            text-align: left;
            transition: all 0.4s ease;
        }

        /* Resplandor especial para la tarjeta central activa */
        .card-item-3d.is-active {
            filter: drop-shadow(0 0 20px rgba(0, 210, 255, 0.20));
        }

        .card-item-3d.is-active .card-back {
            border-color: #00d2ff !important; /* Borde cian ne├│n met├ílico */
            box-shadow: inset 0 2px 8px rgba(255, 255, 255, 0.25), inset 0 -2px 8px rgba(0, 210, 255, 0.4), 0 0 30px rgba(0, 210, 255, 0.6), 0 15px 45px rgba(0, 0, 0, 0.7) !important;
        }

        /* Estilo del contenido trasero de la tarjeta */
        .card-back-content {
            display: flex;
            flex-direction: column;
            height: 100%;
            justify-content: space-between;
        }

        .card-back-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding-bottom: clamp(6px, 1.5vw, 10px);
        }

        .card-back-header h4 {
            font-family: 'Montserrat', sans-serif;
            font-size: clamp(0.9rem, 2.2vw, 1.15rem);
            font-weight: 700;
            color: #00d2ff; /* T├¡tulo en cian */
            margin: 0;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .card-tag-back {
            font-family: monospace;
            font-size: clamp(0.55rem, 1.3vw, 0.65rem);
            color: #ff007f; /* Rosa ne├│n */
            border: 1px solid rgba(255, 0, 127, 0.3);
            padding: 2px 6px;
            border-radius: 4px;
            background: rgba(255, 0, 127, 0.05);
            font-weight: 700;
        }

        .card-back-desc {
            font-size: clamp(0.7rem, 1.8vw, 0.85rem);
            line-height: 1.4;
            color: #ccd1e0; /* Texto lavanda muy claro */
            margin: clamp(8px, 2vw, 15px) 0;
            flex-grow: 1;
            overflow-y: auto;
            padding-right: 4px;
        }

        /* Scrollbar discreto si el texto se desborda en pantallas peque├▒as */
        .card-back-desc::-webkit-scrollbar {
            width: 3px;
        }
        .card-back-desc::-webkit-scrollbar-thumb {
            background: rgba(0, 210, 255, 0.2);
            border-radius: 1.5px;
        }

        .card-back-footer {
            display: flex;
            justify-content: center;
            align-items: center;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            padding-top: clamp(6px, 1.5vw, 10px);
        }

        .console-text {
            font-family: monospace;
            font-size: clamp(0.6rem, 1.5vw, 0.72rem);
            color: #00f0ff; /* C├│digo cian */
            opacity: 0.9;
        }

        .console-time {
            color: #ff007f; /* Hora rosa ne├│n */
            font-weight: bold;
            margin-left: 2px;
        }

        .card-btn-action {
            background: linear-gradient(135deg, #00d2ff 0%, #e0a0ff 100%);
            border: none;
            color: #fff;
            padding: clamp(5px, 1.5vw, 7px) clamp(10px, 2.5vw, 15px);
            border-radius: 20px;
            font-family: 'Montserrat', sans-serif;
            font-size: clamp(0.65rem, 1.5vw, 0.75rem);
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
            box-shadow: 0 4px 10px rgba(0, 210, 255, 0.25);
            letter-spacing: 0.5px;
        }

        .card-btn-action:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(0, 210, 255, 0.45);
        }

        .card-btn-action:active {
            transform: translateY(0);
        }

        /* Informaci├│n del destino activo abajo */
        .active-info-container {
            text-align: center;
            margin-top: 30px;
            z-index: 5;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
            min-height: 80px;
            will-change: transform, opacity;
        }

        .active-info-title-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 15px;
        }

        .title-line {
            width: 40px;
            height: 1px;
            background: #00d2ff;
            opacity: 0.6;
        }

        .active-title-3d {
            font-family: 'Montserrat', sans-serif;
            font-size: clamp(1.25rem, 4vw, 1.75rem);
            font-weight: 700;
            color: #fff;
            margin: 0;
            letter-spacing: 1px;
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }

        .active-subtitle-3d {
            font-size: clamp(0.85rem, 2vw, 1.05rem);
            color: #5c00d2; /* P├║rpura intenso de alta legibilidad */
            margin: 0;
            font-weight: 700;
            letter-spacing: 0.5px;
            text-shadow: 0 0 8px rgba(92, 0, 210, 0.15);
        }

        /* Controles laterales flotantes */
        .nav-btn-container-3d {
            position: absolute;
            width: 100%;
            max-width: 900px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            pointer-events: none;
            z-index: 10;
            padding: 0 20px;
        }

        .nav-btn-3d-cf {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: rgba(12, 10, 26, 0.85); /* Fondo oscuro cian */
            border: 1px solid rgba(0, 210, 255, 0.2);
            color: #00d2ff;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
            pointer-events: auto;
        }

        .nav-btn-3d-cf:hover {
            background: #00d2ff;
            color: #0c0a1a;
            border-color: #00d2ff;
            box-shadow: 0 0 20px rgba(0, 210, 255, 0.6);
            transform: scale(1.1);
        }

        .nav-btn-3d-cf:active {
            transform: scale(0.95);
        }

        .nav-btn-3d-cf svg {
            width: 20px;
            height: 20px;
            fill: currentColor;
        }

        /* Navegaci├│n por puntos */
        .navigation-dots-3d {
            display: flex;
            justify-content: center;
            gap: 12px;
            margin-top: 15px;
            z-index: 5;
        }

        .dot-3d {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: rgba(0, 210, 255, 0.25);
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .dot-3d.is-active {
            background: #00d2ff;
            transform: scale(1.3);
            box-shadow: 0 0 8px rgba(0, 210, 255, 0.6);
        }

        /* --- RESPONSIVE OVERRIDES --- */
        @media (max-width: 768px) {
            .slider-container-3d {
                min-height: 480px;
                margin: 20px auto;
                padding: 10px 0 20px 0;
            }
            .carousel-viewport-3d {
                height: 350px;
                padding-top: 15px;
            }
            .nav-btn-container-3d {
                display: flex; /* Mostrar flechas en m├│vil */
                width: 100%;
                max-width: 100%;
                top: 35%; /* Centrado con respecto a las tarjetas */
                transform: translateY(-50%);
                padding: 0 10px;
                box-sizing: border-box;
            }
            .nav-btn-3d-cf {
                width: 42px;
                height: 42px;
                background: rgba(12, 10, 26, 0.9); /* M├ís opaco para mejor visibilidad */
            }
            .nav-btn-3d-cf svg {
                width: 16px;
                height: 16px;
            }
            .active-info-container {
                margin-top: 20px;
                min-height: 70px;
            }
        }
        @media (max-width: 480px) {
            .slider-container-3d {
                min-height: 400px;
            }
            .carousel-viewport-3d {
                height: 290px;
                padding-top: 10px;
            }
        }
    
        /* BARRA DE BOTONES HORIZONTAL */
        .horizontal-button-bar {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 15px;
            width: 90%;
            max-width: 850px;
            margin: 30px auto 40px auto;
            flex-wrap: wrap;
        }
        .btn-horizontal-bar {
            flex: 1;
            min-width: 150px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            background: rgba(12, 10, 26, 0.75);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1.5px solid rgba(0, 210, 255, 0.4);
            color: #fff;
            padding: 12px 24px;
            border-radius: 30px;
            font-family: 'Montserrat', sans-serif;
            font-weight: 700;
            text-transform: uppercase;
            font-size: 0.85rem;
            letter-spacing: 1px;
            text-decoration: none;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
            cursor: pointer;
            outline: none;
            box-sizing: border-box;
        }
        .btn-horizontal-bar i {
            color: #00d2ff;
            font-size: 1.1rem;
        }
        .btn-horizontal-bar:hover {
            background: rgba(0, 210, 255, 0.35);
            border-color: rgba(224, 160, 255, 0.8);
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0, 210, 255, 0.4);
        }
        @media (max-width: 580px) {
            .horizontal-button-bar {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 8px;
                width: 95%;
            }
            .btn-horizontal-bar {
                width: 100%;
                min-width: 0;
                padding: 6px 10px;
                font-size: 0.68rem;
                border-radius: 20px;
                gap: 5px;
            }
            .btn-horizontal-bar i {
                font-size: 0.85rem;
            }
            .btn-horizontal-bar img {
                width: 16px !important;
                height: 16px !important;
            }
        }
        
        /* Ken Burns Gallery Styles */
        .galeria-franja {
            position: relative;
            width: 100%;
            height: 520px; /* Incrementado para mejor proporci├│n en notebooks/computadoras */
            overflow: hidden;
            background: #050510;
            border-top: 2px solid rgba(0, 210, 255, 0.3);
            border-bottom: 2px solid rgba(0, 210, 255, 0.3);
            box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.5), 0 10px 30px rgba(0, 0, 0, 0.5);
        }
        .galeria-slide {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            opacity: 0;
            visibility: hidden;
            transition: opacity 1.5s ease-in-out, visibility 1.5s;
            z-index: 1;
        }
        .galeria-slide.active {
            opacity: 1;
            visibility: visible;
            z-index: 2;
        }
        .galeria-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transform: scale(1);
        }
        .galeria-slide.active .galeria-img {
            animation: kenBurnsAnimation 7s forwards ease-out;
        }
        @keyframes kenBurnsAnimation {
            0% { transform: scale(1); }
            100% { transform: scale(1.12); }
        }
        .galeria-overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(to top, rgba(12, 10, 26, 0.5) 0%, transparent 40%, rgba(12, 10, 26, 0.2) 100%);
            z-index: 3;
            pointer-events: none;
        }
        .galeria-content {
            position: absolute;
            bottom: 30px;
            left: 30px;
            z-index: 4;
            display: flex;
            flex-direction: column;
            gap: 5px;
            pointer-events: none;
        }
        .galeria-title {
            color: #00d2ff;
            font-family: 'Montserrat', sans-serif;
            font-weight: 900;
            font-size: 1.1rem;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            text-shadow: 0 2px 10px rgba(0, 210, 255, 0.5);
        }
        .galeria-subtitle {
            color: #fff;
            font-family: 'Open Sans', sans-serif;
            font-size: 0.9rem;
            opacity: 0.9;
        }
        .galeria-nav-btn {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background: rgba(12, 10, 26, 0.6);
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #fff;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 5;
            transition: all 0.3s ease;
            font-size: 1.2rem;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
        .galeria-nav-btn:hover {
            background: rgba(0, 210, 255, 0.4);
            border-color: #00d2ff;
            box-shadow: 0 0 15px rgba(0, 210, 255, 0.5);
            color: #fff;
        }
        .galeria-nav-btn.prev { left: 25px; }
        .galeria-nav-btn.next { right: 25px; }
        
        .galeria-dots {
            position: absolute;
            bottom: 25px;
            right: 30px;
            z-index: 5;
            display: flex;
            gap: 8px;
        }
        .galeria-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.3);
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .galeria-dot.active {
            background: #00d2ff;
            transform: scale(1.3);
            box-shadow: 0 0 8px rgba(0, 210, 255, 0.8);
        }
        @media (max-width: 768px) {
            .galeria-franja { height: 300px; }
            .galeria-nav-btn { width: 40px; height: 40px; font-size: 1rem; }
            .galeria-nav-btn.prev { left: 15px; }
            .galeria-nav-btn.next { right: 15px; }
            .galeria-content { bottom: 20px; left: 20px; }
            .galeria-dots { bottom: 15px; right: 20px; }
        }
    
    
        /* New Info Box Styles */
        .info-box {
            width: 90%;
            max-width: 1050px;
            min-height: 400px;
            margin: 50px auto;
            padding: 50px;
            background: linear-gradient(135deg, rgba(76, 99, 137, 0.45) 0%, rgba(63, 85, 122, 0.5) 100%);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 2px solid rgba(0, 216, 255, 0.35);
            border-radius: 30px;
            display: flex;
            gap: 50px;
            align-items: center;
            color: white;
            text-align: left;
            box-shadow: 0 20px 45px rgba(0, 210, 255, 0.15);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        .info-box:hover {
            border-color: rgba(224, 160, 255, 0.8);
            transform: translateY(-5px);
            box-shadow: 0 25px 50px rgba(224, 160, 255, 0.25);
        }
        .columna {
            flex: 1;
        }
        .info-box h2 {
            color: #00d8ff;
            font-size: clamp(1.8rem, 4vw, 3rem);
            margin-bottom: 25px;
            text-transform: uppercase;
            font-family: 'Montserrat', sans-serif;
            font-weight: 900;
            line-height: 1.2;
            text-shadow: 0 0 10px rgba(0, 216, 255, 0.3);
        }
        .info-box p {
            font-size: clamp(1.05rem, 1.5vw, 1.3rem);
            line-height: 1.8;
            color: #ccd1e0;
        }
        @media (max-width: 768px) {
            .info-box {
                flex-direction: column;
                padding: 30px;
                gap: 30px;
            }
        }
        
        /* Estilos de zoom de los deslizadores de veh├¡culos */
        .car-slide img, .car-slide2 img {
            transform: scale(1.02) !important;
            transition: transform 6s ease-out !important;
        }
        .car-slide.active img, .car-slide2.active img {
            transform: scale(1.08) !important;
        }

        /* Bot├│n LIBRAS circular interactivo */
        .libras-round-button {
            display: inline-flex;
            justify-content: center;
            align-items: center;
            width: 80px;
            height: 60px;
            border-radius: 50%;
            background: #ffffff;
            border: 2px solid #00d2ff;
            box-shadow: 0 0 15px rgba(0, 210, 255, 0.4);
            overflow: hidden;
            transition: all 0.3s ease;
            animation: pulse-libras 2s infinite;
        }

        .libras-round-button:hover {
            transform: scale(1.1);
            box-shadow: 0 0 25px rgba(0, 210, 255, 0.8);
            border-color: #ffd700;
        }

        .libras-btn-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        @keyframes pulse-libras {
            0% {
                box-shadow: 0 0 0 0 rgba(0, 210, 255, 0.6);
            }
            70% {
                box-shadow: 0 0 0 10px rgba(0, 210, 255, 0);
            }
            100% {
                box-shadow: 0 0 0 0 rgba(0, 210, 255, 0);
            }
        }

    </style>
</head>

<body>



    <div class="header-idioma-container">
        <span class="label-idioma-fijo">Idioma:</span>
        <div class="lista-idioma-fija">
            <a href="index.html" class="opcion-idioma-fija activo" hreflang="es">
                <img src="https://flagcdn.com/w20/es.png" class="mini-flag" alt="Espa├▒ol" width="20" height="13" loading="lazy"> ES
            </a>
            <a href="index-pt.html" class="opcion-idioma-fija" hreflang="pt-BR">
                <img src="https://flagcdn.com/w20/br.png" class="mini-flag" alt="Portugu├⌐s" width="20" height="13" loading="lazy"> PT
            </a>
        </div>
    </div>

    <section class="hero">
        <img src="images/plataforma.jpeg" alt="Tours privados en Foz de Iguaz├║ con Gu├¡a Ebert" class="hero-background"
            width="1920" height="1080">
        <div class="fire-wrapper" aria-hidden="true">
            <div class="hero-container">
                <h1 class="titulo-metalico" style="margin:0; line-height:1.1; font-size: clamp(1.9rem, 5.5vw, 2.7rem);">
                    Trifoz Turismo
                </h1>
                <h2 class="subtitulo-amarillo" style="margin:10px 0 0 0; font-size: clamp(0.9rem, 2.2vw, 1.15rem);">
                    Tours &amp; Traslados Privados en la Triple Frontera
                </h2>
                <h3 style="margin:12px 0 20px; font-size: clamp(0.85rem, 2vw, 1.1rem); color:#fff; opacity:0.9;">
                    Especialistas en LIBRAS ΓÇó Espa├▒ol ΓÇó Portugu├⌐s<br>
                    Incluye paseos guiados con gu├¡as certificados
                </h3>
            </div>
        </div>

        <div class="booking-bar-wrapper">
            <div class="booking-bar">
                <div class="booking-field" id="booking-destino-wrapper">
                    <div class="booking-field-icon">≡ƒôì</div>
                    <div class="booking-field-body">
                        <span class="booking-field-label">Destino</span>
                        <div class="dropdown-container">
                            <div class="custom-select-trigger" id="trigger-destino">
                                <span>┬┐A d├│nde vas?</span> <i class="fas fa-chevron-down" style="font-size:0.8em;"></i>
                            </div>
                            <input type="hidden" id="booking-destino" value="">
                            <ul class="dropdown-menu" id="menu-destino">
                                <li class="dropdown-item help-option" data-value="Itinerario Personalizado">Γ£¿ Necesito
                                    ayuda con el itinerario</li>
                                <li class="dropdown-divider"></li>
                                <li class="dropdown-item" data-value="Cataratas de Iguaz├║ (Brasil)"><span
                                        class="country-tag">BR</span> Cataratas de Iguaz├║ (Brasil)</li>
                                <li class="dropdown-item" data-value="Cataratas del Iguaz├║ (Argentina)"><span
                                        class="country-tag">AR</span> Cataratas del Iguaz├║ (Arg)</li>
                                <li class="dropdown-item" data-value="Parque de las Aves">≡ƒª£ Parque de las Aves</li>
                                <li class="dropdown-item" data-value="Hito de las 3 Fronteras">≡ƒÅ¢∩╕Å Hito de las 3
                                    Fronteras</li>
                                <li class="dropdown-item" data-value="Itaip├║ Binacional">ΓÜí Itaip├║ Binacional</li>
                                <li class="dropdown-item" data-value="Macuco Safari">≡ƒÜñ Macuco Safari</li>
                                <li class="dropdown-item" data-value="Roda Gigante Yup Star">≡ƒÄí Rueda Gigante Yup Star
                                </li>
                                <li class="dropdown-item" data-value="Museo de Cera Dreamland">≡ƒÄ¡ Museo de Cera
                                    Dreamland</li>
                                <li class="dropdown-item" data-value="Ciudad del Este (Paraguay)"><span
                                        class="country-tag">PY</span> Ciudad del Este</li>
                                <li class="dropdown-divider"></li>
                                <li class="dropdown-header">TRASLADOS &amp; HOTELES</li>
                                <li class="dropdown-item" data-value="Aeropuerto de Foz de Iguaz├║">Γ£ê∩╕Å <span
                                        class="country-tag">BR</span> Aeropuerto de Foz de Iguaz├║</li>
                                <li class="dropdown-item" data-value="Aeropuerto de Puerto Iguaz├║">Γ£ê∩╕Å <span
                                        class="country-tag">AR</span> Aeropuerto de Puerto Iguaz├║</li>
                                <li class="dropdown-item" data-value="Aeropuerto de Ciudad del Este">Γ£ê∩╕Å <span
                                        class="country-tag">PY</span> Aeropuerto de Ciudad del Este</li>
                                <li class="dropdown-item" data-value="Traslado para Hoteles">≡ƒÅ¿ Traslado para Hoteles
                                    (BR / AR / PY)</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="booking-field">
                    <div class="booking-field-icon" style="color: var(--amarillo);"><i class="fas fa-user-group"></i>
                    </div>
                    <div class="booking-field-body">
                        <span class="booking-field-label">Pasajeros</span>
                        <div class="passenger-counter">
                            <button type="button" class="pax-btn" id="pax-minus">ΓêÆ</button>
                            <span class="pax-value" id="pax-display">2</span>
                            <button type="button" class="pax-btn" id="pax-plus">+</button>
                        </div>
                    </div>
                </div>

                <div class="booking-field" id="booking-datetime-wrapper">
                    <div class="booking-field-icon">≡ƒùô∩╕Å</div>
                    <div class="booking-field-body">
                        <span class="booking-field-label">Fecha &amp; Hora</span>
                        <input type="datetime-local" id="booking-datetime" class="booking-datetime"
                            aria-label="Fecha y hora de reserva">
                    </div>
                </div>

                <button class="booking-cta" id="booking-submit-btn">
                    <i class="fab fa-whatsapp" style="font-size:1.25rem;"></i>
                    <span class="booking-cta-label">
                        M├üS INFORMACI├ôN
                        <span class="booking-cta-phone">+55(45)933003337</span>
                    </span>
                </button>

                <div class="social-buttons-container">
                    <a href="mailto:trifozturismo@gmail.com" class="btn-social btn-email" aria-label="Enviar Email"><i
                            class="fa-solid fa-envelope"></i></a>
                    <a href="https://www.facebook.com/share/1Qr8RiKxrz/" target="_blank" rel="noopener noreferrer"
                        class="btn-social btn-facebook" aria-label="Facebook"><i
                            class="fa-brands fa-facebook-f"></i></a>
                    <a href="https://www.instagram.com/trifoz.turismo" target="_blank" rel="noopener noreferrer"
                        class="btn-social btn-instagram" aria-label="Instagram"><i
                            class="fa-brands fa-instagram"></i></a>
                </div>
            </div>
        </div>
    </section>

    <button class="booking-mobile-btn" id="booking-mobile-trigger">
        <i class="fab fa-whatsapp" style="font-size:1.4rem;"></i>
        <span class="booking-mobile-btn-label">
            M├üS INFORMACI├ôN
            <span class="booking-mobile-btn-phone">+55(45)933003337</span>
        </span>
    </button>

    <div class="booking-overlay" id="booking-overlay"></div>

    <div class="booking-mobile-panel" id="booking-mobile-panel">
        <div class="booking-mobile-panel-handle"></div>
        <div class="booking-mobile-panel-header">
            <span class="booking-mobile-panel-title">
                <i class="fas fa-map-marker-alt" style="color: #ff4500;"></i> Hacer una consulta
            </span>
            <button class="booking-mobile-close" id="booking-mobile-close">&#x2715;</button>
        </div>

        <div class="booking-mobile-field">
            <div class="booking-mobile-field-body">
                <span class="booking-mobile-label">Destino</span>
                <div class="dropdown-container">
                    <div class="custom-select-trigger" id="trigger-destino-m">
                        <span>┬┐A d├│nde vas?</span> <i class="fas fa-chevron-down" style="font-size:0.8em;"></i>
                    </div>
                    <input type="hidden" id="booking-destino-m" value="">
                    <ul class="dropdown-menu" id="menu-destino-m">
                        <li class="dropdown-item help-option" data-value="Itinerario Personalizado">Γ£¿ Necesito ayuda con
                            el itinerario</li>
                        <li class="dropdown-divider"></li>
                        <li class="dropdown-item" data-value="Cataratas de Iguaz├║ (Brasil)">Cataratas de Iguaz├║ (Brasil)
                        </li>
                        <li class="dropdown-item" data-value="Cataratas del Iguaz├║ (Argentina)">Cataratas del Iguaz├║
                            (Arg)</li>
                        <li class="dropdown-item" data-value="Parque de las Aves">Parque de las Aves</li>
                        <li class="dropdown-item" data-value="Hito de las Tres Fronteras">Hito de las 3 Fronteras</li>
                        <li class="dropdown-item" data-value="Itaip├║ Binacional">Itaip├║ Binacional</li>
                        <li class="dropdown-item" data-value="Macuco Safari">Macuco Safari</li>
                        <li class="dropdown-item" data-value="Ciudad del Este">Ciudad del Este (Paraguay)</li>
                        <li class="dropdown-divider"></li>
                        <li class="dropdown-header">TRASLADOS &amp; HOTELES</li>
                        <li class="dropdown-item" data-value="Aeropuerto de Foz de Iguaz├║">Γ£ê∩╕Å <span
                                class="country-tag">BR</span> Aeropuerto de Foz de Iguaz├║</li>
                        <li class="dropdown-item" data-value="Aeropuerto de Puerto Iguaz├║">Γ£ê∩╕Å <span
                                class="country-tag">AR</span> Aeropuerto de Puerto Iguaz├║</li>
                        <li class="dropdown-item" data-value="Aeropuerto de Ciudad del Este">Γ£ê∩╕Å <span
                                class="country-tag">PY</span> Aeropuerto de Ciudad del Este</li>
                        <li class="dropdown-item" data-value="Traslado para Hoteles">≡ƒÅ¿ Traslado para Hoteles (BR / AR /
                            PY)</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="booking-mobile-field">
            <div class="booking-mobile-field-body">
                <span class="booking-mobile-label">Pasajeros</span>
                <div class="booking-mobile-pax">
                    <button type="button" class="booking-mobile-pax-btn" id="pax-minus-m">ΓêÆ</button>
                    <span class="booking-mobile-pax-val" id="pax-display-m">2</span>
                    <button type="button" class="booking-mobile-pax-btn" id="pax-plus-m">+</button>
                </div>
            </div>
        </div>

        <div class="booking-mobile-field">
            <div class="booking-mobile-field-body">
                <span class="booking-mobile-label">Fecha &amp; Hora</span>
                <input type="datetime-local" id="booking-datetime-m" class="booking-mobile-datetime">
            </div>
        </div>

        <button class="booking-mobile-cta" id="booking-submit-btn-m">
            <i class="fab fa-whatsapp" style="font-size:1.4rem;"></i>
            <span style="display:flex; flex-direction:column; line-height:1.2; text-align:left;">
                <b>SOLICITAR CONSULTA</b>
                <span class="booking-mobile-cta-phone">+55(45)933003337</span>
            </span>
        </button>
    </div>



    <section class="attractions">
        <div style="display: flex; flex-direction: column; align-items: center; margin-bottom: 15px; gap: 6px;">
            <a href="https://www.youtube.com/shorts/Ulz_WJArmqA" target="_blank" rel="noopener noreferrer" class="libras-round-button" aria-label="Video LIBRAS">
                <img src="images/una.jpeg" alt="LIBRAS" class="libras-btn-img">
            </a>
            <span style="font-family: 'Montserrat', sans-serif; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; color: #ffd700; letter-spacing: 1.5px; text-shadow: 0 2px 4px rgba(0,0,0,0.6);">Invitaci├│n</span>
        </div>
        <div style="text-align: center; margin-bottom: 15px; padding: 0 20px;">
            <h2 class="subtitulo-amarillo" style="font-size: clamp(1.4rem, 6vw, 2.2rem); margin-bottom: 5px;">
                Atracciones Imperdibles en Foz de Iguaz├║
            </h2>
        </div>
        <div class="slider-container-3d">
            <!-- Texto gigante en el fondo -->
            <div class="bg-text-back">CATARATAS</div>
            
            <!-- Controles laterales flotantes -->
            <div class="nav-btn-container-3d">
                <button class="nav-btn-3d-cf" id="prevBtn3D" aria-label="Anterior">
                    <svg viewBox="0 0 24 24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg>
                </button>
                <button class="nav-btn-3d-cf" id="nextBtn3D" aria-label="Siguiente">
                    <svg viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
                </button>
            </div>

            <!-- Viewport 3D -->
            <div class="carousel-viewport-3d">
                <div class="carousel-3d-wrapper" id="carousel">
                    
                    <div class="card-item-3d" data-index="0">
                        <div class="card-back" style="background: url('images/cataratas mejorada.jpg') no-repeat center center / cover; padding: 0;">
                        </div>
                    </div>

                    <div class="card-item-3d" data-index="1">
                        <div class="card-back" style="background: url('images/macuco_safari_real.jpg') no-repeat center center / cover; padding: 0;">
                        </div>
                    </div>

                    <div class="card-item-3d" data-index="2">
                        <div class="card-back" style="background: url('images/buda.jpeg') no-repeat center center / cover; padding: 0;">
                        </div>
                    </div>

                    <div class="card-item-3d" data-index="3">
                        <div class="card-back" style="background: url('images/dutty.jpeg') no-repeat center center / cover; padding: 0;">
                        </div>
                    </div>

                    <div class="card-item-3d" data-index="4">
                        <div class="card-back" style="background: url('images/Kattamaram (2).jpeg') no-repeat center center / cover; padding: 0;">
                        </div>
                    </div>

                    <div class="card-item-3d" data-index="5">
                        <div class="card-back" style="background: url('images/dutty.jpeg') no-repeat center center / cover; padding: 0;">
                        </div>
                    </div>

                    <div class="card-item-3d" data-index="6">
                        <div class="card-back" style="background: url('images/china 1.png') no-repeat center center / cover; padding: 0;">
                        </div>
                    </div>

                    <div class="card-item-3d" data-index="7">
                        <div class="card-back" style="background: url('images/marco_real.jpg') no-repeat center center / cover; padding: 0;">
                        </div>
                    </div>

                    <div class="card-item-3d" data-index="8">
                        <div class="card-back" style="background: url('images/pda.png') no-repeat center center / cover; padding: 0;">
                        </div>
                    </div>

                </div>
            </div>

            <!-- Informaci├│n del destino activo -->
            <div class="active-info-container" style="display: flex; flex-direction: column; align-items: center; gap: 15px; margin-top: 25px;">
                <div class="active-info-title-row">
                    <span class="title-line"></span>
                    <h3 class="active-title-3d" id="activeTitle">Cataratas del Iguaz├║</h3>
                    <span class="title-line"></span>
                </div>
                <p class="active-subtitle-3d" id="activeSubtitle" style="margin: 0; max-width: 600px; line-height: 1.4;">Maravilla del Mundo ΓÇó Paseo Privado</p>
                <button class="card-btn-action" id="activeCardBtn" data-dest="Cataratas del Iguaz├║ (Argentina)">CONSULTAR</button>
            </div>

            <!-- Navegaci├│n por puntos -->
            <div class="navigation-dots-3d" id="dotsContainer3D">
                <!-- Se generan din├ímicamente -->
            </div>
        </div>

                <div class="contenedor-catalogo" style="display: flex; justify-content: center; align-items: center; padding: 40px 15px; width: 100%;">
            <div class="video-card card" style="max-width: 650px; width: 100%; margin: 0 auto; box-shadow: 0 15px 35px rgba(0, 35, 102, 0.1); background: rgba(255, 255, 255, 0.85); border-radius: 16px; border: 1.5px solid rgba(255, 255, 255, 0.4); overflow: hidden; display: flex; flex-direction: column;">
                <div class="card-image" style="width: 100%; overflow: hidden;">
                    <img src="images/macuco_safari_real.jpg" alt="Macuco Safari" width="800" height="500"
                        style="width: 100%; height: auto; display: block; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.03)'" onmouseout="this.style.transform='scale(1)'">
                </div>
                <div class="card-content"
                    style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 35px 25px; gap: 20px; text-align: center; background: rgba(255, 255, 255, 0.95);">
                    <div style="text-align: center;">
                        <h3 style="font-family: 'Montserrat', sans-serif; font-weight: 900; letter-spacing: 2px; font-size: clamp(1.4rem, 4vw, 1.85rem); margin: 0 0 10px 0; color: #002366; text-transform: uppercase;">MACUCO SAFARI</h3>
                        <p style="color: #333333; font-size: clamp(0.9rem, 2vw, 1.05rem); margin: 0; line-height: 1.5; max-width: 600px;">Aventura extrema en las ca├¡das de agua.</p>
                    </div>
                    <a href="https://youtu.be/1dUpxFeU_u4?si=1p_wqlZU0Bks6DNa" target="_blank"
                        rel="noopener noreferrer" class="btn-video-elegant" style="text-decoration: none; display: inline-flex; align-items: center; gap: 8px; font-family: 'Montserrat', sans-serif; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px; color: #fff; background: rgba(255, 0, 0, 0.85); padding: 12px 25px; border-radius: 30px; box-shadow: 0 4px 15px rgba(255,0,0,0.4); transition: all 0.3s;" onmouseover="this.style.background='#ff0000'; this.style.transform='translateY(-2px)';" onmouseout="this.style.background='rgba(255, 0, 0, 0.85)'; this.style.transform='translateY(0)';">
                        <i class="fab fa-youtube" style="color: #fff; font-size: 1.1rem;"></i> Ver Aventura Macuco Safari
                    </a>
                </div>
            </div>
        </div>
    </section>


    <!-- Barra de botones horizontal -->
    <div class="horizontal-button-bar">
        <a href="#galeria" class="btn-horizontal-bar" aria-label="Galer├¡a de Fotos">
            <i class="fas fa-images"></i>
            <span>Galer├¡a</span>
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
        <h2 style="color: var(--amarillo); font-size: clamp(1.8rem, 5vw, 2.5rem); text-transform: uppercase; font-family: 'Oswald', sans-serif; letter-spacing: 2px; text-shadow: 2px 2px 5px rgba(0,0,0,0.8); margin-bottom: 10px;">┬┐Por qu├⌐ elegir Trifoz Turismo?</h2>
        <p class="subtitulo-info" style="color: #fff; font-size: clamp(1rem, 2.5vw, 1.25rem); font-weight: 500; opacity: 0.95; margin-bottom: 50px; text-shadow: 1px 1px 3px rgba(0,0,0,0.8);">Tu viaje so├▒ado en la Triple Frontera, con confort premium y un servicio dise├▒ado exclusivamente para ti.</p>

        <div class="info-content-wrapper" style="display: flex; flex-direction: column; gap: 40px; align-items: center; width: 100%;">
            <div class="info-side-image" onmouseover="this.style.borderColor='rgba(224, 160, 255, 0.8)'; this.style.transform='translateY(-5px)';" onmouseout="this.style.borderColor='rgba(0, 210, 255, 0.4)'; this.style.transform='translateY(0)';" style="width: 95%; max-width: 580px; aspect-ratio: 1.52; height: auto; position: relative; border-radius: 20px; overflow: hidden; box-shadow: 0 15px 35px rgba(0,0,0,0.5); border: 2px solid rgba(0, 210, 255, 0.4); transition: all 0.4s ease; margin: 0 auto;">
                <div class="car-slides" style="width: 100%; height: 100%; position: relative;">
                    <div class="car-slide active" style="position: absolute; inset: 0; opacity: 1; transition: opacity 1.2s ease-in-out; z-index: 1;">
                        <img src="images/1.1.jpeg" alt="Veh├¡culo premium Trifoz Turismo" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; transform: scale(1.02); transition: transform 5s ease-out;">
                        <div style="position: absolute; inset: 0; background: rgba(0, 0, 0, 0.35); z-index: 2; pointer-events: none;"></div>
                    </div>
                    <div class="car-slide" style="position: absolute; inset: 0; opacity: 0; transition: opacity 1.2s ease-in-out; z-index: 1;">
                        <img src="images/car2 - copia.jpeg" alt="Veh├¡culo premium Trifoz Turismo" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; transform: scale(1.02); transition: transform 5s ease-out;">
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
                    <h2>EXPLORA FOZ DO IGUA├çU CON NOSOTROS</h2>
                    <p>
                        Descubrir la inmensidad de las Cataratas y la biodiversidad ├║nica de la selva paranaense es una experiencia inolvidable. Nos complace acompa├▒arte de forma cercana y segura, ofreciendo un servicio de traslados privados dise├▒ado a tu medida.
                    </p>
                </div>
                <div class="columna">
                    <p>
                        Nos encargamos de toda la log├¡stica: desde recogidas puntuales en los aeropuertos de la regi├│n hasta los cruces fronterizos hacia Argentina y Paraguay, facilitando los tr├ímites aduaneros para que tu ├║nica preocupaci├│n sea disfrutar de la naturaleza. Adem├ís, organizamos paseos confortables dentro del territorio brasile├▒o, garantizando itinerarios flexibles tanto para viajeros individuales como para familias y grupos organizados. Nuestro guiado incluye comunicaci├│n accesible en espa├▒ol, portugu├⌐s y LIBRAS, buscando siempre brindar un trato c├ílido y humano.
                    </p>
                    <div style="border-top: 1px solid rgba(255, 255, 255, 0.15); padding-top: 20px; margin-top: 20px;">
                        <h3 style="color: #00d2ff; font-family: 'Montserrat', sans-serif; font-weight: 800; font-size: 1.1rem; margin: 0 0 8px 0; text-transform: uppercase; letter-spacing: 0.5px;">Naturaleza &amp; Paseos</h3>
                        <p style="font-size: 0.95rem; opacity: 0.85; margin: 0; line-height: 1.4;">Tours guiados por las Cataratas y los rincones m├ís bellos de la regi├│n.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    
    

    
    <!-- SECCI├ôN GALER├ìA DE FOTOS -->
    <section id="galeria" class="galeria-franja">
        <div class="galeria-overlay"></div>
        <div class="galeria-slides-container" style="width: 100%; height: 100%; position: relative;">
            <div class="galeria-slide active">
                <img src="images/cataratas.jpg" alt="Cataratas del Iguaz├║" class="galeria-img">
                <div class="galeria-content">
                    <span class="galeria-title">Cataratas del Iguaz├║</span>
                    <span class="galeria-subtitle">Una de las siete maravillas naturales del mundo</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/aeroporto.jpg" alt="Traslados al Aeropuerto" class="galeria-img">
                <div class="galeria-content">
                    <span class="galeria-title">Traslados al Aeropuerto</span>
                    <span class="galeria-subtitle">Puntualidad y confort 24/7 en la Triple Frontera</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/templo budista 1.png" alt="Templo Budista Chen Tien" class="galeria-img">
                <div class="galeria-content">
                    <span class="galeria-title">Templo Budista Chen Tien</span>
                    <span class="galeria-subtitle">Paz, meditaci├│n y espectaculares esculturas en Foz</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/mezquita 1.png" alt="Mezquita Omar Ibn Al-Khattab" class="galeria-img" style="object-fit: contain; background-color: #050510;">
                <div class="galeria-content">
                    <span class="galeria-title">Mezquita Omar Ibn Al-Khattab</span>
                    <span class="galeria-subtitle">Arquitectura isl├ímica y riqueza cultural en el coraz├│n de Foz</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/cataratas_panorama.png" alt="Vistas Panor├ímicas" class="galeria-img">
                <div class="galeria-content">
                    <span class="galeria-title">Vistas Panor├ímicas</span>
                    <span class="galeria-subtitle">Paisajes ├║nicos e inolvidables de la selva</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/china 1.png" alt="Cultura y Sabores" class="galeria-img">
                <div class="galeria-content">
                    <span class="galeria-title">Cultura y Sabores</span>
                    <span class="galeria-subtitle">Experiencias gastron├│micas y multiculturales locales</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/dutty.jpeg" alt="Duty Free Shop" class="galeria-img">
                <div class="galeria-content">
                    <span class="galeria-title">Duty Free Shop</span>
                    <span class="galeria-subtitle">Compras internacionales exclusivas libre de impuestos</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/feirinha argentina.jpeg" alt="Feirinha de Puerto Iguaz├║" class="galeria-img">
                <div class="galeria-content">
                    <span class="galeria-title">Feirinha de Puerto Iguaz├║</span>
                    <span class="galeria-subtitle">Sabores locales, olivas y quesos tradicionales</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/Kattamaram (2).jpeg" alt="Paseo en Kattamaram" class="galeria-img">
                <div class="galeria-content">
                    <span class="galeria-title">Paseo en Kattamaram</span>
                    <span class="galeria-subtitle">Navegaci├│n inolvidable en el encuentro de los r├¡os</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/museo de cera.png" alt="Dreamland Museo de Cera" class="galeria-img">
                <div class="galeria-content">
                    <span class="galeria-title">Dreamland Museo de Cera</span>
                    <span class="galeria-subtitle">Diversi├│n para toda la familia con r├⌐plicas perfectas</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/pda.png" alt="Parque de las Aves" class="galeria-img">
                <div class="galeria-content">
                    <span class="galeria-title">Parque de las Aves</span>
                    <span class="galeria-subtitle">Contacto directo con la fauna y aves rescatadas</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/usina hidrelectrica.jpeg" alt="Itaip├║ Binacional" class="galeria-img">
                <div class="galeria-content">
                    <span class="galeria-title">Itaip├║ Binacional</span>
                    <span class="galeria-subtitle">Una de las mayores obras de ingenier├¡a del planeta</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/wonder_park_v2.jpg" alt="Wonder Park Show" class="galeria-img">
                <div class="galeria-content">
                    <span class="galeria-title">Wonder Park Show</span>
                    <span class="galeria-subtitle">Espect├ículos de luces y atracciones interactivas</span>
                </div>
            </div>
            <div class="galeria-slide">
                <img src="images/yup star.jpeg" alt="Yup Star Foz" class="galeria-img">
                <div class="galeria-content">
                    <span class="galeria-title">Yup Star Foz</span>
                    <span class="galeria-subtitle">Una de las ruedas de la fortuna m├ís grandes de Am├⌐rica Latina</span>
                </div>
            </div>
        </div>
        <button class="galeria-nav-btn prev" aria-label="Anterior">&#x276E;</button>
        <button class="galeria-nav-btn next" aria-label="Siguiente">&#x276F;</button>
        <div class="galeria-dots">
            <span class="galeria-dot active" data-index="0"></span>
            <span class="galeria-dot" data-index="1"></span>
            <span class="galeria-dot" data-index="2"></span>
            <span class="galeria-dot" data-index="3"></span>
            <span class="galeria-dot" data-index="4"></span>
            <span class="galeria-dot" data-index="5"></span>
            <span class="galeria-dot" data-index="6"></span>
            <span class="galeria-dot" data-index="7"></span>
            <span class="galeria-dot" data-index="8"></span>
            <span class="galeria-dot" data-index="9"></span>
            <span class="galeria-dot" data-index="10"></span>
            <span class="galeria-dot" data-index="11"></span>
            <span class="galeria-dot" data-index="12"></span>
        </div>
    </section>

    <footer>
        <div class="social-buttons-footer">
            <a href="mailto:trifozturismo@gmail.com" class="btn-social btn-email" aria-label="Enviar Email"><i
                    class="fa-solid fa-envelope"></i></a>
            <a href="https://www.facebook.com/share/1Qr8RiKxrz/" target="_blank" rel="noopener noreferrer"
                class="btn-social btn-facebook" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
            <a href="https://www.instagram.com/trifoz.turismo" target="_blank" rel="noopener noreferrer"
                class="btn-social btn-instagram" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
        </div>
        <p>┬⌐ 2026 Trifoz Turismo ΓÇó Gu├¡a Tur├¡stico Ebert ΓÇó Foz de Iguaz├║</p>
    </footer>

    <!-- Librer├¡as de animaci├│n GSAP y Draggable -->