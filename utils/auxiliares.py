from datos import *
def obtener_nombre_doctor(id_doctor):
    """Devuelve el nombre del doctor dado su ID."""
    if id_doctor is not None:
        for d in matriz_medicos:
            if d[0] == id_doctor:
                return d[1]
    return "---"

def obtener_nombre_paciente(id_paciente):
    """Devuelve el nombre completo del paciente dado su ID."""
    if id_paciente is not None:
        for p in matriz_pacientes:
            if p['id'] == id_paciente:
                return f"{p['nombre']} {p['apellido']}"
    return "---"

def buscar_por_dni(dni):
    resultados = []
    for p in matriz_pacientes:
        if p['dni'].startswith(dni):
            resultados.append(p)
    return resultados

def buscar_por_nombre_o_apellido(filtro):
    resultados = []
    filtro = filtro.lower()
    for p in matriz_pacientes:
        if filtro in p['nombre'].lower() or filtro in p['apellido'].lower():
            resultados.append(p)
    return resultados



#====================================================
#PACIENTES
#====================================================
def buscar_paciente(dni, lista_pacientes):
    dni = dni.strip() 
    for paciente in lista_pacientes:
        if paciente['dni'] == dni:
            return paciente 
    return None 

def obtener_id_por_dni(mpacientes, dni_buscado):
    resultado = list(filter(lambda p: p['dni'] == dni_buscado, mpacientes))
    if resultado:
        return resultado[0]['id']
    else:
        return None


def generar_nuevo_id(matriz_pacientes):
    """Genera un nuevo ID para pacientes basado en el máximo ID existente"""
    if not matriz_pacientes: 
        return 1
    return max(paciente['id'] for paciente in matriz_pacientes) + 1