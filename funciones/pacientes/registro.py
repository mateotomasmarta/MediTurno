from datos import matriz_pacientes, matriz_turnos
from agenda import mostrar_turnos_por_doctor
from utils.auxiliares import obtener_nombre_paciente, buscar_valor_por_clave
import time

# ===================================================================
# FUNCIONES DE VALIDACIÓN Y AYUDA
# ===================================================================

# FUNCIONES DE VALIDACIÓN
def validar_si_no():
    while True:
        respuesta = input("Por favor ingresa 'si' o 'no' (sin comillas): ").strip().lower()  # Se normaliza a minúsculas
        if respuesta == "si" or respuesta == "no":  # Validamos si es "si" o "no"
            return respuesta  # Si es válido, lo retornamos
        else:
            print("⚠️ Respuesta inválida. Por favor, ingresa solo 'si' o 'no'.")


def validar_dni():
    # Pedís el DNI al usuario, importante que solo tenga números y entre 7 y 8 dígitos
    dni = input("ingresá tu DNI (importante respetar la cantidad de digitos y no agregar letras ni guiones): ")
    return dni.isdigit() and 7 <= len(dni) <= 8


def validar_edad():
    while True:
        edad = input("Ingresá tu edad: ").strip()
        if edad.isdigit():
            edad = int(edad)
            if 0 < edad < 100:
                return edad
            else:
                print("⚠️ Ingresá una edad válida entre 1 y 100.")
        else:
            print("⚠️ La edad debe ser un número.")


def normalizar_cadena(cadena):
    # Normaliza una cadena para comparar cuando necesite buscar nombres de pacientes o dni:
    # sin espacios, todo en minúsculas
    return cadena.strip().lower()


# ===================================================================
# FUNCIONES AUXILIARES DATOS PACIENTES
# ===================================================================
def tomar_nombre():
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
                bandera == False
                # Mostrás resultado final
                return nombre_formateado, apellido_formateado  # Devolvemos una tupla con nombre y apellido

def buscar_paciente(dni, lista_pacientes):
    # Buscás el paciente según DNI y nombre exacto (todo normalizado)
    dni = dni.strip()  # saco cualquier espacio que joda
    nombre = normalizar_cadena(nombre)  # paso todo a minúscula por las dudas

    for paciente in lista_pacientes:
        # me fijo si coincide dni y nombre en la matriz
        if paciente['dni'] == dni and normalizar_cadena(paciente['nombre']) == nombre:
            return paciente  # te devuelve el paciente que encuentra
    return None  # si no encuentra, devuelve None


def generar_nuevo_id(matriz):
    # La funcion recorre cada posicion 0 de cada fila de la matriz y busca el numero mayor,
    # a partir de este le suma 1 y crea el id, osea te devuelve un valor
    return max([turno[0] for turno in matriz], default=0) + 1


def obtener_id_por_dni(mpacientes, dni_buscado):
    # Busca en la matriz de pacientes el paciente cuyo dni coincida y devuelve el paciente_id
    resultado = list(filter(lambda p: p['dni'] == dni_buscado, mpacientes))
    if resultado:
        return resultado[0]['id']
    else:
        return None

#habria que usar esta funcion un poco mas ampliamente para vaidar
# que no haya mas de un dni igual para distintos pacientes



def lista_registro():
    """lista_nuevo: [id, dni, nombre, apellido, edad]"""
    lista_nuevo = []

    print("Bienvenido! Te pediremos tus datos para registrarte como paciente")

    nombre , apellido = tomar_nombre()  # pide nombre y valida
    lista_nuevo.insert(2, nombre)
    lista_nuevo.insert(3, apellido)

    dni = validar_dni()  # pide dni y valida
    lista_nuevo.insert(1, dni)

    edad = validar_edad()  # pide edad y valida
    lista_nuevo.insert(4, edad)

    id = generar_nuevo_id(matriz_turnos)
    lista_nuevo.insert(0, id)

    return lista_nuevo


