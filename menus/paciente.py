import time
from utils.validaciones import validar_si_no, validar_dni,validar_edad
from datos import matriz_pacientes, matriz_turnos
from utils.auxiliares import buscar_paciente, obtener_id_por_dni,obtener_nombre_paciente
from funciones.pacientes.registro import lista_registro
from funciones.pacientes.turnos import obtener_turnos_paciente, cargar_turno_paciente
from funciones.pacientes.turnos import mostrar_turnosdipo_paciente


def autenticar_paciente():
    """Maneja el proceso de login/registro de pacientes"""
    print("\n" + "═" * 50)
    print("🏥 BIENVENIDO AL SISTEMA DE PACIENTES")
    print("═" * 50)
    
    while True:
        print("\n¿Ya tienes una cuenta registrada?")
        print("1. Sí, ingresar con mi DNI")
        print("2. No, quiero registrarme")
        print("3. Volver al menú principal")
        
        opcion = input("\n➤ Seleccione una opción [1-3]: ").strip()
        
        if opcion == "1":
            dni = input("\nIngrese su DNI: ").strip()
            paciente = buscar_paciente(dni, matriz_pacientes)
            
            if paciente:
                print(f"\nBienvenido/a {paciente['nombre']} {paciente['apellido']}!")
                return paciente  # Devuelve el diccionario del paciente
            else:
                print("\n⚠️ No se encontró un paciente con ese DNI.")
                print("¿Desea registrarse? (s/n)")
                if input().lower() == 's':
                    return registrar_paciente()
        
        elif opcion == "2":
            return registrar_paciente()
        
        elif opcion == "3":
            print("\n🔙 Volviendo al menú principal...")
            time.sleep(1)

        
        else:
            print("\n⚠️ Opción inválida. Por favor intente nuevamente.")

def registrar_paciente():
    """Maneja el proceso de registro de nuevos pacientes"""
    print("\n" + "═" * 50)
    print("📝 REGISTRO DE NUEVO PACIENTE")
    print("═" * 50)
    
    # Utilizamos la función de registro existente
    nuevo_paciente = lista_registro()
    
    # Convertimos la lista a diccionario para consistencia
    paciente_dict = {
        'id': nuevo_paciente[0],
        'dni': nuevo_paciente[1],
        'nombre': nuevo_paciente[2],
        'apellido': nuevo_paciente[3],
        'edad': nuevo_paciente[4]
    }
    
    # Agregamos el nuevo paciente a la matriz (esto debería hacerse en datos.py)
    matriz_pacientes.append(paciente_dict)
    
    print(f"\n✅ Registro exitoso! Bienvenido/a {paciente_dict['nombre']} {paciente_dict['apellido']}")
    return paciente_dict

def mostrar_menu_pacientes():
    """Menú principal para pacientes autenticados"""
    paciente_actual = autenticar_paciente()
    
    if not paciente_actual:
        return  # Regresa al menú principal
    
    while True:
        # Obtener nombre completo correctamente
        nombre_completo = f"{paciente_actual['nombre']} {paciente_actual['apellido']}"
        
        print("\n" + "═" * 50)
        print(f"🏥 MÓDULO DE PACIENTES | {nombre_completo}")
        print("═" * 50)
        print("\n1. 🗓  Ver mis turnos")
        print("2. 🕒 Agendar nuevo turno")
        print("3. ↩️  Volver al menú principal")
        
        opcion = input("\n➤ Seleccione una opción [1-3]: ").strip()
        
        if opcion == "1":
            ver_mis_turnos(paciente_actual['dni'])
            
        elif opcion == "2":
            mostrar_turnosdipo_paciente()
            cargar_turno_paciente(paciente_actual['id'], paciente_actual['edad'])
            
        elif opcion == "3":
            break
            
        else:
            print("\n⚠️ Opción inválida. Por favor intente nuevamente.")
        time.sleep(1)

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

if __name__ == "__main__":
    mostrar_menu_pacientes()