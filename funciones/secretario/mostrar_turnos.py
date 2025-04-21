def mostrar_turnos(turnos):
    if not turnos:
        print("No se encontraron turnos.")
        return

    for turno in turnos:
        estado = "Disponible" if turno['paciente_id'] is None else "Ocupado"
        print(f"ID: {turno['id']} | Día: {turno['dia']} | Hora: {turno['hora']} | Estado: {estado}")
