from utils.validaciones import validar_edad, validar_dni
from utils.auxiliares import generar_nuevo_id
from datos import matriz_pacientes

def tomar_nombre():
    bandera = True
    while bandera == True:
        entrada = input("Ingresá solo tu primer nombre y primer apellido: ").strip()
        partes = entrada.split()

        if len(partes) != 2:
            print("⚠️ Tenés que ingresar un solo *nombre y apellido*, nada más.")
        else:
            nombre, apellido = partes

            if not (nombre.isalpha() and apellido.isalpha()):
                print("⚠️ El nombre y apellido solo deben tener letras.")
            else:
                nombre_formateado = nombre.capitalize()
                apellido_formateado = apellido.capitalize()
                bandera = False
                return nombre_formateado, apellido_formateado 

def lista_registro():
    """lista_nuevo: [id, dni, nombre, apellido, edad]"""
    lista_nuevo = []
    print("=" * 70)
    print("BIENVENIDO! Te pediremos tus datos para registrarte como paciente")
    print("=" * 70)

    
    dni = validar_dni()  
    lista_nuevo.append(dni) 
    nombre, apellido = tomar_nombre()  
    lista_nuevo.append(nombre)  
    lista_nuevo.append(apellido)  

    edad = validar_edad() 
    lista_nuevo.append(edad)  

    id = generar_nuevo_id(matriz_pacientes)  
    lista_nuevo.insert(0, id)  
    return lista_nuevo  
