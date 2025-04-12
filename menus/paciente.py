import time

def mostrar_menu_pacientes():
    """Submenú para pacientes con diseño mejorado"""
    while True:
        try:
            print("\033[H\033[J", end="")
            
            # Arte ASCII para el subtítulo
            print("""
   ___       _       _             
  / _ \__ _| |_ ___| |_ ___ _ __  
 / /_)/ _` | __/ __| __/ _ \ '_ \ 
/ ___/ (_| | |_\__ \ ||  __/ | | |
\/    \__,_|\__|___/\__\___|_| |_|
            """)
            
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
                
        except:
            break

if __name__ == "__main__":
    mostrar_menu_pacientes()