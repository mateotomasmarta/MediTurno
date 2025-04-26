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

def buscar_valor_por_clave(matriz,clave,clavebuscada):
    for diccionario in matriz:
        if diccionario[clave]==clavebuscada:
            return diccionario
