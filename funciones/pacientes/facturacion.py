
from utils.auxiliares import buscar_paciente_por_id
import re
import json
from db.funciones.archivos_json import cargar_facturas, guardar_facturas

def generar_facturas_desde_turnos(path_turnos="db/turnos.txt", path_facturas="db/facturacion.json"):
    facturas = cargar_facturas(path_facturas)
    turnos_ocupados = []

    patron_split = re.compile(r"[;\t]+|\s{2,}")  # acepta ;, tabulaciones, o ≥2 espacios

    try:
        with open(path_turnos, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = [p for p in patron_split.split(linea.strip()) if p]
                if len(partes) < 6:
                    continue

                id_turno = partes[0]
                dia = partes[1]
                hora = partes[2]
                id_paciente = partes[3]
                estado = partes[4].lower().strip()

                # ignorar turnos disponibles o con campos vacíos
                if estado != "ocupado":
                    continue
                if id_paciente.lower() == "none":
                    continue

                try:
                    turno_obj = {
                        "id_turno": int(id_turno),
                        "dia": dia,
                        "hora": hora,
                        "id_paciente": int(id_paciente)
                    }
                    turnos_ocupados.append(turno_obj)
                except ValueError:
                    continue  # ignorar si id no es numérico

    except FileNotFoundError:
        print("❌ No se encontró el archivo de turnos.")
        return

    nuevas = 0
    for turno in turnos_ocupados:
        if any(f["id_turno"] == turno["id_turno"] for f in facturas):
            continue

        nuevo_id = max((f["id_factura"] for f in facturas), default=0) + 1

        facturas.append({
            "id_factura": nuevo_id,
            "id_paciente": turno["id_paciente"],
            "id_turno": turno["id_turno"],
            "dia": turno["dia"],
            "hora": turno["hora"],
            "importe": 25000
        })
        nuevas += 1

    guardar_facturas(facturas, path_facturas)
    print(f"✅ {nuevas} factura(s) generadas y guardadas en '{path_facturas}'.")
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
#APLICAMOS RECURSIVIDAD
def secretario_facturas_min(facturas): 
    ''' Ordena recursivamente las facturas de menor a mayor por DNI. '''
    if len(facturas) <= 1:
        return facturas

    paciente_min = min(facturas, key=lambda f: f["id_paciente"])
    facturas.remove(paciente_min)
    return [paciente_min] + secretario_facturas_min(facturas) 

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
            coincidencia = patron_factura.search(fecha)
            fecha_formateada = coincidencia.group(1) if coincidencia else fecha

            print(f"| ID Factura: {str(f['id_factura']).ljust(6)} | Fecha: {fecha_formateada.ljust(10)} | Hora: {f['hora'].ljust(5)} | Importe: ${str(f['importe']).ljust(8)}|")
            print("-" * 60)

    if not facturas_encontradas:
        print("No se encontraron facturas para este paciente.".center(60))

    print("=" * 60)