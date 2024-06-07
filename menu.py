def mostrar_menu():
    print("1. Cargar archivo: Se pedirá el nombre del archivo y se cargarán en una lista los elementos del mismo.\n2.Imprimir lista: Se imprimirá por pantalla la tabla (en forma de columnas) con los datos de los servicios.\n3. Asignar totales: Se deberá hacer uso de una función lambda que asignará a cada servicio el total calculado (totalServicio) de la siguiente forma: cantidad x precioUnitario.\n4.Filtrar por tipo: Se deberá generar un archivo igual al original, pero donde solo aparezcan servicios del tipo seleccionado\n5.Mostrar servicios: Se deberá mostrar por pantalla un listado de los servicios ordenados por descripción de manera ascendente.\n6.Guardar servicios: Se deberá guardar el listado del punto anterior en un archivo de tipo json\n7.Salir.")

def validar_respuesta_menu(hasta:int):
    while True:
        respuesta = input("RESPUESTA:")
        if respuesta.isdigit():
            respuesta = int(respuesta)
            if 1 <= respuesta <= hasta:
                return respuesta
            else:
                print(f"Error, la respuesta debe estar entre (1-{hasta})")
        else:
            print("error, Que su respuesta sea un numero")
