#version linea por linea de turnos

from utils.auxiliares import obtener_id_por_dni, obtener_nombre_paciente
from db.funciones.archivos_json import cargar_archivo_pacientes
from utils.validaciones import validar_turno_disponible

RUTA_PACIENTES = 'db/datos.json'
RUTA_TURNOS = "db/turnos.txt"


def leer_todos_los_turnos(path=RUTA_TURNOS):
    turnos = []
    with open(path, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            elementos = linea.strip().split('\t')
            fila = []
            for elem in elementos:
                if elem == "None":
                    fila.append(None)
                elif elem.isdigit():
                    fila.append(int(elem))
                else:
                    fila.append(elem)
            turnos.append(fila



def actualizar_turno_por_id(id_turno, id_paciente, estado, id_medico, path=RUTA_TURNOS):
    # Primero leemos todas las líneas
    with open(path, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    for i, linea in enumerate(lineas):
        elementos = linea.strip().split('\t')
        # Convertimos el ID del turno de la línea
        try:
            id_actual = int(elementos[0])
        except ValueError:
            continue  # si no es un número, ignorar esa línea

        if id_actual == id_turno:
            # Actualizamos los campos: 
            # 3° posición -> ID paciente
            # 4° posición -> estado
            # 5° posición -> ID médico
            elementos[3] = str(id_paciente) if id_paciente is not None else "None"
            elementos[4] = estado
            elementos[5] = str(id_medico) if id_medico is not None else "None"

            # Reconstruimos la línea y la guardamos en la lista
            lineas[i] = '\t'.join(elementos) + '\n'
            break
    else:
        # Si no se encontró el turno, podemos decidir si:
        #  - devolver error
        #  - o crear un nuevo turno
        # Ahora sólo aviso que no existe.
        raise ValueError(f"Turno con ID {id_turno} no encontrado.")

    # Reescribimos el archivo con la línea actualizada
    with open(path, "w", encoding="utf-8") as archivo:
        archivo.writelines(lineas)






def cargar_turno_paciente(id_paciente, edad_paciente):
    print("Por favor, selecciona un día y una hora para tu turno.")
    
    dias_validos = {1: "lunes", 2: "miércoles", 3: "viernes"}
    horas_validas = ["08:00", "09:00", "16:00", "10:00", "11:00", "13:00", "15:00", "18:00"]

    print("Días disponibles:")
    for key, value in dias_validos.items():
        print(f"{key} = {value.capitalize()}")
    
    dia_turno_num = input("Selecciona el número del día (1, 2, 3): ").strip()
    while not dia_turno_num.isdigit() or int(dia_turno_num) not in dias_validos:
        print(" ⚠️ Opción inválida. Por favor, selecciona un número válido (1, 2, 3).")
        dia_turno_num = input("Selecciona el número del día (1, 2, 3): ").strip()
    
    dia_turno = dias_validos[int(dia_turno_num)]

    hora_turno = input("Hora (ejemplo: 08:00, 09:00, 16:00): ").strip()
    while hora_turno not in horas_validas:
        print(" ⚠️ Hora inválida. Por favor, ingresa una hora válida (08:00, 09:00, 16:00).")
        hora_turno = input("Hora (ejemplo: 08:00, 09:00, 16:00): ").strip()

    # Buscar el turno disponible y obtener su ID
    id_turno_encontrado = None
    with open(RUTA_TURNOS, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split('\t')
            if datos[1] == dia_turno and datos[2] == hora_turno:
                if datos[4] == 'disponible' and datos[3] == 'None':
                    id_turno_encontrado = int(datos[0])
                    break
    
    if id_turno_encontrado is None:
        print("⚠️ El turno no está disponible.")
        return

    # Definir el id_medico según la edad
    id_medico = 2 if edad_paciente <= 18 else 1

    # Usar la función que actualiza el turno por ID directamente
    try:
        actualizar_turno_por_id(id_turno_encontrado, id_paciente, 'ocupado', id_medico)
        print(f" 🟢 ¡Turno asignado con éxito! Tu turno es el {dia_turno} a las {hora_turno}.")
    except ValueError as e:
        print("❌ Error al asignar el turno:", e)



def mostrar_turnosdiponibles():
    print("\n" + "═" * 70)
    print(f"📊 TURNOS DISPONIBLES")
    print("═" * 70)
    print("\nID  DÍA       HORA   ESTADO       ")
    print("-" * 70)

    with open(RUTA_TURNOS, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            turno = linea.strip().split('\t')
            id_turno, dia, hora, id_paciente, estado, doctor_turno = turno
            if estado == 'disponible':
                print(f"{id_turno:<4} {dia:<9} {hora:<6} 🟢 DISPONIBLE ")

    print("\n" + "═" * 70)


def mostrar_turnos_paciente_por_dni(dni_paciente):
    id_paciente = obtener_id_por_dni(dni_paciente)
    if not id_paciente:
        print("\n⚠️ No se encontró paciente con ese DNI")
        return
    
    print("\n" + "═" * 50)
    print(f"📅 TURNOS DE {obtener_nombre_paciente(id_paciente).upper()}")
    print("═" * 50)

    turnos_paciente = []

    with open(RUTA_TURNOS, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split('\t')
            partes[0] = int(partes[0])
            partes[3] = int(partes[3]) if partes[3] != 'None' else None

            if partes[3] == id_paciente:
                turnos_paciente.append(partes)

    if not turnos_paciente:
        print("\nℹ️ No tienes turnos asignados.")
    else:
        print("\nID  DÍA        HORA     ESTADO")
        print("-" * 30)
        for partes in turnos_paciente:
            # Estado fijo porque son todos ocupados por el paciente
            estado = "🔴 OCUPADO"
            print(f"{partes[0]:<3} {partes[1]:<10} {partes[2]:<8} {estado}")

    print("\n" + "═" * 50)
    input("\n⏎ Presione Enter para continuar...")
