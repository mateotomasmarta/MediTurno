from utils.validaciones import validar_edad, validar_dni
from utils.auxiliares import generar_nuevo_id
from db.funciones.archivos_json import cargar_archivo_pacientes,guardar_archivo_pacientes
import json
RUTA_PACIENTES = 'db/datos.json'

def tomar_nombre():
    bandera = True
    while bandera:
        try:
            entrada = input("Ingresá solo tu primer nombre y primer apellido: ").strip()
            partes = entrada.split()

            if len(partes) != 2:
                print("⚠️ Tenés que ingresar un solo *nombre y apellido*, nada más.")
            else:
                nombre, apellido = partes

                if not (nombre.isalpha() and apellido.isalpha()):
                    print("⚠️ El nombre y apellido solo deben tener letras.")
                else:
                    nombre_formateado = nombre.capitalize()
                    apellido_formateado = apellido.capitalize()
                    bandera = False
                    return nombre_formateado, apellido_formateado
        except Exception as e:
            print(f"⚠️ Ocurrió un error inesperado: {e}")

def lista_registro():
    """lista_nuevo: [id, dni, nombre, apellido, edad]"""
    lista_nuevo = []
    print("=" * 70)
    print("BIENVENIDO! Te pediremos tus datos para registrarte como paciente")
    print("=" * 70)

    try:
        pacientes = cargar_archivo_pacientes(RUTA_PACIENTES)
        dni = validar_dni()  
        lista_nuevo.append(dni) 
        nombre, apellido = tomar_nombre()  
        lista_nuevo.append(nombre)  
        lista_nuevo.append(apellido)  

        edad = validar_edad() 
        lista_nuevo.append(edad)  

        id = generar_nuevo_id()  # Ahora generar_nuevo_id debe leer del JSON
        lista_nuevo.insert(0, id)  
        return lista_nuevo  
    except Exception as e:
        print(f"⚠️ Ocurrió un error durante el registro: {e}")
        return None

def registrar_paciente():
    """Maneja el proceso de registro de nuevos pacientes"""
    print("\n" + "═" * 50)
    print("📝 REGISTRO DE NUEVO PACIENTE")
    print("═" * 50)
    
    try:
        nuevo_paciente = lista_registro()  
        if not nuevo_paciente:
            print("⚠️ No se pudo completar el registro.")
            return None
        
        claves = ['id', 'dni', 'nombre', 'apellido', 'edad']
        nuevo_diccionario = dict(zip(claves, nuevo_paciente)) 
        
        pacientes = cargar_archivo_pacientes(RUTA_PACIENTES)
        for paciente in pacientes:
            if paciente['dni'] == nuevo_diccionario['dni']:
                print(f"⚠️ Ya existe un paciente registrado con el DNI {nuevo_diccionario['dni']}. No se puede registrar nuevamente.")
                return None  
        
        pacientes.append(nuevo_diccionario)
        guardar_archivo_pacientes(pacientes)

        print(f"\n✅ Registro exitoso! Bienvenido/a {nuevo_diccionario['nombre']} {nuevo_diccionario['apellido']}")
        print("⚠️ Porfavor inicie sesion con su DNI para acceder al sistema.")
        print("🔙 Volviendo al menú de login...")
        return nuevo_diccionario
    except Exception as e:
        print(f"⚠️ Ocurrió un error inesperado durante el registro: {e}")
        return None