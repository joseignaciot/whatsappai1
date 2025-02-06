import time
import requests

# Usamos el nombre de host "nocodb" para acceder al contenedor NocoDB a través de la red interna de Docker
NOCODB_URL = "http://nocodb:8080"
PROJECT_NAME = "HistorialChat"
TABLE_NAME = "conversaciones"

def wait_for_nocodb():
    print("Esperando que NocoDB esté disponible...")
    for i in range(30):
        try:
            res = requests.get(f"{NOCODB_URL}/api/v1/db")
            if res.status_code == 200:
                print("NocoDB está listo.")
                return True
        except Exception as e:
            pass
        time.sleep(5)
    print("NocoDB no está disponible después de 150 segundos.")
    return False

def create_project():
    url = f"{NOCODB_URL}/api/v1/db/projects"
    payload = {
        "name": PROJECT_NAME,
        "driver": "sqlite",  # O el driver que prefieras
        "dbConfig": {"filename": "nocodb_data.db"}
    }
    headers = {"Content-Type": "application/json"}
    print("Creando proyecto...")
    res = requests.post(url, json=payload, headers=headers)
    if res.status_code in [200, 201]:
        project = res.json()
        print("Proyecto creado:", project)
        return project.get("id")
    else:
        print("Error al crear proyecto:", res.text)
        return None

def create_table(project_id):
    url = f"{NOCODB_URL}/api/v1/db/data/{project_id}/tables"
    payload = {
        "name": TABLE_NAME,
        "columns": [
            {"name": "user_id", "type": "Text"},
            {"name": "timestamp", "type": "DateTime"},
            {"name": "mensaje", "type": "LongText"},
            {"name": "respuesta", "type": "LongText"},
            {"name": "contexto", "type": "LongText"}
        ]
    }
    headers = {"Content-Type": "application/json"}
    print("Creando tabla de conversaciones...")
    res = requests.post(url, json=payload, headers=headers)
    if res.status_code in [200, 201]:
        table = res.json()
        print("Tabla creada:", table)
    else:
        print("Error al crear la tabla:", res.text)

if __name__ == "__main__":
    if wait_for_nocodb():
        project_id = create_project()
        if project_id:
            create_table(project_id)
    else:
        print("No se pudo conectar a NocoDB. Saliendo.")
