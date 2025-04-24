from datos import matriz_turnos

def muestra_turnos_ocupados():
   turno_agendados= list(dato for dato in matriz_turnos if dato[4]=='ocupado')
   print("")
   print(f'Los turnos agendados son:')
   for fila in turno_agendados:
      print(fila)
      print(" ")
    #muestra los turnos no disponibles( )
   return turno_agendados

def muestra_turnos_disponibes():
    turnos_disponibles=list(dato for dato in matriz_turnos if dato[4]=='disponible')
    print("")
    print(f'Los turnos disponibles son:')
    for fila in turnos_disponibles:
      print(fila)
      print("")
    
    return turnos_disponibles

def elegir_turno_a_modificar(turno_agendados):
   
    
    bandera=True

    while bandera:
     bandera=True
     print("")
     id_turno=int(input("Ingrese el numero de la id del turno que desea modificar "))

     for i in range(len(turno_agendados)) :
        if  turno_agendados[i][0]==id_turno:
           print("")
           print(f'El turno que desea cambiar es {turno_agendados[i]} ')
           bandera=False
        elif bandera==True and i == len(turno_agendados)-1:
           print("Intente de nuevo")
      
    return id_turno

   
    #pide que eliga el turno del paciente que desea modificar mediante ingresando el numero de turno (id).( variable que luego mando a funcion modificar turno)


def modificar_turno():
    pass

def main():
    
    turnos_a=muestra_turnos_ocupados()
    
    turno_a_modificar=elegir_turno_a_modificar(turnos_a)
main()
