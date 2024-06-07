
def convertir_datos_numericos(lista):
    """
    descripcion : Convierte las claves numéricas a enteros o floats en una lista de diccionariod
    parametros: Lista de diccionarios representando a los héroes.
    retorno: la lista con las claves convertidas
    """
    for e_lista in lista:
        e_lista["id_servicio"] = int(e_lista["id_servicio"])
        e_lista["tipo"] = int(e_lista["tipo"])
        e_lista["precioUnitario"] = float(e_lista["precioUnitario"])
        e_lista["cantidad"] = int(e_lista["cantidad"])
        e_lista["totalServicio"] = int(e_lista["totalServicio"])
    return lista

def leer_json(ruta_archivo:str):
    import json
    """
    descripcion: intenta leer un archivo json devolviendo la lista de heroes si ocurre algun error devuelve un false y muestra el error
    parametros:recibe la ruta y la clave de la lista
    retorno:o un boool o la lista 
    """
    
    try:
        with open(ruta_archivo,"r") as archivo:
            datos = json.load(archivo)#leo los datos
            return datos
    except FileNotFoundError:
        print("El archivo no existe")
        return False
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return False
    

def mostrar_columnas(lista_dict,id_servicio=True,descripcion=True,tipo=True,precioUnitario=True,cantidad=True,totalServicio=True):
    """
    descripcion:esta funcion imprime en columnas los valored de una lista de diccionarios
    parametros:la lista y como parametros opcionales un true o false si no quiero pasar la clave
    retorna= un strin en manera de msj
    """
    
    msj = ""
    print("id_servicio||descripcion||tipo||precioUnitario||cantidad||totalServicio")
    for dict in lista_dict:
        if id_servicio: msj += str(dict["id_servicio"]) + "||"
        if descripcion: msj += str(dict["descripcion"]) + "||"
        if tipo: msj += str(dict["tipo"]) + "||"
        if precioUnitario: msj += str(dict["precioUnitario"]) + "||"
        if cantidad: msj += str(dict["cantidad"]) + "||"
        if totalServicio: msj += str(dict["totalServicio"])
        msj += "\n"
    return msj


def asignar_servicio(lista:list):
    """
    descripcion:esta funcion calcula la cantidad de un servicio y la asigna con clave valor a un diccionario
    parametros: la lista
    retorno:no retorna nada
    """
    calcular_total = lambda cantidad, precio_unitario: cantidad * precio_unitario
    for e_lista in lista:
        cantidad = e_lista["cantidad"]
        precio_unitario = e_lista["precioUnitario"]
        e_lista['totalServicio'] = calcular_total(cantidad,precio_unitario)
        (lambda x: x)



def filtrar_por(lista,clave,tipo_buscado):
    """
    descripcion:esta funcion filtra una lista de diccionarios por el tipo buscado
    parametros: recibe la lista, la clave y el tipo buscado
    retorno: retorna la lista filtrada
    """
    personajes_genero_bucado = list(filter(lambda personaje: personaje[clave] == tipo_buscado, lista))
    return personajes_genero_bucado

def crear_json(lista, nombre_archivo):
    """
    descripcion: crea un archivo json con la lista de dicccionarios que le paso
    parametros: lista, nombre que le dara al archivo
    retorno : no retorna nada
    """
    import json
    try:
        with open(nombre_archivo, 'w') as archivo:
            json.dump(lista, archivo, indent=4)
        print(f'Archivo {nombre_archivo} creado')
    except Exception as e:
        print(f"error al crear el archivo")



def ordenar_porclave(lista:list,clave:str,orden:str):
    """
    descripcion: ordena una lista por la clave recibida y por el ordena que desea el usuario
    parametros :Lista de diccionarios representando a los héroes, la clave que desea ordenar y el orden(ascendente,descendente)
    retorno Lista de héroes ordenadas por la clave
    """
    if lista is None or lista is False:
        print("No se pudo leer la lista de héroes.")
        return False
    
    elif lista:
        if orden == "ascendente":
            orden = False
        elif orden == "descendente":
            orden = True
        heroes_ordenados = sorted(lista, key=lambda x: x[clave], reverse=orden)
        print(f"heroes ordenados por {clave}")
        return heroes_ordenados
    else:
        return False
