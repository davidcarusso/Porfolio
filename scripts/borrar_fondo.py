from rembg import remove

def borrar_fondo_imagen(archivo):
    #ruta de imagen
    path_imagen = "image/foto_personal.jpg"
    #Abrir el archivo 
    entrada_imagen = archivo.read()
    #eliminamos el fondo
    salida_imagen = remove(entrada_imagen)

    return salida_imagen


borrar_fondo_imagen()




