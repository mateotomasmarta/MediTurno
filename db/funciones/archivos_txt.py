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
            archivo.write('\t'.join(str(x) for x in turno) + '\n')

matriz_turnos = cargar_turnos()