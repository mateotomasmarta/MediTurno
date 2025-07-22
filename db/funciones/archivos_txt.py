RUTA_TURNOS = "db/turnos.txt"

def cargar_turnos_generico():
    """
    Carga los turnos desde el archivo 'db/turnos.txt' y los devuelve como una matriz.
    Usa readline() para leer línea por línea.
    Si el archivo no existe, retorna una lista vacía.
    """
    matriz = []
    try:
        with open('db/turnos.txt', 'r', encoding='utf-8') as f:
            linea = f.readline()
            while linea:
                elementos = linea.strip().split('\t')
                fila = []
                for elem in elementos:
                    if elem == 'None':
                        fila.append(None)
                    elif elem.isdigit():
                        fila.append(int(elem))
                    else:
                        fila.append(elem)
                matriz.append(fila)
                linea = f.readline()
        return matriz
    except FileNotFoundError:
        return []


def guardar_turnos_generico(matriz_turnos, path="db/turnos.txt"):
    with open(path, "w", encoding="utf-8") as archivo:
        for turno in matriz_turnos:
            fila_serializada = []
            for elem in turno:
                if elem is None:
                    fila_serializada.append("None")
                else:
                    fila_serializada.append(str(elem))
            archivo.write('\t'.join(fila_serializada) + '\n')


def cargar_turno_por_linea(num_linea, path="db/turnos.txt"):
    """
    Lee una línea específica del archivo y devuelve la lista con los datos serializados/deserializados.
    num_linea: índice empezando en 1 (primera línea es línea 1)
    """
    with open(path, "r", encoding="utf-8") as archivo:
        for i in range(num_linea - 1):
            archivo.readline()  # descartamos líneas anteriores
        
        linea = archivo.readline()
        if not linea:
            return None  # si la línea no existe
        
        elementos = linea.strip().split('\t')
        fila = []
        for elem in elementos:
            if elem == "None":
                fila.append(None)
            elif elem.isdigit():
                fila.append(int(elem))
            else:
                fila.append(elem)
        return fila
import os

def guardar_turno_por_linea(nueva_fila, num_linea, path="db/turnos.txt"):
    """
    Modifica la línea `num_linea` en el archivo con los datos de `nueva_fila`.
    Si la línea no existe, no hace nada.
    """
    ruta_temp = path + ".tmp"
    
    with open(path, "r", encoding="utf-8") as archivo_original, \
         open(ruta_temp, "w", encoding="utf-8") as archivo_temp:
        
        for i, linea in enumerate(archivo_original, start=1):
            if i == num_linea:
                # Serializamos nueva_fila para escribir
                fila_serializada = []
                for elem in nueva_fila:
                    if elem is None:
                        fila_serializada.append("None")
                    else:
                        fila_serializada.append(str(elem))
                archivo_temp.write('\t'.join(fila_serializada) + '\n')
            else:
                archivo_temp.write(linea)
    
    os.replace(ruta_temp, path)



matriz_turnos = cargar_turnos()

def cargar_medicos(path="db/medicos.txt"):
    matriz_medicos = []
    with open(path, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            if len(partes) == 4:
                partes[0] = int(partes[0])  # Convierte el ID a entero
                matriz_medicos.append(partes)
    return matriz_medicos

def buscar_medico_por_id(id_medico, path="db/medicos.txt"):
    """Busca un médico por su ID y retorna la lista con sus datos, o None si no existe."""
    medicos = cargar_medicos(path)
    for medico in medicos:
        if medico[0] == id_medico:
            return medico
    return None

def buscar_medico_por_nombre(nombre, path="db/medicos.txt"):
    """Busca médicos por nombre (parcial o completo, insensible a mayúsculas/minúsculas)."""
    medicos = cargar_medicos(path)
    resultado = []
    for medico in medicos:
        if nombre.lower() in medico[1].lower():
            resultado.append(medico)
    return resultado

matriz_medicos = cargar_medicos()
