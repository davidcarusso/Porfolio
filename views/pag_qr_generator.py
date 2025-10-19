import streamlit as st

from scripts.qr_generator import generate_qr_image


def apply_custom_styles():
    """Aplica estilos CSS personalizados a la aplicación."""
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
        }
        .stTextInput > div > div > input {
            font-size: 20px;
        }
        h1 {
            text-align: center;
            color: #E31837;
        }
        .info-text {
            text-align: center;
            font-size: 18px;
            color: #666;
        }
        </style>
    """, unsafe_allow_html=True)


def render_header():
    """Renderiza el header de la aplicación."""
    st.markdown("<h1>📱 Generador de QR - Cencosud</h1>", unsafe_allow_html=True)
    st.markdown("<p class='info-text'>El cliente debe escanear el código QR desde su dispositivo</p>", unsafe_allow_html=True)
    st.write("")
    st.write("")


def render_input_section(widget_key=0):
    """
    Renderiza la sección de input para ingresar la URL.
    
    Args:
        widget_key: Key única para recrear el widget
    
    Returns:
        str: URL ingresada por el usuario
    """
    input_web_path = st.text_input(
        "Ingrese la ruta web (URL):",
        placeholder="https://ejemplo.com",
        label_visibility="visible",
        key=f"url_input_{widget_key}"
    )
    st.write("")
    
    return input_web_path


def render_qr_display(qr_buffer):
    """
    Renderiza el código QR generado en pantalla.
    
    Args:
        qr_buffer (BytesIO): Buffer con la imagen del QR
    """
    # Centrar el QR y mostrarlo grande
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.image(qr_buffer, width="stretch")
        st.markdown(
            "<p style='text-align: center; font-size: 16px; color: #666;'>Escanea este código QR</p>",
            unsafe_allow_html=True
        )
    
    # Botón para limpiar
    st.write("")
    st.write("")
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
    with col_btn2:
        if st.button("🔄 Generar otro QR", width="stretch"):
            # Incrementar el contador para crear un nuevo widget con key diferente
            st.session_state.widget_key += 1
            st.rerun()


def render_empty_state():
    """Renderiza el estado vacío cuando no hay input."""
    st.info("👆 Ingresa una URL para generar el código QR que el cliente debe escanear")
    st.write("")
    st.write("")
    st.markdown("""
        <div style='text-align: center; padding: 2rem;'>
            <p style='font-size: 18px; color: #999;'>
                📱 El código QR aparecerá aquí<br>
                listo para ser escaneado por el cliente
            </p>
        </div>
    """, unsafe_allow_html=True)




# Inicializar contador para forzar recreación del widget
if 'widget_key' not in st.session_state:
    st.session_state.widget_key = 0

# Aplicar estilos personalizados
apply_custom_styles()

# Renderizar header
render_header()

# Renderizar sección de input
input_web_path = render_input_section(st.session_state.widget_key)

# Generar y mostrar QR si hay input
if input_web_path:
    try:
        qr_buffer = generate_qr_image(input_web_path)
        render_qr_display(qr_buffer)
        
    except Exception as e:
        st.error(f"❌ Error al generar el código QR: {str(e)}")
else:
    # Mostrar mensaje cuando no hay input
    st.info("👆 Ingresa una URL para generar el código QR que el cliente debe escanear")
    st.write("")
    st.write("")
    st.markdown("""
        <div style='text-align: center; padding: 2rem;'>
            <p style='font-size: 18px; color: #999;'>
                📱 El código QR aparecerá aquí<br>
                listo para ser escaneado por el cliente
            </p>
        </div>
    """, unsafe_allow_html=True)
