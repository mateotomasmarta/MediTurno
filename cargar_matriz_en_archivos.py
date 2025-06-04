from datos import matriz_turnos
def cargar_matriz_en_archivos (matriz, archivo):
    try:
        lineas= [f"{ID_TURNO};{DIA};{HORARIO};{ID_PACIENTE};{ESTADO};{ID_DOCTOR}\n" for ID_TURNO, DIA, HORARIO, ID_PACIENTE, ESTADO, ID_DOCTOR in matriz]
        arch= open(archivo,"w", encoding="UTF-8")
        arch.writelines(lineas)
    except OSError as mensaje:
        print("no se puede grabar el archivo", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass

cargar_matriz_en_archivos(matriz_turnos , 'matrices.txt') 
