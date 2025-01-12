import streamlit as st
from PIL import Image


st.write("# Acerca de mi")

col1 , col2 = st.columns([1,2])

with col1: 
    imagen_cara = Image.open("image/foto_personal.jpg")
    st.image(imagen_cara)


with col2:
    st.write("""
             👋 Hola! Soy David Carusso 💻 
             Desarrollador en Python y analista de datos. 📊 
             
             - Uso pandas, Seaborn, Streamlit y Power BI. """)
    st.write("🚀 Aprendiendo cada día.")
    st.button("### Contacto")