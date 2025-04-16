from datos import matriz_pacientes, matriz_turnos

def buscar_paciente():
    while True:
        #Comienza un bloque que "try" ejecutar el código. Si hay un error, se salta al bloque except.
        try:
            print("\nBUSCAR PACIENTE")
            print("1. Buscar por DNI")
            print("2. Buscar por Apellido")
            print("3. Volver al menú principal")

        #Guarda la opción ingresada por el usuario. .strip() elimina espacios al principio o al final por si los escribió sin querer.
            opcion = input("Elegí una opción: ").strip()

            if opcion == "1":
                #Si eligió la opción 1, le pedimos el DNI.
                dni = input("Ingresá el DNI del paciente: ").strip()
                #Verificamos que el DNI sea solo números. Si no lo es, se muestra un mensaje y se vuelve al inicio del menú.
                if not dni.isdigit():
                    print("El DNI debe ser numérico.")
                    continue

                 #Creamos una lista vacía para guardar los pacientes encontrados.
                pacientes_encontrados = []
                for paciente in matriz_pacientes:
                    #Recorremos cada paciente de la matriz.
                    if paciente['dni'] == dni:
                        #Si el DNI coincide con el ingresado, lo agregamos a la lista.
                        pacientes_encontrados.append(paciente)

            elif opcion == "2":
                #Si eligió la opción 2, le pedimos el apellido y lo pasamos a minúscula
                apellido = input("Ingresá el apellido del paciente: ").strip().lower()
                #Si no escribió nada, mostramos un mensaje y volvemos al menú.
                if apellido == "":
                    print("El apellido no puede estar vacío.")
                    continue

                pacientes_encontrados = []
                #Recorremos la matriz de pacientes. Si el apellido coincide (en minúsculas), se guarda en la lista de encontrados.
                for paciente in matriz_pacientes:
                    if paciente['apellido'].lower() == apellido:
                        pacientes_encontrados.append(paciente)

            elif opcion == "3":
                #Sale del bucle while y vuelve al menú principal.
                break
            #Si se escribió otra cosa que no era "1", "2" o "4", se muestra un mensaje y se vuelve al menú.
            else:
                print("Opción inválida.")
                continue

            if not pacientes_encontrados:
                print("No se encontró ningún paciente con esos datos.")
            else:
                #Si hay pacientes encontrados, mostramos sus datos uno por uno.
                for paciente in pacientes_encontrados:
                    print("Nombre:", paciente['nombre'])
                    print("Apellido:", paciente['apellido'])
                    print("DNI:", paciente['dni'])
                    print("Edad:", paciente['edad'])
                    print("Turnos asignados:")
                    
                    #Recorremos los turnos y si alguno tiene el mismo paciente_id, lo mostramos y marcamos que sí tiene turnos.
                    tiene_turnos = False
                    for turno in matriz_turnos:
                        if turno['paciente_id'] == paciente['id']:
                            print("-", turno['dia'], turno['hora'])
                            tiene_turnos = True
                   #Si no se encontraron turnos, se avisa.
                    if not tiene_turnos:
                        print("No tiene turnos asignados.")
       #Si en todo el proceso ocurre un error inesperado, se muestra el mensaje 
        except Exception as e:
            print("Ocurrió un error:", e)

