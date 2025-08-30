import streamlit as st
from PIL import Image

imagen_perfil_linkedn = "https://media.licdn.com/dms/image/v2/D4D03AQGckbHJt1p9yw/profile-displayphoto-shrink_400_400/B4DZZa1GXoGgAk-/0/1745280592269?e=1759363200&v=beta&t=vvCHc5JRY2VskTZFhw3o0kKi922naMwBJPPCWhMh9YI"


# Estilos CSS para redondear la imagen
st.markdown("""
    <style>
        img {
            border-radius: 50%;
            object-fit: cover;
        }
        [data-testid="stImage"] {
            text-align: center;
        }
        .boton-contacto {
            text-align: center;
        }

    </style>
""", unsafe_allow_html=True)



st.write("# Acerca de mi")

col1 , col2 = st.columns([1,2])

with col1:

    #imagen_cara = Image.open("image/Carusso.jpeg")
    st.image(imagen_perfil_linkedn,  caption="David Carusso | Data Analyst")


with col2:
    st.markdown("""
        ## 👋 Hola! Soy **David Carusso**
        **💻 Desarrollador Python | 📊 Analista de Datos**
        
        ### Habilidades Técnicas:
        - 🐼 Procesamiento de datos con Pandas
        - 📈 Visualizaciones 
        - 🚀 Desarrollo de aplicaciones con Streamlit
        - 📊 Business Intelligence con Power BI
        
        ### En constante aprendizaje...
        """)

    st.markdown('<div class="boton-contacto">', unsafe_allow_html=True)
    st.link_button(
        "📬 Contacto", 
        "https://www.linkedin.com/in/davidcarusso/",
        help="Haz click para visitar mi perfil profesional.",
        type="secondary" )  # lo envia a otra pestaña, sin cerrar la principal
    st.markdown("</div>", unsafe_allow_html=True)


# Footer con badges
st.divider()
cols = st.columns(5)
with cols[0]:
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/davidcarusso)")
#Añadir más badges según necesites

# Sección de certificaciones
with st.expander("📚 Certificaciones y Cursos"):
    st.write("""
    - Microsoft Power BI Certification (Censosud)
    - Python for Data Science (Platzy)
    """)
