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

secretaria = ("admin", "admin123")

# Estructura: ID_DOCTOR, NOMBRE, ESPECIALIDAD, SALA
matriz_medicos = [
    [1, 'Dr. Juan Russo', 'Guardia', 'Sala 1'],
    [2, 'Dra. Ana Brizuela', 'Pediatría', 'Sala 2']
]