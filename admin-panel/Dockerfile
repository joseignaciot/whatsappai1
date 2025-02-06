# Utiliza una imagen base de Python 3.10-slim
FROM python:3.10-slim

# Instala dependencias básicas necesarias (git, wget, gcc y g++)
RUN apt-get update && \
    apt-get install -y git wget gcc g++ && \
    rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos e instala las dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación (incluyendo app.py y demás archivos)
COPY . /app

# Expone el puerto que use tu aplicación (ajústalo según lo que hayas configurado en app.py)
EXPOSE 8080

# Comando de inicio: ejecuta app.py con Python
CMD ["python", "app.py"]
