from utils.validaciones import validar_edad, validar_dni
from utils.auxiliares import generar_nuevo_id
from datos import matriz_pacientes

def tomar_nombre():
    bandera = True
    while bandera == True:
        # Cargás como variable el nombre y apellido evitando espacios en blanco
        entrada = input("Ingresá solo tu primer nombre y primer apellido: ").strip()
        # Separás en palabras la cadena para contar cuántas se ingresaron
        partes = entrada.split()

        # Validás que haya exactamente 2 palabras a partir del split
        if len(partes) != 2:
            print("⚠️ Tenés que ingresar un solo *nombre y apellido*, nada más.")
        else:
            nombre, apellido = partes

            # Validás que solo tenga letras
            if not (nombre.isalpha() and apellido.isalpha()):
                print("⚠️ El nombre y apellido solo deben tener letras.")
            else:
                # Formateás a Capital Inicial
                nombre_formateado = nombre.capitalize()
                apellido_formateado = apellido.capitalize()
                bandera = False
                # Mostrás resultado final
                return nombre_formateado, apellido_formateado 

def lista_registro():
    """lista_nuevo: [id, dni, nombre, apellido, edad]"""
    lista_nuevo = []
    print("=" * 70)
    print("BIENVENIDO! Te pediremos tus datos para registrarte como paciente")
    print("=" * 70)

    
    dni = validar_dni()  
    lista_nuevo.append(dni) 
    # Pedir y validar el nombre y apellido
    nombre, apellido = tomar_nombre()  # pide nombre y valida
    lista_nuevo.append(nombre)  # Se agrega nombre en la posición 1
    lista_nuevo.append(apellido)  # Se agrega apellido en la posición 2

    # Pedir y validar la edad
    edad = validar_edad()  # Pide y valida la edad
    lista_nuevo.append(edad)  # Se agrega la edad en la posición 3

    # Generar un nuevo ID
    id = generar_nuevo_id(matriz_pacientes)  # Genera un nuevo ID
    lista_nuevo.insert(0, id)  # Se inserta el ID en la posición 0

    return lista_nuevo  # Devolvemos la lista con los datos
