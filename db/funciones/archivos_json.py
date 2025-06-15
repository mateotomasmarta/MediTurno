import json
RUTA_PACIENTES = "db/datos.json"
RUTA_FACTURAS = 'db/facturacion.json'

def leer_archivo_pacientes(RUTA):
    with open(RUTA, 'r', encoding='utf-8') as archivo:
        return archivo.read()
    

        
def cargar_archivo_pacientes(RUTA):
    with open(RUTA, 'r', encoding='utf-8') as f:
        datos = json.load(f)
        return datos

def guardar_archivo_pacientes(pacientes):
    with open(RUTA_PACIENTES, 'w', encoding='utf-8') as f:
        json.dump(pacientes, f, ensure_ascii=False, indent=4)


def cargar_facturas(path="facturacion.json"):
    try:
        with open(path, "r", encoding="UTF-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_facturas(facturas, path="facturacion.json"):
    with open(path, "w", encoding="UTF-8") as archivo:
        json.dump(facturas, archivo, ensure_ascii=False, indent=4)


def cargar_archivo_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    contenido = leer_archivo_pacientes(RUTA_PACIENTES)
    print(contenido)
