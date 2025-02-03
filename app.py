import streamlit as st


# --- Configuracion de Pagina ---
def configuraciones():
    st.set_page_config(page_title="David Carusso")

 
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

    # --- Crear un diccionario para agrupar en un indice --- 
    pages =  {
    "Informacion" : [pagina_1] , 
    "Proyectos" : [pagina_2, pagina_3]
    }

    # --- Crea el objeto multipagina --- 
    pg = st.navigation(pages)
    pg.run()


if __name__ == "__main__":
    configuraciones()
    paginas()