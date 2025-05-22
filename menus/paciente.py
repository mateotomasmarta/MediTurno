import time
from utils.validaciones import validar_dni
from datos import matriz_pacientes, matriz_turnos
from utils.auxiliares import buscar_paciente, obtener_id_por_dni,obtener_nombre_paciente
from funciones.pacientes.registro import lista_registro, registrar_paciente
from funciones.pacientes.turnos import obtener_turnos_paciente, cargar_turno_paciente, mostrar_turnosdipo_paciente, ver_mis_turnos



def autenticar_paciente():
    """Maneja el proceso de login/registro de pacientes"""
    print("\n" + "═" * 50)
    print("🏥 BIENVENIDO AL SISTEMA DE PACIENTES")
    print("═" * 50)
    
    while True:
        try:
            print("\n¿Ya tienes una cuenta registrada?")
            print("1. Sí, ingresar con mi DNI")
            print("2. No, quiero registrarme")
            print("3. Volver al menú principal")
            
            opcion = input("\n➤ Seleccione una opción [1-3]: ").strip()
            
            if opcion == "1":
                try:
                    dni = validar_dni()
                    paciente = buscar_paciente(dni, matriz_pacientes)
                    
                    if paciente:
                        print(f"\nBienvenido/a {paciente['nombre']} {paciente['apellido']}!")
                        return paciente  
                    else:
                        print("\n⚠️ No se encontró un paciente con ese DNI.")
                        print("¿Desea registrarse? (s/n)")
                        if input().lower() == 's':
                            return registrar_paciente()
                except Exception as e:
                    print(f"⚠️ Error al validar el DNI: {e}")
            
            elif opcion == "2":
                try:
                    resultado = registrar_paciente()
                    if resultado is None:
                        print("🔙 Volviendo al inicio...")
                        autenticar_paciente()
                except Exception as e:
                    print(f"⚠️ Error al registrar paciente: {e}")
            
            elif opcion == "3":
                print("\n🔙 Volviendo al menú principal...")
                time.sleep(1)
                break
            
            else:
                print("\n⚠️ Opción inválida. Por favor intente nuevamente.")
        except Exception as e:
            print(f"⚠️ Ocurrió un error inesperado: {e}")

def mostrar_menu_pacientes():
    """Menú principal para pacientes autenticados"""
    paciente_actual = autenticar_paciente()
        
    if not paciente_actual:
        return  
        
    while True:
        try:
                nombre_completo = f"{paciente_actual['nombre']} {paciente_actual['apellido']}"
                
                print("\n" + "═" * 50)
                print(f"🏥 MÓDULO DE PACIENTES | {nombre_completo}")
                print("═" * 50)
                print("\n1. 🗓  Ver mis turnos")
                print("2. 🕒 Agendar nuevo turno")
                print("3. ↩️  Volver al menú principal")
                
                opcion = input("\n➤ Seleccione una opción [1-3]: ").strip()
                
                if opcion == "1":
                    try:
                        ver_mis_turnos(paciente_actual['dni'])
                    except Exception as e:
                        print(f"⚠️ Error al mostrar los turnos: {e}")
                
                elif opcion == "2":
                    try:
                        mostrar_turnosdipo_paciente()
                        cargar_turno_paciente(paciente_actual['id'], paciente_actual['edad'])
                    except Exception as e:
                        print(f"⚠️ Error al agendar un turno: {e}")
                
                elif opcion == "3":
                    print("\n🔙 Volviendo al menú principal...")
                    break
                
                else:
                    print("\n⚠️ Opción inválida. Por favor intente nuevamente.")
                time.sleep(1)
        except Exception as e:
            print(f"⚠️ Ocurrió un error inesperado en el menú: {e}")


if __name__ == "__main__":
    mostrar_menu_pacientes()