# ===================================================================
# FUNCIONES DE TURNOS
# ===================================================================
def obtener_turnos_paciente(matriz_turnos, id_paciente):
    # Filtramos la matriz con lambda para quedarnos con los turnos de ese paciente
    turnos_filtrados = list(filter(lambda t: t[3] == id_paciente, matriz_turnos))

    #la variable turnos_filtrados ahoracontiene una lista, basicamente la fila del pacielte encontrado

    if not turnos_filtrados:
        return "No tiene aún turnos asignados."

    # Creamos una lista de tuplas con (día, hora)
    lista_tuplas = list(map(lambda t: (t[1], t[2]), turnos_filtrados))

    return lista_tuplas


def validar_turno(dia_turno, hora_turno):
    # Validar que el turno esté disponible
    turno_valido = False  # Bandera para verificar si el turno es válido

    # Compara el día y la hora con los datos de la matriz de turnos
    for i in range(len(matriz_turnos)):
        # Desempaquetamos la fila de la matriz para obtener los valores
        id_turno, dia, hora, id_paciente_turno, estado, id_doctor = matriz_turnos[i]

        # Compara si el día y la hora coinciden con los ingresados por el paciente
        if dia == dia_turno and hora == hora_turno:
            # Verifica si el turno está disponible
            if estado == 'disponible':
                turno_valido = True # El turno es válido y disponible
                print(f"Turno disponible: {dia_turno} a las {hora_turno}")
            else:
                # El turno está ocupado
                print(f"Lo siento, el turno para {dia_turno} a las {hora_turno} ya está ocupado.")
            break  # Ya encontramos el turno, no es necesario seguir buscando

    # Si no se encontró un turno válido, informamos al paciente
    if not turno_valido:
        print(f"No se encontró un turno disponible para el día {dia_turno} y la hora {hora_turno}.")
    
    return turno_valido


def cargar_turno_paciente(id_paciente):
    # Pedir al paciente el día y hora de su preferencia
    print("Por favor, selecciona un día y una hora para tu turno.")
    dia_turno = input("Día (lunes, miércoles, viernes): ").strip().lower()
    hora_turno = input("Hora (ejemplo: 08:00, 09:00, 16:00): ").strip()

    # Validamos si el turno está disponible (utilizamos la función de búsqueda)
    turno_encontrado = validar_turno_disponible(dia_turno, hora_turno)

    if turno_encontrado:

        # Usamos un bucle 'for i in range' para recorrer la matriz de turnos
        for i in range(len(matriz_turnos)):
            # Buscamos el turno que coincida con la fecha y la hora seleccionadas
            if matriz_turnos[i][1] == dia_turno and matriz_turnos[i][2] == hora_turno:
                # Verificamos que el campo del paciente esté vacío (es decir, aún no tiene asignado un paciente)
                if matriz_turnos[i][3] is None:
                    # Asignamos el turno al paciente
                    matriz_turnos[i][3] = id_paciente  # Asignamos el ID del paciente al turno
                    matriz_turnos[i][4] = 'ocupado'   # Cambiamos el estado a ocupado
                    print(f"¡Turno asignado con éxito! Tu turno es el {dia_turno} a las {hora_turno}.")
                    break





# =============================================================================


# PROGRAMA PRINCIPAL


# =============================================================================


def login_pacientes():
    # arranca el menú principal para pacientes
    # si ya tiene cuenta pedís solo dni, y si no le pedimos todos los datos
    print("\n👨‍⚕️ Bienvenido al módulo de Pacientes 👨‍⚕️")
    print("¿Ya tenés cuenta? (si/no): ")
    tiene_cuenta = validar_si_no()


