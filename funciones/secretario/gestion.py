from datos import matriz_turnos

def muestra_turnos_ocupados():
   turno_agendados= list(dato for dato in matriz_turnos if dato[4]=='ocupado')
   print("")
   print(f'Los turnos agendados son:')
   for fila in turno_agendados:
      print(fila)
      print(" ")
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

def elegir_dia (turnos_disponibles):
   
   bandera=True
   while bandera:
     bandera=True
     print("")
     dia_id=int(input("Ingrese el numero de la id del turno que desea elegir para la modificacion "))

     for i in range(len(turnos_disponibles)) :

        if  turnos_disponibles[i][0]==dia_id:
           print("")
           print(f'El turno que desea cambiar es {turnos_disponibles[i]} ')
           bandera=False
        elif bandera==True and i == len(turnos_disponibles)-1:
           print("Intente de nuevo")
       
   return dia_id

def modifica_turno (turno,dia,matriz): 
    
   print(matriz)
   print("")

   for fila in matriz:
      if fila[0]== turno:
         paciente= fila[3]
         doctor= fila[5]
         estado=fila[4]
    
   matriz[dia-1][3]=paciente
  
   matriz[dia-1][5]=doctor
   
   matriz[dia-1][4]=estado
  

   matriz[turno-1][3]=None
   
   matriz[turno-1][5]=None
  
   matriz[turno-1][4]='disponible'
   

   print (matriz)


def main():
    
    turnos_a=muestra_turnos_ocupados()
    
    turno_a_modificar=elegir_turno_a_modificar(turnos_a)

    turnos_d=muestra_turnos_disponibes()
    dia=elegir_dia(turnos_d)
    modifica_turno(turno_a_modificar,dia,matriz_turnos)
main()
