from db.funciones.archivos_txt import cargar_turnos, guardar_turnos
from utils.auxiliares import obtener_id_por_dni, obtener_nombre_paciente
from db.funciones.archivos_json import cargar_archivo_pacientes
from utils.validaciones import validar_turno_disponible

RUTA_PACIENTES = 'db/datos.json'

def obtener_turnos_paciente(id_paciente):
    """Obtiene los turnos de un paciente desde el archivo txt"""
    matriz_turnos = cargar_turnos()
    turnos_filtrados = list(filter(lambda t: t[3] == id_paciente, matriz_turnos))
    if not turnos_filtrados:
        return "No tiene aún turnos asignados."
    return list(map(lambda t: (t[1], t[2]), turnos_filtrados))

def cargar_turno_paciente(id_paciente, edad_paciente, matriz_turnos):
    """Carga un turno para un paciente y guarda en txt"""
    matriz_turnos = cargar_turnos()
    print("Por favor, selecciona un día y una hora para tu turno.")
    
    dias_validos = {1: "lunes", 2: "miércoles", 3: "viernes"}
    horas_validas = ["08:00", "09:00", "16:00", "10:00", "11:00", "13:00", "15:00", "18:00"]

    # Selección del día
    print("Días disponibles:")
    for key, value in dias_validos.items():
        print(f"{key} = {value.capitalize()}")
    
    dia_turno_num = input("Selecciona el número del día (1, 2, 3): ").strip()
    while not dia_turno_num.isdigit() or int(dia_turno_num) not in dias_validos:
        print(" ⚠️ Opción inválida. Por favor, selecciona un número válido (1, 2, 3).")
        dia_turno_num = input("Selecciona el número del día (1, 2, 3): ").strip()
    
    dia_turno = dias_validos[int(dia_turno_num)]

    # Validación de la hora
    hora_turno = input("Hora (ejemplo: 08:00, 09:00, 16:00): ").strip()
    while hora_turno not in horas_validas:
        print(" ⚠️ Hora inválida. Por favor, ingresa una hora válida (08:00, 09:00, 16:00).")
        hora_turno = input("Hora (ejemplo: 08:00, 09:00, 16:00): ").strip()

    turno_encontrado = validar_turno_disponible(dia_turno, hora_turno, matriz_turnos)

    if turno_encontrado:
        for i in range(len(matriz_turnos)):
            if matriz_turnos[i][1] == dia_turno and matriz_turnos[i][2] == hora_turno:
                if matriz_turnos[i][3] is None:
                    matriz_turnos[i][3] = id_paciente  
                    matriz_turnos[i][4] = 'ocupado'   
                    if edad_paciente <= 18:
                        matriz_turnos[i][5] = 2
                    else:
                        matriz_turnos[i][5] = 1
                    guardar_turnos(matriz_turnos)  # Guardar cambios
                    print(f" 🟢 ¡Turno asignado con éxito! Tu turno es el {dia_turno} a las {hora_turno}.")
                    break

def mostrar_turnosdipo_paciente(matriz_turnos):
    """Muestra los turnos disponibles leyendo del archivo txt"""
    matriz_turnos = cargar_turnos()
    print("\n" + "═" * 70)
    print(f"📊 TURNOS DISPONIBLES")
    print("═" * 70)
    print("\nID  DÍA       HORA   ESTADO       ")
    print("-" * 70)

    for turno in matriz_turnos:
        id_turno, dia, hora, id_paciente, estado, doctor_turno = turno
        if estado == 'disponible':
            print(f"{(id_turno):<4} {dia:<9} {hora:<6} 🟢 DISPONIBLE ")

    print("\n" + "═" * 70)

def ver_mis_turnos(dni_paciente, matriz_turnos):
    """Muestra los turnos del paciente leyendo del archivo txt"""
    matriz_turnos = cargar_turnos()
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
        for turno in matriz_turnos:
            if turno[3] == id_paciente:
                estado = "🔴 OCUPADO" if turno[4] == 'ocupado' else "🟢 DISPONIBLE"
                print(f"{turno[0]:<3} {turno[1]:<10} {turno[2]:<8} {estado}")
    
    print("\n" + "═" * 50)
    input("\n⏎ Presione Enter para continuar...")