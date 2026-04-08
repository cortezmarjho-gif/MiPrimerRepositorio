def transformar_multiple(texto, lista_opciones):
    resultado = texto

    for opcion in lista_opciones:
        if opcion == 1:
            resultado = resultado.upper()
        elif opcion == 2:
            resultado = resultado.lower()
        elif opcion == 3:
            resultado = resultado.capitalize()
        else:
            return "Opción inválida"

    return resultado


# Probar con el usuario
texto = input("Ingrese un texto: ")
entrada = input("Ingrese varias opciones separadas por coma (ej: 1,2,3): ")
lista_opciones = list(map(int, entrada.split(",")))
resultado = transformar_multiple(texto, lista_opciones)
print("Resultado final:", resultado)