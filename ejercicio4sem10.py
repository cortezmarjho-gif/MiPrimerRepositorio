def transformar_lista(lista, opcion):
    nueva_lista = []

    for palabra in lista:
        if opcion == 1:
            nueva_lista.append(palabra.upper())
        elif opcion == 2:
            nueva_lista.append(palabra.lower())
        elif opcion == 3:
            nueva_lista.append(palabra.capitalize())
        else:
            return "Opción inválida"

    return nueva_lista


# Ejemplo de uso
palabras = ["hola", "MUNDO", "python"]
print("Opciones: 1=Mayúsculas, 2=Minúsculas, 3=Primera letra mayúscula")
opcion = int(input("Elija una opción: "))
resultado = transformar_lista(palabras, opcion)
print("Resultado:", resultado)