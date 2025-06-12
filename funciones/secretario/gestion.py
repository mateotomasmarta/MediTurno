<<<<<<< HEAD
<<<<<<< HEAD


def vaciar_turno(matriz):
    turno_vaciar=int(input("ingrese el id del turno a eliminar:"))
    for i in range (len(matriz)): 
        if matriz[i][0]== turno_vaciar: 
            matriz[i][4] = None
            matriz[i][5] ='disponible'
            matriz[i][6]= None
            
    
def eliminar_turno(matriz_t):
    turno_eliminar = int(input("ingrese el id del turno a eliminar"))
    variable= 1 
    while variable == 1:
        for i in range (len(matriz_t)):
            if matriz [i][0] == turno_eliminar:
                del matriz[i]
                variable= 0





    

        




    
    
   
        

    


=======
def vaciar_turno(matriz):
=======

from db.funciones.archivos_txt import guardar_turnos

def vaciar_turno(matriz_turnos):
>>>>>>> origin/main
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
<<<<<<< HEAD
    
    matriz[dia-1][3] = paciente
    matriz[dia-1][5] = doctor
    matriz[dia-1][4] = estado

    matriz[turno-1][3] = None
    matriz[turno-1][5] = None
    matriz[turno-1][4] = 'disponible'

    print("✅ El turno ha sido modificado correctamente.")
>>>>>>> origin/main
=======
            break
>>>>>>> origin/main

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