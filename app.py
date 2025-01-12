import streamlit as st

from views.pag_compresion_imagen import comprimir_imagens_pag

# --- Configuracion de Pagina ---
def configuracion_pagina():
    st.set_page_config(
        page_title="David Carusso"
    )


def iniciar_menu(): 
    # --- Crea el objeto pagina para luego agrupparlos --- 
    pagina_1 = st.Page(
                page= "views/pag_aboutme.py",
                title= "Acerca de mi",
                default=True 
            )

    pagina_2 = st.Page(
                page= "views/pag_compresion_imagen.py",
                title="Comprimir Imagen"
            )

    # --- Crear un diccionario para agrupar en un indice --- 
    pages =  {
            "Informacion" : [pagina_1] , 
            "Proyectos" : [pagina_2]
        }

    # --- Crea el objeto multipagina --- 
    pg = st.navigation(pages)
    pg.run()


# --- Inicializacion de funciones ---
if __name__ == "__main__":
    configuracion_pagina()
    iniciar_menu()



