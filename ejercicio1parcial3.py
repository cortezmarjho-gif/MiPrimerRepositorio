etiqueta = input("Ingrese la etiqueta de rastreo: ")

if etiqueta == "":
    print("Error, la etiqueta está vacía")

else:
    datos = etiqueta.split("-")

    print("Categoria:", datos[1])

    codigo = datos[0][:3]
    print("Codigo recortado:", codigo)

    mensaje = "Ruta Internacional" if datos[2] == "INT" else "Ruta Nacional"

    print(mensaje)