def transformar_palabra(palabra, opcion):
    if opcion == 1:
        print(palabra.upper())
    elif opcion == 2:
        print(palabra.lower())
    elif opcion == 3:
        print(palabra.capitalize())
    else:
        print("Opción inválida")


palabra = input("Ingrese una palabra: ")
print("Opciones: 1=Mayúsculas, 2=Minúsculas, 3=Primera letra mayúscula")
opcion = int(input("Elija una opción: "))
transformar_palabra(palabra, opcion)