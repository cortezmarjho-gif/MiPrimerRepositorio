import random

secreto = random.randint(1, 10)
lista = []

num = int(input("Adivina un número del 1 al 10: "))

while num != secreto:

    lista.append(num)

    if num < secreto:
        print("El número es más grande")
    else:
        print("El número es más pequeño")

    num = int(input("Prueba otra vez: "))

lista.append(num)

print("Ganaste")

print("Intentos que hiciste:")

for i in range(len(lista)):
    print(lista[i])