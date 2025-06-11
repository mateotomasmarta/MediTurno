import sys
import time
from menus.paciente import mostrar_menu_pacientes
from menus.secretario import mostrar_menu_secretaria
from utils.archivo_turnos import cargar_turnos_desde_archivo, guardar_turnos_en_archivo

def cargar_turnos_desde_archivo(archprueba):
    matriz_turnos_nueva = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as arch:
            for linea in arch:
                datos = linea.strip().split("\t")  # Asumamos que los campos van tabulados
                if len(datos) == 6:  # ID, Día, Hora, ID Paciente, Estado, ID Médico
                    matriz_turnos.append([int(datos[0]), datos[1], datos[2], datos[3], datos[4], datos[5]])
    except FileNotFoundError:
        print("Archivo no encontrado, se crea matriz vacía")
    return matriz_turnos


def mostrar_menu_principal():
    global matriz_turnos
    matriz_turnos = cargar_turnos_desde_archivo(ARCHIVO_TURNOS)

    while True:
        print("╔══════════════════════════════════════════╗")
        print("║            💎 MENÚ PRINCIPAL 💎         ║")
        print("╠══════════════════════════════════════════╣")
        print("║                                          ║")
        print("║  1. 👨⚕️  Acceso Pacientes              ║")
        print("║  2. 👩💼 Acceso Secretaría              ║")
        print("║  3. 🔴 Salir del Sistema                ║")
        print("║                                          ║")
        print("╚══════════════════════════════════════════╝")

        opcion = input("➤➤➤ Seleccione una opción [1-3]: ")
        
        if opcion == "1":
            print("🔄 Cargando módulo de pacientes...")
            time.sleep(1)
            mostrar_menu_pacientes(matriz_turnos)  # PASÁS LA MATRIZ
            
        elif opcion == "2":
            print("🔄 Cargando módulo de secretaría...")
            time.sleep(1)
            mostrar_menu_secretaria(matriz_turnos)  # PASÁS LA MATRIZ
            
        elif opcion == "3":
            print("\n" + " " * 15 + "👋 Cerrando aplicación...")
            for i in range(3, 0, -1):
                print(f"{' '*15}⏳ Saliendo en {i}...")
                time.sleep(1)
            guardar_turnos_en_archivo(matriz_turnos, ARCHIVO_TURNOS)  # GUARDÁS TODO
            print(" " * 15 + "✅ Aplicación cerrada con éxito")
            time.sleep(1)
            sys.exit(0)
            
        else:
            print("⚠️  Opción inválida! Intente nuevamente")
            time.sleep(1)

if __name__ == "__main__":
    mostrar_menu_principal()
