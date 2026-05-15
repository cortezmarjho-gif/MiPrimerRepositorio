nombre = input("Ingrese su nombre completo: ")

lista = nombre.split()

lista.reverse()

nuevo = ""

for palabra in lista:

    for letra in palabra:
        nuevo += letra

    nuevo += " "

print("Nombre transformado:", nuevo)