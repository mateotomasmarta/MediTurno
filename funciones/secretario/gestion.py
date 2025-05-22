def vaciar_turno(matriz):
    try:
        turno_vaciar = int(input("Ingrese el ID del turno a vaciar: "))
        for i in range(len(matriz)):
            if matriz[i][0] == turno_vaciar:  
                matriz[i][3] = None  
                matriz[i][4] = 'disponible'  
                matriz[i][5] = None  
                print(f"✅ Turno con ID {turno_vaciar} marcado como disponible.")
                return
        print(f"⚠️ No se encontró un turno con el ID {turno_vaciar}.")
    except ValueError:
        print("⚠️ Debe ingresar un número válido para el ID del turno.")
    except Exception as e:
        print(f"⚠️ Ocurrió un error inesperado: {e}")
def vaciar_turno(matriz):

    turno_vaciar = int(input("Ingrese el ID del turno a vaciar: "))
    for i in range(len(matriz)):
        if matriz[i][0] == turno_vaciar:  
            matriz[i][3] = None  
            matriz[i][4] = 'disponible'  
            matriz[i][5] = None  
            print(f"✅ Turno con ID {turno_vaciar} marcado como disponible.")
            return
    print(f"⚠️ No se encontró un turno con el ID {turno_vaciar}.")
            
    
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

def modifica_turno(turno, dia, matriz): 
    
    for fila in matriz:
        if fila[0] == turno:
            paciente = fila[3]
            doctor = fila[5]
            estado = fila[4]
    
    matriz[dia-1][3] = paciente
    matriz[dia-1][5] = doctor
    matriz[dia-1][4] = estado

    matriz[turno-1][3] = None
    matriz[turno-1][5] = None
    matriz[turno-1][4] = 'disponible'

    print("✅ El turno ha sido modificado correctamente.")



