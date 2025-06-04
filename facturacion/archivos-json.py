import json
ruta = "db/datos.json"

def abrir_archivo(ruta):
        """
        Abre un archivo y devuelve su contenido como un objeto JSON.
        
        :param ruta: Ruta del archivo a abrir.
        :return: Contenido del archivo como objeto JSON.
        """
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
        
def leer_archivo(ruta):
    """
    Lee el contenido de un archivo y lo devuelve como una cadena de texto.
    
    :param ruta: Ruta del archivo a leer.
    :return: Contenido del archivo como cadena de texto.
    """
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return archivo.read()
    
def escribir_archivo(ruta, contenido):

    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(contenido, archivo, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    contenido = leer_archivo(ruta)
    print(contenido)
