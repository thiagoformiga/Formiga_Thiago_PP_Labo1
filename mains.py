from funciones import*
from menu import*

bandera_leer = False
bandera_ordenar = False

while True:
    mostrar_menu()
    respuesta = validar_respuesta_menu(7)
    match respuesta:
        case 1:
            lista = leer_json("data.json")
            lista_convertida = convertir_datos_numericos(lista)
            bandera_leer = True
        case 2:
            if bandera_leer == True:
                print(mostrar_columnas(lista_convertida))
            else:
                print("ERROR, PRIMERO CARGAR LA LISTA")
        case 3:
            if bandera_leer == True:
                asignar_servicio(lista_convertida)
                print(lista_convertida)
            else:
                print("ERROR, PRIMERO CARGAR LA LISTA")
        case 4:
            if bandera_leer == True:
                tipo = int(input("ingrese el tipo de servicio que busca(1-3)"))
                while tipo != 1 and tipo != 2 and tipo != 3:
                    tipo = int(input("ERROR, ingrese el tipo de servicio que busca(1-3)"))
                lista_servicios_tipos = filtrar_por(lista,"tipo",tipo)
                crear_json(lista_servicios_tipos,"tipos_servicio.json")
            else:
                print("ERROR, PRIMERO CARGAR LA LISTA")
        case 5:
            if bandera_leer == True:
                lista_ordenada = ordenar_porclave(lista_convertida,"descripcion","ascendente")
                print(mostrar_columnas(lista_ordenada))
                bandera_ordenar = True
            else:
                print("ERROR, PRIMERO CARGAR LA LISTA")
        case 6:
            if bandera_ordenar == True:
                crear_json(lista_ordenada,"tipos_servicio_ordenanos.json")
            else:
                print("ERROR, PRIMERO CARGAR LA LISTA")
        case 7:
            print("Saliendo del programa")
            break