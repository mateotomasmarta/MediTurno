import time
from funciones.secretario.login import validar_credenciales
from utils.auxiliares import buscar_por_dni, buscar_por_nombre_o_apellido
from funciones.secretario.agenda import mostrar_turnos_disponibles_secretaria, mostrar_turnos_ocupados, mostrar_todos_turnos, imprimir_turno_por_dni
from datos import matriz_turnos
from funciones.secretario.gestion import vaciar_turno,elegir_turno_a_modificar, elegir_dia, modifica_turno


def mostrar_menu_secretaria():
    """Menú de secretaría con sistema de login"""
    while True:
        print("╔══════════════════════════════════════════╗")
        print("║        🔐 ACCESO SECRETARÍA 🔐          ║")
        print("╠══════════════════════════════════════════╣")
        
        usuario = input("Usuario: ")
        password = input("Contraseña: ")

        if validar_credenciales(usuario, password):
            menu_secretario_principal()
            break
        else:
            print("⚠️ Credenciales incorrectas!")
            time.sleep(1.5)


def menu_secretario_principal():
    """Menú principal después del login"""
    while True:
        print("╔══════════════════════════════════════════╗")
        print("║        📋 MÓDULO DE SECRETARÍA 📋        ║")
        print("╠══════════════════════════════════════════╣")
        print("║                                          ║")
        print("║  1. 👥 Gestionar Pacientes               ║")
        print("║  2. 📅 Gestionar Turnos                  ║")
        print("║  3. ↩️  Volver al menú principal         ║")
        print("║                                          ║")
        print("╚══════════════════════════════════════════╝")
        
        opcion = input("➤ Seleccione una opción [1-3]: ")
        
        if opcion == "1":
            while True:
                print("╔══════════════════════════════════════════╗")
                print("║        📋 GESTIONAR PACIENTES            ║")
                print("╠══════════════════════════════════════════╣")
                print("║                                          ║")
                print("║  1. 📋 Buscar por DNI                    ║")
                print("║  2. 📋 Buscar por Nombre o Apellido      ║")
                print("║  3. ↩️ Volver al menú principal         ║")
                print("║                                          ║")
                print("╚══════════════════════════════════════════╝")
                
                opcion_paciente = input("➤ Seleccione una opción [1-3]: ")
                
                if opcion_paciente == "1":
                    dni = input("📋 Ingrese el DNI del paciente: ")
                    resultados = buscar_por_dni(dni)
                    if resultados:
                        for i, paciente in enumerate(resultados, 1):
                            print(" " * 10 + f"\n🧑 Paciente #{i}:")
                            print(" " * 12 + f"├─ Nombre: {paciente['nombre']}")
                            print(" " * 12 + f"├─ Apellido: {paciente['apellido']}")
                            print(" " * 12 + f"├─ Edad: {paciente['edad']} años")
                            print(" " * 12 + f"└─ DNI: {paciente['dni']}")
                    else:
                        print("\n" + " " * 10 + "⚠️ No se encontraron resultados.")
                    opcion = input("➤ Desea realizar otra búsqueda? (s/n): ").lower()
                    if opcion != "s":
                        break
                
                elif opcion_paciente == "2":
                    filtro = input("📋 Ingrese el nombre o apellido del paciente: ")
                    resultados = buscar_por_nombre_o_apellido(filtro)
                    if resultados:
                        for i, paciente in enumerate(resultados, 1):
                            print(" " * 10 + f"\n🧑 Paciente #{i}:")
                            print(" " * 12 + f"├─ Nombre: {paciente['nombre']}")
                            print(" " * 12 + f"├─ Apellido: {paciente['apellido']}")
                            print(" " * 12 + f"├─ Edad: {paciente['edad']} años")
                            print(" " * 12 + f"└─ DNI: {paciente['dni']}")
                    else:
                        print("\n" + " " * 10 + "⚠️ No se encontraron resultados.")
                    opcion = input("➤ Desea realizar otra búsqueda? (s/n): ").lower()
                    if opcion != "s":
                        break
                
                elif opcion_paciente == "3":
                    break
                else:
                    print("\n⚠️ Opción inválida!")
                    time.sleep(1)
        
        elif opcion == "2":
            print("\n" + "═" * 70)
            print("📊 TODOS LOS TURNOS")
            
            while True:
                mostrar_todos_turnos()
                print("\n╔══════════════════════════════════════════╗")
                print("║        🛠️ GESTIONAR TURNOS               ║")
                print("╠══════════════════════════════════════════╣")
                print("║                                          ║")
                print("║  1. ✏️ Modificar un turno                ║")
                print("║  2. 🗑️ Eliminar un turno                 ║")
                print("║  3. 📅 Filtrar turnos                    ║")
                print("║  4. ↩️ Volver al menú principal          ║")
                print("║                                          ║")
                print("╚══════════════════════════════════════════╝")
                
                opcion_turno = input("➤ Seleccione una opción [1-4]: ")
                
                if opcion_turno == "1":
                    while True:
                        mostrar_turnos_ocupados()
                        turnos_a_modificar = elegir_turno_a_modificar(matriz_turnos)
                        turnos_d=mostrar_turnos_disponibles_secretaria()
                        dia=elegir_dia(turnos_d)
                        modifica_turno(turnos_a_modificar, dia, matriz_turnos)
                        opcion = input("➤ ¿Desea modificar otro turno? (si/no): ").lower()
                        if opcion != "si":
                            break
                    
                
                elif opcion_turno == "2":
                    while True:
                        dni = input("📋 Ingrese el DNI del paciente: ")
                        imprimir_turno_por_dni(dni)
                        vaciar_turno(matriz_turnos)
                        opcion = input("➤ ¿Desea eliminar otro turno? (s/n): ").lower()
                        if opcion != "s":
                            break
                
                elif opcion_turno == "3":
                    while True:
                        print("╔══════════════════════════════════════════╗")
                        print("║        📅 FILTRAR TURNOS                 ║")
                        print("╠══════════════════════════════════════════╣")
                        print("║                                          ║")
                        print("║  1. 📅 Filtrar por ocupados              ║")
                        print("║  2. 📅 Filtrar por disponibles           ║")
                        print("║  3. ↩️ Volver al menú principal          ║")
                        print("║                                          ║")
                        print("╚══════════════════════════════════════════╝")
                        
                        opcion_filtro = input("➤ Seleccione una opción [1-3]: ")
                        
                        if opcion_filtro == "1":
                            mostrar_turnos_ocupados()
                        elif opcion_filtro == "2":
                            mostrar_turnos_disponibles_secretaria()
                        elif opcion_filtro == "3":
                            break
                        else:
                            print("\n⚠️ Opción inválida!")
                            time.sleep(1)
                    
                
                elif opcion_turno == "4":
                    break
                
                else:
                    print("\n⚠️ Opción inválida!")
                    time.sleep(1)
        
        elif opcion == "3":
            break
        
        else:
            print("\n⚠️ Opción inválida!")
            time.sleep(1)


if __name__ == "__main__":
    mostrar_menu_secretaria()
