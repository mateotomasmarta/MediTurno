import re 
import from datos matriz_pacientes, matriz_turnos

#funcion validar dni 
def validar_dni(dni):
    patron = r"^\d{7,8}$"
    coincidencia = re.match(patron, dni)
    if coincidencia is not None:
        return True
    else:
        return False

def buscar_id_paciente (matriz_pacientes, dni):
    for paciente in matriz_pacientes:
        if paciente['dni'] == dni:
            return paciente['id']
    return None

def chequear_turno (matriz_turnos, dia, hora, dni):
    for fila in matriz_turnos:
        if fila[1].lower() == dia and fila[2]== hora and fila[3]==dni and fila[4]== 'ocupado':
          existencia= 1
        elif fila[1].lower() == dia and fila[2]== hora and fila[3]==dni and fila[4]== 'disponible':
            existencia = 2
        else:
            existencia= 0
    return existencia   

def buscar_id_turno(documento):
     for fila in matriz_turnos:
         if fila[1].lower() == dia and fila[2]== hora and fila[3]==dni and fila[4]== 'ocupado
             id_turno= fila[0]
    return id_turno

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





    

        




    
    
   
        

    