# =============================================================================
#PACIENTE REGISTRADO:
# =============================================================================
    if tiene_cuenta == "si":
        
        dni = validar_dni()  # pide dni y valida
        paciente = buscar_paciente(dni, matriz_pacientes)

        if paciente is None:
            while True:
                print("❌ Credenciales inválidas. Volviendo al menú principal...")
                time.sleep(2)
                login_pacientes()

        else:
            # Si se encuentra el paciente, obtenés su id a partir del dni
            id_paciente = obtener_id_por_dni(matriz_turnos, dni)

            # Buscás y mostrás los turnos
            nombre_pacienteregistrado = obtener_nombre_paciente(id_paciente)
            print(f"¡Hola, {nombre_pacienteregistrado}! Estos son tus turnos disponibles:")
            turnos = obtener_turnos_paciente(matriz_turnos, id_paciente)
            print(', '.join(turnos))

            #QUIERE CARGAR NUEVO TURNO
            time.sleep(2)
            print("desea cargar un nuevo turno?")
            carga=validar_si_no()

            if carga == "si":

                print("estos son los turnos disponibles:")
                diccionario_paciente= buscar_valor_por_clave(matriz_pacientes, 'id', id_paciente)
                edad=diccionario_paciente['edad']

                if edad <=18:
                    mostrar_turnos_por_doctor(2)
                else:
                    mostrar_turnos_por_doctor(1)

                time.sleep(3)

                cargar_turno_paciente(id_paciente)

# =============================================================================
#PACIENTE NUEVO:
# =============================================================================

    else:

        #para registrar en la matriz
        while continuar_registro:
            lista_nuevo = lista_registro()

             # Claves esperadas en la matriz de pacientes
            claves = ['id', 'dni', 'nombre', 'apellido', 'edad']
            nuevo_diccionario = dict(zip(claves, lista_nuevo))

            print("Desea cambiar algún dato? marque 'si'. De querer confirmar la carga de datos, marque 'no'.")
            confirmo = validar_si_no()

            if confirmo == "no":
            # Si el paciente confirma, se guarda el registro y se sale del bucle
                print("¡Registro exitoso! Estos son tus datos como paciente:")
                for clave, valor in nuevo_diccionario.items():
                    print(f"{clave.capitalize()}: {valor}")
                matriz_pacientes.append(nuevo_diccionario)

                continuar_registro = False

            else:
                 # Si el paciente quiere cambiar algún dato, volvemos a pedir los datos
                print("Comenzaremos de nuevo a solicitar sus datos.")
                nuevo_diccionario.clear()  # Limpiar el diccionario (opcional, ya que se va a sobreescribir)
                continuar_registro=True

        time.sleep(3)

# =============================================================================
#AHORA PARA CARGAR TURNOS 

        if nuevo_diccionario['edad'] <= 18 :
            print("Bienvenido al sector de pediatria, seras atendido por la Dra. Ana Brizuela")
            print("desea ver los turnos disponibles?")
            desea_turno=validar_si_no()

            if desea_turno == "si":
                print("estos son los turnos disponibles:")
                mostrar_turnos_por_doctor(2)
                print("desea cargar un turno?")
                carga_turno=validar_si_no()

                if carga_turno == si:
                    cargar_turno_paciente(nuevo_diccionario[id])
        
            else:
                print("Muchas gracias, ahora estas registrado.")
                print("Volviendo al menu principal...")
                time.sleep(2)

        if nuevo_diccionario['edad'] >=18 :
            print("Bienvenido al sector de guardia, seras atendido por el Dr. Juan Russo")
            print("desea ver los turnos disponibles?")
            desea_turno=validar_si_no()

            if desea_turno == "si":
                print("estos son los turnos disponibles:")
                mostrar_turnos_por_doctor(1)
                print("desea cargar un turno?")
                carga_turno=validar_si_no()

                if carga_turno == si:
                    cargar_turno_paciente(nuevo_diccionario[id])
        
            else:
                print("Muchas gracias, ahora estas registrado.")
                print("Volviendo al menu principal...")
                time.sleep(2)







