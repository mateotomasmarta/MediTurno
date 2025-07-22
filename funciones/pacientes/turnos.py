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



import os

def guardar_turno_por_linea(nueva_fila, num_linea, path=RUTA_TURNOS):
    ruta_temp = path + ".tmp"
    with open(path, "r", encoding="utf-8") as archivo_original, \
         open(ruta_temp, "w", encoding="utf-8") as archivo_temp:
        for i, linea in enumerate(archivo_original, start=1):
            if i == num_linea:
                fila_serializada = []
                for elem in nueva_fila:
                    fila_serializada.append("None" if elem is None else str(elem))
                archivo_temp.write('\t'.join(fila_serializada) + '\n')
            else:
                archivo_temp.write(linea)
    os.replace(ruta_temp, path)


def obtener_turnos_paciente(id_paciente):
    """Obtiene los turnos de un paciente leyendo línea por línea."""
    turnos_paciente = []
    with open(RUTA_TURNOS, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            turno = linea.strip().split('\t')
            turno[0] = int(turno[0])  # id_turno
            turno[3] = int(turno[3]) if turno[3] != 'None' else None
            if turno[3] == id_paciente:
                turnos_paciente.append((turno[1], turno[2]))
    if not turnos_paciente:
        return "No tiene aún turnos asignados."
    return turnos_paciente


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

    # Validar que el turno está disponible leyendo línea por línea:
    turno_disponible = False
    num_linea = 0
    with open(RUTA_TURNOS, "r", encoding="utf-8") as archivo:
        for i, linea in enumerate(archivo, start=1):
            datos = linea.strip().split('\t')
            if datos[1] == dia_turno and datos[2] == hora_turno:
                num_linea = i
                if datos[4] == 'disponible' and datos[3] == 'None':
                    turno_disponible = True
                break
    
    if not turno_disponible:
        print("⚠️ El turno no está disponible.")
        return

    # Cargar la línea, modificarla y guardar:
    turno_actual = cargar_turno_por_linea(num_linea)
    turno_actual[3] = id_paciente
    turno_actual[4] = 'ocupado'
    turno_actual[5] = 2 if edad_paciente <= 18 else 1
    guardar_turno_por_linea(turno_actual, num_linea)

    print(f" 🟢 ¡Turno asignado con éxito! Tu turno es el {dia_turno} a las {hora_turno}.")


def mostrar_turnosdipo_paciente():
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


def ver_mis_turnos(dni_paciente):
    pacientes = cargar_archivo_pacientes(RUTA_PACIENTES)
    id_paciente = obtener_id_por_dni(dni_paciente)
    if not id_paciente:
        print("\n⚠️ No se encontró paciente con ese DNI")
        return
    
    turnos = obtener_turnos_paciente(id_paciente)
    
    print("\n" + "═" * 50)
    print(f"📅 TURNOS DE {obtener_nombre_paciente(id_paciente).upper()}")
    print("═" * 50)
    
    if turnos == "No tiene aún turnos asignados.":
        print("\nℹ️ No tienes turnos asignados.")
    else:
        print("\nID  DÍA        HORA     ESTADO")
        print("-" * 30)
        with open(RUTA_TURNOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                turno = linea.strip().split('\t')
                turno[0] = int(turno[0])
                turno[3] = int(turno[3]) if turno[3] != 'None' else None
                if turno[3] == id_paciente:
                    estado = "🔴 OCUPADO" if turno[4] == 'ocupado' else "🟢 DISPONIBLE"
                    print(f"{turno[0]:<3} {turno[1]:<10} {turno[2]:<8} {estado}")
    
    print("\n" + "═" * 50)
    input("\n⏎ Presione Enter para continuar...")
