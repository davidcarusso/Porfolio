import streamlit as st


# --- Configuracion de Pagina ---
def configuraciones():
    st.set_page_config(
        page_title="David Carusso",
        page_icon= "📊" ,
        initial_sidebar_state="auto")

 
# --- Crea el objeto pagina para luego agrupparlos --- 
def paginas():
    pagina_1 = st.Page(
    page= "views/pag_aboutme.py",
    title= "Acerca de mi",
    default=True 
    )

    pagina_2 = st.Page(
    page= "views/pag_compresion_imagen.py",
    title="Comprimir Imagen"
    )

    pagina_3 = st.Page(
    page="views/pag_plotly.py",
    title="Graficos Plotly"
    )
    
    pagina_4 = st.Page(
    page="views/pag_costo_universidades.py",
    title="Costo Universidades"
    )

    pagina_5 = st.Page(
    page= "views/powerapps.py",
    title= "Apps Comercial Presencial" 
    )
    
    

    # --- Crear un diccionario para agrupar en un indice --- 
    pages =  {
    "Informacion" : [pagina_1] , 
    "Herramientas" : [pagina_2 ], 
    "Analisis de Datos": [pagina_3, pagina_4],
    "PowerApps Tools": [pagina_5]
    }

    # --- Crea el objeto multipagina --- 
    pg = st.navigation(pages, position="top")

    return pg


if __name__ == "__main__":
    configuraciones()
    pg = paginas()
    pg.run()