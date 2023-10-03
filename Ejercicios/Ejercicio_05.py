inventario = {} #diccionario

def agregar_producto(producto, cantidad):
    try:
        cantidad = int (cantidad)
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        if producto in inventario:
            inventario[producto] += cantidad
        else:
            inventario[producto] = cantidad
            print(F"Se agregaron {cantidad} unidades de {producto} al inventario")

    except ValueError as error:
        print("El error: ", str(error))

def eliminar_producto(producto, cantidad):
    try:
        cantidad = int (cantidad)
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        if producto in inventario:
            if inventario[producto] >= cantidad:
                inventario[producto] -= cantidad
                print(F"Se eliminaron {cantidad} unidades de {producto} del inventario.")
            else:
                print("No hay suficiente stock par eliminar esa cantidad")
        else:
            print("El producto no existe en el inventario")
    
    except ValueError as error:
        print("Error: ", str(error))

def verificar_stock(producto):
    try:
        if producto in inventario:
            print(F"Stock de {producto}: {inventario[producto]} unidades")
        else:
            print(F"El producto no existe en el inventario")
    
    except Exception as error:
        print("Error: ", str(error))


try:

    while True:
        print("\nMenú:")
        print("1. Agregar producto al inventario")
        print("2. Eliminar producto del inventario")
        print("3. Verificar stock de un producto")
        print("4. Verificar el inventario")
        print("5. Eliminar todo el inventario")
        print("6. Salir")
        opcion = input("Ingrese la opción que desea: ")

        if opcion == '1':
            producto = input("Ingrese el nombre del producto: ").lower()
            cantidad =  input("Ingrese la cantidad a agregar: ")
        
        elif opcion == '2':
            producto = input("Ingrese el nombre de producto: ").lower()
            cantidad = input("Ingrese la cantidad a eliminar: ")
            eliminar_producto(producto,cantidad)

        elif opcion == '4':
            for producto in inventario:
                print(F'Stock de {producto}: {inventario[producto]} unidades')
        
        elif opcion == '5':
            inventario.clear()
            if len(inventario)==0:
                print("El inventario se ha eliminado")

        elif opcion == '6':
            break
            
        else:
            print("Opción no válida")    

except KeyboardInterrupt:
    print("Saliendo del programa")