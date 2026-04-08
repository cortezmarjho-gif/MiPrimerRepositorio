def transformar_texto(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return "Opción inválida"


# Pedir datos al usuario
texto = input("Ingrese un texto: ")
print("Opciones: 1=Mayúsculas, 2=Minúsculas, 3=Primera letra mayúscula")
opcion = int(input("Elija una opción: "))
resultado = transformar_texto(texto, opcion)
print("Resultado:", resultado)