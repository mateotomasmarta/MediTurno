def validar_dni(dni):
    return dni.isdigit()

def validar_dia(dia):
    return dia.lower() in ["lunes", "miércoles", "viernes"]
