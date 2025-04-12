import time

def mostrar_menu_secretaria():
    """Submenú para secretaría con diseño mejorado"""
    while True:
        try:
            print("\033[H\033[J", end="")
            print("""
   ___      _      _             _       
  / __| ___| |_ __| |__ _ _ __ (_)__ ___
 | (__ / _ \  _/ _` / _` | '  \| / _(_-<
  \___|\___/\__\__,_\__,_|_|_|_|_\__/__/
        """)
            
            # Marco decorativo
            print("╔══════════════════════════════════════════╗")
            print("║        📋 MÓDULO DE SECRETARÍA 📋         ║")
            print("╠══════════════════════════════════════════╣")
            print("║                                          ║")
            print("║  1. 👥 Gestionar Pacientes               ║")
            print("║  2. 📅 Gestionar Turnos                  ║")
            print("║  3. ↩️  Volver al menú principal         ║")
            print("║                                          ║")
            print("╚══════════════════════════════════════════╝")
            
            
            opcion = input("\n" + " " * 10 + "➤ Seleccione una opción [1-3]:")
            
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
                
        except KeyboardInterrupt:
            print("\n\n" + " " * 15 + "🚨 Volviendo al menú principal...")
            time.sleep(1)
            break

if __name__ == "__main__":
    mostrar_menu_secretaria()