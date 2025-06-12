
import re

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

def pedir_mail():
    patron_mail = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    while True:
        mail = input("Ingresá tu correo electrónico: ").strip()
        if re.match(patron_mail, mail):
            return mail
        else:
            print("❌ El correo electrónico ingresado no es válido. Intentá nuevamente.")



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

def validar_turno_disponible(dia_turno, hora_turno, matriz_turnos):
    turno_valido = False  
    for i in range(len(matriz_turnos)):
        id_turno, dia, hora, id_paciente_turno, estado, id_doctor = matriz_turnos[i]
        if dia == dia_turno and hora == hora_turno:
            if estado == 'disponible':
                turno_valido = True 
                print(f"Turno disponible: {dia_turno} a las {hora_turno}")
            else:
                print(f"Lo siento, el turno para {dia_turno} a las {hora_turno} ya está ocupado.")
            break 

    if not turno_valido:
        print(f"No se encontró un turno disponible para el día {dia_turno} y la hora {hora_turno}.")
    return turno_valido

def validar_si_no():
    while True:
        respuesta = input("Por favor ingresa 'si' o 'no' (sin comillas): ").strip().lower()  # Se normaliza a minúsculas
        if respuesta == "si" or respuesta == "no":  
            return respuesta  
        else:
            print("⚠️ Respuesta inválida. Por favor, ingresa solo 'si' o 'no'.")
