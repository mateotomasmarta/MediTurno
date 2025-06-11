from datos import matriz_turnos, matriz_medicos

def exportacion_datos(nombre_archivo):
    try:
        arch = open(nombre_archivo, "w", encoding="utf-8")
        
        arch.write("=== MÉDICOS ===\n")
        for medico in matriz_medicos:
            linea = "ID: " + str(medico[0]) + " - Nombre: " + medico[1] + " - Especialidad: " + medico[2] + " - Sala: " + medico[3] + "\n"
            arch.write(linea)
        
        arch.write("\n")  # Línea en blanco para separar secciones
        
        arch.write("=== TURNOS ===\n")
        for turno in matriz_turnos:
            linea = "ID Turno: " + str(turno[0]) + " - Día: " + turno[1] + " - Hora: " + turno[2] + " - ID Paciente: " + str(turno[3]) + " - Estado: " + turno[4] + " - ID Médico: " + str(turno[5]) + "\n"
            arch.write(linea)
        
        print("Archivo creado correctamente.")
    
    except OSError as e:
        print("No se puede grabar el archivo:", e)
    
    finally:
        try:
            arch.close()
        except NameError:
            pass

# Programa principal
exportar_datos("exportacion_datos.txt")


######## MATEO LEE ESTO:                        ###########################

#modulo con funciones de turnos traer la funcion y y como te retorna la matriz la sacas de ahi
def cargar_turnos_desde_archivo(nombre_archivo):
    matriz_turnos = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as arch:
            for linea in arch:
                datos = linea.strip().split("\t")  # Asumamos que los campos van tabulados
                if len(datos) == 6:  # ID, Día, Hora, ID Paciente, Estado, ID Médico
                    matriz_turnos.append([int(datos[0]), datos[1], datos[2], datos[3], datos[4], datos[5]])
    except FileNotFoundError:
        print("Archivo no encontrado, se crea matriz vacía")
    return matriz_turnos

def guardar_turnos_en_archivo(matriz_turnos, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as arch:
        for turno in matriz_turnos:
            linea = "\t".join(map(str, turno)) + "\n"
            arch.write(linea)

# Al iniciar el programa:
matriz_turnos = cargar_turnos_desde_archivo("turnos.txt")

# Trabajás con matriz_turnos: agregar, modificar, borrar

# Al terminar o cuando quieras guardar cambios:
guardar_turnos_en_archivo(matriz_turnos, "turnos.txt")

