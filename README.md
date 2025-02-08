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


Base de datos:
Creo una con phpmyadmin que se llama weather_db y despues ejecuto esto para crear la tabla:

CREATE TABLE IF NOT EXISTS weather_data (
  id INT AUTO_INCREMENT PRIMARY KEY,
  `date` DATETIME,
  coord_lon DECIMAL(9,6),
  coord_lat DECIMAL(9,6),
  weather_id INT,
  weather_main VARCHAR(20),
  weather_description VARCHAR(100),
  weather_icon VARCHAR(5),
  base VARCHAR(10),
  main_temp DECIMAL(5,2),
  main_feels_like DECIMAL(5,2),
  main_temp_min DECIMAL(5,2),
  main_temp_max DECIMAL(5,2),
  main_pressure SMALLINT,
  main_humidity TINYINT,
  main_sea_level SMALLINT,
  main_grnd_level SMALLINT,
  visibility INT,
  wind_speed DECIMAL(4,2),
  wind_deg SMALLINT,
  wind_gust DECIMAL(4,2),
  clouds_all TINYINT,
  dt INT,
  sys_country CHAR(2),
  sys_sunrise INT,
  sys_sunset INT,
  timezone INT,
  timezone_id INT,
  name VARCHAR(50),
  cod INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

Despues he creado un usuario con estos datos:
usuario123
clave123