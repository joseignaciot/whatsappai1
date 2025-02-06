# Usa una imagen base ligera de Python 3.10-slim
FROM python:3.10-slim

# Instala dependencias básicas: git, wget, gcc y g++
RUN apt-get update && \
    apt-get install -y git wget gcc g++ && \
    rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Instala vLLM desde PyPI
RUN pip install --no-cache-dir vllm

# Copia el entrypoint al contenedor y le da permisos de ejecución
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expone el puerto que vLLM utiliza (ajusta si es necesario)
EXPOSE 8000

# Usa el entrypoint para iniciar el servicio
CMD ["/entrypoint.sh"]
