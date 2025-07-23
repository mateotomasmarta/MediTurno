import os
import tempfile
import shutil


RUTA_TURNOS = "db/turnos.txt"

def cargar_turno_por_linea(num_linea, ruta=RUTA_TURNOS):
    """Carga una línea específica del archivo de turnos."""
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            for i, linea in enumerate(f, start=1):
                if i == num_linea:
                    datos = linea.strip().split('\t')
                    return [int(datos[0]), datos[1], datos[2],
                            int(datos[3]) if datos[3] != 'None' else None,
                            datos[4],
                            int(datos[5]) if datos[5] != 'None' else None]
    except Exception as e:
        print(f"⚠️ Error al cargar la línea {num_linea}: {e}")
    return None



def guardar_turno_por_linea(fila, num_linea, ruta=RUTA_TURNOS):

    try:
        # Crear archivo temporal en la misma carpeta
        dir_name = os.path.dirname(ruta)
        with tempfile.NamedTemporaryFile('w', delete=False, encoding='utf-8', dir=dir_name) as tmp:
            with open(ruta, 'r', encoding='utf-8') as original:
                for i, linea in enumerate(original, start=1):
                    if i == num_linea:
                        nueva_linea = "\t".join([
                            str(fila[0]), fila[1], fila[2],
                            str(fila[3]) if fila[3] is not None else 'None',
                            fila[4],
                            str(fila[5]) if fila[5] is not None else 'None'
                        ]) + "\n"
                        tmp.write(nueva_linea)
                    else:
                        tmp.write(linea)

        # Reemplazar el archivo original por el temporal
        shutil.move(tmp.name, ruta)

    except Exception as e:
        print(f"❌ Error al guardar la línea {num_linea}: {e}")


def iterar_turnos_disponibles(ruta=RUTA_TURNOS):
    """Iterador que devuelve turnos disponibles línea por línea."""
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            for linea in f:
                datos = linea.strip().split('\t')
                if len(datos) >= 6 and datos[4] == "disponible":
                    yield datos
    except FileNotFoundError:
        print("❌ Archivo de turnos no encontrado.")


def buscar_turno_por_dia_y_hora(dia, hora, ruta=RUTA_TURNOS):
    """Devuelve el número de línea del primer turno disponible con día y hora específicos."""
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            for i, linea in enumerate(f, start=1):
                datos = linea.strip().split('\t')
                if len(datos) >= 5 and datos[1] == dia and datos[2] == hora and datos[4] == "disponible":
                    return i
    except FileNotFoundError:
        print("❌ No se encontró el archivo de turnos.")
    return None

def obtener_medico_por_id(id_buscado):
    """Busca un médico por ID sin cargar toda la lista en memoria"""
    try:
        with open("db/medicos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                # Cambiar el separador según corresponda
                datos = linea.strip().split(",")  # Cambié \t por ,
                if int(datos[0]) == id_buscado:
                    return datos  # [id, nombre, apellido, especialidad]
    except FileNotFoundError:
        print("❌ No se encontró el archivo de médicos.")
    except ValueError:
        print("❌ Error: formato incorrecto en archivo de médicos.")
    return None


def iterar_todos_los_turnos(ruta=RUTA_TURNOS):
    """Iterador que devuelve todos los turnos (ocupados y disponibles) línea por línea."""
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                datos = linea.strip().split('\t')
                if len(datos) >= 6:
                    yield [
                        int(datos[0]),            # ID
                        datos[1],                 # Día
                        datos[2],                 # Hora
                        int(datos[3]) if datos[3] != 'None' else None,  # ID Paciente
                        datos[4],                 # Estado
                        int(datos[5]) if datos[5] != 'None' else None   # ID Doctor
                    ]
    except FileNotFoundError:
        print("❌ No se encontró el archivo de turnos.")
