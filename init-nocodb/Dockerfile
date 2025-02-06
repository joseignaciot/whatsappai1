# Usa una imagen base de Python 3.10-slim
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos e instala las dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el script de inicialización
COPY init_nocodb.py /app/

# Comando de inicio: ejecuta el script
CMD ["python", "init_nocodb.py"]
