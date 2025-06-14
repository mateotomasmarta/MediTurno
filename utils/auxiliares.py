from db.funciones.archivos_json import *
from datos import matriz_medicos
RUTA_PACIENTES = 'db/datos.json'

def obtener_nombre_doctor(id_doctor):
    for doctor in matriz_medicos:
        if doctor[0] == id_doctor:
            return f"{doctor[1]} {doctor[2]}"
    return "Sin asignar"


def obtener_nombre_paciente(id_paciente):
    if id_paciente is not None:
        pacientes = cargar_archivo_pacientes(RUTA_PACIENTES)
        for p in pacientes:
            if p['id'] == id_paciente:
                return f"{p['nombre']} {p['apellido']}"
    return "---"

def buscar_por_dni(dni):
    resultados = []
    pacientes = cargar_archivo_pacientes(RUTA_PACIENTES)
    for p in pacientes:
        if p['dni'].startswith(dni):
            resultados.append(p)
    return resultados

def buscar_por_nombre_o_apellido(filtro):
    resultados = []
    filtro = filtro.lower()
    pacientes = cargar_archivo_pacientes(RUTA_PACIENTES)
    for p in pacientes:
        if filtro in p['nombre'].lower() or filtro in p['apellido'].lower():
            resultados.append(p)
    return resultados

def buscar_paciente(dni, pacientes):
    dni = dni.strip()
    for paciente in pacientes:
        if paciente['dni'] == dni:
            return paciente
    return None

def obtener_id_por_dni(dni_buscado):
    pacientes = cargar_archivo_pacientes(RUTA_PACIENTES)
    resultado = list(filter(lambda p: p['dni'] == dni_buscado, pacientes))
    if resultado:
        return resultado[0]['id']
    else:
        return None

def generar_nuevo_id():
    pacientes = cargar_archivo_pacientes(RUTA_PACIENTES)
    if not pacientes:
        return 1
    return max(paciente['id'] for paciente in pacientes) + 1


#RECURSIVIDAD
def buscar_paciente_por_id(pacientes, id_paciente, index=0):
    if index >= len(pacientes):
        return None 
    if pacientes[index]['id'] == id_paciente:
        return pacientes[index]
    return buscar_paciente_por_id(pacientes, id_paciente, index + 1)  # Llamada recursiva