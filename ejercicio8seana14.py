def buscar_producto(arreglo, producto):

    for p in arreglo:
        if p == producto:
            return "Producto encontrado"

    return "Producto no encontrado"


productos = []

for i in range(5):
    nombre = input("Ingrese un producto: ")
    productos.append(nombre)

buscar = input("Qué producto desea buscar: ")

print(buscar_producto(productos, buscar))