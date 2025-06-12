<<<<<<< HEAD
<<<<<<< HEAD
matriz_pacientes =[
            {
                'id': 1,
                'dni': '30123456',
                'nombre': 'Ana',
                'apellido': 'Gómez',
                'edad': 28
            },
            {
                'id': 2,
                'dni': '28987654',
                'nombre': 'Carlos',
                'apellido': 'López',
                'edad': 35
            },
            {
                'id': 3,
                'dni': '35123456',
                'nombre': 'María',
                'apellido': 'Sánchez',
                'edad': 42

            }
            {
                'id': 4,
                'dni': '53233456',
                'nombre': 'Lautaro',
                'apellido': 'Gomez',
                'edad': 5

            }
{
                'id': 5,
                'dni': '49090334',
                'nombre': 'Lucia',
                'apellido': 'Fernandez',
                'edad': 13

            }
        ]


# ID TURNO -- DIA -- HORARIO -- ID PACIENTE -- ESTADO -- ID DOCTOR
matriz_turnos = [
            [1, 'lunes', '08:00', 1, 'ocupado', 1],
            [2, 'lunes', '09:00', , 'disponible', None],
            [3, 'lunes', '10:00', None, 'disponible', None],
            [4, 'lunes', '13:00', 5, 'ocupado', 2],
            [5, 'lunes', '16:00', None, 'disponible', None],
            [6, 'miércoles', '18:00', None, 'disponible', None],

            [7, 'miércoles', '08:00', 2, 'ocupado', 1],
            [8, 'miércoles', '09:00', 3, 'ocupado', 1],
            [9, 'miércoles', '10:00', None, 'disponible', None],
            [10, 'miércoles', '11:00', None, 'disponible', None],
            [11, 'viernes', '13:00', None, 'disponible', None],
            [12, 'viernes', '15:00', 4, 'ocupado', 2],
            
            [13, 'viernes', '09:00', None, 'disponible', None],
            [14, 'viernes', '11:00', None, 'disponible', None],
            [15, 'viernes', '13:00', 5, 'ocupado', 2],
            [16, 'viernes', '15:00', 2, 'ocupado', 1],
            [17, 'viernes', '16:00', None, 'disponible', None],
            [18, 'viernes', '18:00', None, 'disponible', None],
            
]

secretaria = ("admin", "admin123"),

# ID DOCTOR -- NOMBRE -- ESPECIALIDAD -- SALA
matriz_medicos = [
    [1, 'Dr. Juan Russo', 'Guaría', 'Sala 1'],
    [1, 'Dra. Ana Brizuela', 'Pediatría', 'Sala 2']
]
=======
# Estructura: ID_TURNO, DIA, HORARIO, ID_PACIENTE, ESTADO, ID_DOCTOR
matriz_turnos = [
    [1, 'lunes', '08:00', 1, 'ocupado', 1],
    [2, 'lunes', '09:00', None, 'disponible', None],
    [3, 'lunes', '10:00', None, 'disponible', None],
    [4, 'lunes', '13:00', 5, 'ocupado', 2],
    [5, 'lunes', '16:00', None, 'disponible', None],
    [6, 'miércoles', '18:00', None, 'disponible', None],
    [7, 'miércoles', '08:00', 2, 'ocupado', 1],
    [8, 'miércoles', '09:00', 3, 'ocupado', 1],
    [9, 'miércoles', '10:00', None, 'disponible', None],
    [10, 'miércoles', '11:00', None, 'disponible', None],
    [11, 'viernes', '13:00', None, 'disponible', None],
    [12, 'viernes', '15:00', 4, 'ocupado', 2],
    [13, 'viernes', '09:00', None, 'disponible', None],
    [14, 'viernes', '11:00', None, 'disponible', None],
    [15, 'viernes', '13:00', 5, 'ocupado', 2],
    [16, 'viernes', '15:00', 2, 'ocupado', 1],
    [17, 'viernes', '16:00', None, 'disponible', None],
    [18, 'viernes', '18:00', None, 'disponible', None]
]
=======

>>>>>>> origin/main

secretaria = ("admin", "admin123")

# Estructura: ID_DOCTOR, NOMBRE, ESPECIALIDAD, SALA
matriz_medicos = [
    [1, 'Dr. Juan Russo', 'Guardia', 'Sala 1'],
    [2, 'Dra. Ana Brizuela', 'Pediatría', 'Sala 2']
]
>>>>>>> origin/main
