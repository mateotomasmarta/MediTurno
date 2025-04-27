from datos import matriz_turnos

def validar_dni():
    bandera = True
    while bandera == True:
        dni = input("Ingresá tu DNI (7 u 8 dígitos, solo números, sin guiones ni letras): ").strip()
        
        if not dni.isdigit():
            print("❌ El DNI debe contener solo números.")
        elif not (7 <= len(dni) <= 8):
            print("❌ El DNI debe tener entre 7 y 8 dígitos.")
        else:
            bandera = False
            return dni  


def pedir_dni():
    documento = input("ingresá tu DNI (importante respetar la cantidad de digitos y no agregar letras ni guiones): ")
    return documento

def validar_edad():
    while True:
        edad = input("Ingresá tu edad: ").strip()
        if edad.isdigit():
            edad = int(edad)
            if 0 < edad < 100:
                return edad
            else:
                print("⚠️ Ingresá una edad válida entre 1 y 100.")
        else:
            print("⚠️ La edad debe ser un número.")

def validar_turno_disponible(dia_turno, hora_turno):
    turno_valido = False  
    # Compara el día y la hora con los datos de la matriz de turnos
    for i in range(len(matriz_turnos)):
        # Desempaquetamos la fila de la matriz para obtener los valores
        id_turno, dia, hora, id_paciente_turno, estado, id_doctor = matriz_turnos[i]
        # Compara si el día y la hora coinciden con los ingresados por el paciente
        if dia == dia_turno and hora == hora_turno:
            # Verifica si el turno está disponible
            if estado == 'disponible':
                turno_valido = True # El turno es válido y disponible
                print(f"Turno disponible: {dia_turno} a las {hora_turno}")
            else:
                # El turno está ocupado
                print(f"Lo siento, el turno para {dia_turno} a las {hora_turno} ya está ocupado.")
            break  # Ya encontramos el turno, no es necesario seguir buscando

    # Si no se encontró un turno válido, informamos al paciente
    if not turno_valido:
        print(f"No se encontró un turno disponible para el día {dia_turno} y la hora {hora_turno}.")
    
    return turno_valido

def validar_si_no():
    while True:
        respuesta = input("Por favor ingresa 'si' o 'no' (sin comillas): ").strip().lower()  # Se normaliza a minúsculas
        if respuesta == "si" or respuesta == "no":  # Validamos si es "si" o "no"
            return respuesta  # Si es válido, lo retornamos
        else:
            print("⚠️ Respuesta inválida. Por favor, ingresa solo 'si' o 'no'.")
