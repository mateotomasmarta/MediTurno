from db.funciones.archivos_txt import cargar_turno_por_linea, guardar_turno_por_linea


def vaciar_turno():
    try:
        turno_vaciar = int(input("Ingrese el ID del turno a vaciar: "))
        fila = cargar_turno_por_linea(turno_vaciar)
        if fila:
            fila[3] = None
            fila[4] = 'disponible'
            fila[5] = None
            guardar_turno_por_linea(fila, turno_vaciar)
            print(f"✅ Turno con ID {turno_vaciar} marcado como disponible.")
        else:
            print(f"⚠️ No se encontró un turno con el ID {turno_vaciar}.")
    except ValueError:
        print("⚠️ Debe ingresar un número válido para el ID del turno.")
    except Exception as e:
        print(f"⚠️ Ocurrió un error inesperado: {e}")


def elegir_turno_a_modificar():
    while True:
        try:
            id_turno = int(input("Ingrese la ID del turno que desea modificar: "))
            fila = cargar_turno_por_linea(id_turno)
            if fila and fila[4] == 'ocupado':
                print(f"\nEl turno que desea cambiar es {fila}")
                return id_turno
            print("⚠️ No se encontró un turno ocupado con esa ID.")
        except ValueError:
            print("⚠️ Debe ingresar un número válido para la ID del turno.")
        except Exception as e:
            print(f"⚠️ Ocurrió un error inesperado: {e}")


def elegir_dia(turnos_disponibles):
    bandera = True
    while bandera:
        try:
            print("")
            dia_id = int(input("Ingrese el número de la ID del turno que desea elegir para la modificación: "))
            for turno in turnos_disponibles:
                if turno[0] == dia_id:
                    bandera = False
                    return dia_id
            print("⚠️ No se encontró un turno con esa ID. Intente de nuevo.")
        except ValueError:
            print("⚠️ Debe ingresar un número válido para la ID del turno.")
        except Exception as e:
            print(f"⚠️ Ocurrió un error inesperado: {e}")



def modifica_turno(id_origen, id_destino):
    try:
        turno_origen = cargar_turno_por_linea(id_origen)
        turno_destino = cargar_turno_por_linea(id_destino)

        if not turno_origen or not turno_destino:
            print("❌ No se encontraron los turnos especificados.")
            return

        if turno_origen[4] != 'ocupado' or turno_destino[4] != 'disponible':
            print("❌ Validación de estado fallida (origen debe ser ocupado y destino disponible).")
            return

        # Transferencia
        turno_destino[3] = turno_origen[3]
        turno_destino[4] = turno_origen[4]
        turno_destino[5] = turno_origen[5]

        # Liberar el original
        turno_origen[3] = None
        turno_origen[4] = 'disponible'
        turno_origen[5] = None

        guardar_turno_por_linea(turno_destino, id_destino)
        guardar_turno_por_linea(turno_origen, id_origen)

        print("✅ El turno ha sido modificado correctamente.")

    except Exception as e:
        print(f"❌ Error al modificar el turno: {e}")
