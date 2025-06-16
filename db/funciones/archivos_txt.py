RUTA_TURNOS = "db/turnos.txt"

def cargar_turnos():
    """
    Carga los turnos desde el archivo 'db/turnos.txt' y los devuelve como una matriz.
    Si el archivo no existe, retorna una lista vacía.
    """
    try:
        with open('db/turnos.txt', 'r', encoding='utf-8') as f:
            matriz = []
            for linea in f:
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
            return matriz
    except FileNotFoundError:
        return []

def guardar_turnos(matriz_turnos, path="db/turnos.txt"):
    with open(path, "w", encoding="utf-8") as archivo:
        for turno in matriz_turnos:
            archivo.write('\t'.join(str(x) for x in turno) + '\n') #serializacion

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
