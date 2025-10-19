import streamlit as st


# --- Configuracion de Pagina ---
def configuraciones():
    st.set_page_config(
        page_title="David Carusso - Consultor BI & Dashboards",
        page_icon="📊",
        initial_sidebar_state="auto",
        menu_items={
            'Get Help': 'https://wa.me/5491150419371',
            'Report a bug': "mailto:david.ismael.carusso@gmail.com",
            'About': "# David Carusso\nConsultor de Business Intelligence y Desarrollo Python"
        })

 
# --- Crea el objeto pagina para luego agruparlos --- 
def paginas():
    # Landing como página principal
    pagina_landing = st.Page(
        page="views/pag_landing.py",
        title="🏠 Inicio",
        url_path="/",
        default=True
    )
    
    pagina_about = st.Page(
        page="views/pag_aboutme.py",
        title="👤 Acerca de mi",
        url_path="about-me"
    )

    pagina_2 = st.Page(
        page="views/pag_compresion_imagen.py",
        title="🖼️ Comprimir Imagen",
        url_path="image-compression"
    )

    pagina_3 = st.Page(
        page="views/pag_plotly.py",
        title="📊 Dashboard de Ventas",
        url_path="sales-dashboard"
    )
    
    pagina_4 = st.Page(
        page="views/pag_costo_universidades.py",
        title="🎓 Análisis Universidades",
        url_path="university-cost-analysis"
    )

    pagina_5 = st.Page(
        page="views/powerapps.py",
        title="🚀 PowerApps Demo",
        url_path="powerapps-demo"
    )

    pagina_6 = st.Page(
        page="views/pag_qr_generator.py",
        title="⛆ Qr Generator",
        url_path="qr-code-generator"
    )
    
    # --- Crear un diccionario para agrupar en un indice --- 
    pages = {
        "Principal": [pagina_landing],
        "Sobre mí": [pagina_about],
        "Demos Técnicas": [pagina_3, pagina_4, pagina_2, pagina_6],
        "Otros Proyectos": [pagina_5]
    }

    # --- Crea el objeto multipagina --- 
    pg = st.navigation(pages, position="sidebar")

    return pg


if __name__ == "__main__":
    configuraciones()
    pg = paginas()
    pg.run()