from main import matriz_turnos_nueva as matriz_turnos #te cambia tipo alias lo que tom abas antes por la matriz nueva
from utils.auxiliares import obtener_nombre_doctor, obtener_nombre_paciente,buscar_por_dni


def mostrar_turnos_ocupados():
    print("\n" + "═" * 70)
    print("📊 TURNOS OCUPADOS")
    print("═" * 70)
    print("\nID  DÍA       HORA   PACIENTE          ESTADO      DOCTOR")
    print("-" * 60)
    
    for turno in matriz_turnos_nueva:
        id_turno, dia, hora, id_paciente, estado, id_doctor = turno
        if estado == 'ocupado':
            nombre_paciente = obtener_nombre_paciente(id_paciente)
            nombre_doctor = obtener_nombre_doctor(id_doctor)
            print(f"{(id_turno):<4} {dia:<9} {hora:<6} {nombre_paciente:<16} 🔴 OCUPADO {nombre_doctor}")
    
    print("\n" + "═" * 70)
    def guardar_turnos_en_archivo(matriz_turnos, nombre_archivo): #obvio llamamos solo la funcion con el parametro
    with open(nombre_archivo, "w", encoding="utf-8") as arch:
        for turno in matriz_turnos:
            linea = "\t".join(map(str, turno)) + "\n"
            arch.write(linea)


def mostrar_turnos_disponibles():
    print("\n" + "═" * 70)
    print("📊 TURNOS DISPONIBLES")
    print("═" * 70)
    print("\nID  DÍA       HORA   PACIENTE          ESTADO      DOCTOR")
    print("-" * 60)
    
    for turno in matriz_turnos:
        id_turno, dia, hora, id_paciente, estado, id_doctor = turno
        if estado == 'disponible':
            nombre_paciente = obtener_nombre_paciente(id_paciente)
            nombre_doctor = obtener_nombre_doctor(id_doctor)
            print(f"{(id_turno):<4} {dia:<9} {hora:<6} {nombre_paciente:<16} 🟢 DISPONIBLE {nombre_doctor}")
    
    print("\n" + "═" * 70)

def mostrar_todos_turnos():
    print("\n" + "═" * 70)
    print("📊 TODOS LOS TURNOS")
    print("═" * 70)
    print("\nID  DÍA       HORA   PACIENTE          ESTADO      DOCTOR")
    print("-" * 60)
    
    for turno in matriz_turnos:
        id_turno, dia, hora, id_paciente, estado, id_doctor = turno
        nombre_paciente = obtener_nombre_paciente(id_paciente)
        nombre_doctor = obtener_nombre_doctor(id_doctor)
        estado_emoji = "🔴 OCUPADO" if estado == 'ocupado' else "🟢 DISPONIBLE"
        print(f"{(id_turno):<4} {dia:<9} {hora:<6} {nombre_paciente:<16} {estado_emoji:<12} {nombre_doctor}")
    
    print("\n" + "═" * 70)
    

def imprimir_turno_por_dni(dni):
    pacientes = buscar_por_dni(dni)
    
    if not pacientes:
        print(f"\n⚠️ No se encontraron pacientes con el DNI: {dni}")
        return

    print("\n" + "═" * 70)
    print(f"📋 Turnos encontrados para el DNI: {dni}")
    print("═" * 70)
    print("\nID  DÍA       HORA   PACIENTE          ESTADO      DOCTOR")
    print("-" * 60)
    
    for paciente in pacientes:
        id_paciente = paciente['id']
        nombre_paciente = f"{paciente['nombre']} {paciente['apellido']}"
        

        for turno in matriz_turnos:
            id_turno, dia, hora, turno_id_paciente, estado, id_doctor = turno
            if turno_id_paciente == id_paciente:
                nombre_doctor = obtener_nombre_doctor(id_doctor)
                estado_emoji = "🔴 OCUPADO" if estado == 'ocupado' else "🟢 DISPONIBLE"
                print(f"{(id_turno):<4} {dia:<9} {hora:<6} {nombre_paciente:<16} {estado_emoji:<12} {nombre_doctor}")
    
    print("\n" + "═" * 70)

def mostrar_turnosdipo_paciente():
    print("\n" + "═" * 70)
    print(f"📊 TURNOS DISPONIBLES")
    print("═" * 70)
    print("\nID  DÍA       HORA   ESTADO       ")
    print("-" * 70)

    for turno in matriz_turnos:
        id_turno, dia, hora, id_paciente, estado, doctor_turno = turno
        if estado == 'disponible' :

            # Mostrar turno disponible
            print(f"{(id_turno):<4} {dia:<9} {hora:<6} 🟢 DISPONIBLE ")

    print("\n" + "═" * 70)
