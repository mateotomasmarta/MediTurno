import json

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








