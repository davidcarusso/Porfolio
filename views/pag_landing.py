import streamlit as st

# ========== SEO y Meta Tags ==========
st.markdown("""
    <!-- Meta Tags para SEO -->
    <meta name="description" content="Consultor de Business Intelligence en Buenos Aires. Dashboards interactivos con Streamlit y Power BI. Análisis de datos personalizados para PyMEs. Primera consulta gratis.">
    <meta name="keywords" content="consultor business intelligence, dashboards streamlit, power bi buenos aires, análisis de datos python, visualización de datos, automatización reportes, consultor bi zona sur, desarrollador python buenos aires">
    <meta name="author" content="David Carusso">
    <meta name="robots" content="index, follow">
    <meta name="language" content="Spanish">
    <meta name="geo.region" content="AR-B">
    <meta name="geo.placename" content="Buenos Aires">
    
    <!-- Open Graph para redes sociales -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="David Carusso - Consultor BI & Dashboards | Buenos Aires">
    <meta property="og:description" content="Transformá tus datos en decisiones estratégicas. Dashboards interactivos y análisis personalizados con Python y Power BI.">
    <meta property="og:url" content="https://davidcarusso.com.ar">
    <meta property="og:site_name" content="David Carusso Portfolio">
    <meta property="og:locale" content="es_AR">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="David Carusso - Consultor BI & Dashboards">
    <meta name="twitter:description" content="Dashboards interactivos con Streamlit y Power BI en Buenos Aires">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="https://davidcarusso.com.ar">
    
    <!-- Schema.org para Google -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "ProfessionalService",
      "name": "David Carusso - Consultoría BI",
      "image": "https://davidcarusso.com.ar/logo.png",
      "description": "Consultor de Business Intelligence especializado en dashboards interactivos con Streamlit y Power BI en Buenos Aires",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Buenos Aires",
        "addressRegion": "Buenos Aires",
        "addressCountry": "AR"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": -34.6037,
        "longitude": -58.3816
      },
      "url": "https://davidcarusso.com.ar",
      "telephone": "+5491150419371",
      "email": "david.ismael.carusso@gmail.com",
      "priceRange": "$",
      "openingHoursSpecification": {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "opens": "09:00",
        "closes": "18:00"
      },
      "sameAs": [
        "https://www.linkedin.com/in/davidcarusso/",
        "https://github.com/davidcarusso"
      ],
      "areaServed": {
        "@type": "GeoCircle",
        "geoMidpoint": {
          "@type": "GeoCoordinates",
          "latitude": -34.6037,
          "longitude": -58.3816
        },
        "geoRadius": "50000"
      },
      "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Servicios de Business Intelligence",
        "itemListElement": [
          {
            "@type": "Offer",
            "itemOffered": {
              "@type": "Service",
              "name": "Dashboards Interactivos",
              "description": "Visualizaciones dinámicas con Streamlit y Plotly"
            }
          },
          {
            "@type": "Offer",
            "itemOffered": {
              "@type": "Service",
              "name": "Business Intelligence",
              "description": "Análisis profundo de datos con Power BI y Python"
            }
          },
          {
            "@type": "Offer",
            "itemOffered": {
              "@type": "Service",
              "name": "Automatización de Procesos",
              "description": "Scripts personalizados para eliminar tareas repetitivas"
            }
          }
        ]
      }
    }
    </script>
""", unsafe_allow_html=True)

# CSS personalizado para la landing
st.markdown("""
    <style>
        /* Hero section */
        .hero-section {
            text-align: center;
            padding: 3rem 1rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px;
            color: white;
            margin-bottom: 2rem;
        }
        .hero-title {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }
        .hero-subtitle {
            font-size: 1.3rem;
            margin-bottom: 2rem;
            opacity: 0.95;
        }
        
        /* Sección de servicios */
        .service-card {
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 4px solid #667eea;
            margin-bottom: 1rem;
            transition: transform 0.2s;
        }
        .service-card:hover {
            transform: translateX(5px);
        }
        
        /* CTA buttons */
        .cta-container {
            text-align: center;
            margin: 2rem 0;
        }
        
        /* Stats */
        .stat-box {
            text-align: center;
            padding: 1rem;
            background: #f8f9fa;
            border-radius: 8px;
        }
        .stat-number {
            font-size: 2rem;
            font-weight: 700;
            color: #667eea;
        }
        .stat-label {
            font-size: 0.9rem;
            color: #6c757d;
        }
        
        /* Testimonials */
        .testimonial {
            background: #fff;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">📊 Transformá tus datos en decisiones estratégicas</h1>
        <p class="hero-subtitle">Dashboards interactivos y análisis de datos personalizados con Streamlit y Power BI</p>
    </div>
""", unsafe_allow_html=True)

# CTAs principales
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div class="cta-container">', unsafe_allow_html=True)
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        st.link_button(
            "💬 Consultá por WhatsApp",
            "https://wa.me/5491150419371?text=Hola%20David,%20vi%20tu%20portafolio%20y%20me%20interesa%20una%20consultoría",
            use_container_width=True,
            type="primary"
        )
    with col_btn2:
        st.link_button(
            "📧 Enviame un email",
            "mailto:david.ismael.carusso@gmail.com?subject=Consulta sobre servicios de BI",
            use_container_width=True
        )
    
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# Sección: ¿Por qué elegirme?
st.markdown("## 🎯 ¿Por qué trabajar conmigo?")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-number">100%</div>
            <div class="stat-label">Proyectos personalizados</div>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-number">Python</div>
            <div class="stat-label">Tecnología moderna</div>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-number">24-48h</div>
            <div class="stat-label">Respuesta inicial</div>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# Servicios
