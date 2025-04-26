from datos import matriz_medicos, matriz_pacientes


def vaciar_turno(matriz):

    turno_vaciar = int(input("Ingrese el ID del turno a vaciar: "))
    for i in range(len(matriz)):
        if matriz[i][0] == turno_vaciar:  # Busca el turno por ID
            matriz[i][3] = None  # Elimina el ID del paciente
            matriz[i][4] = 'disponible'  # Cambia el estado a disponible
            matriz[i][5] = None  # Elimina el ID del doctor
            print(f"✅ Turno con ID {turno_vaciar} marcado como disponible.")
            return
    print(f"⚠️ No se encontró un turno con el ID {turno_vaciar}.")
            
    








