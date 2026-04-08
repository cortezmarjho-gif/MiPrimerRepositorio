def transformar_y_contar(texto, opcion):
    if opcion == 1:
        resultado = texto.upper()
    elif opcion == 2:
        resultado = texto.lower()
    elif opcion == 3:
        resultado = texto.capitalize()
    else:
        return "Opción inválida"

    return len(resultado)


# Probar con el usuario
texto = input("Ingrese un texto: ")
opcion = int(input("Ingrese una opción (1, 2 o 3): "))
resultado = transformar_y_contar(texto, opcion)
print("Cantidad de caracteres:", resultado)