#ejemplo diccionario de inventario

def guardar_inventario(diccionario, archivo):
    with open(archivo,"w+") as f:
        for producto, detalles in diccionario.items():
            Id, cantidad, precio = detalles
            f.write(f"Nombre: {producto}, Id: {Id}, Cantidad: {cantidad}, Precio: {precio}\n" )

inventario = {
    "producto1": ("001",3525,4843.43),
    "producto2": ("002",20,53),
    "producto3": ("003",80,100.99),
    "producto4": ("004",3,153.3),
    "producto5": ("005",100,633)
}


archivo = "files/inventario.txt"

guardar_inventario(inventario, archivo)
print("Inventario guardado")


