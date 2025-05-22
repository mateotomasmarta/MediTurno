from datos import matriz_turnos, matriz_pacientes
from utils.auxiliares import buscar_paciente, obtener_id_por_dni, obtener_nombre_paciente

from utils.validaciones import validar_turno_disponible

def obtener_turnos_paciente(matriz_turnos, id_paciente):
    
    turnos_filtrados = list(filter(lambda t: t[3] == id_paciente, matriz_turnos))
    if not turnos_filtrados:
        return "No tiene aún turnos asignados."
    # Creamos una lista de tuplas con (día, hora)
    lista_tuplas = list(map(lambda t: (t[1], t[2]), turnos_filtrados))
    return lista_tuplas



def cargar_turno_paciente(id_paciente, edad_paciente):
    print("Por favor, selecciona un día y una hora para tu turno.")
    
    dias_validos = ["lunes", "miércoles", "viernes"]
    horas_validas = ["08:00", "09:00", "16:00", "10:00", "11:00", "13:00", "15:00", "18:00"]

    dia_turno = input("Día (lunes, miércoles, viernes): ").strip().lower()
    while dia_turno not in dias_validos:
        print(" ⚠️ Día inválido. Por favor, ingresa un día válido (lunes, miércoles, viernes).")
        dia_turno = input("Día (lunes, miércoles, viernes): ").strip().lower()

    # Validación de la hora
    hora_turno = input("Hora (ejemplo: 08:00, 09:00, 16:00): ").strip()
    while hora_turno not in horas_validas:
        print(" ⚠️ Hora inválida. Por favor, ingresa una hora válida (08:00, 09:00, 16:00).")
        hora_turno = input("Hora (ejemplo: 08:00, 09:00, 16:00): ").strip()

    turno_encontrado = validar_turno_disponible(dia_turno, hora_turno)

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
                    print(f" 🟢 ¡Turno asignado con éxito! Tu turno es el {dia_turno} a las {hora_turno}.")
                    break
                
def mostrar_turnosdipo_paciente():
    print("\n" + "═" * 70)
    print(f"📊 TURNOS DISPONIBLES")
    print("═" * 70)
    print("\nID  DÍA       HORA   ESTADO       ")
    print("-" * 70)

    for turno in matriz_turnos:
        id_turno, dia, hora, id_paciente, estado, doctor_turno = turno
        if estado == 'disponible' :

            print(f"{(id_turno):<4} {dia:<9} {hora:<6} 🟢 DISPONIBLE ")

    print("\n" + "═" * 70)

def ver_mis_turnos(dni_paciente):
    """Muestra los turnos del paciente actual"""
    id_paciente = obtener_id_por_dni(matriz_pacientes, dni_paciente)
    if not id_paciente:
        print("\n⚠️ No se encontró paciente con ese DNI")
        return
    
    turnos = obtener_turnos_paciente(matriz_turnos, id_paciente)
    
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