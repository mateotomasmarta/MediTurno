import json
from utils.auxiliares import buscar_paciente_por_id
import re
from utils.auxiliares import buscar_paciente_por_id
# Cargar facturas desde el archivo JSON

def cargar_facturas():
    try:
        with open("facturacion.json", "r", encoding="UTF-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

# Guardar facturas en el archivo JSON

def guardar_facturas(facturas):
    with open("facturacion.json", "w", encoding="UTF-8") as archivo:
        json.dump(facturas, archivo, ensure_ascii=False, indent=4)

# Crear facturas nuevas a partir del archivo turnos.txt

def generar_facturas_desde_turnos():
    facturas = cargar_facturas()
    turnos_ocupados = []

    with open("turnos.txt", "r", encoding="utf-8") as archivo_turnos:
        for linea in archivo_turnos:
            partes = linea.strip().split(";")
            if len(partes) < 6:
                continue
            id_turno = int(partes[0])
            dia = partes[1]
            hora = partes[2]
            id_paciente = int(partes[3])
            estado = partes[4]
            id_doctor = partes[5]

            if estado == "ocupado":
                turnos_ocupados.append({
                    "id_turno": id_turno,
                    "dia": dia,
                    "hora": hora,
                    "id_paciente": id_paciente
                })

    for turno in turnos_ocupados:
        if any(f["id_turno"] == turno["id_turno"] for f in facturas):
            continue

        nuevo_id = max((f["id_factura"] for f in facturas), default=0) + 1
        nueva_factura = {
            "id_factura": nuevo_id,
            "id_paciente": turno["id_paciente"],
            "id_turno": turno["id_turno"],
            "dia": turno["dia"],
            "hora": turno["hora"],
            "importe": 25000
        }
        facturas.append(nueva_factura)

    guardar_facturas(facturas)

# Generar subfacturas con nombre y apellido desde el JSON

def generar_subfacturas():
    with open("datos.json", "r", encoding="utf-8") as archivo_datos:
        pacientes = json.load(archivo_datos)

    facturas = cargar_facturas()
    subfacturas = []

    for factura in facturas:
        paciente = buscar_paciente_por_id(pacientes, factura["id_paciente"])
        if paciente:
            subfactura = {
                "id_factura": factura["id_factura"],
                "nombre": paciente["nombre"],
                "apellido": paciente["apellido"],
                "dni": paciente["dni"],
                "dia": factura["dia"],
                "hora": factura["hora"],
                "importe": factura["importe"]
            }
            subfacturas.append(subfactura)

    return subfacturas



# ------------------------ Funciones para manejar facturación ------------------------

def cargar_facturas(path="facturacion.json"):
    try:
        with open(path, "r", encoding="UTF-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_facturas(facturas, path="facturacion.json"):
    with open(path, "w", encoding="UTF-8") as archivo:
        json.dump(facturas, archivo, ensure_ascii=False, indent=4)

def generar_facturas_desde_turnos(path_turnos="turnos.txt", path_facturas="facturacion.json"):
    facturas = cargar_facturas(path_facturas)
    turnos_ocupados = []

    with open(path_turnos, "r", encoding="utf-8") as archivo_turnos:
        for linea in archivo_turnos:
            partes = linea.strip().split(";")
            if len(partes) < 6:
                continue

            id_turno = int(partes[0])
            dia = partes[1]
            hora = partes[2]
            id_paciente = int(partes[3])
            estado = partes[4]
            id_doctor = partes[5]

            if estado == "ocupado":
                turnos_ocupados.append({
                    "id_turno": id_turno,
                    "dia": dia,
                    "hora": hora,
                    "id_paciente": id_paciente
                })

    for turno in turnos_ocupados:
        if any(f["id_turno"] == turno["id_turno"] for f in facturas):
            continue

        nuevo_id = max((f["id_factura"] for f in facturas), default=0) + 1

        nueva_factura = {
            "id_factura": nuevo_id,
            "id_paciente": turno["id_paciente"],
            "id_turno": turno["id_turno"],
            "dia": turno["dia"],
            "hora": turno["hora"],
            "importe": 25000
        }

        facturas.append(nueva_factura)

    guardar_facturas(facturas, path_facturas)


def generar_subfacturas(path_datos="datos.json", path_facturas="facturacion.json"):
    facturas = cargar_facturas(path_facturas)
    with open(path_datos, "r", encoding="utf-8") as archivo_datos:
        pacientes = json.load(archivo_datos)

    subfacturas = []
    for factura in facturas:
        paciente = buscar_paciente_por_id(pacientes, factura["id_paciente"])
        if paciente:
            subfactura = {
                "id_factura": factura["id_factura"],
                "nombre": paciente["nombre"],
                "apellido": paciente["apellido"],
                "dni": paciente["dni"],
                "dia": factura["dia"],
                "hora": factura["hora"],
                "importe": factura["importe"]
            }
            subfacturas.append(subfactura)

    return subfacturas

# ------------------------ Funciones adicionales ------------------------

def secretario_facturas_min(facturas):
    ''' Ordena recursivamente las facturas de menor a mayor por DNI. '''
    if len(facturas) <= 1:
        return facturas

    paciente_min = min(facturas, key=lambda f: f["id_paciente"])
    facturas.remove(paciente_min)
    return [paciente_min] + secretariofacturasmin(facturas)


def imprimir_factura_paciente(id_paciente, path_facturas="facturacion.json", path_datos="datos.json"):
    facturas = cargar_facturas(path_facturas)
    with open(path_datos, "r", encoding="utf-8") as archivo_datos:
        pacientes = json.load(archivo_datos)

    paciente = buscar_paciente_por_id(pacientes, id_paciente)
    if not paciente:
        print("Paciente no encontrado.")
        return

    sub_total = 0
    print(f"\n--- Facturas del paciente {paciente['nombre']} {paciente['apellido']} (DNI: {paciente['dni']}) ---")

    patron_factura = re.compile(r"(\\d{4}-\\d{2}-\\d{2})")  # ejemplo simple con fecha

    for f in facturas:
        if f["id_paciente"] == id_paciente:
            sub_total += f["importe"]
            fecha = f["dia"]
            coincidencia = patron_factura.search(fecha)
            fecha_formateada = coincidencia.group(1) if coincidencia else fecha

            print("\n--- Factura ---")
            print(f"ID Factura: {f['id_factura']}")
            print(f"Fecha: {fecha_formateada}")
            print(f"Hora: {f['hora']}")
            print(f"Importe: ${f['importe']}")

    print(f"\nSubtotal a pagar: ${sub_total}")

