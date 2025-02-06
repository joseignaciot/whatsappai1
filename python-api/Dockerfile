# Usa una imagen base de Python 3.10-slim
FROM python:3.10-slim

# Instala dependencias básicas (opcional, si las necesitas)
RUN apt-get update && \
    apt-get install -y git wget gcc g++ && \
    rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt
COPY requirements.txt /app/

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación (por ejemplo, app.py)
COPY . /app

# Cambia los permisos de setup.sh para que sea ejecutable
RUN chmod +x setup.sh

# Expone el puerto (si es necesario)
EXPOSE 5000

# Comando de inicio (ajústalo según tu aplicación)
CMD ["python", "app.py"]
