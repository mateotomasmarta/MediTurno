import json
from utils.auxiliares import buscar_paciente_por_id

try:
    with open("facturacion.json", "r", encoding="UTF-8") as archivo: #leemos el archivo
        facturas = json.load(archivo) #pasamos a python el formato json y lo metemos en una variable
except FileNotFoundError:
    facturas = [] #si no existe creamos una lista vacia


turnos_ocupados = []

with open("matriz.txt", "r", encoding="utf-8") as archivo_turnos: #leemos el archivo txt
    for linea in archivo_turnos: #por cada turno  tenes una linea del archivo
        partes = linea.strip().split(";") #con strip te sacas los espacios y saltos de linea y con split separas en varias partes cada linea
#la corta en pedazos cada vez que ve un ;
        if len(partes) < 6: #si tiene menos de 6 partes es por que algo esta mal
            continue
#split automaticamente te devuelve una lista con esas partes
        id_turno = int(partes[0]) #con el int volves un nro el dato que esta en texto
        dia = partes[1]
        hora = partes [2]
        id_paciente = int(partes[3])
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
            #con esto ya chequeaste que la nueva factura que se cree no sea repetida con un turno viejo

        nuevo_id = max((f["id_factura"]for f in facturas), default=0) + 1

        nueva_factura = { 
            "id_factura": nuevo_id,
            "id_paciente": turno["id_paciente"], #pongo turno por que es mi indice del iterable en el que sigo estando, 
            #entonces por cada turno que cumpla con la condicion de ser nuevo y estar ocupado, se va cargando con su data
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

for factura in facturas: #queds guardada en memoria la variable facturas mientras siga ejecutandose
    paciente = buscar_paciente_por_id(pacientes, factura["id_paciente"]) #te retorna el diccionario completo de ese paciente
    if paciente:
        subfactura = {
            "id_factura": factura["id_factura"], #factura por que es el indice de mi iterable
            "nombre": paciente["nombre"], #saca la clave del diccionario que encontraste con el mismo id
            "apellido": paciente["apellido"],
            "dni": paciente["dni"],
            "dia": factura["dia"],
            "hora": factura["hora"],
            "importe": factura["importe"]
        }
        subfacturas.append(subfactura)


####para cuando se agregue al menu:

#METER SLICING SI O SI EN EL PRINT DE LA SUBFACTURA
#queda pendiente: meter el print de la subfactura para pacientes en la marcha del menu
#meter print de facturas y subfacturas en especifico o en general para la secretaria
respuesta = input("¿Desea imprimir la sub-factura detallada? (s/n): ").lower()

if respuesta == "s":
    for sf in subfacturas:
        print("\n--- Sub-factura ---")
        print(f"Factura Nº: {sf['id_factura']}")
        print(f"Paciente: {sf['nombre']} {sf['apellido']}")
        print(f"DNI: {sf['dni']}")
        print(f"Fecha: {sf['dia']} - Hora: {sf['hora']}")
        print(f"Importe: ${sf['importe']}")





