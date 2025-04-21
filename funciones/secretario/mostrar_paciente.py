from datos import matriz_turnos

def mostrar_datos_paciente(paciente):
    print(f"Nombre: {paciente['nombre']}")
    print(f"Apellido: {paciente['apellido']}")
    print(f"DNI: {paciente['dni']}")
    print(f"Edad: {paciente['edad']}")
    mostrar_turnos_paciente(paciente['id'])

def mostrar_turnos_paciente(paciente_id):
    turnos = [t for t in matriz_turnos if t['paciente_id'] == paciente_id]
    if not turnos:
        print("No tiene turnos asignados.")
    else:
        print("Turnos asignados:")
        for t in turnos:
            print("-", t['dia'], t['hora'])
