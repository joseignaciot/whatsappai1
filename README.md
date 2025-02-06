# Proyecto WhatsAppAI

Este proyecto se compone de varios servicios que se gestionan mediante Docker Compose. Cada servicio se encarga de una parte del sistema (por ejemplo, n8n, deepseek, python-api, admin-panel y nocodb) y se ejecuta íntegramente en contenedores.

## Requisitos Previos

- Tener Docker y Docker Compose instalados en tu sistema.

## Estructura del Proyecto

- **docker-compose.yml**: Define los servicios y los volúmenes que se usarán.
- **deepseek/**: Contiene el Dockerfile y el entrypoint para servir el modelo con vLLM.
- **python-api/**: Contiene el Dockerfile, requirements.txt y el código de la API (app.py).
- **admin-panel/**: Contiene el Dockerfile, requirements.txt y el código de la aplicación del panel de administración.
- **nocodb/**: Se utiliza la imagen oficial de nocodb.

## Construcción y Ejecución

Para construir las imágenes y levantar todos los servicios en contenedores, ejecuta el siguiente comando en el directorio raíz del proyecto:

```bash
docker compose up --build
