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



#-------------------FUNCIONES NUEVAS CON SLICING Y CON LO QUE YA HABIA QUEDADO EN FACTURACION OFICIAL------------

from utils.auxiliares import buscar_paciente_por_id
import re
import json
from db.funciones.archivos_json import cargar_archivo_pacientes, guardar_facturas, cargar_facturas
from db.funciones.archivos_txt import cargar_turnos
from utils.auxiliares import buscar_paciente_por_id


def imprimir_factura_paciente(id_paciente, path_facturas="db/facturacion.json", path_datos="db/datos.json"):
    import json
    import re
    from utils.auxiliares import buscar_paciente_por_id

    with open(path_facturas, "r", encoding="utf-8") as archivo_facturas:
        facturas = json.load(archivo_facturas)
        if facturas and isinstance(facturas[0], list):
            facturas = facturas[0]
    with open(path_datos, "r", encoding="utf-8") as archivo_datos:
        pacientes = json.load(archivo_datos)

    paciente = buscar_paciente_por_id(pacientes, id_paciente)
    if not paciente:
        print("Paciente no encontrado.")
        return

    sub_total = 0
    print("\n" + "=" * 60)
    print(f"{'FACTURAS DE PACIENTE'.center(60)}")
    print("=" * 60)
    print(f"Nombre: {paciente['nombre']} {paciente['apellido']}".ljust(40) + f"DNI: {paciente['dni']}")
    print("-" * 60)

    patron_factura = re.compile(r"(\d{4}-\d{2}-\d{2}|lunes|miércoles|viernes)", re.IGNORECASE)
    facturas_encontradas = False
    for f in facturas:
        if int(f["id_paciente"]) == int(id_paciente):
            facturas_encontradas = True
            sub_total += f["importe"]
            fecha = f["dia"]

            # Nuevo bloque: primero intenta con regex, si falla usa slicing
            coincidencia = patron_factura.search(fecha)
            if coincidencia:
                fecha_formateada = coincidencia.group(1)
            else:
                fecha_formateada = fecha[:10]  # muestra por ejemplo "2025-07-21"

            print(f"| ID Factura: {str(f['id_factura']).ljust(6)} | Fecha: {fecha_formateada.ljust(10)} | Hora: {f['hora'].ljust(5)} | Importe: ${str(f['importe']).ljust(8)}|")
            print("-" * 60)

    if not facturas_encontradas:
        print("No se encontraron facturas para este paciente.".center(60))

    print("=" * 60)

def imprimir_todas_las_facturas_ordenadas(ruta_facturas="db/facturacion.json"):
    facturas = cargar_facturas(ruta_facturas)
    # Orden personalizado de días
    orden_dias = {"lunes": 1, "miércoles": 2, "viernes": 3}
    # Ordenar por día y luego por hora
    facturas_ordenadas = sorted(
        facturas,
        key=lambda f: (
            orden_dias.get(f.get("dia", "").lower(), 99),
            f.get("hora", "")
        )
    )

    print("\n" + "="*70)
    print("FACTURAS ORDENADAS POR DÍA Y HORARIO".center(70))
    print("="*70)
    for f in facturas_ordenadas:
        print(f"| Día: {str(f.get('dia', '---')).capitalize()[:10]:<10} | Hora: {str(f.get('hora', '---'))[:5]:<5} | ID Factura: {str(f.get('id_factura', '')):<4} | Paciente: {str(f.get('id_paciente', '')):<4} | Importe: ${str(f.get('importe', '')):<8}|")
        print("-"*70)
    print("="*70)
    
def imprimir_facturas_por_dni(dni, ruta_pacientes="db/datos.json", ruta_facturas="db/facturacion.json"):
    pacientes = cargar_archivo_pacientes(ruta_pacientes)
    facturas = cargar_facturas(ruta_facturas)
    paciente = buscar_paciente(dni, pacientes)

    if not paciente:
        print(f"No se encontró paciente con DNI {dni}.")
        return

    facturas_cliente = [f for f in facturas if int(f.get("id_paciente", -1)) == int(paciente["id"])]

    if not facturas_cliente:
        print(f"No hay facturas para el paciente {paciente.get('nombre', '')} {paciente.get('apellido', '')} (DNI: {dni})")
        return

    print("\n" + "="*60)
    print(f"FACTURAS DE: {paciente.get('nombre', '').upper()} {paciente.get('apellido', '').upper()} (DNI: {dni})".center(60))
    print("="*60)
    for f in facturas_cliente:
        dia = f.get("dia", "---")
        hora = f.get("hora", "---")
        print(f"| ID Factura: {str(f.get('id_factura', '')).ljust(6)} | Día: {str(dia)[:10].ljust(10)} | Hora: {str(hora)[:5].ljust(5)} | Importe: ${str(f['importe']).ljust(8)}|")
        print("-"*60)
    print(f"{'TOTAL':>50}: ${sum(f['importe'] for f in facturas_cliente)}")
    print("="*60)

def cierre_total_con_detalle(ruta):

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            facturas = json.load(archivo)
            # Si hay lista de listas, aplanar para manejarlos mejor
            if facturas and isinstance(facturas[0], list): #verifica si es una lista de listas
                facturas = facturas[0] #esto me sirve para tomar la primera lista de la lista de listas
            total_general = 0
            totales_por_dia = {}
            for factura in facturas:
                total_general += factura["importe"]
                dia = factura["dia"]
                totales_por_dia[dia] = totales_por_dia.get(dia, 0) + factura["importe"] #.get() devuelve el valor de la clave si existe, o 0 si no existe

            print("\n" + "="*50)
            print(f"{'CIERRE DE CAJA':^50}")
            print("="*50)
            for dia, total in totales_por_dia.items():
                print(f"Total generado el día {dia.capitalize():<10}: ${total}")
            print("-"*50)
            print(f"{'TOTAL GENERAL':<30}: ${total_general}")
            print("="*50)
            return total_general, totales_por_dia
    except Exception as e:
        print(f"No se puede abrir el archivo: {e}")
        return 0, {}


