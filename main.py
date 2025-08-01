import sys
import time
from menus.paciente import mostrar_menu_pacientes
from menus.secretario import mostrar_menu_secretaria
from db.funciones.archivos_txt import cargar_turno_por_linea, buscar_turno_por_dia_y_hora, iterar_turnos_disponibles



def mostrar_menu_principal():
    
    while True:
        print("╔══════════════════════════════════════════╗")
        print("║            💎 MENÚ PRINCIPAL 💎          ║")
        print("╠══════════════════════════════════════════╣")
        print("║                                          ║")
        print("║  1. 👨⚕️  Acceso Pacientes                ║")
        print("║  2. 👩💼 Acceso Secretaría               ║")
        print("║  3. 🔴 Salir del Sistema                 ║")
        print("║                                          ║")
        print("╚══════════════════════════════════════════╝")

        opcion = input("➤➤➤ Seleccione una opción [1-3]: ")
        
        if opcion == "1":
            print("🔄 Cargando módulo de pacientes...")
            time.sleep(1)
            mostrar_menu_pacientes()  # Pasamos los turnos como parámetro
            
        elif opcion == "2":
            print("🔄 Cargando módulo de secretaría...")
            time.sleep(1)
            mostrar_menu_secretaria()  # Pasamos los turnos como parámetro
            
        elif opcion == "3":
            print("\n" + " " * 15 + "👋 Cerrando aplicación...")
            for i in range(3, 0, -1):
                print(f"{' '*15}⏳ Saliendo en {i}...")
                time.sleep(1)
            print(" " * 15 + "✅ Aplicación cerrada con éxito")
            time.sleep(1)
            sys.exit(0)
            
        else:
            print("⚠️  Opción inválida! Intente nuevamente")
            time.sleep(1)

if __name__ == "__main__":
    mostrar_menu_principal()  # Cargar turnos al iniciar