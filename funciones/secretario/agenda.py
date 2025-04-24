from datos import matriz_turnos
from utils.auxiliares import obtener_nombre_doctor, obtener_nombre_paciente

def mostrar_turnos_ocupados():
    print("\n" + "═" * 70)
    print("📊 TURNOS OCUPADOS")
    print("═" * 70)
    print("\nID  DÍA       HORA   PACIENTE          ESTADO      DOCTOR")
    print("-" * 60)
    
    for turno in matriz_turnos:
        id_turno, dia, hora, id_paciente, estado, id_doctor = turno
        if estado == 'ocupado':
            nombre_paciente = obtener_nombre_paciente(id_paciente)
            nombre_doctor = obtener_nombre_doctor(id_doctor)
            print(f"{(id_turno):<4} {dia:<9} {hora:<6} {nombre_paciente:<16} 🔴 OCUPADO {nombre_doctor}")
    
    print("\n" + "═" * 70)


def mostrar_turnos_disponibles():
    """Muestra todos los turnos disponibles."""
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
    """Muestra todos los turnos, tanto ocupados como disponibles."""
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