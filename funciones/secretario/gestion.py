

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





    

        




    
    
   
        

    





