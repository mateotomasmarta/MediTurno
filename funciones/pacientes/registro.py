# FUNCIONES DE VALIDACIÓN Y AYUDA

def validar_dni():
    # Pedís el DNI al usuario, importante que solo tenga números y entre 7 y 8 dígitos
    dni = input("ingresá tu DNI (importante respetar la cantidad de digitos y no agregar letras ni guiones): ")
    return dni.isdigit() and 7 <= len(dni) <= 8

def tomar_nombre():
    while True:
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

                # Mostrás resultado final
                return f"{nombre_formateado} {apellido_formateado}"

def normalizar_cadena(cadena):
    # Normaliza una cadena para comparar cuando necesite buscar nombres de pacientes o dni:
    # sin espacios, todo en minúsculas
    return cadena.strip().lower()

def buscar_paciente(dni, nombre, lista_pacientes):
    # Buscás el paciente según DNI y nombre exacto (todo normalizado)
    dni = dni.strip()  # saco cualquier espacio que joda
    nombre = normalizar_cadena(nombre)  # paso todo a minúscula por las dudas

    for paciente in lista_pacientes:
        # me fijo si coincide dni y nombre en la matriz
        if paciente['dni'] == dni and normalizar_cadena(paciente['nombre']) == nombre:
            return paciente  # te devuelve el paciente que encuentra
    return None  # si no encuentra, devuelve None

def generar_nuevo_id(lista):
    # item['id'] for item in lista => toma de la lista todos los valores donde haya clave 'id'
    # max busca el más grande y le sumás uno para generar un nuevo ID
    # si la lista está vacía, por default arranca de 0 y le suma 1
    return max([item['id'] for item in lista], default=0) + 1

def obtener_id_por_dni(mturnos, dni_buscado):
    # busca en la matriz de turnos el paciente cuyo dni coincida y devuelve el paciente_id
    resultado = list(filter(lambda p: p['dni'] == dni_buscado, mturnos))
    if resultado:
        return resultado[0]['paciente_id']
    else:
        return None


# FUNCIONES DE TURNOS

def obtener_turnos_paciente(turnos, id_paciente):
    # filtrás de la matriz de turnos solo aquellos que coincidan con el id del paciente
    turnos_filtrados = list(filter(lambda turno: turno['paciente_id'] == id_paciente, turnos))
    # convertís el filtro a lista para poder verificar si está vacío

    if not turnos_filtrados:
        return "No tiene aún turnos asignados."

    # devolvés una lista de tuplas con día y hora, sacados de los turnos del paciente
    return list(map(lambda turno: (turno['dia'], turno['hora']), turnos_filtrados))


# PROGRAMA PRINCIPAL

from datos import matriz_pacientes, matriz_turnos
import time

def mostrar_menu_pacientes():
    # arranca el menú principal para pacientes
    print("\n👨‍⚕️ Bienvenido al módulo de Pacientes 👨‍⚕️")
    tiene_cuenta = input("¿Ya tenés cuenta? (si/no): ").strip().lower()
    # lo que te contesta te ahorra los espacios y lo vuelve minúscula

    if tiene_cuenta == "si":
        nombre = tomar_nombre()  # pide nombre y valida
        dni = validar_dni()      # pide dni y valida

        paciente = buscar_paciente(dni, nombre, matriz_pacientes)

        if paciente is None:
            print("❌ Credenciales inválidas. Volviendo al menú principal...")
            time.sleep(2)
        else:
            # si se encuentra el paciente, obtenés su id a partir del dni
            id_paciente = obtener_id_por_dni(matriz_turnos, dni)
            # buscás y mostrás los turnos
            turnos = obtener_turnos_paciente(matriz_turnos, id_paciente)
            print(turnos)


def prueba_git():
    pass