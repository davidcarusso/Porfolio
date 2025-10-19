import qrcode
from io import BytesIO


def generate_qr_image(data, box_size=15, border=4, error_correction='H'):
    """
    Genera un código QR a partir de los datos proporcionados.
    
    Args:
        data (str): Texto o URL para convertir en QR
        box_size (int): Tamaño de cada caja del QR (default: 15)
        border (int): Tamaño del borde (default: 4)
        error_correction (str): Nivel de corrección de errores ('L', 'M', 'Q', 'H')
    
    Returns:
        BytesIO: Buffer con la imagen del QR en formato PNG
    """
    # Mapeo de niveles de corrección de errores
    error_levels = {
        'L': qrcode.constants.ERROR_CORRECT_L,
        'M': qrcode.constants.ERROR_CORRECT_M,
        'Q': qrcode.constants.ERROR_CORRECT_Q,
        'H': qrcode.constants.ERROR_CORRECT_H
    }
    
    # Crear el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=error_levels.get(error_correction, qrcode.constants.ERROR_CORRECT_H),
        box_size=box_size,
        border=border,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    # Generar la imagen
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convertir a BytesIO
    buf = BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    
    return buf


def validate_url(url):
    """
    Valida si una URL tiene un formato básico correcto.
    
    Args:
        url (str): URL a validar
    
    Returns:
        bool: True si la URL parece válida, False en caso contrario
    """
    if not url:
        return False
    
    # Validación básica
    url = url.strip()
    valid_prefixes = ['http://', 'https://', 'www.']
    
    return any(url.startswith(prefix) for prefix in valid_prefixes) or '.' in url