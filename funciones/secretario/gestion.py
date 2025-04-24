import re 
import from datos matriz_pacientes, matriz_datos

#funcion validar dni 
def validar_dni(dni):
    patron = r"^\d{7,8}$"
    coincidencia = re.match(patron, dni)
    if coincidencia is not None:
        return True
    else:
        return False



def eliminar_turno(matriz_turnos, matriz_pacientes):
    print("=== ELIMINAR UN TURNO ===")
    entrada = input("Ingrese los datos del turno a eliminar (DNI, día, hora):\n> ")
    partes = entrada.strip().split(',')
    dni, dia, hora = [p.strip().lower() for p in partes]


#chequear que los datos sean correctos en formato

