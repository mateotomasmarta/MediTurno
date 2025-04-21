from datos import matriz_turnos

def turnos_por_dia(dia):
    return [t for t in matriz_turnos if t['dia'].lower() == dia.lower()]

def turnos_disponibles():
    return [t for t in matriz_turnos if t['paciente_id'] is None]

def turnos_ocupados():
    return [t for t in matriz_turnos if t['paciente_id'] is not None]
