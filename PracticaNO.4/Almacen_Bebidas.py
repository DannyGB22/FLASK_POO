from controlador import AlmacenBebidas

almacen = AlmacenBebidas()

print("Hola Bienvenido al almacen de bebidas".center(100,'-'))

while True:
    print("\n----------Menu-----------------------------------------------------------")
    print("1. Agregar bebida")
    print("2. Eliminar bebida")
    print("3. Actualizar bebida")
    print("4. Mostrar todas las bebidas")
    print("5. Calcular precio promedio de las bebidas")
    print("6. Cantidad de bebidas por marca")
    print("7. Cantidad de bebidas por clasificación")
    print("8. Salir")
    

    seleccion = input('\nIngrese el numero de la seleccion que desea hacer: ')

    if seleccion == "1":
     almacen.DarAlta()
    elif seleccion == "2": 
        id = int(input("Ingrese el ID de la bebida que desea eliminar: "))
        almacen.DarBaja(id)
    elif seleccion == "3":
        id = int(input("Ingrese el ID de la bebida que desea actualizar: "))
        almacen.actualizar(id)
    elif seleccion == "4":
        almacen.Mostrar()
    elif seleccion == "5":
        almacen.PrecioPromedio()  
    elif seleccion == "6":
        marca = input("Ingrese la marca de bebidas que desea buscar: ")
        almacen.BebidaMarca(marca)
    elif seleccion == "7":
        clasificacion = input("Ingrese la clasificación de bebidas que desea buscar: ")
        almacen.Clasificacion(clasificacion)
    elif seleccion == "8":
        break
    else:
        print("Seleccion invalida, agregue un numero  valido del Menu.")
        
        


    