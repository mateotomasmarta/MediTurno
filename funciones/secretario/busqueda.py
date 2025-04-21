from datos import matriz_pacientes

def buscar_por_dni(dni):
    return [p for p in matriz_pacientes if p['dni'] == dni]

def buscar_por_apellido(apellido):
    return [p for p in matriz_pacientes if p['apellido'].lower() == apellido.lower()]

def buscar_por_dni_y_apellido(dni, apellido):
    return [p for p in matriz_pacientes if p['dni'] == dni and p['apellido'].lower() == apellido.lower()]


