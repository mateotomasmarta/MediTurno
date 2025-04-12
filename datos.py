matriz_pacientes =[
            {
                'id': 1,
                'dni': '30123456',
                'nombre': 'Ana',
                'apellido': 'Gómez',
                'telefono': '3515551234',
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
        ]

matriz_pacientes =[
            {
                'id': 1,
                'dni': '30123456',
                'nombre': 'Ana',
                'apellido': 'Gómez',
                'telefono': '3515551234',
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
        ]

matriz_turnos = [
        # Día 1
        {'id': 1, 'dia': 'lunes', 'hora': '08:00', 'paciente_id': 1, 'estado': 'disponible'},
        {'id': 2, 'dia': 'lunes', 'hora': '09:00', 'paciente_id': None, 'estado': 'disponible'},
        {'id': 3, 'dia': 'lunes', 'hora': '10:00', 'paciente_id': None, 'estado': 'disponible'},
        {'id': 4, 'dia': 'lunes', 'hora': '11:00', 'paciente_id': 2, 'estado': 'disponible'},
        {'id': 5, 'dia': 'lunes', 'hora': '16:00', 'paciente_id': None, 'estado': 'disponible'},
        
        # Día 2
        {'id': 6, 'dia': 'miércoles', 'hora': '08:00', 'paciente_id': None, 'estado': 'disponible'},
        {'id': 7, 'dia': 'miércoles', 'hora': '09:00', 'paciente_id': 2, 'estado': 'disponible'},
        {'id': 8, 'dia': 'miércoles', 'hora': '10:00', 'paciente_id': 3, 'estado': 'disponible'},
        {'id': 9, 'dia': 'miércoles', 'hora': '11:00', 'paciente_id': None, 'estado': 'disponible'},
        {'id': 10, 'dia': 'miércoles', 'hora': '16:00', 'paciente_id': None, 'estado': 'disponible'},
        
        # Día 3
        {'id': 11, 'dia': 'viernes', 'hora': '08:00', 'paciente_id': None, 'estado': 'disponible'},
        {'id': 12, 'dia': 'viernes', 'hora': '09:00', 'paciente_id': 1, 'estado': 'disponible'},
        {'id': 13, 'dia': 'viernes', 'hora': '10:00', 'paciente_id': None, 'estado': 'disponible'},
        {'id': 14, 'dia': 'viernes', 'hora': '11:00', 'paciente_id': None, 'estado': 'disponible'},
        {'id': 15, 'dia': 'viernes', 'hora': '16:00', 'paciente_id': 3, 'estado': 'disponible'}
    ]

matriz_secretario =[
            {
                'id': 1,
                'usuario': 'admin',
                'password': 'admin123',  # En producción usaría hashing
            }
    ]

