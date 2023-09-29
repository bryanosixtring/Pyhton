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

        #complementar el programa