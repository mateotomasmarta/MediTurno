import json
from db.funciones.archivos_json import cargar_archivo_pacientes, cargar_facturas
from utils.auxiliares import buscar_paciente

def imprimir_facturas_por_dni(dni, ruta_pacientes="db/datos.json", ruta_facturas="db/facturacion.json"):
    pacientes = cargar_archivo_pacientes(ruta_pacientes)
    facturas = cargar_facturas(ruta_facturas)
    paciente = buscar_paciente(dni, pacientes)

    if not paciente:
        print(f"No se encontró paciente con DNI {dni}.")
        return

    facturas_cliente = [f for f in facturas if int(f.get("id_paciente", -1)) == int(paciente["id"])]

    if not facturas_cliente:
        print(f"No hay facturas para el paciente {paciente.get('nombre', '')} {paciente.get('apellido', '')} (DNI: {dni})")
        return

    print("\n" + "="*60)
    print(f"FACTURAS DE: {paciente.get('nombre', '').upper()} {paciente.get('apellido', '').upper()} (DNI: {dni})".center(60))
    print("="*60)
    for f in facturas_cliente:
        dia = f.get("dia", "---")
        hora = f.get("hora", "---")
        print(f"| ID Factura: {str(f.get('id_factura', '')).ljust(6)} | Día: {str(dia).ljust(10)} | Hora: {str(hora).ljust(5)} | Importe: ${str(f['importe']).ljust(8)}|")
        print("-"*60)
    print(f"{'TOTAL':>50}: ${sum(f['importe'] for f in facturas_cliente)}")
    print("="*60)
def cierre_total_con_detalle(ruta):

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            facturas = json.load(archivo)
            # Si hay lista de listas, aplanar para manejarlos mejor
            if facturas and isinstance(facturas[0], list): #verifica si es una lista de listas
                facturas = facturas[0] #esto me sirve para tomar la primera lista de la lista de listas
            total_general = 0
            totales_por_dia = {}
            for factura in facturas:
                total_general += factura["importe"]
                dia = factura["dia"]
                totales_por_dia[dia] = totales_por_dia.get(dia, 0) + factura["importe"] #.get() devuelve el valor de la clave si existe, o 0 si no existe

            print("\n" + "="*50)
            print(f"{'CIERRE DE CAJA':^50}")
            print("="*50)
            for dia, total in totales_por_dia.items():
                print(f"Total generado el día {dia.capitalize():<10}: ${total}")
            print("-"*50)
            print(f"{'TOTAL GENERAL':<30}: ${total_general}")
            print("="*50)
            return total_general, totales_por_dia
    except Exception as e:
        print(f"No se puede abrir el archivo: {e}")
        return 0, {}



