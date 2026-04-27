suma = 0
lista = []

num = int(input("Pon un número (0 para salir): "))

while num != 0:

    if num % 2 != 0:
        suma = suma + num
        lista.append(num)

    num = int(input("Pon otro número (0 para salir): "))

print("Suma de impares:", suma)

print("Números impares:")

for i in range(len(lista)):
    print(lista[i])
