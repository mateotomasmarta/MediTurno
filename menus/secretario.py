import time
from funciones.secretario.login import validar_credenciales
from utils.auxiliares import buscar_por_dni, buscar_por_nombre_o_apellido
from funciones.secretario.agenda import (
    mostrar_turnos_disponibles_secretaria,
    mostrar_turnos_ocupados,
    mostrar_todos_turnos,
    imprimir_turno_por_dni
)
from funciones.secretario.gestion import (
    vaciar_turno,
    elegir_turno_a_modificar,
    elegir_dia,
    modifica_turno
)
from funciones.secretario.facturacion import (
    imprimir_facturas_por_dni,
    imprimir_todas_las_facturas_ordenadas,
    cierre_total_con_detalle
)


def mostrar_menu_secretaria():
    """Menú de secretaría con sistema de login"""
    while True:
        print("╔══════════════════════════════════════════╗")
        print("║        🔐 ACCESO SECRETARÍA 🔐           ║")
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
        print("║  3. 💰 Facturación                       ║")
        print("║  4. ↩️  Volver al menú principal          ║")
        print("║                                          ║")
        print("╚══════════════════════════════════════════╝")

        opcion = input("➤ Seleccione una opción [1-4]: ")

        if opcion == "1":
            gestionar_pacientes()
        elif opcion == "2":
            gestionar_turnos()
        elif opcion == "3":
            menu_facturacion()
        elif opcion == "4":
            break
        else:
            print("\n⚠️ Opción inválida!")
            time.sleep(1)


def gestionar_pacientes():
    while True:
        print("╔══════════════════════════════════════════╗")
        print("║        📋 GESTIONAR PACIENTES            ║")
        print("╠══════════════════════════════════════════╣")
        print("║                                          ║")
        print("║  1. 📋 Buscar por DNI                    ║")
        print("║  2. 📋 Buscar por Nombre o Apellido      ║")
        print("║  3. ↩️ Volver al menú principal           ║")
        print("║                                          ║")
        print("╚══════════════════════════════════════════╝")

        opcion_paciente = input("➤ Seleccione una opción [1-3]: ")

        if opcion_paciente == "1":
            dni = input("📋 Ingrese el DNI del paciente: ")
            resultados = buscar_por_dni(dni)
            imprimir_resultados_busqueda(resultados)
        elif opcion_paciente == "2":
            filtro = input("📋 Ingrese el nombre o apellido del paciente: ")
            resultados = buscar_por_nombre_o_apellido(filtro)
            imprimir_resultados_busqueda(resultados)
        elif opcion_paciente == "3":
            break
        else:
            print("\n⚠️ Opción inválida!")
            time.sleep(1)


def imprimir_resultados_busqueda(resultados):
    if resultados:
        for i, paciente in enumerate(resultados, 1):
            print(" " * 10 + f"\n🧑 Paciente #{i}:")
            print(" " * 12 + f"├─ Nombre: {paciente['nombre']}")
            print(" " * 12 + f"├─ Apellido: {paciente['apellido']}")
            print(" " * 12 + f"├─ Edad: {paciente['edad']} años")
            print(" " * 12 + f"└─ DNI: {paciente['dni']}")
            print(" " * 12 + f"└─ Mail: {paciente['mail']}")
    else:
        print("\n" + " " * 10 + "⚠️ No se encontraron resultados.")
    opcion = input("➤ Desea realizar otra búsqueda? (s/n): ").lower()
    if opcion != "s":
        return


def gestionar_turnos():
    while True:
        print("\n" + "═" * 70)
        print("📊 TODOS LOS TURNOS")
        mostrar_todos_turnos()

        print("\n╔══════════════════════════════════════════╗")
        print("║        🛠️ GESTIONAR TURNOS                ║")
        print("╠══════════════════════════════════════════╣")
        print("║                                          ║")
        print("║  1. ✏️ Modificar un turno                 ║")
        print("║  2. 🗑️ Eliminar un turno                  ║")
        print("║  3. 📅 Filtrar turnos                    ║")
        print("║  4. ↩️ Volver al menú principal           ║")
        print("║                                          ║")
        print("╚══════════════════════════════════════════╝")

        opcion_turno = input("➤ Seleccione una opción [1-4]: ")

        if opcion_turno == "1":
            mostrar_turnos_ocupados()
            turno_a_modificar = elegir_turno_a_modificar()
            turnos_disponibles = mostrar_turnos_disponibles_secretaria()
            dia = elegir_dia(turnos_disponibles)
            modifica_turno(turno_a_modificar, dia)
        elif opcion_turno == "2":
            dni = input("📋 Ingrese el DNI del paciente: ")
            imprimir_turno_por_dni(dni)
            vaciar_turno()
        elif opcion_turno == "3":
            filtrar_turnos()
        elif opcion_turno == "4":
            break
        else:
            print("\n⚠️ Opción inválida!")
            time.sleep(1)


def filtrar_turnos():
    while True:
        print("╔══════════════════════════════════════════╗")
        print("║        📅 FILTRAR TURNOS                 ║")
        print("╠══════════════════════════════════════════╣")
        print("║                                          ║")
        print("║  1. 📅 Filtrar por ocupados              ║")
        print("║  2. 📅 Filtrar por disponibles           ║")
        print("║  3. ↩️ Volver al menú principal           ║")
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


def menu_facturacion():
    while True:
        print("╔══════════════════════════════════════════╗")
        print("║           💳 MENÚ FACTURACIÓN            ║")
        print("╠══════════════════════════════════════════╣")
        print("║                                          ║")
        print("║  1. 🧾 Ver facturas por paciente         ║")
        print("║  2. 📑 Ver todas las facturas            ║")
        print("║  3. 🔒 Cerrar caja                       ║")
        print("║  4. ↩️ Volver al menú principal          ║")
        print("║                                          ║")
        print("╚══════════════════════════════════════════╝")

        try:
            opcion_factura = input("➤ Seleccione una opción [1-4]: ")

            if opcion_factura == "1":
                dni = input("Ingrese el DNI del paciente: ").strip()
                imprimir_facturas_por_dni(dni)
                input("\nPresione ENTER para continuar...")

            elif opcion_factura == "2":
                imprimir_todas_las_facturas_ordenadas("db/facturacion.json")

            elif opcion_factura == "3":
                print("🔐 Cerrando caja (total general)...")
                total = cierre_total_con_detalle("db/facturacion.json")
                if total == 0:
                    print("⚠️ No hay facturas o no se pudo abrir el archivo.")
                else:
                    print(f"✅ Caja cerrada exitosamente")

            elif opcion_factura == "4":
                break
            else:
                print("⚠️ Opción inválida. Intente nuevamente.")

        except Exception as e:
            print(f"❌ Error inesperado en el menú de facturación: {e}")


if __name__ == "__main__":
    mostrar_menu_secretaria()