import json
from utils.auxiliares import buscar_paciente_por_id

try:
    with open("facturacion.json", "r", encoding="UTF-8") as archivo:
        facturas = json.load(archivo)
except FileNotFoundError:
    facturas = []


turnos_ocupados = []

with open("matriz.txt", "r", encoding="utf-8") as archivo_turnos:
    for linea in archivo_turnos:
        partes = linea.strip().split(";")
        if len(partes) < 6:
            continue

        id_turno = int(partes[0])
        dia = partes[1]
        hora = partes [2]
        id_paciente = partes [3]
        estado = partes [4]
        id_doctor = partes [5]

        if estado == "ocupado":
            turnos_ocupados.append({
                "id_turno": id_turno,
                "dia":dia,
                "hora":hora,
                "id_paciente":int(id_paciente)
            })

    for turno in turnos_ocupados:
        factura_existente = False
        for f in facturas:
            if f["id_turno"] == turno["id_turno"]:
                factura_existente=True
                break
        if factura_existente:
            continue

        nuevo_id = max((f["id_factura"]for f in facturas), default=0) + 1

        nueva_factura = { 
            "id_factura": nuevo_id,
            "id_paciente": turno["id_paciente"],
            "id_turno": turno["id_turno"],
            "dia": turno["dia"],
            "hora": turno["hora"],
            "importe": 25000
        }

        facturas.append(nueva_factura)



with open("facturacion.json", "w", encoding="UTF-8") as archivo:
    json.dump(facturas, archivo, ensure_ascii=False, indent=4)


#subfactura detallada para pacientes

with open("datos.json", "r", encoding="utf-8") as archivo_datos:
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


####para cuando se agregue al menu:

#METER SLICING SI O SI EN EL PRINT DE LA SUBFACTURA

respuesta = input("¿Desea imprimir la sub-factura detallada? (s/n): ").lower()

if respuesta == "s":
    for sf in subfacturas:
        print("\n--- Sub-factura ---")
        print(f"Factura Nº: {sf['id_factura']}")
        print(f"Paciente: {sf['nombre']} {sf['apellido']}")
        print(f"DNI: {sf['dni']}")
        print(f"Fecha: {sf['dia']} - Hora: {sf['hora']}")
        print(f"Importe: ${sf['importe']}")





