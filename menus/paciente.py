import time

def mostrar_menu_pacientes():
    """Submenú para pacientes con diseño mejorado"""
    while True:
        # Marco decorativo
        print("╔══════════════════════════════════════════╗")
        print("║         🏥 MÓDULO DE PACIENTES 🏥         ║")
        print("╠══════════════════════════════════════════╣")
        print("║                                          ║")
        print("║  1. 🗓  Ver mis turnos                   ║")
        print("║  2. 🕒 Agendar nuevo turno               ║")
        print("║  3. ↩️  Volver al menú principal         ║")
        print("║                                          ║")
        print("╚══════════════════════════════════════════╝")
        
        opcion = input("➤ Seleccione una opción [1-3]:")
        
        if opcion == "1":
            print("\n" + " " * 15 + "🔨 Función en construcción...")
            input("\n" + " " * 10 + "⏎ Presione Enter para continuar...")
        elif opcion == "2":
            print("\n" + " " * 15 + "🔨 Función en construcción...")
            input("\n" + " " * 10 + "⏎ Presione Enter para continuar...")
        elif opcion == "3":
            break
        else:
            print("\n" + " " * 10 + "⚠️  Opción inválida! Intente nuevamente")
            time.sleep(1)

if __name__ == "__main__":
    mostrar_menu_pacientes()