st.markdown("## 💼 Servicios")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="service-card">
            <h3>📈 Dashboards Interactivos</h3>
            <p>Visualizaciones dinámicas con Streamlit y Plotly que actualizan en tiempo real.</p>
            <ul>
                <li>Análisis de ventas y KPIs</li>
                <li>Monitoreo de operaciones</li>
                <li>Reportes automatizados</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="service-card">
            <h3>🔄 Automatización de Procesos</h3>
            <p>Eliminá tareas repetitivas y ahorrá tiempo con scripts personalizados.</p>
            <ul>
                <li>Procesamiento de archivos Excel/CSV</li>
                <li>Reportes automáticos por email</li>
                <li>Integración con APIs</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="service-card">
            <h3>📊 Business Intelligence</h3>
            <p>Análisis profundo de datos con Power BI y Python.</p>
            <ul>
                <li>Modelos de datos optimizados</li>
                <li>Métricas personalizadas</li>
                <li>Integración de múltiples fuentes</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="service-card">
            <h3>🚀 Aplicaciones Web</h3>
            <p>Herramientas internas para tu equipo, sin complicaciones.</p>
            <ul>
                <li>Apps de gestión empresarial</li>
                <li>Herramientas de análisis</li>
                <li>Portales de datos</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# Proyectos destacados
st.markdown("## 🎨 Proyectos Demostrativos")
st.markdown("*Explorá ejemplos reales de lo que puedo hacer por tu negocio*")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("### 📊 Dashboard de Ventas")
        st.markdown("Sistema interactivo con filtros, mapas y análisis temporal.")
        if st.button("Ver Demo →", key="demo1", use_container_width=True):
            st.switch_page("views/pag_plotly.py")

with col2:
    with st.container(border=True):
        st.markdown("### 🎓 Análisis Educativo")
        st.markdown("Visualización de costos universitarios con filtros geográficos.")
        if st.button("Ver Demo →", key="demo2", use_container_width=True):
            st.switch_page("views/pag_costo_universidades.py")

with col3:
    with st.container(border=True):
        st.markdown("### 🖼️ Herramienta Útil")
        st.markdown("Compresor de imágenes con ajuste de calidad.")
        if st.button("Ver Demo →", key="demo3", use_container_width=True):
            st.switch_page("views/pag_compresion_imagen.py")

st.divider()

# Proceso de trabajo
st.markdown("## 🔄 ¿Cómo trabajamos juntos?")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        **1️⃣ Consulta inicial**  
        Hablamos de tus necesidades y objetivos (gratis, sin compromiso)
    """)

with col2:
    st.markdown("""
        **2️⃣ Propuesta**  
        Te envío un plan de trabajo con tiempos y costos
    """)

with col3:
    st.markdown("""
        **3️⃣ Desarrollo**  
        Creo la solución con entregas parciales para tu feedback
    """)

with col4:
    st.markdown("""
        **4️⃣ Entrega**  
        Recibís tu proyecto + documentación + soporte inicial
    """)

st.divider()

# Testimonios (adaptados de proyectos)
st.markdown("## 💬 Lo que dicen de mi trabajo")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="testimonial">
            <p><em>"Los dashboards que desarrollo son claros, interactivos y fáciles de usar. Se nota la atención al detalle."</em></p>
            <strong>— Análisis de portafolio técnico</strong>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="testimonial">
            <p><em>"Dominio sólido de Python, Pandas y Plotly. Capacidad demostrada para crear visualizaciones profesionales."</em></p>
            <strong>— Evaluación técnica</strong>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# FAQ
with st.expander("❓ Preguntas Frecuentes"):
    st.markdown("""
    **¿Cuánto tiempo toma un proyecto?**  
    Depende de la complejidad. Un dashboard básico puede estar listo en 1-2 semanas. Proyectos más complejos pueden tomar 3-4 semanas.
    
    **¿Trabajás con empresas de todos los tamaños?**  
    Sí, desde emprendimientos hasta PyMEs. Adapto las soluciones a tu presupuesto y necesidades.
    
    **¿Qué incluye el servicio?**  
    Desarrollo, documentación, capacitación básica y soporte post-entrega durante 30 días.
    
    **¿Necesito conocimientos técnicos?**  
    No, me encargo de todo. Solo necesitás tener clara tu necesidad de negocio.
    
    **¿Ofrecés mantenimiento?**  
    Sí, podemos armar un plan de soporte mensual para actualizaciones y mejoras.
    """)

# CTA Final
st.markdown("---")
st.markdown("## 🚀 ¿Listo para empezar?")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
        <div style="text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 10px;">
            <h3>Primera consulta sin cargo</h3>
            <p>Hablemos de tu proyecto y veamos cómo puedo ayudarte</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_final1, col_final2 = st.columns(2)
    with col_final1:
        st.link_button(
            "💬 WhatsApp",
            "https://wa.me/5491150419371?text=Hola%20David,%20quiero%20agendar%20una%20consulta",
            use_container_width=True,
            type="primary"
        )
    with col_final2:
        st.link_button(
            "📧 Email",
            "mailto:david.ismael.carusso@gmail.com",
            use_container_width=True
        )

# Footer
st.divider()
st.markdown("""
    <div style="text-align: center; color: #6c757d; padding: 1rem;">
        <p>📍 Zona Sur GBA - Buenos Aires, Argentina | 📱 +54 9 11 5041-9371</p>
        <p>
            <a href="https://www.linkedin.com/in/davidcarusso/" target="_blank">LinkedIn</a> | 
            <a href="https://github.com/davidcarusso" target="_blank">GitHub</a>
        </p>
    </div>
""", unsafe_allow_html=True)