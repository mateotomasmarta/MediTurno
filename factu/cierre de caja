import json

def mostrar_total(ruta, tot):
    try:
        archivo= open(ruta, "r", encoding="utf-8")
        facturas= json.load(archivo)
        
        for factura in facturas:

                print(f'ID FACTURA: {factura["id_factura"]} ID PACIENTE {factura["id_paciente"]} ID TURNO {factura["id_turno"]} DIA {factura["dia"]} HORA {factura["hora"]} IMPORTE {factura["importe"]}')
                print("")

              
                print("*" * 50)
                print(f"El total del es: {tot}")

    except:
        
        print("no se puede abrir")

    finally:
        try:
            archivo.close()
        except Exception as e:
            print(f"no se pudo cerrar el archivo correctamente: {e}")


def mostrar_por_dia(ruta, tot,dia):
   try:
        archivo= open(ruta, "r", encoding="utf-8")
        facturas= json.load(archivo)
        
        for factura in facturas:

            
            if factura["dia"]==dia:

                print(f'ID FACTURA: {factura["id_factura"]} ID PACIENTE {factura["id_paciente"]} ID TURNO {factura["id_turno"]} DIA {factura["dia"]} HORA {factura["hora"]} IMPORTE {factura["importe"]}')
                print("")

              
        print("*" * 50)
        print(f"El total del dia {dia} es: {tot}")

   except:
        
        print("no se puede abrir")

   finally:
        try:
            archivo.close()
        except Exception as e:
            print(f"no se pudo cerrar el archivo correctamente: {e}")
   

def cierre_por_dia(ruta,dia):
    print(dia)
    total=0

    try:
        archivo= open(ruta, "r", encoding="utf-8")
        facturas= json.load(archivo)
        
        for factura in facturas:

            
            if factura["dia"]==dia:

                total=total+ factura["importe"]

        return total
        
    except:
        
        print("no se puede abrir")

    finally:
        try:
            archivo.close()
        except Exception as e:
            print(f"no se pudo cerrar el archivo correctamente: {e}")



def cierre_total(ruta):
    total=0
    try:
        archivo= open(ruta, "r", encoding="utf-8")
        facturas= json.load(archivo)
        
        for factura in facturas:
              total=total+ factura["importe"]

        return total
        
    except:
        
        print("no se puede abrir")

    finally:
        try:
            archivo.close()
        except Exception as e:
            print(f"no se pudo cerrar el archivo correctamente: {e}")


def main():
    valores_permitidos=[1,2,3]
   
    opcion=int(input("Ingrese 1 para ver el cierre de caja por dia, 2 para ver el cierre de caja total, 3 para salir"))

    if opcion in valores_permitidos:
           if opcion ==1:
            
            while True:
             try:
           
               num_dia=int(input("por favor ingrese un numero para ver las facturas de ese dia(lunes=1 miercoles=2, viernes=3)"))

               if num_dia in valores_permitidos:
                  break
               print("ingrese 1, 2 o 3 por favor")
             except ValueError:
               print("ingrese un numero por favor")
             except Exception as e:
               print(f"⚠️ Ocurrió un error inesperado: {e}")
        
    
    
            if num_dia==1:
               dia="lunes"
            elif num_dia==2:
               dia="miércoles"
            elif num_dia==3:
               dia="viernes"


            total_monto_por_dia=cierre_por_dia("db/facturacion.json",dia) 
            mostrar_por_dia("db/facturacion.json",total_monto_por_dia,dia)     

           elif opcion==2:
            
             total_monto=cierre_total("db/facturacion.json")
             mostrar_total("db/facturacion.json", total_monto)

           elif opcion==3:
               print("saliendo")
               
        
                       
    # print(f'ID FACTURA: {factura["id_factura"]} ID PACIENTE {factura["id_paciente"]} ID TURNO {factura["id_turno"]} DIA {factura["dia"]} HORA {factura["hora"]} IMPORTE {factura["importe"]}')
    #            print("")

main()
