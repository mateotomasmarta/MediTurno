from datos import matriz_turnos
from utils.validaciones import validar_turno_disponible

def obtener_turnos_paciente(matriz_turnos, id_paciente):
    # Filtramos la matriz con lambda para quedarnos con los turnos de ese paciente
    turnos_filtrados = list(filter(lambda t: t[3] == id_paciente, matriz_turnos))
    #la variable turnos_filtrados ahoracontiene una lista, basicamente la fila del pacielte encontrado
    if not turnos_filtrados:
        return "No tiene aún turnos asignados."
    # Creamos una lista de tuplas con (día, hora)
    lista_tuplas = list(map(lambda t: (t[1], t[2]), turnos_filtrados))
    return lista_tuplas



def cargar_turno_paciente(id_paciente,edad_paciente):
    # Pedir al paciente el día y hora de su preferencia
    print("Por favor, selecciona un día y una hora para tu turno.")
    dia_turno = input("Día (lunes, miércoles, viernes): ").strip().lower()
    hora_turno = input("Hora (ejemplo: 08:00, 09:00, 16:00): ").strip()
    # Validamos si el turno está disponible (utilizamos la función de búsqueda)
    turno_encontrado = validar_turno_disponible(dia_turno, hora_turno)

    if turno_encontrado:

        # Usamos un bucle 'for i in range' para recorrer la matriz de turnos
        for i in range(len(matriz_turnos)):
            # Buscamos el turno que coincida con la fecha y la hora seleccionadas
            if matriz_turnos[i][1] == dia_turno and matriz_turnos[i][2] == hora_turno:
                # Verificamos que el campo del paciente esté vacío (es decir, aún no tiene asignado un paciente)
                if matriz_turnos[i][3] is None:
                    # Asignamos el turno al paciente
                    matriz_turnos[i][3] = id_paciente  # Asignamos el ID del paciente al turno
                    matriz_turnos[i][4] = 'ocupado'   # Cambiamos el estado a ocupado
                    if edad_paciente <= 18:
                        matriz_turnos[i][5] = 2
                    else:
                        matriz_turnos[i][5] = 1
                    print(f"¡Turno asignado con éxito! Tu turno es el {dia_turno} a las {hora_turno}.")
                    break

def mostrar_turnosdipo_paciente():
    print("\n" + "═" * 70)
    print(f"📊 TURNOS DISPONIBLES")
    print("═" * 70)
    print("\nID  DÍA       HORA   ESTADO       ")
    print("-" * 70)

    for turno in matriz_turnos:
        id_turno, dia, hora, id_paciente, estado, doctor_turno = turno
        if estado == 'disponible' :

            # Mostrar turno disponible
            print(f"{(id_turno):<4} {dia:<9} {hora:<6} 🟢 DISPONIBLE ")

    print("\n" + "═" * 70)