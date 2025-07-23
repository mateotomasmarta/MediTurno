from db.funciones.archivos_txt import cargar_turno_por_linea, guardar_turno_por_linea
from utils.auxiliares import obtener_id_por_dni, obtener_nombre_paciente
from db.funciones.archivos_json import cargar_archivo_pacientes

RUTA_TURNOS = "db/turnos.txt"
RUTA_PACIENTES = "db/datos.json"

def cargar_turno_paciente(id_paciente, edad_paciente):
    print("Por favor, selecciona un día y una hora para tu turno.")

    dias_validos = {1: "lunes", 2: "miércoles", 3: "viernes"}
    horas_validas = ["08:00", "09:00", "10:00", "11:00", "13:00", "15:00", "16:00", "18:00"]

    # Elegir día
    for k, v in dias_validos.items():
        print(f"{k} = {v.capitalize()}")
    dia_num = input("Selecciona el número del día (1, 2, 3): ").strip()
    while not dia_num.isdigit() or int(dia_num) not in dias_validos:
        dia_num = input("⚠️ Día inválido. Reintentá (1, 2, 3): ").strip()
    dia_turno = dias_validos[int(dia_num)]

    # Elegir hora
    hora_turno = input("Hora (ejemplo: 08:00): ").strip()
    while hora_turno not in horas_validas:
        hora_turno = input("⚠️ Hora inválida. Reintentá: ").strip()

    try:
        with open(RUTA_TURNOS, "r", encoding="utf-8") as archivo:
            num_linea = 1
            linea = archivo.readline()
            encontrado = False

            while linea:
                datos = linea.strip().split("\t")
                if len(datos) >= 6 and datos[1] == dia_turno and datos[2] == hora_turno and datos[4] == "disponible":
                    fila = cargar_turno_por_linea(num_linea)
                    fila[3] = id_paciente
                    fila[4] = "ocupado"
                    fila[5] = 2 if edad_paciente <= 18 else 1
                    guardar_turno_por_linea(fila, num_linea)
                    print(f"🟢 ¡Turno asignado con éxito! {dia_turno} a las {hora_turno}")
                    encontrado = True
                    break
                linea = archivo.readline()
                num_linea += 1

            if not encontrado:
                print("❌ Ese turno ya está ocupado o no existe.")

    except FileNotFoundError:
        print("❌ No se encontró el archivo de turnos.")


def mostrar_turnosdipo_paciente():
    print("\n" + "═" * 70)
    print("📊 TURNOS DISPONIBLES")
    print("═" * 70)
    print("\nID  DÍA       HORA   ESTADO       ")
    print("-" * 70)

    try:
        with open(RUTA_TURNOS, "r", encoding="utf-8") as archivo:
            linea = archivo.readline()
            while linea:
                datos = linea.strip().split('\t')
                if len(datos) >= 6 and datos[4] == "disponible":
                    print(f"{datos[0]:<4} {datos[1]:<9} {datos[2]:<6} 🟢 DISPONIBLE ")
                linea = archivo.readline()
    except FileNotFoundError:
        print("❌ No se encontró el archivo de turnos.")

    print("\n" + "═" * 70)


def ver_mis_turnos(dni_paciente):
    pacientes = cargar_archivo_pacientes(RUTA_PACIENTES)
    id_paciente = obtener_id_por_dni(dni_paciente)

    if not id_paciente:
        print("\n⚠️ No se encontró paciente con ese DNI")
        return

    nombre_paciente = obtener_nombre_paciente(id_paciente)
    print("\n" + "═" * 50)
    print(f"📅 TURNOS DE {nombre_paciente.upper()}")
    print("═" * 50)

    encontrados = False
    try:
        with open(RUTA_TURNOS, "r", encoding="utf-8") as archivo:
            linea = archivo.readline()
            while linea:
                datos = linea.strip().split('\t')
                if len(datos) >= 6 and datos[3] == str(id_paciente):
                    estado = "🔴 OCUPADO" if datos[4] == 'ocupado' else "🟢 DISPONIBLE"
                    print(f"{datos[0]:<3} {datos[1]:<10} {datos[2]:<8} {estado}")
                    encontrados = True
                linea = archivo.readline()
    except FileNotFoundError:
        print("❌ No se encontró el archivo de turnos.")
        return

    if not encontrados:
        print("\nℹ️ No tienes turnos asignados.")

    print("\n" + "═" * 50)
    input("\n⏎ Presione Enter para continuar...")
