def transformar(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return "Opción inválida"


while True:
    print("\n--- MENÚ ---")
    print("1. Convertir a MAYÚSCULAS")
    print("2. Convertir a minúsculas")
    print("3. Primera letra en mayúscula")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 4:
        print("Programa finalizado")
        break

    texto = input("Ingrese un texto: ")
    resultado = transformar(texto, opcion)
    print("Resultado:", resultado)