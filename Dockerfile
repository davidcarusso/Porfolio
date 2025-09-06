
# Usa una imagen base con Python
FROM python:3.10

# Crea un directorio para la app
WORKDIR /app

# Copia los archivos de tu proyecto
COPY . /app

# Instala las dependencias
RUN pip install -r requirements.txt

# Expone el puerto 5000
EXPOSE 5000

# Comando para ejecutar la app
CMD ["streamlit", "run", "app.py"]


