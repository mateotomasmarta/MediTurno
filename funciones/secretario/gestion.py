
from db.funciones.archivos_txt import guardar_turnos

def vaciar_turno(matriz_turnos):
    try:
        turno_vaciar = int(input("Ingrese el ID del turno a vaciar: "))
        for i in range(len(matriz_turnos)):
            if matriz_turnos[i][0] == turno_vaciar:
                matriz_turnos[i][3] = None
                matriz_turnos[i][4] = 'disponible'
                matriz_turnos[i][5] = None
                print(f"✅ Turno con ID {turno_vaciar} marcado como disponible.")
                guardar_turnos(matriz_turnos)
                return
        print(f"⚠️ No se encontró un turno con el ID {turno_vaciar}.")
    except ValueError:
        print("⚠️ Debe ingresar un número válido para el ID del turno.")
    except Exception as e:
        print(f"⚠️ Ocurrió un error inesperado: {e}")

def elegir_turno_a_modificar(turno_agendados):
    bandera = True
    while bandera:
        try:
            print("")
            id_turno = int(input("Ingrese el número de la ID del turno que desea modificar: "))
            for i in range(len(turno_agendados)):
                if turno_agendados[i][0] == id_turno:
                    print("")
                    print(f'El turno que desea cambiar es {turno_agendados[i]} ')
                    bandera = False
                    return id_turno
            print("⚠️ No se encontró un turno con esa ID. Intente de nuevo.")
        except ValueError:
            print("⚠️ Debe ingresar un número válido para la ID del turno.")
        except Exception as e:
            print(f"⚠️ Ocurrió un error inesperado: {e}")

def elegir_dia(turnos_disponibles):
    bandera = True
    while bandera:
        try:
            print("")
            dia_id = int(input("Ingrese el número de la ID del turno que desea elegir para la modificación: "))
            for i in range(len(turnos_disponibles)):
                if turnos_disponibles[i][0] == dia_id:
                    print("")
                    bandera = False
                    return dia_id
            print("⚠️ No se encontró un turno con esa ID. Intente de nuevo.")
        except ValueError:
            print("⚠️ Debe ingresar un número válido para la ID del turno.")
        except Exception as e:
            print(f"⚠️ Ocurrió un error inesperado: {e}")

def modifica_turno(turno, dia, matriz_turnos):
    # turno y dia son IDs de turno
    paciente = None
    doctor = None
    estado = None
    for fila in matriz_turnos:
        if fila[0] == turno:
            paciente = fila[3]
            doctor = fila[5]
            estado = fila[4]
            break

    for fila in matriz_turnos:
        if fila[0] == dia:
            fila[3] = paciente
            fila[5] = doctor
            fila[4] = estado

    for fila in matriz_turnos:
        if fila[0] == turno:
            fila[3] = None
            fila[5] = None
            fila[4] = 'disponible'

    guardar_turnos(matriz_turnos)
    print("✅ El turno ha sido modificado correctamente.")