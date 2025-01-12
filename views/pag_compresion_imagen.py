import streamlit as st
from PIL import Image
import io



def comprimir_imagens_pag():
    st.write("# Aplicacion de imagenes")


    archivo = st.file_uploader("Ingrese una imagen", type=["jpg", "jpeg"])


    if archivo is not None:

        # Elegir la calidad con un slider
        calidad = st.slider("Seleccionar la calidad de compresion",min_value= 0 , max_value=100, value=15 , step= 5)

        #abrir la imagen 
        imagen_original = Image.open(archivo)

        # comprimir la imagen
        buffer = io.BytesIO()
        imagen_original.save(buffer, format="JPEG", optimize=True, quality = calidad)
        buffer.seek(0)  # Regresar al inicio del buffer


        imagen_comprimida = Image.open(buffer)

        tamaño_original = round( (archivo.size) / (1024**2), 1)
        tamaño_comprimido = round( (buffer.getbuffer().nbytes) / ( 1024**2) , 1)

        col1, col2 = st.columns(2)
        with col1:
            st.image(archivo, caption="Imagen Original")
            st.write(f"{ round(archivo.size / (1024*1024), 1 )} MB")
        with col2:
            st.image(imagen_comprimida, caption="Imagen Comprimida")
            st.write(f"{round(buffer.getbuffer().nbytes / (1024*1024), 1 ) } MB" )

        diferencia_porcentual = round(-((tamaño_original - tamaño_comprimido) / tamaño_original )*100, 1)
        st.write(
                {
                    "Peso actual" : f"{tamaño_comprimido} MB",
                    "Diferencia" : f"{diferencia_porcentual} %"}
                )


        # Descargar archivo
        ext = ".jpeg"
        nombre_archivo = st.text_input("Para Descargar ingresa el nombre del archivo")

        if nombre_archivo:
            nombre_archivo = nombre_archivo + ext
            st.download_button("Descargar", data=buffer, file_name = nombre_archivo , mime="image/jpg")
        else:
            st.warning("Ingresar un nombre")     

    else:
        st.warning("Subir una foto")


comprimir_imagens_pag()





    

    
